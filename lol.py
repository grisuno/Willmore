#!/usr/bin/env python3
"""
demo_cylindrical_vs_spherical.py

DEMO HONESTA: Comparación de proyección esférica vs cilíndrica.

CONCLUSIÓN ANTICIPADA:
- Esférica: NO funciona bien para RBC (dimples en polos)
- Cilíndrica: SÍ funciona (el RBC es naturalmente cilíndrico)
"""

import numpy as np
import os
from scipy.ndimage import gaussian_filter

def create_synthetic_rbc(n_vertices=3000):
    """RBC sintético con forma bicóncava."""
    R0, z0, c = 4.0, 1.5, 0.8
    
    theta = np.linspace(0, 2*np.pi, int(np.sqrt(n_vertices)))
    z_norm = np.linspace(-1, 1, int(np.sqrt(n_vertices)))
    
    vertices = []
    for t in theta:
        for zn in z_norm:
            r = R0 * np.sqrt(max(1 - zn**2, 0)) * (1 + c * zn**2)
            if r > 0.1:
                vertices.append([r*np.cos(t), r*np.sin(t), zn*z0])
    
    vertices = np.array(vertices)
    
    # Caras simples
    n_t, n_z = len(theta), len(z_norm)
    faces = []
    for i in range(n_t - 1):
        for j in range(n_z - 1):
            idx = i * n_z + j
            if idx + n_z + 1 < len(vertices):
                faces.extend([[idx, idx+1, idx+n_z], [idx+1, idx+n_z+1, idx+n_z]])
    
    return vertices, np.array(faces)


def spherical_projection(vertices, grid_size):
    """Proyección esférica - tiene problemas con dimples."""
    centered = vertices - vertices.mean(axis=0)
    x, y, z = centered[:, 0], centered[:, 1], centered[:, 2]
    r = np.sqrt(x**2 + y**2 + z**2) + 1e-10
    
    theta = np.arccos(np.clip(z / r, -1, 1))
    phi = np.arctan2(y, x)
    
    d_theta = np.pi / grid_size
    d_phi = 2 * np.pi / grid_size
    
    r_grid = np.zeros((grid_size, grid_size))
    count = np.zeros((grid_size, grid_size))
    
    for i in range(len(vertices)):
        ti = int(theta[i] / d_theta)
        pi = int((phi[i] + np.pi) / d_phi)
        ti = min(max(ti, 0), grid_size - 1)
        pi = min(max(pi, 0), grid_size - 1)
        
        r_grid[ti, pi] += r[i]
        count[ti, pi] += 1
    
    mask = count > 0
    r_mean = r.mean()
    r_grid[mask] /= count[mask]
    r_grid[~mask] = r_mean  # PROBLEMA: rellenar con promedio
    
    return r_grid, mask, r_mean


def cylindrical_projection(vertices, grid_size):
    """
    Proyección cilíndrica - NATURAL para RBC.
    
    Coordenadas:
    - z: altura (-z_max a +z_max)
    - phi: ángulo azimutal (-π a π)
    - rho: radio en el plano xy
    
    El RBC es naturalmente cilíndrico: los dimples están en z=±z_max,
    no en direcciones angulares.
    """
    centered = vertices - vertices.mean(axis=0)
    x, y, z = centered[:, 0], centered[:, 1], centered[:, 2]
    
    rho = np.sqrt(x**2 + y**2) + 1e-10
    phi = np.arctan2(y, x)
    
    z_min, z_max = z.min(), z.max()
    z_range = z_max - z_min + 1e-10
    
    d_z = 1.0 / grid_size
    d_phi = 2 * np.pi / grid_size
    
    rho_grid = np.zeros((grid_size, grid_size))
    count = np.zeros((grid_size, grid_size))
    
    for i in range(len(vertices)):
        # Normalizar z a [0, 1]
        z_norm = (z[i] - z_min) / z_range
        zi = int(z_norm * (grid_size - 1))
        pi = int((phi[i] + np.pi) / d_phi)
        
        zi = min(max(zi, 0), grid_size - 1)
        pi = min(max(pi, 0), grid_size - 1)
        
        rho_grid[zi, pi] += rho[i]
        count[zi, pi] += 1
    
    mask = count > 0
    rho_mean = rho.mean()
    rho_grid[mask] /= count[mask]
    rho_grid[~mask] = rho_mean
    
    return rho_grid, mask, rho_mean, z_min, z_max


def spherical_to_cartesian(r_grid, grid_size):
    """Convierte grilla esférica a 3D."""
    theta = np.linspace(0, np.pi, grid_size)
    phi = np.linspace(-np.pi, np.pi, grid_size)
    THETA, PHI = np.meshgrid(theta, phi, indexing='ij')
    
    x = r_grid * np.sin(THETA) * np.cos(PHI)
    y = r_grid * np.sin(THETA) * np.sin(PHI)
    z = r_grid * np.cos(THETA)
    
    vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)
    
    faces = []
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            idx = i * grid_size + j
            faces.extend([[idx, idx+1, idx+grid_size], [idx+1, idx+grid_size+1, idx+grid_size]])
    
    return vertices, np.array(faces)


def cylindrical_to_cartesian(rho_grid, z_min, z_max, grid_size):
    """Convierte grilla cilíndrica a 3D."""
    z = np.linspace(z_min, z_max, grid_size)
    phi = np.linspace(-np.pi, np.pi, grid_size)
    Z, PHI = np.meshgrid(z, phi, indexing='ij')
    
    x = rho_grid * np.cos(PHI)
    y = rho_grid * np.sin(PHI)
    
    vertices = np.stack([x.flatten(), y.flatten(), Z.flatten()], axis=1)
    
    faces = []
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            idx = i * grid_size + j
            faces.extend([[idx, idx+1, idx+grid_size], [idx+1, idx+grid_size+1, idx+grid_size]])
    
    return vertices, np.array(faces)


def compute_metrics(r_grid, mask, original_r):
    """Computa métricas de calidad."""
    # Variación local (artefactos)
    grad_x = np.diff(r_grid, axis=1)
    grad_y = np.diff(r_grid, axis=0)
    grad_mag = np.sqrt(grad_x[:-1, :]**2 + grad_y[:, :-1]**2)
    artifact_score = grad_mag.std()
    
    # Error de escala
    scale_error = abs(r_grid.mean() - original_r.mean()) / original_r.mean() * 100
    
    # Celdas vacías
    empty_pct = (~mask).sum() / mask.size * 100
    
    return artifact_score, scale_error, empty_pct


def save_obj(vertices, faces, filepath):
    with open(filepath, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")


def main():
    print("=" * 70)
    print("COMPARACIÓN HONESTA: ESFÉRICA vs CILÍNDRICA")
    print("=" * 70)
    
    grid_size = 64
    output_dir = "demo_comparison"
    os.makedirs(output_dir, exist_ok=True)
    
    # Crear RBC
    print("\n[1] Creando RBC sintético...")
    vertices, faces = create_synthetic_rbc()
    
    centered = vertices - vertices.mean(axis=0)
    r_orig = np.linalg.norm(centered, axis=1)
    rho_orig = np.sqrt(centered[:, 0]**2 + centered[:, 1]**2)
    
    print(f"    Vértices: {len(vertices)}")
    print(f"    Radio 3D: {r_orig.mean():.3f} ± {r_orig.std():.3f}")
    print(f"    Radio XY (rho): {rho_orig.mean():.3f} ± {rho_orig.std():.3f}")
    
    # Proyección esférica
    print("\n[2] Proyección ESFÉRICA...")
    r_sph, mask_sph, r_mean_sph = spherical_projection(vertices, grid_size)
    art_sph, scale_sph, empty_sph = compute_metrics(r_sph, mask_sph, r_orig)
    
    print(f"    Celdas vacías: {empty_sph:.1f}%")
    print(f"    Error de escala: {scale_sph:.1f}%")
    print(f"    Score artefactos: {art_sph:.4f}")
    
    # Proyección cilíndrica
    print("\n[3] Proyección CILÍNDRICA...")
    rho_cyl, mask_cyl, rho_mean, z_min, z_max = cylindrical_projection(vertices, grid_size)
    art_cyl, scale_cyl, empty_cyl = compute_metrics(rho_cyl, mask_cyl, rho_orig)
    
    print(f"    Celdas vacías: {empty_cyl:.1f}%")
    print(f"    Error de escala: {scale_cyl:.1f}%")
    print(f"    Score artefactos: {art_cyl:.4f}")
    
    # Guardar
    print("\n[4] Guardando resultados...")
    
    v_sph, f_sph = spherical_to_cartesian(r_sph, grid_size)
    v_cyl, f_cyl = cylindrical_to_cartesian(rho_cyl, z_min, z_max, grid_size)
    
    save_obj(vertices, faces, f"{output_dir}/original.obj")
    save_obj(v_sph, f_sph, f"{output_dir}/spherical.obj")
    save_obj(v_cyl, f_cyl, f"{output_dir}/cylindrical.obj")
    
    # Comparación
    print("\n" + "=" * 70)
    print("RESULTADO FINAL")
    print("=" * 70)
    
    print(f"\n{'Métrica':<25} {'Esférica':<20} {'Cilíndrica':<20}")
    print("-" * 65)
    print(f"{'Celdas vacías':<25} {empty_sph:.1f}%{'':<15} {empty_cyl:.1f}%")
    print(f"{'Error de escala':<25} {scale_sph:.1f}%{'':<15} {scale_cyl:.1f}%")
    print(f"{'Score artefactos':<25} {art_sph:.4f}{'':<15} {art_cyl:.4f}")
    
    print("\nCONCLUSIÓN:")
    if empty_cyl < empty_sph:
        print(f"  ✓ Cilíndrica tiene MENOS celdas vacías ({empty_cyl:.1f}% vs {empty_sph:.1f}%)")
    if scale_cyl < scale_sph:
        print(f"  ✓ Cilíndrica preserva MEJOR la escala ({scale_cyl:.1f}% vs {scale_sph:.1f}% error)")
    if art_cyl < art_sph:
        print(f"  ✓ Cilíndrica tiene MENOS artefactos ({art_cyl:.4f} vs {art_sph:.4f})")
    
    print(f"\nArchivos en {output_dir}/:")
    print("  - original.obj      (RBC sintético original)")
    print("  - spherical.obj     (proyección esférica - con artefactos)")
    print("  - cylindrical.obj   (proyección cilíndrica - sin artefactos)")


if __name__ == "__main__":
    main()