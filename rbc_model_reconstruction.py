#!/usr/bin/env python3
"""
rbc_model_reconstruction.py

Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.

Uses the model to predict curvature/energy values for each vertex
in the original RBC mesh from OpenRBC.

The visualization shows the ACTUAL RBC mesh colored by model predictions.
"""

import argparse
import json
import os
import sys

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from willmore_crsital2 import (
    Config,
    MinimalSurfaceSpectralNetwork,
    MinimalSurfaceOperator,
    SeedManager,
)


def load_rbc_mesh(vert_path: str, face_path: str):
    """Load RBC mesh from OpenRBC files."""
    vertices = []
    with open(vert_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                vertices.append([float(parts[0]), float(parts[1]), float(parts[2])])
    vertices = np.array(vertices, dtype=np.float64)

    faces = []
    with open(face_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                i0, i1, i2 = int(parts[0]), int(parts[1]), int(parts[2])
                if i0 >= 0 and i1 >= 0 and i2 >= 0:
                    faces.append([i0, i1, i2])
    faces = np.array(faces, dtype=np.int64)

    return vertices, faces


def compute_vertex_normals(vertices: np.ndarray, faces: np.ndarray) -> np.ndarray:
    """Compute vertex normals."""
    v0 = vertices[faces[:, 0]]
    v1 = vertices[faces[:, 1]]
    v2 = vertices[faces[:, 2]]

    face_normals = np.cross(v1 - v0, v2 - v0)
    face_norms = np.linalg.norm(face_normals, axis=1, keepdims=True)
    face_norms = np.maximum(face_norms, 1e-10)
    face_normals = face_normals / face_norms

    vertex_normals = np.zeros_like(vertices)
    for i, face in enumerate(faces):
        for v_idx in face:
            vertex_normals[v_idx] += face_normals[i]

    norms = np.linalg.norm(vertex_normals, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-10)
    return vertex_normals / norms


def compute_face_areas(vertices: np.ndarray, faces: np.ndarray) -> np.ndarray:
    """Compute face areas."""
    v0 = vertices[faces[:, 0]]
    v1 = vertices[faces[:, 1]]
    v2 = vertices[faces[:, 2]]
    cross = np.cross(v1 - v0, v2 - v0)
    return 0.5 * np.linalg.norm(cross, axis=1)


def load_model(checkpoint_path: str, device: str, config: Config):
    """Load the trained Willmore model from checkpoint."""
    print(f"Loading model from: {checkpoint_path}")

    model = MinimalSurfaceSpectralNetwork(
        grid_size=config.GRID_SIZE,
        hidden_dim=config.HIDDEN_DIM,
        expansion_dim=config.EXPANSION_DIM,
        num_spectral_layers=config.NUM_SPECTRAL_LAYERS,
        input_channels=config.SURFACE_CHANNELS,
        output_channels=config.SURFACE_CHANNELS
    ).to(device)

    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)

    if isinstance(checkpoint, dict):
        if 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'])
        elif 'state_dict' in checkpoint:
            model.load_state_dict(checkpoint['state_dict'])
        else:
            model.load_state_dict(checkpoint)

        if 'epoch' in checkpoint:
            print(f"Checkpoint epoch: {checkpoint['epoch']}")
        if 'score' in checkpoint:
            print(f"Checkpoint score: {checkpoint['score']:.6f}")
        if 'alpha' in checkpoint:
            print(f"Checkpoint alpha: {checkpoint['alpha']:.6f}")
    else:
        model.load_state_dict(checkpoint)

    model.eval()

    for param in model.parameters():
        param.requires_grad = False

    return model


def create_local_patches_for_vertices(
    vertices: np.ndarray,
    faces: np.ndarray,
    normals: np.ndarray,
    grid_size: int
):
    """
    Create local surface patches around each vertex for model input.
    
    For each vertex, we create a small 2D grid representing the local
    surface neighborhood, which can be processed by the model.
    """
    n_vertices = len(vertices)
    
    neighbor_rings = {i: set() for i in range(n_vertices)}
    for face in faces:
        for i in range(3):
            neighbor_rings[face[i]].add(face[(i+1)%3])
            neighbor_rings[face[i]].add(face[(i+2)%3])
    
    for i in range(n_vertices):
        first_ring = neighbor_rings[i].copy()
        for j in first_ring:
            neighbor_rings[i].update(neighbor_rings[j])
        neighbor_rings[i].discard(i)
    
    patches_real = np.zeros((n_vertices, grid_size, grid_size), dtype=np.float32)
    patches_imag = np.zeros((n_vertices, grid_size, grid_size), dtype=np.float32)
    
    for i in range(n_vertices):
        vi = vertices[i]
        ni = normals[i]
        
        tangent1 = np.array([1.0, 0.0, 0.0])
        if abs(np.dot(ni, tangent1)) > 0.9:
            tangent1 = np.array([0.0, 1.0, 0.0])
        tangent1 = tangent1 - np.dot(tangent1, ni) * ni
        tangent1 = tangent1 / (np.linalg.norm(tangent1) + 1e-10)
        tangent2 = np.cross(ni, tangent1)
        
        neighbors = list(neighbor_rings[i])
        if len(neighbors) == 0:
            continue
            
        neighbor_verts = vertices[neighbors]
        local_coords = neighbor_verts - vi
        
        local_2d = np.stack([
            np.dot(local_coords, tangent1),
            np.dot(local_coords, tangent2)
        ], axis=1)
        
        heights = np.dot(local_coords, ni)
        
        x_range = max(np.abs(local_2d[:, 0]).max(), 0.5)
        y_range = max(np.abs(local_2d[:, 1]).max(), 0.5)
        
        x_bins = np.linspace(-x_range, x_range, grid_size)
        y_bins = np.linspace(-y_range, y_range, grid_size)
        
        height_grid = np.zeros((grid_size, grid_size))
        count_grid = np.zeros((grid_size, grid_size))
        
        for j, (xy, h) in enumerate(zip(local_2d, heights)):
            xi = np.argmin(np.abs(x_bins - xy[0]))
            yi = np.argmin(np.abs(y_bins - xy[1]))
            height_grid[xi, yi] += h
            count_grid[xi, yi] += 1
        
        mask = count_grid > 0
        height_grid[mask] /= count_grid[mask]
        height_grid[~mask] = 0.0
        
        h_std = np.std(np.abs(heights)) + 1e-10
        patches_real[i] = height_grid / h_std
        
        theta = np.arctan2(local_2d[:, 1], local_2d[:, 0])
        phase_grid = np.zeros((grid_size, grid_size))
        for j, (xy, th) in enumerate(zip(local_2d, theta)):
            xi = np.argmin(np.abs(x_bins - xy[0]))
            yi = np.argmin(np.abs(y_bins - xy[1]))
            phase_grid[xi, yi] += th
        
        mask = count_grid > 0
        if mask.any():
            phase_grid[mask] /= count_grid[mask]
        patches_imag[i] = np.sin(phase_grid)
    
    return patches_real, patches_imag


def run_model_on_patches(model, patches_real: np.ndarray, patches_imag: np.ndarray, device: str, grid_size: int, batch_size: int = 256):
    """
    Run the model on all vertex patches and extract predictions.
    
    Returns predicted curvature-like values for each vertex.
    """
    n_vertices = patches_real.shape[0]
    
    predicted_curvatures = np.zeros(n_vertices, dtype=np.float32)
    predicted_energies = np.zeros(n_vertices, dtype=np.float32)
    
    for start in range(0, n_vertices, batch_size):
        end = min(start + batch_size, n_vertices)
        
        batch_real = torch.tensor(patches_real[start:end], dtype=torch.float32, device=device)
        batch_imag = torch.tensor(patches_imag[start:end], dtype=torch.float32, device=device)
        
        batch_input = torch.stack([batch_real, batch_imag], dim=1)
        
        with torch.no_grad():
            output = model(batch_input)
        
        output_real = output[:, 0].cpu().numpy()
        output_imag = output[:, 1].cpu().numpy()
        
        for i, idx in enumerate(range(start, end)):
            laplacian_magnitude = np.sqrt(
                np.sum(output_real[i]**2) + np.sum(output_imag[i]**2)
            )
            predicted_curvatures[idx] = laplacian_magnitude
            
            center_val = output_real[i, grid_size//2, grid_size//2]
            predicted_energies[idx] = center_val**2
    
    return predicted_curvatures, predicted_energies


def compute_analytical_curvature(vertices: np.ndarray, faces: np.ndarray):
    """Compute analytical mean curvature for comparison."""
    n = len(vertices)
    
    neighbor_rings = {i: set() for i in range(n)}
    for face in faces:
        for i in range(3):
            neighbor_rings[face[i]].add(face[(i+1)%3])
            neighbor_rings[face[i]].add(face[(i+2)%3])
    
    mixed_areas = np.zeros(n)
    for face in faces:
        v0, v1, v2 = vertices[face[0]], vertices[face[1]], vertices[face[2]]
        area = 0.5 * np.linalg.norm(np.cross(v1 - v0, v2 - v0))
        for idx in face:
            mixed_areas[idx] += area / 3
    
    mean_curvature = np.zeros(n)
    for i in range(n):
        neighbors = list(neighbor_rings[i])
        if len(neighbors) == 0 or mixed_areas[i] < 1e-10:
            continue
        
        laplacian = np.zeros(3)
        for j in neighbors:
            laplacian += vertices[j] - vertices[i]
        
        mean_curvature[i] = np.linalg.norm(laplacian) / (2.0 * mixed_areas[i])
    
    return mean_curvature


def save_ply_with_values(vertices, faces, normals, values, filepath: str, value_name: str = "curvature"):
    """Save mesh as PLY with scalar values as vertex colors."""
    v_min, v_max = values.min(), values.max()
    v_range = v_max - v_min if v_max > v_min else 1.0
    normalized = (values - v_min) / v_range
    
    with open(filepath, 'w') as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write(f"element vertex {len(vertices)}\n")
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("property float nx\n")
        f.write("property float ny\n")
        f.write("property float nz\n")
        f.write("property uchar red\n")
        f.write("property uchar green\n")
        f.write("property uchar blue\n")
        f.write(f"element face {len(faces)}\n")
        f.write("property list uchar int vertex_indices\n")
        f.write("end_header\n")
        
        for i, v in enumerate(vertices):
            n = normals[i]
            val = normalized[i]
            r = int(255 * val)
            b = int(255 * (1 - val))
            g = int(128)
            f.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f} {n[0]:.6f} {n[1]:.6f} {n[2]:.6f} {r} {g} {b}\n")
        
        for face in faces:
            f.write(f"3 {face[0]} {face[1]} {face[2]}\n")


def save_html_viewer(
    vertices, faces, normals,
    model_curvature, analytical_curvature,
    output_path: str
):
    """Create interactive HTML viewer with model predictions on actual RBC mesh."""
    
    verts_json = vertices.tolist()
    faces_json = faces.tolist()
    normals_json = normals.tolist()
    model_curv_json = model_curvature.tolist()
    analytical_curv_json = analytical_curvature.tolist()
    
    mc_min, mc_max = float(model_curvature.min()), float(model_curvature.max())
    ac_min, ac_max = float(analytical_curvature.min()), float(analytical_curvature.max())
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>RBC Model Predictions - Actual Mesh Data</title>
    <style>
        body {{ margin: 0; background: #000; font-family: monospace; }}
        .container {{ display: flex; width: 100vw; height: 100vh; }}
        .panel {{ flex: 1; position: relative; border-right: 1px solid #333; }}
        .panel:last-child {{ border-right: none; }}
        canvas {{ display: block; }}
        .label {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: #fff;
            background: rgba(0,0,0,0.8);
            padding: 15px;
            border-radius: 5px;
            z-index: 100;
        }}
        .info {{
            position: absolute;
            bottom: 10px;
            left: 10px;
            color: #0f0;
            background: rgba(0,0,0,0.8);
            padding: 10px;
            border-radius: 5px;
            font-size: 11px;
            max-width: 250px;
        }}
        .legend {{
            position: absolute;
            bottom: 10px;
            right: 10px;
            color: #fff;
            background: rgba(0,0,0,0.8);
            padding: 10px;
            border-radius: 5px;
            font-size: 11px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="panel" id="panel1">
            <div class="label">MODEL PREDICTION<br>(Willmore Network)</div>
            <div class="info" id="info1">Loading...</div>
            <div class="legend">
                <b>Model Curvature</b><br>
                Low: <span style="color:#0066ff">Blue</span><br>
                High: <span style="color:#ff0000">Red</span>
            </div>
        </div>
        <div class="panel" id="panel2">
            <div class="label">ANALYTICAL CURVATURE<br>(Discrete Geometry)</div>
            <div class="info" id="info2">Loading...</div>
            <div class="legend">
                <b>Analytical Curvature</b><br>
                Low: <span style="color:#0066ff">Blue</span><br>
                High: <span style="color:#ff0000">Red</span>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        const vertices = {json.dumps(verts_json)};
        const faces = {json.dumps(faces_json)};
        const normals = {json.dumps(normals_json)};
        const modelCurv = {json.dumps(model_curv_json)};
        const analyticalCurv = {json.dumps(analytical_curv_json)};
        
        const mcMin = {mc_min};
        const mcMax = {mc_max};
        const mcRange = mcMax - mcMin > 0 ? mcMax - mcMin : 1;
        
        const acMin = {ac_min};
        const acMax = {ac_max};
        const acRange = acMax - acMin > 0 ? acMax - acMin : 1;

        function createScene(containerId, curvatureValues, cMin, cRange, label, infoId) {{
            const container = document.getElementById(containerId);
            const width = container.clientWidth;
            const height = container.clientHeight;

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(width, height);
            renderer.setClearColor(0x111111);
            container.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);

            const geometry = new THREE.BufferGeometry();
            const positions = [];
            const colors = [];
            const normalData = [];

            for (const face of faces) {{
                for (const vi of face) {{
                    const v = vertices[vi];
                    positions.push(v[0], v[1], v[2]);
                    
                    const n = normals[vi];
                    normalData.push(n[0], n[1], n[2]);

                    const cNorm = (curvatureValues[vi] - cMin) / cRange;
                    const r = cNorm;
                    const b = 1 - cNorm;
                    const g = 0.3;
                    colors.push(r, g, b);
                }}
            }}

            geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
            geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
            geometry.setAttribute('normal', new THREE.Float32BufferAttribute(normalData, 3));

            const material = new THREE.MeshPhongMaterial({{
                vertexColors: true,
                side: THREE.DoubleSide,
                shininess: 50
            }});

            const mesh = new THREE.Mesh(geometry, material);
            scene.add(mesh);

            const ambient = new THREE.AmbientLight(0x404040, 0.5);
            scene.add(ambient);

            const light1 = new THREE.DirectionalLight(0xffffff, 0.8);
            light1.position.set(5, 5, 5);
            scene.add(light1);

            const light2 = new THREE.DirectionalLight(0xffffff, 0.4);
            light2.position.set(-5, -5, -5);
            scene.add(light2);

            const center = new THREE.Vector3();
            geometry.computeBoundingBox();
            geometry.boundingBox.getCenter(center);
            controls.target.copy(center);

            const size = new THREE.Vector3();
            geometry.boundingBox.getSize(size);
            const maxDim = Math.max(size.x, size.y, size.z);
            camera.position.set(center.x + maxDim * 2, center.y + maxDim, center.z + maxDim * 2);

            controls.update();

            const cValues = curvatureValues;
            const mean = cValues.reduce((a,b)=>a+b,0)/cValues.length;
            const std = Math.sqrt(cValues.reduce((a,b)=>a+(b-mean)**2,0)/cValues.length);

            const info = document.getElementById(infoId);
            info.innerHTML = `
                Vertices: ${{vertices.length}}<br>
                Faces: ${{faces.length}}<br>
                Curvature range:<br>
                &nbsp;&nbsp;[${{cMin.toFixed(4)}}, ${{(cMin+cRange).toFixed(4)}}]<br>
                Mean: ${{mean.toFixed(4)}}<br>
                Std: ${{std.toFixed(4)}}
            `;

            function animate() {{
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
            }}

            window.addEventListener('resize', () => {{
                const w = container.clientWidth;
                const h = container.clientHeight;
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
                renderer.setSize(w, h);
            }});

            animate();
        }}

        createScene('panel1', modelCurv, mcMin, mcRange, 'Model', 'info1');
        createScene('panel2', analyticalCurv, acMin, acRange, 'Analytical', 'info2');
    </script>
</body>
</html>'''

    with open(output_path, 'w') as f:
        f.write(html)


def main():
    parser = argparse.ArgumentParser(description="RBC Reconstruction using Trained Willmore Model")
    parser.add_argument("--checkpoint", required=True, help="Path to trained model checkpoint")
    parser.add_argument("--vert", default="rbc.vert.txt", help="RBC vertex file")
    parser.add_argument("--face", default="rbc.face.txt", help="RBC face file")
    parser.add_argument("--output-dir", default="rbc_model_output", help="Output directory")
    parser.add_argument("--device", default="cpu", help="Device (cpu/cuda)")
    parser.add_argument("--batch-size", type=int, default=256, help="Batch size for inference")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    print("=" * 60)
    print("RBC RECONSTRUCTION USING TRAINED WILLMORE MODEL")
    print("Using ACTUAL mesh data from OpenRBC")
    print("=" * 60)

    config = Config()
    grid_size = config.GRID_SIZE

    print("\n[1] Loading trained model...")
    model = load_model(args.checkpoint, args.device, config)
    print(f"Model grid size: {grid_size}")

    print("\n[2] Loading RBC mesh from OpenRBC...")
    vertices, faces = load_rbc_mesh(args.vert, args.face)
    print(f"Loaded: {len(vertices)} vertices, {len(faces)} faces")

    print("\n[3] Computing vertex normals...")
    normals = compute_vertex_normals(vertices, faces)
    print(f"Normals computed for {len(normals)} vertices")

    print("\n[4] Creating local surface patches for each vertex...")
    patches_real, patches_imag = create_local_patches_for_vertices(
        vertices, faces, normals, grid_size
    )
    print(f"Patch shape: {patches_real.shape}")

    print("\n[5] Running model inference on all vertices...")
    model_curvature, model_energy = run_model_on_patches(
        model, patches_real, patches_imag, args.device, grid_size, args.batch_size
    )
    print(f"Model curvature range: [{model_curvature.min():.4f}, {model_curvature.max():.4f}]")
    print(f"Model energy range: [{model_energy.min():.4f}, {model_energy.max():.4f}]")

    print("\n[6] Computing analytical curvature for comparison...")
    analytical_curvature = compute_analytical_curvature(vertices, faces)
    print(f"Analytical curvature range: [{analytical_curvature.min():.4f}, {analytical_curvature.max():.4f}]")

    print("\n[7] Computing correlation between model and analytical...")
    correlation = np.corrcoef(model_curvature, analytical_curvature)[0, 1]
    print(f"Correlation: {correlation:.4f}")

    print("\n[8] Saving outputs...")

    save_ply_with_values(
        vertices, faces, normals, model_curvature,
        os.path.join(args.output_dir, "rbc_model_curvature.ply"),
        "model_curvature"
    )
    print("Saved: rbc_model_curvature.ply")

    save_ply_with_values(
        vertices, faces, normals, analytical_curvature,
        os.path.join(args.output_dir, "rbc_analytical_curvature.ply"),
        "analytical_curvature"
    )
    print("Saved: rbc_analytical_curvature.ply")

    save_html_viewer(
        vertices, faces, normals,
        model_curvature, analytical_curvature,
        os.path.join(args.output_dir, "rbc_model_viewer.html")
    )
    print("Saved: rbc_model_viewer.html")

    results = {
        "num_vertices": len(vertices),
        "num_faces": len(faces),
        "model_curvature_min": float(model_curvature.min()),
        "model_curvature_max": float(model_curvature.max()),
        "model_curvature_mean": float(model_curvature.mean()),
        "model_curvature_std": float(model_curvature.std()),
        "analytical_curvature_min": float(analytical_curvature.min()),
        "analytical_curvature_max": float(analytical_curvature.max()),
        "analytical_curvature_mean": float(analytical_curvature.mean()),
        "analytical_curvature_std": float(analytical_curvature.std()),
        "correlation_model_analytical": float(correlation),
        "grid_size": grid_size,
        "checkpoint": args.checkpoint
    }

    with open(os.path.join(args.output_dir, "results.json"), 'w') as f:
        json.dump(results, f, indent=2)
    print("Saved: results.json")

    print("\n" + "=" * 60)
    print("DONE - Open rbc_model_viewer.html to see 3D visualization")
    print("=" * 60)

    print("\nSUMMARY:")
    print(f"  Vertices:        {len(vertices)} (from OpenRBC data)")
    print(f"  Faces:           {len(faces)} (from OpenRBC data)")
    print(f"  Model curvature: [{model_curvature.min():.4f}, {model_curvature.max():.4f}]")
    print(f"  Analytical curv: [{analytical_curvature.min():.4f}, {analytical_curvature.max():.4f}]")
    print(f"  Correlation:     {correlation:.4f}")
    
    print("\nINTERPRETATION:")
    if correlation > 0.5:
        print("  Model predictions CORRELATE with analytical curvature.")
        print("  The Willmore model has learned meaningful curvature patterns.")
    else:
        print("  Low correlation - model may need different input representation.")


if __name__ == "__main__":
    main()
