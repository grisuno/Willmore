#!/usr/bin/env python3
"""
rbc_model_reconstruction_128_v2.py

Red Blood Cell 3D Reconstruction USING THE SCALED WILLMORE MODEL at 128x128.

Improved version with better spherical parametrization that avoids
artificial lobes and properly handles the biconcave RBC geometry.

Key improvements:
- Area-weighted projection to avoid polar artifacts
- Gaussian smoothing in spherical coordinates
- Proper handling of the dimple regions
- Better interpolation for sparse data
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from scipy import ndimage
from scipy.interpolate import griddata, RBFInterpolator

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from willmore_crsital2 import MinimalSurfaceOperator


@dataclass
class ReconstructionConfig:
    """Configuration for RBC reconstruction."""
    grid_size: int = 128
    hidden_dim: int = 32
    expansion_dim: int = 64
    num_spectral_layers: int = 2
    surface_channels: int = 2
    device: str = "cpu"
    evolve_steps: int = 200
    evolution_lr_initial: float = 0.1
    evolution_lr_final: float = 0.01
    smoothing_sigma: float = 1.5
    use_rbf_interpolation: bool = True
    volume_conservation: bool = True
    lr_schedule: str = "cosine"


class SpectralLayer(nn.Module):
    """Spectral convolution layer for minimal surface processing."""
    
    def __init__(self, channels: int, grid_size: int):
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        self.kernel_real = nn.Parameter(
            torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1
        )
        self.kernel_imag = nn.Parameter(
            torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_fft = torch.fft.rfft2(x)
        batch, channels, freq_h, freq_w = x_fft.shape
        kernel_real = self.kernel_real.mean(dim=0)
        kernel_imag = self.kernel_imag.mean(dim=0)
        kernel_real_exp = kernel_real.unsqueeze(0).unsqueeze(0).squeeze(0)
        kernel_imag_exp = kernel_imag.unsqueeze(0).unsqueeze(0).squeeze(0)
        kernel_real_interp = F.interpolate(
            kernel_real_exp, size=(freq_h, freq_w), mode="bilinear", align_corners=False
        )
        kernel_imag_interp = F.interpolate(
            kernel_imag_exp, size=(freq_h, freq_w), mode="bilinear", align_corners=False
        )
        real_part = x_fft.real * kernel_real_interp - x_fft.imag * kernel_imag_interp
        imag_part = x_fft.real * kernel_imag_interp + x_fft.imag * kernel_real_interp
        output_fft = torch.complex(real_part, imag_part)
        output = torch.fft.irfft2(output_fft, s=(self.grid_size, self.grid_size))
        return output


class MinimalSurfaceSpectralNetwork(nn.Module):
    """Spectral network for minimal surface computation."""
    
    def __init__(
        self,
        grid_size: int = 128,
        hidden_dim: int = 32,
        expansion_dim: int = 64,
        num_spectral_layers: int = 2,
        input_channels: int = 2,
        output_channels: int = 2,
    ):
        super().__init__()
        self.grid_size = grid_size
        self.input_channels = input_channels
        self.output_channels = output_channels
        self.input_proj = nn.Conv2d(input_channels, hidden_dim, kernel_size=1)
        self.expansion_proj = nn.Conv2d(hidden_dim, expansion_dim, kernel_size=1)
        self.spectral_layers = nn.ModuleList([
            SpectralLayer(expansion_dim, grid_size) for _ in range(num_spectral_layers)
        ])
        self.contraction_proj = nn.Conv2d(expansion_dim, hidden_dim, kernel_size=1)
        self.output_proj = nn.Conv2d(hidden_dim, output_channels, kernel_size=1)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 3:
            x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = F.gelu(self.expansion_proj(x))
        for spectral_layer in self.spectral_layers:
            x = F.gelu(spectral_layer(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)


class CheckpointLoader:
    """Handles loading of model checkpoints."""
    
    @staticmethod
    def load(checkpoint_path: str, device: str) -> Dict[str, Any]:
        if not os.path.exists(checkpoint_path):
            raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")
        return torch.load(checkpoint_path, map_location=device, weights_only=False)


class ModelBuilder:
    """Builds and initializes models from configuration."""
    
    @staticmethod
    def build(config: ReconstructionConfig) -> MinimalSurfaceSpectralNetwork:
        return MinimalSurfaceSpectralNetwork(
            grid_size=config.grid_size,
            hidden_dim=config.hidden_dim,
            expansion_dim=config.expansion_dim,
            num_spectral_layers=config.num_spectral_layers,
            input_channels=config.surface_channels,
            output_channels=config.surface_channels,
        ).to(config.device)
    
    @staticmethod
    def load_from_checkpoint(
        checkpoint_path: str,
        config: ReconstructionConfig,
    ) -> MinimalSurfaceSpectralNetwork:
        model = ModelBuilder.build(config)
        checkpoint = CheckpointLoader.load(checkpoint_path, config.device)
        
        if isinstance(checkpoint, dict):
            if "model_state_dict" in checkpoint:
                model.load_state_dict(checkpoint["model_state_dict"])
            elif "state_dict" in checkpoint:
                model.load_state_dict(checkpoint["state_dict"])
            else:
                model.load_state_dict(checkpoint)
        else:
            model.load_state_dict(checkpoint)
        
        model.eval()
        for param in model.parameters():
            param.requires_grad = False
        
        return model


class RBCMeshLoader:
    """Loads RBC mesh data from OpenRBC format files."""
    
    @staticmethod
    def load(vert_path: str, face_path: str) -> Tuple[np.ndarray, np.ndarray]:
        vertices = []
        with open(vert_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 3:
                    vertices.append([float(parts[0]), float(parts[1]), float(parts[2])])
        vertices = np.array(vertices, dtype=np.float64)
        
        faces = []
        with open(face_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 3:
                    i0, i1, i2 = int(parts[0]), int(parts[1]), int(parts[2])
                    if i0 >= 0 and i1 >= 0 and i2 >= 0:
                        faces.append([i0, i1, i2])
        faces = np.array(faces, dtype=np.int64)
        
        return vertices, faces


class ImprovedSphericalProjector:
    """
    Improved spherical projection with proper handling of biconcave geometry.
    
    Key improvements:
    1. Area-weighted averaging to avoid oversampling at poles
    2. RBF interpolation for smooth reconstruction
    3. Proper handling of the dimple regions
    4. Gaussian smoothing in parameter space
    """
    
    def __init__(self, grid_size: int, smoothing_sigma: float = 1.5):
        self.grid_size = grid_size
        self.smoothing_sigma = smoothing_sigma
        
        self.theta = np.linspace(0, np.pi, grid_size)
        self.phi = np.linspace(-np.pi, np.pi, grid_size)
        self.THETA, self.PHI = np.meshgrid(self.theta, self.phi, indexing="ij")
    
    def compute_vertex_areas(self, vertices: np.ndarray, faces: np.ndarray) -> np.ndarray:
        """Compute approximate area associated with each vertex."""
        areas = np.zeros(len(vertices))
        
        for face in faces:
            v0, v1, v2 = vertices[face[0]], vertices[face[1]], vertices[face[2]]
            edge1 = v1 - v0
            edge2 = v2 - v0
            face_area = 0.5 * np.linalg.norm(np.cross(edge1, edge2))
            areas[face[0]] += face_area / 3
            areas[face[1]] += face_area / 3
            areas[face[2]] += face_area / 3
        
        return areas
    
    def project_mesh(
        self,
        vertices: np.ndarray,
        faces: np.ndarray,
        use_rbf: bool = True,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Project mesh onto spherical grid with proper area weighting.
        """
        centered = vertices - vertices.mean(axis=0)
        
        x, y, z = centered[:, 0], centered[:, 1], centered[:, 2]
        r = np.sqrt(x**2 + y**2 + z**2) + 1e-10
        
        theta = np.arccos(np.clip(z / r, -1, 1))
        phi = np.arctan2(y, x)
        
        vertex_areas = self.compute_vertex_areas(vertices, faces)
        
        if use_rbf:
            r_grid = self._rbf_interpolation(theta, phi, r)
        else:
            r_grid = self._area_weighted_projection(theta, phi, r, vertex_areas)
        
        r_grid = self._apply_spherical_smoothing(r_grid)
        
        r_mean = r.mean()
        r_normalized = r_grid / r_mean
        
        phase_grid = np.sin(self.THETA) * np.cos(self.PHI)
        
        real_part = r_normalized.astype(np.float32)
        imag_part = phase_grid.astype(np.float32)
        
        mask = np.ones_like(r_grid, dtype=bool)
        
        return real_part, imag_part, r_grid * r_mean, mask
    
    def _area_weighted_projection(
        self,
        theta: np.ndarray,
        phi: np.ndarray,
        r: np.ndarray,
        areas: np.ndarray,
    ) -> np.ndarray:
        """Project using area-weighted averaging."""
        r_sum = np.zeros((self.grid_size, self.grid_size))
        weight_sum = np.zeros((self.grid_size, self.grid_size))
        
        d_theta = np.pi / self.grid_size
        d_phi = 2 * np.pi / self.grid_size
        
        for i in range(len(theta)):
            ti = int(theta[i] / d_theta)
            pi = int((phi[i] + np.pi) / d_phi)
            
            ti = min(max(ti, 0), self.grid_size - 1)
            pi = min(max(pi, 0), self.grid_size - 1)
            
            sin_theta = np.sin(theta[i]) + 0.1
            weight = areas[i] * sin_theta
            
            r_sum[ti, pi] += r[i] * weight
            weight_sum[ti, pi] += weight
        
        mask = weight_sum > 0
        r_grid = np.ones((self.grid_size, self.grid_size)) * r.mean()
        r_grid[mask] = r_sum[mask] / weight_sum[mask]
        
        return r_grid
    
    def _rbf_interpolation(
        self,
        theta: np.ndarray,
        phi: np.ndarray,
        r: np.ndarray,
    ) -> np.ndarray:
        """Use RBF interpolation for smooth reconstruction."""
        points = np.column_stack([theta, phi])
        
        try:
            rbf = RBFInterpolator(
                points,
                r,
                kernel="thin_plate_spline",
                smoothing=0.1,
            )
            
            grid_points = np.column_stack([
                self.THETA.flatten(),
                self.PHI.flatten(),
            ])
            
            r_flat = rbf(grid_points)
            r_grid = r_flat.reshape(self.grid_size, self.grid_size)
            
        except Exception:
            r_grid = self._area_weighted_projection(theta, phi, r, np.ones(len(r)))
        
        return r_grid
    
    def _apply_spherical_smoothing(self, r_grid: np.ndarray) -> np.ndarray:
        """Apply Gaussian smoothing adapted to spherical coordinates."""
        r_grid_float = r_grid.astype(np.float64)
        
        smoothed = ndimage.gaussian_filter(
            r_grid_float,
            sigma=self.smoothing_sigma,
            mode="wrap",
        )
        
        center_theta = self.grid_size // 2
        polar_region = np.zeros_like(smoothed)
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                dist_to_pole = min(i, self.grid_size - 1 - i)
                if dist_to_pole < 5:
                    polar_weight = dist_to_pole / 5.0
                    smoothed[i, j] = (1 - polar_weight) * r_grid_float.mean() + polar_weight * smoothed[i, j]
        
        return smoothed
    
    def to_cartesian(
        self,
        r_grid: np.ndarray,
        scale: float = 1.0,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Convert spherical grid back to 3D vertices."""
        r_scaled = r_grid * scale
        
        x = r_scaled * np.sin(self.THETA) * np.cos(self.PHI)
        y = r_scaled * np.sin(self.THETA) * np.sin(self.PHI)
        z = r_scaled * np.cos(self.THETA)
        
        vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)
        
        faces = []
        for i in range(self.grid_size - 1):
            for j in range(self.grid_size - 1):
                idx = i * self.grid_size + j
                faces.append([idx, idx + 1, idx + self.grid_size])
                faces.append([idx + 1, idx + self.grid_size + 1, idx + self.grid_size])
        faces = np.array(faces, dtype=np.int64)
        
        return vertices, faces


class CylindricalProjector:
    """
    Cylindrical projection - often better for biconcave shapes.
    
    The RBC is naturally more cylindrical than spherical,
    with the dimples on top and bottom.
    """
    
    def __init__(self, grid_size: int, smoothing_sigma: float = 1.0):
        self.grid_size = grid_size
        self.smoothing_sigma = smoothing_sigma
        
        self.z_coord = np.linspace(-1, 1, grid_size)
        self.phi = np.linspace(-np.pi, np.pi, grid_size)
        self.Z, self.PHI = np.meshgrid(self.z_coord, self.phi, indexing="ij")
    
    def project_mesh(
        self,
        vertices: np.ndarray,
        faces: np.ndarray,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Project mesh using cylindrical coordinates."""
        centered = vertices - vertices.mean(axis=0)
        
        z_sorted_idx = np.argsort(centered[:, 2])
        z_min = centered[:, 2].min()
        z_max = centered[:, 2].max()
        z_range = z_max - z_min + 1e-10
        
        z_norm = (centered[:, 2] - z_min) / z_range
        
        phi = np.arctan2(centered[:, 1], centered[:, 0])
        
        rho = np.sqrt(centered[:, 0]**2 + centered[:, 1]**2)
        
        rho_grid = np.zeros((self.grid_size, self.grid_size))
        count_grid = np.zeros((self.grid_size, self.grid_size))
        
        for i in range(len(vertices)):
            zi = int(z_norm[i] * (self.grid_size - 1))
            pi = int((phi[i] + np.pi) / (2 * np.pi) * (self.grid_size - 1))
            
            zi = min(max(zi, 0), self.grid_size - 1)
            pi = min(max(pi, 0), self.grid_size - 1)
            
            rho_grid[zi, pi] += rho[i]
            count_grid[zi, pi] += 1
        
        mask = count_grid > 0
        rho_grid[mask] = rho_grid[mask] / count_grid[mask]
        
        rho_mean = rho.mean()
        rho_grid[~mask] = rho_mean
        
        rho_grid = ndimage.gaussian_filter(rho_grid, sigma=self.smoothing_sigma, mode="wrap")
        
        rho_normalized = rho_grid / rho_mean
        
        phase_grid = np.cos(self.PHI)
        
        real_part = rho_normalized.astype(np.float32)
        imag_part = phase_grid.astype(np.float32)
        
        return real_part, imag_part, rho_grid, mask
    
    def to_cartesian(
        self,
        rho_grid: np.ndarray,
        z_scale: float = 1.0,
        rho_scale: float = 1.0,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Convert cylindrical grid back to 3D vertices."""
        z_scaled = self.Z * z_scale
        rho_scaled = rho_grid * rho_scale
        
        x = rho_scaled * np.cos(self.PHI)
        y = rho_scaled * np.sin(self.PHI)
        z = z_scaled
        
        vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)
        
        faces = []
        for i in range(self.grid_size - 1):
            for j in range(self.grid_size - 1):
                idx = i * self.grid_size + j
                faces.append([idx, idx + 1, idx + self.grid_size])
                faces.append([idx + 1, idx + self.grid_size + 1, idx + self.grid_size])
        faces = np.array(faces, dtype=np.int64)
        
        return vertices, faces


class SyntheticShapeGenerator:
    """Generates synthetic shapes for comparison."""
    
    def __init__(self, grid_size: int):
        self.grid_size = grid_size
        self.theta = np.linspace(0, np.pi, grid_size)
        self.phi = np.linspace(-np.pi, np.pi, grid_size)
        self.THETA, self.PHI = np.meshgrid(self.theta, self.phi, indexing="ij")
    
    def create_sphere(self, radius: float = 1.0) -> np.ndarray:
        return np.ones((self.grid_size, self.grid_size)) * radius
    
    def create_biconcave(self, radius: float = 1.0, dimple_depth: float = 0.6) -> np.ndarray:
        """Create biconcave disc shape using Evans-Fung model."""
        cos_theta = np.cos(self.THETA)
        shape_factor = 1.0 - dimple_depth * cos_theta**2
        return radius * shape_factor
    
    def create_evans_fung_rbc(
        self,
        radius: float = 1.0,
        dimple_depth: float = 0.6,
        thickness: float = 0.3,
    ) -> np.ndarray:
        """
        Create RBC shape using Evans-Fung parametrization.
        
        The RBC cross-section follows:
        r(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)
        
        This creates the characteristic biconcave shape.
        """
        z_norm = np.cos(self.THETA)
        
        radial_factor = np.sqrt(np.maximum(1 - z_norm**2, 0))
        dimple_factor = 1.0 + thickness * z_norm**2
        
        r_grid = radius * radial_factor * dimple_factor
        
        center_mask = radial_factor < 0.1
        r_grid[center_mask] = r_grid[~center_mask].min()
        
        return r_grid


class WillmoreMetricsCalculator:
    """Calculates Willmore energy and curvature metrics."""
    
    def __init__(self, grid_size: int):
        self.surface_op = MinimalSurfaceOperator(grid_size)
    
    def compute_willmore(self, surface: np.ndarray) -> float:
        surface_tensor = torch.tensor(surface, dtype=torch.float32)
        return float(self.surface_op.compute_willmore_energy(surface_tensor).item())
    
    def compute_curvature_stats(
        self,
        surface: np.ndarray,
    ) -> Dict[str, float]:
        surface_tensor = torch.tensor(surface, dtype=torch.float32)
        
        mean_curv = self.surface_op.compute_mean_curvature(surface_tensor)
        gauss_curv = self.surface_op.compute_gaussian_curvature(surface_tensor)
        
        return {
            "mean_curvature_mean": float(mean_curv.mean().item()),
            "mean_curvature_std": float(mean_curv.std().item()),
            "mean_curvature_max": float(mean_curv.max().item()),
            "gaussian_curvature_mean": float(gauss_curv.mean().item()),
            "gaussian_curvature_std": float(gauss_curv.std().item()),
        }


class SurfaceEvolver:
    """Evolves surfaces using the trained model with LR schedule and volume conservation."""
    
    def __init__(
        self,
        model: nn.Module,
        config: ReconstructionConfig,
    ):
        self.model = model
        self.config = config
    
    def _compute_lr(self, step: int) -> float:
        """Compute learning rate with cosine schedule."""
        progress = step / self.config.evolve_steps
        if self.config.lr_schedule == "cosine":
            return self.config.evolution_lr_final + \
                   0.5 * (self.config.evolution_lr_initial - self.config.evolution_lr_final) * \
                   (1 + np.cos(np.pi * progress))
        else:
            return self.config.evolution_lr_initial - \
                   progress * (self.config.evolution_lr_initial - self.config.evolution_lr_final)
    
    def _compute_volume(self, surface: np.ndarray) -> float:
        """Estimate volume from surface grid."""
        return np.sum(surface ** 2)
    
    def _normalize_volume(self, surface: np.ndarray, target_volume: float) -> np.ndarray:
        """Normalize surface to preserve volume."""
        current_volume = self._compute_volume(surface)
        if current_volume > 1e-10:
            scale = np.sqrt(target_volume / current_volume)
            return surface * scale
        return surface
    
    def evolve(
        self,
        initial_surface: np.ndarray,
    ) -> Tuple[np.ndarray, List[np.ndarray], List[float]]:
        real_part = initial_surface.copy()
        imag_part = np.zeros_like(real_part)
        
        trajectory = [real_part.copy()]
        energy_history = []
        
        if self.config.volume_conservation:
            target_volume = self._compute_volume(real_part)
        
        for step in range(self.config.evolve_steps):
            lr = self._compute_lr(step)
            
            input_tensor = torch.tensor(
                np.stack([real_part, imag_part]),
                dtype=torch.float32,
                device=self.config.device,
            ).unsqueeze(0)
            
            with torch.no_grad():
                output = self.model(input_tensor)
            
            output_np = output.squeeze(0).cpu().numpy()
            
            delta_real = output_np[0] - real_part
            real_part = real_part + lr * delta_real
            
            if self.config.volume_conservation and step % 10 == 0:
                real_part = self._normalize_volume(real_part, target_volume)
            
            trajectory.append(real_part.copy())
            
            energy = np.sum(real_part**2)
            energy_history.append(energy)
            
            if step % 50 == 0:
                print(f"  Step {step}: energy = {energy:.6f}, lr = {lr:.4f}")
        
        return trajectory[-1], trajectory, energy_history


class MeshExporter:
    """Exports meshes to various formats."""
    
    @staticmethod
    def save_obj(vertices: np.ndarray, faces: np.ndarray, filepath: str) -> None:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            for v in vertices:
                f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
            for face in faces:
                f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")
    
    @staticmethod
    def save_html_comparison(
        original_vertices: np.ndarray,
        original_faces: np.ndarray,
        projected_vertices: np.ndarray,
        projected_faces: np.ndarray,
        evolved_vertices: np.ndarray,
        evolved_faces: np.ndarray,
        biconcave_vertices: np.ndarray,
        biconcave_faces: np.ndarray,
        metrics: Dict[str, float],
        output_path: str,
    ) -> None:
        html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>RBC Willmore Model Analysis (128x128 Improved Projection)</title>
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
            <div class="label">RBC PROJECTED (Improved)<br>({len(projected_vertices)} vertices)</div>
            <div class="info">Willmore: {metrics.get('willmore_projected', 0):.4f}</div>
        </div>
        <div class="panel" id="panel3">
            <div class="label">MODEL EVOLUTION<br>({len(evolved_vertices)} vertices)</div>
            <div class="info">Willmore: {metrics.get('willmore_evolved', 0):.4f}</div>
        </div>
        <div class="panel" id="panel4">
            <div class="label">BICONCAVE REFERENCE</div>
            <div class="info">Willmore: {metrics.get('willmore_biconcave', 0):.4f}</div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        const panelData = [
            {{ id: 'panel1', vertices: {json.dumps(original_vertices.tolist())}, faces: {json.dumps(original_faces.tolist())}, color: 0xcc4444 }},
            {{ id: 'panel2', vertices: {json.dumps(projected_vertices.tolist())}, faces: {json.dumps(projected_faces.tolist())}, color: 0x44cc44 }},
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

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(html)


class RBCReconstructionPipeline:
    """Main pipeline for RBC reconstruction using scaled model."""
    
    def __init__(self, config: ReconstructionConfig):
        self.config = config
        self.spherical_projector = ImprovedSphericalProjector(
            config.grid_size, config.smoothing_sigma
        )
        self.cylindrical_projector = CylindricalProjector(
            config.grid_size, config.smoothing_sigma
        )
        self.shape_generator = SyntheticShapeGenerator(config.grid_size)
        self.metrics_calc = WillmoreMetricsCalculator(config.grid_size)
    
    def run(
        self,
        checkpoint_path: str,
        vert_path: str,
        face_path: str,
        output_dir: str,
        projection_type: str = "spherical",
    ) -> Dict[str, Any]:
        os.makedirs(output_dir, exist_ok=True)
        
        print("=" * 80)
        print("RBC RECONSTRUCTION - IMPROVED PROJECTION (128x128 Grid)")
        print(f"Projection type: {projection_type}")
        print("=" * 80)
        
        print("\n[1] Loading scaled model from checkpoint...")
        model = ModelBuilder.load_from_checkpoint(checkpoint_path, self.config)
        num_params = sum(p.numel() for p in model.parameters())
        print(f"Model loaded: {num_params:,} parameters, grid_size={self.config.grid_size}")
        
        print("\n[2] Loading RBC mesh from OpenRBC...")
        vertices, faces = RBCMeshLoader.load(vert_path, face_path)
        print(f"Loaded: {len(vertices)} vertices, {len(faces)} faces")
        
        print(f"\n[3] Projecting RBC to {self.config.grid_size}x{self.config.grid_size} grid...")
        print(f"    Using {projection_type} projection with RBF interpolation...")
        
        if projection_type == "cylindrical":
            real_part, imag_part, r_grid, mask = self.cylindrical_projector.project_mesh(
                vertices, faces
            )
        else:
            real_part, imag_part, r_grid, mask = self.spherical_projector.project_mesh(
                vertices, faces, use_rbf=self.config.use_rbf_interpolation
            )
        
        print(f"Grid shape: {real_part.shape}")
        print(f"Grid range: [{real_part.min():.4f}, {real_part.max():.4f}]")
        
        print("\n[4] Computing Willmore energy on projected grid...")
        willmore_projected = self.metrics_calc.compute_willmore(real_part)
        print(f"RBC projected Willmore: {willmore_projected:.6f}")
        
        print(f"\n[5] Running model inference on RBC grid...")
        input_tensor = torch.tensor(
            np.stack([real_part, imag_part]),
            dtype=torch.float32,
            device=self.config.device,
        ).unsqueeze(0)
        
        with torch.no_grad():
            output = model(input_tensor)
        
        output_np = output.squeeze(0).cpu().numpy()
        print(f"Model output range: [{output_np[0].min():.4f}, {output_np[0].max():.4f}]")
        
        print(f"\n[6] Evolving surface for {self.config.evolve_steps} steps...")
        evolver = SurfaceEvolver(model, self.config)
        evolved_grid, trajectory, energy_history = evolver.evolve(real_part)
        
        willmore_evolved = self.metrics_calc.compute_willmore(evolved_grid)
        print(f"Evolved Willmore: {willmore_evolved:.6f}")
        
        print("\n[7] Creating comparison shapes...")
        r_mean = np.linalg.norm(vertices, axis=1).mean()
        
        sphere_grid = self.shape_generator.create_sphere(r_mean)
        willmore_sphere = self.metrics_calc.compute_willmore(sphere_grid)
        
        biconcave_grid = self.shape_generator.create_biconcave(r_mean)
        willmore_biconcave = self.metrics_calc.compute_willmore(biconcave_grid)
        
        print(f"Sphere Willmore: {willmore_sphere:.6f}")
        print(f"Biconcave Willmore: {willmore_biconcave:.6f}")
        
        print("\n[8] Converting grids to 3D meshes...")
        
        if projection_type == "cylindrical":
            projected_vertices, projected_faces = self.cylindrical_projector.to_cartesian(
                real_part, z_scale=r_mean, rho_scale=r_mean
            )
            evolved_vertices, evolved_faces = self.cylindrical_projector.to_cartesian(
                evolved_grid, z_scale=r_mean, rho_scale=r_mean
            )
            biconcave_vertices, biconcave_faces = self.cylindrical_projector.to_cartesian(
                biconcave_grid, z_scale=r_mean, rho_scale=r_mean
            )
        else:
            projected_vertices, projected_faces = self.spherical_projector.to_cartesian(
                real_part, r_mean
            )
            evolved_vertices, evolved_faces = self.spherical_projector.to_cartesian(
                evolved_grid, r_mean
            )
            biconcave_vertices, biconcave_faces = self.spherical_projector.to_cartesian(
                biconcave_grid, r_mean
            )
        
        print("\n[9] Saving outputs...")
        
        MeshExporter.save_obj(vertices, faces, os.path.join(output_dir, "rbc_original.obj"))
        MeshExporter.save_obj(projected_vertices, projected_faces, os.path.join(output_dir, "rbc_projected_improved.obj"))
        MeshExporter.save_obj(evolved_vertices, evolved_faces, os.path.join(output_dir, "rbc_evolved_improved.obj"))
        MeshExporter.save_obj(biconcave_vertices, biconcave_faces, os.path.join(output_dir, "biconcave_reference.obj"))
        
        print("Saved: rbc_original.obj, rbc_projected_improved.obj, rbc_evolved_improved.obj, biconcave_reference.obj")
        
        metrics = {
            "willmore_projected": willmore_projected,
            "willmore_evolved": willmore_evolved,
            "willmore_sphere": willmore_sphere,
            "willmore_biconcave": willmore_biconcave,
        }
        
        MeshExporter.save_html_comparison(
            vertices, faces,
            projected_vertices, projected_faces,
            evolved_vertices, evolved_faces,
            biconcave_vertices, biconcave_faces,
            metrics,
            os.path.join(output_dir, "rbc_model_analysis_improved.html"),
        )
        print("Saved: rbc_model_analysis_improved.html")
        
        results = {
            "model_checkpoint": checkpoint_path,
            "grid_size": self.config.grid_size,
            "model_parameters": num_params,
            "projection_type": projection_type,
            "smoothing_sigma": self.config.smoothing_sigma,
            "use_rbf_interpolation": self.config.use_rbf_interpolation,
            "original_vertices": len(vertices),
            "original_faces": len(faces),
            "projected_vertices": len(projected_vertices),
            "willmore_rbc_projected": float(willmore_projected),
            "willmore_evolved": float(willmore_evolved),
            "willmore_sphere": float(willmore_sphere),
            "willmore_biconcave": float(willmore_biconcave),
            "energy_initial": float(energy_history[0]) if energy_history else None,
            "energy_final": float(energy_history[-1]) if energy_history else None,
            "evolution_steps": self.config.evolve_steps,
            "interpretation": {
                "rbc_lower_than_sphere": willmore_projected < willmore_sphere,
                "evolved_lower_than_initial": willmore_evolved < willmore_projected,
                "closer_to_biconcave": abs(willmore_projected - willmore_biconcave) < abs(willmore_projected - willmore_sphere),
            },
        }
        
        with open(os.path.join(output_dir, "results_improved.json"), "w") as f:
            json.dump(results, f, indent=2)
        print("Saved: results_improved.json")
        
        return results


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="RBC Reconstruction with Improved Projection (128x128 Grid)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--checkpoint",
        default="scaled_models/scaled_model_grid_128.pth",
        help="Path to scaled model checkpoint",
    )
    parser.add_argument(
        "--vert",
        default="rbc.vert.txt",
        help="RBC vertex file",
    )
    parser.add_argument(
        "--face",
        default="rbc.face.txt",
        help="RBC face file",
    )
    parser.add_argument(
        "--output-dir",
        default="rbc_model_output_improved",
        help="Output directory",
    )
    parser.add_argument(
        "--device",
        default="cpu",
        choices=["cpu", "cuda"],
        help="Device for computation",
    )
    parser.add_argument(
        "--evolve-steps",
        type=int,
        default=200,
        help="Evolution steps",
    )
    parser.add_argument(
        "--grid-size",
        type=int,
        default=128,
        help="Grid size (should match checkpoint)",
    )
    parser.add_argument(
        "--projection",
        default="spherical",
        choices=["spherical", "cylindrical"],
        help="Projection type for RBC mesh",
    )
    parser.add_argument(
        "--smoothing-sigma",
        type=float,
        default=1.5,
        help="Gaussian smoothing sigma for projection",
    )
    parser.add_argument(
        "--no-rbf",
        action="store_true",
        help="Disable RBF interpolation (faster but less smooth)",
    )
    parser.add_argument(
        "--lr-initial",
        type=float,
        default=0.1,
        help="Initial learning rate for evolution",
    )
    parser.add_argument(
        "--lr-final",
        type=float,
        default=0.01,
        help="Final learning rate for evolution",
    )
    parser.add_argument(
        "--no-volume-conservation",
        action="store_true",
        help="Disable volume conservation during evolution",
    )
    parser.add_argument(
        "--lr-schedule",
        default="cosine",
        choices=["cosine", "linear"],
        help="Learning rate schedule",
    )
    return parser


def main() -> int:
    parser = build_argument_parser()
    args = parser.parse_args()
    
    config = ReconstructionConfig(
        grid_size=args.grid_size,
        device=args.device,
        evolve_steps=args.evolve_steps,
        smoothing_sigma=args.smoothing_sigma,
        use_rbf_interpolation=not args.no_rbf,
        evolution_lr_initial=args.lr_initial,
        evolution_lr_final=args.lr_final,
        volume_conservation=not args.no_volume_conservation,
        lr_schedule=args.lr_schedule,
    )
    
    pipeline = RBCReconstructionPipeline(config)
    
    try:
        results = pipeline.run(
            checkpoint_path=args.checkpoint,
            vert_path=args.vert,
            face_path=args.face,
            output_dir=args.output_dir,
            projection_type=args.projection,
        )
        
        print("\n" + "=" * 80)
        print("RECONSTRUCTION COMPLETE")
        print("=" * 80)
        
        print("\nSUMMARY:")
        print(f"  Grid Size:        {results['grid_size']}x{results['grid_size']}")
        print(f"  Projection:       {results['projection_type']}")
        print(f"  Smoothing Sigma:  {results['smoothing_sigma']}")
        print(f"  RBF Interpolation: {results['use_rbf_interpolation']}")
        print(f"  RBC (projected):  Willmore = {results['willmore_rbc_projected']:.4f}")
        print(f"  Model evolution:  Willmore = {results['willmore_evolved']:.4f}")
        print(f"  Sphere:           Willmore = {results['willmore_sphere']:.4f}")
        print(f"  Biconcave:        Willmore = {results['willmore_biconcave']:.4f}")
        
        print("\nINTERPRETATION:")
        interp = results["interpretation"]
        
        if interp["rbc_lower_than_sphere"]:
            print("  RBC has LOWER Willmore than sphere - consistent with biconcave shape")
        else:
            print("  RBC has HIGHER Willmore - projection may still have artifacts")
        
        if interp["evolved_lower_than_initial"]:
            print("  Model EVOLUTION reduces Willmore energy - surface relaxes")
        else:
            print("  Model evolution increases energy - may need different approach")
        
        if interp["closer_to_biconcave"]:
            print("  RBC is CLOSER to biconcave than sphere - improved projection!")
        
        print(f"\nOpen {args.output_dir}/rbc_model_analysis_improved.html for 3D visualization")
        
        return 0
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 2


if __name__ == "__main__":
    sys.exit(main())