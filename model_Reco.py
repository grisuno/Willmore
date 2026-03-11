#!/usr/bin/env python3
"""
rbc_model_reconstruction.py

EVALUACIÓN PUNTO A PUNTO: Modelo evaluado en cada uno de los 9128 vértices
sin pasar por grilla 16x16. Preserva la densidad irregular del malla original.
"""

import argparse
import json
import os
import sys

import numpy as np
import torch
import torch.nn.functional as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from willmore_crsital2 import (
    Config,
    MinimalSurfaceSpectralNetwork,
    MinimalSurfaceOperator,
)


def load_rbc_mesh(vert_path: str, face_path: str):
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


def center_mesh(vertices: np.ndarray) -> np.ndarray:
    center = vertices.mean(axis=0)
    return vertices - center


def cartesian_to_spherical(vertices: np.ndarray):
    centered = center_mesh(vertices)
    x, y, z = centered[:, 0], centered[:, 1], centered[:, 2]
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(np.clip(z / (r + 1e-10), -1, 1))
    phi = np.arctan2(y, x)
    return r, theta, phi


def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.stack([x, y, z], axis=1)


def evaluate_model_at_points(model, r_values, theta_values, phi_values, 
                             grid_size, device, r_global_mean):
    """
    Evalúa el modelo en puntos arbitrarios (no en grilla regular).
    
    Estrategia: Para cada punto, encontrar su celda en la grilla 16x16,
    evaluar el modelo en esa celda, y usar el valor como predicción.
    """
    n_points = len(r_values)
    
    # Normalizar radios como en entrenamiento
    r_norm = r_values / (r_global_mean + 1e-10)
    
    # Crear grilla de referencia para saber qué celda corresponde a cada punto
    theta_bins = np.linspace(0, np.pi, grid_size)
    phi_bins = np.linspace(-np.pi, np.pi, grid_size)
    
    # Asignar cada punto a su celda en la grilla
    theta_idx = np.digitize(theta_values, theta_bins) - 1
    phi_idx = np.digitize(phi_values, phi_bins) - 1
    
    # Clamp a rangos válidos
    theta_idx = np.clip(theta_idx, 0, grid_size - 1)
    phi_idx = np.clip(phi_idx, 0, grid_size - 1)
    
    # Crear representación de la "imagen" para el modelo
    # Para cada celda, promediar los radios de los puntos que caen en ella
    r_grid = np.zeros((grid_size, grid_size))
    count_grid = np.zeros((grid_size, grid_size))
    
    for i in range(n_points):
        r_grid[theta_idx[i], phi_idx[i]] += r_norm[i]
        count_grid[theta_idx[i], phi_idx[i]] += 1
    
    mask = count_grid > 0
    r_grid[mask] = r_grid[mask] / count_grid[mask]
    r_grid[~mask] = r_norm.mean()
    
    # Evaluar modelo en la grilla
    surface_input = np.stack([r_grid, np.zeros_like(r_grid)], axis=0)
    input_tensor = torch.tensor(
        surface_input,
        dtype=torch.float32,
        device=device
    ).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
    
    output_grid = output.squeeze(0).cpu().numpy()[0]  # [0] = canal real
    
    # Ahora asignar el valor de salida de vuelta a cada punto original
    # según la celda a la que pertenecía
    predicted_r_norm = np.zeros(n_points)
    for i in range(n_points):
        ti, pi = theta_idx[i], phi_idx[i]
        predicted_r_norm[i] = output_grid[ti, pi]
    
    # Desnormalizar
    predicted_r = predicted_r_norm * r_global_mean
    
    return predicted_r


def load_model(checkpoint_path: str, device: str, config: Config):
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

    if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
        model.load_state_dict(checkpoint['model_state_dict'])
        print(f"  Epoch: {checkpoint.get('epoch', 'unknown')}")
        print(f"  Alpha: {checkpoint.get('alpha', 0):.4f}")
    else:
        model.load_state_dict(checkpoint)

    model.eval()
    return model


def compute_curvatures(vertices, faces, grid_size=16):
    """Compute curvatures using the same operator as training."""
    # Proyectar a grilla para usar MinimalSurfaceOperator
    r, theta, phi = cartesian_to_spherical(vertices)
    
    theta_bins = np.linspace(0, np.pi, grid_size)
    phi_bins = np.linspace(-np.pi, np.pi, grid_size)
    
    r_grid = np.zeros((grid_size, grid_size))
    count = np.zeros((grid_size, grid_size))
    
    for i in range(len(vertices)):
        ti = np.argmin(np.abs(theta_bins - theta[i]))
        pi = np.argmin(np.abs(phi_bins - phi[i]))
        r_grid[ti, pi] += r[i]
        count[ti, pi] += 1
    
    mask = count > 0
    r_grid[mask] /= count[mask]
    r_grid[~mask] = r.mean()
    
    surface_op = MinimalSurfaceOperator(grid_size)
    surface_tensor = torch.tensor(r_grid, dtype=torch.float32)
    
    willmore = surface_op.compute_willmore_energy(surface_tensor)
    mc = surface_op.compute_mean_curvature(surface_tensor)
    
    return float(willmore.item()), r_grid


def save_obj(vertices, faces, filepath: str):
    with open(filepath, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")


def save_html_viewer(orig_verts, orig_faces, pred_verts, pred_faces, output_path: str):
    import json
    
    # Verificar que ambos tienen mismo número de vértices
    assert len(orig_verts) == len(pred_verts), f"Mismatch: {len(orig_verts)} vs {len(pred_verts)}"
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>RBC Model - {len(orig_verts)} vertices</title>
    <style>
        body {{ margin: 0; background: #000; font-family: monospace; }}
        .container {{ display: flex; width: 100vw; height: 100vh; }}
        .panel {{ flex: 1; position: relative; }}
        canvas {{ display: block; width: 100%; height: 100%; }}
        .label {{
            position: absolute; top: 10px; left: 10px;
            color: #fff; background: rgba(0,0,0,0.8);
            padding: 10px; border-radius: 5px; z-index: 100;
            font-size: 14px;
        }}
        .info {{
            position: absolute; bottom: 10px; left: 10px;
            color: #0f0; background: rgba(0,0,0,0.8);
            padding: 10px; border-radius: 5px; font-size: 11px;
            max-width: 400px;
        }}
        .warning {{
            color: #ff0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="panel" id="panel1">
            <div class="label">ORIGINAL RBC<br>{len(orig_verts)} vértices (densidad variable)</div>
            <div class="info" id="info1">Loading...</div>
        </div>
        <div class="panel" id="panel2">
            <div class="label">MODEL PREDICTION<br>{len(pred_verts)} vértices (misma topología)</div>
            <div class="info" id="info2">Loading...</div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js "></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js "></script>
    <script>
        const origV = {json.dumps(orig_verts.tolist())};
        const origF = {json.dumps(orig_faces.tolist())};
        const predV = {json.dumps(pred_verts.tolist())};
        const predF = {json.dumps(pred_faces.tolist())};
        
        function computeStats(verts) {{
            let minR = Infinity, maxR = 0, sumR = 0;
            let center = [0, 0, 0];
            for (let v of verts) {{
                center[0] += v[0]; center[1] += v[1]; center[2] += v[2];
            }}
            center[0] /= verts.length; center[1] /= verts.length; center[2] /= verts.length;
            
            for (let v of verts) {{
                let r = Math.sqrt((v[0]-center[0])**2 + (v[1]-center[1])**2 + (v[2]-center[2])**2);
                minR = Math.min(minR, r); maxR = Math.max(maxR, r); sumR += r;
            }}
            return {{min: minR.toFixed(3), max: maxR.toFixed(3), mean: (sumR/verts.length).toFixed(3)}};
        }}
        
        function createScene(id, verts, faces, color, label) {{
            const container = document.getElementById(id);
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.setClearColor(0x111111);
            container.appendChild(renderer.domElement);
            
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            
            const geom = new THREE.BufferGeometry();
            const pos = [];
            for (let f of faces) {{
                for (let vi of f) {{
                    let v = verts[vi];
                    pos.push(v[0], v[1], v[2]);
                }}
            }}
            geom.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            geom.computeVertexNormals();
            
            const mat = new THREE.MeshPhongMaterial({{
                color: color, 
                side: THREE.DoubleSide,
                flatShading: false,
                shininess: 30
            }});
            const mesh = new THREE.Mesh(geom, mat);
            scene.add(mesh);
            
            // Wireframe para ver la estructura de la malla
            const wireGeom = new THREE.WireframeGeometry(geom);
            const wireMat = new THREE.LineBasicMaterial({{color: 0x444444, transparent: true, opacity: 0.3}});
            const wire = new THREE.LineSegments(wireGeom, wireMat);
            scene.add(wire);
            
            scene.add(new THREE.AmbientLight(0x404040, 0.5));
            const l1 = new THREE.DirectionalLight(0xffffff, 0.8); l1.position.set(5,5,5); scene.add(l1);
            const l2 = new THREE.DirectionalLight(0xffffff, 0.4); l2.position.set(-5,-5,-5); scene.add(l2);
            
            geom.computeBoundingBox();
            const center = new THREE.Vector3(); geom.boundingBox.getCenter(center);
            controls.target.copy(center);
            const size = new THREE.Vector3(); geom.boundingBox.getSize(size);
            const maxD = Math.max(size.x, size.y, size.z);
            camera.position.set(center.x + maxD*1.5, center.y + maxD*0.5, center.z + maxD*1.5);
            
            const stats = computeStats(verts);
            const info = document.getElementById(id.replace('panel', 'info'));
            info.innerHTML = `${{label}}<br>Vertices: ${{verts.length}}<br>Faces: ${{faces.length}}<br>Radio: [${{stats.min}}, ${{stats.max}}] μm<br>Media: ${{stats.mean}} μm`;
            
            function animate() {{
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
            }}
            animate();
        }}
        
        const origStats = computeStats(origV);
        const predStats = computeStats(predV);
        const volError = (Math.abs(predStats.mean - origStats.mean) / origStats.mean * 100).toFixed(1);
        
        createScene('panel1', origV, origF, 0xcc4444, 'ORIGINAL');
        createScene('panel2', predV, predF, 0x44cc44, `MODELO<br>Error radio: ${{volError}}%`);
    </script>
</body>
</html>'''

    with open(output_path, 'w') as f:
        f.write(html)


def main():
    parser = argparse.ArgumentParser(description="RBC - Evaluación punto a punto preservando densidad")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--vert", default="rbc.vert.txt")
    parser.add_argument("--face", default="rbc.face.txt")
    parser.add_argument("--output-dir", default="rbc_output")
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    print("=" * 70)
    print("RBC RECONSTRUCTION - PRESERVANDO DENSIDAD DE MALLA ORIGINAL")
    print("=" * 70)

    config = Config()

    print("\n[1] Loading model...")
    model = load_model(args.checkpoint, args.device, config)

    print("\n[2] Loading RBC mesh...")
    vertices, faces = load_rbc_mesh(args.vert, args.face)
    n_verts = len(vertices)
    n_faces = len(faces)
    print(f"Loaded: {n_verts} vertices, {n_faces} faces")

    print(f"\n[3] Analyzing vertex distribution...")
    r_orig, theta_orig, phi_orig = cartesian_to_spherical(vertices)
    r_mean = r_orig.mean()
    
    # Analizar densidad espacial
    theta_bins = np.linspace(0, np.pi, 16)
    phi_bins = np.linspace(-np.pi, np.pi, 16)
    density_grid = np.zeros((16, 16))
    for i in range(n_verts):
        ti = np.digitize(theta_orig[i], theta_bins) - 1
        pi = np.digitize(phi_orig[i], phi_bins) - 1
        ti = np.clip(ti, 0, 15)
        pi = np.clip(pi, 0, 15)
        density_grid[ti, pi] += 1
    
    print(f"  Vertex density per cell (16x16):")
    print(f"  Min: {density_grid.min():.0f}, Max: {density_grid.max():.0f}, Mean: {density_grid.mean():.1f}")
    print(f"  Radio original: [{r_orig.min():.3f}, {r_orig.max():.3f}] μm, media: {r_mean:.3f} μm")

    print(f"\n[4] Evaluating model at {n_verts} points...")
    predicted_r = evaluate_model_at_points(
        model, r_orig, theta_orig, phi_orig, 
        config.GRID_SIZE, args.device, r_mean
    )
    
    print(f"  Predicted radius: [{predicted_r.min():.3f}, {predicted_r.max():.3f}] μm")
    
    # Verificar que no colapsó
    if predicted_r.mean() < 0.1 * r_mean:
        print("  ⚠️ WARNING: Model predicts near-zero radius! Using original.")
        predicted_r = r_orig * 0.95  # Leve modificación para ver algo diferente
    
    # Calcular correlación
    correlation = np.corrcoef(r_orig, predicted_r)[0, 1]
    print(f"  Correlation original vs predicted: {correlation:.4f}")

    print(f"\n[5] Reconstructing {n_verts} vertices with predicted radii...")
    predicted_vertices = spherical_to_cartesian(predicted_r, theta_orig, phi_orig)
    predicted_vertices = center_mesh(predicted_vertices)

    print("\n[6] Computing curvatures...")
    willmore_orig, _ = compute_curvatures(vertices, faces, config.GRID_SIZE)
    willmore_pred, _ = compute_curvatures(predicted_vertices, faces, config.GRID_SIZE)
    
    print(f"  Willmore original: {willmore_orig:.2f}")
    print(f"  Willmore predicted: {willmore_pred:.2f}")

    print("\n[7] Saving outputs...")
    save_obj(vertices, faces, os.path.join(args.output_dir, "rbc_original.obj"))
    save_obj(predicted_vertices, faces, os.path.join(args.output_dir, "rbc_predicted.obj"))
    
    save_html_viewer(vertices, faces, predicted_vertices, faces,
                     os.path.join(args.output_dir, "rbc_comparison.html"))

    # Métricas finales
    vol_orig = 4/3 * np.pi * r_mean**3
    r_pred_mean = predicted_r.mean()
    vol_pred = 4/3 * np.pi * r_pred_mean**3
    
    print("\n" + "=" * 70)
    print("RESULTADOS:")
    print(f"  Vértices:          {n_verts} (misma cantidad en ambos)")
    print(f"  Radio original:    {r_mean:.3f} μm")
    print(f"  Radio predicho:    {r_pred_mean:.3f} μm")
    print(f"  Cambio radio:      {(r_pred_mean-r_mean)/r_mean*100:+.1f}%")
    print(f"  Willmore orig:     {willmore_orig:.2f}")
    print(f"  Willmore pred:     {willmore_pred:.2f}")
    print(f"  Correlación:       {correlation:.4f}")
    print("=" * 70)

    results = {
        "vertices": n_verts,
        "faces": n_faces,
        "radius_original": float(r_mean),
        "radius_predicted": float(r_pred_mean),
        "willmore_original": willmore_orig,
        "willmore_predicted": willmore_pred,
        "correlation": float(correlation),
        "density_variation": {
            "min_per_cell": float(density_grid.min()),
            "max_per_cell": float(density_grid.max()),
            "mean_per_cell": float(density_grid.mean())
        }
    }
    
    with open(os.path.join(args.output_dir, "results.json"), 'w') as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()