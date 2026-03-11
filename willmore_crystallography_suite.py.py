#!/usr/bin/env python3
"""
willmore_crystallography_suite.py

Comprehensive crystallographic analysis suite for Willmore energy neural network checkpoints.
Integrates spectral geometry, Ricci curvature, thermodynamic metrics, topological phase detection,
and functional validation tests to validate crystal purity and model performance.

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
License: AGPL v3
"""

import argparse
import copy
import glob
import json
import logging
import math
import os
import re
import time
import warnings
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any, Union, Protocol, runtime_checkable, Callable

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from scipy import stats, signal, linalg
from scipy.stats import entropy as scipy_entropy
from scipy.linalg import eigh, expm, eigvals
from scipy.optimize import fsolve
from sklearn.decomposition import PCA

warnings.filterwarnings('ignore')


@dataclass(frozen=True)
class WillmoreSuiteConfig:
    """Master configuration for Willmore crystallography suite."""

    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    NUM_SPECTRAL_LAYERS: int = 2
    EXPANSION_DIM: int = 64
    SURFACE_CHANNELS: int = 2

    SURFACE_TENSION_COEFFICIENT: float = 1.0
    WILLMORE_ENERGY_WEIGHT: float = 1.0
    MEAN_CURVATURE_TARGET: float = 0.0
    NUM_EIGENMODES: int = 8
    ENERGY_SCALE: float = 1.0

    MBL_LEVEL_SPACING_WIGNER_DYSON: float = 0.5307
    MBL_LEVEL_SPACING_POISSON: float = 0.3863
    MBL_TOLERANCE: float = 0.05

    ALPHA_CRYSTAL_THRESHOLD: float = 7.0
    ALPHA_PERFECT_CRYSTAL_THRESHOLD: float = 10.0
    DELTA_CRYSTAL_THRESHOLD: float = 0.1
    DELTA_OPTICAL_THRESHOLD: float = 0.01
    KAPPA_CRYSTAL_THRESHOLD: float = 1.5

    ENTROPY_BINS: int = 50
    EIGENVALUE_TOL: float = 1e-10
    KAPPA_MAX_DIM: int = 10000
    KAPPA_GRADIENT_BATCHES: int = 5
    PARAM_FLATTEN_LIMIT: int = 2000
    RICCI_CURVATURE_SAMPLES: int = 100

    ACCURACY_THRESHOLD: float = 0.95
    MSE_THRESHOLD: float = 0.05

    DEVICE: str = 'cpu'
    FIGURE_DPI: int = 300
    SAVE_FORMAT: str = 'png'


class SpectralLayer(nn.Module):
    """Spectral convolution layer with learnable frequency-domain kernels."""

    def __init__(self, channels: int, grid_size: int):
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        # CORREGIDO: Ahora coincide con willmore_crystal2.py
        # freq_h = grid_size // 2 + 1 (9 para grid_size=16)
        # freq_w = grid_size (16 para grid_size=16)
        self.freq_h = grid_size // 2 + 1
        self.freq_w = grid_size
        self.kernel_real = nn.Parameter(
            torch.randn(channels, channels, self.freq_h, self.freq_w) * 0.1
        )
        self.kernel_imag = nn.Parameter(
            torch.randn(channels, channels, self.freq_h, self.freq_w) * 0.1
        )
        self.bias = nn.Parameter(torch.zeros(channels, 1, 1))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, C, H, W = x.shape
        x_fft = torch.fft.rfft2(x)
        # x_fft forma: (B, C, H, W//2+1) = (B, C, 16, 9)

        # Interpolar kernels al tamaño de x_fft (como en willmore_crystal2.py)
        # kernel es (C_out, C_in, 9, 16), necesitamos (C_out, C_in, 16, 9) para einsum
        kernel_real_interp = F.interpolate(
            self.kernel_real, size=(H, W//2+1), mode='bilinear', align_corners=False
        )
        kernel_imag_interp = F.interpolate(
            self.kernel_imag, size=(H, W//2+1), mode='bilinear', align_corners=False
        )

        # Operación espectral: convolución en frecuencia
        out_real = torch.einsum('bchw,kchw->bkhw', x_fft.real, kernel_real_interp) - \
                   torch.einsum('bchw,kchw->bkhw', x_fft.imag, kernel_imag_interp)
        out_imag = torch.einsum('bchw,kchw->bkhw', x_fft.real, kernel_imag_interp) + \
                   torch.einsum('bchw,kchw->bkhw', x_fft.imag, kernel_real_interp)

        output_fft = torch.complex(out_real, out_imag)
        output = torch.fft.irfft2(output_fft, s=(H, W))
        output = output + self.bias
        return output


class MinimalSurfaceSpectralNetwork(nn.Module):
    """Willmore minimal surface spectral network architecture."""

    def __init__(self, config: WillmoreSuiteConfig):
        super().__init__()
        self.config = config
        self.grid_size = config.GRID_SIZE
        self.input_channels = config.SURFACE_CHANNELS
        self.output_channels = config.SURFACE_CHANNELS
        self.hidden_dim = config.HIDDEN_DIM
        self.expansion_dim = config.EXPANSION_DIM

        self.input_proj = nn.Conv2d(self.input_channels, self.hidden_dim, kernel_size=1)
        self.expansion_proj = nn.Conv2d(self.hidden_dim, self.expansion_dim, kernel_size=1)
        self.spectral_layers = nn.ModuleList([
            SpectralLayer(self.expansion_dim, self.grid_size)
            for _ in range(config.NUM_SPECTRAL_LAYERS)
        ])
        self.contraction_proj = nn.Conv2d(self.expansion_dim, self.hidden_dim, kernel_size=1)
        self.output_proj = nn.Conv2d(self.hidden_dim, self.output_channels, kernel_size=1)
        self.layer_norm = nn.LayerNorm([self.hidden_dim, self.grid_size, self.grid_size])

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 3:
            x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = self.layer_norm(x)
        x = F.gelu(self.expansion_proj(x))
        for spectral_layer in self.spectral_layers:
            x = F.gelu(spectral_layer(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)

    def get_spectral_representation(self, x: torch.Tensor) -> torch.Tensor:
        """Extract spectral features for analysis."""
        with torch.no_grad():
            if x.dim() == 3:
                x = x.unsqueeze(0)
            x = F.gelu(self.input_proj(x))
            x = F.gelu(self.expansion_proj(x))
            return torch.fft.rfft2(x)


class MinimalSurfaceOperator:
    """Analytical minimal surface operations for ground truth generation."""

    def __init__(self, grid_size: int = 16):
        self.grid_size = grid_size
        self._precompute_spectral_operators()

    def _precompute_spectral_operators(self):
        kx = torch.fft.fftfreq(self.grid_size, d=1.0) * 2 * np.pi
        ky = torch.fft.fftfreq(self.grid_size, d=1.0) * 2 * np.pi
        KX, KY = torch.meshgrid(kx, ky, indexing='ij')
        self.laplacian_spectrum = -(KX**2 + KY**2).float()
        self.kx, self.ky = kx, ky
        self.KX, self.KY = KX, KY

    def apply_laplacian(self, field: torch.Tensor) -> torch.Tensor:
        field_fft = torch.fft.fft2(field)
        laplacian_fft = field_fft * self.laplacian_spectrum.to(field.device)
        return torch.fft.ifft2(laplacian_fft).real

    def compute_mean_curvature(self, surface: torch.Tensor) -> torch.Tensor:
        surface = surface.to(torch.float64)
        grad_x = torch.gradient(surface, dim=0)[0]
        grad_y = torch.gradient(surface, dim=1)[0]
        grad_norm_sq = grad_x**2 + grad_y**2 + 1e-10
        grad_norm = torch.sqrt(grad_norm_sq)
        div_x = torch.gradient(grad_x / grad_norm, dim=0)[0]
        div_y = torch.gradient(grad_y / grad_norm, dim=1)[0]
        H = div_x + div_y
        return H.float()

    def compute_gaussian_curvature(self, surface: torch.Tensor) -> torch.Tensor:
        surface = surface.to(torch.float64)
        fx = torch.gradient(surface, dim=0)[0]
        fy = torch.gradient(surface, dim=1)[0]
        fxx = torch.gradient(fx, dim=0)[0]
        fyy = torch.gradient(fy, dim=1)[0]
        fxy = torch.gradient(fx, dim=1)[0]
        denom = (1 + fx**2 + fy**2)**2 + 1e-10
        K = (fxx * fyy - fxy**2) / denom
        return K.float()

    def compute_willmore_energy(self, surface: torch.Tensor) -> torch.Tensor:
        H = self.compute_mean_curvature(surface)
        dA = torch.ones_like(surface) / self.grid_size**2
        W = torch.sum(H**2 * dA)
        return W

    def compute_surface_area(self, surface: torch.Tensor) -> torch.Tensor:
        fx = torch.gradient(surface, dim=0)[0]
        fy = torch.gradient(surface, dim=1)[0]
        area_element = torch.sqrt(1 + fx**2 + fy**2)
        total_area = torch.sum(area_element) / self.grid_size**2
        return total_area


class SurfacePotentialGenerator:
    """Generate various surface potential configurations."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config
        self.grid_size = config.GRID_SIZE

    def pyramid_potential(self) -> torch.Tensor:
        x = torch.linspace(-1, 1, self.grid_size)
        y = torch.linspace(-1, 1, self.grid_size)
        X, Y = torch.meshgrid(x, y, indexing='ij')
        potential = torch.abs(X) + torch.abs(Y)
        return potential * self.config.SURFACE_TENSION_COEFFICIENT

    def cube_potential(self) -> torch.Tensor:
        x = torch.linspace(-1, 1, self.grid_size)
        y = torch.linspace(-1, 1, self.grid_size)
        X, Y = torch.meshgrid(x, y, indexing='ij')
        potential = torch.max(torch.abs(X), torch.abs(Y))
        return potential * self.config.SURFACE_TENSION_COEFFICIENT

    def dodecahedron_potential(self) -> torch.Tensor:
        x = torch.linspace(-1, 1, self.grid_size)
        y = torch.linspace(-1, 1, self.grid_size)
        X, Y = torch.meshgrid(x, y, indexing='ij')
        phi = (1 + np.sqrt(5)) / 2
        potential = torch.abs(X * phi) + torch.abs(Y / phi)
        return potential * self.config.SURFACE_TENSION_COEFFICIENT

    def torus_potential(self) -> torch.Tensor:
        x = torch.linspace(0, 2 * np.pi, self.grid_size)
        y = torch.linspace(0, 2 * np.pi, self.grid_size)
        X, Y = torch.meshgrid(x, y, indexing='ij')
        R, r = 1.0, 0.3
        potential = (R + r * torch.cos(X))**2 + (r * torch.sin(Y))**2
        return potential * self.config.SURFACE_TENSION_COEFFICIENT * 0.1

    def hyperbolic_potential(self) -> torch.Tensor:
        x = torch.linspace(-1, 1, self.grid_size)
        y = torch.linspace(-1, 1, self.grid_size)
        X, Y = torch.meshgrid(x, y, indexing='ij')
        r = torch.sqrt(X**2 + Y**2 + 1e-10)
        potential = torch.cosh(r) - 1
        return potential * self.config.SURFACE_TENSION_COEFFICIENT

    def generate_mixed_potential(self, seed: int) -> torch.Tensor:
        rng = np.random.RandomState(seed)
        weights = rng.dirichlet([1.0, 1.0, 1.0, 1.0, 1.0])
        potentials = [
            self.pyramid_potential(),
            self.cube_potential(),
            self.dodecahedron_potential(),
            self.torus_potential(),
            self.hyperbolic_potential()
        ]
        result = torch.zeros(self.grid_size, self.grid_size)
        for w, v in zip(weights, potentials):
            result += w * v
        return result


class MinimalSurfaceDataset(Dataset):
    """Dataset for minimal surface evolution problems."""

    def __init__(self, config: WillmoreSuiteConfig, seed: int = 42, num_samples: int = 200):
        self.config = config
        self.num_samples = num_samples
        self.grid_size = config.GRID_SIZE
        self.surface_op = MinimalSurfaceOperator(config.GRID_SIZE)
        self.potential_generator = SurfacePotentialGenerator(config)
        torch.manual_seed(seed)
        np.random.seed(seed)

        self.initial_surfaces = []
        self.target_surfaces = []
        self.potentials = []

        for i in range(num_samples):
            potential = self.potential_generator.generate_mixed_potential(seed + i)
            initial, target = self._generate_surface_pair(potential, seed + i)
            self.initial_surfaces.append(initial)
            self.target_surfaces.append(target)
            self.potentials.append(potential)

        self.initial_surfaces = torch.stack(self.initial_surfaces)
        self.target_surfaces = torch.stack(self.target_surfaces)
        self.potentials = torch.stack(self.potentials)

        split_idx = int(num_samples * 0.7)
        self.train_initial = self.initial_surfaces[:split_idx]
        self.train_target = self.target_surfaces[:split_idx]
        self.val_initial = self.initial_surfaces[split_idx:]
        self.val_target = self.target_surfaces[split_idx:]

    def _generate_surface_pair(self, potential: torch.Tensor, sample_seed: int) -> Tuple[torch.Tensor, torch.Tensor]:
        rng = np.random.RandomState(sample_seed)
        n_states = min(self.config.NUM_EIGENMODES, self.grid_size)
        state_idx = rng.randint(0, n_states)

        psi = torch.randn(self.grid_size, self.grid_size) * 0.1
        norm = torch.sqrt(torch.sum(psi**2)) + 1e-8
        psi = psi / norm * self.config.ENERGY_SCALE

        phase = torch.randn(self.grid_size, self.grid_size) * 0.5
        psi_real = psi * torch.cos(phase)
        psi_imag = psi * torch.sin(phase)
        initial = torch.stack([psi_real, psi_imag], dim=0)

        dt = 0.01
        surface_real, surface_imag = psi_real.clone(), psi_imag.clone()

        for _ in range(2):
            h_real = self.surface_op.compute_mean_curvature(surface_real)
            h_imag = self.surface_op.compute_mean_curvature(surface_imag)
            kinetic_real, kinetic_imag = -0.5 * h_real, -0.5 * h_imag
            total_h_real = kinetic_real + potential * surface_real
            total_h_imag = kinetic_imag + potential * surface_imag
            new_real = surface_real + dt * total_h_imag
            new_imag = surface_imag - dt * total_h_real
            norm = torch.sqrt(torch.sum(new_real**2 + new_imag**2)) + 1e-8
            target_norm = torch.sqrt(torch.sum(surface_real**2 + surface_imag**2)) + 1e-8
            new_real, new_imag = new_real / norm * target_norm, new_imag / norm * target_norm
            surface_real, surface_imag = new_real, new_imag

        target = torch.stack([surface_real, surface_imag], dim=0)
        return initial, target

    def __len__(self) -> int:
        return len(self.train_initial)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.train_initial[idx], self.train_target[idx]

    def get_validation_batch(self) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.val_initial, self.val_target


class WeightIntegrityCalculator:
    """Validate weight tensor integrity (NaN/Inf detection)."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config

    def compute(self, model: nn.Module) -> Dict[str, Any]:
        has_nan = has_inf = False
        nan_count = inf_count = total_params = 0

        for param in model.parameters():
            data = param.data
            numel = data.numel()
            total_params += numel
            n_nan = torch.isnan(data).sum().item()
            n_inf = torch.isinf(data).sum().item()
            if n_nan > 0:
                has_nan = True
                nan_count += n_nan
            if n_inf > 0:
                has_inf = True
                inf_count += n_inf

        corruption_ratio = (nan_count + inf_count) / total_params if total_params > 0 else 0.0

        return {
            'is_valid': not (has_nan or has_inf),
            'has_nan': has_nan,
            'has_inf': has_inf,
            'total_params': total_params,
            'nan_count': nan_count,
            'inf_count': inf_count,
            'corruption_ratio': corruption_ratio
        }


class DiscretizationCalculator:
    """Compute weight discretization metrics (delta, alpha)."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config

    def compute(self, model: nn.Module) -> Dict[str, Any]:
        margins = []
        layer_deltas = {}

        for name, param in model.named_parameters():
            if param.numel() > 0:
                p_data = param.data.detach()
                margin = (p_data - p_data.round()).abs().max().item()
                margins.append(margin)
                layer_deltas[name] = margin

        delta = max(margins) if margins else 0.0
        alpha = -np.log(delta + 1e-10) if delta > 0 else 20.0

        return {
            'delta': delta,
            'alpha': alpha,
            'is_discrete': delta < self.config.DELTA_CRYSTAL_THRESHOLD,
            'is_perfect_crystal': alpha > self.config.ALPHA_PERFECT_CRYSTAL_THRESHOLD,
            'layer_deltas': layer_deltas,
            'purity_score': min(alpha / self.config.ALPHA_CRYSTAL_THRESHOLD, 1.0)
        }


class SpectralGeometryCalculator:
    """Compute spectral geometry properties of weight matrices."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config

    def compute(self, model: nn.Module) -> Dict[str, Any]:
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        all_weights = all_weights[:self.config.PARAM_FLATTEN_LIMIT].cpu().numpy()

        n = len(all_weights)
        if n < 2:
            return {
                'spectral_gap': 0.0,
                'effective_dimension': 0,
                'level_spacing_ratio': 0.0,
                'participation_ratio': 0.0
            }

        outer_product = np.outer(all_weights, all_weights) / n
        outer_product += np.eye(n) * self.config.EIGENVALUE_TOL

        try:
            eigenvalues = eigh(outer_product, eigvals_only=True)
            eigenvalues = np.sort(eigenvalues)[::-1]

            spectral_gap = eigenvalues[0] - eigenvalues[1] if len(eigenvalues) > 1 else 0.0

            spacings = np.diff(eigenvalues[eigenvalues > self.config.EIGENVALUE_TOL])
            if len(spacings) >= 2:
                ratios = [
                    min(abs(s1), abs(s2)) / max(abs(s1), abs(s2))
                    for s1, s2 in zip(spacings[:-1], spacings[1:])
                    if abs(s1) > 1e-15 and abs(s2) > 1e-15
                ]
                level_spacing_ratio = np.mean(ratios) if ratios else 0.0
            else:
                level_spacing_ratio = 0.0

            participation_ratio = (np.sum(eigenvalues)**2) / (np.sum(eigenvalues**2) + 1e-10)
            effective_dim = int(np.sum(eigenvalues > self.config.EIGENVALUE_TOL))

            return {
                'spectral_gap': float(spectral_gap),
                'effective_dimension': effective_dim,
                'participation_ratio': float(participation_ratio),
                'level_spacing_ratio': float(level_spacing_ratio),
                'is_mbl': abs(level_spacing_ratio - self.config.MBL_LEVEL_SPACING_POISSON) < 0.1,
                'is_thermal': abs(level_spacing_ratio - self.config.MBL_LEVEL_SPACING_WIGNER_DYSON) < 0.1
            }
        except Exception as e:
            return {
                'error': str(e),
                'spectral_gap': 0.0,
                'level_spacing_ratio': 0.0,
                'effective_dimension': 0,
                'participation_ratio': 0.0
            }


class RicciCurvatureCalculator:
    """Compute Ricci curvature of weight space metric."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config

    def compute(self, model: nn.Module) -> Dict[str, Any]:
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        n = min(len(all_weights), self.config.PARAM_FLATTEN_LIMIT)
        w = all_weights[:n].cpu().numpy()

        if n < 2:
            return {
                'ricci_scalar': 0.0,
                'mean_curvature': 0.0,
                'curvature_variance': 0.0,
                'is_singular': True
            }

        metric_tensor = np.outer(w, w) / n
        metric_tensor += np.eye(n) * self.config.EIGENVALUE_TOL

        try:
            eigenvalues = eigh(metric_tensor, eigvals_only=True)
            eigenvalues = eigenvalues[eigenvalues > self.config.EIGENVALUE_TOL]

            if len(eigenvalues) >= 2:
                ricci_scalar = len(eigenvalues) * np.sum(1.0 / eigenvalues)
            else:
                ricci_scalar = 0.0

            return {
                'ricci_scalar': float(ricci_scalar),
                'mean_curvature': float(np.mean(eigenvalues)),
                'curvature_variance': float(np.var(eigenvalues)),
                'is_singular': np.any(eigenvalues < 1e-6)
            }
        except Exception as e:
            return {
                'error': str(e),
                'ricci_scalar': 0.0,
                'mean_curvature': 0.0,
                'curvature_variance': 0.0,
                'is_singular': True
            }


class WillmoreEnergyCalculator:
    """Compute Willmore energy and curvature metrics from weights."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config
        self.surface_op = MinimalSurfaceOperator(config.GRID_SIZE)

    def compute(self, model: nn.Module) -> Dict[str, Any]:
        weights = []
        for param in model.parameters():
            if param.numel() > 0:
                weights.append(param.detach().flatten())

        if not weights:
            return self._empty_metrics()

        W = torch.cat(weights)[:self.config.PARAM_FLATTEN_LIMIT]
        n = W.numel()

        if n < self.config.GRID_SIZE**2:
            padded = torch.zeros(self.config.GRID_SIZE**2)
            padded[:n] = W
            surface = padded.view(self.config.GRID_SIZE, self.config.GRID_SIZE)
        else:
            surface = W[:self.config.GRID_SIZE**2].view(self.config.GRID_SIZE, self.config.GRID_SIZE)

        return self._compute_surface_metrics(surface)

    def _compute_surface_metrics(self, surface: torch.Tensor) -> Dict[str, Any]:
        try:
            mean_curvature = self.surface_op.compute_mean_curvature(surface)
            gaussian_curvature = self.surface_op.compute_gaussian_curvature(surface)
            willmore_energy = self.surface_op.compute_willmore_energy(surface)
            surface_area = self.surface_op.compute_surface_area(surface)

            mean_curvature_mean = mean_curvature.mean().item()
            mean_curvature_var = mean_curvature.var().item()
            gaussian_curvature_mean = gaussian_curvature.mean().item()
            total_gaussian = torch.sum(gaussian_curvature).item() / self.config.GRID_SIZE**2

            is_minimal_surface = abs(mean_curvature_mean) < 0.01
            is_crystalline_surface = willmore_energy.item() < 0.01 and mean_curvature_var < 0.001

            return {
                'willmore_energy': float(willmore_energy.item()),
                'mean_curvature_mean': float(mean_curvature_mean),
                'mean_curvature_var': float(mean_curvature_var),
                'gaussian_curvature_mean': float(gaussian_curvature_mean),
                'total_gaussian_curvature': float(total_gaussian),
                'surface_area': float(surface_area.item()),
                'is_minimal_surface': float(is_minimal_surface),
                'is_crystalline_surface': float(is_crystalline_surface),
                'curvature_ratio': float(abs(mean_curvature_mean) / (abs(gaussian_curvature_mean) + 1e-10))
            }
        except Exception:
            return self._empty_metrics()

    @staticmethod
    def _empty_metrics() -> Dict[str, Any]:
        return {
            'willmore_energy': 0.0,
            'mean_curvature_mean': 0.0,
            'mean_curvature_var': 0.0,
            'gaussian_curvature_mean': 0.0,
            'total_gaussian_curvature': 0.0,
            'surface_area': 0.0,
            'is_minimal_surface': 0.0,
            'is_crystalline_surface': 0.0,
            'curvature_ratio': 0.0
        }


class TopologicalPhaseDetector:
    """Detect topological phase state via Fourier mass center analysis."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config
        self.phase_state = 0.0
        self.alignment_history = np.zeros(100)
        self.history_ptr = 0

    def detect(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        if spectral_field.dim() == 3:
            spectral_field = spectral_field.unsqueeze(0)

        B, C, H, W = spectral_field.shape
        device = spectral_field.device

        kx = torch.fft.fftfreq(H, d=1.0) * 2 * np.pi
        ky = torch.fft.fftfreq(W, d=1.0) * 2 * np.pi
        KX, KY = torch.meshgrid(kx, ky, indexing='ij')
        KX, KY = KX.to(device), KY.to(device)

        density = torch.abs(spectral_field)**2
        density = density.mean(dim=1)
        total_mass = density.sum(dim=(-2, -1), keepdim=True) + 1e-10

        R_x = (KX * density).sum(dim=(-2, -1)) / total_mass.squeeze()
        R_y = (KY * density).sum(dim=(-2, -1)) / total_mass.squeeze()

        dx = KX - R_x.view(-1, 1, 1)
        dy = KY - R_y.view(-1, 1, 1)

        I_xx = (dx**2 * density).sum(dim=(-2, -1)) / total_mass.squeeze()
        I_yy = (dy**2 * density).sum(dim=(-2, -1)) / total_mass.squeeze()
        I_xy = (dx * dy * density).sum(dim=(-2, -1)) / total_mass.squeeze()

        inertia_tensor = torch.stack([
            torch.stack([I_xx, I_xy], dim=-1),
            torch.stack([I_xy, I_yy], dim=-1)
        ], dim=-2)

        eigenvalues = torch.linalg.eigvalsh(inertia_tensor)
        anisotropy = eigenvalues[..., 0] / (eigenvalues[..., 1] + 1e-10)

        loc_mean = (1.0 - anisotropy).mean().item()
        alignment_val = (R_x < -0.5).float().mean().item()

        self.alignment_history[self.history_ptr] = alignment_val
        self.history_ptr = (self.history_ptr + 1) % len(self.alignment_history)

        is_aligned = float(alignment_val > 0.7)
        is_localized = float(loc_mean > 0.8)

        fft_2d = torch.fft.fft2(spectral_field, dim=(-2, -1))
        magnitude = torch.abs(torch.fft.fftshift(fft_2d, dim=(-2, -1)))
        power_spectrum = magnitude**2
        total_power = power_spectrum.sum(dim=(-2, -1))
        spectral_conc = power_spectrum.max(dim=-1)[0].max(dim=-1)[0] / (total_power + 1e-10)

        phase_flat = torch.angle(fft_2d).view(B, C, -1)
        phase_mean = torch.atan2(
            torch.sin(phase_flat).mean(dim=-1),
            torch.cos(phase_flat).mean(dim=-1)
        )
        phase_coherence = torch.abs(
            torch.cos(phase_flat - phase_mean.unsqueeze(-1))
        ).mean(dim=-1)

        resonance_score = spectral_conc.mean().item() * 0.3 + phase_coherence.mean().item() * 0.3 + 0.4
        is_resonant = float(resonance_score > 0.6)

        transition_prob = is_aligned * is_localized * is_resonant
        alpha = 0.95
        self.phase_state = alpha * self.phase_state + (1 - alpha) * transition_prob

        return {
            'R_cm_x': float(R_x.mean().item()),
            'R_cm_y': float(R_y.mean().item()),
            'localization_index': float(loc_mean),
            'alignment_score': float(alignment_val),
            'anisotropy': float(anisotropy.mean().item()),
            'phase_state': float(self.phase_state),
            'is_crystalline': float(self.phase_state > 0.7),
            'transition_probability': float(transition_prob),
            'resonance_score': float(resonance_score),
            'is_resonant': is_resonant,
            'phase_coherence': float(phase_coherence.mean().item()),
            'spectral_concentration': float(spectral_conc.mean().item())
        }


class BerryPhaseCalculator:
    """Compute Berry phase from checkpoint trajectory."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config

    def load_checkpoints(self, checkpoint_dir: str) -> List[Dict]:
        pattern = os.path.join(checkpoint_dir, "*.pth")
        files = sorted(glob.glob(pattern), key=self._extract_epoch)

        checkpoints = []
        for f in files:
            try:
                ckpt = torch.load(f, map_location='cpu', weights_only=False)
                checkpoints.append({
                    'path': f,
                    'epoch': self._extract_epoch(f),
                    'state_dict': ckpt.get('model_state_dict', ckpt),
                    'metrics': ckpt.get('metrics', {})
                })
            except Exception as e:
                logging.warning(f"Could not load {f}: {e}")

        return checkpoints

    def _extract_epoch(self, filepath: str) -> int:
        match = re.search(r'epoch[_]?(\d+)', filepath)
        return int(match.group(1)) if match else 0

    def flatten_spectral_kernels(self, state_dict: Dict) -> Optional[torch.Tensor]:
        kernels = []

        for key in state_dict.keys():
            if 'spectral_layers' in key and 'kernel_real' in key:
                imag_key = key.replace('kernel_real', 'kernel_imag')
                if imag_key in state_dict:
                    kr = state_dict[key]
                    ki = state_dict[imag_key]
                    kernels.append(torch.complex(kr, ki).flatten())

        return torch.cat(kernels) if kernels else None

    def calculate_berry_phase(self, checkpoint_dir: str) -> Dict[str, Any]:
        checkpoints = self.load_checkpoints(checkpoint_dir)

        if len(checkpoints) < 2:
            return {'error': f'Need at least 2 checkpoints, found {len(checkpoints)}'}

        kernel_trajectory = []
        for ckpt in checkpoints:
            kernel = self.flatten_spectral_kernels(ckpt['state_dict'])
            if kernel is not None:
                kernel_trajectory.append(kernel)

        if len(kernel_trajectory) < 2:
            return {'error': 'Could not extract spectral kernels from checkpoints'}

        berry_phases = []
        for i in range(1, len(kernel_trajectory)):
            prev = kernel_trajectory[i-1] / (torch.norm(kernel_trajectory[i-1]) + 1e-10)
            curr = kernel_trajectory[i] / (torch.norm(kernel_trajectory[i]) + 1e-10)

            overlap = torch.sum(torch.conj(prev) * curr)
            phase = torch.angle(overlap).item()
            berry_phases.append(phase)

        total_phase = np.sum(berry_phases)
        winding_number = int(round(total_phase / (2 * np.pi)))

        return {
            'total_berry_phase': float(total_phase),
            'berry_phase_mod_2pi': float(total_phase % (2 * np.pi)),
            'winding_number': winding_number,
            'num_checkpoints': len(checkpoints),
            'is_quantized': abs(total_phase % (2 * np.pi)) < 0.5 or abs(total_phase % (2 * np.pi) - 2*np.pi) < 0.5
        }


class FunctionalTest(ABC):
    """Abstract base class for functional validation tests."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def run(self, model: nn.Module, dataset: MinimalSurfaceDataset) -> Dict[str, Any]:
        pass


class AccuracyTest(FunctionalTest):
    """Test 1: Model accuracy on validation set."""

    def run(self, model: nn.Module, dataset: MinimalSurfaceDataset) -> Dict[str, Any]:
        model.eval()
        device = next(model.parameters()).device
        val_x, val_y = dataset.get_validation_batch()
        val_x, val_y = val_x.to(device), val_y.to(device)

        with torch.no_grad():
            outputs = model(val_x)
            per_sample_mse = ((outputs - val_y)**2).mean(dim=(1, 2, 3))
            accuracy = (per_sample_mse < self.config.MSE_THRESHOLD).float().mean().item()
            mean_mse = per_sample_mse.mean().item()

        return {
            'test_name': 'Accuracy Validation',
            'accuracy': accuracy,
            'mean_mse': mean_mse,
            'threshold': self.config.ACCURACY_THRESHOLD,
            'passed': accuracy >= self.config.ACCURACY_THRESHOLD
        }


class SurfaceReconstructionTest(FunctionalTest):
    """Test 2: Surface reconstruction quality via Willmore energy."""

    def __init__(self, config: WillmoreSuiteConfig):
        super().__init__(config)
        self.surface_op = MinimalSurfaceOperator(config.GRID_SIZE)

    def run(self, model: nn.Module, dataset: MinimalSurfaceDataset) -> Dict[str, Any]:
        model.eval()
        device = next(model.parameters()).device
        val_x, val_y = dataset.get_validation_batch()
        val_x, val_y = val_x.to(device), val_y.to(device)

        willmore_energies = []
        area_errors = []

        with torch.no_grad():
            outputs = model(val_x)

            for i in range(min(10, outputs.size(0))):
                out_surface = outputs[i, 0]
                target_surface = val_y[i, 0]

                willmore_out = self.surface_op.compute_willmore_energy(out_surface).item()
                willmore_target = self.surface_op.compute_willmore_energy(target_surface).item()
                willmore_energies.append(abs(willmore_out - willmore_target))

                area_out = self.surface_op.compute_surface_area(out_surface).item()
                area_target = self.surface_op.compute_surface_area(target_surface).item()
                area_errors.append(abs(area_out - area_target))

        mean_willmore_error = np.mean(willmore_energies) if willmore_energies else float('inf')
        mean_area_error = np.mean(area_errors) if area_errors else float('inf')

        return {
            'test_name': 'Surface Reconstruction',
            'mean_willmore_error': mean_willmore_error,
            'mean_area_error': mean_area_error,
            'willmore_threshold': 0.1,
            'passed': mean_willmore_error < 0.1 and mean_area_error < 0.1
        }


class GeneralizationTest(FunctionalTest):
    """Test 3: Generalization to unseen potential configurations."""

    def run(self, model: nn.Module, dataset: MinimalSurfaceDataset) -> Dict[str, Any]:
        model.eval()
        device = next(model.parameters()).device

        test_seeds = [9999, 8888, 7777, 6666, 5555]
        test_accuracies = []

        for seed in test_seeds:
            test_dataset = MinimalSurfaceDataset(self.config, seed=seed, num_samples=50)
            test_x, test_y = test_dataset.get_validation_batch()
            test_x, test_y = test_x.to(device), test_y.to(device)

            with torch.no_grad():
                outputs = model(test_x)
                per_sample_mse = ((outputs - test_y)**2).mean(dim=(1, 2, 3))
                accuracy = (per_sample_mse < self.config.MSE_THRESHOLD).float().mean().item()
                test_accuracies.append(accuracy)

        mean_test_accuracy = np.mean(test_accuracies)
        min_test_accuracy = np.min(test_accuracies)

        return {
            'test_name': 'Generalization',
            'mean_test_accuracy': mean_test_accuracy,
            'min_test_accuracy': min_test_accuracy,
            'test_seeds': test_seeds,
            'individual_accuracies': test_accuracies,
            'passed': mean_test_accuracy >= 0.9 and min_test_accuracy >= 0.8
        }


class CheckpointAnalyzer:
    """Main analyzer orchestrating all metrics and functional tests."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config
        self.logger = logging.getLogger("CheckpointAnalyzer")

        self.integrity_calc = WeightIntegrityCalculator(config)
        self.discretization_calc = DiscretizationCalculator(config)
        self.spectral_geom_calc = SpectralGeometryCalculator(config)
        self.ricci_calc = RicciCurvatureCalculator(config)
        self.willmore_calc = WillmoreEnergyCalculator(config)
        self.topo_detector = TopologicalPhaseDetector(config)

        self.accuracy_test = AccuracyTest(config)
        self.reconstruction_test = SurfaceReconstructionTest(config)
        self.generalization_test = GeneralizationTest(config)

    def analyze_checkpoint(self, checkpoint_path: str, dataset: Optional[MinimalSurfaceDataset] = None) -> Dict[str, Any]:
        self.logger.info(f"Analyzing: {checkpoint_path}")
        start_time = time.time()

        try:
            checkpoint = torch.load(checkpoint_path, map_location='cpu', weights_only=False)
        except Exception as e:
            return {'error': str(e), 'checkpoint_path': checkpoint_path}

        model = MinimalSurfaceSpectralNetwork(self.config)

        if 'model_state_dict' in checkpoint:
            state_dict = checkpoint['model_state_dict']
        else:
            state_dict = checkpoint

        try:
            model.load_state_dict(state_dict, strict=False)
        except Exception as e:
            self.logger.warning(f"State dict load warning: {e}")
            model.load_state_dict(state_dict, strict=False)

        model.eval()
        epoch = checkpoint.get('epoch', 'unknown') if isinstance(checkpoint, dict) else 'unknown'

        results = {
            'metadata': {
                'checkpoint_path': checkpoint_path,
                'epoch': epoch,
                'timestamp': datetime.now().isoformat()
            }
        }

        self.logger.info("  Computing weight integrity...")
        results['weight_integrity'] = self.integrity_calc.compute(model)

        self.logger.info("  Computing discretization metrics...")
        results['discretization'] = self.discretization_calc.compute(model)

        self.logger.info("  Computing spectral geometry...")
        results['spectral_geometry'] = self.spectral_geom_calc.compute(model)

        self.logger.info("  Computing Ricci curvature...")
        results['ricci_curvature'] = self.ricci_calc.compute(model)

        self.logger.info("  Computing Willmore energy...")
        results['willmore_energy'] = self.willmore_calc.compute(model)

        self.logger.info("  Computing topological phase...")
        spectral_field = self._extract_spectral_field(model)
        if spectral_field is not None:
            results['topological_phase'] = self.topo_detector.detect(spectral_field)
        else:
            results['topological_phase'] = {'error': 'Could not extract spectral field'}

        if dataset is not None:
            self.logger.info("  Running functional test 1: Accuracy...")
            results['functional_test_1_accuracy'] = self.accuracy_test.run(model, dataset)

            self.logger.info("  Running functional test 2: Surface reconstruction...")
            results['functional_test_2_reconstruction'] = self.reconstruction_test.run(model, dataset)

            self.logger.info("  Running functional test 3: Generalization...")
            results['functional_test_3_generalization'] = self.generalization_test.run(model, dataset)

            results['is_functional'] = all([
                results['functional_test_1_accuracy'].get('passed', False),
                results['functional_test_2_reconstruction'].get('passed', False),
                results['functional_test_3_generalization'].get('passed', False)
            ])
        else:
            results['is_functional'] = False

        results['is_crystal'] = results['discretization'].get('is_discrete', False)
        results['health_score'] = self._compute_health_score(results)
        results['metadata']['analysis_duration'] = time.time() - start_time

        return results

    def _extract_spectral_field(self, model: nn.Module) -> Optional[torch.Tensor]:
        if hasattr(model, 'spectral_layers'):
            layers = model.spectral_layers
        else:
            return None

        spectral_weights = []
        for layer in layers:
            if hasattr(layer, 'kernel_real') and hasattr(layer, 'kernel_imag'):
                kr_avg = layer.kernel_real.data.mean(dim=0)
                ki_avg = layer.kernel_imag.data.mean(dim=0)
                spectral_weights.append(torch.complex(kr_avg, ki_avg))

        return torch.stack(spectral_weights).mean(dim=0) if spectral_weights else None

    def _compute_health_score(self, results: Dict) -> float:
        scores = []

        if 'discretization' in results:
            alpha = results['discretization'].get('alpha', 0)
            scores.append(min(alpha / self.config.ALPHA_CRYSTAL_THRESHOLD, 1.0))

        if 'functional_test_1_accuracy' in results:
            acc_score = 1.0 if results['functional_test_1_accuracy'].get('passed', False) else 0.0
            scores.append(acc_score)

        if 'spectral_geometry' in results:
            lsr = results['spectral_geometry'].get('level_spacing_ratio', 0.5)
            mbl_score = 1.0 - abs(lsr - self.config.MBL_LEVEL_SPACING_POISSON) / 0.2
            scores.append(max(0, min(1, mbl_score)))

        if 'willmore_energy' in results:
            is_minimal = results['willmore_energy'].get('is_minimal_surface', 0.0)
            scores.append(float(is_minimal))

        return np.mean(scores) if scores else 0.0


class ComprehensiveVisualizer:
    """Generate comprehensive visualization of all metrics."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config

    def visualize_analysis(self, results: Dict[str, Any], output_path: str):
        fig = plt.figure(figsize=(20, 16), dpi=self.config.FIGURE_DPI)
        gs = GridSpec(4, 4, figure=fig, hspace=0.3, wspace=0.3)

        epoch = results.get('metadata', {}).get('epoch', 'unknown')
        fig.suptitle(f'Willmore Crystal Analysis - Epoch {epoch}', fontsize=16, fontweight='bold')

        self._plot_weight_integrity(results, fig.add_subplot(gs[0, 0]))
        self._plot_discretization(results, fig.add_subplot(gs[0, 1]))
        self._plot_spectral_geometry(results, fig.add_subplot(gs[0, 2]))
        self._plot_ricci_curvature(results, fig.add_subplot(gs[0, 3]))

        self._plot_functional_test_1(results, fig.add_subplot(gs[1, 0]))
        self._plot_functional_test_2(results, fig.add_subplot(gs[1, 1]))
        self._plot_functional_test_3(results, fig.add_subplot(gs[1, 2]))
        self._plot_health_summary(results, fig.add_subplot(gs[1, 3]))

        self._plot_layer_deltas(results, fig.add_subplot(gs[2, :2]))
        self._plot_phase_diagram(results, fig.add_subplot(gs[2, 2:]))

        self._plot_crystal_verdict(results, fig.add_subplot(gs[3, :]))

        plt.savefig(output_path, dpi=self.config.FIGURE_DPI, bbox_inches='tight')
        plt.close()
        logging.info(f"Visualization saved to {output_path}")

    def _plot_weight_integrity(self, results: Dict, ax):
        if 'weight_integrity' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        wi = results['weight_integrity']
        labels = ['Valid', 'NaN', 'Inf']
        sizes = [
            wi.get('total_params', 0) - wi.get('nan_count', 0) - wi.get('inf_count', 0),
            wi.get('nan_count', 0),
            wi.get('inf_count', 0)
        ]
        colors = ['#2E86AB', '#D62828', '#F18F01']
        explode = (0, 0.1, 0.1) if wi.get('has_nan') or wi.get('has_inf') else (0, 0, 0)

        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)
        ax.set_title('Weight Integrity', fontweight='bold')

    def _plot_discretization(self, results: Dict, ax):
        if 'discretization' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        disc = results['discretization']
        alpha = disc.get('alpha', 0)
        delta = disc.get('delta', 1)

        theta = np.linspace(0, np.pi, 100)
        ax.fill_between(np.cos(theta), np.sin(theta), 0, alpha=0.1, color='gray')

        alpha_angle = np.pi * (1 - min(alpha / 15, 1))
        ax.arrow(0, 0, 0.8*np.cos(alpha_angle), 0.8*np.sin(alpha_angle),
                head_width=0.1, head_length=0.05, fc='blue', ec='blue')

        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-0.2, 1.2)
        ax.set_aspect('equal')
        ax.axis('off')

        color = '#06A77D' if disc.get('is_perfect_crystal') else '#F18F01' if disc.get('is_discrete') else '#D62828'
        ax.text(0, -0.3, f'alpha = {alpha:.2f}\ndelta = {delta:.6f}', 
               ha='center', fontsize=10, color=color, fontweight='bold')
        ax.set_title('Crystal Purity (alpha)', fontweight='bold')

    def _plot_spectral_geometry(self, results: Dict, ax):
        if 'spectral_geometry' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        sg = results['spectral_geometry']
        metrics = ['Spectral\nGap', 'Level Spacing\nRatio', 'Participation\nRatio']
        values = [
            sg.get('spectral_gap', 0) * 10,
            sg.get('level_spacing_ratio', 0),
            sg.get('participation_ratio', 0) / 100
        ]
        colors = ['#2E86AB', '#A23B72', '#06A77D']

        bars = ax.bar(metrics, values, color=colors, alpha=0.7)
        ax.set_title('Spectral Geometry', fontweight='bold')
        ax.tick_params(axis='x', rotation=0)

        ax.axhline(y=self.config.MBL_LEVEL_SPACING_WIGNER_DYSON, color='red', linestyle='--', alpha=0.5, label='Wigner-Dyson')
        ax.axhline(y=self.config.MBL_LEVEL_SPACING_POISSON, color='green', linestyle='--', alpha=0.5, label='Poisson')

    def _plot_ricci_curvature(self, results: Dict, ax):
        if 'ricci_curvature' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        rc = results['ricci_curvature']
        ricci = rc.get('ricci_scalar', 0)

        color = '#D62828' if ricci < 0 else '#06A77D'
        ax.bar(['Ricci Scalar'], [ricci], color=color, alpha=0.7)
        ax.set_title(f'Ricci Curvature\n({ricci:.2e})', fontweight='bold')
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    def _plot_functional_test_1(self, results: Dict, ax):
        if 'functional_test_1_accuracy' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        test = results['functional_test_1_accuracy']
        acc = test.get('accuracy', 0)
        threshold = test.get('threshold', 0.95)

        colors = ['#D62828', '#F18F01', '#06A77D']
        bars = ax.bar(['Accuracy'], [acc], color=colors[0] if acc < threshold else colors[2], alpha=0.7)
        ax.axhline(y=threshold, color='gray', linestyle='--', alpha=0.5, label=f'Threshold ({threshold})')
        ax.set_ylim(0, 1)
        ax.set_title('TEST 1: Accuracy', fontweight='bold')

        passed = test.get('passed', False)
        status = 'PASS' if passed else 'FAIL'
        color = '#06A77D' if passed else '#D62828'
        ax.text(0.5, 0.95, status, transform=ax.transAxes, fontsize=12, color=color, fontweight='bold', ha='center', va='top')

    def _plot_functional_test_2(self, results: Dict, ax):
        if 'functional_test_2_reconstruction' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        test = results['functional_test_2_reconstruction']
        willmore_err = test.get('mean_willmore_error', float('inf'))
        area_err = test.get('mean_area_error', float('inf'))

        x_pos = [0, 1]
        values = [min(willmore_err, 1.0), min(area_err, 1.0)]
        colors = ['#06A77D' if v < 0.1 else '#F18F01' if v < 0.5 else '#D62828' for v in values]

        ax.bar(x_pos, values, color=colors, alpha=0.7)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(['Willmore Error', 'Area Error'])
        ax.set_title('TEST 2: Surface Reconstruction', fontweight='bold')

        passed = test.get('passed', False)
        status = 'PASS' if passed else 'FAIL'
        color = '#06A77D' if passed else '#D62828'
        ax.text(0.5, 0.95, status, transform=ax.transAxes, fontsize=12, color=color, fontweight='bold', ha='center', va='top')

    def _plot_functional_test_3(self, results: Dict, ax):
        if 'functional_test_3_generalization' not in results:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        test = results['functional_test_3_generalization']
        accs = test.get('individual_accuracies', [])

        if accs:
            ax.plot(range(len(accs)), accs, 'o-', color='#F18F01', linewidth=2, markersize=8)
            ax.axhline(y=0.9, color='green', linestyle='--', alpha=0.5, label='Target (0.9)')
            ax.set_xlabel('Test Seed Index')
            ax.set_ylabel('Accuracy')
            ax.set_ylim(0, 1)

        ax.set_title('TEST 3: Generalization', fontweight='bold')

        passed = test.get('passed', False)
        status = 'PASS' if passed else 'FAIL'
        color = '#06A77D' if passed else '#D62828'
        ax.text(0.5, 0.95, status, transform=ax.transAxes, fontsize=12, color=color, fontweight='bold', ha='center', va='top')

    def _plot_health_summary(self, results: Dict, ax):
        ax.axis('off')

        health = results.get('health_score', 0)
        is_crystal = results.get('is_crystal', False)
        is_functional = results.get('is_functional', False)

        summary = f"""
========================================
       CRYSTAL HEALTH REPORT          
========================================
  Health Score:    {health:.2%}          
  Is Crystal:      {'YES' if is_crystal else 'NO':8}        
  Is Functional:   {'YES' if is_functional else 'NO':8}        
========================================
  FUNCTIONAL TESTS:                       
    1. Accuracy:    {'PASS' if results.get('functional_test_1_accuracy',{}).get('passed') else 'FAIL':8}     
    2. Reconstruct: {'PASS' if results.get('functional_test_2_reconstruction',{}).get('passed') else 'FAIL':8}     
    3. Generalize:  {'PASS' if results.get('functional_test_3_generalization',{}).get('passed') else 'FAIL':8}     
========================================
"""

        color = '#06A77D' if is_crystal and is_functional else '#F18F01' if is_crystal else '#D62828'

        ax.text(0.5, 0.5, summary, transform=ax.transAxes, fontsize=10,
               verticalalignment='center', horizontalalignment='center',
               fontfamily='monospace', bbox=dict(boxstyle='round', 
               facecolor='lightyellow', edgecolor=color, linewidth=3))
        ax.set_title('Health Summary', fontweight='bold')

    def _plot_layer_deltas(self, results: Dict, ax):
        if 'discretization' not in results or 'layer_deltas' not in results['discretization']:
            ax.text(0.5, 0.5, 'No data', ha='center')
            return

        layer_deltas = results['discretization']['layer_deltas']
        names = list(layer_deltas.keys())[:12]
        values = [layer_deltas[n] for n in names]

        short_names = [n.replace('spectral_layers.', 'SL').replace('kernel_real', 'KR')[:20] for n in names]

        colors = ['#06A77D' if v < 0.1 else '#F18F01' if v < 0.4 else '#D62828' for v in values]
        ax.barh(range(len(short_names)), values, color=colors, alpha=0.7)
        ax.set_yticks(range(len(short_names)))
        ax.set_yticklabels(short_names, fontsize=8)
        ax.set_xlabel('Delta (discretization margin)')
        ax.set_title('Layer-wise Discretization', fontweight='bold')
        ax.axvline(x=0.1, color='green', linestyle='--', alpha=0.5, label='Crystal threshold')

    def _plot_phase_diagram(self, results: Dict, ax):
        ax.set_xlabel('Alpha (Purity)')
        ax.set_ylabel('Delta (Discretization)')
        ax.set_title('Phase Diagram Position', fontweight='bold')

        if 'discretization' in results:
            alpha = results['discretization'].get('alpha', 0)
            delta = results['discretization'].get('delta', 1)

            ax.fill_between([0, 15], [0, 0], [0.1, 0.1], alpha=0.2, color='green', label='Crystal')
            ax.fill_between([0, 15], [0.4, 0.4], [1, 1], alpha=0.2, color='red', label='Glass')

            color = '#06A77D' if delta < 0.1 else '#F18F01' if delta < 0.4 else '#D62828'
            ax.scatter([alpha], [delta], s=300, c=color, marker='*', zorder=5, edgecolors='black')

            ax.set_xlim(0, 15)
            ax.set_ylim(1e-6, 1)
            ax.set_yscale('log')
            ax.legend()

    def _plot_crystal_verdict(self, results: Dict, ax):
        ax.axis('off')

        is_crystal = results.get('is_crystal', False)
        is_functional = results.get('is_functional', False)
        health = results.get('health_score', 0)

        if is_crystal and is_functional:
            verdict = "PERFECT WILLMORE CRYSTAL"
            subtitle = "Weights are crystallized AND model is functional"
            color = '#06A77D'
            symbol = "DIAMOND"
        elif is_crystal:
            verdict = "CRYSTALLIZED BUT NON-FUNCTIONAL"
            subtitle = "Weights are ordered but model underperforms - needs retraining"
            color = '#F18F01'
            symbol = "WARNING"
        else:
            verdict = "AMORPHOUS GLASS"
            subtitle = "Weights are disordered - continue crystallization pressure"
            color = '#D62828'
            symbol = "CLOUD"

        text = f"""
{symbol} {verdict} {symbol}

{subtitle}

Health Score: {health:.1%}
Alpha: {results.get('discretization',{}).get('alpha',0):.2f}
Delta: {results.get('discretization',{}).get('delta',1):.6f}

Recommendation: {'Use this checkpoint for production' if is_crystal and is_functional else 'Continue training with higher lambda pressure' if not is_crystal else 'Investigate loss function - possible overfitting'}
"""

        ax.text(0.5, 0.5, text, transform=ax.transAxes, fontsize=14,
               verticalalignment='center', horizontalalignment='center',
               fontweight='bold', color=color,
               bbox=dict(boxstyle='round,pad=1', facecolor='white', 
                        edgecolor=color, linewidth=4, alpha=0.9))


class BatchProcessor:
    """Process multiple checkpoints and find the best one."""

    def __init__(self, config: WillmoreSuiteConfig):
        self.config = config
        self.logger = logging.getLogger("BatchProcessor")
        self.analyzer = CheckpointAnalyzer(config)
        self.visualizer = ComprehensiveVisualizer(config)
        self.berry_calc = BerryPhaseCalculator(config)

    def process_directory(self, checkpoint_dir: str, output_dir: str, dataset: Optional[MinimalSurfaceDataset] = None):
        self.logger.info(f"Processing directory: {checkpoint_dir}")
        os.makedirs(output_dir, exist_ok=True)

        pattern = os.path.join(checkpoint_dir, "*.pth")
        checkpoint_files = sorted(glob.glob(pattern), 
                                  key=lambda x: int(re.search(r'epoch[_]?(\d+)', x).group(1)) if re.search(r'epoch[_]?(\d+)', x) else 0)

        if not checkpoint_files:
            self.logger.error(f"No checkpoints found in {checkpoint_dir}")
            return

        self.logger.info(f"Found {len(checkpoint_files)} checkpoints")

        if dataset is None:
            dataset = MinimalSurfaceDataset(self.config, seed=42, num_samples=200)

        all_results = []
        for i, ckpt_path in enumerate(checkpoint_files):
            self.logger.info(f"[{i+1}/{len(checkpoint_files)}] Analyzing {os.path.basename(ckpt_path)}")

            try:
                results = self.analyzer.analyze_checkpoint(ckpt_path, dataset)
                all_results.append(results)

                ckpt_name = Path(ckpt_path).stem
                viz_path = os.path.join(output_dir, f"{ckpt_name}_analysis.png")
                self.visualizer.visualize_analysis(results, viz_path)

                json_path = os.path.join(output_dir, f"{ckpt_name}_metrics.json")
                with open(json_path, 'w') as f:
                    json.dump(results, f, indent=2, default=str)

            except Exception as e:
                self.logger.error(f"Error processing {ckpt_path}: {e}")
                import traceback
                self.logger.error(traceback.format_exc())

        ranked = self._rank_checkpoints(all_results)
        self._generate_summary(ranked, output_dir)

        self.logger.info("Computing Berry phase across trajectory...")
        berry_results = self.berry_calc.calculate_berry_phase(checkpoint_dir)
        berry_path = os.path.join(output_dir, "berry_phase_analysis.json")
        with open(berry_path, 'w') as f:
            json.dump(berry_results, f, indent=2, default=str)

        self.logger.info(f"Analysis complete. Best checkpoint: {ranked[0]['path'] if ranked else 'None'}")
        return ranked

    def _rank_checkpoints(self, all_results: List[Dict]) -> List[Dict]:
        scored = []
        for r in all_results:
            if 'error' in r:
                continue

            score = (
                r.get('health_score', 0) * 0.4 +
                (1.0 if r.get('is_crystal') else 0) * 0.3 +
                (1.0 if r.get('is_functional') else 0) * 0.3
            )

            scored.append({
                'path': r['metadata']['checkpoint_path'],
                'epoch': r['metadata']['epoch'],
                'score': score,
                'health': r.get('health_score', 0),
                'is_crystal': r.get('is_crystal', False),
                'is_functional': r.get('is_functional', False),
                'alpha': r.get('discretization', {}).get('alpha', 0),
                'delta': r.get('discretization', {}).get('delta', 1),
                'results': r
            })

        return sorted(scored, key=lambda x: x['score'], reverse=True)

    def _generate_summary(self, ranked: List[Dict], output_dir: str):
        summary = {
            'total_checkpoints': len(ranked),
            'best_checkpoint': ranked[0]['path'] if ranked else None,
            'best_epoch': ranked[0]['epoch'] if ranked else None,
            'best_score': ranked[0]['score'] if ranked else 0,
            'ranking': [
                {
                    'path': r['path'],
                    'epoch': r['epoch'],
                    'score': r['score'],
                    'health': r['health'],
                    'is_crystal': r['is_crystal'],
                    'is_functional': r['is_functional'],
                    'alpha': r['alpha'],
                    'delta': r['delta']
                }
                for r in ranked[:10]
            ]
        }

        summary_path = os.path.join(output_dir, "ranking_summary.json")
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2, default=str)

        self.logger.info("=" * 80)
        self.logger.info("CHECKPOINT RANKING")
        self.logger.info("=" * 80)
        for i, r in enumerate(ranked[:5], 1):
            status = "CRYSTAL+FUNC" if r['is_crystal'] and r['is_functional'] else "CRYSTAL" if r['is_crystal'] else "GLASS"
            self.logger.info(f"{i}. {status} Epoch {r['epoch']}: Score={r['score']:.3f}, "
                           f"alpha={r['alpha']:.2f}, delta={r['delta']:.6f}, "
                           f"Crystal={r['is_crystal']}, Functional={r['is_functional']}")

        self.logger.info("=" * 80)


def setup_logging(log_level: str = 'INFO'):
    """Configure logging for the suite."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main():
    parser = argparse.ArgumentParser(
        description='Willmore Crystallography Analysis Suite'
    )
    parser.add_argument(
        '--checkpoint_dir', '-c',
        type=str,
        default='willmore_results',
        help='Directory containing checkpoints'
    )
    parser.add_argument(
        '--output_dir', '-o',
        type=str,
        default='crystallography_analysis',
        help='Output directory for analysis results'
    )
    parser.add_argument(
        '--checkpoint', '-ckpt',
        type=str,
        default=None,
        help='Analyze single checkpoint instead of directory'
    )
    parser.add_argument(
        '--grid_size', '-L',
        type=int,
        default=16,
        help='Grid size (must match training)'
    )
    parser.add_argument(
        '--accuracy_threshold',
        type=float,
        default=0.95,
        help='Accuracy threshold for functional tests'
    )
    parser.add_argument(
        '--log_level',
        type=str,
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level'
    )

    args = parser.parse_args()

    setup_logging(args.log_level)

    config = WillmoreSuiteConfig(
        GRID_SIZE=args.grid_size,
        ACCURACY_THRESHOLD=args.accuracy_threshold,
        DEVICE='cpu'
    )

    processor = BatchProcessor(config)

    if args.checkpoint:
        logging.info(f"Analyzing single checkpoint: {args.checkpoint}")
        analyzer = CheckpointAnalyzer(config)
        dataset = MinimalSurfaceDataset(config, seed=42, num_samples=200)
        results = analyzer.analyze_checkpoint(args.checkpoint, dataset)

        os.makedirs(args.output_dir, exist_ok=True)

        viz_path = os.path.join(args.output_dir, "single_checkpoint_analysis.png")
        visualizer = ComprehensiveVisualizer(config)
        visualizer.visualize_analysis(results, viz_path)

        json_path = os.path.join(args.output_dir, "single_checkpoint_metrics.json")
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)

        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE")
        print("=" * 80)
        print(f"Crystal: {'YES' if results.get('is_crystal') else 'NO'}")
        print(f"Functional: {'YES' if results.get('is_functional') else 'NO'}")
        print(f"Health Score: {results.get('health_score', 0):.1%}")
        print(f"Alpha: {results.get('discretization', {}).get('alpha', 0):.2f}")
        print(f"Delta: {results.get('discretization', {}).get('delta', 0):.6f}")
        print(f"\nFunctional Tests:")
        print(f"  1. Accuracy: {'PASS' if results.get('functional_test_1_accuracy',{}).get('passed') else 'FAIL'}")
        print(f"  2. Reconstruction: {'PASS' if results.get('functional_test_2_reconstruction',{}).get('passed') else 'FAIL'}")
        print(f"  3. Generalization: {'PASS' if results.get('functional_test_3_generalization',{}).get('passed') else 'FAIL'}")
        print("=" * 80)
    else:
        dataset = MinimalSurfaceDataset(config, seed=42, num_samples=200)
        processor.process_directory(args.checkpoint_dir, args.output_dir, dataset)


if __name__ == "__main__":
    main()