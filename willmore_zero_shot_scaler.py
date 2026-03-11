#!/usr/bin/env python3
"""
willmore_zero_shot_scaler.py

Zero-shot grid scaling for Willmore Crystal Minimal Surface Networks.

This module implements progressive grid resolution scaling from a trained model
at grid_size=16 to higher resolutions (32, 64, 128, 256, 512, 1024, 2048) using
spectral weight interpolation and zero-shot transfer.

The scaling approach preserves the learned spectral representations while
adapting the spatial discretization, enabling the model to generalize to
finer grid resolutions without retraining.

Architecture:
    - ConfigurationLoader: TOML-based configuration management
    - CheckpointManager: Model checkpoint loading and validation
    - SpectralWeightInterpolator: Fourier-space weight interpolation
    - GridScaler: Core scaling logic with progressive resolution increase
    - ScalingPipeline: Orchestrates the complete scaling process
    - MetricsEvaluator: Performance evaluation at each scale level

Usage:
    python willmore_zero_shot_scaler.py --config scaler_config.toml
"""

import argparse
import json
import logging
import math
import os
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

try:
    import tomli
except ImportError:
    import tomllib as tomli

from willmore_crsital2 import (
    Config as WillmoreConfig,
    MinimalSurfaceSpectralNetwork,
    MinimalSurfaceOperator,
    MinimalSurfaceDataset,
    MinimalSurfaceInferenceEngine,
    CrystallographyMetricsCalculator,
    WillmoreEnergyCalculator,
    SeedManager,
    LoggerFactory,
)


LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
LOGGER = logging.getLogger("WillmoreZeroShotScaler")


DEFAULT_CONFIG_TOML: str = """
[scaler]
source_grid_size = 16
target_grid_sizes = [32, 64, 128, 256, 512, 1024, 2048]
checkpoint_path = "checkpoints_phase3/checkpoint_phase3_training_epoch_4767_20260225_193336.pth"
output_dir = "scaled_models"
device = "cpu"
seed = 42

[interpolation]
method = "fourier"
boundary_mode = "reflect"
preserve_spectral_structure = true
amplitude_normalization = true
phase_preservation = true

[validation]
num_test_samples = 100
compute_willmore_energy = true
compute_curvature_metrics = true
compute_spectral_metrics = true
mse_threshold = 0.05

[progressive]
enable_progressive = true
validate_each_step = true
save_intermediate = true
early_stop_on_degradation = true
degradation_threshold = 0.5

[metrics]
track_willmore_energy = true
track_mean_curvature = true
track_gaussian_curvature = true
track_surface_area = true
track_spectral_concentration = true
track_phase_coherence = true

[output]
save_pytorch_format = true
save_json_metrics = true
save_detailed_report = true
compress_checkpoints = false
"""


@dataclass
class ScalerConfig:
    """Configuration dataclass for the zero-shot scaler."""
    source_grid_size: int = 16
    target_grid_sizes: List[int] = field(default_factory=lambda: [32, 64, 128, 256, 512, 1024, 2048])
    checkpoint_path: str = ""
    output_dir: str = "scaled_models"
    device: str = "cpu"
    seed: int = 42
    interpolation_method: str = "fourier"
    boundary_mode: str = "reflect"
    preserve_spectral_structure: bool = True
    amplitude_normalization: bool = True
    phase_preservation: bool = True
    num_test_samples: int = 100
    compute_willmore_energy: bool = True
    compute_curvature_metrics: bool = True
    compute_spectral_metrics: bool = True
    mse_threshold: float = 0.05
    enable_progressive: bool = True
    validate_each_step: bool = True
    save_intermediate: bool = True
    early_stop_on_degradation: bool = True
    degradation_threshold: float = 0.5
    save_pytorch_format: bool = True
    save_json_metrics: bool = True
    save_detailed_report: bool = True
    compress_checkpoints: bool = False


class IConfigurationLoader(ABC):
    """Abstract interface for configuration loading."""
    
    @abstractmethod
    def load(self, source: Union[str, Path, Dict[str, Any]]) -> ScalerConfig:
        """Load configuration from the specified source."""
        pass


class TOMLConfigurationLoader(IConfigurationLoader):
    """TOML-based configuration loader."""
    
    def load(self, source: Union[str, Path, Dict[str, Any]]) -> ScalerConfig:
        if isinstance(source, dict):
            return self._from_dict(source)
        return self._from_toml(Path(source))
    
    def _from_toml(self, path: Path) -> ScalerConfig:
        if not path.exists():
            LOGGER.warning(f"Config file {path} not found, using defaults")
            return self._from_dict({})
        
        with open(path, "rb") as f:
            data = tomli.load(f)
        return self._from_dict(data)
    
    def _from_dict(self, data: Dict[str, Any]) -> ScalerConfig:
        scaler = data.get("scaler", {})
        interp = data.get("interpolation", {})
        valid = data.get("validation", {})
        prog = data.get("progressive", {})
        metrics = data.get("metrics", {})
        output = data.get("output", {})
        
        return ScalerConfig(
            source_grid_size=scaler.get("source_grid_size", 16),
            target_grid_sizes=scaler.get("target_grid_sizes", [32, 64, 128, 256, 512, 1024, 2048]),
            checkpoint_path=scaler.get("checkpoint_path", ""),
            output_dir=scaler.get("output_dir", "scaled_models"),
            device=scaler.get("device", "cpu"),
            seed=scaler.get("seed", 42),
            interpolation_method=interp.get("method", "fourier"),
            boundary_mode=interp.get("boundary_mode", "reflect"),
            preserve_spectral_structure=interp.get("preserve_spectral_structure", True),
            amplitude_normalization=interp.get("amplitude_normalization", True),
            phase_preservation=interp.get("phase_preservation", True),
            num_test_samples=valid.get("num_test_samples", 100),
            compute_willmore_energy=valid.get("compute_willmore_energy", True),
            compute_curvature_metrics=valid.get("compute_curvature_metrics", True),
            compute_spectral_metrics=valid.get("compute_spectral_metrics", True),
            mse_threshold=valid.get("mse_threshold", 0.05),
            enable_progressive=prog.get("enable_progressive", True),
            validate_each_step=prog.get("validate_each_step", True),
            save_intermediate=prog.get("save_intermediate", True),
            early_stop_on_degradation=prog.get("early_stop_on_degradation", True),
            degradation_threshold=prog.get("degradation_threshold", 0.5),
            save_pytorch_format=output.get("save_pytorch_format", True),
            save_json_metrics=output.get("save_json_metrics", True),
            save_detailed_report=output.get("save_detailed_report", True),
            compress_checkpoints=output.get("compress_checkpoints", False),
        )


class ICheckpointManager(ABC):
    """Abstract interface for checkpoint management."""
    
    @abstractmethod
    def load_checkpoint(self, path: str, device: str) -> Dict[str, Any]:
        """Load a model checkpoint from disk."""
        pass
    
    @abstractmethod
    def save_checkpoint(self, model: nn.Module, metrics: Dict[str, Any], path: str) -> None:
        """Save a model checkpoint to disk."""
        pass


class WillmoreCheckpointManager(ICheckpointManager):
    """Checkpoint manager for Willmore Crystal models."""
    
    def __init__(self, config: ScalerConfig):
        self._config = config
        self._logger = LoggerFactory.create_logger("WillmoreCheckpointManager")
    
    def load_checkpoint(self, path: str, device: str) -> Dict[str, Any]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Checkpoint not found: {path}")
        
        self._logger.info(f"Loading checkpoint from {path}")
        checkpoint = torch.load(path, map_location=device, weights_only=False)
        
        required_keys = ["model_state_dict"]
        for key in required_keys:
            if key not in checkpoint:
                raise ValueError(f"Invalid checkpoint: missing key '{key}'")
        
        if "config" in checkpoint:
            stored_config = checkpoint["config"]
            self._logger.info(f"Checkpoint config: grid_size={stored_config.get('GRID_SIZE', 'unknown')}")
        
        return checkpoint
    
    def save_checkpoint(self, model: nn.Module, metrics: Dict[str, Any], path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        checkpoint = {
            "model_state_dict": model.state_dict(),
            "metrics": metrics,
            "timestamp": datetime.now().isoformat(),
            "grid_size": getattr(model, "grid_size", "unknown"),
        }
        
        torch.save(checkpoint, path)
        self._logger.info(f"Checkpoint saved to {path}")


class ISpectralWeightInterpolator(ABC):
    """Abstract interface for spectral weight interpolation."""
    
    @abstractmethod
    def interpolate(
        self,
        source_weight: torch.Tensor,
        target_shape: Tuple[int, ...],
        **kwargs,
    ) -> torch.Tensor:
        """Interpolate spectral weights to a new shape."""
        pass


class FourierSpectralInterpolator(ISpectralWeightInterpolator):
    """Fourier-based spectral weight interpolation."""
    
    def __init__(self, config: ScalerConfig):
        self._config = config
        self._logger = LoggerFactory.create_logger("FourierSpectralInterpolator")
    
    def interpolate(
        self,
        source_weight: torch.Tensor,
        target_shape: Tuple[int, ...],
        **kwargs,
    ) -> torch.Tensor:
        if source_weight.dim() == 2:
            return self._interpolate_2d_spectral(source_weight, target_shape)
        elif source_weight.dim() == 4:
            return self._interpolate_4d_spectral(source_weight, target_shape)
        else:
            return self._interpolate_generic(source_weight, target_shape)
    
    def _interpolate_2d_spectral(
        self,
        source: torch.Tensor,
        target_shape: Tuple[int, int],
    ) -> torch.Tensor:
        source_fft = torch.fft.fft2(source)
        source_h, source_w = source.shape
        target_h, target_w = target_shape
        
        padded_fft = self._pad_spectrum_2d(source_fft, target_h, target_w)
        result = torch.fft.ifft2(padded_fft).real
        
        if self._config.amplitude_normalization:
            source_norm = torch.norm(source)
            result_norm = torch.norm(result)
            if result_norm > 1e-10:
                result = result * (source_norm / result_norm)
        
        return result
    
    def _interpolate_4d_spectral(
        self,
        source: torch.Tensor,
        target_shape: Tuple[int, int, int, int],
    ) -> torch.Tensor:
        out_channels, in_channels, source_h, source_w = source.shape
        target_h, target_w = target_shape[2], target_shape[3]
        
        result = torch.zeros(out_channels, in_channels, target_h, target_w, dtype=source.dtype)
        
        for oc in range(out_channels):
            for ic in range(in_channels):
                result[oc, ic] = self._interpolate_2d_spectral(
                    source[oc, ic], (target_h, target_w)
                )
        
        return result
    
    def _pad_spectrum_2d(
        self,
        spectrum: torch.Tensor,
        target_h: int,
        target_w: int,
    ) -> torch.Tensor:
        source_h, source_w = spectrum.shape
        
        if target_h <= source_h and target_w <= source_w:
            return spectrum[:target_h, :target_w]
        
        result = torch.zeros(target_h, target_w, dtype=spectrum.dtype)
        
        half_h_source = source_h // 2
        half_w_source = source_w // 2
        half_h_target = target_h // 2
        half_w_target = target_w // 2
        
        if source_h % 2 == 0:
            h_indices_source = list(range(half_h_source)) + list(range(source_h - half_h_source, source_h))
        else:
            h_indices_source = list(range(half_h_source + 1)) + list(range(source_h - half_h_source, source_h))
        
        if target_h % 2 == 0:
            h_indices_target = list(range(half_h_target)) + list(range(target_h - half_h_target, target_h))
        else:
            h_indices_target = list(range(half_h_target + 1)) + list(range(target_h - half_h_target, target_h))
        
        min_h = min(len(h_indices_source), len(h_indices_target))
        
        for i in range(min_h):
            src_i = h_indices_source[i]
            tgt_i = h_indices_target[i]
            result[tgt_i, :min(source_w, target_w)] = spectrum[src_i, :min(source_w, target_w)]
        
        return result
    
    def _interpolate_generic(
        self,
        source: torch.Tensor,
        target_shape: Tuple[int, ...],
    ) -> torch.Tensor:
        source_flat = source.flatten().unsqueeze(0).unsqueeze(0)
        target_size = int(np.prod(target_shape))
        
        interpolated = F.interpolate(
            source_flat,
            size=target_size,
            mode="linear",
            align_corners=False,
        )
        
        return interpolated.view(target_shape)


class BilinearSpectralInterpolator(ISpectralWeightInterpolator):
    """Bilinear interpolation for spectral weights."""
    
    def __init__(self, config: ScalerConfig):
        self._config = config
        self._logger = LoggerFactory.create_logger("BilinearSpectralInterpolator")
    
    def interpolate(
        self,
        source_weight: torch.Tensor,
        target_shape: Tuple[int, ...],
        **kwargs,
    ) -> torch.Tensor:
        if source_weight.dim() == 2:
            source = source_weight.unsqueeze(0).unsqueeze(0)
            result = F.interpolate(
                source,
                size=target_shape,
                mode="bilinear",
                align_corners=False,
            )
            return result.squeeze(0).squeeze(0)
        elif source_weight.dim() == 4:
            return F.interpolate(
                source_weight,
                size=target_shape[2:],
                mode="bilinear",
                align_corners=False,
            )
        else:
            return self._interpolate_generic(source_weight, target_shape)
    
    def _interpolate_generic(
        self,
        source: torch.Tensor,
        target_shape: Tuple[int, ...],
    ) -> torch.Tensor:
        source_flat = source.flatten().unsqueeze(0).unsqueeze(0)
        target_size = int(np.prod(target_shape))
        
        interpolated = F.interpolate(
            source_flat,
            size=target_size,
            mode="linear",
            align_corners=False,
        )
        
        result = interpolated.view(target_shape)
        
        if self._config.amplitude_normalization:
            source_norm = torch.norm(source)
            result_norm = torch.norm(result)
            if result_norm > 1e-10:
                result = result * (source_norm / result_norm)
        
        return result


class IGridScaler(ABC):
    """Abstract interface for grid scaling."""
    
    @abstractmethod
    def scale_model(
        self,
        source_model: nn.Module,
        target_grid_size: int,
    ) -> nn.Module:
        """Scale a model to a new grid resolution."""
        pass


class WillmoreGridScaler(IGridScaler):
    """Grid scaler for Willmore Crystal networks."""
    
    def __init__(
        self,
        config: ScalerConfig,
        interpolator: ISpectralWeightInterpolator,
    ):
        self._config = config
        self._interpolator = interpolator
        self._logger = LoggerFactory.create_logger("WillmoreGridScaler")
    
    def scale_model(
        self,
        source_model: nn.Module,
        target_grid_size: int,
    ) -> nn.Module:
        source_grid = getattr(source_model, "grid_size", self._config.source_grid_size)
        self._logger.info(f"Scaling model from grid_size={source_grid} to grid_size={target_grid_size}")
        
        hidden_dim = self._extract_hidden_dim(source_model)
        expansion_dim = self._extract_expansion_dim(source_model)
        num_spectral_layers = self._count_spectral_layers(source_model)
        
        target_model = MinimalSurfaceSpectralNetwork(
            grid_size=target_grid_size,
            hidden_dim=hidden_dim,
            expansion_dim=expansion_dim,
            num_spectral_layers=num_spectral_layers,
        ).to(self._config.device)
        
        self._transfer_weights(source_model, target_model, source_grid, target_grid_size)
        
        self._validate_weight_transfer(source_model, target_model)
        
        return target_model
    
    def _extract_hidden_dim(self, model: nn.Module) -> int:
        if hasattr(model, "input_proj"):
            return model.input_proj.out_channels
        return 32
    
    def _extract_expansion_dim(self, model: nn.Module) -> int:
        if hasattr(model, "expansion_proj"):
            return model.expansion_proj.out_channels
        return 64
    
    def _count_spectral_layers(self, model: nn.Module) -> int:
        if hasattr(model, "spectral_layers"):
            return len(model.spectral_layers)
        return 2
    
    def _transfer_weights(
        self,
        source: nn.Module,
        target: nn.Module,
        source_grid: int,
        target_grid: int,
    ) -> None:
        source_state = source.state_dict()
        target_state = target.state_dict()
        
        for name, param in source_state.items():
            if name in target_state:
                target_shape = target_state[name].shape
                
                if param.shape == target_shape:
                    target_state[name] = param.clone()
                elif "spectral_layers" in name and ("kernel_real" in name or "kernel_imag" in name):
                    target_state[name] = self._scale_spectral_kernel(
                        param, target_shape, source_grid, target_grid
                    )
                else:
                    target_state[name] = self._scale_conv_weight(param, target_shape)
        
        target.load_state_dict(target_state)
    
    def _scale_spectral_kernel(
        self,
        kernel: torch.Tensor,
        target_shape: Tuple[int, ...],
        source_grid: int,
        target_grid: int,
    ) -> torch.Tensor:
        scale_factor = target_grid / source_grid
        
        if kernel.dim() == 4:
            return self._interpolator.interpolate(kernel, target_shape)
        else:
            return self._interpolator.interpolate(kernel, target_shape)
    
    def _scale_conv_weight(
        self,
        weight: torch.Tensor,
        target_shape: Tuple[int, ...],
    ) -> torch.Tensor:
        if weight.dim() == 4:
            return self._interpolator.interpolate(weight, target_shape)
        elif weight.dim() == 2:
            return self._interpolator.interpolate(weight, target_shape)
        elif weight.dim() == 1:
            if weight.shape[0] == target_shape[0]:
                return weight.clone()
            elif weight.shape[0] < target_shape[0]:
                result = torch.zeros(target_shape, dtype=weight.dtype)
                result[:weight.shape[0]] = weight
                return result
            else:
                return weight[:target_shape[0]].clone()
        
        return weight
    
    def _validate_weight_transfer(
        self,
        source: nn.Module,
        target: nn.Module,
    ) -> None:
        source_params = sum(p.numel() for p in source.parameters())
        target_params = sum(p.numel() for p in target.parameters())
        
        self._logger.info(
            f"Weight transfer complete: {source_params:,} -> {target_params:,} parameters"
        )


class IMetricsEvaluator(ABC):
    """Abstract interface for metrics evaluation."""
    
    @abstractmethod
    def evaluate(
        self,
        model: nn.Module,
        grid_size: int,
        num_samples: int,
    ) -> Dict[str, Any]:
        """Evaluate model performance and metrics."""
        pass


class WillmoreMetricsEvaluator(IMetricsEvaluator):
    """Metrics evaluator for Willmore Crystal models."""
    
    def __init__(self, config: ScalerConfig):
        self._config = config
        self._willmore_calc = None
        self._surface_op = None
        self._logger = LoggerFactory.create_logger("WillmoreMetricsEvaluator")
    
    def evaluate(
        self,
        model: nn.Module,
        grid_size: int,
        num_samples: int,
    ) -> Dict[str, Any]:
        self._surface_op = MinimalSurfaceOperator(grid_size)
        
        metrics = {
            "grid_size": grid_size,
            "timestamp": datetime.now().isoformat(),
            "num_parameters": sum(p.numel() for p in model.parameters()),
        }
        
        weight_surface = self._construct_weight_surface(model, grid_size)
        
        if self._config.compute_willmore_energy:
            willmore_metrics = self._compute_willmore_metrics(weight_surface)
            metrics.update(willmore_metrics)
        
        if self._config.compute_curvature_metrics:
            curvature_metrics = self._compute_curvature_metrics(weight_surface)
            metrics.update(curvature_metrics)
        
        if self._config.compute_spectral_metrics:
            spectral_metrics = self._compute_spectral_metrics(model)
            metrics.update(spectral_metrics)
        
        inference_metrics = self._evaluate_inference_quality(model, grid_size, num_samples)
        metrics.update(inference_metrics)
        
        return metrics
    
    def _construct_weight_surface(
        self,
        model: nn.Module,
        grid_size: int,
    ) -> torch.Tensor:
        weights = []
        for param in model.parameters():
            if param.numel() > 0:
                weights.append(param.detach().flatten())
        
        if not weights:
            return torch.zeros(grid_size, grid_size)
        
        all_weights = torch.cat(weights)[:grid_size * grid_size]
        
        if all_weights.numel() < grid_size * grid_size:
            padded = torch.zeros(grid_size * grid_size)
            padded[:all_weights.numel()] = all_weights
            all_weights = padded
        
        return all_weights[:grid_size * grid_size].view(grid_size, grid_size)
    
    def _compute_willmore_metrics(
        self,
        surface: torch.Tensor,
    ) -> Dict[str, Any]:
        try:
            willmore_energy = self._surface_op.compute_willmore_energy(surface)
            surface_area = self._surface_op.compute_surface_area(surface)
            
            return {
                "willmore_energy": float(willmore_energy.item()),
                "surface_area": float(surface_area.item()),
            }
        except Exception as e:
            self._logger.warning(f"Willmore computation failed: {e}")
            return {"willmore_energy": float("inf"), "surface_area": 0.0}
    
    def _compute_curvature_metrics(
        self,
        surface: torch.Tensor,
    ) -> Dict[str, Any]:
        try:
            mean_curvature = self._surface_op.compute_mean_curvature(surface)
            gaussian_curvature = self._surface_op.compute_gaussian_curvature(surface)
            
            return {
                "mean_curvature_mean": float(mean_curvature.mean().item()),
                "mean_curvature_std": float(mean_curvature.std().item()),
                "mean_curvature_max": float(mean_curvature.max().item()),
                "gaussian_curvature_mean": float(gaussian_curvature.mean().item()),
                "gaussian_curvature_std": float(gaussian_curvature.std().item()),
            }
        except Exception as e:
            self._logger.warning(f"Curvature computation failed: {e}")
            return {
                "mean_curvature_mean": 0.0,
                "mean_curvature_std": 0.0,
                "mean_curvature_max": 0.0,
                "gaussian_curvature_mean": 0.0,
                "gaussian_curvature_std": 0.0,
            }
    
    def _compute_spectral_metrics(
        self,
        model: nn.Module,
    ) -> Dict[str, Any]:
        try:
            weights = []
            for name, param in model.named_parameters():
                if "spectral" in name and param.numel() > 0:
                    weights.append(param.detach().flatten())
            
            if not weights:
                return {"spectral_concentration": 0.0, "phase_coherence": 0.0}
            
            spectral_weights = torch.cat(weights)
            fft_spectrum = torch.fft.fft(spectral_weights)
            power_spectrum = torch.abs(fft_spectrum) ** 2
            
            total_power = power_spectrum.sum()
            max_power = power_spectrum.max()
            spectral_concentration = (max_power / (total_power + 1e-10)).item()
            
            phase = torch.angle(fft_spectrum)
            phase_coherence = torch.abs(torch.mean(torch.exp(1j * phase))).item()
            
            return {
                "spectral_concentration": spectral_concentration,
                "phase_coherence": phase_coherence,
                "spectral_power_total": float(total_power.item()),
            }
        except Exception as e:
            self._logger.warning(f"Spectral metrics computation failed: {e}")
            return {"spectral_concentration": 0.0, "phase_coherence": 0.0}
    
    def _evaluate_inference_quality(
        self,
        model: nn.Module,
        grid_size: int,
        num_samples: int,
    ) -> Dict[str, Any]:
        try:
            model.eval()
            
            test_input = torch.randn(1, 2, grid_size, grid_size)
            
            with torch.no_grad():
                output = model(test_input)
            
            output_norm = torch.norm(output).item()
            input_norm = torch.norm(test_input).item()
            
            output_variance = output.var().item()
            output_mean = output.mean().item()
            
            return {
                "inference_output_norm": output_norm,
                "inference_input_norm": input_norm,
                "inference_norm_ratio": output_norm / (input_norm + 1e-10),
                "inference_output_variance": output_variance,
                "inference_output_mean": output_mean,
                "inference_successful": True,
            }
        except Exception as e:
            self._logger.warning(f"Inference evaluation failed: {e}")
            return {
                "inference_output_norm": 0.0,
                "inference_input_norm": 0.0,
                "inference_norm_ratio": 0.0,
                "inference_output_variance": 0.0,
                "inference_output_mean": 0.0,
                "inference_successful": False,
                "inference_error": str(e),
            }


class ScalingPipeline:
    """Orchestrates the complete progressive scaling process."""
    
    def __init__(self, config: ScalerConfig):
        self._config = config
        self._checkpoint_manager = WillmoreCheckpointManager(config)
        
        if config.interpolation_method == "fourier":
            interpolator = FourierSpectralInterpolator(config)
        else:
            interpolator = BilinearSpectralInterpolator(config)
        
        self._scaler = WillmoreGridScaler(config, interpolator)
        self._evaluator = WillmoreMetricsEvaluator(config)
        self._logger = LoggerFactory.create_logger("ScalingPipeline")
        
        self._results: List[Dict[str, Any]] = []
        self._best_model: Optional[nn.Module] = None
        self._best_metrics: Optional[Dict[str, Any]] = None
    
    def execute(self) -> Dict[str, Any]:
        self._logger.info("=" * 80)
        self._logger.info("WILLMORE CRYSTAL ZERO-SHOT GRID SCALING")
        self._logger.info("=" * 80)
        
        SeedManager.set_seed(self._config.seed, self._config.device)
        
        os.makedirs(self._config.output_dir, exist_ok=True)
        
        source_model = self._load_source_model()
        source_metrics = self._evaluator.evaluate(
            source_model,
            self._config.source_grid_size,
            self._config.num_test_samples,
        )
        
        self._results.append({
            "stage": "source",
            "grid_size": self._config.source_grid_size,
            "metrics": source_metrics,
        })
        
        self._logger.info(f"Source model metrics: Willmore={source_metrics.get('willmore_energy', 'N/A'):.4f}")
        
        current_model = source_model
        current_grid = self._config.source_grid_size
        
        for target_grid in self._config.target_grid_sizes:
            self._logger.info("-" * 80)
            self._logger.info(f"SCALING: {current_grid} -> {target_grid}")
            self._logger.info("-" * 80)
            
            try:
                start_time = time.time()
                
                scaled_model = self._scaler.scale_model(current_model, target_grid)
                
                scaling_time = time.time() - start_time
                
                if self._config.validate_each_step:
                    metrics = self._evaluator.evaluate(
                        scaled_model,
                        target_grid,
                        self._config.num_test_samples,
                    )
                else:
                    metrics = {"grid_size": target_grid}
                
                metrics["scaling_time_seconds"] = scaling_time
                metrics["scale_factor"] = target_grid / current_grid
                
                self._results.append({
                    "stage": "scaled",
                    "source_grid": current_grid,
                    "target_grid": target_grid,
                    "metrics": metrics,
                })
                
                self._log_metrics(metrics, target_grid)
                
                if self._config.save_intermediate:
                    self._save_scaled_model(scaled_model, metrics, target_grid)
                
                degradation = self._check_degradation(source_metrics, metrics)
                
                if degradation and self._config.early_stop_on_degradation:
                    self._logger.warning(
                        f"Degradation detected at grid_size={target_grid}, stopping early"
                    )
                    break
                
                current_model = scaled_model
                current_grid = target_grid
                
                if self._best_metrics is None or self._is_better_metrics(metrics, self._best_metrics):
                    self._best_model = scaled_model
                    self._best_metrics = metrics
                
            except Exception as e:
                self._logger.error(f"Scaling to {target_grid} failed: {e}")
                self._results.append({
                    "stage": "failed",
                    "target_grid": target_grid,
                    "error": str(e),
                })
                break
        
        final_results = self._compile_final_results()
        self._save_final_results(final_results)
        
        return final_results
    
    def _load_source_model(self) -> nn.Module:
        checkpoint = self._checkpoint_manager.load_checkpoint(
            self._config.checkpoint_path,
            self._config.device,
        )
        
        stored_config = checkpoint.get("config", {})
        grid_size = stored_config.get("GRID_SIZE", self._config.source_grid_size)
        hidden_dim = stored_config.get("HIDDEN_DIM", 32)
        expansion_dim = stored_config.get("EXPANSION_DIM", 64)
        num_spectral_layers = stored_config.get("NUM_SPECTRAL_LAYERS", 2)
        
        model = MinimalSurfaceSpectralNetwork(
            grid_size=grid_size,
            hidden_dim=hidden_dim,
            expansion_dim=expansion_dim,
            num_spectral_layers=num_spectral_layers,
        ).to(self._config.device)
        
        model.load_state_dict(checkpoint["model_state_dict"])
        model.eval()
        
        self._logger.info(f"Source model loaded: grid_size={grid_size}")
        
        return model
    
    def _log_metrics(self, metrics: Dict[str, Any], grid_size: int) -> None:
        self._logger.info(f"Grid Size: {grid_size}")
        self._logger.info(f"  Parameters: {metrics.get('num_parameters', 'N/A'):,}")
        
        if "willmore_energy" in metrics:
            self._logger.info(f"  Willmore Energy: {metrics['willmore_energy']:.4f}")
        
        if "mean_curvature_mean" in metrics:
            self._logger.info(f"  Mean Curvature: {metrics['mean_curvature_mean']:.4f}")
        
        if "spectral_concentration" in metrics:
            self._logger.info(f"  Spectral Concentration: {metrics['spectral_concentration']:.4f}")
        
        if "inference_successful" in metrics:
            self._logger.info(f"  Inference: {'SUCCESS' if metrics['inference_successful'] else 'FAILED'}")
    
    def _check_degradation(
        self,
        source_metrics: Dict[str, Any],
        current_metrics: Dict[str, Any],
    ) -> bool:
        source_willmore = source_metrics.get("willmore_energy", float("inf"))
        current_willmore = current_metrics.get("willmore_energy", float("inf"))
        
        if source_willmore == float("inf") or current_willmore == float("inf"):
            return False
        
        if current_willmore > source_willmore * (1 + self._config.degradation_threshold):
            return True
        
        return False
    
    def _is_better_metrics(
        self,
        current: Dict[str, Any],
        best: Dict[str, Any],
    ) -> bool:
        current_willmore = current.get("willmore_energy", float("inf"))
        best_willmore = best.get("willmore_energy", float("inf"))
        
        if current_willmore == float("inf"):
            return False
        if best_willmore == float("inf"):
            return True
        
        return current_willmore < best_willmore
    
    def _save_scaled_model(
        self,
        model: nn.Module,
        metrics: Dict[str, Any],
        grid_size: int,
    ) -> None:
        filename = f"scaled_model_grid_{grid_size}.pth"
        path = os.path.join(self._config.output_dir, filename)
        self._checkpoint_manager.save_checkpoint(model, metrics, path)
    
    def _compile_final_results(self) -> Dict[str, Any]:
        return {
            "source_grid_size": self._config.source_grid_size,
            "target_grid_sizes": self._config.target_grid_sizes,
            "scaling_history": self._results,
            "best_metrics": self._best_metrics,
            "config": {
                "interpolation_method": self._config.interpolation_method,
                "amplitude_normalization": self._config.amplitude_normalization,
                "phase_preservation": self._config.phase_preservation,
            },
            "timestamp": datetime.now().isoformat(),
        }
    
    def _save_final_results(self, results: Dict[str, Any]) -> None:
        if self._config.save_json_metrics:
            json_path = os.path.join(self._config.output_dir, "scaling_results.json")
            with open(json_path, "w") as f:
                json.dump(results, f, indent=2, default=str)
            self._logger.info(f"Results saved to {json_path}")
        
        if self._config.save_detailed_report:
            report_path = os.path.join(self._config.output_dir, "scaling_report.txt")
            self._write_detailed_report(results, report_path)
            self._logger.info(f"Detailed report saved to {report_path}")
    
    def _write_detailed_report(
        self,
        results: Dict[str, Any],
        path: str,
    ) -> None:
        with open(path, "w") as f:
            f.write("=" * 80 + "\n")
            f.write("WILLMORE CRYSTAL ZERO-SHOT GRID SCALING REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Source Grid Size: {results['source_grid_size']}\n")
            f.write(f"Target Grid Sizes: {results['target_grid_sizes']}\n")
            f.write(f"Timestamp: {results['timestamp']}\n\n")
            
            f.write("-" * 80 + "\n")
            f.write("SCALING HISTORY\n")
            f.write("-" * 80 + "\n\n")
            
            for entry in results["scaling_history"]:
                stage = entry.get("stage", "unknown")
                f.write(f"Stage: {stage}\n")
                
                if "grid_size" in entry:
                    f.write(f"  Grid Size: {entry['grid_size']}\n")
                
                if "source_grid" in entry and "target_grid" in entry:
                    f.write(f"  Scale: {entry['source_grid']} -> {entry['target_grid']}\n")
                
                metrics = entry.get("metrics", {})
                for key, value in metrics.items():
                    if isinstance(value, float):
                        f.write(f"  {key}: {value:.6f}\n")
                    else:
                        f.write(f"  {key}: {value}\n")
                
                f.write("\n")
            
            if results.get("best_metrics"):
                f.write("-" * 80 + "\n")
                f.write("BEST METRICS\n")
                f.write("-" * 80 + "\n\n")
                
                for key, value in results["best_metrics"].items():
                    if isinstance(value, float):
                        f.write(f"{key}: {value:.6f}\n")
                    else:
                        f.write(f"{key}: {value}\n")


def create_default_config_file(path: str) -> None:
    """Create a default configuration file."""
    with open(path, "w") as f:
        f.write(DEFAULT_CONFIG_TOML)
    LOGGER.info(f"Default configuration written to {path}")


def build_argument_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Willmore Crystal Zero-Shot Grid Scaler",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to TOML configuration file",
    )
    
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="checkpoints_phase3/checkpoint_phase3_training_epoch_4767_20260225_193336.pth",
        help="Path to source model checkpoint",
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default="scaled_models",
        help="Output directory for scaled models",
    )
    
    parser.add_argument(
        "--device",
        type=str,
        default="cpu",
        choices=["cpu", "cuda"],
        help="Device for computation",
    )
    
    parser.add_argument(
        "--source-grid",
        type=int,
        default=16,
        help="Source model grid size",
    )
    
    parser.add_argument(
        "--target-grids",
        type=int,
        nargs="+",
        default=[32, 64, 128, 256, 512, 1024, 2048],
        help="Target grid sizes for progressive scaling",
    )
    
    parser.add_argument(
        "--interpolation",
        type=str,
        default="fourier",
        choices=["fourier", "bilinear"],
        help="Weight interpolation method",
    )
    
    parser.add_argument(
        "--generate-config",
        type=str,
        default=None,
        help="Generate default configuration file at specified path",
    )
    
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility",
    )
    
    return parser


def main() -> int:
    """Main entry point for the zero-shot scaler."""
    parser = build_argument_parser()
    args = parser.parse_args()
    
    if args.generate_config:
        create_default_config_file(args.generate_config)
        return 0
    
    config_loader = TOMLConfigurationLoader()
    
    if args.config:
        config = config_loader.load(args.config)
    else:
        override_dict = {
            "scaler": {
                "checkpoint_path": args.checkpoint,
                "output_dir": args.output_dir,
                "device": args.device,
                "source_grid_size": args.source_grid,
                "target_grid_sizes": args.target_grids,
                "seed": args.seed,
            },
            "interpolation": {
                "method": args.interpolation,
            },
        }
        config = config_loader.load(override_dict)
    
    LOGGER.info(f"Configuration loaded:")
    LOGGER.info(f"  Source grid: {config.source_grid_size}")
    LOGGER.info(f"  Target grids: {config.target_grid_sizes}")
    LOGGER.info(f"  Interpolation: {config.interpolation_method}")
    LOGGER.info(f"  Device: {config.device}")
    
    pipeline = ScalingPipeline(config)
    
    try:
        results = pipeline.execute()
        
        LOGGER.info("=" * 80)
        LOGGER.info("SCALING COMPLETE")
        LOGGER.info("=" * 80)
        
        if results.get("best_metrics"):
            best = results["best_metrics"]
            LOGGER.info(f"Best Willmore Energy: {best.get('willmore_energy', 'N/A'):.4f}")
            LOGGER.info(f"Best Grid Size: {best.get('grid_size', 'N/A')}")
        
        return 0
        
    except FileNotFoundError as e:
        LOGGER.error(f"File not found: {e}")
        return 1
    except ValueError as e:
        LOGGER.error(f"Configuration error: {e}")
        return 2
    except RuntimeError as e:
        LOGGER.error(f"Runtime error: {e}")
        return 3
    except Exception as e:
        LOGGER.error(f"Unexpected error: {e}")
        return 4


if __name__ == "__main__":
    sys.exit(main())