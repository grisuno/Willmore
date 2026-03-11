#!/usr/bin/env python3
"""
willmore_crystal.py

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
Date of creation: 2026
License: AGPL v3

Description:
Surface Tension and Willmore Energy Grokking via Minimal Surface Topological Crystallization.
Based on the physical law that governs soap bubble formation:
  - Mean Curvature H = 0 (minimal surfaces)
  - Willmore Energy: W = integral(H^2 dA)
  - Surface Tension minimization

The training of neural networks is modeled as a Ricci flow in weight space,
where regularization acts as surface tension and discrete algorithms are
minimal surfaces (hyperspheres of Perelman) that emerge as low-entropy attractors.

Five-phase protocol:
  Phase 1 - Batch size prospecting
  Phase 2 - Seed mining with decreasing delta criterion
  Phase 3 - Full training of best seed + batch size until grokking
  Phase 4 - Refinement via simulated annealing toward crystal state
  Phase 5 - Quadruple precision (float128) high-pressure crystallization
"""

import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os
import time
import json
from datetime import datetime
from typing import Dict, Tuple, Optional, List, Any, Union
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from collections import deque
import logging
import math
import copy
import warnings

warnings.filterwarnings('ignore')


@dataclass
class Config:
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
    SURFACE_AREA_TARGET: float = 1.0
    GAUSS_CURVATURE_WEIGHT: float = 0.1
    RICCI_FLOW_STEP: float = 0.01
    BATCH_SIZE: int = 32
    LEARNING_RATE: float = 0.005
    WEIGHT_DECAY: float = 1e-4
    EPOCHS: int = 5000
    REFINEMENT_EPOCHS: int = 2000
    PHASE5_EPOCHS: int = 3000
    CHECKPOINT_INTERVAL_MINUTES: int = 5
    MAX_CHECKPOINTS: int = 10
    TARGET_ACCURACY: float = 0.95
    TIME_STEPS: int = 2
    DT: float = 0.01
    TRAIN_RATIO: float = 0.7
    NUM_SAMPLES: int = 200
    GRADIENT_CLIP_NORM: float = 1.0
    NOISE_AMPLITUDE: float = 0.01
    NOISE_INTERVAL_EPOCHS: int = 25
    MOMENTUM: float = 0.9
    COSINE_ANNEALING_ETA_MIN_FACTOR: float = 0.01
    MSE_THRESHOLD: float = 0.05
    CYCLIC_LR_BASE_FACTOR: float = 0.01
    CYCLIC_LR_MAX_FACTOR: float = 2.0
    CYCLIC_LR_STEP_SIZE: int = 50
    ENTROPY_BINS: int = 50
    PCA_COMPONENTS: int = 2
    KDE_BANDWIDTH: str = 'scott'
    MIN_VARIANCE_THRESHOLD: float = 1e-8
    ENTROPY_EPS: float = 1e-10
    HBAR: float = 1e-6
    HBAR_PHYSICAL: float = 1.0545718e-34
    POYNTING_THRESHOLD: float = 1.0
    ENERGY_FLOW_SCALE: float = 0.1
    DISCRETIZATION_MARGIN: float = 0.1
    TARGET_SLOTS: int = 7
    KAPPA_MAX_DIM: int = 10000
    EIGENVALUE_TOL: float = 1e-10
    KAPPA_GRADIENT_BATCHES: int = 5
    ALPHA_CRYSTAL_THRESHOLD: float = 7.0
    ALPHA_PERFECT_CRYSTAL_THRESHOLD: float = 10.0
    SPECTRAL_PEAK_LIMIT: int = 10
    SPECTRAL_POWER_LIMIT: int = 100
    PARAM_FLATTEN_LIMIT: int = 1000
    GRADIENT_BUFFER_LIMIT: int = 500
    GRADIENT_BUFFER_WINDOW: int = 10
    LOSS_HISTORY_WINDOW: int = 50
    GRADIENT_BUFFER_MAXLEN: int = 50
    LOSS_HISTORY_MAXLEN: int = 100
    TEMP_HISTORY_MAXLEN: int = 100
    CV_HISTORY_MAXLEN: int = 100
    CV_THRESHOLD: float = 1.0
    WEIGHT_METRIC_DIM_LIMIT: int = 256
    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    RANDOM_SEED: int = 1
    LOG_LEVEL: str = 'INFO'
    RESULTS_DIR: str = 'willmore_results'
    MINING_MAX_ATTEMPTS: int = 300
    MINING_START_SEED: int = 1
    MINING_GLASS_PATIENCE_EPOCHS: int = 50
    MINING_PROSPECT_EPOCHS: int = 40
    MINING_PROSPECT_DELTA_EPOCH_INTERVAL: int = 10
    MINING_TARGET_LC: float = 0.01
    MINING_TARGET_SP: float = 0.01
    MINING_TARGET_KAPPA: float = 1.01
    MINING_TARGET_DELTA: float = 0.001
    MINING_TARGET_TEMP: float = 1e-10
    MINING_TARGET_CV: float = 1e-10
    BATCH_CANDIDATES: List[int] = field(default_factory=lambda: [8,16,32,64,128,256,512,1024])
    BATCH_PROSPECT_EPOCHS: int = 30
    BATCH_PROSPECT_SEED: int = 103
    LAMBDA_INITIAL: float = 1.0
    LAMBDA_MAX: float = 1e35
    LAMBDA_GROWTH_FACTOR: float = 10.0
    LAMBDA_GROWTH_INTERVAL_EPOCHS: int = 1000
    LAMBDA_PRECISION_DTYPE: str = 'float64'
    ANNEALING_INITIAL_TEMPERATURE: float = 1.0
    ANNEALING_FINAL_TEMPERATURE: float = 1e-6
    ANNEALING_COOLING_RATE: float = 0.995
    ANNEALING_RESTART_THRESHOLD: float = 0.01
    GROKKING_TRAIN_ACC_THRESHOLD: float = 0.99
    GROKKING_VAL_ACC_THRESHOLD: float = 0.95
    GROKKING_PATIENCE: int = 2000
    GROKKING_DELTA_SLOPE_WINDOW: int = 50
    GROKKING_DELTA_SLOPE_THRESHOLD: float = -1e-6
    BACKBONE_CHECKPOINT_PATH: str = 'weights/latest.pth'
    BACKBONE_ENABLED: bool = True
    LOG_INTERVAL_EPOCHS: int = 10
    NORMALIZATION_EPS: float = 1e-8
    POYNTING_OUTER_LIMIT: int = 50
    TORUS_GRID_SIZE: int = 16
    TOPO_ALIGNMENT_THRESHOLD: float = 0.7
    TOPO_HYSTERESIS_WIDTH: float = 0.1
    TOPO_COUPLING_STRENGTH: float = 0.5
    TOPO_LAMBDA_BASE: float = 1e20
    TOPO_LAMBDA_CRITICAL: float = 1e34
    TOPO_ALIGNMENT_HISTORY_LEN: int = 100
    TOPO_PHASE_SMOOTHING: float = 0.95
    TOPO_LOCALIZATION_LIQUID: float = 0.2
    TOPO_LOCALIZATION_CRYSTAL: float = 1.0
    TOPO_CRYSTALLIZATION_PRESSURE_DECAY: float = 0.999
    TOPO_ENABLED: bool = True
    FOURIER_MODE_COUPLING: float = 0.3
    FOURIER_DOMINANT_MODE_THRESHOLD: float = 0.5
    FOURIER_SPECTRAL_CONCENTRATION_THRESHOLD: float = 0.8
    FOURIER_PHASE_COHERENCE_THRESHOLD: float = 0.6
    PHASE5_LAMBDA_INITIAL: float = 1e30
    PHASE5_LAMBDA_MAX: float = 1e40
    PHASE5_LAMBDA_GROWTH_FACTOR: float = 2.0
    PHASE5_LAMBDA_GROWTH_INTERVAL_EPOCHS: int = 100
    PHASE5_PRECISION: str = 'float128'
    PHASE5_THERMAL_INJECTION_SCALE: float = 1e-5
    PHASE5_DELTA_TARGET: float = 0.001
    PHASE5_ALPHA_TARGET: float = 7.0
    PHASE5_ENABLE: bool = True
    PHASE5_CHECKPOINT_LATEST_PATH: str = 'weights/phase5_latest.pth'
    PHASE5_THERMAL_RESCALING_FACTOR: float = 1e10
    DELTA_CRYSTAL_THRESHOLD: float = 0.1
    DELTA_OPTICAL_THRESHOLD: float = 0.01
    KAPPA_CRYSTAL_THRESHOLD: float = 1.5
    TEMPERATURE_CRYSTAL_THRESHOLD: float = 1e-9
    GIBBS_T0: float = 1e-3
    GIBBS_C: float = 0.5
    GIBBS_FREE_ENERGY_WEIGHT: float = 0.1
    RICCI_CURVATURE_SAMPLES: int = 100
    RICCI_MAX_DIMENSION: int = 5000
    RICCI_SCALAR_WEIGHT: float = 0.05
    SPECTRAL_GAP_WEIGHT: float = 0.05
    PARTICIPATION_RATIO_WEIGHT: float = 0.05
    MBL_LEVEL_SPACING_WEIGHT: float = 0.05
    BRAGG_PEAK_HARMONIC_RATIO_THRESHOLD: float = 0.1
    WILLMORE_ENERGY_THRESHOLD: float = 0.01
    MEAN_CURVATURE_VARIANCE_THRESHOLD: float = 0.001
    SURFACE_AREA_CONSERVATION_WEIGHT: float = 0.1
    GAUSS_BONNET_INTEGRAL_TARGET: float = 4.0


class IPhaseDetector(ABC):
    @abstractmethod
    def detect(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        pass


class IMetricCalculator(ABC):
    @abstractmethod
    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        pass


class SeedManager:
    @staticmethod
    def set_seed(seed: int, device: str = None):
        if device is None:
            device = Config.DEVICE
        torch.manual_seed(seed)
        np.random.seed(seed)
        if device == 'cuda':
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False


class LoggerFactory:
    @staticmethod
    def create_logger(name: str, level: str = None) -> logging.Logger:
        if level is None:
            level = Config.LOG_LEVEL
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper()))
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger


class MinimalSurfaceOperator:
    def __init__(self, grid_size: int = None):
        if grid_size is None:
            grid_size = Config.GRID_SIZE
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

    def mean_curvature_flow(self, surface: torch.Tensor, dt: float = None) -> torch.Tensor:
        if dt is None:
            dt = Config.DT
        H = self.compute_mean_curvature(surface)
        evolved = surface - dt * H
        norm_original = torch.norm(surface) + Config.NORMALIZATION_EPS
        norm_evolved = torch.norm(evolved) + Config.NORMALIZATION_EPS
        return evolved / norm_evolved * norm_original


class SpectralLayer(nn.Module):
    def __init__(self, channels: int, grid_size: int):
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        self.kernel_real = nn.Parameter(torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1)
        self.kernel_imag = nn.Parameter(torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_fft = torch.fft.rfft2(x)
        batch, channels, freq_h, freq_w = x_fft.shape
        kernel_real = self.kernel_real.mean(dim=0)
        kernel_imag = self.kernel_imag.mean(dim=0)
        kernel_real_exp = kernel_real.unsqueeze(0).unsqueeze(0).squeeze(0)
        kernel_imag_exp = kernel_imag.unsqueeze(0).unsqueeze(0).squeeze(0)
        kernel_real_interp = F.interpolate(kernel_real_exp, size=(freq_h, freq_w), mode='bilinear', align_corners=False)
        kernel_imag_interp = F.interpolate(kernel_imag_exp, size=(freq_h, freq_w), mode='bilinear', align_corners=False)
        real_part = x_fft.real * kernel_real_interp - x_fft.imag * kernel_imag_interp
        imag_part = x_fft.real * kernel_imag_interp + x_fft.imag * kernel_real_interp
        output_fft = torch.complex(real_part, imag_part)
        output = torch.fft.irfft2(output_fft, s=(self.grid_size, self.grid_size))
        return output


class MinimalSurfaceBackbone(nn.Module):
    def __init__(self, grid_size: int = None, hidden_dim: int = None, num_spectral_layers: int = None):
        super().__init__()
        if grid_size is None: grid_size = Config.GRID_SIZE
        if hidden_dim is None: hidden_dim = Config.HIDDEN_DIM
        if num_spectral_layers is None: num_spectral_layers = Config.NUM_SPECTRAL_LAYERS
        self.grid_size = grid_size
        self.input_proj = nn.Conv2d(1, hidden_dim, kernel_size=1)
        self.spectral_layers = nn.ModuleList([SpectralLayer(hidden_dim, grid_size) for _ in range(num_spectral_layers)])
        self.output_proj = nn.Conv2d(hidden_dim, 1, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 2: x = x.unsqueeze(0).unsqueeze(0)
        elif x.dim() == 3: x = x.unsqueeze(1)
        x = F.gelu(self.input_proj(x))
        for spectral_layer in self.spectral_layers:
            x = F.gelu(spectral_layer(x))
        return self.output_proj(x).squeeze(1)


class MinimalSurfaceInferenceEngine:
    def __init__(self, config: Config):
        self.config = config
        self.logger = LoggerFactory.create_logger("MinimalSurfaceInferenceEngine")
        self.backbone = None
        self.fallback_operator = MinimalSurfaceOperator(config.GRID_SIZE)
        self._try_load_backbone()

    def _try_load_backbone(self):
        if not self.config.BACKBONE_ENABLED:
            self.logger.info("Backbone disabled, using analytical minimal surface operator")
            return
        checkpoint_path = self.config.BACKBONE_CHECKPOINT_PATH
        if not os.path.exists(checkpoint_path):
            self.logger.info(f"Backbone checkpoint not found at {checkpoint_path}, using analytical operator")
            return
        try:
            checkpoint = torch.load(checkpoint_path, map_location=self.config.DEVICE, weights_only=False)
            self.backbone = MinimalSurfaceBackbone(grid_size=self.config.GRID_SIZE, hidden_dim=self.config.HIDDEN_DIM, num_spectral_layers=self.config.NUM_SPECTRAL_LAYERS).to(self.config.DEVICE)
            if 'model_state_dict' in checkpoint:
                self.backbone.load_state_dict(checkpoint['model_state_dict'])
            else:
                self.backbone.load_state_dict(checkpoint)
            self.backbone.eval()
            for param in self.backbone.parameters():
                param.requires_grad = False
            self.logger.info(f"Backbone loaded from {checkpoint_path}")
        except Exception as e:
            self.logger.warning(f"Failed to load backbone: {e}, using analytical operator")
            self.backbone = None

    def apply_mean_curvature(self, surface: torch.Tensor) -> torch.Tensor:
        if self.backbone is not None:
            with torch.no_grad():
                return self.backbone(surface.to(self.config.DEVICE))
        return self.fallback_operator.compute_mean_curvature(surface)

    def mean_curvature_evolve(self, surface: torch.Tensor, dt: float = None) -> torch.Tensor:
        if dt is None: dt = Config.DT
        if self.backbone is not None:
            with torch.no_grad():
                evolved = self.backbone(surface.to(self.config.DEVICE))
                norm_original = torch.norm(surface) + Config.NORMALIZATION_EPS
                norm_evolved = torch.norm(evolved) + Config.NORMALIZATION_EPS
                return evolved / norm_evolved * norm_original
        return self.fallback_operator.mean_curvature_flow(surface, dt)


class SurfacePotentialGenerator:
    def __init__(self, config: Config):
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
        potentials = [self.pyramid_potential(), self.cube_potential(), self.dodecahedron_potential(), self.torus_potential(), self.hyperbolic_potential()]
        result = torch.zeros(self.grid_size, self.grid_size)
        for w, v in zip(weights, potentials):
            result += w * v
        return result


class MinimalSurfaceDataset(Dataset):
    def __init__(self, config: Config, surface_engine: MinimalSurfaceInferenceEngine, seed: int = None):
        if seed is None: seed = Config.RANDOM_SEED
        self.config = config
        self.num_samples = config.NUM_SAMPLES
        self.grid_size = config.GRID_SIZE
        self.train_ratio = config.TRAIN_RATIO
        self.surface_engine = surface_engine
        self.potential_generator = SurfacePotentialGenerator(config)
        torch.manual_seed(seed)
        np.random.seed(seed)
        self.initial_surfaces, self.target_surfaces, self.potentials = [], [], []
        self.energies, self.willmore_energies = [], []
        for i in range(self.num_samples):
            potential = self.potential_generator.generate_mixed_potential(seed + i)
            surface_real, surface_imag, energy = self._solve_minimal_surface(potential, seed + i)
            initial = torch.stack([surface_real, surface_imag], dim=0)
            evolved_real, evolved_imag, willmore_e = self._evolve_minimal_surface(surface_real, surface_imag, potential, energy)
            target = torch.stack([evolved_real, evolved_imag], dim=0)
            self.initial_surfaces.append(initial)
            self.target_surfaces.append(target)
            self.potentials.append(potential)
            self.energies.append(energy)
            self.willmore_energies.append(willmore_e)
        self.initial_surfaces = torch.stack(self.initial_surfaces)
        self.target_surfaces = torch.stack(self.target_surfaces)
        self.potentials = torch.stack(self.potentials)
        self.energies = torch.tensor(self.energies)
        self.willmore_energies = torch.tensor(self.willmore_energies)
        split_idx = int(self.num_samples * self.train_ratio)
        self.train_surfaces = self.initial_surfaces[:split_idx]
        self.train_targets = self.target_surfaces[:split_idx]
        self.val_surfaces = self.initial_surfaces[split_idx:]
        self.val_targets = self.target_surfaces[split_idx:]

    def _solve_minimal_surface(self, potential: torch.Tensor, sample_seed: int) -> Tuple[torch.Tensor, torch.Tensor, float]:
        h_field = self.surface_engine.apply_mean_curvature(torch.randn(self.grid_size, self.grid_size))
        if h_field.dim() > 2: h_field = h_field.squeeze()
        surface_op = MinimalSurfaceOperator(self.grid_size)
        kinetic = -0.5 * h_field
        hamiltonian_matrix = kinetic + potential
        try:
            eigenvalues, eigenvectors = torch.linalg.eigh(hamiltonian_matrix)
        except Exception:
            eigenvalues = torch.zeros(self.grid_size)
            eigenvectors = torch.eye(self.grid_size)
        rng = np.random.RandomState(sample_seed)
        n_states = min(self.config.NUM_EIGENMODES, self.grid_size)
        state_idx = rng.randint(0, n_states)
        energy = eigenvalues[state_idx].item() * self.config.ENERGY_SCALE
        psi_column = eigenvectors[:, state_idx]
        psi_2d = psi_column.unsqueeze(1).expand(-1, self.grid_size)
        perturbation = torch.randn_like(psi_2d) * 0.1
        psi_2d = psi_2d + perturbation
        norm = torch.sqrt(torch.sum(psi_2d**2)) + Config.NORMALIZATION_EPS
        psi_2d = psi_2d / norm * self.config.SURFACE_AREA_TARGET
        phase = torch.randn(self.grid_size, self.grid_size) * 0.5
        psi_real = psi_2d * torch.cos(phase)
        psi_imag = psi_2d * torch.sin(phase)
        return psi_real, psi_imag, energy

    def _evolve_minimal_surface(self, surface_real: torch.Tensor, surface_imag: torch.Tensor, potential: torch.Tensor, energy: float) -> Tuple[torch.Tensor, torch.Tensor, float]:
        dt = self.config.DT
        surface_op = MinimalSurfaceOperator(self.grid_size)
        willmore_e = 0.0
        for _ in range(self.config.TIME_STEPS):
            h_real = self.surface_engine.apply_mean_curvature(surface_real)
            if h_real.dim() > 2: h_real = h_real.squeeze()
            h_imag = self.surface_engine.apply_mean_curvature(surface_imag)
            if h_imag.dim() > 2: h_imag = h_imag.squeeze()
            kinetic_real, kinetic_imag = -0.5 * h_real, -0.5 * h_imag
            total_h_real = kinetic_real + potential * surface_real
            total_h_imag = kinetic_imag + potential * surface_imag
            new_real = surface_real + dt * total_h_imag
            new_imag = surface_imag - dt * total_h_real
            norm = torch.sqrt(torch.sum(new_real**2 + new_imag**2)) + Config.NORMALIZATION_EPS
            target_norm = torch.sqrt(torch.sum(surface_real**2 + surface_imag**2)) + Config.NORMALIZATION_EPS
            new_real, new_imag = new_real / norm * target_norm, new_imag / norm * target_norm
            surface_real, surface_imag = new_real, new_imag
        willmore_e = surface_op.compute_willmore_energy(surface_real).item()
        return surface_real, surface_imag, willmore_e

    def __len__(self): return len(self.train_surfaces)
    def __getitem__(self, idx): return self.train_surfaces[idx], self.train_targets[idx]
    def get_validation_batch(self) -> Tuple[torch.Tensor, torch.Tensor]: return self.val_surfaces, self.val_targets


class MinimalSurfaceSpectralNetwork(nn.Module):
    def __init__(self, grid_size: int = None, hidden_dim: int = None, expansion_dim: int = None, num_spectral_layers: int = None, input_channels: int = None, output_channels: int = None):
        super().__init__()
        if grid_size is None: grid_size = Config.GRID_SIZE
        if hidden_dim is None: hidden_dim = Config.HIDDEN_DIM
        if expansion_dim is None: expansion_dim = Config.EXPANSION_DIM
        if num_spectral_layers is None: num_spectral_layers = Config.NUM_SPECTRAL_LAYERS
        if input_channels is None: input_channels = Config.SURFACE_CHANNELS
        if output_channels is None: output_channels = Config.SURFACE_CHANNELS
        self.grid_size = grid_size
        self.input_channels = input_channels
        self.output_channels = output_channels
        self.input_proj = nn.Conv2d(input_channels, hidden_dim, kernel_size=1)
        self.expansion_proj = nn.Conv2d(hidden_dim, expansion_dim, kernel_size=1)
        self.spectral_layers = nn.ModuleList([SpectralLayer(expansion_dim, grid_size) for _ in range(num_spectral_layers)])
        self.contraction_proj = nn.Conv2d(expansion_dim, hidden_dim, kernel_size=1)
        self.output_proj = nn.Conv2d(hidden_dim, output_channels, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 3: x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = F.gelu(self.expansion_proj(x))
        for spectral_layer in self.spectral_layers:
            x = F.gelu(spectral_layer(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)


class WillmoreEnergyCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config
        self.surface_op = MinimalSurfaceOperator(config.GRID_SIZE)
        self.logger = LoggerFactory.create_logger("WillmoreEnergyCalculator")

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
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
        return self.compute_surface_metrics(surface)

    def compute_surface_metrics(self, surface: torch.Tensor) -> Dict[str, Any]:
        try:
            mean_curvature = self.surface_op.compute_mean_curvature(surface)
            gaussian_curvature = self.surface_op.compute_gaussian_curvature(surface)
            willmore_energy = self.surface_op.compute_willmore_energy(surface)
            surface_area = self.surface_op.compute_surface_area(surface)
            mean_curvature_mean = mean_curvature.mean().item()
            mean_curvature_var = mean_curvature.var().item()
            gaussian_curvature_mean = gaussian_curvature.mean().item()
            total_gaussian = torch.sum(gaussian_curvature).item() / self.config.GRID_SIZE**2
            is_minimal_surface = abs(mean_curvature_mean) < self.config.WILLMORE_ENERGY_THRESHOLD
            is_crystalline_surface = willmore_energy.item() < self.config.WILLMORE_ENERGY_THRESHOLD and mean_curvature_var < self.config.MEAN_CURVATURE_VARIANCE_THRESHOLD
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
        except Exception as e:
            self.logger.debug(f"Surface metrics computation failed: {e}")
            return self._empty_metrics()

    @staticmethod
    def _empty_metrics() -> Dict[str, Any]:
        return {'willmore_energy': 0.0, 'mean_curvature_mean': 0.0, 'mean_curvature_var': 0.0, 'gaussian_curvature_mean': 0.0, 'total_gaussian_curvature': 0.0, 'surface_area': 0.0, 'is_minimal_surface': 0.0, 'is_crystalline_surface': 0.0, 'curvature_ratio': 0.0}


class RicciFlowCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config
        self.logger = LoggerFactory.create_logger("RicciFlowCalculator")

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        n = min(len(all_weights), self.config.PARAM_FLATTEN_LIMIT)
        w = all_weights[:n].cpu().numpy()
        if n < 2:
            return self._empty_metrics()
        metric_tensor = np.outer(w, w) / n
        metric_tensor += np.eye(n) * self.config.EIGENVALUE_TOL
        ricci_scalar = self._compute_ricci_scalar(metric_tensor)
        sectional_curvatures = self._estimate_sectional_curvatures(metric_tensor)
        flow_velocity = self._compute_flow_velocity(metric_tensor)
        return {'ricci_scalar': float(ricci_scalar), 'mean_sectional_curvature': float(np.mean(sectional_curvatures)), 'ricci_flow_velocity': float(flow_velocity), 'curvature_std': float(np.std(sectional_curvatures))}

    def _compute_ricci_scalar(self, metric: np.ndarray) -> float:
        eigenvalues = np.linalg.eigvalsh(metric)
        eigenvalues = eigenvalues[eigenvalues > self.config.EIGENVALUE_TOL]
        n = len(eigenvalues)
        if n < 2: return 0.0
        return float(n * np.sum(1.0 / eigenvalues))

    def _estimate_sectional_curvatures(self, metric: np.ndarray) -> np.ndarray:
        curvatures = []
        n = metric.shape[0]
        samples = min(self.config.RICCI_CURVATURE_SAMPLES, n * (n - 1) // 2)
        for _ in range(samples):
            i, j = np.random.choice(n, 2, replace=False)
            block = metric[np.ix_([i, j], [i, j])]
            det = np.linalg.det(block)
            if det > self.config.EIGENVALUE_TOL:
                curvatures.append(1.0 / det)
        return np.array(curvatures) if curvatures else np.array([0.0])

    def _compute_flow_velocity(self, metric: np.ndarray) -> float:
        n = metric.shape[0]
        return float(np.trace(metric) / n)

    @staticmethod
    def _empty_metrics() -> Dict[str, Any]:
        return {'ricci_scalar': 0.0, 'mean_sectional_curvature': 0.0, 'ricci_flow_velocity': 0.0, 'curvature_std': 0.0}


class FullFourierAnalyzer:
    def __init__(self, config: Config):
        self.config = config
        self.grid_size = config.TORUS_GRID_SIZE
        kx = torch.fft.fftfreq(self.grid_size) * 2 * np.pi
        ky = torch.fft.fftfreq(self.grid_size) * 2 * np.pi
        self.KX, self.KY = torch.meshgrid(kx, ky, indexing='ij')
        self.K_MAG = torch.sqrt(self.KX**2 + self.KY**2)

    def compute_full_spectrum(self, spectral_field: torch.Tensor) -> Dict[str, torch.Tensor]:
        if spectral_field.dim() == 3: spectral_field = spectral_field.unsqueeze(0)
        B, C, H, W = spectral_field.shape
        device = spectral_field.device
        fft_2d = torch.fft.fft2(spectral_field, dim=(-2, -1))
        fft_shifted = torch.fft.fftshift(fft_2d, dim=(-2, -1))
        magnitude = torch.abs(fft_shifted)
        phase = torch.angle(fft_shifted)
        power_spectrum = magnitude**2
        power_spectrum_sum = power_spectrum.sum(dim=(-2, -1), keepdim=True) + 1e-10
        power_normalized = power_spectrum / power_spectrum_sum
        total_power = power_spectrum.sum(dim=(-2, -1))
        mean_power = power_spectrum.mean(dim=(-2, -1))
        std_power = power_spectrum.std(dim=(-2, -1))
        spectral_concentration = (power_spectrum.max(dim=-1)[0].max(dim=-1)[0]) / (total_power + 1e-10)
        center = H // 2
        low_freq_power = power_spectrum[:, :, center-2:center+3, center-2:center+3].sum(dim=(-2, -1))
        low_freq_ratio = low_freq_power / (total_power + 1e-10)
        high_freq_ratio = 1.0 - low_freq_ratio
        phase_flat = phase.view(B, C, -1)
        phase_mean = torch.atan2(torch.sin(phase_flat).mean(dim=-1), torch.cos(phase_flat).mean(dim=-1))
        phase_coherence = torch.abs(torch.cos(phase_flat - phase_mean.unsqueeze(-1))).mean(dim=-1)
        return {'fft_2d': fft_shifted, 'magnitude': magnitude, 'phase': phase, 'power_spectrum': power_spectrum, 'power_normalized': power_normalized, 'spectral_concentration': spectral_concentration, 'low_freq_ratio': low_freq_ratio, 'high_freq_ratio': high_freq_ratio, 'phase_coherence': phase_coherence, 'total_power': total_power, 'mean_power': mean_power, 'std_power': std_power}

    def compute_resonance_metrics(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        spectrum = self.compute_full_spectrum(spectral_field)
        spectral_conc = spectrum['spectral_concentration'].mean().item()
        low_freq_ratio = spectrum['low_freq_ratio'].mean().item()
        phase_coherence = spectrum['phase_coherence'].mean().item()
        resonance_score = spectral_conc * 0.3 + phase_coherence * 0.3 + min(low_freq_ratio * 2, 1.0) * 0.2 + 0.2
        is_resonant = spectral_conc > self.config.FOURIER_SPECTRAL_CONCENTRATION_THRESHOLD and phase_coherence > self.config.FOURIER_PHASE_COHERENCE_THRESHOLD
        return {'spectral_concentration': spectral_conc, 'low_freq_ratio': low_freq_ratio, 'phase_coherence': phase_coherence, 'resonance_score': resonance_score, 'is_resonant': is_resonant}


class FourierMassCenterAnalyzer:
    def __init__(self, config: Config):
        self.config = config
        self.grid_size = config.TORUS_GRID_SIZE
        self.full_fourier = FullFourierAnalyzer(config)
        self._cached_KX = None
        self._cached_KY = None
        self._cached_shape = None

    def _get_freq_grids(self, H: int, W: int, device: torch.device):
        if self._cached_shape != (H, W) or self._cached_KX is None:
            kx = torch.fft.fftfreq(H) * 2 * np.pi
            ky = torch.fft.fftfreq(W) * 2 * np.pi
            self._cached_KX, self._cached_KY = torch.meshgrid(kx, ky, indexing='ij')
            self._cached_shape = (H, W)
        return self._cached_KX.to(device), self._cached_KY.to(device)

    def compute_mass_center(self, spectral_field: torch.Tensor) -> Dict[str, torch.Tensor]:
        if spectral_field.dim() == 3: spectral_field = spectral_field.unsqueeze(0)
        B, C, H, W = spectral_field.shape
        device = spectral_field.device
        kx, ky = self._get_freq_grids(H, W, device)
        density = torch.abs(spectral_field)**2
        density = density.mean(dim=1)
        total_mass = density.sum(dim=(-2, -1), keepdim=True) + 1e-10
        R_x = (kx * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        R_y = (ky * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        dx = kx - R_x.view(-1, 1, 1)
        dy = ky - R_y.view(-1, 1, 1)
        I_xx = (dx**2 * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        I_yy = (dy**2 * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        I_xy = (dx * dy * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        inertia_tensor = torch.stack([torch.stack([I_xx, I_xy], dim=-1), torch.stack([I_xy, I_yy], dim=-1)], dim=-2)
        eigenvalues = torch.linalg.eigvalsh(inertia_tensor)
        anisotropy = eigenvalues[..., 0] / (eigenvalues[..., 1] + 1e-10)
        left_alignment = (R_x < -0.5).float()
        resonance = self.full_fourier.compute_resonance_metrics(spectral_field)
        return {'R_cm': torch.stack([R_x, R_y], dim=-1), 'inertia_tensor': inertia_tensor, 'eigenvalues': eigenvalues, 'anisotropy': anisotropy, 'left_alignment': left_alignment, 'localization_index': 1.0 - anisotropy, 'total_mass': total_mass.squeeze(), 'resonance_score': resonance['resonance_score'], 'is_resonant': resonance['is_resonant'], 'phase_coherence': resonance['phase_coherence'], 'spectral_concentration': resonance['spectral_concentration']}


class TopologicalPhaseDetector(IPhaseDetector):
    def __init__(self, config: Config):
        self.config = config
        self.mass_analyzer = FourierMassCenterAnalyzer(config)
        self.phase_state = 0.0
        self.alignment_history = np.zeros(config.TOPO_ALIGNMENT_HISTORY_LEN)
        self.history_ptr = 0

    def detect(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        mass_analysis = self.mass_analyzer.compute_mass_center(spectral_field)
        R_cm = mass_analysis['R_cm']
        localization = mass_analysis['localization_index']
        alignment = mass_analysis['left_alignment']
        resonance_score = mass_analysis['resonance_score']
        phase_coherence = mass_analysis['phase_coherence']
        spectral_conc = mass_analysis['spectral_concentration']
        alignment_val = alignment.mean().item() if alignment.dim() > 0 else alignment.item()
        self.alignment_history[self.history_ptr] = alignment_val
        self.history_ptr = (self.history_ptr + 1) % len(self.alignment_history)
        loc_mean = localization.mean().item() if localization.dim() > 0 else localization.item()
        is_aligned = float(alignment_val > self.config.TOPO_ALIGNMENT_THRESHOLD)
        is_localized = float(loc_mean > 0.8)
        is_resonant = float(resonance_score > 0.6)
        transition_prob = is_aligned * is_localized * is_resonant
        alpha = self.config.TOPO_PHASE_SMOOTHING
        self.phase_state = alpha * self.phase_state + (1 - alpha) * transition_prob
        return {'R_cm': R_cm.detach(), 'R_cm_x': float(R_cm[..., 0].mean().item()), 'R_cm_y': float(R_cm[..., 1].mean().item()), 'localization_index': float(loc_mean), 'alignment_score': float(alignment_val), 'anisotropy': float(mass_analysis['anisotropy'].mean().item()), 'phase_state': float(self.phase_state), 'is_crystalline': float(self.phase_state > 0.7), 'transition_probability': float(transition_prob), 'resonance_score': float(resonance_score), 'is_resonant': mass_analysis['is_resonant'], 'phase_coherence': float(phase_coherence), 'spectral_concentration': float(spectral_conc)}


class SpectralFieldExtractor:
    @staticmethod
    def extract(model: nn.Module, grid_size: int = 16) -> Optional[torch.Tensor]:
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
        if not spectral_weights:
            return None
        return torch.stack(spectral_weights).mean(dim=0)


class TopologicalMetricsCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config
        self.phase_detector = TopologicalPhaseDetector(config)
        self.field_extractor = SpectralFieldExtractor()

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        if not self.config.TOPO_ENABLED:
            return self._empty_metrics()
        spectral_field = self.field_extractor.extract(model, self.config.GRID_SIZE)
        if spectral_field is None:
            return self._empty_metrics()
        phase_info = self.phase_detector.detect(spectral_field)
        return {'topo_R_cm_x': phase_info['R_cm_x'], 'topo_R_cm_y': phase_info['R_cm_y'], 'topo_localization': phase_info['localization_index'], 'topo_alignment': phase_info['alignment_score'], 'topo_anisotropy': phase_info['anisotropy'], 'topo_phase_state': phase_info['phase_state'], 'topo_is_crystalline': phase_info['is_crystalline'], 'topo_transition_prob': phase_info['transition_probability'], 'topo_resonance_score': phase_info['resonance_score'], 'topo_is_resonant': float(phase_info['is_resonant']), 'topo_phase_coherence': phase_info['phase_coherence'], 'topo_spectral_conc': phase_info['spectral_concentration'], '_phase_info': phase_info}

    @staticmethod
    def _empty_metrics() -> Dict[str, Any]:
        return {'topo_R_cm_x': 0.0, 'topo_R_cm_y': 0.0, 'topo_localization': 0.0, 'topo_alignment': 0.0, 'topo_anisotropy': 1.0, 'topo_phase_state': 0.0, 'topo_is_crystalline': 0.0, 'topo_transition_prob': 0.0, 'topo_resonance_score': 0.0, 'topo_is_resonant': 0.0, 'topo_phase_coherence': 0.0, 'topo_spectral_conc': 0.0, '_phase_info': None}


class LocalComplexityAnalyzer:
    @staticmethod
    def compute_local_complexity(weights: torch.Tensor, epsilon: float = 1e-6) -> float:
        if weights.numel() == 0: return 0.0
        w = weights.detach().flatten()
        w = w / (torch.norm(w) + epsilon)
        w_expanded = w.unsqueeze(0)
        similarities = F.cosine_similarity(w_expanded, w_expanded.unsqueeze(1), dim=2)
        mask = ~torch.eye(similarities.size(0), device=similarities.device, dtype=torch.bool)
        if mask.sum() == 0: return 0.0
        avg_similarity = (similarities.abs() * mask).sum() / mask.sum()
        lc = 1.0 - avg_similarity.item()
        return max(0.0, min(1.0, lc))


class SuperpositionAnalyzer:
    @staticmethod
    def compute_superposition(weights: torch.Tensor) -> float:
        w = weights.detach()
        if w.dim() > 2: w = w.reshape(w.size(0), -1)
        if w.size(0) < 2 or w.size(1) < 2: return 0.0
        try:
            correlation_matrix = torch.corrcoef(w)
            correlation_matrix = correlation_matrix.nan_to_num(nan=0.0)
            n = correlation_matrix.size(0)
            mask = ~torch.eye(n, device=correlation_matrix.device, dtype=torch.bool)
            if mask.sum() == 0: return 0.0
            avg_correlation = (correlation_matrix.abs() * mask).sum() / mask.sum()
            return avg_correlation.item()
        except Exception:
            return 0.0


class CrystallographyMetricsCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config
        self.logger = LoggerFactory.create_logger("CrystallographyMetrics")

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        val_x = kwargs.get('val_x')
        val_y = kwargs.get('val_y')
        return self.compute_all_metrics(model, val_x, val_y)

    def compute_kappa(self, model: nn.Module, val_x: torch.Tensor, val_y: torch.Tensor, num_batches: int = None) -> float:
        if num_batches is None: num_batches = self.config.KAPPA_GRADIENT_BATCHES
        model.eval()
        grads = []
        for i in range(num_batches):
            try:
                model.zero_grad()
                noise_scale = self.config.NOISE_AMPLITUDE * (i + 1) / num_batches
                val_x_perturbed = val_x + torch.randn_like(val_x) * noise_scale
                outputs = model(val_x_perturbed)
                loss = F.mse_loss(outputs, val_y)
                loss.backward()
                grad_list = []
                for p in model.parameters():
                    if p.grad is not None and p.grad.numel() > 0:
                        grad_list.append(p.grad.flatten())
                if grad_list:
                    grad_vector = torch.cat(grad_list)
                    if torch.isfinite(grad_vector).all():
                        grads.append(grad_vector.detach())
            except Exception:
                continue
        if len(grads) < 2: return float('inf')
        grads_tensor = torch.stack(grads)
        n_samples, n_dims = grads_tensor.shape
        if n_dims > self.config.KAPPA_MAX_DIM:
            indices = torch.randperm(n_dims, device=grads_tensor.device)[:self.config.KAPPA_MAX_DIM]
            grads_tensor = grads_tensor[:, indices]
            n_dims = self.config.KAPPA_MAX_DIM
        try:
            if n_samples < n_dims:
                gram = torch.mm(grads_tensor, grads_tensor.t()) / max(n_samples - 1, 1)
                eigenvals = torch.linalg.eigvalsh(gram)
            else:
                cov = torch.cov(grads_tensor.t())
                eigenvals = torch.linalg.eigvalsh(cov).real
            eigenvals = eigenvals[eigenvals > self.config.EIGENVALUE_TOL]
            if len(eigenvals) == 0: return float('inf')
            return (eigenvals.max() / eigenvals.min()).item()
        except Exception:
            return float('inf')

    def compute_discretization_margin(self, model: nn.Module) -> float:
        margins = []
        for param in model.parameters():
            if param.numel() > 0:
                margin = (param.data - param.data.round()).abs().max().item()
                margins.append(margin)
        return max(margins) if margins else 0.0

    def compute_alpha_purity(self, model: nn.Module) -> float:
        delta = self.compute_discretization_margin(model)
        if delta < self.config.MIN_VARIANCE_THRESHOLD: return 20.0
        return -np.log(delta + self.config.ENTROPY_EPS)

    def compute_kappa_quantum(self, model: nn.Module) -> float:
        flat_params = []
        for param in model.parameters():
            if param.numel() > 0:
                flat_params.append(param.data.detach().flatten())
        if not flat_params: return 1.0
        W = torch.cat(flat_params)[:self.config.KAPPA_MAX_DIM]
        n = W.numel()
        if n < 2: return 1.0
        params_centered = W - W.mean()
        cov_matrix = torch.outer(params_centered, params_centered) / n
        cov_matrix = cov_matrix + self.config.HBAR * torch.eye(n, device=W.device)
        try:
            eigenvals = torch.linalg.eigvalsh(cov_matrix)
            eigenvals = eigenvals[eigenvals > self.config.HBAR]
            return (eigenvals.max() / eigenvals.min()).item() if len(eigenvals) > 0 else 1.0
        except Exception:
            return 1.0

    def compute_poynting_vector(self, model: nn.Module) -> Dict[str, Any]:
        all_params = []
        for param in model.parameters():
            if param is not None and param.numel() > 0:
                all_params.append(param.data.detach().flatten())
        if not all_params:
            return {'poynting_magnitude': 0.0, 'energy_distribution': {}, 'is_radiating': False, 'field_orthogonality': 0.0}
        E = torch.cat(all_params)[:self.config.PARAM_FLATTEN_LIMIT]
        poynting_magnitude = torch.norm(E) * self.config.ENERGY_FLOW_SCALE
        return {'poynting_magnitude': float(poynting_magnitude.item()), 'energy_distribution': {'total_norm': float(torch.norm(E).item())}, 'is_radiating': float(poynting_magnitude.item()) > self.config.POYNTING_THRESHOLD, 'field_orthogonality': 0.0}

    def compute_hbar_effective(self, model: nn.Module, lambda_pressure: float) -> float:
        delta = self.compute_discretization_margin(model)
        if lambda_pressure <= 0: return 0.0
        omega = math.sqrt(abs(lambda_pressure))
        if omega < self.config.NORMALIZATION_EPS: return 0.0
        return (delta**2 * lambda_pressure) / omega

    def compute_all_metrics(self, model: nn.Module, val_x: torch.Tensor, val_y: torch.Tensor) -> Dict[str, Any]:
        try:
            delta = self.compute_discretization_margin(model)
            alpha = self.compute_alpha_purity(model)
        except Exception:
            delta, alpha = 1.0, 0.0
        kappa = self.compute_kappa(model, val_x, val_y) if val_x is not None else float('inf')
        kappa_q = self.compute_kappa_quantum(model)
        poynting = self.compute_poynting_vector(model)
        return {'kappa': kappa, 'delta': delta, 'alpha': alpha, 'kappa_q': kappa_q, 'poynting': poynting, 'purity_index': 1.0 - delta, 'is_crystal': alpha > self.config.ALPHA_CRYSTAL_THRESHOLD, 'energy_flow': poynting.get('poynting_magnitude', 0.0)}


class ThermodynamicMetricsCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        gradient_buffer = kwargs.get('gradient_buffer', [])
        learning_rate = kwargs.get('learning_rate', self.config.LEARNING_RATE)
        loss_history = kwargs.get('loss_history', [])
        temp_history = kwargs.get('temp_history', [])
        delta = kwargs.get('delta', 1.0)
        alpha = kwargs.get('alpha', 0.0)
        temperature = self.compute_effective_temperature(gradient_buffer, learning_rate)
        cv, is_transition = self.compute_specific_heat(loss_history, temp_history)
        gibbs_free_energy = self.compute_gibbs_free_energy(delta, alpha, temperature)
        critical_temp = self.compute_critical_temperature(alpha)
        phase_stability_numeric = 1 if temperature < critical_temp else 0
        return {'temperature': temperature, 'specific_heat': cv, 'is_phase_transition': is_transition, 'gibbs_free_energy': gibbs_free_energy, 'critical_temperature': critical_temp, 'phase_stability': phase_stability_numeric}

    def compute_effective_temperature(self, gradient_buffer: Any, learning_rate: float) -> float:
        buf = list(gradient_buffer) if not isinstance(gradient_buffer, list) else gradient_buffer
        if len(buf) < 2: return 0.0
        grads = []
        for g in buf[-self.config.GRADIENT_BUFFER_WINDOW:]:
            flat = g.detach().flatten()
            if flat.numel() > 0:
                grads.append(flat[:self.config.GRADIENT_BUFFER_LIMIT])
        if not grads: return 0.0
        try:
            grads_stacked = torch.stack(grads)
            second_moment = torch.mean(torch.norm(grads_stacked, dim=1)**2)
            first_moment_sq = torch.norm(torch.mean(grads_stacked, dim=0))**2
            variance = second_moment - first_moment_sq
            return float((learning_rate / 2.0) * variance)
        except Exception:
            return 0.0

    def compute_specific_heat(self, loss_history: Any, temp_history: Any) -> Tuple[float, bool]:
        l_hist = list(loss_history) if not isinstance(loss_history, list) else loss_history
        t_hist = list(temp_history) if not isinstance(temp_history, list) else temp_history
        if len(l_hist) < 2 or len(t_hist) < 2: return 0.0, False
        u_var = np.var(l_hist[-self.config.LOSS_HISTORY_WINDOW:])
        t_mean = np.mean(t_hist[-self.config.LOSS_HISTORY_WINDOW:]) + self.config.NORMALIZATION_EPS
        cv = u_var / (t_mean**2)
        return float(cv), cv > self.config.CV_THRESHOLD

    def compute_gibbs_free_energy(self, delta: float, alpha: float, temperature: float) -> float:
        internal_energy = delta
        entropy_proxy = -alpha
        if temperature > 0:
            return internal_energy - temperature * entropy_proxy
        return internal_energy

    def compute_critical_temperature(self, alpha: float) -> float:
        return self.config.GIBBS_T0 * np.exp(-self.config.GIBBS_C * alpha)


class SpectralGeometryCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        all_weights = all_weights[:self.config.PARAM_FLATTEN_LIMIT].cpu().numpy()
        n = len(all_weights)
        if n < 2:
            return {'spectral_gap': 0.0, 'effective_dimension': 0, 'participation_ratio': 0.0, 'level_spacing_ratio': 0.0}
        outer_product = np.outer(all_weights, all_weights) / n
        outer_product += np.eye(n) * self.config.EIGENVALUE_TOL
        try:
            eigenvalues = np.linalg.eigvalsh(outer_product)
            eigenvalues = np.sort(eigenvalues)[::-1]
            effective_dim = np.sum(eigenvalues > self.config.EIGENVALUE_TOL)
            spectral_gap = float(eigenvalues[0] - eigenvalues[1]) if len(eigenvalues) > 1 else 0.0
            participation_ratio = float((np.sum(eigenvalues)**2) / (np.sum(eigenvalues**2) + 1e-10))
            return {'spectral_gap': spectral_gap, 'effective_dimension': int(effective_dim), 'participation_ratio': participation_ratio, 'level_spacing_ratio': 0.0}
        except Exception:
            return {'spectral_gap': 0.0, 'effective_dimension': 0, 'participation_ratio': 0.0, 'level_spacing_ratio': 0.0}


class RicciCurvatureCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        n = min(len(all_weights), self.config.PARAM_FLATTEN_LIMIT)
        w = all_weights[:n].cpu().numpy()
        if n < 2:
            return {'ricci_scalar': 0.0, 'mean_sectional_curvature': 0.0}
        metric_tensor = np.outer(w, w) / n
        metric_tensor += np.eye(n) * self.config.EIGENVALUE_TOL
        eigenvalues = np.linalg.eigvalsh(metric_tensor)
        eigenvalues = eigenvalues[eigenvalues > self.config.EIGENVALUE_TOL]
        n_eig = len(eigenvalues)
        if n_eig < 2:
            return {'ricci_scalar': 0.0, 'mean_sectional_curvature': 0.0}
        ricci_scalar = float(n_eig * np.sum(1.0 / eigenvalues))
        return {'ricci_scalar': ricci_scalar, 'mean_sectional_curvature': 0.0}


class SpectroscopyMetricsCalculator(IMetricCalculator):
    def __init__(self, config: Config):
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        coeffs = {name: param.data for name, param in model.named_parameters()}
        W = torch.cat([c.detach().flatten()[:self.config.PARAM_FLATTEN_LIMIT] for c in coeffs.values()])
        fft_spectrum = torch.fft.fft(W)
        power_spectrum = torch.abs(fft_spectrum)**2
        threshold = torch.mean(power_spectrum) + 2 * torch.std(power_spectrum)
        num_peaks = (power_spectrum > threshold).sum().item()
        ps_normalized = power_spectrum / (torch.sum(power_spectrum) + 1e-10)
        ps_normalized = ps_normalized[ps_normalized > 1e-10]
        spectral_entropy = -torch.sum(ps_normalized * torch.log(ps_normalized + 1e-10)) if len(ps_normalized) > 0 else torch.tensor(0.0)
        return {'bragg_peaks': [], 'is_crystalline_structure': num_peaks > 0, 'spectral_entropy': float(spectral_entropy.item()), 'num_peaks': int(num_peaks)}


class LambdaPressureScheduler:
    def __init__(self, config: Config):
        self.config = config
        self._lambda = np.float64(config.LAMBDA_INITIAL)
        self._lambda_max = np.float64(config.LAMBDA_MAX)
        self._growth_factor = np.float64(config.LAMBDA_GROWTH_FACTOR)
        self._growth_interval = config.LAMBDA_GROWTH_INTERVAL_EPOCHS
        self.logger = LoggerFactory.create_logger("LambdaPressureScheduler")

    @property
    def current_lambda(self) -> np.float64:
        return self._lambda

    def step(self, epoch: int):
        if epoch > 0 and epoch % self._growth_interval == 0:
            new_lambda = self._lambda * self._growth_factor
            if new_lambda <= self._lambda_max:
                self._lambda = np.float64(new_lambda)
                self.logger.info(f"Lambda pressure increased to {self._lambda:.6e} at epoch {epoch}")

    def compute_regularization_loss(self, model: nn.Module) -> torch.Tensor:
        delta = torch.tensor(0.0, device=self.config.DEVICE)
        for param in model.parameters():
            if param.numel() > 0:
                margin = (param - param.round()).abs().max()
                delta = torch.max(delta, margin)
        return delta * float(self._lambda)

    def set_lambda(self, value: float):
        self._lambda = np.float64(value)


class AdaptiveLambdaScheduler(LambdaPressureScheduler):
    def __init__(self, config: Config):
        super().__init__(config)
        self._base_growth_factor = np.float64(config.LAMBDA_GROWTH_FACTOR)
        self._accelerated_growth_factor = np.float64(config.LAMBDA_GROWTH_FACTOR * 2.0)

    def step_adaptive(self, epoch: int, topo_phase_state: float = 0.0):
        if epoch > 0 and epoch % self._growth_interval == 0:
            growth = self._accelerated_growth_factor if topo_phase_state > 0.5 else self._base_growth_factor
            new_lambda = self._lambda * growth
            if new_lambda <= self._lambda_max:
                self._lambda = np.float64(new_lambda)
                self.logger.info(f"Lambda pressure {'(ACCELERATED) ' if topo_phase_state > 0.5 else ''}increased to {self._lambda:.6e} at epoch {epoch}")


class QuadruplePrecisionLambdaScheduler:
    def __init__(self, config: Config):
        self.config = config
        self._lambda = np.longdouble(str(config.PHASE5_LAMBDA_INITIAL))
        self._lambda_max = np.longdouble(str(config.PHASE5_LAMBDA_MAX))
        self._growth_factor = np.longdouble(str(config.PHASE5_LAMBDA_GROWTH_FACTOR))
        self._growth_interval = config.PHASE5_LAMBDA_GROWTH_INTERVAL_EPOCHS
        self.logger = LoggerFactory.create_logger("QuadruplePrecisionLambdaScheduler")

    @property
    def current_lambda(self) -> np.longdouble:
        return self._lambda

    def step(self, epoch: int, improvement: bool = True):
        if epoch > 0 and epoch % self._growth_interval == 0 and improvement:
            new_lambda = self._lambda * self._growth_factor
            if new_lambda <= self._lambda_max:
                self._lambda = new_lambda
                self.logger.info(f"Phase 5 Lambda (float128) increased to {float(self._lambda):.6e} at epoch {epoch}")

    def compute_regularization_loss(self, model: nn.Module) -> torch.Tensor:
        delta = torch.tensor(0.0, device=self.config.DEVICE, dtype=torch.float64)
        for param in model.parameters():
            if param.numel() > 0:
                margin = (param.double() - param.double().round()).abs().max()
                delta = torch.max(delta, margin)
        return delta * float(self._lambda)

    def set_lambda(self, value: float):
        self._lambda = np.longdouble(str(value))


class AnnealingScheduler:
    def __init__(self, config: Config):
        self.config = config
        self._temperature = config.ANNEALING_INITIAL_TEMPERATURE
        self._cooling_rate = config.ANNEALING_COOLING_RATE
        self._final_temp = config.ANNEALING_FINAL_TEMPERATURE
        self.logger = LoggerFactory.create_logger("AnnealingScheduler")

    @property
    def temperature(self) -> float:
        return self._temperature

    def step(self):
        self._temperature = max(self._temperature * self._cooling_rate, self._final_temp)

    def accept_perturbation(self, delta_loss: float) -> bool:
        if delta_loss < 0: return True
        if self._temperature < self.config.NORMALIZATION_EPS: return False
        probability = math.exp(-delta_loss / self._temperature)
        return np.random.random() < probability

    def should_restart(self, current_delta: float, best_delta: float) -> bool:
        return (current_delta - best_delta) > self.config.ANNEALING_RESTART_THRESHOLD


class TopologicalAnnealingScheduler(AnnealingScheduler):
    def __init__(self, config: Config):
        super().__init__(config)
        self._base_cooling_rate = config.ANNEALING_COOLING_RATE

    def step_adaptive(self, alignment_trend: float = 0.0, resonance_score: float = 0.0):
        combined_signal = alignment_trend + (resonance_score - 0.5) * 0.1
        if combined_signal > 0:
            effective_rate = self._base_cooling_rate * 0.99
        elif combined_signal < -0.01:
            effective_rate = min(self._base_cooling_rate * 1.01, 0.9999)
        else:
            effective_rate = self._base_cooling_rate
        self._temperature = max(self._temperature * effective_rate, self._final_temp)


class TrainingMetricsMonitor:
    def __init__(self, config: Config):
        self.config = config
        self.metrics_history = {'epoch': [], 'loss': [], 'val_loss': [], 'val_acc': [], 'train_acc': [], 'lc': [], 'sp': [], 'alpha': [], 'kappa': [], 'kappa_q': [], 'delta': [], 'temperature': [], 'specific_heat': [], 'poynting_magnitude': [], 'energy_flow': [], 'purity_index': [], 'is_crystal': [], 'lambda_pressure': [], 'hbar_effective': [], 'spectral_entropy': [], 'num_bragg_peaks': [], 'learning_rate': [], 'annealing_temp': [], 'delta_slope': [], 'norm_conservation_error': [], 'gibbs_free_energy': [], 'critical_temperature': [], 'spectral_gap': [], 'participation_ratio': [], 'level_spacing_ratio': [], 'ricci_scalar': [], 'topo_R_cm_x': [], 'topo_R_cm_y': [], 'topo_localization': [], 'topo_alignment': [], 'topo_alignment_trend': [], 'topo_anisotropy': [], 'topo_phase_state': [], 'topo_is_crystalline': [], 'topo_transition_prob': [], 'topo_resonance_score': [], 'topo_is_resonant': [], 'topo_phase_coherence': [], 'topo_spectral_conc': [], 'topo_num_bragg_peaks': [], 'topo_harmonic_count': [], 'topo_loss_total': [], 'topo_lambda_effective': [], 'phase_stability': [], 'willmore_energy': [], 'mean_curvature_mean': [], 'mean_curvature_var': [], 'gaussian_curvature_mean': [], 'surface_area': [], 'is_minimal_surface': [], 'ricci_flow_velocity': [], 'curvature_ratio': []}
        self.gradient_buffer = deque(maxlen=config.GRADIENT_BUFFER_MAXLEN)
        self.loss_history = deque(maxlen=config.LOSS_HISTORY_MAXLEN)
        self.temp_history = deque(maxlen=config.TEMP_HISTORY_MAXLEN)

    def update_metrics(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.metrics_history:
                self.metrics_history[key].append(value)
        if 'loss' in kwargs:
            self.loss_history.append(kwargs['loss'])
        if 'temperature' in kwargs:
            self.temp_history.append(kwargs['temperature'])

    def compute_delta_slope(self) -> float:
        window = self.config.GROKKING_DELTA_SLOPE_WINDOW
        deltas = self.metrics_history.get('delta', [])
        if len(deltas) < window: return 0.0
        recent = deltas[-window:]
        x = np.arange(len(recent), dtype=np.float64)
        y = np.array(recent, dtype=np.float64)
        if np.std(x) < 1e-15: return 0.0
        return float(np.polyfit(x, y, 1)[0])

    def format_progress_bar(self, epoch: int, total_epochs: int, phase: str) -> str:
        h = self.metrics_history
        def safe_get(key): vals = h.get(key, []); return vals[-1] if vals else 0.0
        loss = safe_get('loss'); val_loss = safe_get('val_loss'); val_acc = safe_get('val_acc')
        train_acc = safe_get('train_acc'); lc = safe_get('lc'); sp = safe_get('sp')
        alpha = safe_get('alpha'); kappa = safe_get('kappa'); kappa_q = safe_get('kappa_q')
        delta = safe_get('delta'); temp = safe_get('temperature'); cv = safe_get('specific_heat')
        poynting = safe_get('poynting_magnitude'); lam = safe_get('lambda_pressure')
        hbar = safe_get('hbar_effective'); s_ent = safe_get('spectral_entropy')
        lr = safe_get('learning_rate'); a_temp = safe_get('annealing_temp')
        gibbs = safe_get('gibbs_free_energy'); crit_temp = safe_get('critical_temperature')
        spec_gap = safe_get('spectral_gap'); part_ratio = safe_get('participation_ratio')
        ricci = safe_get('ricci_scalar'); phase_stab = safe_get('phase_stability')
        topo_phase = safe_get('topo_phase_state'); topo_cryst = safe_get('topo_is_crystalline')
        topo_res = safe_get('topo_resonance_score'); topo_phase_coh = safe_get('topo_phase_coherence')
        willmore_e = safe_get('willmore_energy'); mean_curv = safe_get('mean_curvature_mean')
        surf_area = safe_get('surface_area'); is_minimal = safe_get('is_minimal_surface')
        kappa_str = f"{kappa:.2e}" if kappa != float('inf') and not np.isinf(kappa) else "inf"
        stability_str = "S" if phase_stab >= 0.5 else "U"
        lines = []
        lines.append(f"[{phase}] Epoch {epoch}/{total_epochs}")
        lines.append(f"Loss={loss:.6f} ValLoss={val_loss:.6f} TrainAcc={train_acc:.4f} ValAcc={val_acc:.4f}")
        lines.append(f"LC={lc:.4f} SP={sp:.4f} Alpha={alpha:.4f} Kappa={kappa_str} Kappa_q={kappa_q:.2e}")
        lines.append(f"Delta={delta:.6f} T_eff={temp:.2e} C_v={cv:.2e} Poynting={poynting:.2e}")
        lines.append(f"Lambda={lam:.2e} hbar_eff={hbar:.2e} S_spectral={s_ent:.4f}")
        lines.append(f"LR={lr:.2e} AnnealT={a_temp:.2e} Gibbs={gibbs:.4e} T_crit={crit_temp:.2e}")
        lines.append(f"SpecGap={spec_gap:.4e} PartRatio={part_ratio:.4f} Ricci={ricci:.2e} Stability={stability_str}")
        lines.append(f"Topo[Phase={topo_phase:.4f} Cryst={int(topo_cryst)} Resonance={topo_res:.4f} PhaseCoh={topo_phase_coh:.4f}]")
        lines.append(f"Willmore={willmore_e:.4e} MeanCurv={mean_curv:.4e} Area={surf_area:.4f} IsMinimal={int(is_minimal)}")
        return "\n".join(lines)


class CheckpointManager:
    def __init__(self, config: Config, checkpoint_dir: str = "checkpoints"):
        self.config = config
        self.interval_minutes = config.CHECKPOINT_INTERVAL_MINUTES
        self.max_checkpoints = config.MAX_CHECKPOINTS
        self.last_checkpoint_time = time.time()
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(self.checkpoint_dir, exist_ok=True)
        self.checkpoint_files = []

    def should_save_checkpoint(self) -> bool:
        current_time = time.time()
        elapsed_minutes = (current_time - self.last_checkpoint_time) / 60
        return elapsed_minutes >= self.interval_minutes

    def save_checkpoint(self, model: nn.Module, optimizer: optim.Optimizer, epoch: int, metrics: Dict[str, Any], phase: str = "training", lambda_value: float = 0.0, config_snapshot: Dict[str, Any] = None) -> str:
        checkpoint = {'epoch': epoch, 'phase': phase, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict(), 'metrics': metrics, 'lambda_pressure': float(lambda_value), 'config': config_snapshot if config_snapshot else asdict(self.config), 'timestamp': datetime.now().isoformat()}
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        checkpoint_path = os.path.join(self.checkpoint_dir, f"checkpoint_{phase}_epoch_{epoch}_{timestamp}.pth")
        torch.save(checkpoint, checkpoint_path)
        self.checkpoint_files.append(checkpoint_path)
        if len(self.checkpoint_files) > self.max_checkpoints:
            oldest_file = self.checkpoint_files.pop(0)
            if os.path.exists(oldest_file): os.remove(oldest_file)
        latest_path = os.path.join(self.checkpoint_dir, "latest.pth")
        torch.save(checkpoint, latest_path)
        self.last_checkpoint_time = time.time()
        return checkpoint_path


class Phase5CheckpointManager:
    def __init__(self, config: Config):
        self.config = config
        self.checkpoint_dir = "weights"
        os.makedirs(self.checkpoint_dir, exist_ok=True)
        self.latest_path = config.PHASE5_CHECKPOINT_LATEST_PATH
        self.best_delta = float('inf')
        self.best_alpha = 0.0
        self.best_acc = 0.0
        self.logger = LoggerFactory.create_logger("Phase5CheckpointManager")

    def should_save(self, current_delta: float, current_alpha: float, current_acc: float) -> bool:
        is_better_delta = current_delta < self.best_delta
        acc_not_collapsed = current_acc >= self.best_acc * 0.9
        return (is_better_delta and acc_not_collapsed) or (current_alpha > self.best_alpha and acc_not_collapsed)

    def save_checkpoint(self, model: nn.Module, optimizer: optim.Optimizer, epoch: int, metrics: Dict[str, Any], lambda_value: np.longdouble) -> bool:
        current_delta = metrics.get('delta', float('inf'))
        current_alpha = metrics.get('alpha', 0.0)
        current_acc = metrics.get('val_acc', 0.0)
        if not self.should_save(current_delta, current_alpha, current_acc):
            return False
        checkpoint = {'epoch': epoch, 'phase': 'phase5', 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict(), 'metrics': metrics, 'lambda_pressure': float(lambda_value), 'lambda_precision': 'float128', 'config': asdict(self.config), 'timestamp': datetime.now().isoformat()}
        torch.save(checkpoint, self.latest_path)
        self.best_delta = min(self.best_delta, current_delta)
        self.best_alpha = max(self.best_alpha, current_alpha)
        self.best_acc = max(self.best_acc, current_acc)
        self.logger.info(f"Phase 5 checkpoint SAVED: epoch={epoch}, delta={current_delta:.6f}, alpha={current_alpha:.4f}")
        return True


class WeightIntegrityChecker:
    @staticmethod
    def check(model: nn.Module) -> Dict[str, Any]:
        has_nan, has_inf = False, False
        total_params, nan_count, inf_count = 0, 0, 0
        for name, param in model.named_parameters():
            data = param.data
            numel = data.numel()
            total_params += numel
            n_nan = torch.isnan(data).sum().item()
            n_inf = torch.isinf(data).sum().item()
            if n_nan > 0: has_nan, nan_count = True, nan_count + n_nan
            if n_inf > 0: has_inf, inf_count = True, inf_count + n_inf
        return {'is_valid': not (has_nan or has_inf), 'has_nan': has_nan, 'has_inf': has_inf, 'total_params': total_params, 'nan_count': nan_count, 'inf_count': inf_count}


class TrainingEngine:
    def __init__(self, config: Config):
        self.config = config
        self.logger = LoggerFactory.create_logger("TrainingEngine")
        self.criterion = nn.MSELoss()
        self.lc_analyzer = LocalComplexityAnalyzer()
        self.sp_analyzer = SuperpositionAnalyzer()
        self.crystal_calc = CrystallographyMetricsCalculator(config)
        self.thermo_calc = ThermodynamicMetricsCalculator(config)
        self.spectro_calc = SpectroscopyMetricsCalculator(config)
        self.spectral_geom_calc = SpectralGeometryCalculator(config)
        self.ricci_calc = RicciCurvatureCalculator(config)
        self.topo_calc = TopologicalMetricsCalculator(config)
        self.willmore_calc = WillmoreEnergyCalculator(config)
        self.ricci_flow_calc = RicciFlowCalculator(config)

    def compute_weight_metrics(self, model: nn.Module) -> Tuple[float, float]:
        lc_values, sp_values = [], []
        limit = self.config.WEIGHT_METRIC_DIM_LIMIT
        for name, param in model.named_parameters():
            if 'weight' in name and param.dim() >= 2:
                w = param[:min(param.size(0), limit), :min(param.size(1), limit)]
                lc_values.append(self.lc_analyzer.compute_local_complexity(w))
                sp_values.append(self.sp_analyzer.compute_superposition(w))
        return (np.mean(lc_values) if lc_values else 0.0, np.mean(sp_values) if sp_values else 0.0)

    def compute_norm_conservation_error(self, model: nn.Module, val_x: torch.Tensor) -> float:
        model.eval()
        with torch.no_grad():
            outputs = model(val_x)
            input_norms = torch.norm(val_x.view(val_x.size(0), -1), dim=1)
            output_norms = torch.norm(outputs.view(outputs.size(0), -1), dim=1)
            relative_error = torch.abs(output_norms - input_norms) / (input_norms + self.config.NORMALIZATION_EPS)
            return relative_error.mean().item()

    def train_single_epoch(self, model: nn.Module, optimizer: optim.Optimizer, dataloader: DataLoader, epoch: int, lambda_scheduler: Optional[Union[LambdaPressureScheduler, QuadruplePrecisionLambdaScheduler]] = None) -> Tuple[float, float]:
        model.train()
        total_loss, total_mse, total_samples, correct = 0.0, 0.0, 0, 0
        for batch_x, batch_y in dataloader:
            batch_x, batch_y = batch_x.to(self.config.DEVICE), batch_y.to(self.config.DEVICE)
            optimizer.zero_grad()
            outputs = model(batch_x)
            mse_loss = self.criterion(outputs, batch_y)
            reg_loss = lambda_scheduler.compute_regularization_loss(model) if lambda_scheduler is not None else torch.tensor(0.0)
            loss = mse_loss + reg_loss
            loss.backward()
            if epoch % self.config.NOISE_INTERVAL_EPOCHS == 0:
                for param in model.parameters():
                    if param.grad is not None:
                        param.grad.add_(torch.randn_like(param.grad) * self.config.NOISE_AMPLITUDE)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=self.config.GRADIENT_CLIP_NORM)
            optimizer.step()
            total_loss += loss.item() * batch_x.size(0)
            total_mse += mse_loss.item() * batch_x.size(0)
            total_samples += batch_x.size(0)
            with torch.no_grad():
                per_sample_mse = ((outputs - batch_y)**2).mean(dim=(1, 2, 3))
                correct += (per_sample_mse < self.config.MSE_THRESHOLD).sum().item()
        return (total_loss / total_samples if total_samples > 0 else 0.0, correct / total_samples if total_samples > 0 else 0.0)

    def validate(self, model: nn.Module, val_x: torch.Tensor, val_y: torch.Tensor) -> Tuple[float, float]:
        model.eval()
        val_x, val_y = val_x.to(self.config.DEVICE), val_y.to(self.config.DEVICE)
        with torch.no_grad():
            outputs = model(val_x)
            val_loss = self.criterion(outputs, val_y).item()
            per_sample_mse = ((outputs - val_y)**2).mean(dim=(1, 2, 3))
            val_acc = (per_sample_mse < self.config.MSE_THRESHOLD).float().mean().item()
        return val_loss, val_acc

    def collect_all_metrics(self, model: nn.Module, monitor: TrainingMetricsMonitor, val_x: torch.Tensor, val_y: torch.Tensor, lambda_scheduler: Optional[Union[LambdaPressureScheduler, QuadruplePrecisionLambdaScheduler]] = None, annealing_scheduler: Optional[AnnealingScheduler] = None, current_lr: float = 0.0, epoch: int = 0) -> Dict[str, Any]:
        lc, sp = self.compute_weight_metrics(model)
        crystal_metrics = self.crystal_calc.compute_all_metrics(model, val_x, val_y)
        alpha = crystal_metrics.get('alpha', 0.0)
        kappa = crystal_metrics.get('kappa', float('inf'))
        kappa_q = crystal_metrics.get('kappa_q', 1.0)
        delta = crystal_metrics.get('delta', 1.0)
        poynting = crystal_metrics.get('energy_flow', 0.0)
        purity_index = crystal_metrics.get('purity_index', 0.0)
        is_crystal = crystal_metrics.get('is_crystal', False)
        effective_lr = current_lr if current_lr > 0 else self.config.LEARNING_RATE
        thermo_metrics = self.thermo_calc.compute(model, gradient_buffer=monitor.gradient_buffer, learning_rate=effective_lr, loss_history=monitor.loss_history, temp_history=monitor.temp_history, delta=delta, alpha=alpha)
        temp = thermo_metrics.get('temperature', 0.0)
        cv = thermo_metrics.get('specific_heat', 0.0)
        gibbs = thermo_metrics.get('gibbs_free_energy', 0.0)
        crit_temp = thermo_metrics.get('critical_temperature', 0.0)
        phase_stab = thermo_metrics.get('phase_stability', 0.0)
        spectro = self.spectro_calc.compute(model)
        spectral_entropy = spectro.get('spectral_entropy', 0.0)
        num_peaks = spectro.get('num_peaks', 0)
        spectral_geom = self.spectral_geom_calc.compute(model)
        spectral_gap = spectral_geom.get('spectral_gap', 0.0)
        part_ratio = spectral_geom.get('participation_ratio', 0.0)
        ricci_metrics = self.ricci_calc.compute(model)
        ricci_scalar = ricci_metrics.get('ricci_scalar', 0.0)
        lambda_val = float(lambda_scheduler.current_lambda) if lambda_scheduler else 0.0
        hbar_eff = self.crystal_calc.compute_hbar_effective(model, lambda_val)
        annealing_temp = annealing_scheduler.temperature if annealing_scheduler else 0.0
        delta_slope = monitor.compute_delta_slope()
        norm_err = self.compute_norm_conservation_error(model, val_x) if val_x is not None else 0.0
        topo_metrics = self.topo_calc.compute(model, epoch=epoch)
        topo_public = {k: v for k, v in topo_metrics.items() if not k.startswith('_')}
        willmore_metrics = self.willmore_calc.compute(model)
        ricci_flow_metrics = self.ricci_flow_calc.compute(model)
        result = {'lc': lc, 'sp': sp, 'alpha': alpha, 'kappa': kappa, 'kappa_q': kappa_q, 'delta': delta, 'temperature': temp, 'specific_heat': cv, 'poynting_magnitude': poynting, 'energy_flow': poynting, 'purity_index': purity_index, 'is_crystal': is_crystal, 'lambda_pressure': lambda_val, 'hbar_effective': hbar_eff, 'spectral_entropy': spectral_entropy, 'num_bragg_peaks': num_peaks, 'learning_rate': current_lr, 'annealing_temp': annealing_temp, 'delta_slope': delta_slope, 'norm_conservation_error': norm_err, 'gibbs_free_energy': gibbs, 'critical_temperature': crit_temp, 'spectral_gap': spectral_gap, 'participation_ratio': part_ratio, 'ricci_scalar': ricci_scalar, 'phase_stability': phase_stab, 'willmore_energy': willmore_metrics.get('willmore_energy', 0.0), 'mean_curvature_mean': willmore_metrics.get('mean_curvature_mean', 0.0), 'mean_curvature_var': willmore_metrics.get('mean_curvature_var', 0.0), 'gaussian_curvature_mean': willmore_metrics.get('gaussian_curvature_mean', 0.0), 'surface_area': willmore_metrics.get('surface_area', 0.0), 'is_minimal_surface': willmore_metrics.get('is_minimal_surface', 0.0), 'ricci_flow_velocity': ricci_flow_metrics.get('ricci_flow_velocity', 0.0), 'curvature_ratio': willmore_metrics.get('curvature_ratio', 0.0)}
        result.update(topo_public)
        return result


class BatchSizeProspector:
    def __init__(self, config: Config, surface_engine: MinimalSurfaceInferenceEngine):
        self.config = config
        self.surface_engine = surface_engine
        self.logger = LoggerFactory.create_logger("BatchSizeProspector")

    def prospect(self) -> int:
        self.logger.info("Phase 1: Batch size prospecting started")
        candidates = self.config.BATCH_CANDIDATES
        seed = self.config.BATCH_PROSPECT_SEED
        epochs = self.config.BATCH_PROSPECT_EPOCHS
        results = {}
        for bs in candidates:
            self.logger.info(f"  Testing batch_size={bs}")
            SeedManager.set_seed(seed, self.config.DEVICE)
            dataset = MinimalSurfaceDataset(self.config, self.surface_engine, seed=seed)
            loader = DataLoader(dataset, batch_size=bs, shuffle=True)
            val_x, val_y = dataset.get_validation_batch()
            val_x, val_y = val_x.to(self.config.DEVICE), val_y.to(self.config.DEVICE)
            model = MinimalSurfaceSpectralNetwork(grid_size=self.config.GRID_SIZE, hidden_dim=self.config.HIDDEN_DIM, expansion_dim=self.config.EXPANSION_DIM, num_spectral_layers=self.config.NUM_SPECTRAL_LAYERS).to(self.config.DEVICE)
            optimizer = optim.SGD(model.parameters(), lr=self.config.LEARNING_RATE, weight_decay=self.config.WEIGHT_DECAY, momentum=self.config.MOMENTUM)
            engine = TrainingEngine(self.config)
            crystal_calc = CrystallographyMetricsCalculator(self.config)
            for ep in range(1, epochs + 1):
                engine.train_single_epoch(model, optimizer, loader, ep)
            val_loss, val_acc = engine.validate(model, val_x, val_y)
            delta = crystal_calc.compute_discretization_margin(model)
            kappa = crystal_calc.compute_kappa(model, val_x, val_y)
            results[bs] = {'delta': delta, 'val_acc': val_acc, 'val_loss': val_loss, 'kappa': kappa}
            self.logger.info(f"    batch_size={bs}: delta={delta:.6f}, val_acc={val_acc:.4f}, kappa={kappa:.2e}")
        crystal_candidates = {bs: r for bs, r in results.items() if r['kappa'] < 1.5 and r['kappa'] != float('inf')}
        best_bs = min(crystal_candidates.keys(), key=lambda k: crystal_candidates[k]['delta']) if crystal_candidates else min(results.keys(), key=lambda k: results[k]['delta'])
        self.logger.info(f"Phase 1 complete: Best batch_size={best_bs} (delta={results[best_bs]['delta']:.6f})")
        return best_bs


class SeedMiner:
    def __init__(self, config: Config, surface_engine: MinimalSurfaceInferenceEngine, batch_size: int):
        self.config = config
        self.surface_engine = surface_engine
        self.batch_size = batch_size
        self.logger = LoggerFactory.create_logger("SeedMiner")

    def mine(self) -> Optional[int]:
        self.logger.info("Phase 2: Seed mining started")
        prospect_epochs = self.config.MINING_PROSPECT_EPOCHS
        interval = self.config.MINING_PROSPECT_DELTA_EPOCH_INTERVAL
        max_attempts = self.config.MINING_MAX_ATTEMPTS
        start_seed = self.config.MINING_START_SEED
        seed_results = {}
        for i in range(start_seed, start_seed + max_attempts):
            current_seed = i
            SeedManager.set_seed(current_seed, self.config.DEVICE)
            dataset = MinimalSurfaceDataset(self.config, self.surface_engine, seed=current_seed)
            loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
            val_x, val_y = dataset.get_validation_batch()
            val_x, val_y = val_x.to(self.config.DEVICE), val_y.to(self.config.DEVICE)
            model = MinimalSurfaceSpectralNetwork(grid_size=self.config.GRID_SIZE, hidden_dim=self.config.HIDDEN_DIM, expansion_dim=self.config.EXPANSION_DIM, num_spectral_layers=self.config.NUM_SPECTRAL_LAYERS).to(self.config.DEVICE)
            optimizer = optim.SGD(model.parameters(), lr=self.config.LEARNING_RATE, weight_decay=self.config.WEIGHT_DECAY, momentum=self.config.MOMENTUM)
            engine = TrainingEngine(self.config)
            crystal_calc = CrystallographyMetricsCalculator(self.config)
            delta_trajectory, kappa_trajectory = [], []
            for ep in range(1, prospect_epochs + 1):
                engine.train_single_epoch(model, optimizer, loader, ep)
                if ep % interval == 0:
                    delta = crystal_calc.compute_discretization_margin(model)
                    kappa = crystal_calc.compute_kappa(model, val_x, val_y)
                    delta_trajectory.append((ep, delta))
                    kappa_trajectory.append((ep, kappa))
            last_delta = delta_trajectory[-1][1] if delta_trajectory else 1.0
            final_kappa = kappa_trajectory[-1][1] if kappa_trajectory else float('inf')
            delta_velocity = (delta_trajectory[-1][1] - delta_trajectory[0][1]) / max(len(delta_trajectory), 1) if len(delta_trajectory) > 1 else 0.0
            is_cooling = delta_velocity < 0
            is_kappa_crystalline = final_kappa < 1.5 and final_kappa != float('inf')
            seed_results[current_seed] = {'last_delta': last_delta, 'delta_velocity': delta_velocity, 'is_cooling': is_cooling, 'final_kappa': final_kappa, 'is_kappa_crystalline': is_kappa_crystalline}
            self.logger.info(f"  Seed {current_seed}: delta={last_delta:.6f} v_delta={delta_velocity:+.6f} k={final_kappa:.2e}")
        crystalline_cooling = {s: r for s, r in seed_results.items() if r['is_kappa_crystalline'] and r['is_cooling']}
        if crystalline_cooling:
            best_seed = min(crystalline_cooling.keys(), key=lambda s: crystalline_cooling[s]['last_delta'])
        else:
            crystalline = {s: r for s, r in seed_results.items() if r['is_kappa_crystalline']}
            best_seed = min(crystalline.keys(), key=lambda s: crystalline[s]['last_delta']) if crystalline else min(seed_results.keys(), key=lambda s: seed_results[s]['last_delta'])
        self.logger.info(f"Phase 2 complete: Best seed={best_seed} (delta={seed_results[best_seed]['last_delta']:.6f})")
        return best_seed


class FullTrainingOrchestrator:
    def __init__(self, config: Config, surface_engine: MinimalSurfaceInferenceEngine, seed: int, batch_size: int):
        self.config = config
        self.surface_engine = surface_engine
        self.seed = seed
        self.batch_size = batch_size
        self.logger = LoggerFactory.create_logger("FullTrainingOrchestrator")

    def run_phase3_training(self) -> Tuple[nn.Module, optim.Optimizer, TrainingMetricsMonitor]:
        self.logger.info(f"Phase 3: Full training started (seed={self.seed}, batch_size={self.batch_size}, epochs={self.config.EPOCHS})")
        SeedManager.set_seed(self.seed, self.config.DEVICE)
        dataset = MinimalSurfaceDataset(self.config, self.surface_engine, seed=self.seed)
        loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
        val_x, val_y = dataset.get_validation_batch()
        val_x, val_y = val_x.to(self.config.DEVICE), val_y.to(self.config.DEVICE)
        model = MinimalSurfaceSpectralNetwork(grid_size=self.config.GRID_SIZE, hidden_dim=self.config.HIDDEN_DIM, expansion_dim=self.config.EXPANSION_DIM, num_spectral_layers=self.config.NUM_SPECTRAL_LAYERS).to(self.config.DEVICE)
        optimizer = optim.SGD(model.parameters(), lr=self.config.LEARNING_RATE, weight_decay=self.config.WEIGHT_DECAY, momentum=self.config.MOMENTUM)
        scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=self.config.EPOCHS, eta_min=self.config.LEARNING_RATE * self.config.COSINE_ANNEALING_ETA_MIN_FACTOR)
        lambda_scheduler = AdaptiveLambdaScheduler(self.config)
        engine = TrainingEngine(self.config)
        monitor = TrainingMetricsMonitor(self.config)
        checkpoint_mgr = CheckpointManager(self.config, checkpoint_dir="checkpoints_phase3")
        grokking_detected, grokking_epoch = False, None
        best_delta = float('inf')
        patience_counter = 0
        start_time = time.time()
        for epoch in range(1, self.config.EPOCHS + 1):
            topo_phase = monitor.metrics_history['topo_phase_state'][-1] if monitor.metrics_history['topo_phase_state'] else 0.0
            lambda_scheduler.step_adaptive(epoch, topo_phase)
            train_loss, train_acc = engine.train_single_epoch(model, optimizer, loader, epoch, lambda_scheduler)
            scheduler.step()
            val_loss, val_acc = engine.validate(model, val_x, val_y)
            current_lr = optimizer.param_groups[0]['lr']
            all_metrics = engine.collect_all_metrics(model, monitor, val_x, val_y, lambda_scheduler=lambda_scheduler, current_lr=current_lr, epoch=epoch)
            monitor.update_metrics(epoch=epoch, loss=train_loss, val_loss=val_loss, val_acc=val_acc, train_acc=train_acc, **all_metrics)
            for param in model.parameters():
                if param.grad is not None:
                    monitor.gradient_buffer.append(param.grad.detach().clone().flatten()[:500])
                    break
            delta = all_metrics['delta']
            if delta < best_delta:
                best_delta, patience_counter = delta, 0
            else:
                patience_counter += 1
            if train_acc >= self.config.GROKKING_TRAIN_ACC_THRESHOLD and val_acc >= self.config.GROKKING_VAL_ACC_THRESHOLD and not grokking_detected:
                delta_slope = monitor.compute_delta_slope()
                if delta_slope < self.config.GROKKING_DELTA_SLOPE_THRESHOLD:
                    grokking_detected, grokking_epoch = True, epoch
                    self.logger.info(f"  GROKKING detected at epoch {epoch}: train_acc={train_acc:.4f}, val_acc={val_acc:.4f}")
            if epoch % self.config.LOG_INTERVAL_EPOCHS == 0:
                self.logger.info(monitor.format_progress_bar(epoch, self.config.EPOCHS, "P3-TRAIN"))
            if checkpoint_mgr.should_save_checkpoint():
                metrics_snapshot = {'epoch': epoch, 'train_loss': train_loss, 'val_loss': val_loss, 'val_acc': val_acc, 'train_acc': train_acc, **all_metrics}
                path = checkpoint_mgr.save_checkpoint(model, optimizer, epoch, metrics_snapshot, phase="phase3_training", lambda_value=float(lambda_scheduler.current_lambda))
                self.logger.info(f"  Checkpoint saved: {path}")
            integrity = WeightIntegrityChecker.check(model)
            if not integrity['is_valid']:
                self.logger.warning(f"  Weight integrity compromised at epoch {epoch}: NaN={integrity['nan_count']}, Inf={integrity['inf_count']}")
            if grokking_detected and patience_counter > self.config.GROKKING_PATIENCE:
                self.logger.info(f"  Stopping Phase 3 at epoch {epoch}: grokking achieved and patience exceeded")
                break
        elapsed = time.time() - start_time
        self.logger.info(f"Phase 3 complete in {elapsed:.1f}s. Grokking={'YES at epoch ' + str(grokking_epoch) if grokking_detected else 'NO'}. Best delta={best_delta:.6f}")
        return model, optimizer, monitor


class RefinementOrchestrator:
    def __init__(self, config: Config, surface_engine: MinimalSurfaceInferenceEngine, model: nn.Module, optimizer: optim.Optimizer, monitor: TrainingMetricsMonitor, seed: int, batch_size: int):
        self.config = config
        self.surface_engine = surface_engine
        self.model = model
        self.optimizer = optimizer
        self.monitor = monitor
        self.seed = seed
        self.batch_size = batch_size
        self.logger = LoggerFactory.create_logger("RefinementOrchestrator")

    def run_phase4_refinement(self) -> nn.Module:
        self.logger.info(f"Phase 4: Refinement via simulated annealing (epochs={self.config.REFINEMENT_EPOCHS})")
        dataset = MinimalSurfaceDataset(self.config, self.surface_engine, seed=self.seed)
        loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
        val_x, val_y = dataset.get_validation_batch()
        val_x, val_y = val_x.to(self.config.DEVICE), val_y.to(self.config.DEVICE)
        lambda_scheduler = AdaptiveLambdaScheduler(self.config)
        lambda_scheduler.set_lambda(self.config.LAMBDA_MAX * 0.1)
        annealing = TopologicalAnnealingScheduler(self.config)
        engine = TrainingEngine(self.config)
        checkpoint_mgr = CheckpointManager(self.config, checkpoint_dir="checkpoints_phase4")
        best_model_state = copy.deepcopy(self.model.state_dict())
        best_delta = CrystallographyMetricsCalculator(self.config).compute_discretization_margin(self.model)
        self.logger.info(f"  Starting refinement from delta={best_delta:.6f}")
        for pg in self.optimizer.param_groups:
            pg['lr'] = self.config.LEARNING_RATE * 0.1
        start_time = time.time()
        for epoch in range(1, self.config.REFINEMENT_EPOCHS + 1):
            topo_phase = self.monitor.metrics_history['topo_phase_state'][-1] if self.monitor.metrics_history['topo_phase_state'] else 0.0
            topo_alignment_trend = self.monitor.metrics_history['topo_alignment_trend'][-1] if self.monitor.metrics_history['topo_alignment_trend'] else 0.0
            topo_resonance = self.monitor.metrics_history['topo_resonance_score'][-1] if self.monitor.metrics_history['topo_resonance_score'] else 0.0
            lambda_scheduler.step_adaptive(epoch, topo_phase)
            annealing.step_adaptive(topo_alignment_trend, topo_resonance)
            previous_state = copy.deepcopy(self.model.state_dict())
            train_loss, train_acc = engine.train_single_epoch(self.model, self.optimizer, loader, epoch, lambda_scheduler)
            val_loss, val_acc = engine.validate(self.model, val_x, val_y)
            current_delta = CrystallographyMetricsCalculator(self.config).compute_discretization_margin(self.model)
            delta_diff = current_delta - best_delta
            if not annealing.accept_perturbation(delta_diff):
                self.model.load_state_dict(previous_state)
                current_delta = best_delta
            elif current_delta < best_delta:
                best_delta = current_delta
                best_model_state = copy.deepcopy(self.model.state_dict())
            if annealing.should_restart(current_delta, best_delta):
                self.model.load_state_dict(best_model_state)
                self.logger.info(f"  Annealing restart at epoch {epoch}, reverting to best_delta={best_delta:.6f}")
            current_lr = self.optimizer.param_groups[0]['lr']
            all_metrics = engine.collect_all_metrics(self.model, self.monitor, val_x, val_y, lambda_scheduler=lambda_scheduler, annealing_scheduler=annealing, current_lr=current_lr, epoch=epoch)
            self.monitor.update_metrics(epoch=epoch, loss=train_loss, val_loss=val_loss, val_acc=val_acc, train_acc=train_acc, **all_metrics)
            if epoch % self.config.LOG_INTERVAL_EPOCHS == 0:
                self.logger.info(self.monitor.format_progress_bar(epoch, self.config.REFINEMENT_EPOCHS, "P4-REFINE"))
                self.logger.info(f"  Annealing T={annealing.temperature:.2e}, best_delta={best_delta:.6f}")
            if checkpoint_mgr.should_save_checkpoint():
                metrics_snapshot = {'epoch': epoch, 'train_loss': train_loss, 'val_loss': val_loss, 'val_acc': val_acc, 'train_acc': train_acc, 'best_delta': best_delta, **all_metrics}
                path = checkpoint_mgr.save_checkpoint(self.model, self.optimizer, epoch, metrics_snapshot, phase="phase4_refinement", lambda_value=float(lambda_scheduler.current_lambda))
                self.logger.info(f"  Checkpoint saved: {path}")
        self.model.load_state_dict(best_model_state)
        elapsed = time.time() - start_time
        self.logger.info(f"Phase 4 complete in {elapsed:.1f}s. Final best_delta={best_delta:.6f}")
        return self.model


class Phase5Orchestrator:
    def __init__(self, config: Config, surface_engine: MinimalSurfaceInferenceEngine, model: nn.Module, monitor: TrainingMetricsMonitor, seed: int, batch_size: int):
        self.config = config
        self.surface_engine = surface_engine
        self.model = model
        self.monitor = monitor
        self.seed = seed
        self.batch_size = batch_size
        self.logger = LoggerFactory.create_logger("Phase5Orchestrator")
        self.checkpoint_mgr = Phase5CheckpointManager(config)

    def run_phase5_crystallization(self) -> nn.Module:
        self.logger.info("=" * 80)
        self.logger.info("PHASE 5: QUADRUPLE PRECISION (float128) HIGH-PRESSURE CRYSTALLIZATION")
        self.logger.info("=" * 80)
        dataset = MinimalSurfaceDataset(self.config, self.surface_engine, seed=self.seed)
        loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
        val_x, val_y = dataset.get_validation_batch()
        val_x, val_y = val_x.to(self.config.DEVICE), val_y.to(self.config.DEVICE)
        optimizer = optim.SGD(self.model.parameters(), lr=self.config.LEARNING_RATE * 0.01, weight_decay=self.config.WEIGHT_DECAY, momentum=self.config.MOMENTUM)
        lambda_scheduler = QuadruplePrecisionLambdaScheduler(self.config)
        engine = TrainingEngine(self.config)
        crystal_calc = CrystallographyMetricsCalculator(self.config)
        best_delta = crystal_calc.compute_discretization_margin(self.model)
        best_alpha = crystal_calc.compute_alpha_purity(self.model)
        self.logger.info(f"  Starting Phase 5 from delta={best_delta:.6f}, alpha={best_alpha:.4f}")
        start_time = time.time()
        for epoch in range(1, self.config.PHASE5_EPOCHS + 1):
            previous_state = copy.deepcopy(self.model.state_dict())
            train_loss, train_acc = engine.train_single_epoch(self.model, optimizer, loader, epoch, lambda_scheduler)
            thermal_scale = self.config.PHASE5_THERMAL_INJECTION_SCALE * (1.0 + epoch / self.config.PHASE5_EPOCHS)
            with torch.no_grad():
                for param in self.model.parameters():
                    param.add_(torch.randn_like(param) * thermal_scale)
            val_loss, val_acc = engine.validate(self.model, val_x, val_y)
            current_delta = crystal_calc.compute_discretization_margin(self.model)
            current_alpha = crystal_calc.compute_alpha_purity(self.model)
            integrity = WeightIntegrityChecker.check(self.model)
            if not integrity['is_valid']:
                self.logger.warning(f"  Model collapsed at epoch {epoch}. Reverting to previous state.")
                self.model.load_state_dict(previous_state)
                continue
            is_improvement = current_delta < best_delta or current_alpha > best_alpha
            if current_delta < best_delta: best_delta = current_delta
            if current_alpha > best_alpha: best_alpha = current_alpha
            lambda_scheduler.step(epoch, improvement=is_improvement)
            all_metrics = engine.collect_all_metrics(self.model, self.monitor, val_x, val_y, lambda_scheduler=lambda_scheduler, current_lr=optimizer.param_groups[0]['lr'], epoch=epoch)
            all_metrics['val_acc'] = val_acc
            all_metrics['train_acc'] = train_acc
            self.monitor.update_metrics(epoch=epoch, loss=train_loss, val_loss=val_loss, val_acc=val_acc, train_acc=train_acc, **all_metrics)
            if epoch % self.config.LOG_INTERVAL_EPOCHS == 0:
                self.logger.info(self.monitor.format_progress_bar(epoch, self.config.PHASE5_EPOCHS, "P5-CRYSTAL"))
                self.logger.info(f"  Lambda(float128)={float(lambda_scheduler.current_lambda):.2e}, delta={current_delta:.6f}, alpha={current_alpha:.4f}")
            self.checkpoint_mgr.save_checkpoint(self.model, optimizer, epoch, all_metrics, lambda_scheduler.current_lambda)
            if current_delta < self.config.PHASE5_DELTA_TARGET and current_alpha > self.config.PHASE5_ALPHA_TARGET:
                self.logger.info(f"  CRYSTAL ACHIEVED at epoch {epoch}: delta={current_delta:.6f}, alpha={current_alpha:.4f}")
                break
        elapsed = time.time() - start_time
        self.logger.info(f"Phase 5 complete in {elapsed:.1f}s. Final delta={best_delta:.6f}, alpha={best_alpha:.4f}")
        return self.model


class ExperimentOrchestrator:
    def __init__(self, config: Config):
        self.config = config
        self.logger = LoggerFactory.create_logger("ExperimentOrchestrator")

    def run(self):
        self.logger.info("=" * 80)
        self.logger.info("SURFACE TENSION AND WILLMORE ENERGY TOPOLOGICAL CRYSTALLIZATION")
        self.logger.info("Minimal Surface Physics for Deep Learning Training")
        self.logger.info("=" * 80)
        self.logger.info(f"Device: {self.config.DEVICE}")
        self.logger.info(f"Grid size: {self.config.GRID_SIZE}")
        self.logger.info(f"Hidden dim: {self.config.HIDDEN_DIM}")
        self.logger.info(f"Expansion dim: {self.config.EXPANSION_DIM}")
        self.logger.info(f"Surface tension coefficient: {self.config.SURFACE_TENSION_COEFFICIENT}")
        self.logger.info(f"Willmore energy weight: {self.config.WILLMORE_ENERGY_WEIGHT}")
        os.makedirs(self.config.RESULTS_DIR, exist_ok=True)
        surface_engine = MinimalSurfaceInferenceEngine(self.config)
        
        self.logger.info("-" * 80)
        self.logger.info("PHASE 1: BATCH SIZE PROSPECTING")
        self.logger.info("-" * 80)
        prospector = BatchSizeProspector(self.config, surface_engine)
        best_batch_size = prospector.prospect()
        
        self.logger.info("-" * 80)
        self.logger.info("PHASE 2: SEED MINING WITH DECREASING DELTA")
        self.logger.info("-" * 80)
        miner = SeedMiner(self.config, surface_engine, best_batch_size)
        best_seed = miner.mine()
        if best_seed is None:
            best_seed = self.config.RANDOM_SEED
        
        self.logger.info("-" * 80)
        self.logger.info("PHASE 3: FULL TRAINING TO GROKKING")
        self.logger.info("-" * 80)
        trainer = FullTrainingOrchestrator(self.config, surface_engine, best_seed, best_batch_size)
        model, optimizer, monitor = trainer.run_phase3_training()
        
        self.logger.info("-" * 80)
        self.logger.info("PHASE 4: REFINEMENT VIA SIMULATED ANNEALING")
        self.logger.info("-" * 80)
        refiner = RefinementOrchestrator(self.config, surface_engine, model, optimizer, monitor, best_seed, best_batch_size)
        model = refiner.run_phase4_refinement()
        
        crystal_calc = CrystallographyMetricsCalculator(self.config)
        final_delta = crystal_calc.compute_discretization_margin(model)
        final_alpha = crystal_calc.compute_alpha_purity(model)
        
        if self.config.PHASE5_ENABLE:
            delta_threshold = self.config.PHASE5_DELTA_TARGET * 10
            alpha_threshold = self.config.PHASE5_ALPHA_TARGET * 0.8
            if final_delta > delta_threshold or final_alpha < alpha_threshold:
                self.logger.info("-" * 80)
                self.logger.info("PHASE 5: QUADRUPLE PRECISION CRYSTALLIZATION REQUIRED")
                self.logger.info("-" * 80)
                phase5 = Phase5Orchestrator(self.config, surface_engine, model, monitor, best_seed, best_batch_size)
                model = phase5.run_phase5_crystallization()
        
        self.logger.info("-" * 80)
        self.logger.info("FINAL RESULTS")
        self.logger.info("-" * 80)
        self._save_final_results(model, monitor, best_seed, best_batch_size)

    def _save_final_results(self, model: nn.Module, monitor: TrainingMetricsMonitor, seed: int, batch_size: int):
        os.makedirs("weights", exist_ok=True)
        crystal_calc = CrystallographyMetricsCalculator(self.config)
        delta = crystal_calc.compute_discretization_margin(model)
        alpha = crystal_calc.compute_alpha_purity(model)
        kappa_q = crystal_calc.compute_kappa_quantum(model)
        poynting = crystal_calc.compute_poynting_vector(model)
        integrity = WeightIntegrityChecker.check(model)
        topo_calc = TopologicalMetricsCalculator(self.config)
        topo_final = topo_calc.compute(model)
        topo_public = {k: v for k, v in topo_final.items() if not k.startswith('_')}
        willmore_calc = WillmoreEnergyCalculator(self.config)
        willmore_final = willmore_calc.compute(model)
        
        final_checkpoint = {
            'model_state_dict': model.state_dict(),
            'config': asdict(self.config),
            'seed': seed,
            'batch_size': batch_size,
            'final_metrics': {'delta': delta, 'alpha': alpha, 'kappa_q': kappa_q, 'poynting_magnitude': poynting['poynting_magnitude'], 'integrity': integrity, **topo_public, **willmore_final},
            'metrics_history': monitor.metrics_history,
            'timestamp': datetime.now().isoformat()
        }
        final_path = "weights/willmore_crystal_final.pth"
        torch.save(final_checkpoint, final_path)
        self.logger.info(f"Final model saved to {final_path}")
        
        results_summary = {'seed': seed, 'batch_size': batch_size, 'delta': delta, 'alpha': alpha, 'kappa_q': kappa_q, 'poynting_magnitude': poynting['poynting_magnitude'], 'is_valid': integrity['is_valid'], 'total_params': integrity['total_params'], **topo_public, **willmore_final, 'timestamp': datetime.now().isoformat()}
        results_path = os.path.join(self.config.RESULTS_DIR, "final_results.json")
        with open(results_path, 'w') as f:
            json.dump(results_summary, f, indent=2, default=str)
        self.logger.info(f"Results summary saved to {results_path}")
        
        self.logger.info("=" * 80)
        self.logger.info("EXPERIMENT COMPLETE")
        self.logger.info(f"  Seed: {seed}")
        self.logger.info(f"  Batch size: {batch_size}")
        self.logger.info(f"  Delta: {delta:.6f}")
        self.logger.info(f"  Alpha: {alpha:.4f}")
        self.logger.info(f"  Kappa_q: {kappa_q:.2e}")
        self.logger.info(f"  Poynting: {poynting['poynting_magnitude']:.2e}")
        self.logger.info(f"  Valid: {integrity['is_valid']}")
        self.logger.info(f"  Total params: {integrity['total_params']}")
        self.logger.info(f"  Willmore Energy: {willmore_final.get('willmore_energy', 0.0):.4e}")
        self.logger.info(f"  Mean Curvature: {willmore_final.get('mean_curvature_mean', 0.0):.4e}")
        self.logger.info(f"  Surface Area: {willmore_final.get('surface_area', 0.0):.4f}")
        self.logger.info(f"  Is Minimal Surface: {willmore_final.get('is_minimal_surface', 0.0):.0f}")
        self.logger.info("=" * 80)


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Surface Tension and Willmore Energy Topological Crystallization')
    parser.add_argument('--grid_size', type=int, default=Config.GRID_SIZE, help='Grid size for spatial discretization')
    parser.add_argument('--hidden_dim', type=int, default=Config.HIDDEN_DIM, help='Hidden dimension of spectral network')
    parser.add_argument('--expansion_dim', type=int, default=Config.EXPANSION_DIM, help='Expansion dimension for spectral processing')
    parser.add_argument('--num_spectral_layers', type=int, default=Config.NUM_SPECTRAL_LAYERS, help='Number of spectral layers')
    parser.add_argument('--epochs', type=int, default=Config.EPOCHS, help='Number of training epochs for Phase 3')
    parser.add_argument('--refinement_epochs', type=int, default=Config.REFINEMENT_EPOCHS, help='Number of refinement epochs for Phase 4')
    parser.add_argument('--phase5_epochs', type=int, default=Config.PHASE5_EPOCHS, help='Number of epochs for Phase 5 crystallization')
    parser.add_argument('--lr', type=float, default=Config.LEARNING_RATE, help='Base learning rate')
    parser.add_argument('--lambda_max', type=float, default=Config.LAMBDA_MAX, help='Maximum lambda regularization pressure')
    parser.add_argument('--phase5_lambda_max', type=float, default=Config.PHASE5_LAMBDA_MAX, help='Maximum lambda for Phase 5 (float128 precision)')
    parser.add_argument('--mining_attempts', type=int, default=Config.MINING_MAX_ATTEMPTS, help='Number of seed mining attempts')
    parser.add_argument('--backbone_path', type=str, default=Config.BACKBONE_CHECKPOINT_PATH, help='Path to minimal surface backbone checkpoint')
    parser.add_argument('--no_backbone', action='store_true', help='Disable minimal surface backbone, use analytical operator')
    parser.add_argument('--num_samples', type=int, default=Config.NUM_SAMPLES, help='Number of training samples')
    parser.add_argument('--surface_tension', type=float, default=Config.SURFACE_TENSION_COEFFICIENT, help='Surface tension coefficient for soap bubble physics')
    parser.add_argument('--willmore_weight', type=float, default=Config.WILLMORE_ENERGY_WEIGHT, help='Willmore energy weight for minimal surface optimization')
    parser.add_argument('--num_eigenmodes', type=int, default=Config.NUM_EIGENMODES, help='Number of eigenmodes to sample from')
    parser.add_argument('--checkpoint_interval', type=int, default=Config.CHECKPOINT_INTERVAL_MINUTES, help='Checkpoint interval in minutes')
    parser.add_argument('--no_topo', action='store_true', help='Disable topological Fourier mass center detection')
    parser.add_argument('--topo_alignment_threshold', type=float, default=Config.TOPO_ALIGNMENT_THRESHOLD, help='Alignment threshold for topological phase transition detection')
    parser.add_argument('--no_phase5', action='store_true', help='Disable Phase 5 quadruple precision crystallization')
    parser.add_argument('--phase5_delta_target', type=float, default=Config.PHASE5_DELTA_TARGET, help='Target delta for Phase 5 crystallization')
    parser.add_argument('--phase5_alpha_target', type=float, default=Config.PHASE5_ALPHA_TARGET, help='Target alpha for Phase 5 crystallization')
    parser.add_argument('--ricci_flow_step', type=float, default=Config.RICCI_FLOW_STEP, help='Step size for Ricci flow evolution')
    return parser


def main():
    parser = build_argument_parser()
    args = parser.parse_args()
    config = Config()
    config.GRID_SIZE = args.grid_size
    config.HIDDEN_DIM = args.hidden_dim
    config.EXPANSION_DIM = args.expansion_dim
    config.NUM_SPECTRAL_LAYERS = args.num_spectral_layers
    config.EPOCHS = args.epochs
    config.REFINEMENT_EPOCHS = args.refinement_epochs
    config.PHASE5_EPOCHS = args.phase5_epochs
    config.LEARNING_RATE = args.lr
    config.LAMBDA_MAX = args.lambda_max
    config.PHASE5_LAMBDA_MAX = args.phase5_lambda_max
    config.MINING_MAX_ATTEMPTS = args.mining_attempts
    config.BACKBONE_CHECKPOINT_PATH = args.backbone_path
    config.BACKBONE_ENABLED = not args.no_backbone
    config.NUM_SAMPLES = args.num_samples
    config.SURFACE_TENSION_COEFFICIENT = args.surface_tension
    config.WILLMORE_ENERGY_WEIGHT = args.willmore_weight
    config.NUM_EIGENMODES = args.num_eigenmodes
    config.CHECKPOINT_INTERVAL_MINUTES = args.checkpoint_interval
    config.TOPO_ENABLED = not args.no_topo
    config.TOPO_ALIGNMENT_THRESHOLD = args.topo_alignment_threshold
    config.PHASE5_ENABLE = not args.no_phase5
    config.PHASE5_DELTA_TARGET = args.phase5_delta_target
    config.PHASE5_ALPHA_TARGET = args.phase5_alpha_target
    config.RICCI_FLOW_STEP = args.ricci_flow_step
    orchestrator = ExperimentOrchestrator(config)
    orchestrator.run()


if __name__ == "__main__":
    main()
