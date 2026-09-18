# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `compute_metrics` | function | `lol.py:164` | `def compute_metrics(r_grid, mask, original_r)` |
| `create_synthetic_rbc` | function | `lol.py:16` | `def create_synthetic_rbc(n_vertices)` |
| `cylindrical_projection` | function | `lol.py:76` | `def cylindrical_projection(vertices, grid_size)` |
| `cylindrical_to_cartesian` | function | `lol.py:144` | `def cylindrical_to_cartesian(rho_grid, z_min, z_max, grid_size)` |
| `main` | function | `lol.py:189` | `def main()` |
| `save_obj` | function | `lol.py:181` | `def save_obj(vertices, faces, filepath)` |
| `spherical_projection` | function | `lol.py:44` | `def spherical_projection(vertices, grid_size)` |
| `spherical_to_cartesian` | function | `lol.py:123` | `def spherical_to_cartesian(r_grid, grid_size)` |
| `cartesian_to_spherical` | function | `model_Reco.py:54` | `def cartesian_to_spherical(vertices)` |
| `center_mesh` | function | `model_Reco.py:49` | `def center_mesh(vertices)` |
| `compute_curvatures` | function | `model_Reco.py:159` | `def compute_curvatures(vertices, faces, grid_size)` |
| `evaluate_model_at_points` | function | `model_Reco.py:70` | `def evaluate_model_at_points(model, r_values, theta_values, phi_values, grid_size, device, r_global_mean)` |
| `load_model` | function | `model_Reco.py:134` | `def load_model(checkpoint_path, device, config)` |
| `load_rbc_mesh` | function | `model_Reco.py:27` | `def load_rbc_mesh(vert_path, face_path)` |
| `main` | function | `model_Reco.py:338` | `def main()` |
| `save_html_viewer` | function | `model_Reco.py:197` | `def save_html_viewer(orig_verts, orig_faces, pred_verts, pred_faces, output_path)` |
| `save_obj` | function | `model_Reco.py:189` | `def save_obj(vertices, faces, filepath)` |
| `spherical_to_cartesian` | function | `model_Reco.py:63` | `def spherical_to_cartesian(r, theta, phi)` |
| `compute_willmore_on_grid` | function | `rbc.py:224` | `def compute_willmore_on_grid(surface, grid_size)` |
| `create_biconcave_grid` | function | `rbc.py:212` | `def create_biconcave_grid(grid_size, radius)` |
| `create_sphere_grid` | function | `rbc.py:202` | `def create_sphere_grid(grid_size, radius)` |
| `load_model` | function | `rbc.py:53` | `def load_model(checkpoint_path, device, config)` |
| `load_rbc_mesh` | function | `rbc.py:30` | `def load_rbc_mesh(vert_path, face_path)` |
| `main` | function | `rbc.py:393` | `def main()` |
| `project_rbc_to_spherical_grid` | function | `rbc.py:94` | `def project_rbc_to_spherical_grid(vertices, grid_size)` |
| `run_model_evolution` | function | `rbc.py:164` | `def run_model_evolution(model, input_grid, steps, device)` |
| `save_html_comparison` | function | `rbc.py:240` | `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved` |
| `save_obj` | function | `rbc.py:231` | `def save_obj(vertices, faces, filepath)` |
| `spherical_grid_to_cartesian` | function | `rbc.py:139` | `def spherical_grid_to_cartesian(r_grid, grid_size, scale)` |
| `compute_willmore_on_grid` | function | `rbc_model_reconstruction (1).py:224` | `def compute_willmore_on_grid(surface, grid_size)` |
| `create_biconcave_grid` | function | `rbc_model_reconstruction (1).py:212` | `def create_biconcave_grid(grid_size, radius)` |
| `create_sphere_grid` | function | `rbc_model_reconstruction (1).py:202` | `def create_sphere_grid(grid_size, radius)` |
| `load_model` | function | `rbc_model_reconstruction (1).py:53` | `def load_model(checkpoint_path, device, config)` |
| `load_rbc_mesh` | function | `rbc_model_reconstruction (1).py:30` | `def load_rbc_mesh(vert_path, face_path)` |
| `main` | function | `rbc_model_reconstruction (1).py:393` | `def main()` |
| `project_rbc_to_spherical_grid` | function | `rbc_model_reconstruction (1).py:94` | `def project_rbc_to_spherical_grid(vertices, grid_size)` |
| `run_model_evolution` | function | `rbc_model_reconstruction (1).py:164` | `def run_model_evolution(model, input_grid, steps, device)` |
| `save_html_comparison` | function | `rbc_model_reconstruction (1).py:240` | `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved` |
| `save_obj` | function | `rbc_model_reconstruction (1).py:231` | `def save_obj(vertices, faces, filepath)` |
| `spherical_grid_to_cartesian` | function | `rbc_model_reconstruction (1).py:139` | `def spherical_grid_to_cartesian(r_grid, grid_size, scale)` |
| `compute_analytical_curvature` | function | `rbc_model_reconstruction.py:252` | `def compute_analytical_curvature(vertices, faces)` |
| `compute_face_areas` | function | `rbc_model_reconstruction.py:75` | `def compute_face_areas(vertices, faces)` |
| `compute_vertex_normals` | function | `rbc_model_reconstruction.py:54` | `def compute_vertex_normals(vertices, faces)` |
| `create_local_patches_for_vertices` | function | `rbc_model_reconstruction.py:124` | `def create_local_patches_for_vertices(vertices, faces, normals, grid_size)` |
| `load_model` | function | `rbc_model_reconstruction.py:84` | `def load_model(checkpoint_path, device, config)` |
| `load_rbc_mesh` | function | `rbc_model_reconstruction.py:31` | `def load_rbc_mesh(vert_path, face_path)` |
| `main` | function | `rbc_model_reconstruction.py:530` | `def main()` |
| `run_model_on_patches` | function | `rbc_model_reconstruction.py:215` | `def run_model_on_patches(model, patches_real, patches_imag, device, grid_size, batch_size)` |
| `save_html_viewer` | function | `rbc_model_reconstruction.py:319` | `def save_html_viewer(vertices, faces, normals, model_curvature, analytical_curvature, output_path)` |
| `save_ply_with_values` | function | `rbc_model_reconstruction.py:284` | `def save_ply_with_values(vertices, faces, normals, values, filepath, value_name)` |
| `CheckpointLoader` | class | `rbc_model_reconstruction_128.py:120` | `class CheckpointLoader` |
| `CylindricalProjector` | class | `rbc_model_reconstruction_128.py:377` | `class CylindricalProjector` |
| `ImprovedSphericalProjector` | class | `rbc_model_reconstruction_128.py:195` | `class ImprovedSphericalProjector` |
| `MeshExporter` | class | `rbc_model_reconstruction_128.py:589` | `class MeshExporter` |
| `MinimalSurfaceSpectralNetwork` | class | `rbc_model_reconstruction_128.py:85` | `class MinimalSurfaceSpectralNetwork(Module)` |
| `ModelBuilder` | class | `rbc_model_reconstruction_128.py:130` | `class ModelBuilder` |
| `RBCMeshLoader` | class | `rbc_model_reconstruction_128.py:169` | `class RBCMeshLoader` |
| `RBCReconstructionPipeline` | class | `rbc_model_reconstruction_128.py:757` | `class RBCReconstructionPipeline` |
| `ReconstructionConfig` | class | `rbc_model_reconstruction_128.py:37` | `class ReconstructionConfig` |
| `SpectralLayer` | class | `rbc_model_reconstruction_128.py:51` | `class SpectralLayer(Module)` |
| `SurfaceEvolver` | class | `rbc_model_reconstruction_128.py:542` | `class SurfaceEvolver` |
| `SyntheticShapeGenerator` | class | `rbc_model_reconstruction_128.py:469` | `class SyntheticShapeGenerator` |
| `WillmoreMetricsCalculator` | class | `rbc_model_reconstruction_128.py:514` | `class WillmoreMetricsCalculator` |
| `__init__` | method | `rbc_model_reconstruction_128.py:54` | `def __init__(self, channels, grid_size)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:88` | `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:206` | `def __init__(self, grid_size, smoothing_sigma)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:385` | `def __init__(self, grid_size, smoothing_sigma)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:472` | `def __init__(self, grid_size)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:517` | `def __init__(self, grid_size)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:545` | `def __init__(self, model, config)` |
| `__init__` | method | `rbc_model_reconstruction_128.py:760` | `def __init__(self, config)` |
| `_apply_spherical_smoothing` | method | `rbc_model_reconstruction_128.py:330` | `def _apply_spherical_smoothing(self, r_grid)` |
| `_area_weighted_projection` | method | `rbc_model_reconstruction_128.py:267` | `def _area_weighted_projection(self, theta, phi, r, areas)` |
| `_rbf_interpolation` | method | `rbc_model_reconstruction_128.py:300` | `def _rbf_interpolation(self, theta, phi, r)` |
| `build` | method | `rbc_model_reconstruction_128.py:134` | `def build(config)` |
| `build_argument_parser` | method | `rbc_model_reconstruction_128.py:926` | `def build_argument_parser()` |
| `compute_curvature_stats` | method | `rbc_model_reconstruction_128.py:524` | `def compute_curvature_stats(self, surface)` |
| `compute_vertex_areas` | method | `rbc_model_reconstruction_128.py:214` | `def compute_vertex_areas(self, vertices, faces)` |
| `compute_willmore` | method | `rbc_model_reconstruction_128.py:520` | `def compute_willmore(self, surface)` |
| `create_biconcave` | method | `rbc_model_reconstruction_128.py:481` | `def create_biconcave(self, radius, dimple_depth)` |
| `create_evans_fung_rbc` | method | `rbc_model_reconstruction_128.py:487` | `def create_evans_fung_rbc(self, radius, dimple_depth, thickness)` |
| `create_sphere` | method | `rbc_model_reconstruction_128.py:478` | `def create_sphere(self, radius)` |
| `evolve` | method | `rbc_model_reconstruction_128.py:553` | `def evolve(self, initial_surface)` |
| `forward` | method | `rbc_model_reconstruction_128.py:65` | `def forward(self, x)` |
| `forward` | method | `rbc_model_reconstruction_128.py:109` | `def forward(self, x)` |
| `load` | method | `rbc_model_reconstruction_128.py:124` | `def load(checkpoint_path, device)` |
| `load` | method | `rbc_model_reconstruction_128.py:173` | `def load(vert_path, face_path)` |
| `load_from_checkpoint` | method | `rbc_model_reconstruction_128.py:145` | `def load_from_checkpoint(checkpoint_path, config)` |
| `main` | method | `rbc_model_reconstruction_128.py:989` | `def main()` |
| `project_mesh` | method | `rbc_model_reconstruction_128.py:229` | `def project_mesh(self, vertices, faces, use_rbf)` |
| `project_mesh` | method | `rbc_model_reconstruction_128.py:393` | `def project_mesh(self, vertices, faces)` |
| `run` | method | `rbc_model_reconstruction_128.py:771` | `def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)` |
| `save_html_comparison` | method | `rbc_model_reconstruction_128.py:602` | `def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolv` |
| `save_obj` | method | `rbc_model_reconstruction_128.py:593` | `def save_obj(vertices, faces, filepath)` |
| `to_cartesian` | method | `rbc_model_reconstruction_128.py:352` | `def to_cartesian(self, r_grid, scale)` |
| `to_cartesian` | method | `rbc_model_reconstruction_128.py:442` | `def to_cartesian(self, rho_grid, z_scale, rho_scale)` |
| `CheckpointModelLoader` | class | `rbc_willmore_analysis.py:902` | `class CheckpointModelLoader(IModelLoader)` |
| `DiscreteCurvatureCalculator` | class | `rbc_willmore_analysis.py:563` | `class DiscreteCurvatureCalculator(ICurvatureCalculator)` |
| `ICurvatureCalculator` | class | `rbc_willmore_analysis.py:545` | `class ICurvatureCalculator(ABC)` |
| `IFileSystem` | class | `rbc_willmore_analysis.py:149` | `class IFileSystem(ABC)` |
| `ILogger` | class | `rbc_willmore_analysis.py:102` | `class ILogger(ABC)` |
| `IMeshLoader` | class | `rbc_willmore_analysis.py:228` | `class IMeshLoader(ABC)` |
| `IModelLoader` | class | `rbc_willmore_analysis.py:894` | `class IModelLoader(ABC)` |
| `MeshData` | class | `rbc_willmore_analysis.py:188` | `class MeshData` |
| `MinimalSurfaceSpectralNetwork` | class | `rbc_willmore_analysis.py:848` | `class MinimalSurfaceSpectralNetwork(Module)` |
| `OpenRBCMeshLoader` | class | `rbc_willmore_analysis.py:236` | `class OpenRBCMeshLoader(IMeshLoader)` |
| `RBCAnalysisConfig` | class | `rbc_willmore_analysis.py:55` | `class RBCAnalysisConfig` |
| `SpectralLayer` | class | `rbc_willmore_analysis.py:799` | `class SpectralLayer(Module)` |
| `StandardFileSystem` | class | `rbc_willmore_analysis.py:169` | `class StandardFileSystem(IFileSystem)` |
| `StandardLogger` | class | `rbc_willmore_analysis.py:122` | `class StandardLogger(ILogger)` |
| `SurfaceAnalysisEngine` | class | `rbc_willmore_analysis.py:1002` | `class SurfaceAnalysisEngine` |
| `SyntheticMeshGenerator` | class | `rbc_willmore_analysis.py:375` | `class SyntheticMeshGenerator` |
| `__init__` | method | `rbc_willmore_analysis.py:125` | `def __init__(self, name, level)` |
| `__init__` | method | `rbc_willmore_analysis.py:245` | `def __init__(self, filesystem, logger)` |
| `__init__` | method | `rbc_willmore_analysis.py:382` | `def __init__(self, logger)` |
| `__init__` | method | `rbc_willmore_analysis.py:578` | `def __init__(self, logger)` |
| `__init__` | method | `rbc_willmore_analysis.py:806` | `def __init__(self, channels, grid_size)` |
| `__init__` | method | `rbc_willmore_analysis.py:855` | `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)` |
| `__init__` | method | `rbc_willmore_analysis.py:905` | `def __init__(self, filesystem, logger)` |
| `__init__` | method | `rbc_willmore_analysis.py:1009` | `def __init__(self, config, logger, filesystem)` |
| `_analyze_rbc_morphology` | method | `rbc_willmore_analysis.py:1235` | `def _analyze_rbc_morphology(self)` |
| `_compute_areas` | method | `rbc_willmore_analysis.py:355` | `def _compute_areas(self, mesh)` |
| `_compute_asphericity` | method | `rbc_willmore_analysis.py:1141` | `def _compute_asphericity(self, mesh)` |
| `_compute_biconcavity_index` | method | `rbc_willmore_analysis.py:1161` | `def _compute_biconcavity_index(self, mesh, mean_curvature)` |
| `_compute_edge_cotangents` | method | `rbc_willmore_analysis.py:682` | `def _compute_edge_cotangents(self, mesh)` |
| `_compute_histogram` | method | `rbc_willmore_analysis.py:1186` | `def _compute_histogram(self, data, bins)` |
| `_compute_mesh_properties` | method | `rbc_willmore_analysis.py:511` | `def _compute_mesh_properties(self, mesh)` |
| `_compute_mixed_voronoi_area` | method | `rbc_willmore_analysis.py:748` | `def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)` |
| `_compute_normals` | method | `rbc_willmore_analysis.py:330` | `def _compute_normals(self, mesh)` |
| `_compute_surface_area` | method | `rbc_willmore_analysis.py:1125` | `def _compute_surface_area(self, mesh)` |
| `_compute_volume` | method | `rbc_willmore_analysis.py:1130` | `def _compute_volume(self, mesh)` |
| `_detect_model_params` | method | `rbc_willmore_analysis.py:909` | `def _detect_model_params(self, state_dict)` |
| `_generate_synthetic_meshes` | method | `rbc_willmore_analysis.py:1060` | `def _generate_synthetic_meshes(self)` |
| `_get_vertex_neighbors` | method | `rbc_willmore_analysis.py:737` | `def _get_vertex_neighbors(self, vertex_idx, faces)` |
| `_load_bonds` | method | `rbc_willmore_analysis.py:308` | `def _load_bonds(self, path)` |
| `_load_faces` | method | `rbc_willmore_analysis.py:286` | `def _load_faces(self, path)` |
| `_load_rbc_mesh` | method | `rbc_willmore_analysis.py:1048` | `def _load_rbc_mesh(self)` |
| `_load_vertices` | method | `rbc_willmore_analysis.py:267` | `def _load_vertices(self, path)` |
| `_verify_gauss_bonnet` | method | `rbc_willmore_analysis.py:1277` | `def _verify_gauss_bonnet(self)` |
| `analyze_mesh` | method | `rbc_willmore_analysis.py:1076` | `def analyze_mesh(self, mesh, name)` |
| `compute_gaussian_curvature` | method | `rbc_willmore_analysis.py:553` | `def compute_gaussian_curvature(self, mesh)` |
| `compute_gaussian_curvature` | method | `rbc_willmore_analysis.py:616` | `def compute_gaussian_curvature(self, mesh)` |
| `compute_mean_curvature` | method | `rbc_willmore_analysis.py:549` | `def compute_mean_curvature(self, mesh)` |
| `compute_mean_curvature` | method | `rbc_willmore_analysis.py:581` | `def compute_mean_curvature(self, mesh)` |
| `compute_willmore_energy` | method | `rbc_willmore_analysis.py:557` | `def compute_willmore_energy(self, mesh, mean_curvature)` |
| `compute_willmore_energy` | method | `rbc_willmore_analysis.py:664` | `def compute_willmore_energy(self, mesh, mean_curvature)` |
| `create_config_from_args` | method | `rbc_willmore_analysis.py:1470` | `def create_config_from_args(args)` |
| `debug` | method | `rbc_willmore_analysis.py:118` | `def debug(self, message)` |
| `debug` | method | `rbc_willmore_analysis.py:145` | `def debug(self, message)` |
| `error` | method | `rbc_willmore_analysis.py:114` | `def error(self, message)` |
| `error` | method | `rbc_willmore_analysis.py:142` | `def error(self, message)` |
| `exists` | method | `rbc_willmore_analysis.py:153` | `def exists(self, path)` |
| `exists` | method | `rbc_willmore_analysis.py:172` | `def exists(self, path)` |
| `forward` | method | `rbc_willmore_analysis.py:820` | `def forward(self, x)` |
| `forward` | method | `rbc_willmore_analysis.py:880` | `def forward(self, x)` |
| `generate_biconcave_disc` | method | `rbc_willmore_analysis.py:467` | `def generate_biconcave_disc(self, radius, thickness, resolution)` |
| `generate_sphere` | method | `rbc_willmore_analysis.py:385` | `def generate_sphere(self, radius, resolution)` |
| `generate_torus` | method | `rbc_willmore_analysis.py:424` | `def generate_torus(self, R, r, resolution)` |
| `info` | method | `rbc_willmore_analysis.py:106` | `def info(self, message)` |
| `info` | method | `rbc_willmore_analysis.py:136` | `def info(self, message)` |
| `initialize` | method | `rbc_willmore_analysis.py:1028` | `def initialize(self)` |
| `load` | method | `rbc_willmore_analysis.py:232` | `def load(self, vert_path, face_path, bond_path)` |
| `load` | method | `rbc_willmore_analysis.py:249` | `def load(self, vert_path, face_path, bond_path)` |
| `load` | method | `rbc_willmore_analysis.py:898` | `def load(self, checkpoint_path, device, config)` |
| `load` | method | `rbc_willmore_analysis.py:947` | `def load(self, checkpoint_path, device, config)` |
| `main` | method | `rbc_willmore_analysis.py:1488` | `def main()` |
| `makedirs` | method | `rbc_willmore_analysis.py:165` | `def makedirs(self, path)` |
| `makedirs` | method | `rbc_willmore_analysis.py:183` | `def makedirs(self, path)` |
| `num_bonds` | method | `rbc_willmore_analysis.py:214` | `def num_bonds(self)` |
| `num_faces` | method | `rbc_willmore_analysis.py:210` | `def num_faces(self)` |
| `num_vertices` | method | `rbc_willmore_analysis.py:206` | `def num_vertices(self)` |
| `parse_arguments` | method | `rbc_willmore_analysis.py:1376` | `def parse_arguments()` |
| `read_text` | method | `rbc_willmore_analysis.py:157` | `def read_text(self, path)` |
| `read_text` | method | `rbc_willmore_analysis.py:175` | `def read_text(self, path)` |
| `run_mean_curvature_flow` | method | `rbc_willmore_analysis.py:1318` | `def run_mean_curvature_flow(self, mesh, steps, dt)` |
| `run_shape_emergence_test` | method | `rbc_willmore_analysis.py:1192` | `def run_shape_emergence_test(self)` |
| `save_mesh_obj` | method | `rbc_willmore_analysis.py:1362` | `def save_mesh_obj(self, mesh, filename)` |
| `save_results` | method | `rbc_willmore_analysis.py:1357` | `def save_results(self, results, filename)` |
| `to_dict` | method | `rbc_willmore_analysis.py:217` | `def to_dict(self)` |
| `warning` | method | `rbc_willmore_analysis.py:110` | `def warning(self, message)` |
| `warning` | method | `rbc_willmore_analysis.py:139` | `def warning(self, message)` |
| `write_text` | method | `rbc_willmore_analysis.py:161` | `def write_text(self, path, content)` |
| `write_text` | method | `rbc_willmore_analysis.py:179` | `def write_text(self, path, content)` |
| `CheckpointModelLoader` | class | `rbc_willmore_analysis2.py:902` | `class CheckpointModelLoader(IModelLoader)` |
| `DiscreteCurvatureCalculator` | class | `rbc_willmore_analysis2.py:563` | `class DiscreteCurvatureCalculator(ICurvatureCalculator)` |
| `ICurvatureCalculator` | class | `rbc_willmore_analysis2.py:545` | `class ICurvatureCalculator(ABC)` |
| `IFileSystem` | class | `rbc_willmore_analysis2.py:149` | `class IFileSystem(ABC)` |
| `ILogger` | class | `rbc_willmore_analysis2.py:102` | `class ILogger(ABC)` |
| `IMeshLoader` | class | `rbc_willmore_analysis2.py:228` | `class IMeshLoader(ABC)` |
| `IModelLoader` | class | `rbc_willmore_analysis2.py:894` | `class IModelLoader(ABC)` |
| `MeshData` | class | `rbc_willmore_analysis2.py:188` | `class MeshData` |
| `MinimalSurfaceSpectralNetwork` | class | `rbc_willmore_analysis2.py:848` | `class MinimalSurfaceSpectralNetwork(Module)` |
| `OpenRBCMeshLoader` | class | `rbc_willmore_analysis2.py:236` | `class OpenRBCMeshLoader(IMeshLoader)` |
| `RBCAnalysisConfig` | class | `rbc_willmore_analysis2.py:55` | `class RBCAnalysisConfig` |
| `SpectralLayer` | class | `rbc_willmore_analysis2.py:799` | `class SpectralLayer(Module)` |
| `StandardFileSystem` | class | `rbc_willmore_analysis2.py:169` | `class StandardFileSystem(IFileSystem)` |
| `StandardLogger` | class | `rbc_willmore_analysis2.py:122` | `class StandardLogger(ILogger)` |
| `SurfaceAnalysisEngine` | class | `rbc_willmore_analysis2.py:1002` | `class SurfaceAnalysisEngine` |
| `SyntheticMeshGenerator` | class | `rbc_willmore_analysis2.py:375` | `class SyntheticMeshGenerator` |
| `__init__` | method | `rbc_willmore_analysis2.py:125` | `def __init__(self, name, level)` |
| `__init__` | method | `rbc_willmore_analysis2.py:245` | `def __init__(self, filesystem, logger)` |
| `__init__` | method | `rbc_willmore_analysis2.py:382` | `def __init__(self, logger)` |
| `__init__` | method | `rbc_willmore_analysis2.py:578` | `def __init__(self, logger)` |
| `__init__` | method | `rbc_willmore_analysis2.py:806` | `def __init__(self, channels, grid_size)` |
| `__init__` | method | `rbc_willmore_analysis2.py:855` | `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)` |
| `__init__` | method | `rbc_willmore_analysis2.py:905` | `def __init__(self, filesystem, logger)` |
| `__init__` | method | `rbc_willmore_analysis2.py:1009` | `def __init__(self, config, logger, filesystem)` |
| `_analyze_rbc_morphology` | method | `rbc_willmore_analysis2.py:1235` | `def _analyze_rbc_morphology(self)` |
| `_compute_areas` | method | `rbc_willmore_analysis2.py:355` | `def _compute_areas(self, mesh)` |
| `_compute_asphericity` | method | `rbc_willmore_analysis2.py:1141` | `def _compute_asphericity(self, mesh)` |
| `_compute_biconcavity_index` | method | `rbc_willmore_analysis2.py:1161` | `def _compute_biconcavity_index(self, mesh, mean_curvature)` |
| `_compute_edge_cotangents` | method | `rbc_willmore_analysis2.py:682` | `def _compute_edge_cotangents(self, mesh)` |
| `_compute_histogram` | method | `rbc_willmore_analysis2.py:1186` | `def _compute_histogram(self, data, bins)` |
| `_compute_mesh_properties` | method | `rbc_willmore_analysis2.py:511` | `def _compute_mesh_properties(self, mesh)` |
| `_compute_mixed_voronoi_area` | method | `rbc_willmore_analysis2.py:748` | `def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)` |
| `_compute_normals` | method | `rbc_willmore_analysis2.py:330` | `def _compute_normals(self, mesh)` |
| `_compute_surface_area` | method | `rbc_willmore_analysis2.py:1125` | `def _compute_surface_area(self, mesh)` |
| `_compute_volume` | method | `rbc_willmore_analysis2.py:1130` | `def _compute_volume(self, mesh)` |
| `_detect_model_params` | method | `rbc_willmore_analysis2.py:909` | `def _detect_model_params(self, state_dict)` |
| `_generate_synthetic_meshes` | method | `rbc_willmore_analysis2.py:1060` | `def _generate_synthetic_meshes(self)` |
| `_get_vertex_neighbors` | method | `rbc_willmore_analysis2.py:737` | `def _get_vertex_neighbors(self, vertex_idx, faces)` |
| `_load_bonds` | method | `rbc_willmore_analysis2.py:308` | `def _load_bonds(self, path)` |
| `_load_faces` | method | `rbc_willmore_analysis2.py:286` | `def _load_faces(self, path)` |
| `_load_rbc_mesh` | method | `rbc_willmore_analysis2.py:1048` | `def _load_rbc_mesh(self)` |
| `_load_vertices` | method | `rbc_willmore_analysis2.py:267` | `def _load_vertices(self, path)` |
| `_verify_gauss_bonnet` | method | `rbc_willmore_analysis2.py:1277` | `def _verify_gauss_bonnet(self)` |
| `analyze_mesh` | method | `rbc_willmore_analysis2.py:1076` | `def analyze_mesh(self, mesh, name)` |
| `compute_gaussian_curvature` | method | `rbc_willmore_analysis2.py:553` | `def compute_gaussian_curvature(self, mesh)` |
| `compute_gaussian_curvature` | method | `rbc_willmore_analysis2.py:616` | `def compute_gaussian_curvature(self, mesh)` |
| `compute_mean_curvature` | method | `rbc_willmore_analysis2.py:549` | `def compute_mean_curvature(self, mesh)` |
| `compute_mean_curvature` | method | `rbc_willmore_analysis2.py:581` | `def compute_mean_curvature(self, mesh)` |
| `compute_willmore_energy` | method | `rbc_willmore_analysis2.py:557` | `def compute_willmore_energy(self, mesh, mean_curvature)` |
| `compute_willmore_energy` | method | `rbc_willmore_analysis2.py:664` | `def compute_willmore_energy(self, mesh, mean_curvature)` |
| `convert_to_native` | method | `rbc_willmore_analysis2.py:1360` | `def convert_to_native(obj)` |
| `create_config_from_args` | method | `rbc_willmore_analysis2.py:1488` | `def create_config_from_args(args)` |
| `debug` | method | `rbc_willmore_analysis2.py:118` | `def debug(self, message)` |
| `debug` | method | `rbc_willmore_analysis2.py:145` | `def debug(self, message)` |
| `error` | method | `rbc_willmore_analysis2.py:114` | `def error(self, message)` |
| `error` | method | `rbc_willmore_analysis2.py:142` | `def error(self, message)` |
| `exists` | method | `rbc_willmore_analysis2.py:153` | `def exists(self, path)` |
| `exists` | method | `rbc_willmore_analysis2.py:172` | `def exists(self, path)` |
| `forward` | method | `rbc_willmore_analysis2.py:820` | `def forward(self, x)` |
| `forward` | method | `rbc_willmore_analysis2.py:880` | `def forward(self, x)` |
| `generate_biconcave_disc` | method | `rbc_willmore_analysis2.py:467` | `def generate_biconcave_disc(self, radius, thickness, resolution)` |
| `generate_sphere` | method | `rbc_willmore_analysis2.py:385` | `def generate_sphere(self, radius, resolution)` |
| `generate_torus` | method | `rbc_willmore_analysis2.py:424` | `def generate_torus(self, R, r, resolution)` |
| `info` | method | `rbc_willmore_analysis2.py:106` | `def info(self, message)` |
| `info` | method | `rbc_willmore_analysis2.py:136` | `def info(self, message)` |
| `initialize` | method | `rbc_willmore_analysis2.py:1028` | `def initialize(self)` |
| `load` | method | `rbc_willmore_analysis2.py:232` | `def load(self, vert_path, face_path, bond_path)` |
| `load` | method | `rbc_willmore_analysis2.py:249` | `def load(self, vert_path, face_path, bond_path)` |
| `load` | method | `rbc_willmore_analysis2.py:898` | `def load(self, checkpoint_path, device, config)` |
| `load` | method | `rbc_willmore_analysis2.py:947` | `def load(self, checkpoint_path, device, config)` |
| `main` | method | `rbc_willmore_analysis2.py:1506` | `def main()` |
| `makedirs` | method | `rbc_willmore_analysis2.py:165` | `def makedirs(self, path)` |
| `makedirs` | method | `rbc_willmore_analysis2.py:183` | `def makedirs(self, path)` |
| `num_bonds` | method | `rbc_willmore_analysis2.py:214` | `def num_bonds(self)` |
| `num_faces` | method | `rbc_willmore_analysis2.py:210` | `def num_faces(self)` |
| `num_vertices` | method | `rbc_willmore_analysis2.py:206` | `def num_vertices(self)` |
| `parse_arguments` | method | `rbc_willmore_analysis2.py:1394` | `def parse_arguments()` |
| `read_text` | method | `rbc_willmore_analysis2.py:157` | `def read_text(self, path)` |
| `read_text` | method | `rbc_willmore_analysis2.py:175` | `def read_text(self, path)` |
| `run_mean_curvature_flow` | method | `rbc_willmore_analysis2.py:1318` | `def run_mean_curvature_flow(self, mesh, steps, dt)` |
| `run_shape_emergence_test` | method | `rbc_willmore_analysis2.py:1192` | `def run_shape_emergence_test(self)` |
| `save_mesh_obj` | method | `rbc_willmore_analysis2.py:1380` | `def save_mesh_obj(self, mesh, filename)` |
| `save_results` | method | `rbc_willmore_analysis2.py:1357` | `def save_results(self, results, filename)` |
| `to_dict` | method | `rbc_willmore_analysis2.py:217` | `def to_dict(self)` |
| `warning` | method | `rbc_willmore_analysis2.py:110` | `def warning(self, message)` |
| `warning` | method | `rbc_willmore_analysis2.py:139` | `def warning(self, message)` |
| `write_text` | method | `rbc_willmore_analysis2.py:161` | `def write_text(self, path, content)` |
| `write_text` | method | `rbc_willmore_analysis2.py:179` | `def write_text(self, path, content)` |
| `load_model` | function | `test.py:20` | `def load_model(checkpoint_path, device)` |
| `main` | function | `test.py:154` | `def main()` |
| `test_model_behavior` | function | `test.py:45` | `def test_model_behavior(model, config, device)` |
| `AdaptiveLambdaScheduler` | class | `willmore_crsital2.py:1114` | `class AdaptiveLambdaScheduler(LambdaPressureScheduler)` |
| `AnnealingScheduler` | class | `willmore_crsital2.py:1161` | `class AnnealingScheduler` |
| `BatchSizeProspector` | class | `willmore_crsital2.py:1447` | `class BatchSizeProspector` |
| `CheckpointManager` | class | `willmore_crsital2.py:1261` | `class CheckpointManager` |
| `Config` | class | `willmore_crsital2.py:53` | `class Config` |
| `CrystallographyMetricsCalculator` | class | `willmore_crsital2.py:851` | `class CrystallographyMetricsCalculator(IMetricCalculator)` |
| `ExperimentOrchestrator` | class | `willmore_crsital2.py:1725` | `class ExperimentOrchestrator` |
| `FourierMassCenterAnalyzer` | class | `willmore_crsital2.py:711` | `class FourierMassCenterAnalyzer` |
| `FullFourierAnalyzer` | class | `willmore_crsital2.py:668` | `class FullFourierAnalyzer` |
| `FullTrainingOrchestrator` | class | `willmore_crsital2.py:1533` | `class FullTrainingOrchestrator` |
| `IMetricCalculator` | class | `willmore_crsital2.py:207` | `class IMetricCalculator(ABC)` |
| `IPhaseDetector` | class | `willmore_crsital2.py:201` | `class IPhaseDetector(ABC)` |
| `LambdaPressureScheduler` | class | `willmore_crsital2.py:1082` | `class LambdaPressureScheduler` |
| `LocalComplexityAnalyzer` | class | `willmore_crsital2.py:818` | `class LocalComplexityAnalyzer` |
| `LoggerFactory` | class | `willmore_crsital2.py:227` | `class LoggerFactory` |
| `MinimalSurfaceBackbone` | class | `willmore_crsital2.py:331` | `class MinimalSurfaceBackbone(Module)` |
| `MinimalSurfaceDataset` | class | `willmore_crsital2.py:452` | `class MinimalSurfaceDataset(Dataset)` |
| `MinimalSurfaceInferenceEngine` | class | `willmore_crsital2.py:351` | `class MinimalSurfaceInferenceEngine` |
| `MinimalSurfaceOperator` | class | `willmore_crsital2.py:242` | `class MinimalSurfaceOperator` |
| `MinimalSurfaceSpectralNetwork` | class | `willmore_crsital2.py:539` | `class MinimalSurfaceSpectralNetwork(Module)` |
| `Phase5CheckpointManager` | class | `willmore_crsital2.py:1291` | `class Phase5CheckpointManager` |
| `Phase5Orchestrator` | class | `willmore_crsital2.py:1663` | `class Phase5Orchestrator` |
| `QuadruplePrecisionLambdaScheduler` | class | `willmore_crsital2.py:1129` | `class QuadruplePrecisionLambdaScheduler` |
| `RefinementOrchestrator` | class | `willmore_crsital2.py:1599` | `class RefinementOrchestrator` |
| `RicciCurvatureCalculator` | class | `willmore_crsital2.py:1044` | `class RicciCurvatureCalculator(IMetricCalculator)` |
| `RicciFlowCalculator` | class | `willmore_crsital2.py:622` | `class RicciFlowCalculator(IMetricCalculator)` |
| `SeedManager` | class | `willmore_crsital2.py:213` | `class SeedManager` |
| `SeedMiner` | class | `willmore_crsital2.py:1483` | `class SeedMiner` |
| `SpectralFieldExtractor` | class | `willmore_crsital2.py:780` | `class SpectralFieldExtractor` |
| `SpectralGeometryCalculator` | class | `willmore_crsital2.py:1021` | `class SpectralGeometryCalculator(IMetricCalculator)` |
| `SpectralLayer` | class | `willmore_crsital2.py:307` | `class SpectralLayer(Module)` |
| `SpectroscopyMetricsCalculator` | class | `willmore_crsital2.py:1065` | `class SpectroscopyMetricsCalculator(IMetricCalculator)` |
| `SuperpositionAnalyzer` | class | `willmore_crsital2.py:833` | `class SuperpositionAnalyzer` |
| `SurfacePotentialGenerator` | class | `willmore_crsital2.py:399` | `class SurfacePotentialGenerator` |
| `ThermodynamicMetricsCalculator` | class | `willmore_crsital2.py:965` | `class ThermodynamicMetricsCalculator(IMetricCalculator)` |
| `TopologicalAnnealingScheduler` | class | `willmore_crsital2.py:1186` | `class TopologicalAnnealingScheduler(AnnealingScheduler)` |
| `TopologicalMetricsCalculator` | class | `willmore_crsital2.py:798` | `class TopologicalMetricsCalculator(IMetricCalculator)` |
| `TopologicalPhaseDetector` | class | `willmore_crsital2.py:751` | `class TopologicalPhaseDetector(IPhaseDetector)` |
| `TrainingEngine` | class | `willmore_crsital2.py:1338` | `class TrainingEngine` |
| `TrainingMetricsMonitor` | class | `willmore_crsital2.py:1202` | `class TrainingMetricsMonitor` |
| `WeightIntegrityChecker` | class | `willmore_crsital2.py:1322` | `class WeightIntegrityChecker` |
| `WillmoreEnergyCalculator` | class | `willmore_crsital2.py:567` | `class WillmoreEnergyCalculator(IMetricCalculator)` |
| `__getitem__` | method | `willmore_crsital2.py:535` | `def __getitem__(self, idx)` |
| `__init__` | method | `willmore_crsital2.py:243` | `def __init__(self, grid_size)` |
| `__init__` | method | `willmore_crsital2.py:308` | `def __init__(self, channels, grid_size)` |
| `__init__` | method | `willmore_crsital2.py:332` | `def __init__(self, grid_size, hidden_dim, num_spectral_layers)` |
| `__init__` | method | `willmore_crsital2.py:352` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:400` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:453` | `def __init__(self, config, surface_engine, seed)` |
| `__init__` | method | `willmore_crsital2.py:540` | `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)` |
| `__init__` | method | `willmore_crsital2.py:568` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:623` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:669` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:712` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:752` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:799` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:852` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:966` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1022` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1045` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1066` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1083` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1115` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1130` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1162` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1187` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1203` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1262` | `def __init__(self, config, checkpoint_dir)` |
| `__init__` | method | `willmore_crsital2.py:1292` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1339` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crsital2.py:1448` | `def __init__(self, config, surface_engine)` |
| `__init__` | method | `willmore_crsital2.py:1484` | `def __init__(self, config, surface_engine, batch_size)` |
| `__init__` | method | `willmore_crsital2.py:1534` | `def __init__(self, config, surface_engine, seed, batch_size)` |
| `__init__` | method | `willmore_crsital2.py:1600` | `def __init__(self, config, surface_engine, model, optimizer, monitor, seed, batch_size)` |
| `__init__` | method | `willmore_crsital2.py:1664` | `def __init__(self, config, surface_engine, model, monitor, seed, batch_size)` |
| `__init__` | method | `willmore_crsital2.py:1726` | `def __init__(self, config)` |
| `__len__` | method | `willmore_crsital2.py:534` | `def __len__(self)` |
| `_compute_flow_velocity` | method | `willmore_crsital2.py:659` | `def _compute_flow_velocity(self, metric)` |
| `_compute_ricci_scalar` | method | `willmore_crsital2.py:640` | `def _compute_ricci_scalar(self, metric)` |
| `_empty_metrics` | method | `willmore_crsital2.py:618` | `def _empty_metrics()` |
| `_empty_metrics` | method | `willmore_crsital2.py:664` | `def _empty_metrics()` |
| `_empty_metrics` | method | `willmore_crsital2.py:814` | `def _empty_metrics()` |
| `_estimate_sectional_curvatures` | method | `willmore_crsital2.py:647` | `def _estimate_sectional_curvatures(self, metric)` |
| `_evolve_minimal_surface` | method | `willmore_crsital2.py:513` | `def _evolve_minimal_surface(self, surface_real, surface_imag, potential, energy)` |
| `_get_freq_grids` | method | `willmore_crsital2.py:720` | `def _get_freq_grids(self, H, W, device)` |
| `_precompute_spectral_operators` | method | `willmore_crsital2.py:249` | `def _precompute_spectral_operators(self)` |
| `_save_final_results` | method | `willmore_crsital2.py:1789` | `def _save_final_results(self, model, monitor, seed, batch_size)` |
| `_solve_minimal_surface` | method | `willmore_crsital2.py:487` | `def _solve_minimal_surface(self, potential, sample_seed)` |
| `_try_load_backbone` | method | `willmore_crsital2.py:359` | `def _try_load_backbone(self)` |
| `accept_perturbation` | method | `willmore_crsital2.py:1176` | `def accept_perturbation(self, delta_loss)` |
| `apply_laplacian` | method | `willmore_crsital2.py:257` | `def apply_laplacian(self, field)` |
| `apply_mean_curvature` | method | `willmore_crsital2.py:382` | `def apply_mean_curvature(self, surface)` |
| `build_argument_parser` | method | `willmore_crsital2.py:1839` | `def build_argument_parser()` |
| `check` | method | `willmore_crsital2.py:1324` | `def check(model)` |
| `collect_all_metrics` | method | `willmore_crsital2.py:1408` | `def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)` |
| `compute` | method | `willmore_crsital2.py:209` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:573` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:627` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:804` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:856` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:969` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:1025` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:1048` | `def compute(self, model)` |
| `compute` | method | `willmore_crsital2.py:1069` | `def compute(self, model)` |
| `compute_all_metrics` | method | `willmore_crsital2.py:953` | `def compute_all_metrics(self, model, val_x, val_y)` |
| `compute_alpha_purity` | method | `willmore_crsital2.py:911` | `def compute_alpha_purity(self, model)` |
| `compute_critical_temperature` | method | `willmore_crsital2.py:1017` | `def compute_critical_temperature(self, alpha)` |
| `compute_delta_slope` | method | `willmore_crsital2.py:1219` | `def compute_delta_slope(self)` |
| `compute_discretization_margin` | method | `willmore_crsital2.py:903` | `def compute_discretization_margin(self, model)` |
| `compute_effective_temperature` | method | `willmore_crsital2.py:983` | `def compute_effective_temperature(self, gradient_buffer, learning_rate)` |
| `compute_full_spectrum` | method | `willmore_crsital2.py:677` | `def compute_full_spectrum(self, spectral_field)` |
| `compute_gaussian_curvature` | method | `willmore_crsital2.py:273` | `def compute_gaussian_curvature(self, surface)` |
| `compute_gibbs_free_energy` | method | `willmore_crsital2.py:1010` | `def compute_gibbs_free_energy(self, delta, alpha, temperature)` |
| `compute_hbar_effective` | method | `willmore_crsital2.py:946` | `def compute_hbar_effective(self, model, lambda_pressure)` |
| `compute_kappa` | method | `willmore_crsital2.py:861` | `def compute_kappa(self, model, val_x, val_y, num_batches)` |
| `compute_kappa_quantum` | method | `willmore_crsital2.py:916` | `def compute_kappa_quantum(self, model)` |
| `compute_local_complexity` | method | `willmore_crsital2.py:820` | `def compute_local_complexity(weights, epsilon)` |
| `compute_mass_center` | method | `willmore_crsital2.py:728` | `def compute_mass_center(self, spectral_field)` |
| `compute_mean_curvature` | method | `willmore_crsital2.py:262` | `def compute_mean_curvature(self, surface)` |
| `compute_norm_conservation_error` | method | `willmore_crsital2.py:1364` | `def compute_norm_conservation_error(self, model, val_x)` |
| `compute_poynting_vector` | method | `willmore_crsital2.py:935` | `def compute_poynting_vector(self, model)` |
| `compute_regularization_loss` | method | `willmore_crsital2.py:1102` | `def compute_regularization_loss(self, model)` |
| `compute_regularization_loss` | method | `willmore_crsital2.py:1149` | `def compute_regularization_loss(self, model)` |
| `compute_resonance_metrics` | method | `willmore_crsital2.py:701` | `def compute_resonance_metrics(self, spectral_field)` |
| `compute_specific_heat` | method | `willmore_crsital2.py:1001` | `def compute_specific_heat(self, loss_history, temp_history)` |
| `compute_superposition` | method | `willmore_crsital2.py:835` | `def compute_superposition(weights)` |
| `compute_surface_area` | method | `willmore_crsital2.py:290` | `def compute_surface_area(self, surface)` |
| `compute_surface_metrics` | method | `willmore_crsital2.py:590` | `def compute_surface_metrics(self, surface)` |
| `compute_weight_metrics` | method | `willmore_crsital2.py:1354` | `def compute_weight_metrics(self, model)` |
| `compute_willmore_energy` | method | `willmore_crsital2.py:284` | `def compute_willmore_energy(self, surface)` |
| `create_logger` | method | `willmore_crsital2.py:229` | `def create_logger(name, level)` |
| `cube_potential` | method | `willmore_crsital2.py:411` | `def cube_potential(self)` |
| `current_lambda` | method | `willmore_crsital2.py:1092` | `def current_lambda(self)` |
| `current_lambda` | method | `willmore_crsital2.py:1139` | `def current_lambda(self)` |
| `detect` | method | `willmore_crsital2.py:203` | `def detect(self, spectral_field)` |
| `detect` | method | `willmore_crsital2.py:759` | `def detect(self, spectral_field)` |
| `dodecahedron_potential` | method | `willmore_crsital2.py:418` | `def dodecahedron_potential(self)` |
| `extract` | method | `willmore_crsital2.py:782` | `def extract(model, grid_size)` |
| `format_progress_bar` | method | `willmore_crsital2.py:1229` | `def format_progress_bar(self, epoch, total_epochs, phase)` |
| `forward` | method | `willmore_crsital2.py:315` | `def forward(self, x)` |
| `forward` | method | `willmore_crsital2.py:342` | `def forward(self, x)` |
| `forward` | method | `willmore_crsital2.py:557` | `def forward(self, x)` |
| `generate_mixed_potential` | method | `willmore_crsital2.py:442` | `def generate_mixed_potential(self, seed)` |
| `get_validation_batch` | method | `willmore_crsital2.py:536` | `def get_validation_batch(self)` |
| `hyperbolic_potential` | method | `willmore_crsital2.py:434` | `def hyperbolic_potential(self)` |
| `main` | method | `willmore_crsital2.py:1868` | `def main()` |
| `mean_curvature_evolve` | method | `willmore_crsital2.py:388` | `def mean_curvature_evolve(self, surface, dt)` |
| `mean_curvature_flow` | method | `willmore_crsital2.py:297` | `def mean_curvature_flow(self, surface, dt)` |
| `mine` | method | `willmore_crsital2.py:1490` | `def mine(self)` |
| `prospect` | method | `willmore_crsital2.py:1453` | `def prospect(self)` |
| `pyramid_potential` | method | `willmore_crsital2.py:404` | `def pyramid_potential(self)` |
| `run` | method | `willmore_crsital2.py:1730` | `def run(self)` |
| `run_phase3_training` | method | `willmore_crsital2.py:1541` | `def run_phase3_training(self)` |
| `run_phase4_refinement` | method | `willmore_crsital2.py:1610` | `def run_phase4_refinement(self)` |
| `run_phase5_crystallization` | method | `willmore_crsital2.py:1674` | `def run_phase5_crystallization(self)` |
| `safe_get` | method | `willmore_crsital2.py:1231` | `def safe_get(key)` |
| `save_checkpoint` | method | `willmore_crsital2.py:1276` | `def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)` |
| `save_checkpoint` | method | `willmore_crsital2.py:1307` | `def save_checkpoint(self, model, optimizer, epoch, metrics, lambda_value)` |
| `set_lambda` | method | `willmore_crsital2.py:1110` | `def set_lambda(self, value)` |
| `set_lambda` | method | `willmore_crsital2.py:1157` | `def set_lambda(self, value)` |
| `set_seed` | method | `willmore_crsital2.py:215` | `def set_seed(seed, device)` |
| `should_restart` | method | `willmore_crsital2.py:1182` | `def should_restart(self, current_delta, best_delta)` |
| `should_save` | method | `willmore_crsital2.py:1302` | `def should_save(self, current_delta, current_alpha, current_acc)` |
| `should_save_checkpoint` | method | `willmore_crsital2.py:1271` | `def should_save_checkpoint(self)` |
| `step` | method | `willmore_crsital2.py:1095` | `def step(self, epoch)` |
| `step` | method | `willmore_crsital2.py:1142` | `def step(self, epoch, improvement)` |
| `step` | method | `willmore_crsital2.py:1173` | `def step(self)` |
| `step_adaptive` | method | `willmore_crsital2.py:1120` | `def step_adaptive(self, epoch, topo_phase_state)` |
| `step_adaptive` | method | `willmore_crsital2.py:1191` | `def step_adaptive(self, alignment_trend, resonance_score)` |
| `temperature` | method | `willmore_crsital2.py:1170` | `def temperature(self)` |
| `torus_potential` | method | `willmore_crsital2.py:426` | `def torus_potential(self)` |
| `train_single_epoch` | method | `willmore_crsital2.py:1373` | `def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler)` |
| `update_metrics` | method | `willmore_crsital2.py:1210` | `def update_metrics(self)` |
| `validate` | method | `willmore_crsital2.py:1398` | `def validate(self, model, val_x, val_y)` |
| `AccuracyTest` | class | `willmore_crystallography_suite.py.py:799` | `class AccuracyTest(FunctionalTest)` |
| `BatchProcessor` | class | `willmore_crystallography_suite.py.py:1321` | `class BatchProcessor` |
| `BerryPhaseCalculator` | class | `willmore_crystallography_suite.py.py:709` | `class BerryPhaseCalculator` |
| `CheckpointAnalyzer` | class | `willmore_crystallography_suite.py.py:900` | `class CheckpointAnalyzer` |
| `ComprehensiveVisualizer` | class | `willmore_crystallography_suite.py.py:1035` | `class ComprehensiveVisualizer` |
| `DiscretizationCalculator` | class | `willmore_crystallography_suite.py.py:410` | `class DiscretizationCalculator` |
| `FunctionalTest` | class | `willmore_crystallography_suite.py.py:787` | `class FunctionalTest(ABC)` |
| `GeneralizationTest` | class | `willmore_crystallography_suite.py.py:866` | `class GeneralizationTest(FunctionalTest)` |
| `MinimalSurfaceDataset` | class | `willmore_crystallography_suite.py.py:298` | `class MinimalSurfaceDataset(Dataset)` |
| `MinimalSurfaceOperator` | class | `willmore_crystallography_suite.py.py:181` | `class MinimalSurfaceOperator` |
| `MinimalSurfaceSpectralNetwork` | class | `willmore_crystallography_suite.py.py:138` | `class MinimalSurfaceSpectralNetwork(Module)` |
| `RicciCurvatureCalculator` | class | `willmore_crystallography_suite.py.py:500` | `class RicciCurvatureCalculator` |
| `SpectralGeometryCalculator` | class | `willmore_crystallography_suite.py.py:440` | `class SpectralGeometryCalculator` |
| `SpectralLayer` | class | `willmore_crystallography_suite.py.py:92` | `class SpectralLayer(Module)` |
| `SurfacePotentialGenerator` | class | `willmore_crystallography_suite.py.py:237` | `class SurfacePotentialGenerator` |
| `SurfaceReconstructionTest` | class | `willmore_crystallography_suite.py.py:823` | `class SurfaceReconstructionTest(FunctionalTest)` |
| `TopologicalPhaseDetector` | class | `willmore_crystallography_suite.py.py:619` | `class TopologicalPhaseDetector` |
| `WeightIntegrityCalculator` | class | `willmore_crystallography_suite.py.py:374` | `class WeightIntegrityCalculator` |
| `WillmoreEnergyCalculator` | class | `willmore_crystallography_suite.py.py:547` | `class WillmoreEnergyCalculator` |
| `WillmoreSuiteConfig` | class | `willmore_crystallography_suite.py.py:52` | `class WillmoreSuiteConfig` |
| `__getitem__` | method | `willmore_crystallography_suite.py.py:367` | `def __getitem__(self, idx)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:95` | `def __init__(self, channels, grid_size)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:141` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:184` | `def __init__(self, grid_size)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:240` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:301` | `def __init__(self, config, seed, num_samples)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:377` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:413` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:443` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:503` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:550` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:622` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:712` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:790` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:826` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:903` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:1038` | `def __init__(self, config)` |
| `__init__` | method | `willmore_crystallography_suite.py.py:1324` | `def __init__(self, config)` |
| `__len__` | method | `willmore_crystallography_suite.py.py:364` | `def __len__(self)` |
| `_compute_health_score` | method | `willmore_crystallography_suite.py.py:1012` | `def _compute_health_score(self, results)` |
| `_compute_surface_metrics` | method | `willmore_crystallography_suite.py.py:575` | `def _compute_surface_metrics(self, surface)` |
| `_empty_metrics` | method | `willmore_crystallography_suite.py.py:605` | `def _empty_metrics()` |
| `_extract_epoch` | method | `willmore_crystallography_suite.py.py:734` | `def _extract_epoch(self, filepath)` |
| `_extract_spectral_field` | method | `willmore_crystallography_suite.py.py:997` | `def _extract_spectral_field(self, model)` |
| `_generate_summary` | method | `willmore_crystallography_suite.py.py:1407` | `def _generate_summary(self, ranked, output_dir)` |
| `_generate_surface_pair` | method | `willmore_crystallography_suite.py.py:331` | `def _generate_surface_pair(self, potential, sample_seed)` |
| `_plot_crystal_verdict` | method | `willmore_crystallography_suite.py.py:1279` | `def _plot_crystal_verdict(self, results, ax)` |
| `_plot_discretization` | method | `willmore_crystallography_suite.py.py:1085` | `def _plot_discretization(self, results, ax)` |
| `_plot_functional_test_1` | method | `willmore_crystallography_suite.py.py:1145` | `def _plot_functional_test_1(self, results, ax)` |
| `_plot_functional_test_2` | method | `willmore_crystallography_suite.py.py:1165` | `def _plot_functional_test_2(self, results, ax)` |
| `_plot_functional_test_3` | method | `willmore_crystallography_suite.py.py:1188` | `def _plot_functional_test_3(self, results, ax)` |
| `_plot_health_summary` | method | `willmore_crystallography_suite.py.py:1210` | `def _plot_health_summary(self, results, ax)` |
| `_plot_layer_deltas` | method | `willmore_crystallography_suite.py.py:1240` | `def _plot_layer_deltas(self, results, ax)` |
| `_plot_phase_diagram` | method | `willmore_crystallography_suite.py.py:1259` | `def _plot_phase_diagram(self, results, ax)` |
| `_plot_ricci_curvature` | method | `willmore_crystallography_suite.py.py:1132` | `def _plot_ricci_curvature(self, results, ax)` |
| `_plot_spectral_geometry` | method | `willmore_crystallography_suite.py.py:1111` | `def _plot_spectral_geometry(self, results, ax)` |
| `_plot_weight_integrity` | method | `willmore_crystallography_suite.py.py:1067` | `def _plot_weight_integrity(self, results, ax)` |
| `_precompute_spectral_operators` | method | `willmore_crystallography_suite.py.py:188` | `def _precompute_spectral_operators(self)` |
| `_rank_checkpoints` | method | `willmore_crystallography_suite.py.py:1381` | `def _rank_checkpoints(self, all_results)` |
| `analyze_checkpoint` | method | `willmore_crystallography_suite.py.py:918` | `def analyze_checkpoint(self, checkpoint_path, dataset)` |
| `apply_laplacian` | method | `willmore_crystallography_suite.py.py:196` | `def apply_laplacian(self, field)` |
| `calculate_berry_phase` | method | `willmore_crystallography_suite.py.py:751` | `def calculate_berry_phase(self, checkpoint_dir)` |
| `compute` | method | `willmore_crystallography_suite.py.py:380` | `def compute(self, model)` |
| `compute` | method | `willmore_crystallography_suite.py.py:416` | `def compute(self, model)` |
| `compute` | method | `willmore_crystallography_suite.py.py:446` | `def compute(self, model)` |
| `compute` | method | `willmore_crystallography_suite.py.py:506` | `def compute(self, model)` |
| `compute` | method | `willmore_crystallography_suite.py.py:554` | `def compute(self, model)` |
| `compute_gaussian_curvature` | method | `willmore_crystallography_suite.py.py:212` | `def compute_gaussian_curvature(self, surface)` |
| `compute_mean_curvature` | method | `willmore_crystallography_suite.py.py:201` | `def compute_mean_curvature(self, surface)` |
| `compute_surface_area` | method | `willmore_crystallography_suite.py.py:229` | `def compute_surface_area(self, surface)` |
| `compute_willmore_energy` | method | `willmore_crystallography_suite.py.py:223` | `def compute_willmore_energy(self, surface)` |
| `cube_potential` | method | `willmore_crystallography_suite.py.py:251` | `def cube_potential(self)` |
| `detect` | method | `willmore_crystallography_suite.py.py:628` | `def detect(self, spectral_field)` |
| `dodecahedron_potential` | method | `willmore_crystallography_suite.py.py:258` | `def dodecahedron_potential(self)` |
| `flatten_spectral_kernels` | method | `willmore_crystallography_suite.py.py:738` | `def flatten_spectral_kernels(self, state_dict)` |
| `forward` | method | `willmore_crystallography_suite.py.py:112` | `def forward(self, x)` |
| `forward` | method | `willmore_crystallography_suite.py.py:160` | `def forward(self, x)` |
| `generate_mixed_potential` | method | `willmore_crystallography_suite.py.py:282` | `def generate_mixed_potential(self, seed)` |
| `get_spectral_representation` | method | `willmore_crystallography_suite.py.py:171` | `def get_spectral_representation(self, x)` |
| `get_validation_batch` | method | `willmore_crystallography_suite.py.py:370` | `def get_validation_batch(self)` |
| `hyperbolic_potential` | method | `willmore_crystallography_suite.py.py:274` | `def hyperbolic_potential(self)` |
| `load_checkpoints` | method | `willmore_crystallography_suite.py.py:715` | `def load_checkpoints(self, checkpoint_dir)` |
| `main` | method | `willmore_crystallography_suite.py.py:1452` | `def main()` |
| `process_directory` | method | `willmore_crystallography_suite.py.py:1331` | `def process_directory(self, checkpoint_dir, output_dir, dataset)` |
| `pyramid_potential` | method | `willmore_crystallography_suite.py.py:244` | `def pyramid_potential(self)` |
| `run` | method | `willmore_crystallography_suite.py.py:795` | `def run(self, model, dataset)` |
| `run` | method | `willmore_crystallography_suite.py.py:802` | `def run(self, model, dataset)` |
| `run` | method | `willmore_crystallography_suite.py.py:830` | `def run(self, model, dataset)` |
| `run` | method | `willmore_crystallography_suite.py.py:869` | `def run(self, model, dataset)` |
| `setup_logging` | method | `willmore_crystallography_suite.py.py:1444` | `def setup_logging(log_level)` |
| `torus_potential` | method | `willmore_crystallography_suite.py.py:266` | `def torus_potential(self)` |
| `visualize_analysis` | method | `willmore_crystallography_suite.py.py:1041` | `def visualize_analysis(self, results, output_path)` |
| `BilinearSpectralInterpolator` | class | `willmore_zero_shot_scaler.py:387` | `class BilinearSpectralInterpolator(ISpectralWeightInterpolator)` |
| `FourierSpectralInterpolator` | class | `willmore_zero_shot_scaler.py:274` | `class FourierSpectralInterpolator(ISpectralWeightInterpolator)` |
| `ICheckpointManager` | class | `willmore_zero_shot_scaler.py:207` | `class ICheckpointManager(ABC)` |
| `IConfigurationLoader` | class | `willmore_zero_shot_scaler.py:144` | `class IConfigurationLoader(ABC)` |
| `IGridScaler` | class | `willmore_zero_shot_scaler.py:445` | `class IGridScaler(ABC)` |
| `IMetricsEvaluator` | class | `willmore_zero_shot_scaler.py:583` | `class IMetricsEvaluator(ABC)` |
| `ISpectralWeightInterpolator` | class | `willmore_zero_shot_scaler.py:260` | `class ISpectralWeightInterpolator(ABC)` |
| `ScalerConfig` | class | `willmore_zero_shot_scaler.py:115` | `class ScalerConfig` |
| `ScalingPipeline` | class | `willmore_zero_shot_scaler.py:776` | `class ScalingPipeline` |
| `TOMLConfigurationLoader` | class | `willmore_zero_shot_scaler.py:153` | `class TOMLConfigurationLoader(IConfigurationLoader)` |
| `WillmoreCheckpointManager` | class | `willmore_zero_shot_scaler.py:221` | `class WillmoreCheckpointManager(ICheckpointManager)` |
| `WillmoreGridScaler` | class | `willmore_zero_shot_scaler.py:458` | `class WillmoreGridScaler(IGridScaler)` |
| `WillmoreMetricsEvaluator` | class | `willmore_zero_shot_scaler.py:597` | `class WillmoreMetricsEvaluator(IMetricsEvaluator)` |
| `__init__` | method | `willmore_zero_shot_scaler.py:224` | `def __init__(self, config)` |
| `__init__` | method | `willmore_zero_shot_scaler.py:277` | `def __init__(self, config)` |
| `__init__` | method | `willmore_zero_shot_scaler.py:390` | `def __init__(self, config)` |
| `__init__` | method | `willmore_zero_shot_scaler.py:461` | `def __init__(self, config, interpolator)` |
| `__init__` | method | `willmore_zero_shot_scaler.py:600` | `def __init__(self, config)` |
| `__init__` | method | `willmore_zero_shot_scaler.py:779` | `def __init__(self, config)` |
| `_check_degradation` | method | `willmore_zero_shot_scaler.py:930` | `def _check_degradation(self, source_metrics, current_metrics)` |
| `_compile_final_results` | method | `willmore_zero_shot_scaler.py:971` | `def _compile_final_results(self)` |
| `_compute_curvature_metrics` | method | `willmore_zero_shot_scaler.py:677` | `def _compute_curvature_metrics(self, surface)` |
| `_compute_spectral_metrics` | method | `willmore_zero_shot_scaler.py:702` | `def _compute_spectral_metrics(self, model)` |
| `_compute_willmore_metrics` | method | `willmore_zero_shot_scaler.py:661` | `def _compute_willmore_metrics(self, surface)` |
| `_construct_weight_surface` | method | `willmore_zero_shot_scaler.py:639` | `def _construct_weight_surface(self, model, grid_size)` |
| `_count_spectral_layers` | method | `willmore_zero_shot_scaler.py:505` | `def _count_spectral_layers(self, model)` |
| `_evaluate_inference_quality` | method | `willmore_zero_shot_scaler.py:735` | `def _evaluate_inference_quality(self, model, grid_size, num_samples)` |
| `_extract_expansion_dim` | method | `willmore_zero_shot_scaler.py:500` | `def _extract_expansion_dim(self, model)` |
| `_extract_hidden_dim` | method | `willmore_zero_shot_scaler.py:495` | `def _extract_hidden_dim(self, model)` |
| `_from_dict` | method | `willmore_zero_shot_scaler.py:170` | `def _from_dict(self, data)` |
| `_from_toml` | method | `willmore_zero_shot_scaler.py:161` | `def _from_toml(self, path)` |
| `_interpolate_2d_spectral` | method | `willmore_zero_shot_scaler.py:294` | `def _interpolate_2d_spectral(self, source, target_shape)` |
| `_interpolate_4d_spectral` | method | `willmore_zero_shot_scaler.py:314` | `def _interpolate_4d_spectral(self, source, target_shape)` |
| `_interpolate_generic` | method | `willmore_zero_shot_scaler.py:369` | `def _interpolate_generic(self, source, target_shape)` |
| `_interpolate_generic` | method | `willmore_zero_shot_scaler.py:419` | `def _interpolate_generic(self, source, target_shape)` |
| `_is_better_metrics` | method | `willmore_zero_shot_scaler.py:946` | `def _is_better_metrics(self, current, best)` |
| `_load_source_model` | method | `willmore_zero_shot_scaler.py:888` | `def _load_source_model(self)` |
| `_log_metrics` | method | `willmore_zero_shot_scaler.py:914` | `def _log_metrics(self, metrics, grid_size)` |
| `_pad_spectrum_2d` | method | `willmore_zero_shot_scaler.py:332` | `def _pad_spectrum_2d(self, spectrum, target_h, target_w)` |
| `_save_final_results` | method | `willmore_zero_shot_scaler.py:985` | `def _save_final_results(self, results)` |
| `_save_scaled_model` | method | `willmore_zero_shot_scaler.py:961` | `def _save_scaled_model(self, model, metrics, grid_size)` |
| `_scale_conv_weight` | method | `willmore_zero_shot_scaler.py:549` | `def _scale_conv_weight(self, weight, target_shape)` |
| `_scale_spectral_kernel` | method | `willmore_zero_shot_scaler.py:535` | `def _scale_spectral_kernel(self, kernel, target_shape, source_grid, target_grid)` |
| `_transfer_weights` | method | `willmore_zero_shot_scaler.py:510` | `def _transfer_weights(self, source, target, source_grid, target_grid)` |
| `_validate_weight_transfer` | method | `willmore_zero_shot_scaler.py:570` | `def _validate_weight_transfer(self, source, target)` |
| `_write_detailed_report` | method | `willmore_zero_shot_scaler.py:997` | `def _write_detailed_report(self, results, path)` |
| `build_argument_parser` | method | `willmore_zero_shot_scaler.py:1053` | `def build_argument_parser()` |
| `create_default_config_file` | method | `willmore_zero_shot_scaler.py:1046` | `def create_default_config_file(path)` |
| `evaluate` | method | `willmore_zero_shot_scaler.py:587` | `def evaluate(self, model, grid_size, num_samples)` |
| `evaluate` | method | `willmore_zero_shot_scaler.py:606` | `def evaluate(self, model, grid_size, num_samples)` |
| `execute` | method | `willmore_zero_shot_scaler.py:796` | `def execute(self)` |
| `interpolate` | method | `willmore_zero_shot_scaler.py:264` | `def interpolate(self, source_weight, target_shape)` |
| `interpolate` | method | `willmore_zero_shot_scaler.py:281` | `def interpolate(self, source_weight, target_shape)` |
| `interpolate` | method | `willmore_zero_shot_scaler.py:394` | `def interpolate(self, source_weight, target_shape)` |
| `load` | method | `willmore_zero_shot_scaler.py:148` | `def load(self, source)` |
| `load` | method | `willmore_zero_shot_scaler.py:156` | `def load(self, source)` |
| `load_checkpoint` | method | `willmore_zero_shot_scaler.py:211` | `def load_checkpoint(self, path, device)` |
| `load_checkpoint` | method | `willmore_zero_shot_scaler.py:228` | `def load_checkpoint(self, path, device)` |
| `main` | method | `willmore_zero_shot_scaler.py:1129` | `def main()` |
| `save_checkpoint` | method | `willmore_zero_shot_scaler.py:216` | `def save_checkpoint(self, model, metrics, path)` |
| `save_checkpoint` | method | `willmore_zero_shot_scaler.py:246` | `def save_checkpoint(self, model, metrics, path)` |
| `scale_model` | method | `willmore_zero_shot_scaler.py:449` | `def scale_model(self, source_model, target_grid_size)` |
| `scale_model` | method | `willmore_zero_shot_scaler.py:470` | `def scale_model(self, source_model, target_grid_size)` |
| `CheckpointLoader` | class | `wilmore_rbc.py:123` | `class CheckpointLoader` |
| `CylindricalProjector` | class | `wilmore_rbc.py:380` | `class CylindricalProjector` |
| `ImprovedSphericalProjector` | class | `wilmore_rbc.py:198` | `class ImprovedSphericalProjector` |
| `MeshExporter` | class | `wilmore_rbc.py:623` | `class MeshExporter` |
| `MinimalSurfaceSpectralNetwork` | class | `wilmore_rbc.py:88` | `class MinimalSurfaceSpectralNetwork(Module)` |
| `ModelBuilder` | class | `wilmore_rbc.py:133` | `class ModelBuilder` |
| `RBCMeshLoader` | class | `wilmore_rbc.py:172` | `class RBCMeshLoader` |
| `RBCReconstructionPipeline` | class | `wilmore_rbc.py:791` | `class RBCReconstructionPipeline` |
| `ReconstructionConfig` | class | `wilmore_rbc.py:37` | `class ReconstructionConfig` |
| `SpectralLayer` | class | `wilmore_rbc.py:54` | `class SpectralLayer(Module)` |
| `SurfaceEvolver` | class | `wilmore_rbc.py:545` | `class SurfaceEvolver` |
| `SyntheticShapeGenerator` | class | `wilmore_rbc.py:472` | `class SyntheticShapeGenerator` |
| `WillmoreMetricsCalculator` | class | `wilmore_rbc.py:517` | `class WillmoreMetricsCalculator` |
| `__init__` | method | `wilmore_rbc.py:57` | `def __init__(self, channels, grid_size)` |
| `__init__` | method | `wilmore_rbc.py:91` | `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)` |
| `__init__` | method | `wilmore_rbc.py:209` | `def __init__(self, grid_size, smoothing_sigma)` |
| `__init__` | method | `wilmore_rbc.py:388` | `def __init__(self, grid_size, smoothing_sigma)` |
| `__init__` | method | `wilmore_rbc.py:475` | `def __init__(self, grid_size)` |
| `__init__` | method | `wilmore_rbc.py:520` | `def __init__(self, grid_size)` |
| `__init__` | method | `wilmore_rbc.py:548` | `def __init__(self, model, config)` |
| `__init__` | method | `wilmore_rbc.py:794` | `def __init__(self, config)` |
| `_apply_spherical_smoothing` | method | `wilmore_rbc.py:333` | `def _apply_spherical_smoothing(self, r_grid)` |
| `_area_weighted_projection` | method | `wilmore_rbc.py:270` | `def _area_weighted_projection(self, theta, phi, r, areas)` |
| `_compute_lr` | method | `wilmore_rbc.py:556` | `def _compute_lr(self, step)` |
| `_compute_volume` | method | `wilmore_rbc.py:567` | `def _compute_volume(self, surface)` |
| `_normalize_volume` | method | `wilmore_rbc.py:571` | `def _normalize_volume(self, surface, target_volume)` |
| `_rbf_interpolation` | method | `wilmore_rbc.py:303` | `def _rbf_interpolation(self, theta, phi, r)` |
| `build` | method | `wilmore_rbc.py:137` | `def build(config)` |
| `build_argument_parser` | method | `wilmore_rbc.py:960` | `def build_argument_parser()` |
| `compute_curvature_stats` | method | `wilmore_rbc.py:527` | `def compute_curvature_stats(self, surface)` |
| `compute_vertex_areas` | method | `wilmore_rbc.py:217` | `def compute_vertex_areas(self, vertices, faces)` |
| `compute_willmore` | method | `wilmore_rbc.py:523` | `def compute_willmore(self, surface)` |
| `create_biconcave` | method | `wilmore_rbc.py:484` | `def create_biconcave(self, radius, dimple_depth)` |
| `create_evans_fung_rbc` | method | `wilmore_rbc.py:490` | `def create_evans_fung_rbc(self, radius, dimple_depth, thickness)` |
| `create_sphere` | method | `wilmore_rbc.py:481` | `def create_sphere(self, radius)` |
| `evolve` | method | `wilmore_rbc.py:579` | `def evolve(self, initial_surface)` |
| `forward` | method | `wilmore_rbc.py:68` | `def forward(self, x)` |
| `forward` | method | `wilmore_rbc.py:112` | `def forward(self, x)` |
| `load` | method | `wilmore_rbc.py:127` | `def load(checkpoint_path, device)` |
| `load` | method | `wilmore_rbc.py:176` | `def load(vert_path, face_path)` |
| `load_from_checkpoint` | method | `wilmore_rbc.py:148` | `def load_from_checkpoint(checkpoint_path, config)` |
| `main` | method | `wilmore_rbc.py:1046` | `def main()` |
| `project_mesh` | method | `wilmore_rbc.py:232` | `def project_mesh(self, vertices, faces, use_rbf)` |
| `project_mesh` | method | `wilmore_rbc.py:396` | `def project_mesh(self, vertices, faces)` |
| `run` | method | `wilmore_rbc.py:805` | `def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)` |
| `save_html_comparison` | method | `wilmore_rbc.py:636` | `def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolv` |
| `save_obj` | method | `wilmore_rbc.py:627` | `def save_obj(vertices, faces, filepath)` |
| `to_cartesian` | method | `wilmore_rbc.py:355` | `def to_cartesian(self, r_grid, scale)` |
| `to_cartesian` | method | `wilmore_rbc.py:445` | `def to_cartesian(self, rho_grid, z_scale, rho_scale)` |
