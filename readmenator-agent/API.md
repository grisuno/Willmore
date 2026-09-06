# API

## lol.py

### create_synthetic_rbc `def create_synthetic_rbc(n_vertices)`
- Defined: `lol.py:16`
- Doc: RBC sintético con forma bicóncava.

### spherical_projection `def spherical_projection(vertices, grid_size)`
- Defined: `lol.py:44`
- Doc: Proyección esférica - tiene problemas con dimples.

### cylindrical_projection `def cylindrical_projection(vertices, grid_size)`
- Defined: `lol.py:76`
- Doc: Proyección cilíndrica - NATURAL para RBC.

### spherical_to_cartesian `def spherical_to_cartesian(r_grid, grid_size)`
- Defined: `lol.py:123`
- Doc: Convierte grilla esférica a 3D.

### cylindrical_to_cartesian `def cylindrical_to_cartesian(rho_grid, z_min, z_max, grid_size)`
- Defined: `lol.py:144`
- Doc: Convierte grilla cilíndrica a 3D.

### compute_metrics `def compute_metrics(r_grid, mask, original_r)`
- Defined: `lol.py:164`
- Doc: Computa métricas de calidad.

### save_obj `def save_obj(vertices, faces, filepath)`
- Defined: `lol.py:181`

### main `def main()`
- Defined: `lol.py:189`

## model_Reco.py

### load_rbc_mesh `def load_rbc_mesh(vert_path, face_path)`
- Defined: `model_Reco.py:27`
- Depends on: `willmore_crsital2.py`

### center_mesh `def center_mesh(vertices)`
- Defined: `model_Reco.py:49`
- Depends on: `willmore_crsital2.py`

### cartesian_to_spherical `def cartesian_to_spherical(vertices)`
- Defined: `model_Reco.py:54`
- Depends on: `willmore_crsital2.py`

### spherical_to_cartesian `def spherical_to_cartesian(r, theta, phi)`
- Defined: `model_Reco.py:63`
- Depends on: `willmore_crsital2.py`

### evaluate_model_at_points `def evaluate_model_at_points(model, r_values, theta_values, phi_values, grid_size, device, r_global_mean)`
- Defined: `model_Reco.py:70`
- Doc: Evalúa el modelo en puntos arbitrarios (no en grilla regular).
- Depends on: `willmore_crsital2.py`

### load_model `def load_model(checkpoint_path, device, config)`
- Defined: `model_Reco.py:134`
- Depends on: `willmore_crsital2.py`

### compute_curvatures `def compute_curvatures(vertices, faces, grid_size)`
- Defined: `model_Reco.py:159`
- Doc: Compute curvatures using the same operator as training.
- Depends on: `willmore_crsital2.py`

### save_obj `def save_obj(vertices, faces, filepath)`
- Defined: `model_Reco.py:189`
- Depends on: `willmore_crsital2.py`

### save_html_viewer `def save_html_viewer(orig_verts, orig_faces, pred_verts, pred_faces, output_path)`
- Defined: `model_Reco.py:197`
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `model_Reco.py:338`
- Depends on: `willmore_crsital2.py`

## rbc.py

### load_rbc_mesh `def load_rbc_mesh(vert_path, face_path)`
- Defined: `rbc.py:30`
- Doc: Load RBC mesh from OpenRBC files.
- Depends on: `willmore_crsital2.py`

### load_model `def load_model(checkpoint_path, device, config)`
- Defined: `rbc.py:53`
- Doc: Load the trained Willmore model from checkpoint.
- Depends on: `willmore_crsital2.py`

### project_rbc_to_spherical_grid `def project_rbc_to_spherical_grid(vertices, grid_size)`
- Defined: `rbc.py:94`
- Doc: Project entire RBC mesh onto a spherical coordinate grid.
- Depends on: `willmore_crsital2.py`

### spherical_grid_to_cartesian `def spherical_grid_to_cartesian(r_grid, grid_size, scale)`
- Defined: `rbc.py:139`
- Doc: Convert spherical grid back to 3D vertices.
- Depends on: `willmore_crsital2.py`

### run_model_evolution `def run_model_evolution(model, input_grid, steps, device)`
- Defined: `rbc.py:164`
- Doc: Run model iteratively to evolve the surface.
- Depends on: `willmore_crsital2.py`

### create_sphere_grid `def create_sphere_grid(grid_size, radius)`
- Defined: `rbc.py:202`
- Doc: Create a perfect sphere grid for comparison.
- Depends on: `willmore_crsital2.py`

### create_biconcave_grid `def create_biconcave_grid(grid_size, radius)`
- Defined: `rbc.py:212`
- Doc: Create a biconcave disc shape on spherical grid.
- Depends on: `willmore_crsital2.py`

### compute_willmore_on_grid `def compute_willmore_on_grid(surface, grid_size)`
- Defined: `rbc.py:224`
- Doc: Compute Willmore energy using MinimalSurfaceOperator.
- Depends on: `willmore_crsital2.py`

### save_obj `def save_obj(vertices, faces, filepath)`
- Defined: `rbc.py:231`
- Doc: Save mesh as OBJ file.
- Depends on: `willmore_crsital2.py`

### save_html_comparison `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved_faces, sphere_vertices, sphere_faces, biconcave_vertices, biconcave_faces, willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave, output_path)`
- Defined: `rbc.py:240`
- Doc: Create interactive HTML comparing all shapes.
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `rbc.py:393`
- Depends on: `willmore_crsital2.py`

## rbc_model_reconstruction (1).py

### load_rbc_mesh `def load_rbc_mesh(vert_path, face_path)`
- Defined: `rbc_model_reconstruction (1).py:30`
- Doc: Load RBC mesh from OpenRBC files.
- Depends on: `willmore_crsital2.py`

### load_model `def load_model(checkpoint_path, device, config)`
- Defined: `rbc_model_reconstruction (1).py:53`
- Doc: Load the trained Willmore model from checkpoint.
- Depends on: `willmore_crsital2.py`

### project_rbc_to_spherical_grid `def project_rbc_to_spherical_grid(vertices, grid_size)`
- Defined: `rbc_model_reconstruction (1).py:94`
- Doc: Project entire RBC mesh onto a spherical coordinate grid.
- Depends on: `willmore_crsital2.py`

### spherical_grid_to_cartesian `def spherical_grid_to_cartesian(r_grid, grid_size, scale)`
- Defined: `rbc_model_reconstruction (1).py:139`
- Doc: Convert spherical grid back to 3D vertices.
- Depends on: `willmore_crsital2.py`

### run_model_evolution `def run_model_evolution(model, input_grid, steps, device)`
- Defined: `rbc_model_reconstruction (1).py:164`
- Doc: Run model iteratively to evolve the surface.
- Depends on: `willmore_crsital2.py`

### create_sphere_grid `def create_sphere_grid(grid_size, radius)`
- Defined: `rbc_model_reconstruction (1).py:202`
- Doc: Create a perfect sphere grid for comparison.
- Depends on: `willmore_crsital2.py`

### create_biconcave_grid `def create_biconcave_grid(grid_size, radius)`
- Defined: `rbc_model_reconstruction (1).py:212`
- Doc: Create a biconcave disc shape on spherical grid.
- Depends on: `willmore_crsital2.py`

### compute_willmore_on_grid `def compute_willmore_on_grid(surface, grid_size)`
- Defined: `rbc_model_reconstruction (1).py:224`
- Doc: Compute Willmore energy using MinimalSurfaceOperator.
- Depends on: `willmore_crsital2.py`

### save_obj `def save_obj(vertices, faces, filepath)`
- Defined: `rbc_model_reconstruction (1).py:231`
- Doc: Save mesh as OBJ file.
- Depends on: `willmore_crsital2.py`

### save_html_comparison `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved_faces, sphere_vertices, sphere_faces, biconcave_vertices, biconcave_faces, willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave, output_path)`
- Defined: `rbc_model_reconstruction (1).py:240`
- Doc: Create interactive HTML comparing all shapes.
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `rbc_model_reconstruction (1).py:393`
- Depends on: `willmore_crsital2.py`

## rbc_model_reconstruction.py

### load_rbc_mesh `def load_rbc_mesh(vert_path, face_path)`
- Defined: `rbc_model_reconstruction.py:31`
- Doc: Load RBC mesh from OpenRBC files.
- Depends on: `willmore_crsital2.py`

### compute_vertex_normals `def compute_vertex_normals(vertices, faces)`
- Defined: `rbc_model_reconstruction.py:54`
- Doc: Compute vertex normals.
- Depends on: `willmore_crsital2.py`

### compute_face_areas `def compute_face_areas(vertices, faces)`
- Defined: `rbc_model_reconstruction.py:75`
- Doc: Compute face areas.
- Depends on: `willmore_crsital2.py`

### load_model `def load_model(checkpoint_path, device, config)`
- Defined: `rbc_model_reconstruction.py:84`
- Doc: Load the trained Willmore model from checkpoint.
- Depends on: `willmore_crsital2.py`

### create_local_patches_for_vertices `def create_local_patches_for_vertices(vertices, faces, normals, grid_size)`
- Defined: `rbc_model_reconstruction.py:124`
- Doc: Create local surface patches around each vertex for model input.
- Depends on: `willmore_crsital2.py`

### run_model_on_patches `def run_model_on_patches(model, patches_real, patches_imag, device, grid_size, batch_size)`
- Defined: `rbc_model_reconstruction.py:215`
- Doc: Run the model on all vertex patches and extract predictions.
- Depends on: `willmore_crsital2.py`

### compute_analytical_curvature `def compute_analytical_curvature(vertices, faces)`
- Defined: `rbc_model_reconstruction.py:252`
- Doc: Compute analytical mean curvature for comparison.
- Depends on: `willmore_crsital2.py`

### save_ply_with_values `def save_ply_with_values(vertices, faces, normals, values, filepath, value_name)`
- Defined: `rbc_model_reconstruction.py:284`
- Doc: Save mesh as PLY with scalar values as vertex colors.
- Depends on: `willmore_crsital2.py`

### save_html_viewer `def save_html_viewer(vertices, faces, normals, model_curvature, analytical_curvature, output_path)`
- Defined: `rbc_model_reconstruction.py:319`
- Doc: Create interactive HTML viewer with model predictions on actual RBC mesh.
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `rbc_model_reconstruction.py:530`
- Depends on: `willmore_crsital2.py`

## rbc_model_reconstruction_128.py

### build_argument_parser `def build_argument_parser()`
- Defined: `rbc_model_reconstruction_128.py:926`
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `rbc_model_reconstruction_128.py:989`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, channels, grid_size)`
- Defined: `rbc_model_reconstruction_128.py:54`
- Depends on: `willmore_crsital2.py`

### forward `def forward(self, x)`
- Defined: `rbc_model_reconstruction_128.py:65`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- Defined: `rbc_model_reconstruction_128.py:88`
- Depends on: `willmore_crsital2.py`

### forward `def forward(self, x)`
- Defined: `rbc_model_reconstruction_128.py:109`
- Depends on: `willmore_crsital2.py`

### load `def load(checkpoint_path, device)`
- Defined: `rbc_model_reconstruction_128.py:124`
- Depends on: `willmore_crsital2.py`

### build `def build(config)`
- Defined: `rbc_model_reconstruction_128.py:134`
- Depends on: `willmore_crsital2.py`

### load_from_checkpoint `def load_from_checkpoint(checkpoint_path, config)`
- Defined: `rbc_model_reconstruction_128.py:145`
- Depends on: `willmore_crsital2.py`

### load `def load(vert_path, face_path)`
- Defined: `rbc_model_reconstruction_128.py:173`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size, smoothing_sigma)`
- Defined: `rbc_model_reconstruction_128.py:206`
- Depends on: `willmore_crsital2.py`

### compute_vertex_areas `def compute_vertex_areas(self, vertices, faces)`
- Defined: `rbc_model_reconstruction_128.py:214`
- Doc: Compute approximate area associated with each vertex.
- Depends on: `willmore_crsital2.py`

### project_mesh `def project_mesh(self, vertices, faces, use_rbf)`
- Defined: `rbc_model_reconstruction_128.py:229`
- Doc: Project mesh onto spherical grid with proper area weighting.
- Depends on: `willmore_crsital2.py`

### _area_weighted_projection `def _area_weighted_projection(self, theta, phi, r, areas)`
- Defined: `rbc_model_reconstruction_128.py:267`
- Doc: Project using area-weighted averaging.
- Depends on: `willmore_crsital2.py`

### _rbf_interpolation `def _rbf_interpolation(self, theta, phi, r)`
- Defined: `rbc_model_reconstruction_128.py:300`
- Doc: Use RBF interpolation for smooth reconstruction.
- Depends on: `willmore_crsital2.py`

### _apply_spherical_smoothing `def _apply_spherical_smoothing(self, r_grid)`
- Defined: `rbc_model_reconstruction_128.py:330`
- Doc: Apply Gaussian smoothing adapted to spherical coordinates.
- Depends on: `willmore_crsital2.py`

### to_cartesian `def to_cartesian(self, r_grid, scale)`
- Defined: `rbc_model_reconstruction_128.py:352`
- Doc: Convert spherical grid back to 3D vertices.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size, smoothing_sigma)`
- Defined: `rbc_model_reconstruction_128.py:385`
- Depends on: `willmore_crsital2.py`

### project_mesh `def project_mesh(self, vertices, faces)`
- Defined: `rbc_model_reconstruction_128.py:393`
- Doc: Project mesh using cylindrical coordinates.
- Depends on: `willmore_crsital2.py`

### to_cartesian `def to_cartesian(self, rho_grid, z_scale, rho_scale)`
- Defined: `rbc_model_reconstruction_128.py:442`
- Doc: Convert cylindrical grid back to 3D vertices.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size)`
- Defined: `rbc_model_reconstruction_128.py:472`
- Depends on: `willmore_crsital2.py`

### create_sphere `def create_sphere(self, radius)`
- Defined: `rbc_model_reconstruction_128.py:478`
- Depends on: `willmore_crsital2.py`

### create_biconcave `def create_biconcave(self, radius, dimple_depth)`
- Defined: `rbc_model_reconstruction_128.py:481`
- Doc: Create biconcave disc shape using Evans-Fung model.
- Depends on: `willmore_crsital2.py`

### create_evans_fung_rbc `def create_evans_fung_rbc(self, radius, dimple_depth, thickness)`
- Defined: `rbc_model_reconstruction_128.py:487`
- Doc: Create RBC shape using Evans-Fung parametrization.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size)`
- Defined: `rbc_model_reconstruction_128.py:517`
- Depends on: `willmore_crsital2.py`

### compute_willmore `def compute_willmore(self, surface)`
- Defined: `rbc_model_reconstruction_128.py:520`
- Depends on: `willmore_crsital2.py`

### compute_curvature_stats `def compute_curvature_stats(self, surface)`
- Defined: `rbc_model_reconstruction_128.py:524`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, model, config)`
- Defined: `rbc_model_reconstruction_128.py:545`
- Depends on: `willmore_crsital2.py`

### evolve `def evolve(self, initial_surface)`
- Defined: `rbc_model_reconstruction_128.py:553`
- Depends on: `willmore_crsital2.py`

### save_obj `def save_obj(vertices, faces, filepath)`
- Defined: `rbc_model_reconstruction_128.py:593`
- Depends on: `willmore_crsital2.py`

### save_html_comparison `def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolved_faces, biconcave_vertices, biconcave_faces, metrics, output_path)`
- Defined: `rbc_model_reconstruction_128.py:602`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `rbc_model_reconstruction_128.py:760`
- Depends on: `willmore_crsital2.py`

### run `def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)`
- Defined: `rbc_model_reconstruction_128.py:771`
- Depends on: `willmore_crsital2.py`

## rbc_willmore_analysis.py

### parse_arguments `def parse_arguments()`
- Defined: `rbc_willmore_analysis.py:1376`

### create_config_from_args `def create_config_from_args(args)`
- Defined: `rbc_willmore_analysis.py:1470`

### main `def main()`
- Defined: `rbc_willmore_analysis.py:1488`

### info `def info(self, message)`
- Defined: `rbc_willmore_analysis.py:106`

### warning `def warning(self, message)`
- Defined: `rbc_willmore_analysis.py:110`

### error `def error(self, message)`
- Defined: `rbc_willmore_analysis.py:114`

### debug `def debug(self, message)`
- Defined: `rbc_willmore_analysis.py:118`

### __init__ `def __init__(self, name, level)`
- Defined: `rbc_willmore_analysis.py:125`

### info `def info(self, message)`
- Defined: `rbc_willmore_analysis.py:136`

### warning `def warning(self, message)`
- Defined: `rbc_willmore_analysis.py:139`

### error `def error(self, message)`
- Defined: `rbc_willmore_analysis.py:142`

### debug `def debug(self, message)`
- Defined: `rbc_willmore_analysis.py:145`

### exists `def exists(self, path)`
- Defined: `rbc_willmore_analysis.py:153`

### read_text `def read_text(self, path)`
- Defined: `rbc_willmore_analysis.py:157`

### write_text `def write_text(self, path, content)`
- Defined: `rbc_willmore_analysis.py:161`

### makedirs `def makedirs(self, path)`
- Defined: `rbc_willmore_analysis.py:165`

### exists `def exists(self, path)`
- Defined: `rbc_willmore_analysis.py:172`

### read_text `def read_text(self, path)`
- Defined: `rbc_willmore_analysis.py:175`

### write_text `def write_text(self, path, content)`
- Defined: `rbc_willmore_analysis.py:179`

### makedirs `def makedirs(self, path)`
- Defined: `rbc_willmore_analysis.py:183`

### num_vertices `def num_vertices(self)`
- Defined: `rbc_willmore_analysis.py:206`

### num_faces `def num_faces(self)`
- Defined: `rbc_willmore_analysis.py:210`

### num_bonds `def num_bonds(self)`
- Defined: `rbc_willmore_analysis.py:214`

### to_dict `def to_dict(self)`
- Defined: `rbc_willmore_analysis.py:217`

### load `def load(self, vert_path, face_path, bond_path)`
- Defined: `rbc_willmore_analysis.py:232`

### __init__ `def __init__(self, filesystem, logger)`
- Defined: `rbc_willmore_analysis.py:245`

### load `def load(self, vert_path, face_path, bond_path)`
- Defined: `rbc_willmore_analysis.py:249`

### _load_vertices `def _load_vertices(self, path)`
- Defined: `rbc_willmore_analysis.py:267`

### _load_faces `def _load_faces(self, path)`
- Defined: `rbc_willmore_analysis.py:286`

### _load_bonds `def _load_bonds(self, path)`
- Defined: `rbc_willmore_analysis.py:308`

### _compute_normals `def _compute_normals(self, mesh)`
- Defined: `rbc_willmore_analysis.py:330`

### _compute_areas `def _compute_areas(self, mesh)`
- Defined: `rbc_willmore_analysis.py:355`

### __init__ `def __init__(self, logger)`
- Defined: `rbc_willmore_analysis.py:382`

### generate_sphere `def generate_sphere(self, radius, resolution)`
- Defined: `rbc_willmore_analysis.py:385`

### generate_torus `def generate_torus(self, R, r, resolution)`
- Defined: `rbc_willmore_analysis.py:424`

### generate_biconcave_disc `def generate_biconcave_disc(self, radius, thickness, resolution)`
- Defined: `rbc_willmore_analysis.py:467`

### _compute_mesh_properties `def _compute_mesh_properties(self, mesh)`
- Defined: `rbc_willmore_analysis.py:511`

### compute_mean_curvature `def compute_mean_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis.py:549`

### compute_gaussian_curvature `def compute_gaussian_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis.py:553`

### compute_willmore_energy `def compute_willmore_energy(self, mesh, mean_curvature)`
- Defined: `rbc_willmore_analysis.py:557`

### __init__ `def __init__(self, logger)`
- Defined: `rbc_willmore_analysis.py:578`

### compute_mean_curvature `def compute_mean_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis.py:581`

### compute_gaussian_curvature `def compute_gaussian_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis.py:616`

### compute_willmore_energy `def compute_willmore_energy(self, mesh, mean_curvature)`
- Defined: `rbc_willmore_analysis.py:664`

### _compute_edge_cotangents `def _compute_edge_cotangents(self, mesh)`
- Defined: `rbc_willmore_analysis.py:682`

### _get_vertex_neighbors `def _get_vertex_neighbors(self, vertex_idx, faces)`
- Defined: `rbc_willmore_analysis.py:737`

### _compute_mixed_voronoi_area `def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)`
- Defined: `rbc_willmore_analysis.py:748`

### __init__ `def __init__(self, channels, grid_size)`
- Defined: `rbc_willmore_analysis.py:806`

### forward `def forward(self, x)`
- Defined: `rbc_willmore_analysis.py:820`

### __init__ `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- Defined: `rbc_willmore_analysis.py:855`

### forward `def forward(self, x)`
- Defined: `rbc_willmore_analysis.py:880`

### load `def load(self, checkpoint_path, device, config)`
- Defined: `rbc_willmore_analysis.py:898`

### __init__ `def __init__(self, filesystem, logger)`
- Defined: `rbc_willmore_analysis.py:905`

### _detect_model_params `def _detect_model_params(self, state_dict)`
- Defined: `rbc_willmore_analysis.py:909`

### load `def load(self, checkpoint_path, device, config)`
- Defined: `rbc_willmore_analysis.py:947`

### __init__ `def __init__(self, config, logger, filesystem)`
- Defined: `rbc_willmore_analysis.py:1009`

### initialize `def initialize(self)`
- Defined: `rbc_willmore_analysis.py:1028`

### _load_rbc_mesh `def _load_rbc_mesh(self)`
- Defined: `rbc_willmore_analysis.py:1048`

### _generate_synthetic_meshes `def _generate_synthetic_meshes(self)`
- Defined: `rbc_willmore_analysis.py:1060`

### analyze_mesh `def analyze_mesh(self, mesh, name)`
- Defined: `rbc_willmore_analysis.py:1076`

### _compute_surface_area `def _compute_surface_area(self, mesh)`
- Defined: `rbc_willmore_analysis.py:1125`

### _compute_volume `def _compute_volume(self, mesh)`
- Defined: `rbc_willmore_analysis.py:1130`

### _compute_asphericity `def _compute_asphericity(self, mesh)`
- Defined: `rbc_willmore_analysis.py:1141`

### _compute_biconcavity_index `def _compute_biconcavity_index(self, mesh, mean_curvature)`
- Defined: `rbc_willmore_analysis.py:1161`

### _compute_histogram `def _compute_histogram(self, data, bins)`
- Defined: `rbc_willmore_analysis.py:1186`

### run_shape_emergence_test `def run_shape_emergence_test(self)`
- Defined: `rbc_willmore_analysis.py:1192`

### _analyze_rbc_morphology `def _analyze_rbc_morphology(self)`
- Defined: `rbc_willmore_analysis.py:1235`

### _verify_gauss_bonnet `def _verify_gauss_bonnet(self)`
- Defined: `rbc_willmore_analysis.py:1277`

### run_mean_curvature_flow `def run_mean_curvature_flow(self, mesh, steps, dt)`
- Defined: `rbc_willmore_analysis.py:1318`

### save_results `def save_results(self, results, filename)`
- Defined: `rbc_willmore_analysis.py:1357`

### save_mesh_obj `def save_mesh_obj(self, mesh, filename)`
- Defined: `rbc_willmore_analysis.py:1362`

## rbc_willmore_analysis2.py

### parse_arguments `def parse_arguments()`
- Defined: `rbc_willmore_analysis2.py:1394`

### create_config_from_args `def create_config_from_args(args)`
- Defined: `rbc_willmore_analysis2.py:1488`

### main `def main()`
- Defined: `rbc_willmore_analysis2.py:1506`

### info `def info(self, message)`
- Defined: `rbc_willmore_analysis2.py:106`

### warning `def warning(self, message)`
- Defined: `rbc_willmore_analysis2.py:110`

### error `def error(self, message)`
- Defined: `rbc_willmore_analysis2.py:114`

### debug `def debug(self, message)`
- Defined: `rbc_willmore_analysis2.py:118`

### __init__ `def __init__(self, name, level)`
- Defined: `rbc_willmore_analysis2.py:125`

### info `def info(self, message)`
- Defined: `rbc_willmore_analysis2.py:136`

### warning `def warning(self, message)`
- Defined: `rbc_willmore_analysis2.py:139`

### error `def error(self, message)`
- Defined: `rbc_willmore_analysis2.py:142`

### debug `def debug(self, message)`
- Defined: `rbc_willmore_analysis2.py:145`

### exists `def exists(self, path)`
- Defined: `rbc_willmore_analysis2.py:153`

### read_text `def read_text(self, path)`
- Defined: `rbc_willmore_analysis2.py:157`

### write_text `def write_text(self, path, content)`
- Defined: `rbc_willmore_analysis2.py:161`

### makedirs `def makedirs(self, path)`
- Defined: `rbc_willmore_analysis2.py:165`

### exists `def exists(self, path)`
- Defined: `rbc_willmore_analysis2.py:172`

### read_text `def read_text(self, path)`
- Defined: `rbc_willmore_analysis2.py:175`

### write_text `def write_text(self, path, content)`
- Defined: `rbc_willmore_analysis2.py:179`

### makedirs `def makedirs(self, path)`
- Defined: `rbc_willmore_analysis2.py:183`

### num_vertices `def num_vertices(self)`
- Defined: `rbc_willmore_analysis2.py:206`

### num_faces `def num_faces(self)`
- Defined: `rbc_willmore_analysis2.py:210`

### num_bonds `def num_bonds(self)`
- Defined: `rbc_willmore_analysis2.py:214`

### to_dict `def to_dict(self)`
- Defined: `rbc_willmore_analysis2.py:217`

### load `def load(self, vert_path, face_path, bond_path)`
- Defined: `rbc_willmore_analysis2.py:232`

### __init__ `def __init__(self, filesystem, logger)`
- Defined: `rbc_willmore_analysis2.py:245`

### load `def load(self, vert_path, face_path, bond_path)`
- Defined: `rbc_willmore_analysis2.py:249`

### _load_vertices `def _load_vertices(self, path)`
- Defined: `rbc_willmore_analysis2.py:267`

### _load_faces `def _load_faces(self, path)`
- Defined: `rbc_willmore_analysis2.py:286`

### _load_bonds `def _load_bonds(self, path)`
- Defined: `rbc_willmore_analysis2.py:308`

### _compute_normals `def _compute_normals(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:330`

### _compute_areas `def _compute_areas(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:355`

### __init__ `def __init__(self, logger)`
- Defined: `rbc_willmore_analysis2.py:382`

### generate_sphere `def generate_sphere(self, radius, resolution)`
- Defined: `rbc_willmore_analysis2.py:385`

### generate_torus `def generate_torus(self, R, r, resolution)`
- Defined: `rbc_willmore_analysis2.py:424`

### generate_biconcave_disc `def generate_biconcave_disc(self, radius, thickness, resolution)`
- Defined: `rbc_willmore_analysis2.py:467`

### _compute_mesh_properties `def _compute_mesh_properties(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:511`

### compute_mean_curvature `def compute_mean_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:549`

### compute_gaussian_curvature `def compute_gaussian_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:553`

### compute_willmore_energy `def compute_willmore_energy(self, mesh, mean_curvature)`
- Defined: `rbc_willmore_analysis2.py:557`

### __init__ `def __init__(self, logger)`
- Defined: `rbc_willmore_analysis2.py:578`

### compute_mean_curvature `def compute_mean_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:581`

### compute_gaussian_curvature `def compute_gaussian_curvature(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:616`

### compute_willmore_energy `def compute_willmore_energy(self, mesh, mean_curvature)`
- Defined: `rbc_willmore_analysis2.py:664`

### _compute_edge_cotangents `def _compute_edge_cotangents(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:682`

### _get_vertex_neighbors `def _get_vertex_neighbors(self, vertex_idx, faces)`
- Defined: `rbc_willmore_analysis2.py:737`

### _compute_mixed_voronoi_area `def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)`
- Defined: `rbc_willmore_analysis2.py:748`

### __init__ `def __init__(self, channels, grid_size)`
- Defined: `rbc_willmore_analysis2.py:806`

### forward `def forward(self, x)`
- Defined: `rbc_willmore_analysis2.py:820`

### __init__ `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- Defined: `rbc_willmore_analysis2.py:855`

### forward `def forward(self, x)`
- Defined: `rbc_willmore_analysis2.py:880`

### load `def load(self, checkpoint_path, device, config)`
- Defined: `rbc_willmore_analysis2.py:898`

### __init__ `def __init__(self, filesystem, logger)`
- Defined: `rbc_willmore_analysis2.py:905`

### _detect_model_params `def _detect_model_params(self, state_dict)`
- Defined: `rbc_willmore_analysis2.py:909`

### load `def load(self, checkpoint_path, device, config)`
- Defined: `rbc_willmore_analysis2.py:947`

### __init__ `def __init__(self, config, logger, filesystem)`
- Defined: `rbc_willmore_analysis2.py:1009`

### initialize `def initialize(self)`
- Defined: `rbc_willmore_analysis2.py:1028`

### _load_rbc_mesh `def _load_rbc_mesh(self)`
- Defined: `rbc_willmore_analysis2.py:1048`

### _generate_synthetic_meshes `def _generate_synthetic_meshes(self)`
- Defined: `rbc_willmore_analysis2.py:1060`

### analyze_mesh `def analyze_mesh(self, mesh, name)`
- Defined: `rbc_willmore_analysis2.py:1076`

### _compute_surface_area `def _compute_surface_area(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:1125`

### _compute_volume `def _compute_volume(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:1130`

### _compute_asphericity `def _compute_asphericity(self, mesh)`
- Defined: `rbc_willmore_analysis2.py:1141`

### _compute_biconcavity_index `def _compute_biconcavity_index(self, mesh, mean_curvature)`
- Defined: `rbc_willmore_analysis2.py:1161`

### _compute_histogram `def _compute_histogram(self, data, bins)`
- Defined: `rbc_willmore_analysis2.py:1186`

### run_shape_emergence_test `def run_shape_emergence_test(self)`
- Defined: `rbc_willmore_analysis2.py:1192`

### _analyze_rbc_morphology `def _analyze_rbc_morphology(self)`
- Defined: `rbc_willmore_analysis2.py:1235`

### _verify_gauss_bonnet `def _verify_gauss_bonnet(self)`
- Defined: `rbc_willmore_analysis2.py:1277`

### run_mean_curvature_flow `def run_mean_curvature_flow(self, mesh, steps, dt)`
- Defined: `rbc_willmore_analysis2.py:1318`

### save_results `def save_results(self, results, filename)`
- Defined: `rbc_willmore_analysis2.py:1357`

### save_mesh_obj `def save_mesh_obj(self, mesh, filename)`
- Defined: `rbc_willmore_analysis2.py:1380`

### convert_to_native `def convert_to_native(obj)`
- Defined: `rbc_willmore_analysis2.py:1360`

## test.py

### load_model `def load_model(checkpoint_path, device)`
- Defined: `test.py:20`
- Depends on: `willmore_crsital2.py`

### test_model_behavior `def test_model_behavior(model, config, device)`
- Defined: `test.py:45`
- Doc: Test que respeta la escala pequeña del modelo.
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `test.py:154`
- Depends on: `willmore_crsital2.py`

## willmore_crsital2.py

### build_argument_parser `def build_argument_parser()`
- Defined: `willmore_crsital2.py:1839`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### main `def main()`
- Defined: `willmore_crsital2.py:1868`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### detect `def detect(self, spectral_field)`
- Defined: `willmore_crsital2.py:203`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:209`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### set_seed `def set_seed(seed, device)`
- Defined: `willmore_crsital2.py:215`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### create_logger `def create_logger(name, level)`
- Defined: `willmore_crsital2.py:229`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, grid_size)`
- Defined: `willmore_crsital2.py:243`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _precompute_spectral_operators `def _precompute_spectral_operators(self)`
- Defined: `willmore_crsital2.py:249`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### apply_laplacian `def apply_laplacian(self, field)`
- Defined: `willmore_crsital2.py:257`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_mean_curvature `def compute_mean_curvature(self, surface)`
- Defined: `willmore_crsital2.py:262`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_gaussian_curvature `def compute_gaussian_curvature(self, surface)`
- Defined: `willmore_crsital2.py:273`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_willmore_energy `def compute_willmore_energy(self, surface)`
- Defined: `willmore_crsital2.py:284`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_surface_area `def compute_surface_area(self, surface)`
- Defined: `willmore_crsital2.py:290`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### mean_curvature_flow `def mean_curvature_flow(self, surface, dt)`
- Defined: `willmore_crsital2.py:297`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, channels, grid_size)`
- Defined: `willmore_crsital2.py:308`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### forward `def forward(self, x)`
- Defined: `willmore_crsital2.py:315`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, grid_size, hidden_dim, num_spectral_layers)`
- Defined: `willmore_crsital2.py:332`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### forward `def forward(self, x)`
- Defined: `willmore_crsital2.py:342`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:352`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _try_load_backbone `def _try_load_backbone(self)`
- Defined: `willmore_crsital2.py:359`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### apply_mean_curvature `def apply_mean_curvature(self, surface)`
- Defined: `willmore_crsital2.py:382`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### mean_curvature_evolve `def mean_curvature_evolve(self, surface, dt)`
- Defined: `willmore_crsital2.py:388`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:400`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### pyramid_potential `def pyramid_potential(self)`
- Defined: `willmore_crsital2.py:404`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### cube_potential `def cube_potential(self)`
- Defined: `willmore_crsital2.py:411`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### dodecahedron_potential `def dodecahedron_potential(self)`
- Defined: `willmore_crsital2.py:418`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### torus_potential `def torus_potential(self)`
- Defined: `willmore_crsital2.py:426`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### hyperbolic_potential `def hyperbolic_potential(self)`
- Defined: `willmore_crsital2.py:434`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### generate_mixed_potential `def generate_mixed_potential(self, seed)`
- Defined: `willmore_crsital2.py:442`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, surface_engine, seed)`
- Defined: `willmore_crsital2.py:453`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _solve_minimal_surface `def _solve_minimal_surface(self, potential, sample_seed)`
- Defined: `willmore_crsital2.py:487`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _evolve_minimal_surface `def _evolve_minimal_surface(self, surface_real, surface_imag, potential, energy)`
- Defined: `willmore_crsital2.py:513`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __len__ `def __len__(self)`
- Defined: `willmore_crsital2.py:534`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `willmore_crsital2.py:535`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### get_validation_batch `def get_validation_batch(self)`
- Defined: `willmore_crsital2.py:536`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- Defined: `willmore_crsital2.py:540`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### forward `def forward(self, x)`
- Defined: `willmore_crsital2.py:557`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:568`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:573`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_surface_metrics `def compute_surface_metrics(self, surface)`
- Defined: `willmore_crsital2.py:590`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _empty_metrics `def _empty_metrics()`
- Defined: `willmore_crsital2.py:618`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:623`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:627`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _compute_ricci_scalar `def _compute_ricci_scalar(self, metric)`
- Defined: `willmore_crsital2.py:640`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _estimate_sectional_curvatures `def _estimate_sectional_curvatures(self, metric)`
- Defined: `willmore_crsital2.py:647`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _compute_flow_velocity `def _compute_flow_velocity(self, metric)`
- Defined: `willmore_crsital2.py:659`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _empty_metrics `def _empty_metrics()`
- Defined: `willmore_crsital2.py:664`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:669`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_full_spectrum `def compute_full_spectrum(self, spectral_field)`
- Defined: `willmore_crsital2.py:677`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_resonance_metrics `def compute_resonance_metrics(self, spectral_field)`
- Defined: `willmore_crsital2.py:701`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:712`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _get_freq_grids `def _get_freq_grids(self, H, W, device)`
- Defined: `willmore_crsital2.py:720`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_mass_center `def compute_mass_center(self, spectral_field)`
- Defined: `willmore_crsital2.py:728`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:752`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### detect `def detect(self, spectral_field)`
- Defined: `willmore_crsital2.py:759`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### extract `def extract(model, grid_size)`
- Defined: `willmore_crsital2.py:782`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:799`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:804`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _empty_metrics `def _empty_metrics()`
- Defined: `willmore_crsital2.py:814`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_local_complexity `def compute_local_complexity(weights, epsilon)`
- Defined: `willmore_crsital2.py:820`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_superposition `def compute_superposition(weights)`
- Defined: `willmore_crsital2.py:835`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:852`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:856`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_kappa `def compute_kappa(self, model, val_x, val_y, num_batches)`
- Defined: `willmore_crsital2.py:861`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_discretization_margin `def compute_discretization_margin(self, model)`
- Defined: `willmore_crsital2.py:903`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_alpha_purity `def compute_alpha_purity(self, model)`
- Defined: `willmore_crsital2.py:911`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_kappa_quantum `def compute_kappa_quantum(self, model)`
- Defined: `willmore_crsital2.py:916`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_poynting_vector `def compute_poynting_vector(self, model)`
- Defined: `willmore_crsital2.py:935`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_hbar_effective `def compute_hbar_effective(self, model, lambda_pressure)`
- Defined: `willmore_crsital2.py:946`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_all_metrics `def compute_all_metrics(self, model, val_x, val_y)`
- Defined: `willmore_crsital2.py:953`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:966`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:969`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_effective_temperature `def compute_effective_temperature(self, gradient_buffer, learning_rate)`
- Defined: `willmore_crsital2.py:983`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_specific_heat `def compute_specific_heat(self, loss_history, temp_history)`
- Defined: `willmore_crsital2.py:1001`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_gibbs_free_energy `def compute_gibbs_free_energy(self, delta, alpha, temperature)`
- Defined: `willmore_crsital2.py:1010`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_critical_temperature `def compute_critical_temperature(self, alpha)`
- Defined: `willmore_crsital2.py:1017`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1022`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:1025`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1045`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:1048`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1066`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute `def compute(self, model)`
- Defined: `willmore_crsital2.py:1069`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1083`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### current_lambda `def current_lambda(self)`
- Defined: `willmore_crsital2.py:1092`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### step `def step(self, epoch)`
- Defined: `willmore_crsital2.py:1095`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_regularization_loss `def compute_regularization_loss(self, model)`
- Defined: `willmore_crsital2.py:1102`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### set_lambda `def set_lambda(self, value)`
- Defined: `willmore_crsital2.py:1110`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1115`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### step_adaptive `def step_adaptive(self, epoch, topo_phase_state)`
- Defined: `willmore_crsital2.py:1120`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1130`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### current_lambda `def current_lambda(self)`
- Defined: `willmore_crsital2.py:1139`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### step `def step(self, epoch, improvement)`
- Defined: `willmore_crsital2.py:1142`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_regularization_loss `def compute_regularization_loss(self, model)`
- Defined: `willmore_crsital2.py:1149`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### set_lambda `def set_lambda(self, value)`
- Defined: `willmore_crsital2.py:1157`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1162`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### temperature `def temperature(self)`
- Defined: `willmore_crsital2.py:1170`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### step `def step(self)`
- Defined: `willmore_crsital2.py:1173`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### accept_perturbation `def accept_perturbation(self, delta_loss)`
- Defined: `willmore_crsital2.py:1176`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### should_restart `def should_restart(self, current_delta, best_delta)`
- Defined: `willmore_crsital2.py:1182`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1187`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### step_adaptive `def step_adaptive(self, alignment_trend, resonance_score)`
- Defined: `willmore_crsital2.py:1191`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1203`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### update_metrics `def update_metrics(self)`
- Defined: `willmore_crsital2.py:1210`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_delta_slope `def compute_delta_slope(self)`
- Defined: `willmore_crsital2.py:1219`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### format_progress_bar `def format_progress_bar(self, epoch, total_epochs, phase)`
- Defined: `willmore_crsital2.py:1229`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, checkpoint_dir)`
- Defined: `willmore_crsital2.py:1262`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### should_save_checkpoint `def should_save_checkpoint(self)`
- Defined: `willmore_crsital2.py:1271`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### save_checkpoint `def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)`
- Defined: `willmore_crsital2.py:1276`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1292`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### should_save `def should_save(self, current_delta, current_alpha, current_acc)`
- Defined: `willmore_crsital2.py:1302`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### save_checkpoint `def save_checkpoint(self, model, optimizer, epoch, metrics, lambda_value)`
- Defined: `willmore_crsital2.py:1307`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### check `def check(model)`
- Defined: `willmore_crsital2.py:1324`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1339`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_weight_metrics `def compute_weight_metrics(self, model)`
- Defined: `willmore_crsital2.py:1354`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### compute_norm_conservation_error `def compute_norm_conservation_error(self, model, val_x)`
- Defined: `willmore_crsital2.py:1364`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### train_single_epoch `def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler)`
- Defined: `willmore_crsital2.py:1373`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### validate `def validate(self, model, val_x, val_y)`
- Defined: `willmore_crsital2.py:1398`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### collect_all_metrics `def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)`
- Defined: `willmore_crsital2.py:1408`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, surface_engine)`
- Defined: `willmore_crsital2.py:1448`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### prospect `def prospect(self)`
- Defined: `willmore_crsital2.py:1453`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, surface_engine, batch_size)`
- Defined: `willmore_crsital2.py:1484`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### mine `def mine(self)`
- Defined: `willmore_crsital2.py:1490`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, surface_engine, seed, batch_size)`
- Defined: `willmore_crsital2.py:1534`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### run_phase3_training `def run_phase3_training(self)`
- Defined: `willmore_crsital2.py:1541`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, surface_engine, model, optimizer, monitor, seed, batch_size)`
- Defined: `willmore_crsital2.py:1600`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### run_phase4_refinement `def run_phase4_refinement(self)`
- Defined: `willmore_crsital2.py:1610`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config, surface_engine, model, monitor, seed, batch_size)`
- Defined: `willmore_crsital2.py:1664`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### run_phase5_crystallization `def run_phase5_crystallization(self)`
- Defined: `willmore_crsital2.py:1674`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crsital2.py:1726`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### run `def run(self)`
- Defined: `willmore_crsital2.py:1730`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### _save_final_results `def _save_final_results(self, model, monitor, seed, batch_size)`
- Defined: `willmore_crsital2.py:1789`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

### safe_get `def safe_get(key)`
- Defined: `willmore_crsital2.py:1231`
- Imported by: `model_Reco.py`, `rbc.py`, `rbc_model_reconstruction (1).py`, `rbc_model_reconstruction.py`, `rbc_model_reconstruction_128.py`, `test.py`, `willmore_zero_shot_scaler.py`, `wilmore_rbc.py`

## willmore_crystallography_suite.py.py

### setup_logging `def setup_logging(log_level)`
- Defined: `willmore_crystallography_suite.py.py:1444`
- Doc: Configure logging for the suite.

### main `def main()`
- Defined: `willmore_crystallography_suite.py.py:1452`

### __init__ `def __init__(self, channels, grid_size)`
- Defined: `willmore_crystallography_suite.py.py:95`

### forward `def forward(self, x)`
- Defined: `willmore_crystallography_suite.py.py:112`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:141`

### forward `def forward(self, x)`
- Defined: `willmore_crystallography_suite.py.py:160`

### get_spectral_representation `def get_spectral_representation(self, x)`
- Defined: `willmore_crystallography_suite.py.py:171`
- Doc: Extract spectral features for analysis.

### __init__ `def __init__(self, grid_size)`
- Defined: `willmore_crystallography_suite.py.py:184`

### _precompute_spectral_operators `def _precompute_spectral_operators(self)`
- Defined: `willmore_crystallography_suite.py.py:188`

### apply_laplacian `def apply_laplacian(self, field)`
- Defined: `willmore_crystallography_suite.py.py:196`

### compute_mean_curvature `def compute_mean_curvature(self, surface)`
- Defined: `willmore_crystallography_suite.py.py:201`

### compute_gaussian_curvature `def compute_gaussian_curvature(self, surface)`
- Defined: `willmore_crystallography_suite.py.py:212`

### compute_willmore_energy `def compute_willmore_energy(self, surface)`
- Defined: `willmore_crystallography_suite.py.py:223`

### compute_surface_area `def compute_surface_area(self, surface)`
- Defined: `willmore_crystallography_suite.py.py:229`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:240`

### pyramid_potential `def pyramid_potential(self)`
- Defined: `willmore_crystallography_suite.py.py:244`

### cube_potential `def cube_potential(self)`
- Defined: `willmore_crystallography_suite.py.py:251`

### dodecahedron_potential `def dodecahedron_potential(self)`
- Defined: `willmore_crystallography_suite.py.py:258`

### torus_potential `def torus_potential(self)`
- Defined: `willmore_crystallography_suite.py.py:266`

### hyperbolic_potential `def hyperbolic_potential(self)`
- Defined: `willmore_crystallography_suite.py.py:274`

### generate_mixed_potential `def generate_mixed_potential(self, seed)`
- Defined: `willmore_crystallography_suite.py.py:282`

### __init__ `def __init__(self, config, seed, num_samples)`
- Defined: `willmore_crystallography_suite.py.py:301`

### _generate_surface_pair `def _generate_surface_pair(self, potential, sample_seed)`
- Defined: `willmore_crystallography_suite.py.py:331`

### __len__ `def __len__(self)`
- Defined: `willmore_crystallography_suite.py.py:364`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `willmore_crystallography_suite.py.py:367`

### get_validation_batch `def get_validation_batch(self)`
- Defined: `willmore_crystallography_suite.py.py:370`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:377`

### compute `def compute(self, model)`
- Defined: `willmore_crystallography_suite.py.py:380`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:413`

### compute `def compute(self, model)`
- Defined: `willmore_crystallography_suite.py.py:416`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:443`

### compute `def compute(self, model)`
- Defined: `willmore_crystallography_suite.py.py:446`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:503`

### compute `def compute(self, model)`
- Defined: `willmore_crystallography_suite.py.py:506`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:550`

### compute `def compute(self, model)`
- Defined: `willmore_crystallography_suite.py.py:554`

### _compute_surface_metrics `def _compute_surface_metrics(self, surface)`
- Defined: `willmore_crystallography_suite.py.py:575`

### _empty_metrics `def _empty_metrics()`
- Defined: `willmore_crystallography_suite.py.py:605`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:622`

### detect `def detect(self, spectral_field)`
- Defined: `willmore_crystallography_suite.py.py:628`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:712`

### load_checkpoints `def load_checkpoints(self, checkpoint_dir)`
- Defined: `willmore_crystallography_suite.py.py:715`

### _extract_epoch `def _extract_epoch(self, filepath)`
- Defined: `willmore_crystallography_suite.py.py:734`

### flatten_spectral_kernels `def flatten_spectral_kernels(self, state_dict)`
- Defined: `willmore_crystallography_suite.py.py:738`

### calculate_berry_phase `def calculate_berry_phase(self, checkpoint_dir)`
- Defined: `willmore_crystallography_suite.py.py:751`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:790`

### run `def run(self, model, dataset)`
- Defined: `willmore_crystallography_suite.py.py:795`

### run `def run(self, model, dataset)`
- Defined: `willmore_crystallography_suite.py.py:802`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:826`

### run `def run(self, model, dataset)`
- Defined: `willmore_crystallography_suite.py.py:830`

### run `def run(self, model, dataset)`
- Defined: `willmore_crystallography_suite.py.py:869`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:903`

### analyze_checkpoint `def analyze_checkpoint(self, checkpoint_path, dataset)`
- Defined: `willmore_crystallography_suite.py.py:918`

### _extract_spectral_field `def _extract_spectral_field(self, model)`
- Defined: `willmore_crystallography_suite.py.py:997`

### _compute_health_score `def _compute_health_score(self, results)`
- Defined: `willmore_crystallography_suite.py.py:1012`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:1038`

### visualize_analysis `def visualize_analysis(self, results, output_path)`
- Defined: `willmore_crystallography_suite.py.py:1041`

### _plot_weight_integrity `def _plot_weight_integrity(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1067`

### _plot_discretization `def _plot_discretization(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1085`

### _plot_spectral_geometry `def _plot_spectral_geometry(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1111`

### _plot_ricci_curvature `def _plot_ricci_curvature(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1132`

### _plot_functional_test_1 `def _plot_functional_test_1(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1145`

### _plot_functional_test_2 `def _plot_functional_test_2(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1165`

### _plot_functional_test_3 `def _plot_functional_test_3(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1188`

### _plot_health_summary `def _plot_health_summary(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1210`

### _plot_layer_deltas `def _plot_layer_deltas(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1240`

### _plot_phase_diagram `def _plot_phase_diagram(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1259`

### _plot_crystal_verdict `def _plot_crystal_verdict(self, results, ax)`
- Defined: `willmore_crystallography_suite.py.py:1279`

### __init__ `def __init__(self, config)`
- Defined: `willmore_crystallography_suite.py.py:1324`

### process_directory `def process_directory(self, checkpoint_dir, output_dir, dataset)`
- Defined: `willmore_crystallography_suite.py.py:1331`

### _rank_checkpoints `def _rank_checkpoints(self, all_results)`
- Defined: `willmore_crystallography_suite.py.py:1381`

### _generate_summary `def _generate_summary(self, ranked, output_dir)`
- Defined: `willmore_crystallography_suite.py.py:1407`

## willmore_zero_shot_scaler.py

### create_default_config_file `def create_default_config_file(path)`
- Defined: `willmore_zero_shot_scaler.py:1046`
- Doc: Create a default configuration file.
- Depends on: `willmore_crsital2.py`

### build_argument_parser `def build_argument_parser()`
- Defined: `willmore_zero_shot_scaler.py:1053`
- Doc: Build the command-line argument parser.
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `willmore_zero_shot_scaler.py:1129`
- Doc: Main entry point for the zero-shot scaler.
- Depends on: `willmore_crsital2.py`

### load `def load(self, source)`
- Defined: `willmore_zero_shot_scaler.py:148`
- Doc: Load configuration from the specified source.
- Depends on: `willmore_crsital2.py`

### load `def load(self, source)`
- Defined: `willmore_zero_shot_scaler.py:156`
- Depends on: `willmore_crsital2.py`

### _from_toml `def _from_toml(self, path)`
- Defined: `willmore_zero_shot_scaler.py:161`
- Depends on: `willmore_crsital2.py`

### _from_dict `def _from_dict(self, data)`
- Defined: `willmore_zero_shot_scaler.py:170`
- Depends on: `willmore_crsital2.py`

### load_checkpoint `def load_checkpoint(self, path, device)`
- Defined: `willmore_zero_shot_scaler.py:211`
- Doc: Load a model checkpoint from disk.
- Depends on: `willmore_crsital2.py`

### save_checkpoint `def save_checkpoint(self, model, metrics, path)`
- Defined: `willmore_zero_shot_scaler.py:216`
- Doc: Save a model checkpoint to disk.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_zero_shot_scaler.py:224`
- Depends on: `willmore_crsital2.py`

### load_checkpoint `def load_checkpoint(self, path, device)`
- Defined: `willmore_zero_shot_scaler.py:228`
- Depends on: `willmore_crsital2.py`

### save_checkpoint `def save_checkpoint(self, model, metrics, path)`
- Defined: `willmore_zero_shot_scaler.py:246`
- Depends on: `willmore_crsital2.py`

### interpolate `def interpolate(self, source_weight, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:264`
- Doc: Interpolate spectral weights to a new shape.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_zero_shot_scaler.py:277`
- Depends on: `willmore_crsital2.py`

### interpolate `def interpolate(self, source_weight, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:281`
- Depends on: `willmore_crsital2.py`

### _interpolate_2d_spectral `def _interpolate_2d_spectral(self, source, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:294`
- Depends on: `willmore_crsital2.py`

### _interpolate_4d_spectral `def _interpolate_4d_spectral(self, source, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:314`
- Depends on: `willmore_crsital2.py`

### _pad_spectrum_2d `def _pad_spectrum_2d(self, spectrum, target_h, target_w)`
- Defined: `willmore_zero_shot_scaler.py:332`
- Depends on: `willmore_crsital2.py`

### _interpolate_generic `def _interpolate_generic(self, source, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:369`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_zero_shot_scaler.py:390`
- Depends on: `willmore_crsital2.py`

### interpolate `def interpolate(self, source_weight, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:394`
- Depends on: `willmore_crsital2.py`

### _interpolate_generic `def _interpolate_generic(self, source, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:419`
- Depends on: `willmore_crsital2.py`

### scale_model `def scale_model(self, source_model, target_grid_size)`
- Defined: `willmore_zero_shot_scaler.py:449`
- Doc: Scale a model to a new grid resolution.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config, interpolator)`
- Defined: `willmore_zero_shot_scaler.py:461`
- Depends on: `willmore_crsital2.py`

### scale_model `def scale_model(self, source_model, target_grid_size)`
- Defined: `willmore_zero_shot_scaler.py:470`
- Depends on: `willmore_crsital2.py`

### _extract_hidden_dim `def _extract_hidden_dim(self, model)`
- Defined: `willmore_zero_shot_scaler.py:495`
- Depends on: `willmore_crsital2.py`

### _extract_expansion_dim `def _extract_expansion_dim(self, model)`
- Defined: `willmore_zero_shot_scaler.py:500`
- Depends on: `willmore_crsital2.py`

### _count_spectral_layers `def _count_spectral_layers(self, model)`
- Defined: `willmore_zero_shot_scaler.py:505`
- Depends on: `willmore_crsital2.py`

### _transfer_weights `def _transfer_weights(self, source, target, source_grid, target_grid)`
- Defined: `willmore_zero_shot_scaler.py:510`
- Depends on: `willmore_crsital2.py`

### _scale_spectral_kernel `def _scale_spectral_kernel(self, kernel, target_shape, source_grid, target_grid)`
- Defined: `willmore_zero_shot_scaler.py:535`
- Depends on: `willmore_crsital2.py`

### _scale_conv_weight `def _scale_conv_weight(self, weight, target_shape)`
- Defined: `willmore_zero_shot_scaler.py:549`
- Depends on: `willmore_crsital2.py`

### _validate_weight_transfer `def _validate_weight_transfer(self, source, target)`
- Defined: `willmore_zero_shot_scaler.py:570`
- Depends on: `willmore_crsital2.py`

### evaluate `def evaluate(self, model, grid_size, num_samples)`
- Defined: `willmore_zero_shot_scaler.py:587`
- Doc: Evaluate model performance and metrics.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_zero_shot_scaler.py:600`
- Depends on: `willmore_crsital2.py`

### evaluate `def evaluate(self, model, grid_size, num_samples)`
- Defined: `willmore_zero_shot_scaler.py:606`
- Depends on: `willmore_crsital2.py`

### _construct_weight_surface `def _construct_weight_surface(self, model, grid_size)`
- Defined: `willmore_zero_shot_scaler.py:639`
- Depends on: `willmore_crsital2.py`

### _compute_willmore_metrics `def _compute_willmore_metrics(self, surface)`
- Defined: `willmore_zero_shot_scaler.py:661`
- Depends on: `willmore_crsital2.py`

### _compute_curvature_metrics `def _compute_curvature_metrics(self, surface)`
- Defined: `willmore_zero_shot_scaler.py:677`
- Depends on: `willmore_crsital2.py`

### _compute_spectral_metrics `def _compute_spectral_metrics(self, model)`
- Defined: `willmore_zero_shot_scaler.py:702`
- Depends on: `willmore_crsital2.py`

### _evaluate_inference_quality `def _evaluate_inference_quality(self, model, grid_size, num_samples)`
- Defined: `willmore_zero_shot_scaler.py:735`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `willmore_zero_shot_scaler.py:779`
- Depends on: `willmore_crsital2.py`

### execute `def execute(self)`
- Defined: `willmore_zero_shot_scaler.py:796`
- Depends on: `willmore_crsital2.py`

### _load_source_model `def _load_source_model(self)`
- Defined: `willmore_zero_shot_scaler.py:888`
- Depends on: `willmore_crsital2.py`

### _log_metrics `def _log_metrics(self, metrics, grid_size)`
- Defined: `willmore_zero_shot_scaler.py:914`
- Depends on: `willmore_crsital2.py`

### _check_degradation `def _check_degradation(self, source_metrics, current_metrics)`
- Defined: `willmore_zero_shot_scaler.py:930`
- Depends on: `willmore_crsital2.py`

### _is_better_metrics `def _is_better_metrics(self, current, best)`
- Defined: `willmore_zero_shot_scaler.py:946`
- Depends on: `willmore_crsital2.py`

### _save_scaled_model `def _save_scaled_model(self, model, metrics, grid_size)`
- Defined: `willmore_zero_shot_scaler.py:961`
- Depends on: `willmore_crsital2.py`

### _compile_final_results `def _compile_final_results(self)`
- Defined: `willmore_zero_shot_scaler.py:971`
- Depends on: `willmore_crsital2.py`

### _save_final_results `def _save_final_results(self, results)`
- Defined: `willmore_zero_shot_scaler.py:985`
- Depends on: `willmore_crsital2.py`

### _write_detailed_report `def _write_detailed_report(self, results, path)`
- Defined: `willmore_zero_shot_scaler.py:997`
- Depends on: `willmore_crsital2.py`

## wilmore_rbc.py

### build_argument_parser `def build_argument_parser()`
- Defined: `wilmore_rbc.py:960`
- Depends on: `willmore_crsital2.py`

### main `def main()`
- Defined: `wilmore_rbc.py:1046`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, channels, grid_size)`
- Defined: `wilmore_rbc.py:57`
- Depends on: `willmore_crsital2.py`

### forward `def forward(self, x)`
- Defined: `wilmore_rbc.py:68`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- Defined: `wilmore_rbc.py:91`
- Depends on: `willmore_crsital2.py`

### forward `def forward(self, x)`
- Defined: `wilmore_rbc.py:112`
- Depends on: `willmore_crsital2.py`

### load `def load(checkpoint_path, device)`
- Defined: `wilmore_rbc.py:127`
- Depends on: `willmore_crsital2.py`

### build `def build(config)`
- Defined: `wilmore_rbc.py:137`
- Depends on: `willmore_crsital2.py`

### load_from_checkpoint `def load_from_checkpoint(checkpoint_path, config)`
- Defined: `wilmore_rbc.py:148`
- Depends on: `willmore_crsital2.py`

### load `def load(vert_path, face_path)`
- Defined: `wilmore_rbc.py:176`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size, smoothing_sigma)`
- Defined: `wilmore_rbc.py:209`
- Depends on: `willmore_crsital2.py`

### compute_vertex_areas `def compute_vertex_areas(self, vertices, faces)`
- Defined: `wilmore_rbc.py:217`
- Doc: Compute approximate area associated with each vertex.
- Depends on: `willmore_crsital2.py`

### project_mesh `def project_mesh(self, vertices, faces, use_rbf)`
- Defined: `wilmore_rbc.py:232`
- Doc: Project mesh onto spherical grid with proper area weighting.
- Depends on: `willmore_crsital2.py`

### _area_weighted_projection `def _area_weighted_projection(self, theta, phi, r, areas)`
- Defined: `wilmore_rbc.py:270`
- Doc: Project using area-weighted averaging.
- Depends on: `willmore_crsital2.py`

### _rbf_interpolation `def _rbf_interpolation(self, theta, phi, r)`
- Defined: `wilmore_rbc.py:303`
- Doc: Use RBF interpolation for smooth reconstruction.
- Depends on: `willmore_crsital2.py`

### _apply_spherical_smoothing `def _apply_spherical_smoothing(self, r_grid)`
- Defined: `wilmore_rbc.py:333`
- Doc: Apply Gaussian smoothing adapted to spherical coordinates.
- Depends on: `willmore_crsital2.py`

### to_cartesian `def to_cartesian(self, r_grid, scale)`
- Defined: `wilmore_rbc.py:355`
- Doc: Convert spherical grid back to 3D vertices.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size, smoothing_sigma)`
- Defined: `wilmore_rbc.py:388`
- Depends on: `willmore_crsital2.py`

### project_mesh `def project_mesh(self, vertices, faces)`
- Defined: `wilmore_rbc.py:396`
- Doc: Project mesh using cylindrical coordinates.
- Depends on: `willmore_crsital2.py`

### to_cartesian `def to_cartesian(self, rho_grid, z_scale, rho_scale)`
- Defined: `wilmore_rbc.py:445`
- Doc: Convert cylindrical grid back to 3D vertices.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size)`
- Defined: `wilmore_rbc.py:475`
- Depends on: `willmore_crsital2.py`

### create_sphere `def create_sphere(self, radius)`
- Defined: `wilmore_rbc.py:481`
- Depends on: `willmore_crsital2.py`

### create_biconcave `def create_biconcave(self, radius, dimple_depth)`
- Defined: `wilmore_rbc.py:484`
- Doc: Create biconcave disc shape using Evans-Fung model.
- Depends on: `willmore_crsital2.py`

### create_evans_fung_rbc `def create_evans_fung_rbc(self, radius, dimple_depth, thickness)`
- Defined: `wilmore_rbc.py:490`
- Doc: Create RBC shape using Evans-Fung parametrization.
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, grid_size)`
- Defined: `wilmore_rbc.py:520`
- Depends on: `willmore_crsital2.py`

### compute_willmore `def compute_willmore(self, surface)`
- Defined: `wilmore_rbc.py:523`
- Depends on: `willmore_crsital2.py`

### compute_curvature_stats `def compute_curvature_stats(self, surface)`
- Defined: `wilmore_rbc.py:527`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, model, config)`
- Defined: `wilmore_rbc.py:548`
- Depends on: `willmore_crsital2.py`

### _compute_lr `def _compute_lr(self, step)`
- Defined: `wilmore_rbc.py:556`
- Doc: Compute learning rate with cosine schedule.
- Depends on: `willmore_crsital2.py`

### _compute_volume `def _compute_volume(self, surface)`
- Defined: `wilmore_rbc.py:567`
- Doc: Estimate volume from surface grid.
- Depends on: `willmore_crsital2.py`

### _normalize_volume `def _normalize_volume(self, surface, target_volume)`
- Defined: `wilmore_rbc.py:571`
- Doc: Normalize surface to preserve volume.
- Depends on: `willmore_crsital2.py`

### evolve `def evolve(self, initial_surface)`
- Defined: `wilmore_rbc.py:579`
- Depends on: `willmore_crsital2.py`

### save_obj `def save_obj(vertices, faces, filepath)`
- Defined: `wilmore_rbc.py:627`
- Depends on: `willmore_crsital2.py`

### save_html_comparison `def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolved_faces, biconcave_vertices, biconcave_faces, metrics, output_path)`
- Defined: `wilmore_rbc.py:636`
- Depends on: `willmore_crsital2.py`

### __init__ `def __init__(self, config)`
- Defined: `wilmore_rbc.py:794`
- Depends on: `willmore_crsital2.py`

### run `def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)`
- Defined: `wilmore_rbc.py:805`
- Depends on: `willmore_crsital2.py`
