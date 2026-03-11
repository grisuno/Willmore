#!/usr/bin/env python3
"""
rbc_model_reconstruction.py

Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.

The model processes 16x16 grids. We project the ENTIRE RBC mesh onto
a single 16x16 spherical parametrization and run inference.

This shows what the model "sees" when given the RBC shape.
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
        if 'delta' in checkpoint:
            print(f"Checkpoint delta: {checkpoint['delta']:.6f}")
    else:
        model.load_state_dict(checkpoint)

    model.eval()
    for param in model.parameters():
        param.requires_grad = False

    return model


def project_rbc_to_spherical_grid(vertices: np.ndarray, grid_size: int):
    """
    Project entire RBC mesh onto a spherical coordinate grid.
    
    This creates a single grid_size x grid_size representation
    that the model can process.
    """
    centered = vertices - vertices.mean(axis=0)
    
    x, y, z = centered[:, 0], centered[:, 1], centered[:, 2]
    r = np.sqrt(x**2 + y**2 + z**2) + 1e-10
    
    theta = np.arccos(np.clip(z / r, -1, 1))
    phi = np.arctan2(y, x)
    
    theta_bins = np.linspace(0, np.pi, grid_size)
    phi_bins = np.linspace(-np.pi, np.pi, grid_size)
    
    r_grid = np.zeros((grid_size, grid_size))
    count_grid = np.zeros((grid_size, grid_size))
    
    for i in range(len(vertices)):
        ti = np.argmin(np.abs(theta_bins - theta[i]))
        pi = np.argmin(np.abs(phi_bins - phi[i]))
        
        r_grid[ti, pi] += r[i]
        count_grid[ti, pi] += 1
    
    mask = count_grid > 0
    r_grid[mask] = r_grid[mask] / count_grid[mask]
    
    r_mean = r.mean()
    r_grid[~mask] = r_mean
    
    r_normalized = r_grid / r_mean
    
    theta_grid, phi_grid = np.meshgrid(theta_bins, phi_bins, indexing='ij')
    phase_grid = np.sin(theta_grid) * np.cos(phi_grid)
    
    real_part = r_normalized.astype(np.float32)
    imag_part = phase_grid.astype(np.float32)
    
    return real_part, imag_part, r_grid, mask


def spherical_grid_to_cartesian(r_grid: np.ndarray, grid_size: int, scale: float = 1.0):
    """Convert spherical grid back to 3D vertices."""
    theta = np.linspace(0, np.pi, grid_size)
    phi = np.linspace(-np.pi, np.pi, grid_size)
    THETA, PHI = np.meshgrid(theta, phi, indexing='ij')
    
    r_scaled = r_grid * scale
    
    x = r_scaled * np.sin(THETA) * np.cos(PHI)
    y = r_scaled * np.sin(THETA) * np.sin(PHI)
    z = r_scaled * np.cos(THETA)
    
    vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)
    
    faces = []
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            idx = i * grid_size + j
            faces.append([idx, idx + 1, idx + grid_size])
            faces.append([idx + 1, idx + grid_size + 1, idx + grid_size])
    faces = np.array(faces, dtype=np.int64)
    
    return vertices, faces


def run_model_evolution(model, input_grid: np.ndarray, steps: int, device: str):
    """
    Run model iteratively to evolve the surface.
    
    Returns the evolution trajectory.
    """
    real_part = input_grid.copy()
    imag_part = np.zeros_like(real_part)
    
    trajectory = [real_part.copy()]
    energy_history = []
    
    for step in range(steps):
        input_tensor = torch.tensor(
            np.stack([real_part, imag_part]),
            dtype=torch.float32,
            device=device
        ).unsqueeze(0)
        
        with torch.no_grad():
            output = model(input_tensor)
        
        output_np = output.squeeze(0).cpu().numpy()
        
        delta_real = output_np[0] - real_part
        real_part = real_part + 0.1 * delta_real
        
        trajectory.append(real_part.copy())
        
        energy = np.sum(real_part**2)
        energy_history.append(energy)
        
        if step % 20 == 0:
            print(f"  Step {step}: energy = {energy:.6f}")
    
    return trajectory, energy_history


def create_sphere_grid(grid_size: int, radius: float = 1.0):
    """Create a perfect sphere grid for comparison."""
    theta = np.linspace(0, np.pi, grid_size)
    phi = np.linspace(-np.pi, np.pi, grid_size)
    THETA, PHI = np.meshgrid(theta, phi, indexing='ij')
    
    r_grid = np.ones((grid_size, grid_size)) * radius
    return r_grid


def create_biconcave_grid(grid_size: int, radius: float = 1.0):
    """Create a biconcave disc shape on spherical grid."""
    theta = np.linspace(0, np.pi, grid_size)
    phi = np.linspace(-np.pi, np.pi, grid_size)
    THETA, PHI = np.meshgrid(theta, phi, indexing='ij')
    
    shape_factor = 1.0 - 0.6 * np.sin(THETA)**2
    r_grid = radius * shape_factor
    
    return r_grid


def compute_willmore_on_grid(surface: np.ndarray, grid_size: int):
    """Compute Willmore energy using MinimalSurfaceOperator."""
    surface_op = MinimalSurfaceOperator(grid_size)
    surface_tensor = torch.tensor(surface, dtype=torch.float32)
    return float(surface_op.compute_willmore_energy(surface_tensor).item())


def save_obj(vertices, faces, filepath: str):
    """Save mesh as OBJ file."""
    with open(filepath, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")


def save_html_comparison(
    original_vertices, original_faces,
    rbc_grid_vertices, rbc_grid_faces,
    evolved_vertices, evolved_faces,
    sphere_vertices, sphere_faces,
    biconcave_vertices, biconcave_faces,
    willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave,
    output_path: str
):
    """Create interactive HTML comparing all shapes."""
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>RBC Willmore Model Analysis</title>
    <style>
        body {{ margin: 0; background: #000; font-family: monospace; }}
        .container {{ display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; width: 100vw; height: 100vh; }}
        .panel {{ position: relative; border: 1px solid #333; }}
        canvas {{ display: block; }}
        .label {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: #fff;
            background: rgba(0,0,0,0.8);
            padding: 10px;
            border-radius: 5px;
            z-index: 100;
            font-size: 12px;
        }}
        .info {{
            position: absolute;
            bottom: 10px;
            left: 10px;
            color: #0f0;
            background: rgba(0,0,0,0.8);
            padding: 8px;
            border-radius: 5px;
            font-size: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="panel" id="panel1">
            <div class="label">ORIGINAL RBC<br>({len(original_vertices)} vertices)</div>
            <div class="info">From OpenRBC data</div>
        </div>
        <div class="panel" id="panel2">
            <div class="label">RBC ON 16x16 GRID<br>({len(rbc_grid_vertices)} vertices)</div>
            <div class="info">Willmore: {willmore_rbc:.4f}</div>
        </div>
        <div class="panel" id="panel3">
            <div class="label">MODEL EVOLUTION<br>({len(evolved_vertices)} vertices)</div>
            <div class="info">Willmore: {willmore_evolved:.4f}</div>
        </div>
        <div class="panel" id="panel4">
            <div class="label">COMPARISON SHAPES</div>
            <div class="info">Sphere: {willmore_sphere:.4f} | Biconcave: {willmore_biconcave:.4f}</div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        const panelData = [
            {{ id: 'panel1', vertices: {json.dumps(original_vertices.tolist())}, faces: {json.dumps(original_faces.tolist())}, color: 0xcc4444 }},
            {{ id: 'panel2', vertices: {json.dumps(rbc_grid_vertices.tolist())}, faces: {json.dumps(rbc_grid_faces.tolist())}, color: 0x44cc44 }},
            {{ id: 'panel3', vertices: {json.dumps(evolved_vertices.tolist())}, faces: {json.dumps(evolved_faces.tolist())}, color: 0x4444cc }},
            {{ id: 'panel4', vertices: {json.dumps(biconcave_vertices.tolist())}, faces: {json.dumps(biconcave_faces.tolist())}, color: 0xcccc44 }}
        ];

        panelData.forEach(data => {{
            const container = document.getElementById(data.id);
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

            for (const face of data.faces) {{
                for (const vi of face) {{
                    const v = data.vertices[vi];
                    positions.push(v[0], v[1], v[2]);
                }}
            }}

            geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
            geometry.computeVertexNormals();

            const material = new THREE.MeshPhongMaterial({{
                color: data.color,
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

            const center = new THREE.Vector3();
            geometry.computeBoundingBox();
            geometry.boundingBox.getCenter(center);
            controls.target.copy(center);

            const size = new THREE.Vector3();
            geometry.boundingBox.getSize(size);
            const maxDim = Math.max(size.x, size.y, size.z);
            camera.position.set(center.x + maxDim * 2, center.y + maxDim, center.z + maxDim * 2);

            controls.update();

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
        }});
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
    parser.add_argument("--evolve-steps", type=int, default=100, help="Evolution steps")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    print("=" * 60)
    print("RBC RECONSTRUCTION USING TRAINED WILLMORE MODEL")
    print("Model processes 16x16 grids - projecting RBC accordingly")
    print("=" * 60)

    config = Config()
    grid_size = config.GRID_SIZE

    print("\n[1] Loading trained model...")
    model = load_model(args.checkpoint, args.device, config)
    print(f"Model grid size: {grid_size}")

    print("\n[2] Loading RBC mesh from OpenRBC...")
    vertices, faces = load_rbc_mesh(args.vert, args.face)
    print(f"Loaded: {len(vertices)} vertices, {len(faces)} faces")

    print("\n[3] Projecting ENTIRE RBC to 16x16 spherical grid...")
    real_part, imag_part, r_grid, mask = project_rbc_to_spherical_grid(vertices, grid_size)
    print(f"Grid shape: {real_part.shape}")
    print(f"Grid range: [{real_part.min():.4f}, {real_part.max():.4f}]")
    print(f"Valid cells: {mask.sum()}/{grid_size*grid_size}")

    print("\n[4] Computing Willmore energy on projected grid...")
    willmore_rbc = compute_willmore_on_grid(real_part, grid_size)
    print(f"RBC projected Willmore: {willmore_rbc:.6f}")

    print("\n[5] Running model inference on RBC grid...")
    input_tensor = torch.tensor(
        np.stack([real_part, imag_part]),
        dtype=torch.float32,
        device=args.device
    ).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
    
    output_np = output.squeeze(0).cpu().numpy()
    print(f"Model output range: [{output_np[0].min():.4f}, {output_np[0].max():.4f}]")

    print(f"\n[6] Evolving surface for {args.evolve_steps} steps...")
    trajectory, energy_history = run_model_evolution(
        model, real_part, args.evolve_steps, args.device
    )
    
    evolved_grid = trajectory[-1]
    willmore_evolved = compute_willmore_on_grid(evolved_grid, grid_size)
    print(f"Evolved Willmore: {willmore_evolved:.6f}")

    print("\n[7] Creating comparison shapes...")
    
    sphere_grid = create_sphere_grid(grid_size, radius=real_part.mean())
    willmore_sphere = compute_willmore_on_grid(sphere_grid, grid_size)
    
    biconcave_grid = create_biconcave_grid(grid_size, radius=real_part.mean())
    willmore_biconcave = compute_willmore_on_grid(biconcave_grid, grid_size)
    
    print(f"Sphere Willmore: {willmore_sphere:.6f}")
    print(f"Biconcave Willmore: {willmore_biconcave:.6f}")

    print("\n[8] Converting grids to 3D meshes...")
    r_scale = np.linalg.norm(vertices, axis=1).mean()
    
    rbc_grid_vertices, rbc_grid_faces = spherical_grid_to_cartesian(real_part, grid_size, r_scale)
    evolved_vertices, evolved_faces = spherical_grid_to_cartesian(evolved_grid, grid_size, r_scale)
    sphere_vertices, sphere_faces = spherical_grid_to_cartesian(sphere_grid, grid_size, r_scale)
    biconcave_vertices, biconcave_faces = spherical_grid_to_cartesian(biconcave_grid, grid_size, r_scale)

    print("\n[9] Saving outputs...")
    
    save_obj(vertices, faces, os.path.join(args.output_dir, "rbc_original.obj"))
    save_obj(rbc_grid_vertices, rbc_grid_faces, os.path.join(args.output_dir, "rbc_projected.obj"))
    save_obj(evolved_vertices, evolved_faces, os.path.join(args.output_dir, "rbc_evolved.obj"))
    save_obj(biconcave_vertices, biconcave_faces, os.path.join(args.output_dir, "biconcave_reference.obj"))
    
    print("Saved: rbc_original.obj, rbc_projected.obj, rbc_evolved.obj, biconcave_reference.obj")

    save_html_comparison(
        vertices, faces,
        rbc_grid_vertices, rbc_grid_faces,
        evolved_vertices, evolved_faces,
        sphere_vertices, sphere_faces,
        biconcave_vertices, biconcave_faces,
        willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave,
        os.path.join(args.output_dir, "rbc_model_analysis.html")
    )
    print("Saved: rbc_model_analysis.html")

    results = {
        "model_checkpoint": args.checkpoint,
        "grid_size": grid_size,
        "original_vertices": len(vertices),
        "original_faces": len(faces),
        "projected_vertices": len(rbc_grid_vertices),
        "willmore_rbc_projected": float(willmore_rbc),
        "willmore_evolved": float(willmore_evolved),
        "willmore_sphere": float(willmore_sphere),
        "willmore_biconcave": float(willmore_biconcave),
        "energy_initial": float(energy_history[0]) if energy_history else None,
        "energy_final": float(energy_history[-1]) if energy_history else None,
        "evolution_steps": args.evolve_steps,
        "interpretation": {
            "rbc_lower_than_sphere": willmore_rbc < willmore_sphere,
            "evolved_lower_than_initial": willmore_evolved < willmore_rbc,
            "closer_to_biconcave": abs(willmore_rbc - willmore_biconcave) < abs(willmore_rbc - willmore_sphere)
        }
    }

    with open(os.path.join(args.output_dir, "results.json"), 'w') as f:
        json.dump(results, f, indent=2)
    print("Saved: results.json")

    print("\n" + "=" * 60)
    print("DONE - Open rbc_model_analysis.html to see comparison")
    print("=" * 60)

    print("\nSUMMARY:")
    print(f"  RBC (projected):  Willmore = {willmore_rbc:.4f}")
    print(f"  Model evolution:  Willmore = {willmore_evolved:.4f}")
    print(f"  Sphere:           Willmore = {willmore_sphere:.4f}")
    print(f"  Biconcave:        Willmore = {willmore_biconcave:.4f}")
    
    print("\nINTERPRETATION:")
    if willmore_rbc < willmore_sphere:
        print("  RBC has LOWER Willmore than sphere - consistent with biconcave shape")
    else:
        print("  RBC has HIGHER Willmore - projection may distort shape")
    
    if willmore_evolved < willmore_rbc:
        print("  Model EVOLUTION reduces Willmore energy - surface relaxes")
    else:
        print("  Model evolution increases energy - may need different approach")
    
    if abs(willmore_rbc - willmore_biconcave) < abs(willmore_rbc - willmore_sphere):
        print("  RBC is CLOSER to biconcave than sphere - model recognizes shape!")


if __name__ == "__main__":
    main()
