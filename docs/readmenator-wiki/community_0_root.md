# root

*Community 0 | 9 files | cohesion 1.00*

## Definition

This community groups 9 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `AdaptiveLambdaScheduler`, `AnnealingScheduler`, `BatchSizeProspector`, `BilinearSpectralInterpolator`, `CheckpointLoader`, `CheckpointManager`, `Config`, `CrystallographyMetricsCalculator`. Core file: `willmore_crsital2.py` (174 symbols). Documented purpose: EVALUACIÓN PUNTO A PUNTO: Modelo evaluado en cada uno de los 9128 vértices sin pasar por grilla 16x16. Preserva la densidad irregular del malla original..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `model_Reco.py` | py | business_logic | 10 | yes |
| `rbc.py` | py | utility | 11 | yes |
| `rbc_model_reconstruction (1).py` | py | business_logic | 11 | yes |
| `rbc_model_reconstruction.py` | py | business_logic | 10 | yes |
| `rbc_model_reconstruction_128.py` | py | business_logic | 46 | yes |
| `test.py` | py | testing | 3 | yes |
| `willmore_crsital2.py` | py | utility | 174 | yes |
| `willmore_zero_shot_scaler.py` | py | utility | 63 | yes |
| `wilmore_rbc.py` | py | utility | 49 | yes |

## Key Symbols

- `load_rbc_mesh` (function, `model_Reco.py:27`) `def load_rbc_mesh(vert_path, face_path)`
- `center_mesh` (function, `model_Reco.py:49`) `def center_mesh(vertices)`
- `cartesian_to_spherical` (function, `model_Reco.py:54`) `def cartesian_to_spherical(vertices)`
- `spherical_to_cartesian` (function, `model_Reco.py:63`) `def spherical_to_cartesian(r, theta, phi)`
- `evaluate_model_at_points` (function, `model_Reco.py:70`) `def evaluate_model_at_points(model, r_values, theta_values, phi_values, grid_siz` - Evalúa el modelo en puntos arbitrarios (no en grilla regular).
- `load_model` (function, `model_Reco.py:134`) `def load_model(checkpoint_path, device, config)`
- `compute_curvatures` (function, `model_Reco.py:159`) `def compute_curvatures(vertices, faces, grid_size)` - Compute curvatures using the same operator as training.
- `save_obj` (function, `model_Reco.py:189`) `def save_obj(vertices, faces, filepath)`
- `save_html_viewer` (function, `model_Reco.py:197`) `def save_html_viewer(orig_verts, orig_faces, pred_verts, pred_faces, output_path`
- `main` (function, `model_Reco.py:338`) `def main()`
- `load_rbc_mesh` (function, `rbc.py:30`) `def load_rbc_mesh(vert_path, face_path)` - Load RBC mesh from OpenRBC files.
- `load_model` (function, `rbc.py:53`) `def load_model(checkpoint_path, device, config)` - Load the trained Willmore model from checkpoint.
- `project_rbc_to_spherical_grid` (function, `rbc.py:94`) `def project_rbc_to_spherical_grid(vertices, grid_size)` - Project entire RBC mesh onto a spherical coordinate grid.
- `spherical_grid_to_cartesian` (function, `rbc.py:139`) `def spherical_grid_to_cartesian(r_grid, grid_size, scale)` - Convert spherical grid back to 3D vertices.
- `run_model_evolution` (function, `rbc.py:164`) `def run_model_evolution(model, input_grid, steps, device)` - Run model iteratively to evolve the surface.
- `create_sphere_grid` (function, `rbc.py:202`) `def create_sphere_grid(grid_size, radius)` - Create a perfect sphere grid for comparison.
- `create_biconcave_grid` (function, `rbc.py:212`) `def create_biconcave_grid(grid_size, radius)` - Create a biconcave disc shape on spherical grid.
- `compute_willmore_on_grid` (function, `rbc.py:224`) `def compute_willmore_on_grid(surface, grid_size)` - Compute Willmore energy using MinimalSurfaceOperator.
- `save_obj` (function, `rbc.py:231`) `def save_obj(vertices, faces, filepath)` - Save mesh as OBJ file.
- `save_html_comparison` (function, `rbc.py:240`) `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, r` - Create interactive HTML comparing all shapes.
- `main` (function, `rbc.py:393`) `def main()`
- `load_rbc_mesh` (function, `rbc_model_reconstruction (1).py:30`) `def load_rbc_mesh(vert_path, face_path)` - Load RBC mesh from OpenRBC files.
- `load_model` (function, `rbc_model_reconstruction (1).py:53`) `def load_model(checkpoint_path, device, config)` - Load the trained Willmore model from checkpoint.
- `project_rbc_to_spherical_grid` (function, `rbc_model_reconstruction (1).py:94`) `def project_rbc_to_spherical_grid(vertices, grid_size)` - Project entire RBC mesh onto a spherical coordinate grid.
- `spherical_grid_to_cartesian` (function, `rbc_model_reconstruction (1).py:139`) `def spherical_grid_to_cartesian(r_grid, grid_size, scale)` - Convert spherical grid back to 3D vertices.
- `run_model_evolution` (function, `rbc_model_reconstruction (1).py:164`) `def run_model_evolution(model, input_grid, steps, device)` - Run model iteratively to evolve the surface.
- `create_sphere_grid` (function, `rbc_model_reconstruction (1).py:202`) `def create_sphere_grid(grid_size, radius)` - Create a perfect sphere grid for comparison.
- `create_biconcave_grid` (function, `rbc_model_reconstruction (1).py:212`) `def create_biconcave_grid(grid_size, radius)` - Create a biconcave disc shape on spherical grid.
- `compute_willmore_on_grid` (function, `rbc_model_reconstruction (1).py:224`) `def compute_willmore_on_grid(surface, grid_size)` - Compute Willmore energy using MinimalSurfaceOperator.
- `save_obj` (function, `rbc_model_reconstruction (1).py:231`) `def save_obj(vertices, faces, filepath)` - Save mesh as OBJ file.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 8
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (root) and community 1 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `model_Reco.py`
- `rbc.py`
- `rbc_model_reconstruction (1).py`
- `rbc_model_reconstruction.py`
- `rbc_model_reconstruction_128.py`
- `test.py`
- `willmore_crsital2.py`
- `willmore_zero_shot_scaler.py`
- `wilmore_rbc.py`
