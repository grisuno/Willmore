# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 15 | **Total Symbols Extracted:** 652 | **Total Imports:** 169

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    willmore_crystallography_suite_py_py["willmore_crystallography_suite.py.py (py)"]
    class willmore_crystallography_suite_py_py mod;
    willmore_crystallography_suite_py_py_WillmoreSuiteConfig["WillmoreSuiteConfig"]
    class willmore_crystallography_suite_py_py_WillmoreSuiteConfig cls;
    willmore_crystallography_suite_py_py --> willmore_crystallography_suite_py_py_WillmoreSuiteConfig
    willmore_crystallography_suite_py_py_SpectralLayer["SpectralLayer"]
    class willmore_crystallography_suite_py_py_SpectralLayer cls;
    willmore_crystallography_suite_py_py --> willmore_crystallography_suite_py_py_SpectralLayer
    willmore_crystallography_suite_py_py_MinimalSurfaceSpectralNetwork["MinimalSurfaceSpectralNetwork"]
    class willmore_crystallography_suite_py_py_MinimalSurfaceSpectralNetwork cls;
    willmore_crystallography_suite_py_py --> willmore_crystallography_suite_py_py_MinimalSurfaceSpectralNetwork
    willmore_crystallography_suite_py_py_MinimalSurfaceOperator["MinimalSurfaceOperator"]
    class willmore_crystallography_suite_py_py_MinimalSurfaceOperator cls;
    willmore_crystallography_suite_py_py --> willmore_crystallography_suite_py_py_MinimalSurfaceOperator
    willmore_crystallography_suite_py_py_SurfacePotentialGenerator["SurfacePotentialGenerator"]
    class willmore_crystallography_suite_py_py_SurfacePotentialGenerator cls;
    willmore_crystallography_suite_py_py --> willmore_crystallography_suite_py_py_SurfacePotentialGenerator
    willmore_crsital2_py["willmore_crsital2.py (py)"]
    class willmore_crsital2_py mod;
    willmore_crsital2_py_Config["Config"]
    class willmore_crsital2_py_Config cls;
    willmore_crsital2_py --> willmore_crsital2_py_Config
    willmore_crsital2_py_IPhaseDetector["IPhaseDetector"]
    class willmore_crsital2_py_IPhaseDetector cls;
    willmore_crsital2_py --> willmore_crsital2_py_IPhaseDetector
    willmore_crsital2_py_IMetricCalculator["IMetricCalculator"]
    class willmore_crsital2_py_IMetricCalculator cls;
    willmore_crsital2_py --> willmore_crsital2_py_IMetricCalculator
    willmore_crsital2_py_SeedManager["SeedManager"]
    class willmore_crsital2_py_SeedManager cls;
    willmore_crsital2_py --> willmore_crsital2_py_SeedManager
    willmore_crsital2_py_LoggerFactory["LoggerFactory"]
    class willmore_crsital2_py_LoggerFactory cls;
    willmore_crsital2_py --> willmore_crsital2_py_LoggerFactory
    willmore_zero_shot_scaler_py["willmore_zero_shot_scaler.py (py)"]
    class willmore_zero_shot_scaler_py mod;
    willmore_zero_shot_scaler_py_ScalerConfig["ScalerConfig"]
    class willmore_zero_shot_scaler_py_ScalerConfig cls;
    willmore_zero_shot_scaler_py --> willmore_zero_shot_scaler_py_ScalerConfig
    willmore_zero_shot_scaler_py_IConfigurationLoader["IConfigurationLoader"]
    class willmore_zero_shot_scaler_py_IConfigurationLoader cls;
    willmore_zero_shot_scaler_py --> willmore_zero_shot_scaler_py_IConfigurationLoader
    willmore_zero_shot_scaler_py_TOMLConfigurationLoader["TOMLConfigurationLoader"]
    class willmore_zero_shot_scaler_py_TOMLConfigurationLoader cls;
    willmore_zero_shot_scaler_py --> willmore_zero_shot_scaler_py_TOMLConfigurationLoader
    willmore_zero_shot_scaler_py_ICheckpointManager["ICheckpointManager"]
    class willmore_zero_shot_scaler_py_ICheckpointManager cls;
    willmore_zero_shot_scaler_py --> willmore_zero_shot_scaler_py_ICheckpointManager
    willmore_zero_shot_scaler_py_WillmoreCheckpointManager["WillmoreCheckpointManager"]
    class willmore_zero_shot_scaler_py_WillmoreCheckpointManager cls;
    willmore_zero_shot_scaler_py --> willmore_zero_shot_scaler_py_WillmoreCheckpointManager
    rbc_willmore_analysis2_py["rbc_willmore_analysis2.py (py)"]
    class rbc_willmore_analysis2_py mod;
    rbc_willmore_analysis2_py_RBCAnalysisConfig["RBCAnalysisConfig"]
    class rbc_willmore_analysis2_py_RBCAnalysisConfig cls;
    rbc_willmore_analysis2_py --> rbc_willmore_analysis2_py_RBCAnalysisConfig
    rbc_willmore_analysis2_py_ILogger["ILogger"]
    class rbc_willmore_analysis2_py_ILogger cls;
    rbc_willmore_analysis2_py --> rbc_willmore_analysis2_py_ILogger
    rbc_willmore_analysis2_py_StandardLogger["StandardLogger"]
    class rbc_willmore_analysis2_py_StandardLogger cls;
    rbc_willmore_analysis2_py --> rbc_willmore_analysis2_py_StandardLogger
    rbc_willmore_analysis2_py_IFileSystem["IFileSystem"]
    class rbc_willmore_analysis2_py_IFileSystem cls;
    rbc_willmore_analysis2_py --> rbc_willmore_analysis2_py_IFileSystem
    rbc_willmore_analysis2_py_StandardFileSystem["StandardFileSystem"]
    class rbc_willmore_analysis2_py_StandardFileSystem cls;
    rbc_willmore_analysis2_py --> rbc_willmore_analysis2_py_StandardFileSystem
    rbc_willmore_analysis_py["rbc_willmore_analysis.py (py)"]
    class rbc_willmore_analysis_py mod;
    rbc_willmore_analysis_py_RBCAnalysisConfig["RBCAnalysisConfig"]
    class rbc_willmore_analysis_py_RBCAnalysisConfig cls;
    rbc_willmore_analysis_py --> rbc_willmore_analysis_py_RBCAnalysisConfig
    rbc_willmore_analysis_py_ILogger["ILogger"]
    class rbc_willmore_analysis_py_ILogger cls;
    rbc_willmore_analysis_py --> rbc_willmore_analysis_py_ILogger
    rbc_willmore_analysis_py_StandardLogger["StandardLogger"]
    class rbc_willmore_analysis_py_StandardLogger cls;
    rbc_willmore_analysis_py --> rbc_willmore_analysis_py_StandardLogger
    rbc_willmore_analysis_py_IFileSystem["IFileSystem"]
    class rbc_willmore_analysis_py_IFileSystem cls;
    rbc_willmore_analysis_py --> rbc_willmore_analysis_py_IFileSystem
    rbc_willmore_analysis_py_StandardFileSystem["StandardFileSystem"]
    class rbc_willmore_analysis_py_StandardFileSystem cls;
    rbc_willmore_analysis_py --> rbc_willmore_analysis_py_StandardFileSystem
    wilmore_rbc_py["wilmore_rbc.py (py)"]
    class wilmore_rbc_py mod;
    wilmore_rbc_py_ReconstructionConfig["ReconstructionConfig"]
    class wilmore_rbc_py_ReconstructionConfig cls;
    wilmore_rbc_py --> wilmore_rbc_py_ReconstructionConfig
    wilmore_rbc_py_SpectralLayer["SpectralLayer"]
    class wilmore_rbc_py_SpectralLayer cls;
    wilmore_rbc_py --> wilmore_rbc_py_SpectralLayer
    wilmore_rbc_py_MinimalSurfaceSpectralNetwork["MinimalSurfaceSpectralNetwork"]
    class wilmore_rbc_py_MinimalSurfaceSpectralNetwork cls;
    wilmore_rbc_py --> wilmore_rbc_py_MinimalSurfaceSpectralNetwork
    wilmore_rbc_py_CheckpointLoader["CheckpointLoader"]
    class wilmore_rbc_py_CheckpointLoader cls;
    wilmore_rbc_py --> wilmore_rbc_py_CheckpointLoader
    wilmore_rbc_py_ModelBuilder["ModelBuilder"]
    class wilmore_rbc_py_ModelBuilder cls;
    wilmore_rbc_py --> wilmore_rbc_py_ModelBuilder
    rbc_model_reconstruction_128_py["rbc_model_reconstruction_128.py (py)"]
    class rbc_model_reconstruction_128_py mod;
    rbc_model_reconstruction_128_py_ReconstructionConfig["ReconstructionConfig"]
    class rbc_model_reconstruction_128_py_ReconstructionConfig cls;
    rbc_model_reconstruction_128_py --> rbc_model_reconstruction_128_py_ReconstructionConfig
    rbc_model_reconstruction_128_py_SpectralLayer["SpectralLayer"]
    class rbc_model_reconstruction_128_py_SpectralLayer cls;
    rbc_model_reconstruction_128_py --> rbc_model_reconstruction_128_py_SpectralLayer
    rbc_model_reconstruction_128_py_MinimalSurfaceSpectralNetwork["MinimalSurfaceSpectralNetwork"]
    class rbc_model_reconstruction_128_py_MinimalSurfaceSpectralNetwork cls;
    rbc_model_reconstruction_128_py --> rbc_model_reconstruction_128_py_MinimalSurfaceSpectralNetwork
    rbc_model_reconstruction_128_py_CheckpointLoader["CheckpointLoader"]
    class rbc_model_reconstruction_128_py_CheckpointLoader cls;
    rbc_model_reconstruction_128_py --> rbc_model_reconstruction_128_py_CheckpointLoader
    rbc_model_reconstruction_128_py_ModelBuilder["ModelBuilder"]
    class rbc_model_reconstruction_128_py_ModelBuilder cls;
    rbc_model_reconstruction_128_py --> rbc_model_reconstruction_128_py_ModelBuilder
    model_Reco_py["model_Reco.py (py)"]
    class model_Reco_py mod;
    model_Reco_py_load_rbc_mesh["load_rbc_mesh"]
    class model_Reco_py_load_rbc_mesh fn;
    model_Reco_py --> model_Reco_py_load_rbc_mesh
    model_Reco_py_center_mesh["center_mesh"]
    class model_Reco_py_center_mesh fn;
    model_Reco_py --> model_Reco_py_center_mesh
    model_Reco_py_cartesian_to_spherical["cartesian_to_spherical"]
    class model_Reco_py_cartesian_to_spherical fn;
    model_Reco_py --> model_Reco_py_cartesian_to_spherical
    model_Reco_py_spherical_to_cartesian["spherical_to_cartesian"]
    class model_Reco_py_spherical_to_cartesian fn;
    model_Reco_py --> model_Reco_py_spherical_to_cartesian
    model_Reco_py_evaluate_model_at_points["evaluate_model_at_points"]
    class model_Reco_py_evaluate_model_at_points fn;
    model_Reco_py --> model_Reco_py_evaluate_model_at_points
    rbc_py["rbc.py (py)"]
    class rbc_py mod;
    rbc_py_load_rbc_mesh["load_rbc_mesh"]
    class rbc_py_load_rbc_mesh fn;
    rbc_py --> rbc_py_load_rbc_mesh
    rbc_py_load_model["load_model"]
    class rbc_py_load_model fn;
    rbc_py --> rbc_py_load_model
    rbc_py_project_rbc_to_spherical_grid["project_rbc_to_spherical_grid"]
    class rbc_py_project_rbc_to_spherical_grid fn;
    rbc_py --> rbc_py_project_rbc_to_spherical_grid
    rbc_py_spherical_grid_to_cartesian["spherical_grid_to_cartesian"]
    class rbc_py_spherical_grid_to_cartesian fn;
    rbc_py --> rbc_py_spherical_grid_to_cartesian
    rbc_py_run_model_evolution["run_model_evolution"]
    class rbc_py_run_model_evolution fn;
    rbc_py --> rbc_py_run_model_evolution
    rbc_model_reconstruction__1__py["rbc_model_reconstruction (1).py (py)"]
    class rbc_model_reconstruction__1__py mod;
    rbc_model_reconstruction__1__py_load_rbc_mesh["load_rbc_mesh"]
    class rbc_model_reconstruction__1__py_load_rbc_mesh fn;
    rbc_model_reconstruction__1__py --> rbc_model_reconstruction__1__py_load_rbc_mesh
    rbc_model_reconstruction__1__py_load_model["load_model"]
    class rbc_model_reconstruction__1__py_load_model fn;
    rbc_model_reconstruction__1__py --> rbc_model_reconstruction__1__py_load_model
    rbc_model_reconstruction__1__py_project_rbc_to_spherical_grid["project_rbc_to_spherical_grid"]
    class rbc_model_reconstruction__1__py_project_rbc_to_spherical_grid fn;
    rbc_model_reconstruction__1__py --> rbc_model_reconstruction__1__py_project_rbc_to_spherical_grid
    rbc_model_reconstruction__1__py_spherical_grid_to_cartesian["spherical_grid_to_cartesian"]
    class rbc_model_reconstruction__1__py_spherical_grid_to_cartesian fn;
    rbc_model_reconstruction__1__py --> rbc_model_reconstruction__1__py_spherical_grid_to_cartesian
    rbc_model_reconstruction__1__py_run_model_evolution["run_model_evolution"]
    class rbc_model_reconstruction__1__py_run_model_evolution fn;
    rbc_model_reconstruction__1__py --> rbc_model_reconstruction__1__py_run_model_evolution
    rbc_model_reconstruction_py["rbc_model_reconstruction.py (py)"]
    class rbc_model_reconstruction_py mod;
    rbc_model_reconstruction_py_load_rbc_mesh["load_rbc_mesh"]
    class rbc_model_reconstruction_py_load_rbc_mesh fn;
    rbc_model_reconstruction_py --> rbc_model_reconstruction_py_load_rbc_mesh
    rbc_model_reconstruction_py_compute_vertex_normals["compute_vertex_normals"]
    class rbc_model_reconstruction_py_compute_vertex_normals fn;
    rbc_model_reconstruction_py --> rbc_model_reconstruction_py_compute_vertex_normals
    rbc_model_reconstruction_py_compute_face_areas["compute_face_areas"]
    class rbc_model_reconstruction_py_compute_face_areas fn;
    rbc_model_reconstruction_py --> rbc_model_reconstruction_py_compute_face_areas
    rbc_model_reconstruction_py_load_model["load_model"]
    class rbc_model_reconstruction_py_load_model fn;
    rbc_model_reconstruction_py --> rbc_model_reconstruction_py_load_model
    rbc_model_reconstruction_py_create_local_patches_for_vertices["create_local_patches_for_vertices"]
    class rbc_model_reconstruction_py_create_local_patches_for_vertices fn;
    rbc_model_reconstruction_py --> rbc_model_reconstruction_py_create_local_patches_for_vertices
    test_py["test.py (py)"]
    class test_py mod;
    test_py_load_model["load_model"]
    class test_py_load_model fn;
    test_py --> test_py_load_model
    test_py_test_model_behavior["test_model_behavior"]
    class test_py_test_model_behavior fn;
    test_py --> test_py_test_model_behavior
    test_py_main["main"]
    class test_py_main fn;
    test_py --> test_py_main
    lol_py["lol.py (py)"]
    class lol_py mod;
    lol_py_create_synthetic_rbc["create_synthetic_rbc"]
    class lol_py_create_synthetic_rbc fn;
    lol_py --> lol_py_create_synthetic_rbc
    lol_py_spherical_projection["spherical_projection"]
    class lol_py_spherical_projection fn;
    lol_py --> lol_py_spherical_projection
    lol_py_cylindrical_projection["cylindrical_projection"]
    class lol_py_cylindrical_projection fn;
    lol_py --> lol_py_cylindrical_projection
    lol_py_spherical_to_cartesian["spherical_to_cartesian"]
    class lol_py_spherical_to_cartesian fn;
    lol_py --> lol_py_spherical_to_cartesian
    lol_py_cylindrical_to_cartesian["cylindrical_to_cartesian"]
    class lol_py_cylindrical_to_cartesian fn;
    lol_py --> lol_py_cylindrical_to_cartesian
    app_py["app.py (py)"]
    class app_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_numpy["numpy"]
    class ext_numpy ext;
    lol_py -.->|imports| ext_numpy
    ext_os["os"]
    class ext_os ext;
    lol_py -.->|imports| ext_os
    ext_scipy_ndimage["scipy.ndimage"]
    class ext_scipy_ndimage ext;
    lol_py -.->|imports| ext_scipy_ndimage
    ext_argparse["argparse"]
    class ext_argparse ext;
    model_Reco_py -.->|imports| ext_argparse
    ext_json["json"]
    class ext_json ext;
    model_Reco_py -.->|imports| ext_json
    model_Reco_py -.->|imports| ext_os
    ext_sys["sys"]
    class ext_sys ext;
    model_Reco_py -.->|imports| ext_sys
    model_Reco_py -.->|imports| ext_numpy
    ext_torch["torch"]
    class ext_torch ext;
    model_Reco_py -.->|imports| ext_torch
    ext_torch_nn_functional["torch.nn.functional"]
    class ext_torch_nn_functional ext;
    model_Reco_py -.->|imports| ext_torch_nn_functional
    ext_willmore_crsital2["willmore_crsital2"]
    class ext_willmore_crsital2 ext;
    model_Reco_py -.->|imports| ext_willmore_crsital2
    model_Reco_py -.->|imports| ext_json
    rbc_py -.->|imports| ext_argparse
    rbc_py -.->|imports| ext_json
    rbc_py -.->|imports| ext_os
    rbc_py -.->|imports| ext_sys
    rbc_py -.->|imports| ext_numpy
    rbc_py -.->|imports| ext_torch
    rbc_py -.->|imports| ext_willmore_crsital2
    rbc_model_reconstruction__1__py -.->|imports| ext_argparse
    rbc_model_reconstruction__1__py -.->|imports| ext_json
    rbc_model_reconstruction__1__py -.->|imports| ext_os
    rbc_model_reconstruction__1__py -.->|imports| ext_sys
    rbc_model_reconstruction__1__py -.->|imports| ext_numpy
    rbc_model_reconstruction__1__py -.->|imports| ext_torch
    rbc_model_reconstruction__1__py -.->|imports| ext_willmore_crsital2
    rbc_model_reconstruction_py -.->|imports| ext_argparse
    rbc_model_reconstruction_py -.->|imports| ext_json
    rbc_model_reconstruction_py -.->|imports| ext_os
    rbc_model_reconstruction_py -.->|imports| ext_sys
    rbc_model_reconstruction_py -.->|imports| ext_numpy
    rbc_model_reconstruction_py -.->|imports| ext_torch
    rbc_model_reconstruction_py -.->|imports| ext_willmore_crsital2
    rbc_model_reconstruction_128_py -.->|imports| ext_argparse
    rbc_model_reconstruction_128_py -.->|imports| ext_json
    rbc_model_reconstruction_128_py -.->|imports| ext_os
    rbc_model_reconstruction_128_py -.->|imports| ext_sys
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    rbc_model_reconstruction_128_py -.->|imports| ext_dataclasses
    ext_typing["typing"]
    class ext_typing ext;
    rbc_model_reconstruction_128_py -.->|imports| ext_typing
    rbc_model_reconstruction_128_py -.->|imports| ext_numpy
    rbc_model_reconstruction_128_py -.->|imports| ext_torch
    ext_torch_nn["torch.nn"]
    class ext_torch_nn ext;
    rbc_model_reconstruction_128_py -.->|imports| ext_torch_nn
    rbc_model_reconstruction_128_py -.->|imports| ext_torch_nn_functional
    ext_scipy["scipy"]
    class ext_scipy ext;
    rbc_model_reconstruction_128_py -.->|imports| ext_scipy
    ext_scipy_interpolate["scipy.interpolate"]
    class ext_scipy_interpolate ext;
    rbc_model_reconstruction_128_py -.->|imports| ext_scipy_interpolate
    rbc_model_reconstruction_128_py -.->|imports| ext_willmore_crsital2
    ext_traceback["traceback"]
    class ext_traceback ext;
    rbc_model_reconstruction_128_py -.->|imports| ext_traceback
    rbc_willmore_analysis_py -.->|imports| ext_argparse
    rbc_willmore_analysis_py -.->|imports| ext_json
    ext_logging["logging"]
    class ext_logging ext;
    rbc_willmore_analysis_py -.->|imports| ext_logging
    ext_math["math"]
    class ext_math ext;
    rbc_willmore_analysis_py -.->|imports| ext_math
    rbc_willmore_analysis_py -.->|imports| ext_os
    rbc_willmore_analysis_py -.->|imports| ext_sys
    ext_warnings["warnings"]
    class ext_warnings ext;
    rbc_willmore_analysis_py -.->|imports| ext_warnings
    ext_abc["abc"]
    class ext_abc ext;
    rbc_willmore_analysis_py -.->|imports| ext_abc
    rbc_willmore_analysis_py -.->|imports| ext_dataclasses
    ext_datetime["datetime"]
    class ext_datetime ext;
    rbc_willmore_analysis_py -.->|imports| ext_datetime
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    rbc_willmore_analysis_py -.->|imports| ext_pathlib
    rbc_willmore_analysis_py -.->|imports| ext_typing
    rbc_willmore_analysis_py -.->|imports| ext_numpy
    rbc_willmore_analysis_py -.->|imports| ext_torch
    rbc_willmore_analysis_py -.->|imports| ext_torch_nn
    rbc_willmore_analysis_py -.->|imports| ext_torch_nn_functional
    rbc_willmore_analysis2_py -.->|imports| ext_argparse
    rbc_willmore_analysis2_py -.->|imports| ext_json
    rbc_willmore_analysis2_py -.->|imports| ext_logging
    rbc_willmore_analysis2_py -.->|imports| ext_math
    rbc_willmore_analysis2_py -.->|imports| ext_os
    rbc_willmore_analysis2_py -.->|imports| ext_sys
    rbc_willmore_analysis2_py -.->|imports| ext_warnings
    rbc_willmore_analysis2_py -.->|imports| ext_abc
    rbc_willmore_analysis2_py -.->|imports| ext_dataclasses
    rbc_willmore_analysis2_py -.->|imports| ext_datetime
    rbc_willmore_analysis2_py -.->|imports| ext_pathlib
    rbc_willmore_analysis2_py -.->|imports| ext_typing
    rbc_willmore_analysis2_py -.->|imports| ext_numpy
    rbc_willmore_analysis2_py -.->|imports| ext_torch
    rbc_willmore_analysis2_py -.->|imports| ext_torch_nn
    rbc_willmore_analysis2_py -.->|imports| ext_torch_nn_functional
    test_py -.->|imports| ext_argparse
    test_py -.->|imports| ext_numpy
    test_py -.->|imports| ext_torch
    test_py -.->|imports| ext_sys
    test_py -.->|imports| ext_os
    test_py -.->|imports| ext_willmore_crsital2
    willmore_crsital2_py -.->|imports| ext_argparse
    willmore_crsital2_py -.->|imports| ext_torch
    willmore_crsital2_py -.->|imports| ext_torch_nn
    willmore_crsital2_py -.->|imports| ext_torch_nn_functional
    ext_torch_optim["torch.optim"]
    class ext_torch_optim ext;
    willmore_crsital2_py -.->|imports| ext_torch_optim
    ext_torch_utils_data["torch.utils.data"]
    class ext_torch_utils_data ext;
    willmore_crsital2_py -.->|imports| ext_torch_utils_data
    willmore_crsital2_py -.->|imports| ext_numpy
    willmore_crsital2_py -.->|imports| ext_os
    ext_time["time"]
    class ext_time ext;
    willmore_crsital2_py -.->|imports| ext_time
    willmore_crsital2_py -.->|imports| ext_json
    willmore_crsital2_py -.->|imports| ext_datetime
    willmore_crsital2_py -.->|imports| ext_typing
    willmore_crsital2_py -.->|imports| ext_abc
    willmore_crsital2_py -.->|imports| ext_dataclasses
    ext_collections["collections"]
    class ext_collections ext;
    willmore_crsital2_py -.->|imports| ext_collections
    willmore_crsital2_py -.->|imports| ext_logging
    willmore_crsital2_py -.->|imports| ext_math
    ext_copy["copy"]
    class ext_copy ext;
    willmore_crsital2_py -.->|imports| ext_copy
    willmore_crsital2_py -.->|imports| ext_warnings
    willmore_crystallography_suite_py_py -.->|imports| ext_argparse
    willmore_crystallography_suite_py_py -.->|imports| ext_copy
    ext_glob["glob"]
    class ext_glob ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_glob
    willmore_crystallography_suite_py_py -.->|imports| ext_json
    willmore_crystallography_suite_py_py -.->|imports| ext_logging
    willmore_crystallography_suite_py_py -.->|imports| ext_math
    willmore_crystallography_suite_py_py -.->|imports| ext_os
    ext_re["re"]
    class ext_re ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_re
    willmore_crystallography_suite_py_py -.->|imports| ext_time
    willmore_crystallography_suite_py_py -.->|imports| ext_warnings
    willmore_crystallography_suite_py_py -.->|imports| ext_abc
    willmore_crystallography_suite_py_py -.->|imports| ext_collections
    willmore_crystallography_suite_py_py -.->|imports| ext_dataclasses
    willmore_crystallography_suite_py_py -.->|imports| ext_datetime
    willmore_crystallography_suite_py_py -.->|imports| ext_pathlib
    willmore_crystallography_suite_py_py -.->|imports| ext_typing
    ext_matplotlib["matplotlib"]
    class ext_matplotlib ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_matplotlib
    ext_matplotlib_pyplot["matplotlib.pyplot"]
    class ext_matplotlib_pyplot ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_matplotlib_pyplot
    ext_matplotlib_gridspec["matplotlib.gridspec"]
    class ext_matplotlib_gridspec ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_matplotlib_gridspec
    ext_seaborn["seaborn"]
    class ext_seaborn ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_seaborn
    willmore_crystallography_suite_py_py -.->|imports| ext_numpy
    willmore_crystallography_suite_py_py -.->|imports| ext_torch
    willmore_crystallography_suite_py_py -.->|imports| ext_torch_nn
    willmore_crystallography_suite_py_py -.->|imports| ext_torch_nn_functional
    willmore_crystallography_suite_py_py -.->|imports| ext_torch_optim
    willmore_crystallography_suite_py_py -.->|imports| ext_torch_utils_data
    willmore_crystallography_suite_py_py -.->|imports| ext_scipy
    ext_scipy_stats["scipy.stats"]
    class ext_scipy_stats ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_scipy_stats
    ext_scipy_linalg["scipy.linalg"]
    class ext_scipy_linalg ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_scipy_linalg
    ext_scipy_optimize["scipy.optimize"]
    class ext_scipy_optimize ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_scipy_optimize
    ext_sklearn_decomposition["sklearn.decomposition"]
    class ext_sklearn_decomposition ext;
    willmore_crystallography_suite_py_py -.->|imports| ext_sklearn_decomposition
    willmore_crystallography_suite_py_py -.->|imports| ext_traceback
    willmore_zero_shot_scaler_py -.->|imports| ext_argparse
    willmore_zero_shot_scaler_py -.->|imports| ext_json
    willmore_zero_shot_scaler_py -.->|imports| ext_logging
    willmore_zero_shot_scaler_py -.->|imports| ext_math
    willmore_zero_shot_scaler_py -.->|imports| ext_os
    willmore_zero_shot_scaler_py -.->|imports| ext_sys
    willmore_zero_shot_scaler_py -.->|imports| ext_time
    willmore_zero_shot_scaler_py -.->|imports| ext_abc
    willmore_zero_shot_scaler_py -.->|imports| ext_dataclasses
    willmore_zero_shot_scaler_py -.->|imports| ext_datetime
    willmore_zero_shot_scaler_py -.->|imports| ext_pathlib
    willmore_zero_shot_scaler_py -.->|imports| ext_typing
    willmore_zero_shot_scaler_py -.->|imports| ext_numpy
    willmore_zero_shot_scaler_py -.->|imports| ext_torch
    willmore_zero_shot_scaler_py -.->|imports| ext_torch_nn
    willmore_zero_shot_scaler_py -.->|imports| ext_torch_nn_functional
    willmore_zero_shot_scaler_py -.->|imports| ext_willmore_crsital2
    ext_tomli["tomli"]
    class ext_tomli ext;
    willmore_zero_shot_scaler_py -.->|imports| ext_tomli
    ext_tomllib["tomllib"]
    class ext_tomllib ext;
    willmore_zero_shot_scaler_py -.->|imports| ext_tomllib
    wilmore_rbc_py -.->|imports| ext_argparse
    wilmore_rbc_py -.->|imports| ext_json
    wilmore_rbc_py -.->|imports| ext_os
    wilmore_rbc_py -.->|imports| ext_sys
    wilmore_rbc_py -.->|imports| ext_dataclasses
    wilmore_rbc_py -.->|imports| ext_typing
    wilmore_rbc_py -.->|imports| ext_numpy
    wilmore_rbc_py -.->|imports| ext_torch
    wilmore_rbc_py -.->|imports| ext_torch_nn
    wilmore_rbc_py -.->|imports| ext_torch_nn_functional
    wilmore_rbc_py -.->|imports| ext_scipy
    wilmore_rbc_py -.->|imports| ext_scipy_interpolate
    wilmore_rbc_py -.->|imports| ext_willmore_crsital2
    wilmore_rbc_py -.->|imports| ext_traceback
```

---

## Architecture Reference

### PY (14 files)

#### `app.py`
**Path:** `app.py`

*No symbols extracted*

#### `lol.py`
**Path:** `lol.py`

**Functions:**
- `create_synthetic_rbc` (line 16) - *RBC sintético con forma bicóncava.*
- `spherical_projection` (line 44) - *Proyección esférica - tiene problemas con dimples.*
- `cylindrical_projection` (line 76) - *Proyección cilíndrica - NATURAL para RBC.

Coordenadas:
- z: altura (-z_max a +z_max)
- phi: ángulo azimutal (-π a π)
- rho: radio en el plano xy

El RBC es naturalmente cilíndrico: los dimples están en z=±z_max,
no en direcciones angulares.*
- `spherical_to_cartesian` (line 123) - *Convierte grilla esférica a 3D.*
- `cylindrical_to_cartesian` (line 144) - *Convierte grilla cilíndrica a 3D.*
- `compute_metrics` (line 164) - *Computa métricas de calidad.*
- `save_obj` (line 181)
- `main` (line 189)

#### `model_Reco.py`
**Path:** `model_Reco.py`

**Functions:**
- `load_rbc_mesh` (line 27)
- `center_mesh` (line 49)
- `cartesian_to_spherical` (line 54)
- `spherical_to_cartesian` (line 63)
- `evaluate_model_at_points` (line 70) - *Evalúa el modelo en puntos arbitrarios (no en grilla regular).

Estrategia: Para cada punto, encontrar su celda en la grilla 16x16,
evaluar el modelo en esa celda, y usar el valor como predicción.*
- `load_model` (line 134)
- `compute_curvatures` (line 159) - *Compute curvatures using the same operator as training.*
- `save_obj` (line 189)
- `save_html_viewer` (line 197)
- `main` (line 338)

#### `rbc.py`
**Path:** `rbc.py`

**Functions:**
- `load_rbc_mesh` (line 30) - *Load RBC mesh from OpenRBC files.*
- `load_model` (line 53) - *Load the trained Willmore model from checkpoint.*
- `project_rbc_to_spherical_grid` (line 94) - *Project entire RBC mesh onto a spherical coordinate grid.

This creates a single grid_size x grid_size representation
that the model can process.*
- `spherical_grid_to_cartesian` (line 139) - *Convert spherical grid back to 3D vertices.*
- `run_model_evolution` (line 164) - *Run model iteratively to evolve the surface.

Returns the evolution trajectory.*
- `create_sphere_grid` (line 202) - *Create a perfect sphere grid for comparison.*
- `create_biconcave_grid` (line 212) - *Create a biconcave disc shape on spherical grid.*
- `compute_willmore_on_grid` (line 224) - *Compute Willmore energy using MinimalSurfaceOperator.*
- `save_obj` (line 231) - *Save mesh as OBJ file.*
- `save_html_comparison` (line 240) - *Create interactive HTML comparing all shapes.*
- `main` (line 393)

#### `rbc_model_reconstruction (1).py`
**Path:** `rbc_model_reconstruction (1).py`

**Functions:**
- `load_rbc_mesh` (line 30) - *Load RBC mesh from OpenRBC files.*
- `load_model` (line 53) - *Load the trained Willmore model from checkpoint.*
- `project_rbc_to_spherical_grid` (line 94) - *Project entire RBC mesh onto a spherical coordinate grid.

This creates a single grid_size x grid_size representation
that the model can process.*
- `spherical_grid_to_cartesian` (line 139) - *Convert spherical grid back to 3D vertices.*
- `run_model_evolution` (line 164) - *Run model iteratively to evolve the surface.

Returns the evolution trajectory.*
- `create_sphere_grid` (line 202) - *Create a perfect sphere grid for comparison.*
- `create_biconcave_grid` (line 212) - *Create a biconcave disc shape on spherical grid.*
- `compute_willmore_on_grid` (line 224) - *Compute Willmore energy using MinimalSurfaceOperator.*
- `save_obj` (line 231) - *Save mesh as OBJ file.*
- `save_html_comparison` (line 240) - *Create interactive HTML comparing all shapes.*
- `main` (line 393)

#### `rbc_model_reconstruction.py`
**Path:** `rbc_model_reconstruction.py`

**Functions:**
- `load_rbc_mesh` (line 31) - *Load RBC mesh from OpenRBC files.*
- `compute_vertex_normals` (line 54) - *Compute vertex normals.*
- `compute_face_areas` (line 75) - *Compute face areas.*
- `load_model` (line 84) - *Load the trained Willmore model from checkpoint.*
- `create_local_patches_for_vertices` (line 124) - *Create local surface patches around each vertex for model input.

For each vertex, we create a small 2D grid representing the local
surface neighborhood, which can be processed by the model.*
- `run_model_on_patches` (line 215) - *Run the model on all vertex patches and extract predictions.

Returns predicted curvature-like values for each vertex.*
- `compute_analytical_curvature` (line 252) - *Compute analytical mean curvature for comparison.*
- `save_ply_with_values` (line 284) - *Save mesh as PLY with scalar values as vertex colors.*
- `save_html_viewer` (line 319) - *Create interactive HTML viewer with model predictions on actual RBC mesh.*
- `main` (line 530)

#### `rbc_model_reconstruction_128.py`
**Path:** `rbc_model_reconstruction_128.py`

**Classs:**
- `ReconstructionConfig` (line 37) - *Configuration for RBC reconstruction.*
- `SpectralLayer` (line 51) - *Spectral convolution layer for minimal surface processing.*
- `MinimalSurfaceSpectralNetwork` (line 85) - *Spectral network for minimal surface computation.*
- `CheckpointLoader` (line 120) - *Handles loading of model checkpoints.*
- `ModelBuilder` (line 130) - *Builds and initializes models from configuration.*
- `RBCMeshLoader` (line 169) - *Loads RBC mesh data from OpenRBC format files.*
- `ImprovedSphericalProjector` (line 195) - *Improved spherical projection with proper handling of biconcave geometry.

Key improvements:
1. Area-weighted averaging to avoid oversampling at poles
2. RBF interpolation for smooth reconstruction
3. Proper handling of the dimple regions
4. Gaussian smoothing in parameter space*
- `CylindricalProjector` (line 377) - *Cylindrical projection - often better for biconcave shapes.

The RBC is naturally more cylindrical than spherical,
with the dimples on top and bottom.*
- `SyntheticShapeGenerator` (line 469) - *Generates synthetic shapes for comparison.*
- `WillmoreMetricsCalculator` (line 514) - *Calculates Willmore energy and curvature metrics.*
- `SurfaceEvolver` (line 542) - *Evolves surfaces using the trained model.*
- `MeshExporter` (line 589) - *Exports meshes to various formats.*
- `RBCReconstructionPipeline` (line 757) - *Main pipeline for RBC reconstruction using scaled model.*

**Functions:**
- `build_argument_parser` (line 926)
- `main` (line 989)
- `__init__` (line 54)
- `forward` (line 65)
- `__init__` (line 88)
- `forward` (line 109)
- `load` (line 124)
- `build` (line 134)
- `load_from_checkpoint` (line 145)
- `load` (line 173)
- `__init__` (line 206)
- `compute_vertex_areas` (line 214) - *Compute approximate area associated with each vertex.*
- `project_mesh` (line 229) - *Project mesh onto spherical grid with proper area weighting.*
- `_area_weighted_projection` (line 267) - *Project using area-weighted averaging.*
- `_rbf_interpolation` (line 300) - *Use RBF interpolation for smooth reconstruction.*
- `_apply_spherical_smoothing` (line 330) - *Apply Gaussian smoothing adapted to spherical coordinates.*
- `to_cartesian` (line 352) - *Convert spherical grid back to 3D vertices.*
- `__init__` (line 385)
- `project_mesh` (line 393) - *Project mesh using cylindrical coordinates.*
- `to_cartesian` (line 442) - *Convert cylindrical grid back to 3D vertices.*
- `__init__` (line 472)
- `create_sphere` (line 478)
- `create_biconcave` (line 481) - *Create biconcave disc shape using Evans-Fung model.*
- `create_evans_fung_rbc` (line 487) - *Create RBC shape using Evans-Fung parametrization.

The RBC cross-section follows:
r(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)

This creates the characteristic biconcave shape.*
- `__init__` (line 517)
- `compute_willmore` (line 520)
- `compute_curvature_stats` (line 524)
- `__init__` (line 545)
- `evolve` (line 553)
- `save_obj` (line 593)
- `save_html_comparison` (line 602)
- `__init__` (line 760)
- `run` (line 771)

#### `rbc_willmore_analysis.py`
**Path:** `rbc_willmore_analysis.py`

**Classs:**
- `RBCAnalysisConfig` (line 55) - *Configuration container for RBC Willmore analysis.

This dataclass holds all configuration parameters for the analysis
pipeline, including mesh processing, model loading, and visualization
settings.*
- `ILogger` (line 102) - *Abstract interface for logging implementations.*
- `StandardLogger` (line 122) - *Standard logging implementation using Python logging module.*
- `IFileSystem` (line 149) - *Abstract interface for file system operations.*
- `StandardFileSystem` (line 169) - *Standard file system implementation.*
- `MeshData` (line 188) - *Container for 3D mesh data.

Attributes:
    vertices: Nx3 numpy array of vertex positions
    faces: Mx3 numpy array of triangle face indices
    bonds: Kx2 numpy array of bond edge indices
    normals: Nx3 numpy array of vertex normals (computed)
    areas: M numpy array of face areas (computed)*
- `IMeshLoader` (line 228) - *Abstract interface for mesh loading implementations.*
- `OpenRBCMeshLoader` (line 236) - *Mesh loader for OpenRBC format data files.

OpenRBC stores mesh data in three separate text files:
- rbc.vert.txt: Vertex positions (x, y, z per line)
- rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)
- rbc.bond.txt: Bond edges (2 vertex indices per line)*
- `SyntheticMeshGenerator` (line 375) - *Generator for synthetic comparison surfaces.

Creates reference surfaces (sphere, torus) for comparison with
RBC morphology analysis.*
- `ICurvatureCalculator` (line 545) - *Abstract interface for curvature calculation implementations.*
- `DiscreteCurvatureCalculator` (line 563) - *Discrete curvature calculation using the cotangent formula.

Implements the discrete differential geometry approach for computing
mean and Gaussian curvature on triangle meshes based on the work by
Meyer et al. (2003) and others.

The mean curvature at a vertex is computed using the Laplace-Beltrami
operator applied to the vertex positions:

    H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)

where A_i is the Voronoi area around vertex i.*
- `SpectralLayer` (line 799) - *Spectral convolution layer for surface processing.

Implements convolution in the frequency domain using FFT,
allowing the network to learn global surface patterns.*
- `MinimalSurfaceSpectralNetwork` (line 848) - *Neural network for minimal surface detection and Willmore energy learning.

This network learns to predict mean curvature fields and identify
minimal surface configurations through spectral convolution layers.*
- `IModelLoader` (line 894) - *Abstract interface for model loading implementations.*
- `CheckpointModelLoader` (line 902) - *Model loader that loads from PyTorch checkpoint files.*
- `SurfaceAnalysisEngine` (line 1002) - *Main engine for RBC surface analysis using Willmore energy model.

This class orchestrates the complete analysis pipeline, from mesh loading
to curvature computation and shape emergence testing.*

**Functions:**
- `parse_arguments` (line 1376)
- `create_config_from_args` (line 1470)
- `main` (line 1488)
- `info` (line 106)
- `warning` (line 110)
- `error` (line 114)
- `debug` (line 118)
- `__init__` (line 125)
- `info` (line 136)
- `warning` (line 139)
- `error` (line 142)
- `debug` (line 145)
- `exists` (line 153)
- `read_text` (line 157)
- `write_text` (line 161)
- `makedirs` (line 165)
- `exists` (line 172)
- `read_text` (line 175)
- `write_text` (line 179)
- `makedirs` (line 183)
- `num_vertices` (line 206)
- `num_faces` (line 210)
- `num_bonds` (line 214)
- `to_dict` (line 217)
- `load` (line 232)
- `__init__` (line 245)
- `load` (line 249)
- `_load_vertices` (line 267)
- `_load_faces` (line 286)
- `_load_bonds` (line 308)
- `_compute_normals` (line 330)
- `_compute_areas` (line 355)
- `__init__` (line 382)
- `generate_sphere` (line 385)
- `generate_torus` (line 424)
- `generate_biconcave_disc` (line 467)
- `_compute_mesh_properties` (line 511)
- `compute_mean_curvature` (line 549)
- `compute_gaussian_curvature` (line 553)
- `compute_willmore_energy` (line 557)
- `__init__` (line 578)
- `compute_mean_curvature` (line 581)
- `compute_gaussian_curvature` (line 616)
- `compute_willmore_energy` (line 664)
- `_compute_edge_cotangents` (line 682)
- `_get_vertex_neighbors` (line 737)
- `_compute_mixed_voronoi_area` (line 748)
- `__init__` (line 806)
- `forward` (line 820)
- `__init__` (line 855)
- `forward` (line 880)
- `load` (line 898)
- `__init__` (line 905)
- `_detect_model_params` (line 909)
- `load` (line 947)
- `__init__` (line 1009)
- `initialize` (line 1028)
- `_load_rbc_mesh` (line 1048)
- `_generate_synthetic_meshes` (line 1060)
- `analyze_mesh` (line 1076)
- `_compute_surface_area` (line 1125)
- `_compute_volume` (line 1130)
- `_compute_asphericity` (line 1141)
- `_compute_biconcavity_index` (line 1161)
- `_compute_histogram` (line 1186)
- `run_shape_emergence_test` (line 1192)
- `_analyze_rbc_morphology` (line 1235)
- `_verify_gauss_bonnet` (line 1277)
- `run_mean_curvature_flow` (line 1318)
- `save_results` (line 1357)
- `save_mesh_obj` (line 1362)

#### `rbc_willmore_analysis2.py`
**Path:** `rbc_willmore_analysis2.py`

**Classs:**
- `RBCAnalysisConfig` (line 55) - *Configuration container for RBC Willmore analysis.

This dataclass holds all configuration parameters for the analysis
pipeline, including mesh processing, model loading, and visualization
settings.*
- `ILogger` (line 102) - *Abstract interface for logging implementations.*
- `StandardLogger` (line 122) - *Standard logging implementation using Python logging module.*
- `IFileSystem` (line 149) - *Abstract interface for file system operations.*
- `StandardFileSystem` (line 169) - *Standard file system implementation.*
- `MeshData` (line 188) - *Container for 3D mesh data.

Attributes:
    vertices: Nx3 numpy array of vertex positions
    faces: Mx3 numpy array of triangle face indices
    bonds: Kx2 numpy array of bond edge indices
    normals: Nx3 numpy array of vertex normals (computed)
    areas: M numpy array of face areas (computed)*
- `IMeshLoader` (line 228) - *Abstract interface for mesh loading implementations.*
- `OpenRBCMeshLoader` (line 236) - *Mesh loader for OpenRBC format data files.

OpenRBC stores mesh data in three separate text files:
- rbc.vert.txt: Vertex positions (x, y, z per line)
- rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)
- rbc.bond.txt: Bond edges (2 vertex indices per line)*
- `SyntheticMeshGenerator` (line 375) - *Generator for synthetic comparison surfaces.

Creates reference surfaces (sphere, torus) for comparison with
RBC morphology analysis.*
- `ICurvatureCalculator` (line 545) - *Abstract interface for curvature calculation implementations.*
- `DiscreteCurvatureCalculator` (line 563) - *Discrete curvature calculation using the cotangent formula.

Implements the discrete differential geometry approach for computing
mean and Gaussian curvature on triangle meshes based on the work by
Meyer et al. (2003) and others.

The mean curvature at a vertex is computed using the Laplace-Beltrami
operator applied to the vertex positions:

    H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)

where A_i is the Voronoi area around vertex i.*
- `SpectralLayer` (line 799) - *Spectral convolution layer for surface processing.

Implements convolution in the frequency domain using FFT,
allowing the network to learn global surface patterns.*
- `MinimalSurfaceSpectralNetwork` (line 848) - *Neural network for minimal surface detection and Willmore energy learning.

This network learns to predict mean curvature fields and identify
minimal surface configurations through spectral convolution layers.*
- `IModelLoader` (line 894) - *Abstract interface for model loading implementations.*
- `CheckpointModelLoader` (line 902) - *Model loader that loads from PyTorch checkpoint files.*
- `SurfaceAnalysisEngine` (line 1002) - *Main engine for RBC surface analysis using Willmore energy model.

This class orchestrates the complete analysis pipeline, from mesh loading
to curvature computation and shape emergence testing.*

**Functions:**
- `parse_arguments` (line 1394)
- `create_config_from_args` (line 1488)
- `main` (line 1506)
- `info` (line 106)
- `warning` (line 110)
- `error` (line 114)
- `debug` (line 118)
- `__init__` (line 125)
- `info` (line 136)
- `warning` (line 139)
- `error` (line 142)
- `debug` (line 145)
- `exists` (line 153)
- `read_text` (line 157)
- `write_text` (line 161)
- `makedirs` (line 165)
- `exists` (line 172)
- `read_text` (line 175)
- `write_text` (line 179)
- `makedirs` (line 183)
- `num_vertices` (line 206)
- `num_faces` (line 210)
- `num_bonds` (line 214)
- `to_dict` (line 217)
- `load` (line 232)
- `__init__` (line 245)
- `load` (line 249)
- `_load_vertices` (line 267)
- `_load_faces` (line 286)
- `_load_bonds` (line 308)
- `_compute_normals` (line 330)
- `_compute_areas` (line 355)
- `__init__` (line 382)
- `generate_sphere` (line 385)
- `generate_torus` (line 424)
- `generate_biconcave_disc` (line 467)
- `_compute_mesh_properties` (line 511)
- `compute_mean_curvature` (line 549)
- `compute_gaussian_curvature` (line 553)
- `compute_willmore_energy` (line 557)
- `__init__` (line 578)
- `compute_mean_curvature` (line 581)
- `compute_gaussian_curvature` (line 616)
- `compute_willmore_energy` (line 664)
- `_compute_edge_cotangents` (line 682)
- `_get_vertex_neighbors` (line 737)
- `_compute_mixed_voronoi_area` (line 748)
- `__init__` (line 806)
- `forward` (line 820)
- `__init__` (line 855)
- `forward` (line 880)
- `load` (line 898)
- `__init__` (line 905)
- `_detect_model_params` (line 909)
- `load` (line 947)
- `__init__` (line 1009)
- `initialize` (line 1028)
- `_load_rbc_mesh` (line 1048)
- `_generate_synthetic_meshes` (line 1060)
- `analyze_mesh` (line 1076)
- `_compute_surface_area` (line 1125)
- `_compute_volume` (line 1130)
- `_compute_asphericity` (line 1141)
- `_compute_biconcavity_index` (line 1161)
- `_compute_histogram` (line 1186)
- `run_shape_emergence_test` (line 1192)
- `_analyze_rbc_morphology` (line 1235)
- `_verify_gauss_bonnet` (line 1277)
- `run_mean_curvature_flow` (line 1318)
- `save_results` (line 1357)
- `save_mesh_obj` (line 1380)
- `convert_to_native` (line 1360)

#### `test.py`
**Path:** `test.py`

**Functions:**
- `load_model` (line 20)
- `test_model_behavior` (line 45) - *Test que respeta la escala pequeña del modelo.*
- `main` (line 154)

#### `willmore_crsital2.py`
**Path:** `willmore_crsital2.py`

**Classs:**
- `Config` (line 53)
- `IPhaseDetector` (line 201)
- `IMetricCalculator` (line 207)
- `SeedManager` (line 213)
- `LoggerFactory` (line 227)
- `MinimalSurfaceOperator` (line 242)
- `SpectralLayer` (line 307)
- `MinimalSurfaceBackbone` (line 331)
- `MinimalSurfaceInferenceEngine` (line 351)
- `SurfacePotentialGenerator` (line 399)
- `MinimalSurfaceDataset` (line 452)
- `MinimalSurfaceSpectralNetwork` (line 539)
- `WillmoreEnergyCalculator` (line 567)
- `RicciFlowCalculator` (line 622)
- `FullFourierAnalyzer` (line 668)
- `FourierMassCenterAnalyzer` (line 711)
- `TopologicalPhaseDetector` (line 751)
- `SpectralFieldExtractor` (line 780)
- `TopologicalMetricsCalculator` (line 798)
- `LocalComplexityAnalyzer` (line 818)
- `SuperpositionAnalyzer` (line 833)
- `CrystallographyMetricsCalculator` (line 851)
- `ThermodynamicMetricsCalculator` (line 965)
- `SpectralGeometryCalculator` (line 1021)
- `RicciCurvatureCalculator` (line 1044)
- `SpectroscopyMetricsCalculator` (line 1065)
- `LambdaPressureScheduler` (line 1082)
- `AdaptiveLambdaScheduler` (line 1114)
- `QuadruplePrecisionLambdaScheduler` (line 1129)
- `AnnealingScheduler` (line 1161)
- `TopologicalAnnealingScheduler` (line 1186)
- `TrainingMetricsMonitor` (line 1202)
- `CheckpointManager` (line 1261)
- `Phase5CheckpointManager` (line 1291)
- `WeightIntegrityChecker` (line 1322)
- `TrainingEngine` (line 1338)
- `BatchSizeProspector` (line 1447)
- `SeedMiner` (line 1483)
- `FullTrainingOrchestrator` (line 1533)
- `RefinementOrchestrator` (line 1599)
- `Phase5Orchestrator` (line 1663)
- `ExperimentOrchestrator` (line 1725)

**Functions:**
- `build_argument_parser` (line 1839)
- `main` (line 1868)
- `detect` (line 203)
- `compute` (line 209)
- `set_seed` (line 215)
- `create_logger` (line 229)
- `__init__` (line 243)
- `_precompute_spectral_operators` (line 249)
- `apply_laplacian` (line 257)
- `compute_mean_curvature` (line 262)
- `compute_gaussian_curvature` (line 273)
- `compute_willmore_energy` (line 284)
- `compute_surface_area` (line 290)
- `mean_curvature_flow` (line 297)
- `__init__` (line 308)
- `forward` (line 315)
- `__init__` (line 332)
- `forward` (line 342)
- `__init__` (line 352)
- `_try_load_backbone` (line 359)
- `apply_mean_curvature` (line 382)
- `mean_curvature_evolve` (line 388)
- `__init__` (line 400)
- `pyramid_potential` (line 404)
- `cube_potential` (line 411)
- `dodecahedron_potential` (line 418)
- `torus_potential` (line 426)
- `hyperbolic_potential` (line 434)
- `generate_mixed_potential` (line 442)
- `__init__` (line 453)
- `_solve_minimal_surface` (line 487)
- `_evolve_minimal_surface` (line 513)
- `__len__` (line 534)
- `__getitem__` (line 535)
- `get_validation_batch` (line 536)
- `__init__` (line 540)
- `forward` (line 557)
- `__init__` (line 568)
- `compute` (line 573)
- `compute_surface_metrics` (line 590)
- `_empty_metrics` (line 618)
- `__init__` (line 623)
- `compute` (line 627)
- `_compute_ricci_scalar` (line 640)
- `_estimate_sectional_curvatures` (line 647)
- `_compute_flow_velocity` (line 659)
- `_empty_metrics` (line 664)
- `__init__` (line 669)
- `compute_full_spectrum` (line 677)
- `compute_resonance_metrics` (line 701)
- `__init__` (line 712)
- `_get_freq_grids` (line 720)
- `compute_mass_center` (line 728)
- `__init__` (line 752)
- `detect` (line 759)
- `extract` (line 782)
- `__init__` (line 799)
- `compute` (line 804)
- `_empty_metrics` (line 814)
- `compute_local_complexity` (line 820)
- `compute_superposition` (line 835)
- `__init__` (line 852)
- `compute` (line 856)
- `compute_kappa` (line 861)
- `compute_discretization_margin` (line 903)
- `compute_alpha_purity` (line 911)
- `compute_kappa_quantum` (line 916)
- `compute_poynting_vector` (line 935)
- `compute_hbar_effective` (line 946)
- `compute_all_metrics` (line 953)
- `__init__` (line 966)
- `compute` (line 969)
- `compute_effective_temperature` (line 983)
- `compute_specific_heat` (line 1001)
- `compute_gibbs_free_energy` (line 1010)
- `compute_critical_temperature` (line 1017)
- `__init__` (line 1022)
- `compute` (line 1025)
- `__init__` (line 1045)
- `compute` (line 1048)
- `__init__` (line 1066)
- `compute` (line 1069)
- `__init__` (line 1083)
- `current_lambda` (line 1092)
- `step` (line 1095)
- `compute_regularization_loss` (line 1102)
- `set_lambda` (line 1110)
- `__init__` (line 1115)
- `step_adaptive` (line 1120)
- `__init__` (line 1130)
- `current_lambda` (line 1139)
- `step` (line 1142)
- `compute_regularization_loss` (line 1149)
- `set_lambda` (line 1157)
- `__init__` (line 1162)
- `temperature` (line 1170)
- `step` (line 1173)
- `accept_perturbation` (line 1176)
- `should_restart` (line 1182)
- `__init__` (line 1187)
- `step_adaptive` (line 1191)
- `__init__` (line 1203)
- `update_metrics` (line 1210)
- `compute_delta_slope` (line 1219)
- `format_progress_bar` (line 1229)
- `__init__` (line 1262)
- `should_save_checkpoint` (line 1271)
- `save_checkpoint` (line 1276)
- `__init__` (line 1292)
- `should_save` (line 1302)
- `save_checkpoint` (line 1307)
- `check` (line 1324)
- `__init__` (line 1339)
- `compute_weight_metrics` (line 1354)
- `compute_norm_conservation_error` (line 1364)
- `train_single_epoch` (line 1373)
- `validate` (line 1398)
- `collect_all_metrics` (line 1408)
- `__init__` (line 1448)
- `prospect` (line 1453)
- `__init__` (line 1484)
- `mine` (line 1490)
- `__init__` (line 1534)
- `run_phase3_training` (line 1541)
- `__init__` (line 1600)
- `run_phase4_refinement` (line 1610)
- `__init__` (line 1664)
- `run_phase5_crystallization` (line 1674)
- `__init__` (line 1726)
- `run` (line 1730)
- `_save_final_results` (line 1789)
- `safe_get` (line 1231)

#### `willmore_crystallography_suite.py.py`
**Path:** `willmore_crystallography_suite.py.py`

**Classs:**
- `WillmoreSuiteConfig` (line 52) - *Master configuration for Willmore crystallography suite.*
- `SpectralLayer` (line 92) - *Spectral convolution layer with learnable frequency-domain kernels.*
- `MinimalSurfaceSpectralNetwork` (line 138) - *Willmore minimal surface spectral network architecture.*
- `MinimalSurfaceOperator` (line 181) - *Analytical minimal surface operations for ground truth generation.*
- `SurfacePotentialGenerator` (line 237) - *Generate various surface potential configurations.*
- `MinimalSurfaceDataset` (line 298) - *Dataset for minimal surface evolution problems.*
- `WeightIntegrityCalculator` (line 374) - *Validate weight tensor integrity (NaN/Inf detection).*
- `DiscretizationCalculator` (line 410) - *Compute weight discretization metrics (delta, alpha).*
- `SpectralGeometryCalculator` (line 440) - *Compute spectral geometry properties of weight matrices.*
- `RicciCurvatureCalculator` (line 500) - *Compute Ricci curvature of weight space metric.*
- `WillmoreEnergyCalculator` (line 547) - *Compute Willmore energy and curvature metrics from weights.*
- `TopologicalPhaseDetector` (line 619) - *Detect topological phase state via Fourier mass center analysis.*
- `BerryPhaseCalculator` (line 709) - *Compute Berry phase from checkpoint trajectory.*
- `FunctionalTest` (line 787) - *Abstract base class for functional validation tests.*
- `AccuracyTest` (line 799) - *Test 1: Model accuracy on validation set.*
- `SurfaceReconstructionTest` (line 823) - *Test 2: Surface reconstruction quality via Willmore energy.*
- `GeneralizationTest` (line 866) - *Test 3: Generalization to unseen potential configurations.*
- `CheckpointAnalyzer` (line 900) - *Main analyzer orchestrating all metrics and functional tests.*
- `ComprehensiveVisualizer` (line 1035) - *Generate comprehensive visualization of all metrics.*
- `BatchProcessor` (line 1321) - *Process multiple checkpoints and find the best one.*

**Functions:**
- `setup_logging` (line 1444) - *Configure logging for the suite.*
- `main` (line 1452)
- `__init__` (line 95)
- `forward` (line 112)
- `__init__` (line 141)
- `forward` (line 160)
- `get_spectral_representation` (line 171) - *Extract spectral features for analysis.*
- `__init__` (line 184)
- `_precompute_spectral_operators` (line 188)
- `apply_laplacian` (line 196)
- `compute_mean_curvature` (line 201)
- `compute_gaussian_curvature` (line 212)
- `compute_willmore_energy` (line 223)
- `compute_surface_area` (line 229)
- `__init__` (line 240)
- `pyramid_potential` (line 244)
- `cube_potential` (line 251)
- `dodecahedron_potential` (line 258)
- `torus_potential` (line 266)
- `hyperbolic_potential` (line 274)
- `generate_mixed_potential` (line 282)
- `__init__` (line 301)
- `_generate_surface_pair` (line 331)
- `__len__` (line 364)
- `__getitem__` (line 367)
- `get_validation_batch` (line 370)
- `__init__` (line 377)
- `compute` (line 380)
- `__init__` (line 413)
- `compute` (line 416)
- `__init__` (line 443)
- `compute` (line 446)
- `__init__` (line 503)
- `compute` (line 506)
- `__init__` (line 550)
- `compute` (line 554)
- `_compute_surface_metrics` (line 575)
- `_empty_metrics` (line 605)
- `__init__` (line 622)
- `detect` (line 628)
- `__init__` (line 712)
- `load_checkpoints` (line 715)
- `_extract_epoch` (line 734)
- `flatten_spectral_kernels` (line 738)
- `calculate_berry_phase` (line 751)
- `__init__` (line 790)
- `run` (line 795)
- `run` (line 802)
- `__init__` (line 826)
- `run` (line 830)
- `run` (line 869)
- `__init__` (line 903)
- `analyze_checkpoint` (line 918)
- `_extract_spectral_field` (line 997)
- `_compute_health_score` (line 1012)
- `__init__` (line 1038)
- `visualize_analysis` (line 1041)
- `_plot_weight_integrity` (line 1067)
- `_plot_discretization` (line 1085)
- `_plot_spectral_geometry` (line 1111)
- `_plot_ricci_curvature` (line 1132)
- `_plot_functional_test_1` (line 1145)
- `_plot_functional_test_2` (line 1165)
- `_plot_functional_test_3` (line 1188)
- `_plot_health_summary` (line 1210)
- `_plot_layer_deltas` (line 1240)
- `_plot_phase_diagram` (line 1259)
- `_plot_crystal_verdict` (line 1279)
- `__init__` (line 1324)
- `process_directory` (line 1331)
- `_rank_checkpoints` (line 1381)
- `_generate_summary` (line 1407)

#### `willmore_zero_shot_scaler.py`
**Path:** `willmore_zero_shot_scaler.py`

**Classs:**
- `ScalerConfig` (line 115) - *Configuration dataclass for the zero-shot scaler.*
- `IConfigurationLoader` (line 144) - *Abstract interface for configuration loading.*
- `TOMLConfigurationLoader` (line 153) - *TOML-based configuration loader.*
- `ICheckpointManager` (line 207) - *Abstract interface for checkpoint management.*
- `WillmoreCheckpointManager` (line 221) - *Checkpoint manager for Willmore Crystal models.*
- `ISpectralWeightInterpolator` (line 260) - *Abstract interface for spectral weight interpolation.*
- `FourierSpectralInterpolator` (line 274) - *Fourier-based spectral weight interpolation.*
- `BilinearSpectralInterpolator` (line 387) - *Bilinear interpolation for spectral weights.*
- `IGridScaler` (line 445) - *Abstract interface for grid scaling.*
- `WillmoreGridScaler` (line 458) - *Grid scaler for Willmore Crystal networks.*
- `IMetricsEvaluator` (line 583) - *Abstract interface for metrics evaluation.*
- `WillmoreMetricsEvaluator` (line 597) - *Metrics evaluator for Willmore Crystal models.*
- `ScalingPipeline` (line 776) - *Orchestrates the complete progressive scaling process.*

**Functions:**
- `create_default_config_file` (line 1046) - *Create a default configuration file.*
- `build_argument_parser` (line 1053) - *Build the command-line argument parser.*
- `main` (line 1129) - *Main entry point for the zero-shot scaler.*
- `load` (line 148) - *Load configuration from the specified source.*
- `load` (line 156)
- `_from_toml` (line 161)
- `_from_dict` (line 170)
- `load_checkpoint` (line 211) - *Load a model checkpoint from disk.*
- `save_checkpoint` (line 216) - *Save a model checkpoint to disk.*
- `__init__` (line 224)
- `load_checkpoint` (line 228)
- `save_checkpoint` (line 246)
- `interpolate` (line 264) - *Interpolate spectral weights to a new shape.*
- `__init__` (line 277)
- `interpolate` (line 281)
- `_interpolate_2d_spectral` (line 294)
- `_interpolate_4d_spectral` (line 314)
- `_pad_spectrum_2d` (line 332)
- `_interpolate_generic` (line 369)
- `__init__` (line 390)
- `interpolate` (line 394)
- `_interpolate_generic` (line 419)
- `scale_model` (line 449) - *Scale a model to a new grid resolution.*
- `__init__` (line 461)
- `scale_model` (line 470)
- `_extract_hidden_dim` (line 495)
- `_extract_expansion_dim` (line 500)
- `_count_spectral_layers` (line 505)
- `_transfer_weights` (line 510)
- `_scale_spectral_kernel` (line 535)
- `_scale_conv_weight` (line 549)
- `_validate_weight_transfer` (line 570)
- `evaluate` (line 587) - *Evaluate model performance and metrics.*
- `__init__` (line 600)
- `evaluate` (line 606)
- `_construct_weight_surface` (line 639)
- `_compute_willmore_metrics` (line 661)
- `_compute_curvature_metrics` (line 677)
- `_compute_spectral_metrics` (line 702)
- `_evaluate_inference_quality` (line 735)
- `__init__` (line 779)
- `execute` (line 796)
- `_load_source_model` (line 888)
- `_log_metrics` (line 914)
- `_check_degradation` (line 930)
- `_is_better_metrics` (line 946)
- `_save_scaled_model` (line 961)
- `_compile_final_results` (line 971)
- `_save_final_results` (line 985)
- `_write_detailed_report` (line 997)

#### `wilmore_rbc.py`
**Path:** `wilmore_rbc.py`

**Classs:**
- `ReconstructionConfig` (line 37) - *Configuration for RBC reconstruction.*
- `SpectralLayer` (line 54) - *Spectral convolution layer for minimal surface processing.*
- `MinimalSurfaceSpectralNetwork` (line 88) - *Spectral network for minimal surface computation.*
- `CheckpointLoader` (line 123) - *Handles loading of model checkpoints.*
- `ModelBuilder` (line 133) - *Builds and initializes models from configuration.*
- `RBCMeshLoader` (line 172) - *Loads RBC mesh data from OpenRBC format files.*
- `ImprovedSphericalProjector` (line 198) - *Improved spherical projection with proper handling of biconcave geometry.

Key improvements:
1. Area-weighted averaging to avoid oversampling at poles
2. RBF interpolation for smooth reconstruction
3. Proper handling of the dimple regions
4. Gaussian smoothing in parameter space*
- `CylindricalProjector` (line 380) - *Cylindrical projection - often better for biconcave shapes.

The RBC is naturally more cylindrical than spherical,
with the dimples on top and bottom.*
- `SyntheticShapeGenerator` (line 472) - *Generates synthetic shapes for comparison.*
- `WillmoreMetricsCalculator` (line 517) - *Calculates Willmore energy and curvature metrics.*
- `SurfaceEvolver` (line 545) - *Evolves surfaces using the trained model with LR schedule and volume conservation.*
- `MeshExporter` (line 623) - *Exports meshes to various formats.*
- `RBCReconstructionPipeline` (line 791) - *Main pipeline for RBC reconstruction using scaled model.*

**Functions:**
- `build_argument_parser` (line 960)
- `main` (line 1046)
- `__init__` (line 57)
- `forward` (line 68)
- `__init__` (line 91)
- `forward` (line 112)
- `load` (line 127)
- `build` (line 137)
- `load_from_checkpoint` (line 148)
- `load` (line 176)
- `__init__` (line 209)
- `compute_vertex_areas` (line 217) - *Compute approximate area associated with each vertex.*
- `project_mesh` (line 232) - *Project mesh onto spherical grid with proper area weighting.*
- `_area_weighted_projection` (line 270) - *Project using area-weighted averaging.*
- `_rbf_interpolation` (line 303) - *Use RBF interpolation for smooth reconstruction.*
- `_apply_spherical_smoothing` (line 333) - *Apply Gaussian smoothing adapted to spherical coordinates.*
- `to_cartesian` (line 355) - *Convert spherical grid back to 3D vertices.*
- `__init__` (line 388)
- `project_mesh` (line 396) - *Project mesh using cylindrical coordinates.*
- `to_cartesian` (line 445) - *Convert cylindrical grid back to 3D vertices.*
- `__init__` (line 475)
- `create_sphere` (line 481)
- `create_biconcave` (line 484) - *Create biconcave disc shape using Evans-Fung model.*
- `create_evans_fung_rbc` (line 490) - *Create RBC shape using Evans-Fung parametrization.

The RBC cross-section follows:
r(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)

This creates the characteristic biconcave shape.*
- `__init__` (line 520)
- `compute_willmore` (line 523)
- `compute_curvature_stats` (line 527)
- `__init__` (line 548)
- `_compute_lr` (line 556) - *Compute learning rate with cosine schedule.*
- `_compute_volume` (line 567) - *Estimate volume from surface grid.*
- `_normalize_volume` (line 571) - *Normalize surface to preserve volume.*
- `evolve` (line 579)
- `save_obj` (line 627)
- `save_html_comparison` (line 636)
- `__init__` (line 794)
- `run` (line 805)

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
