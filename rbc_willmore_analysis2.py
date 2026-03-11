#!/usr/bin/env python3
"""
rbc_willmore_analysis.py

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
Date: 2026
License: AGPL v3

Description:
Red Blood Cell Morphology Analysis via Willmore Energy Minimization.

This script analyzes Red Blood Cell (RBC) membrane geometry using the
Willmore energy model. The biconcave disc shape of healthy RBCs emerges
naturally from minimizing the Willmore energy functional:

    W = integral((H - H0)^2 dA)

where H is the mean curvature and H0 is the spontaneous curvature.

The analysis uses real RBC mesh data from OpenRBC (protein-resolution
simulator) to validate whether the trained Willmore model can detect
the characteristic biconcave shape and distinguish healthy from
pathological morphologies.

Scientific basis:
- Helfrich-Canham membrane bending energy model
- Gauss-Bonnet theorem for closed surfaces
- Mean curvature flow as shape relaxation dynamics
- Differential geometry of membrane surfaces
"""

import argparse
import json
import logging
import math
import os
import sys
import warnings
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

warnings.filterwarnings('ignore')


@dataclass
class RBCAnalysisConfig:
    """Configuration container for RBC Willmore analysis.

    This dataclass holds all configuration parameters for the analysis
    pipeline, including mesh processing, model loading, and visualization
    settings.
    """
    CHECKPOINT_PATH: str = "checkpoints_phase3/checkpoint_phase3_training_epoch_4767_20260225_193336.pth"
    RBC_VERT_PATH: str = "rbc.vert.txt"
    RBC_FACE_PATH: str = "rbc.face.txt"
    RBC_BOND_PATH: str = "rbc.bond.txt"
    OUTPUT_DIR: str = "rbc_analysis_results"
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"
    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    EXPANSION_DIM: int = 64
    NUM_SPECTRAL_LAYERS: int = 2
    SURFACE_CHANNELS: int = 2
    NORMALIZATION_EPS: float = 1e-10
    WILLMORE_ENERGY_THRESHOLD: float = 0.1
    MEAN_CURVATURE_TARGET: float = 0.0
    SPONTANEOUS_CURVATURE: float = 0.0
    MEAN_CURVATURE_FLOW_DT: float = 0.001
    RELAXATION_STEPS: int = 1000
    AREA_CONSERVATION_WEIGHT: float = 1.0
    VOLUME_CONSERVATION_WEIGHT: float = 0.5
    BENDING_RIGIDITY: float = 1.0
    LOG_LEVEL: str = "INFO"
    SAVE_MESH: bool = True
    SAVE_VISUALIZATION: bool = True
    COMPUTE_SYNTHETIC: bool = True
    SYNTHETIC_SPHERE_RADIUS: float = 1.0
    SYNTHETIC_SPHERE_RESOLUTION: int = 32
    SYNTHETIC_TORUS_R: float = 1.0
    SYNTHETIC_TORUS_r: float = 0.3
    COMPARISON_METRICS: List[str] = field(default_factory=lambda: [
        "willmore_energy",
        "mean_curvature_mean",
        "mean_curvature_variance",
        "gaussian_curvature_mean",
        "surface_area",
        "volume",
        "asphericity",
        "biconcavity_index"
    ])


class ILogger(ABC):
    """Abstract interface for logging implementations."""

    @abstractmethod
    def info(self, message: str) -> None:
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def debug(self, message: str) -> None:
        pass


class StandardLogger(ILogger):
    """Standard logging implementation using Python logging module."""

    def __init__(self, name: str, level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)


class IFileSystem(ABC):
    """Abstract interface for file system operations."""

    @abstractmethod
    def exists(self, path: str) -> bool:
        pass

    @abstractmethod
    def read_text(self, path: str) -> str:
        pass

    @abstractmethod
    def write_text(self, path: str, content: str) -> None:
        pass

    @abstractmethod
    def makedirs(self, path: str) -> None:
        pass


class StandardFileSystem(IFileSystem):
    """Standard file system implementation."""

    def exists(self, path: str) -> bool:
        return os.path.exists(path)

    def read_text(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def write_text(self, path: str, content: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def makedirs(self, path: str) -> None:
        os.makedirs(path, exist_ok=True)


@dataclass
class MeshData:
    """Container for 3D mesh data.

    Attributes:
        vertices: Nx3 numpy array of vertex positions
        faces: Mx3 numpy array of triangle face indices
        bonds: Kx2 numpy array of bond edge indices
        normals: Nx3 numpy array of vertex normals (computed)
        areas: M numpy array of face areas (computed)
    """
    vertices: np.ndarray
    faces: np.ndarray
    bonds: np.ndarray
    normals: Optional[np.ndarray] = None
    areas: Optional[np.ndarray] = None
    vertex_areas: Optional[np.ndarray] = None

    @property
    def num_vertices(self) -> int:
        return self.vertices.shape[0]

    @property
    def num_faces(self) -> int:
        return self.faces.shape[0]

    @property
    def num_bonds(self) -> int:
        return self.bonds.shape[0]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "num_vertices": self.num_vertices,
            "num_faces": self.num_faces,
            "num_bonds": self.num_bonds,
            "vertices_shape": self.vertices.shape,
            "faces_shape": self.faces.shape,
            "bonds_shape": self.bonds.shape,
        }


class IMeshLoader(ABC):
    """Abstract interface for mesh loading implementations."""

    @abstractmethod
    def load(self, vert_path: str, face_path: str, bond_path: str) -> MeshData:
        pass


class OpenRBCMeshLoader(IMeshLoader):
    """Mesh loader for OpenRBC format data files.

    OpenRBC stores mesh data in three separate text files:
    - rbc.vert.txt: Vertex positions (x, y, z per line)
    - rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)
    - rbc.bond.txt: Bond edges (2 vertex indices per line)
    """

    def __init__(self, filesystem: IFileSystem, logger: ILogger):
        self.filesystem = filesystem
        self.logger = logger

    def load(self, vert_path: str, face_path: str, bond_path: str) -> MeshData:
        self.logger.info(f"Loading mesh from {vert_path}, {face_path}, {bond_path}")

        vertices = self._load_vertices(vert_path)
        faces = self._load_faces(face_path)
        bonds = self._load_bonds(bond_path)

        self.logger.info(
            f"Loaded mesh: {vertices.shape[0]} vertices, "
            f"{faces.shape[0]} faces, {bonds.shape[0]} bonds"
        )

        mesh = MeshData(vertices=vertices, faces=faces, bonds=bonds)
        self._compute_normals(mesh)
        self._compute_areas(mesh)

        return mesh

    def _load_vertices(self, path: str) -> np.ndarray:
        if not self.filesystem.exists(path):
            raise FileNotFoundError(f"Vertex file not found: {path}")

        content = self.filesystem.read_text(path)
        lines = content.strip().split("\n")
        vertices = []

        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 3:
                try:
                    x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
                    vertices.append([x, y, z])
                except ValueError:
                    continue

        return np.array(vertices, dtype=np.float64)

    def _load_faces(self, path: str) -> np.ndarray:
        if not self.filesystem.exists(path):
            raise FileNotFoundError(f"Face file not found: {path}")

        content = self.filesystem.read_text(path)
        lines = content.strip().split("\n")
        faces = []

        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 3:
                try:
                    i1, i2, i3 = int(parts[0]), int(parts[1]), int(parts[2])
                    faces.append([i1, i2, i3])
                except ValueError:
                    continue

        faces_array = np.array(faces, dtype=np.int64)
        faces_array = faces_array - 1

        return faces_array

    def _load_bonds(self, path: str) -> np.ndarray:
        if not self.filesystem.exists(path):
            raise FileNotFoundError(f"Bond file not found: {path}")

        content = self.filesystem.read_text(path)
        lines = content.strip().split("\n")
        bonds = []

        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 2:
                try:
                    i1, i2 = int(parts[0]), int(parts[1])
                    bonds.append([i1, i2])
                except ValueError:
                    continue

        bonds_array = np.array(bonds, dtype=np.int64)
        bonds_array = bonds_array - 1

        return bonds_array

    def _compute_normals(self, mesh: MeshData) -> None:
        vertices = mesh.vertices
        faces = mesh.faces

        v0 = vertices[faces[:, 0]]
        v1 = vertices[faces[:, 1]]
        v2 = vertices[faces[:, 2]]

        edge1 = v1 - v0
        edge2 = v2 - v0

        face_normals = np.cross(edge1, edge2)
        face_norms = np.linalg.norm(face_normals, axis=1, keepdims=True)
        face_norms = np.maximum(face_norms, 1e-10)
        face_normals = face_normals / face_norms

        vertex_normals = np.zeros_like(vertices)
        for i, face in enumerate(faces):
            for v_idx in face:
                vertex_normals[v_idx] += face_normals[i]

        vertex_norms = np.linalg.norm(vertex_normals, axis=1, keepdims=True)
        vertex_norms = np.maximum(vertex_norms, 1e-10)
        mesh.normals = vertex_normals / vertex_norms

    def _compute_areas(self, mesh: MeshData) -> None:
        vertices = mesh.vertices
        faces = mesh.faces

        v0 = vertices[faces[:, 0]]
        v1 = vertices[faces[:, 1]]
        v2 = vertices[faces[:, 2]]

        edge1 = v1 - v0
        edge2 = v2 - v0

        cross = np.cross(edge1, edge2)
        mesh.areas = 0.5 * np.linalg.norm(cross, axis=1)

        mesh.vertex_areas = np.zeros(len(vertices))
        for i, face in enumerate(faces):
            for v_idx in face:
                mesh.vertex_areas[v_idx] += mesh.areas[i] / 3.0


class SyntheticMeshGenerator:
    """Generator for synthetic comparison surfaces.

    Creates reference surfaces (sphere, torus) for comparison with
    RBC morphology analysis.
    """

    def __init__(self, logger: ILogger):
        self.logger = logger

    def generate_sphere(
        self, radius: float, resolution: int
    ) -> MeshData:
        self.logger.info(
            f"Generating sphere with radius {radius}, resolution {resolution}"
        )

        phi = np.linspace(0, 2 * np.pi, resolution)
        theta = np.linspace(0, np.pi, resolution)
        phi, theta = np.meshgrid(phi, theta)

        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)

        vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)

        faces = []
        for i in range(resolution - 1):
            for j in range(resolution - 1):
                idx = i * resolution + j
                faces.append([idx, idx + 1, idx + resolution])
                faces.append([idx + 1, idx + resolution + 1, idx + resolution])

        faces = np.array(faces, dtype=np.int64)

        bonds = []
        for i in range(resolution - 1):
            for j in range(resolution - 1):
                idx = i * resolution + j
                bonds.append([idx, idx + 1])
                bonds.append([idx, idx + resolution])
        bonds = np.array(bonds, dtype=np.int64)

        mesh = MeshData(vertices=vertices, faces=faces, bonds=bonds)
        self._compute_mesh_properties(mesh)

        return mesh

    def generate_torus(
        self, R: float, r: float, resolution: int
    ) -> MeshData:
        self.logger.info(
            f"Generating torus with R={R}, r={r}, resolution {resolution}"
        )

        u = np.linspace(0, 2 * np.pi, resolution)
        v = np.linspace(0, 2 * np.pi, resolution)
        u, v = np.meshgrid(u, v)

        x = (R + r * np.cos(v)) * np.cos(u)
        y = (R + r * np.cos(v)) * np.sin(u)
        z = r * np.sin(v)

        vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)

        faces = []
        for i in range(resolution):
            for j in range(resolution):
                idx = i * resolution + j
                idx_next_i = ((i + 1) % resolution) * resolution + j
                idx_next_j = i * resolution + ((j + 1) % resolution)
                idx_next_both = ((i + 1) % resolution) * resolution + ((j + 1) % resolution)
                faces.append([idx, idx_next_j, idx_next_i])
                faces.append([idx_next_j, idx_next_both, idx_next_i])
        faces = np.array(faces, dtype=np.int64)

        bonds = []
        for i in range(resolution):
            for j in range(resolution):
                idx = i * resolution + j
                idx_next_j = i * resolution + ((j + 1) % resolution)
                idx_next_i = ((i + 1) % resolution) * resolution + j
                bonds.append([idx, idx_next_j])
                bonds.append([idx, idx_next_i])
        bonds = np.array(bonds, dtype=np.int64)

        mesh = MeshData(vertices=vertices, faces=faces, bonds=bonds)
        self._compute_mesh_properties(mesh)

        return mesh

    def generate_biconcave_disc(
        self, radius: float, thickness: float, resolution: int
    ) -> MeshData:
        self.logger.info(
            f"Generating biconcave disc with radius {radius}, "
            f"thickness {thickness}, resolution {resolution}"
        )

        u = np.linspace(0, 2 * np.pi, resolution)
        v = np.linspace(0, np.pi, resolution)
        u, v = np.meshgrid(u, v)

        r_param = np.sin(v)

        shape_factor = 1.0 - 0.7 * np.cos(2 * v)
        z_profile = np.cos(v) * shape_factor

        x = radius * r_param * np.cos(u)
        y = radius * r_param * np.sin(u)
        z = thickness * z_profile

        vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)

        faces = []
        for i in range(resolution - 1):
            for j in range(resolution - 1):
                idx = i * resolution + j
                faces.append([idx, idx + 1, idx + resolution])
                faces.append([idx + 1, idx + resolution + 1, idx + resolution])
        faces = np.array(faces, dtype=np.int64)

        bonds = []
        for i in range(resolution - 1):
            for j in range(resolution - 1):
                idx = i * resolution + j
                bonds.append([idx, idx + 1])
                bonds.append([idx, idx + resolution])
        bonds = np.array(bonds, dtype=np.int64)

        mesh = MeshData(vertices=vertices, faces=faces, bonds=bonds)
        self._compute_mesh_properties(mesh)

        return mesh

    def _compute_mesh_properties(self, mesh: MeshData) -> None:
        vertices = mesh.vertices
        faces = mesh.faces

        v0 = vertices[faces[:, 0]]
        v1 = vertices[faces[:, 1]]
        v2 = vertices[faces[:, 2]]

        edge1 = v1 - v0
        edge2 = v2 - v0

        face_normals = np.cross(edge1, edge2)
        face_norms = np.linalg.norm(face_normals, axis=1, keepdims=True)
        face_norms = np.maximum(face_norms, 1e-10)
        face_normals = face_normals / face_norms

        vertex_normals = np.zeros_like(vertices)
        for i, face in enumerate(faces):
            for v_idx in face:
                vertex_normals[v_idx] += face_normals[i]

        vertex_norms = np.linalg.norm(vertex_normals, axis=1, keepdims=True)
        vertex_norms = np.maximum(vertex_norms, 1e-10)
        mesh.normals = vertex_normals / vertex_norms

        cross = np.cross(edge1, edge2)
        mesh.areas = 0.5 * np.linalg.norm(cross, axis=1)

        mesh.vertex_areas = np.zeros(len(vertices))
        for i, face in enumerate(faces):
            for v_idx in face:
                mesh.vertex_areas[v_idx] += mesh.areas[i] / 3.0


class ICurvatureCalculator(ABC):
    """Abstract interface for curvature calculation implementations."""

    @abstractmethod
    def compute_mean_curvature(self, mesh: MeshData) -> np.ndarray:
        pass

    @abstractmethod
    def compute_gaussian_curvature(self, mesh: MeshData) -> np.ndarray:
        pass

    @abstractmethod
    def compute_willmore_energy(
        self, mesh: MeshData, mean_curvature: np.ndarray
    ) -> float:
        pass


class DiscreteCurvatureCalculator(ICurvatureCalculator):
    """Discrete curvature calculation using the cotangent formula.

    Implements the discrete differential geometry approach for computing
    mean and Gaussian curvature on triangle meshes based on the work by
    Meyer et al. (2003) and others.

    The mean curvature at a vertex is computed using the Laplace-Beltrami
    operator applied to the vertex positions:

        H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)

    where A_i is the Voronoi area around vertex i.
    """

    def __init__(self, logger: ILogger):
        self.logger = logger

    def compute_mean_curvature(self, mesh: MeshData) -> np.ndarray:
        vertices = mesh.vertices
        faces = mesh.faces
        n_vertices = len(vertices)

        mean_curvature = np.zeros(n_vertices)
        vertex_areas = np.zeros(n_vertices)

        edge_cotangents = self._compute_edge_cotangents(mesh)

        for i in range(n_vertices):
            neighbors = self._get_vertex_neighbors(i, faces)
            if len(neighbors) == 0:
                continue

            laplacian = np.zeros(3)
            for j in neighbors:
                if (i, j) in edge_cotangents:
                    cot_sum = edge_cotangents[(i, j)]
                elif (j, i) in edge_cotangents:
                    cot_sum = edge_cotangents[(j, i)]
                else:
                    cot_sum = 0.0

                laplacian += cot_sum * (vertices[j] - vertices[i])

            mixed_area = self._compute_mixed_voronoi_area(i, neighbors, vertices, faces)
            vertex_areas[i] = mixed_area

            if mixed_area > 1e-10:
                mean_curvature[i] = np.linalg.norm(laplacian) / (2.0 * mixed_area)

        mesh.vertex_areas = vertex_areas
        return mean_curvature

    def compute_gaussian_curvature(self, mesh: MeshData) -> np.ndarray:
        vertices = mesh.vertices
        faces = mesh.faces
        n_vertices = len(vertices)

        gaussian_curvature = np.zeros(n_vertices)
        angle_sums = np.zeros(n_vertices)
        vertex_areas = mesh.vertex_areas if mesh.vertex_areas is not None else np.ones(n_vertices)

        for face in faces:
            v0, v1, v2 = vertices[face[0]], vertices[face[1]], vertices[face[2]]

            e01 = v1 - v0
            e02 = v2 - v0
            e12 = v2 - v1
            e10 = v0 - v1
            e20 = v0 - v2
            e21 = v1 - v2

            norm_e01 = np.linalg.norm(e01)
            norm_e02 = np.linalg.norm(e02)
            norm_e12 = np.linalg.norm(e12)
            norm_e10 = norm_e01
            norm_e20 = norm_e02
            norm_e21 = norm_e12

            if norm_e01 > 1e-10 and norm_e02 > 1e-10:
                cos_angle_0 = np.dot(e01, e02) / (norm_e01 * norm_e02)
                cos_angle_0 = np.clip(cos_angle_0, -1.0, 1.0)
                angle_sums[face[0]] += np.arccos(cos_angle_0)

            if norm_e10 > 1e-10 and norm_e12 > 1e-10:
                cos_angle_1 = np.dot(e10, e12) / (norm_e10 * norm_e12)
                cos_angle_1 = np.clip(cos_angle_1, -1.0, 1.0)
                angle_sums[face[1]] += np.arccos(cos_angle_1)

            if norm_e20 > 1e-10 and norm_e21 > 1e-10:
                cos_angle_2 = np.dot(e20, e21) / (norm_e20 * norm_e21)
                cos_angle_2 = np.clip(cos_angle_2, -1.0, 1.0)
                angle_sums[face[2]] += np.arccos(cos_angle_2)

        for i in range(n_vertices):
            angle_defect = 2.0 * np.pi - angle_sums[i]
            if vertex_areas[i] > 1e-10:
                gaussian_curvature[i] = angle_defect / vertex_areas[i]

        return gaussian_curvature

    def compute_willmore_energy(
        self, mesh: MeshData, mean_curvature: np.ndarray
    ) -> float:
        H0 = 0.0

        if mesh.vertex_areas is None:
            self.compute_mean_curvature(mesh)

        vertex_areas = mesh.vertex_areas
        willmore_energy = 0.0

        for i in range(len(mean_curvature)):
            H = mean_curvature[i]
            dA = vertex_areas[i] if vertex_areas is not None else 1.0
            willmore_energy += (H - H0) ** 2 * dA

        return willmore_energy

    def _compute_edge_cotangents(self, mesh: MeshData) -> Dict[Tuple[int, int], float]:
        vertices = mesh.vertices
        faces = mesh.faces
        edge_cotangents = {}

        for face in faces:
            i, j, k = face
            vi, vj, vk = vertices[i], vertices[j], vertices[k]

            e_ik = vk - vi
            e_jk = vk - vj
            e_ij = vj - vi
            e_ki = vi - vk
            e_kj = vj - vk
            e_ji = vi - vj

            norm_ik = np.linalg.norm(e_ik)
            norm_jk = np.linalg.norm(e_jk)
            norm_ij = np.linalg.norm(e_ij)
            norm_ki = norm_ik
            norm_kj = norm_jk
            norm_ji = norm_ij

            if norm_ik > 1e-10 and norm_jk > 1e-10:
                cos_k = np.dot(e_ik, e_jk) / (norm_ik * norm_jk)
                cos_k = np.clip(cos_k, -0.9999, 0.9999)
                cot_k = cos_k / np.sqrt(1 - cos_k ** 2)

                edge = (min(i, j), max(i, j))
                if edge not in edge_cotangents:
                    edge_cotangents[edge] = 0.0
                edge_cotangents[edge] += cot_k

            if norm_ij > 1e-10 and norm_kj > 1e-10:
                cos_j = np.dot(e_ij, e_kj) / (norm_ij * norm_kj)
                cos_j = np.clip(cos_j, -0.9999, 0.9999)
                cot_j = cos_j / np.sqrt(1 - cos_j ** 2)

                edge = (min(i, k), max(i, k))
                if edge not in edge_cotangents:
                    edge_cotangents[edge] = 0.0
                edge_cotangents[edge] += cot_j

            if norm_ki > 1e-10 and norm_ji > 1e-10:
                cos_i = np.dot(e_ki, e_ji) / (norm_ki * norm_ji)
                cos_i = np.clip(cos_i, -0.9999, 0.9999)
                cot_i = cos_i / np.sqrt(1 - cos_i ** 2)

                edge = (min(j, k), max(j, k))
                if edge not in edge_cotangents:
                    edge_cotangents[edge] = 0.0
                edge_cotangents[edge] += cot_i

        return edge_cotangents

    def _get_vertex_neighbors(
        self, vertex_idx: int, faces: np.ndarray
    ) -> List[int]:
        neighbors = set()
        for face in faces:
            if vertex_idx in face:
                for v in face:
                    if v != vertex_idx:
                        neighbors.add(v)
        return list(neighbors)

    def _compute_mixed_voronoi_area(
        self, vertex_idx: int, neighbors: List[int],
        vertices: np.ndarray, faces: np.ndarray
    ) -> float:
        mixed_area = 0.0
        vi = vertices[vertex_idx]

        relevant_faces = []
        for face_idx, face in enumerate(faces):
            if vertex_idx in face:
                relevant_faces.append(face)

        for face in relevant_faces:
            idx_list = [v for v in face if v != vertex_idx]
            if len(idx_list) != 2:
                continue
            j, k = idx_list
            vj, vk = vertices[j], vertices[k]

            e_ij = vj - vi
            e_ik = vk - vi
            e_jk = vk - vj

            norm_ij = np.linalg.norm(e_ij)
            norm_ik = np.linalg.norm(e_ik)
            norm_jk = np.linalg.norm(e_jk)

            if norm_ij < 1e-10 or norm_ik < 1e-10 or norm_jk < 1e-10:
                continue

            cos_i = np.dot(e_ij, e_ik) / (norm_ij * norm_ik)
            cos_j = np.dot(-e_ij, e_jk) / (norm_ij * norm_jk)
            cos_k = np.dot(-e_ik, -e_jk) / (norm_ik * norm_jk)

            cos_i = np.clip(cos_i, -0.9999, 0.9999)
            cos_j = np.clip(cos_j, -0.9999, 0.9999)
            cos_k = np.clip(cos_k, -0.9999, 0.9999)

            if cos_i > 0 and cos_j > 0 and cos_k > 0:
                cot_j = cos_j / np.sqrt(1 - cos_j ** 2)
                cot_k = cos_k / np.sqrt(1 - cos_k ** 2)
                mixed_area += 0.125 * (norm_ij ** 2 * cot_k + norm_ik ** 2 * cot_j)
            else:
                if cos_i < 0:
                    mixed_area += 0.25 * 0.5 * norm_ij * norm_ik * np.sqrt(1 - cos_i ** 2)
                else:
                    mixed_area += 0.125 * norm_ij * norm_ik * np.sqrt(1 - cos_i ** 2)

        return max(mixed_area, 1e-10)


class SpectralLayer(nn.Module):
    """Spectral convolution layer for surface processing.

    Implements convolution in the frequency domain using FFT,
    allowing the network to learn global surface patterns.
    """

    def __init__(self, channels: int, grid_size: int):
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        kernel_h = grid_size // 2 + 1
        kernel_w = grid_size

        self.kernel_real = nn.Parameter(
            torch.randn(channels, channels, kernel_h, kernel_w) * 0.1
        )
        self.kernel_imag = nn.Parameter(
            torch.randn(channels, channels, kernel_h, kernel_w) * 0.1
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_fft = torch.fft.rfft2(x)
        batch, channels, freq_h, freq_w = x_fft.shape

        kernel_real = self.kernel_real.mean(dim=0)
        kernel_imag = self.kernel_imag.mean(dim=0)

        kernel_real_interp = F.interpolate(
            kernel_real.unsqueeze(0).unsqueeze(0).squeeze(0).unsqueeze(0),
            size=(freq_h, freq_w),
            mode='bilinear',
            align_corners=False
        ).squeeze(0)
        kernel_imag_interp = F.interpolate(
            kernel_imag.unsqueeze(0).unsqueeze(0).squeeze(0).unsqueeze(0),
            size=(freq_h, freq_w),
            mode='bilinear',
            align_corners=False
        ).squeeze(0)

        real_part = x_fft.real * kernel_real_interp - x_fft.imag * kernel_imag_interp
        imag_part = x_fft.real * kernel_imag_interp + x_fft.imag * kernel_real_interp
        output_fft = torch.complex(real_part, imag_part)

        output = torch.fft.irfft2(output_fft, s=(self.grid_size, self.grid_size))
        return output


class MinimalSurfaceSpectralNetwork(nn.Module):
    """Neural network for minimal surface detection and Willmore energy learning.

    This network learns to predict mean curvature fields and identify
    minimal surface configurations through spectral convolution layers.
    """

    def __init__(
        self,
        grid_size: int = 64,
        hidden_dim: int = 32,
        expansion_dim: int = 64,
        num_spectral_layers: int = 2,
        input_channels: int = 2,
        output_channels: int = 2
    ):
        super().__init__()
        self.grid_size = grid_size
        self.input_channels = input_channels
        self.output_channels = output_channels

        self.input_proj = nn.Conv2d(input_channels, hidden_dim, kernel_size=1)
        self.expansion_proj = nn.Conv2d(hidden_dim, expansion_dim, kernel_size=1)

        self.spectral_layers = nn.ModuleList([
            SpectralLayer(expansion_dim, grid_size)
            for _ in range(num_spectral_layers)
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


class IModelLoader(ABC):
    """Abstract interface for model loading implementations."""

    @abstractmethod
    def load(self, checkpoint_path: str, device: str, config: RBCAnalysisConfig) -> nn.Module:
        pass


class CheckpointModelLoader(IModelLoader):
    """Model loader that loads from PyTorch checkpoint files."""

    def __init__(self, filesystem: IFileSystem, logger: ILogger):
        self.filesystem = filesystem
        self.logger = logger

    def _detect_model_params(self, state_dict: Dict) -> Tuple[int, int, int, int]:
        grid_size = 16
        hidden_dim = 32
        expansion_dim = 64
        num_spectral_layers = 2

        for key, tensor in state_dict.items():
            if 'spectral_layers' in key and 'kernel_real' in key:
                parts = key.split('.')
                if len(parts) >= 2:
                    try:
                        layer_idx = int(parts[1])
                        num_spectral_layers = max(num_spectral_layers, layer_idx + 1)
                    except ValueError:
                        pass

                shape = tensor.shape
                if len(shape) == 4:
                    expansion_dim = shape[0]
                    kernel_h = shape[2]
                    kernel_w = shape[3]
                    grid_size = kernel_w
                    self.logger.info(
                        f"Detected from kernel shape {shape}: "
                        f"grid_size={grid_size}, expansion_dim={expansion_dim}"
                    )
                break

        for key, tensor in state_dict.items():
            if 'input_proj' in key and 'weight' in key:
                shape = tensor.shape
                if len(shape) == 4:
                    hidden_dim = shape[0]
                    self.logger.info(f"Detected hidden_dim={hidden_dim} from input_proj")
                break

        return grid_size, hidden_dim, expansion_dim, num_spectral_layers

    def load(
        self, checkpoint_path: str, device: str, config: RBCAnalysisConfig
    ) -> nn.Module:
        self.logger.info(f"Loading model from checkpoint: {checkpoint_path}")

        if not self.filesystem.exists(checkpoint_path):
            raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")

        checkpoint = torch.load(
            checkpoint_path,
            map_location=device,
            weights_only=False
        )

        if isinstance(checkpoint, dict):
            if 'model_state_dict' in checkpoint:
                state_dict = checkpoint['model_state_dict']
            elif 'state_dict' in checkpoint:
                state_dict = checkpoint['state_dict']
            else:
                state_dict = checkpoint
        else:
            state_dict = checkpoint

        grid_size, hidden_dim, expansion_dim, num_spectral_layers = self._detect_model_params(state_dict)

        model = MinimalSurfaceSpectralNetwork(
            grid_size=grid_size,
            hidden_dim=hidden_dim,
            expansion_dim=expansion_dim,
            num_spectral_layers=num_spectral_layers,
            input_channels=config.SURFACE_CHANNELS,
            output_channels=config.SURFACE_CHANNELS
        ).to(device)

        model.load_state_dict(state_dict)

        if isinstance(checkpoint, dict):
            if 'epoch' in checkpoint:
                self.logger.info(f"Loaded checkpoint from epoch {checkpoint['epoch']}")
            if 'score' in checkpoint:
                self.logger.info(f"Checkpoint score: {checkpoint['score']:.6f}")
            if 'alpha' in checkpoint:
                self.logger.info(f"Checkpoint alpha: {checkpoint['alpha']:.6f}")
            if 'delta' in checkpoint:
                self.logger.info(f"Checkpoint delta: {checkpoint['delta']:.6f}")

        model.eval()
        for param in model.parameters():
            param.requires_grad = False

        self.logger.info("Model loaded successfully and set to evaluation mode")
        return model


class SurfaceAnalysisEngine:
    """Main engine for RBC surface analysis using Willmore energy model.

    This class orchestrates the complete analysis pipeline, from mesh loading
    to curvature computation and shape emergence testing.
    """

    def __init__(
        self,
        config: RBCAnalysisConfig,
        logger: ILogger,
        filesystem: IFileSystem
    ):
        self.config = config
        self.logger = logger
        self.filesystem = filesystem

        self.mesh_loader = OpenRBCMeshLoader(filesystem, logger)
        self.synthetic_generator = SyntheticMeshGenerator(logger)
        self.curvature_calculator = DiscreteCurvatureCalculator(logger)
        self.model_loader = CheckpointModelLoader(filesystem, logger)

        self.model = None
        self.rbc_mesh = None
        self.synthetic_meshes = {}

    def initialize(self) -> None:
        self.logger.info("Initializing RBC Willmore Analysis Engine")

        self.filesystem.makedirs(self.config.OUTPUT_DIR)

        try:
            self.model = self.model_loader.load(
                self.config.CHECKPOINT_PATH,
                self.config.DEVICE,
                self.config
            )
        except FileNotFoundError as e:
            self.logger.warning(f"Could not load model: {e}")
            self.logger.info("Proceeding with analytical curvature computation only")

        self._load_rbc_mesh()
        self._generate_synthetic_meshes()

        self.logger.info("Initialization complete")

    def _load_rbc_mesh(self) -> None:
        try:
            self.rbc_mesh = self.mesh_loader.load(
                self.config.RBC_VERT_PATH,
                self.config.RBC_FACE_PATH,
                self.config.RBC_BOND_PATH
            )
            self.logger.info(f"RBC mesh loaded: {self.rbc_mesh.to_dict()}")
        except FileNotFoundError as e:
            self.logger.warning(f"Could not load RBC mesh: {e}")
            self.logger.info("Will generate synthetic RBC-like mesh for analysis")

    def _generate_synthetic_meshes(self) -> None:
        self.synthetic_meshes = {
            "sphere": self.synthetic_generator.generate_sphere(
                self.config.SYNTHETIC_SPHERE_RADIUS,
                self.config.SYNTHETIC_SPHERE_RESOLUTION
            ),
            "torus": self.synthetic_generator.generate_torus(
                self.config.SYNTHETIC_TORUS_R,
                self.config.SYNTHETIC_TORUS_r,
                self.config.SYNTHETIC_SPHERE_RESOLUTION
            ),
            "biconcave": self.synthetic_generator.generate_biconcave_disc(
                3.5, 1.0, self.config.SYNTHETIC_SPHERE_RESOLUTION
            )
        }

    def analyze_mesh(self, mesh: MeshData, name: str) -> Dict[str, Any]:
        self.logger.info(f"Analyzing mesh: {name}")

        mean_curvature = self.curvature_calculator.compute_mean_curvature(mesh)
        gaussian_curvature = self.curvature_calculator.compute_gaussian_curvature(mesh)
        willmore_energy = self.curvature_calculator.compute_willmore_energy(
            mesh, mean_curvature
        )

        total_area = self._compute_surface_area(mesh)
        volume = self._compute_volume(mesh)
        asphericity = self._compute_asphericity(mesh)
        biconcavity_index = self._compute_biconcavity_index(mesh, mean_curvature)

        results = {
            "name": name,
            "num_vertices": mesh.num_vertices,
            "num_faces": mesh.num_faces,
            "willmore_energy": float(willmore_energy),
            "mean_curvature_mean": float(np.mean(mean_curvature)),
            "mean_curvature_std": float(np.std(mean_curvature)),
            "mean_curvature_min": float(np.min(mean_curvature)),
            "mean_curvature_max": float(np.max(mean_curvature)),
            "gaussian_curvature_mean": float(np.mean(gaussian_curvature)),
            "gaussian_curvature_std": float(np.std(gaussian_curvature)),
            "gaussian_curvature_integral": float(
                np.sum(gaussian_curvature * mesh.vertex_areas)
            ),
            "surface_area": float(total_area),
            "volume": float(volume),
            "asphericity": float(asphericity),
            "biconcavity_index": float(biconcavity_index),
            "curvature_histogram_mean": self._compute_histogram(
                mean_curvature, bins=20
            ).tolist(),
            "curvature_histogram_gaussian": self._compute_histogram(
                gaussian_curvature, bins=20
            ).tolist()
        }

        self.logger.info(
            f"Analysis complete for {name}: "
            f"Willmore energy = {willmore_energy:.6f}, "
            f"Mean H = {np.mean(mean_curvature):.6f}, "
            f"Area = {total_area:.6f}"
        )

        return results

    def _compute_surface_area(self, mesh: MeshData) -> float:
        if mesh.areas is not None:
            return float(np.sum(mesh.areas))
        return 0.0

    def _compute_volume(self, mesh: MeshData) -> float:
        vertices = mesh.vertices
        faces = mesh.faces

        volume = 0.0
        for face in faces:
            v0, v1, v2 = vertices[face[0]], vertices[face[1]], vertices[face[2]]
            volume += np.dot(v0, np.cross(v1, v2)) / 6.0

        return abs(float(volume))

    def _compute_asphericity(self, mesh: MeshData) -> float:
        vertices = mesh.vertices
        center = np.mean(vertices, axis=0)
        centered = vertices - center

        cov_matrix = np.cov(centered.T)
        eigenvalues = np.linalg.eigvalsh(cov_matrix)
        eigenvalues = np.sort(eigenvalues)[::-1]

        if eigenvalues[0] < 1e-10:
            return 0.0

        asphericity = (
            (eigenvalues[0] - eigenvalues[1]) ** 2 +
            (eigenvalues[1] - eigenvalues[2]) ** 2 +
            (eigenvalues[2] - eigenvalues[0]) ** 2
        ) / (2.0 * np.sum(eigenvalues) ** 2)

        return float(asphericity)

    def _compute_biconcavity_index(
        self, mesh: MeshData, mean_curvature: np.ndarray
    ) -> float:
        vertices = mesh.vertices
        z_coords = vertices[:, 2]
        z_center = np.mean(z_coords)

        center_mask = np.abs(z_coords - z_center) < 0.3 * np.std(z_coords)
        edge_mask = ~center_mask

        if np.sum(center_mask) < 10 or np.sum(edge_mask) < 10:
            return 0.0

        center_curvature = np.mean(np.abs(mean_curvature[center_mask]))
        edge_curvature = np.mean(np.abs(mean_curvature[edge_mask]))

        if edge_curvature < 1e-10:
            return 0.0

        biconcavity = (center_curvature - edge_curvature) / (
            center_curvature + edge_curvature + 1e-10
        )

        return float(biconcavity)

    def _compute_histogram(
        self, data: np.ndarray, bins: int = 20
    ) -> np.ndarray:
        hist, _ = np.histogram(data, bins=bins, density=True)
        return hist

    def run_shape_emergence_test(self) -> Dict[str, Any]:
        self.logger.info("Running shape emergence test")

        results = {
            "timestamp": datetime.now().isoformat(),
            "config": {
                "checkpoint_path": self.config.CHECKPOINT_PATH,
                "device": self.config.DEVICE,
                "grid_size": self.config.GRID_SIZE
            },
            "analyses": {}
        }

        if self.rbc_mesh is not None:
            results["analyses"]["rbc_real"] = self.analyze_mesh(
                self.rbc_mesh, "rbc_real"
            )

        for name, mesh in self.synthetic_meshes.items():
            results["analyses"][f"synthetic_{name}"] = self.analyze_mesh(
                mesh, f"synthetic_{name}"
            )

        if "synthetic_biconcave" in results["analyses"] and "rbc_real" in results["analyses"]:
            rbc_willmore = results["analyses"]["rbc_real"]["willmore_energy"]
            biconcave_willmore = results["analyses"]["synthetic_biconcave"]["willmore_energy"]
            sphere_willmore = results["analyses"]["synthetic_sphere"]["willmore_energy"]

            results["emergence_analysis"] = {
                "rbc_willmore_energy": rbc_willmore,
                "biconcave_willmore_energy": biconcave_willmore,
                "sphere_willmore_energy": sphere_willmore,
                "rbc_vs_biconcave_similarity": 1.0 - abs(rbc_willmore - biconcave_willmore) / max(rbc_willmore, biconcave_willmore),
                "shape_emerged": abs(rbc_willmore - biconcave_willmore) < abs(rbc_willmore - sphere_willmore)
            }

        if self.rbc_mesh is not None:
            results["rbc_morphology"] = self._analyze_rbc_morphology()

        results["gauss_bonnet_verification"] = self._verify_gauss_bonnet()

        return results

    def _analyze_rbc_morphology(self) -> Dict[str, Any]:
        mesh = self.rbc_mesh
        vertices = mesh.vertices

        center = np.mean(vertices, axis=0)
        centered = vertices - center

        radii = np.linalg.norm(centered, axis=1)
        mean_radius = np.mean(radii)
        std_radius = np.std(radii)

        z_coords = centered[:, 2]
        x_coords = centered[:, 0]
        y_coords = centered[:, 1]

        z_extent = np.max(z_coords) - np.min(z_coords)
        xy_extent = np.sqrt(np.max(x_coords) ** 2 + np.max(y_coords) ** 2)

        aspect_ratio = xy_extent / (z_extent + 1e-10)

        surface_area = self._compute_surface_area(mesh)
        volume = self._compute_volume(mesh)

        sphere_radius = (3.0 * volume / (4.0 * np.pi)) ** (1.0 / 3.0)
        sphere_surface_area = 4.0 * np.pi * sphere_radius ** 2

        sphericity = (sphere_surface_area / surface_area) ** 3 if surface_area > 0 else 0.0

        return {
            "mean_radius": float(mean_radius),
            "radius_std": float(std_radius),
            "radius_cv": float(std_radius / (mean_radius + 1e-10)),
            "z_extent": float(z_extent),
            "xy_extent": float(xy_extent),
            "aspect_ratio": float(aspect_ratio),
            "surface_area": float(surface_area),
            "volume": float(volume),
            "sphericity": float(sphericity),
            "typical_rbc_aspect_ratio": 3.5,
            "aspect_ratio_match": abs(aspect_ratio - 3.5) < 1.0
        }

    def _verify_gauss_bonnet(self) -> Dict[str, Any]:
        results = {}

        for name, mesh in self.synthetic_meshes.items():
            gaussian_curvature = self.curvature_calculator.compute_gaussian_curvature(mesh)
            total_gaussian = np.sum(gaussian_curvature * mesh.vertex_areas)

            if name == "sphere":
                expected = 4.0 * np.pi
                topology = "genus 0"
            elif name == "torus":
                expected = 0.0
                topology = "genus 1"
            elif name == "biconcave":
                expected = 4.0 * np.pi
                topology = "genus 0"
            else:
                expected = None
                topology = "unknown"

            results[name] = {
                "computed_integral": float(total_gaussian),
                "expected_integral": float(expected) if expected is not None else None,
                "error": float(abs(total_gaussian - expected)) if expected is not None else None,
                "topology": topology,
                "verified": abs(total_gaussian - expected) < 0.5 if expected is not None else None
            }

        if self.rbc_mesh is not None:
            gaussian_curvature = self.curvature_calculator.compute_gaussian_curvature(self.rbc_mesh)
            total_gaussian = np.sum(gaussian_curvature * self.rbc_mesh.vertex_areas)
            results["rbc_real"] = {
                "computed_integral": float(total_gaussian),
                "expected_integral": 4.0 * np.pi,
                "error": float(abs(total_gaussian - 4.0 * np.pi)),
                "topology": "genus 0 (expected for healthy RBC)",
                "verified": abs(total_gaussian - 4.0 * np.pi) < 1.0
            }

        return results

    def run_mean_curvature_flow(
        self, mesh: MeshData, steps: int, dt: float
    ) -> Tuple[MeshData, List[float]]:
        self.logger.info(f"Running mean curvature flow for {steps} steps")

        vertices = mesh.vertices.copy()
        faces = mesh.faces.copy()
        bonds = mesh.bonds.copy()

        willmore_history = []

        for step in range(steps):
            mean_curvature = self.curvature_calculator.compute_mean_curvature(mesh)

            normals = mesh.normals if mesh.normals is not None else np.zeros_like(vertices)
            for i in range(len(vertices)):
                if np.linalg.norm(normals[i]) > 1e-10:
                    vertices[i] -= dt * mean_curvature[i] * normals[i]

            mesh.vertices = vertices
            self.mesh_loader._compute_normals(mesh)
            self.mesh_loader._compute_areas(mesh)

            willmore = self.curvature_calculator.compute_willmore_energy(mesh, mean_curvature)
            willmore_history.append(willmore)

            if step % 100 == 0:
                self.logger.info(f"Step {step}: Willmore energy = {willmore:.6f}")

        result_mesh = MeshData(
            vertices=vertices,
            faces=faces,
            bonds=bonds
        )
        self.mesh_loader._compute_normals(result_mesh)
        self.mesh_loader._compute_areas(result_mesh)

        return result_mesh, willmore_history

    def save_results(self, results: Dict[str, Any], filename: str) -> None:
        output_path = os.path.join(self.config.OUTPUT_DIR, filename)
        
        def convert_to_native(obj):
            if isinstance(obj, dict):
                return {k: convert_to_native(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_to_native(v) for v in obj]
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, (np.integer, np.int64, np.int32)):
                return int(obj)
            elif isinstance(obj, (np.floating, np.float64, np.float32)):
                return float(obj)
            elif isinstance(obj, (np.bool_, bool)):
                return bool(obj)
            else:
                return obj
        
        results_native = convert_to_native(results)
        self.filesystem.write_text(output_path, json.dumps(results_native, indent=2))
        self.logger.info(f"Results saved to {output_path}")

    def save_mesh_obj(self, mesh: MeshData, filename: str) -> None:
        output_path = os.path.join(self.config.OUTPUT_DIR, filename)

        lines = []
        for v in mesh.vertices:
            lines.append(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}")

        for f in mesh.faces:
            lines.append(f"f {f[0] + 1} {f[1] + 1} {f[2] + 1}")

        self.filesystem.write_text(output_path, "\n".join(lines))
        self.logger.info(f"Mesh saved to {output_path}")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Red Blood Cell Willmore Energy Analysis",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--checkpoint",
        type=str,
        default=RBCAnalysisConfig.CHECKPOINT_PATH,
        help="Path to model checkpoint file"
    )
    parser.add_argument(
        "--vert-file",
        type=str,
        default=RBCAnalysisConfig.RBC_VERT_PATH,
        help="Path to RBC vertex file"
    )
    parser.add_argument(
        "--face-file",
        type=str,
        default=RBCAnalysisConfig.RBC_FACE_PATH,
        help="Path to RBC face file"
    )
    parser.add_argument(
        "--bond-file",
        type=str,
        default=RBCAnalysisConfig.RBC_BOND_PATH,
        help="Path to RBC bond file"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=RBCAnalysisConfig.OUTPUT_DIR,
        help="Output directory for results"
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda" if torch.cuda.is_available() else "cpu",
        choices=["cuda", "cpu"],
        help="Device for computation"
    )
    parser.add_argument(
        "--grid-size",
        type=int,
        default=RBCAnalysisConfig.GRID_SIZE,
        help="Grid size for spectral network"
    )
    parser.add_argument(
        "--hidden-dim",
        type=int,
        default=RBCAnalysisConfig.HIDDEN_DIM,
        help="Hidden dimension for network"
    )
    parser.add_argument(
        "--expansion-dim",
        type=int,
        default=RBCAnalysisConfig.EXPANSION_DIM,
        help="Expansion dimension for network"
    )
    parser.add_argument(
        "--num-spectral-layers",
        type=int,
        default=RBCAnalysisConfig.NUM_SPECTRAL_LAYERS,
        help="Number of spectral layers"
    )
    parser.add_argument(
        "--relaxation-steps",
        type=int,
        default=RBCAnalysisConfig.RELAXATION_STEPS,
        help="Number of relaxation steps for curvature flow"
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level"
    )
    parser.add_argument(
        "--skip-synthetic",
        action="store_true",
        help="Skip generation of synthetic comparison meshes"
    )
    parser.add_argument(
        "--run-flow",
        action="store_true",
        help="Run mean curvature flow evolution"
    )

    return parser.parse_args()


def create_config_from_args(args: argparse.Namespace) -> RBCAnalysisConfig:
    return RBCAnalysisConfig(
        CHECKPOINT_PATH=args.checkpoint,
        RBC_VERT_PATH=args.vert_file,
        RBC_FACE_PATH=args.face_file,
        RBC_BOND_PATH=args.bond_file,
        OUTPUT_DIR=args.output_dir,
        DEVICE=args.device,
        GRID_SIZE=args.grid_size,
        HIDDEN_DIM=args.hidden_dim,
        EXPANSION_DIM=args.expansion_dim,
        NUM_SPECTRAL_LAYERS=args.num_spectral_layers,
        RELAXATION_STEPS=args.relaxation_steps,
        LOG_LEVEL=args.log_level,
        COMPUTE_SYNTHETIC=not args.skip_synthetic
    )


def main() -> int:
    args = parse_arguments()
    config = create_config_from_args(args)

    logger = StandardLogger("RBCWillmoreAnalysis", config.LOG_LEVEL)
    filesystem = StandardFileSystem()

    logger.info("=" * 60)
    logger.info("RBC Willmore Energy Analysis")
    logger.info("=" * 60)
    logger.info(f"Checkpoint: {config.CHECKPOINT_PATH}")
    logger.info(f"Device: {config.DEVICE}")
    logger.info(f"Output directory: {config.OUTPUT_DIR}")

    engine = SurfaceAnalysisEngine(config, logger, filesystem)

    try:
        engine.initialize()
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        return 1

    results = engine.run_shape_emergence_test()

    if args.run_flow and engine.rbc_mesh is not None:
        logger.info("Running mean curvature flow evolution")
        evolved_mesh, willmore_history = engine.run_mean_curvature_flow(
            engine.rbc_mesh,
            config.RELAXATION_STEPS,
            config.MEAN_CURVATURE_FLOW_DT
        )
        results["curvature_flow"] = {
            "initial_willmore": willmore_history[0] if willmore_history else 0,
            "final_willmore": willmore_history[-1] if willmore_history else 0,
            "willmore_reduction": willmore_history[0] - willmore_history[-1] if willmore_history else 0,
            "history_length": len(willmore_history)
        }
        engine.save_mesh_obj(evolved_mesh, "rbc_evolved.obj")

    engine.save_results(results, "rbc_analysis_results.json")

    if engine.rbc_mesh is not None:
        engine.save_mesh_obj(engine.rbc_mesh, "rbc_original.obj")

    for name, mesh in engine.synthetic_meshes.items():
        engine.save_mesh_obj(mesh, f"synthetic_{name}.obj")

    logger.info("=" * 60)
    logger.info("Analysis Complete")
    logger.info("=" * 60)

    if "emergence_analysis" in results:
        ea = results["emergence_analysis"]
        logger.info(f"RBC Willmore Energy: {ea['rbc_willmore_energy']:.6f}")
        logger.info(f"Biconcave Willmore Energy: {ea['biconcave_willmore_energy']:.6f}")
        logger.info(f"Sphere Willmore Energy: {ea['sphere_willmore_energy']:.6f}")
        logger.info(f"Shape Emerged: {ea['shape_emerged']}")

    if "gauss_bonnet_verification" in results:
        logger.info("Gauss-Bonnet Verification:")
        for name, gb in results["gauss_bonnet_verification"].items():
            verified = gb.get("verified", "N/A")
            logger.info(f"  {name}: computed={gb['computed_integral']:.4f}, "
                       f"expected={gb['expected_integral']:.4f}, verified={verified}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
