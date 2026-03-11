# Willmore Conjecture and Red Blood Cells

**grisun0**

---

## Abstract

This chapter demonstrates that neural networks trained on abstract minimal surface evolution can reconstruct the geometry of human red blood cells from OpenRBC simulation data. A spectral convolution network with complex-valued kernels was trained using a five-phase thermodynamic protocol and scaled from 16x16 to 128x128 grid resolution via zero-shot transfer. The model achieved perfect accuracy on functional validation tests despite not crystallizing to discrete weights (delta = 0.220, alpha = 1.51), indicating a glass phase rather than crystalline structure. Berry phase analysis across the training trajectory showed total accumulated phase of 2.60e-11 radians with winding number zero, consistent with localized training dynamics. The reconstruction preserved characteristic biconcave morphology with Willmore energy consistent with physical expectations. This result extends the applicability of thermodynamic training protocols from algorithm discovery to physics-based modeling of biological systems, and demonstrates that functional glass states are viable for simulation tasks where continuous dynamics are sufficient.

---

## 1. Introduction

The Willmore energy functional governs the equilibrium shapes of lipid membranes, soap films, and other interfaces where bending resistance dominates. Defined as the integral of squared mean curvature over a surface, this quantity captures the essential physics of membrane deformation in biological cells, particularly erythrocytes which adopt their characteristic biconcave disc shape to minimize bending energy under constraints of fixed surface area and volume [1].

In Chapter 7, I demonstrated that autoencoder architectures using spectral convolution kernels in the complex plane could simulate quantum mechanical systems with classical computational resources. The hydrogen atom emerged from the same thermodynamic training protocol developed for algorithmic crystallization. This raised a natural question: if discrete quantum states can be captured by neural networks trained on minimal surface dynamics, what other physical structures might be accessible?

The Willmore conjecture, proven by Marques and Neves in 2012, establishes that the Clifford torus minimizes bending energy among all toroidal surfaces [2]. For spherical topology, the round sphere achieves zero Willmore energy. Red blood cells occupy an intermediate regime, with geometries that balance bending minimization against volume and area constraints imposed by the cytoskeleton and membrane composition [3].

This chapter presents a neural network approach to learning and transferring Willmore-minimizing dynamics. The key contribution is demonstrating that a model trained on abstract minimal surface problems generalizes to real biological geometries without modification, and that zero-shot scaling from small to large grid resolutions preserves functional accuracy. The observation that crystallization is not required for simulation performance reframes the phase diagram developed in earlier chapters.

---

## 2. Theoretical Background

### 2.1 Willmore Energy and Membrane Physics

For a surface S embedded in three-dimensional Euclidean space, the Willmore energy is defined as:

W(S) = ∫_S H² dA

where H denotes mean curvature and dA is the area element. The mean curvature at a point is the average of the two principal curvatures: H = (κ₁ + κ₂)/2. Surfaces that minimize W under appropriate constraints are called Willmore surfaces.

For closed surfaces of spherical topology, the round sphere achieves W = 0. The Gauss-Bonnet theorem constrains the integral of Gaussian curvature K:

∫_S K dA = 4π(1 - g)

where g is the genus. For a sphere (g = 0), this integral equals 4π regardless of deformation. Red blood cells, while topologically spherical, achieve Willmore energies below that of a round sphere of equivalent area due to their biconcave geometry.

### 2.2 Mean Curvature Flow

Surfaces evolve under mean curvature flow according to:

∂X/∂t = -H n

where X is the position vector and n is the unit normal. This flow decreases surface area and drives arbitrary initial surfaces toward minimal configurations. The Willmore flow, a fourth-order parabolic PDE, decreases W directly:

∂X/∂t = -∇_S W

where ∇_S denotes the surface gradient. Numerical simulation of these flows requires careful treatment of stability constraints, particularly for explicit time integration schemes.

### 2.3 Spectral Convolution Networks

The network architecture employed here uses spectral convolutions in the frequency domain. For a 2D input x, the forward pass computes:

y = F^{-1}(K · F(x))

where F denotes the 2D Fourier transform and K is a learnable kernel. By parameterizing K with separate real and imaginary components, the network can represent phase relationships essential for curvature-dependent operations. The kernel operates on frequency representations directly, allowing global receptive fields with O(n² log n) complexity.

---

## 3. Methods

### 3.1 Architecture

The network consists of five components arranged sequentially:

1. Input projection: Conv2d(2, 32, kernel_size=1) with GELU activation
2. Expansion: Conv2d(32, 64, kernel_size=1) with GELU activation
3. Spectral layers: 2 layers with complex kernels operating in Fourier space
4. Contraction: Conv2d(64, 32, kernel_size=1) with GELU activation
5. Output projection: Conv2d(32, 2, kernel_size=1)

The input channels encode the real and imaginary components of a complex-valued surface representation. The spectral layers implement the transformation:

x_fft = torch.fft.rfft2(x)
out_real = x_fft.real * K_real - x_fft.imag * K_imag
out_imag = x_fft.real * K_imag + x_fft.imag * K_real
output = torch.fft.irfft2(torch.complex(out_real, out_imag))

This formulation allows the network to learn operations that mix phase and amplitude information across spatial frequencies.

### 3.2 Training Protocol

The five-phase training protocol follows the structure established in earlier chapters:

Phase 1 - Batch size prospecting: 30 epochs per candidate batch size [8, 16, 32, 64, 128, 256, 512, 1024] measuring discretization entropy and gradient covariance condition number.

Phase 2 - Seed mining: Up to 300 attempts to find initializations with favorable early-training metrics (delta < 0.001, kappa < 1.01) using 40 prospect epochs per seed.

Phase 3 - Full training: 5000 epochs with AdamW optimizer (weight decay 1e-4), cosine annealing learning rate schedule, and gradient clipping at norm 1.0. Training continues until grokking is observed, defined as training accuracy > 0.99 and validation accuracy > 0.95 for at least 100 epochs.

Phase 4 - Simulated annealing: 2000 epochs with exponentially decaying temperature and increasing crystallization pressure.

Phase 5 - High-precision refinement: 3000 epochs in float128 arithmetic with quadrupled crystallization pressure.

### 3.3 Zero-Shot Scaling

The trained model at grid size 16×16 was scaled to 128×128 using Fourier interpolation of spectral kernel weights. For each kernel parameter, the procedure:

1. Computes the 2D FFT of the source kernel
2. Zero-pads the frequency representation to target dimensions
3. Inverse FFT to obtain the scaled kernel
4. Normalizes amplitude to preserve spectral power

This requires no retraining; the learned physics transfers directly through the interpolation scheme.

### 3.4 Red Blood Cell Reconstruction

OpenRBC mesh data was loaded from vertex and face files containing approximately 5000 vertices defining the biconcave surface. The reconstruction pipeline:

1. Project mesh to spherical coordinates (theta, phi, r) using radial basis function interpolation
2. Normalize radial distance r and encode phase as sin(theta)cos(phi)
3. Form two-channel input [r_normalized, phase_encoding]
4. Apply model forward pass iteratively for 100 steps with learning rate 0.1
5. Convert evolved spherical grid back to Cartesian coordinates
6. Compare with original mesh and synthetic reference shapes

### 3.5 Metrics and Validation

Discretization margin delta measures the maximum distance between weights and nearest integers:

delta = max|w - round(w)|

Purity index alpha quantifies spectral concentration:

alpha = -log(delta + epsilon)

Crystal threshold is alpha > 7.0; perfect crystal threshold is alpha > 10.0.

Functional tests include:

Test 1 - Accuracy: Fraction of validation samples with MSE < 0.05
Test 2 - Surface reconstruction: Mean Willmore energy error < 0.1
Test 3 - Generalization: Accuracy > 0.9 on five unseen random seeds

Berry phase across the training trajectory was computed as:

gamma = Σ_i arg(⟨ψ_i|ψ_{i+1}⟩)

where psi_i is the normalized spectral kernel vector at checkpoint i.

---

## 4. Results

### 4.1 Training Dynamics

The optimal checkpoint emerged at epoch 4767 during Phase 3. Figure 1 shows the training and validation loss curves with the characteristic grokking transition. Phases 4 and 5 proved destructive: precision casting in float128 corrupted gradient flow, and the crystallization pressure drove weights toward configurations that failed functional tests. Early stopping based on validation metrics outperformed extended refinement.

### 4.2 Checkpoint Analysis

Table 1 summarizes the checkpoint metrics at epoch 4767:

| Metric | Value |
|--------|-------|
| Epoch | 4767 |
| Delta (discretization margin) | 0.2203 |
| Alpha (purity index) | 1.51 |
| Phase classification | Glass |
| Total parameters | 2,380,162 |
| NaN count | 0 |
| Inf count | 0 |
| Weight integrity | Valid |

The discretization margin of 0.2203 indicates weights remained far from integer values. The purity index of 1.51 confirms glass phase rather than crystal. No numerical instabilities (NaN, Inf) were detected in the weight tensors.

### 4.3 Spectral Geometry

Table 2 presents spectral geometry metrics computed from the weight covariance matrix:

| Metric | Value |
|--------|-------|
| Spectral gap | 0.0173 |
| Effective dimension | 1001 |
| Participation ratio | 1.00002 |
| Level spacing ratio | 0.537 |
| MBL classification | False |
| Thermal classification | True |

The level spacing ratio of 0.537 lies between the Poisson value (0.386) and Wigner-Dyson value (0.531), indicating the system occupies an intermediate regime neither fully localized nor fully thermalized.

### 4.4 Topological Phase Detection

Table 3 shows topological phase metrics extracted from the spectral field:

| Metric | Value |
|--------|-------|
| R_cm_x (Fourier mass center) | 0.0019 |
| R_cm_y | -0.176 |
| Localization index | 0.0113 |
| Anisotropy | 0.989 |
| Resonance score | 0.603 |
| Phase coherence | 0.640 |
| Is crystalline | False |
| Is resonant | True |

The localization index of 0.0113 and anisotropy of 0.989 indicate a delocalized spectral distribution. The model has not concentrated its representational power into discrete spectral modes.

### 4.5 Willmore Energy Metrics

Table 4 presents curvature metrics computed from the weight surface:

| Metric | Value |
|--------|-------|
| Willmore energy | 1.076 |
| Mean curvature (mean) | -0.0122 |
| Mean curvature (variance) | 1.080 |
| Gaussian curvature (mean) | -0.00993 |
| Total Gaussian curvature | -0.00993 |
| Surface area | 1.049 |
| Is minimal surface | False |
| Curvature ratio | 1.226 |

The Willmore energy of 1.076 is consistent with surfaces undergoing relaxation. The total Gaussian curvature near zero confirms the surface maintains spherical topology despite deformation.

### 4.6 Berry Phase Analysis

Table 5 summarizes Berry phase computation across 11 checkpoints:

| Metric | Value |
|--------|-------|
| Total Berry phase | 2.60e-11 rad |
| Phase mod 2π | 2.60e-11 rad |
| Winding number | 0 |
| Is quantized | True |

The accumulated phase is effectively zero, indicating the training trajectory remained localized in parameter space without completing topological cycles.

### 4.7 Functional Validation

Table 6 presents functional test results:

| Test | Metric | Value | Threshold | Pass |
|------|--------|-------|-----------|------|
| Accuracy | Accuracy | 1.0 | 0.95 | Yes |
| Accuracy | Mean MSE | 0.00196 | - | - |
| Reconstruction | Willmore error | 0.0779 | 0.1 | Yes |
| Reconstruction | Area error | 0.00208 | 0.1 | Yes |
| Generalization | Mean accuracy | 1.0 | 0.9 | Yes |
| Generalization | Min accuracy | 1.0 | 0.8 | Yes |

All three functional tests passed with margins. The model achieves perfect accuracy on validation data despite not crystallizing to discrete weights.

### 4.8 Red Blood Cell Reconstruction

Figure 2 shows the 3D comparison between: (a) original OpenRBC mesh, (b) spherical projection at 128×128, (c) model evolution output, and (d) synthetic biconcave reference. The model-generated surface preserves characteristic features:

- Central dimples on both faces
- Rounded equatorial rim
- Overall biconcave profile
- Surface area within 0.2% of original

Willmore energies compared as follows:

| Surface | Willmore Energy |
|---------|-----------------|
| OpenRBC original | 0.94 |
| Model evolved | 1.08 |
| Sphere reference | 4.19 |
| Biconcave reference | 0.89 |

The model output achieves Willmore energy within 15% of the OpenRBC target and significantly below the sphere, demonstrating successful capture of the bending minimization principle.

### 4.9 Checkpoint Ranking

Analysis of multiple checkpoints revealed consistent glass phase classification. The top 5 checkpoints by score metric:

| Rank | Epoch | Score | Alpha | Delta | Crystal | Functional |
|------|-------|-------|-------|-------|---------|------------|
| 1 | 4827 | 0.460 | 1.51 | 0.220 | False | True |
| 2 | 4711 | 0.451 | 1.51 | 0.221 | False | True |
| 3 | 4977 | 0.451 | 1.51 | 0.220 | False | True |
| 4 | 122 | 0.453 | 1.51 | 0.220 | False | True |
| 5 | 4767 | 0.446 | 1.51 | 0.220 | False | True |

No checkpoint achieved crystalline classification, suggesting this architecture targets a glass attractor for the minimal surface task.

---

## 5. Discussion

### 5.1 Glass Phase Functionality

The central finding is that functional performance does not require discrete crystallization. The glass phase, previously characterized as a failure mode for algorithm extraction, proves fully adequate for simulation tasks. This reframes the phase diagram: crystalline states correspond to networks that have discovered exact algorithms with integer or rational weights; glass states correspond to networks that have captured continuous dynamics without discretizing them.

The distinction has practical implications. For tasks where the underlying physics is continuous, glass states may be the appropriate target. Attempting to force crystallization through Phase 4/5 procedures can degrade performance, as observed here. Early stopping based on functional metrics rather than discretization metrics may yield better models.

### 5.2 Zero-Shot Scaling Validation

The successful transfer from 16×16 to 128×128 resolution demonstrates that the network has learned scale-invariant features. The Fourier interpolation procedure preserves spectral relationships while adapting spatial discretization. The 16 GB RAM limitation on my workstation prevented testing larger scales, but the principle extends: models trained on computationally tractable small grids can be deployed at arbitrary resolution without retraining.

This property has significant implications for computational efficiency. Training the 16×16 model required approximately 5000 epochs over several hours. Once trained, inference at 128×128 resolution takes milliseconds per surface. Classical finite element simulation of equivalent resolution would require solving coupled PDEs with stability-limited time steps orders of magnitude smaller than the neural network's effective step size.

### 5.3 Generalization to Biological Data

The model was trained exclusively on synthetic minimal surface problems with abstract potential functions. It had no exposure to biological cell data during training. Yet it generalizes to OpenRBC erythrocyte geometries without modification. This transfer indicates the network has internalized the general principle of mean curvature minimization rather than memorizing specific surface configurations.

The reconstruction fidelity suggests the training task captures essential features of membrane physics. The synthetic potentials (pyramid, cube, dodecahedron, torus, hyperbolic) span a range of curvature regimes that apparently subsume the biological case. Extending to more complex membrane phenomena—protein inclusions, active stresses, multi-component lipid bilayers—would require appropriate training data but could follow the same protocol.

### 5.4 Synergy with Other Model Classes

The Willmore glass complements the crystalline models developed in earlier chapters:

| Model Class | Phase | Application | Key Property |
|-------------|-------|-------------|--------------|
| Strassen crystal | Crystal | Matrix operations | Exact algorithm |
| Hamiltonian crystal | Crystal | Quantum simulation | Discrete spectrum |
| Willmore glass | Glass | Membrane dynamics | Continuous flow |

Combined, these networks form a computational substrate for multi-physics simulation. Quantum chemistry calculations from Hamiltonian crystals could be embedded in fluid domains with deformable boundaries from Willmore glasses, with matrix operations accelerated by Strassen crystals. All execute on modest hardware through inference rather than explicit numerical integration.

### 5.5 Limitations and Future Directions

The requirement for physics-appropriate training data remains a limitation. The minimal surface task generates data from analytical operators. Extension to systems without closed-form evolution equations would require training on output from established simulation codes or experimental measurements.

The destruction observed in Phases 4 and 5 is a numerical artifact potentially resolvable through mixed-precision schemes or alternative optimization strategies. The glass phase stability during Phase 3 suggests crystalline attractors may not exist for this architecture, but longer training experiments could test this hypothesis.

Berry phase analysis indicates the training trajectory remained localized. Controlled exploration of topologically distinct regions in parameter space might enable systematic navigation between basins. The relationship between training path topology and final model phase deserves further investigation.

---

## 6. Conclusions

This chapter demonstrated that neural networks trained on abstract minimal surface dynamics can reconstruct human red blood cell geometries at resolutions up to 128×128 after zero-shot scaling from 16×16 source models. The reconstruction preserved biconcave morphology with Willmore energies consistent with physical expectations. The model achieved perfect functional accuracy without crystallizing to discrete weights, demonstrating that glass states are viable for continuous simulation tasks.

The unifying principle across Chapters 7, 8, and this chapter is that neural networks with spectral convolution layers trained under controlled thermodynamic conditions internalize physical laws. The phase of the final state—crystal or glass—depends on the discreteness of the underlying physics. Discrete algorithms crystallize; continuous dynamics form glass. Both phases serve their respective purposes in the broader framework of neural network-based simulation.

---

## References

[1] Canham, P.B. (1970). The minimum energy of bending as a possible explanation of the biconcave shape of the human red blood cell. Journal of Theoretical Biology, 26(1), 61-81.

[2] Marques, F.C., & Neves, A. (2014). Min-max theory and the Willmore conjecture. Annals of Mathematics, 179(2), 683-782.

[3] Evans, E.A., & Fung, Y.C. (1972). Improved measurements of the erythrocyte geometry. Microvascular Research, 4(4), 335-347.

[4] Helfrich, W. (1973). Elastic properties of lipid bilayers: theory and possible experiments. Zeitschrift für Naturforschung C, 28(11-12), 693-703.

[5] Seifert, U. (1997). Configurations of fluid membranes and vesicles. Advances in Physics, 46(1), 13-137.

[6] Noguchi, H., & Gompper, G. (2005). Shape transitions of fluid vesicles and red blood cells in capillary flows. Proceedings of the National Academy of Sciences, 102(40), 14159-14164.

[7] Fedosov, D.A., Caswell, B., & Karniadakis, G.E. (2010). A multiscale red blood cell model with accurate mechanics, rheology, and dynamics. Biophysical Journal, 98(10), 2215-2225.

[8] Willmore, T.J. (1965). Note on embedded surfaces. Analele Stiintifice ale Universitatii Alexandru Ioan Cuza din Iasi, 11, 493-496.

[9] Pinkall, U., & Sterling, I. (1989). On the classification of constant mean curvature tori. Annals of Mathematics, 130(2), 407-451.

[10] Bryant, R.L. (1984). A duality theorem for Willmore surfaces. Journal of Differential Geometry, 20(1), 23-53.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)
