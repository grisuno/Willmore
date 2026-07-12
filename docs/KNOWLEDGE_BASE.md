# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 15 | **Total Symbols Extracted:** 652 | **Total Imports:** 169

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
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
- `create_synthetic_rbc` (line 16) `def create_synthetic_rbc(n_vertices)` - *RBC sintético con forma bicóncava.*
- `spherical_projection` (line 44) `def spherical_projection(vertices, grid_size)` - *Proyección esférica - tiene problemas con dimples.*
- `cylindrical_projection` (line 76) `def cylindrical_projection(vertices, grid_size)` - *Proyección cilíndrica - NATURAL para RBC.

Coordenadas:
- z: altura (-z_max a +z_max)
- phi: ángulo azimutal (-π a π)
- rho: radio en el plano xy

El RBC es naturalmente cilíndrico: los dimples están en z=±z_max,
no en direcciones angulares.*
- `spherical_to_cartesian` (line 123) `def spherical_to_cartesian(r_grid, grid_size)` - *Convierte grilla esférica a 3D.*
- `cylindrical_to_cartesian` (line 144) `def cylindrical_to_cartesian(rho_grid, z_min, z_max, grid_size)` - *Convierte grilla cilíndrica a 3D.*
- `compute_metrics` (line 164) `def compute_metrics(r_grid, mask, original_r)` - *Computa métricas de calidad.*
- `save_obj` (line 181) `def save_obj(vertices, faces, filepath)`
- `main` (line 189) `def main()`

#### `model_Reco.py`
**Path:** `model_Reco.py`

**Functions:**
- `load_rbc_mesh` (line 27) `def load_rbc_mesh(vert_path, face_path)`
- `center_mesh` (line 49) `def center_mesh(vertices)`
- `cartesian_to_spherical` (line 54) `def cartesian_to_spherical(vertices)`
- `spherical_to_cartesian` (line 63) `def spherical_to_cartesian(r, theta, phi)`
- `evaluate_model_at_points` (line 70) `def evaluate_model_at_points(model, r_values, theta_values, phi_values, grid_size, device, r_global_mean)` - *Evalúa el modelo en puntos arbitrarios (no en grilla regular).

Estrategia: Para cada punto, encontrar su celda en la grilla 16x16,
evaluar el modelo en esa celda, y usar el valor como predicción.*
- `load_model` (line 134) `def load_model(checkpoint_path, device, config)`
- `compute_curvatures` (line 159) `def compute_curvatures(vertices, faces, grid_size)` - *Compute curvatures using the same operator as training.*
- `save_obj` (line 189) `def save_obj(vertices, faces, filepath)`
- `save_html_viewer` (line 197) `def save_html_viewer(orig_verts, orig_faces, pred_verts, pred_faces, output_path)`
- `main` (line 338) `def main()`

#### `rbc.py`
**Path:** `rbc.py`

**Functions:**
- `load_rbc_mesh` (line 30) `def load_rbc_mesh(vert_path, face_path)` - *Load RBC mesh from OpenRBC files.*
- `load_model` (line 53) `def load_model(checkpoint_path, device, config)` - *Load the trained Willmore model from checkpoint.*
- `project_rbc_to_spherical_grid` (line 94) `def project_rbc_to_spherical_grid(vertices, grid_size)` - *Project entire RBC mesh onto a spherical coordinate grid.

This creates a single grid_size x grid_size representation
that the model can process.*
- `spherical_grid_to_cartesian` (line 139) `def spherical_grid_to_cartesian(r_grid, grid_size, scale)` - *Convert spherical grid back to 3D vertices.*
- `run_model_evolution` (line 164) `def run_model_evolution(model, input_grid, steps, device)` - *Run model iteratively to evolve the surface.

Returns the evolution trajectory.*
- `create_sphere_grid` (line 202) `def create_sphere_grid(grid_size, radius)` - *Create a perfect sphere grid for comparison.*
- `create_biconcave_grid` (line 212) `def create_biconcave_grid(grid_size, radius)` - *Create a biconcave disc shape on spherical grid.*
- `compute_willmore_on_grid` (line 224) `def compute_willmore_on_grid(surface, grid_size)` - *Compute Willmore energy using MinimalSurfaceOperator.*
- `save_obj` (line 231) `def save_obj(vertices, faces, filepath)` - *Save mesh as OBJ file.*
- `save_html_comparison` (line 240) `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved_faces, sphere_vertices, sphere_faces, biconcave_vertices, biconcave_faces, willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave, output_path)` - *Create interactive HTML comparing all shapes.*
- `main` (line 393) `def main()`

#### `rbc_model_reconstruction (1).py`
**Path:** `rbc_model_reconstruction (1).py`

**Functions:**
- `load_rbc_mesh` (line 30) `def load_rbc_mesh(vert_path, face_path)` - *Load RBC mesh from OpenRBC files.*
- `load_model` (line 53) `def load_model(checkpoint_path, device, config)` - *Load the trained Willmore model from checkpoint.*
- `project_rbc_to_spherical_grid` (line 94) `def project_rbc_to_spherical_grid(vertices, grid_size)` - *Project entire RBC mesh onto a spherical coordinate grid.

This creates a single grid_size x grid_size representation
that the model can process.*
- `spherical_grid_to_cartesian` (line 139) `def spherical_grid_to_cartesian(r_grid, grid_size, scale)` - *Convert spherical grid back to 3D vertices.*
- `run_model_evolution` (line 164) `def run_model_evolution(model, input_grid, steps, device)` - *Run model iteratively to evolve the surface.

Returns the evolution trajectory.*
- `create_sphere_grid` (line 202) `def create_sphere_grid(grid_size, radius)` - *Create a perfect sphere grid for comparison.*
- `create_biconcave_grid` (line 212) `def create_biconcave_grid(grid_size, radius)` - *Create a biconcave disc shape on spherical grid.*
- `compute_willmore_on_grid` (line 224) `def compute_willmore_on_grid(surface, grid_size)` - *Compute Willmore energy using MinimalSurfaceOperator.*
- `save_obj` (line 231) `def save_obj(vertices, faces, filepath)` - *Save mesh as OBJ file.*
- `save_html_comparison` (line 240) `def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved_faces, sphere_vertices, sphere_faces, biconcave_vertices, biconcave_faces, willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave, output_path)` - *Create interactive HTML comparing all shapes.*
- `main` (line 393) `def main()`

#### `rbc_model_reconstruction.py`
**Path:** `rbc_model_reconstruction.py`

**Functions:**
- `load_rbc_mesh` (line 31) `def load_rbc_mesh(vert_path, face_path)` - *Load RBC mesh from OpenRBC files.*
- `compute_vertex_normals` (line 54) `def compute_vertex_normals(vertices, faces)` - *Compute vertex normals.*
- `compute_face_areas` (line 75) `def compute_face_areas(vertices, faces)` - *Compute face areas.*
- `load_model` (line 84) `def load_model(checkpoint_path, device, config)` - *Load the trained Willmore model from checkpoint.*
- `create_local_patches_for_vertices` (line 124) `def create_local_patches_for_vertices(vertices, faces, normals, grid_size)` - *Create local surface patches around each vertex for model input.

For each vertex, we create a small 2D grid representing the local
surface neighborhood, which can be processed by the model.*
- `run_model_on_patches` (line 215) `def run_model_on_patches(model, patches_real, patches_imag, device, grid_size, batch_size)` - *Run the model on all vertex patches and extract predictions.

Returns predicted curvature-like values for each vertex.*
- `compute_analytical_curvature` (line 252) `def compute_analytical_curvature(vertices, faces)` - *Compute analytical mean curvature for comparison.*
- `save_ply_with_values` (line 284) `def save_ply_with_values(vertices, faces, normals, values, filepath, value_name)` - *Save mesh as PLY with scalar values as vertex colors.*
- `save_html_viewer` (line 319) `def save_html_viewer(vertices, faces, normals, model_curvature, analytical_curvature, output_path)` - *Create interactive HTML viewer with model predictions on actual RBC mesh.*
- `main` (line 530) `def main()`

#### `rbc_model_reconstruction_128.py`
**Path:** `rbc_model_reconstruction_128.py`

**Classes:**
- `ReconstructionConfig` (line 37) `class ReconstructionConfig` - *Configuration for RBC reconstruction.*
- `SpectralLayer` (line 51) `class SpectralLayer` - *Spectral convolution layer for minimal surface processing.*
- `MinimalSurfaceSpectralNetwork` (line 85) `class MinimalSurfaceSpectralNetwork` - *Spectral network for minimal surface computation.*
- `CheckpointLoader` (line 120) `class CheckpointLoader` - *Handles loading of model checkpoints.*
- `ModelBuilder` (line 130) `class ModelBuilder` - *Builds and initializes models from configuration.*
- `RBCMeshLoader` (line 169) `class RBCMeshLoader` - *Loads RBC mesh data from OpenRBC format files.*
- `ImprovedSphericalProjector` (line 195) `class ImprovedSphericalProjector` - *Improved spherical projection with proper handling of biconcave geometry.

Key improvements:
1. Area-weighted averaging to avoid oversampling at poles
2. RBF interpolation for smooth reconstruction
3. Proper handling of the dimple regions
4. Gaussian smoothing in parameter space*
- `CylindricalProjector` (line 377) `class CylindricalProjector` - *Cylindrical projection - often better for biconcave shapes.

The RBC is naturally more cylindrical than spherical,
with the dimples on top and bottom.*
- `SyntheticShapeGenerator` (line 469) `class SyntheticShapeGenerator` - *Generates synthetic shapes for comparison.*
- `WillmoreMetricsCalculator` (line 514) `class WillmoreMetricsCalculator` - *Calculates Willmore energy and curvature metrics.*
- `SurfaceEvolver` (line 542) `class SurfaceEvolver` - *Evolves surfaces using the trained model.*
- `MeshExporter` (line 589) `class MeshExporter` - *Exports meshes to various formats.*
- `RBCReconstructionPipeline` (line 757) `class RBCReconstructionPipeline` - *Main pipeline for RBC reconstruction using scaled model.*

**Functions:**
- `build_argument_parser` (line 926) `def build_argument_parser()`
- `main` (line 989) `def main()`
- `__init__` (line 54) `def __init__(self, channels, grid_size)`
- `forward` (line 65) `def forward(self, x)`
- `__init__` (line 88) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- `forward` (line 109) `def forward(self, x)`
- `load` (line 124) `def load(checkpoint_path, device)`
- `build` (line 134) `def build(config)`
- `load_from_checkpoint` (line 145) `def load_from_checkpoint(checkpoint_path, config)`
- `load` (line 173) `def load(vert_path, face_path)`
- `__init__` (line 206) `def __init__(self, grid_size, smoothing_sigma)`
- `compute_vertex_areas` (line 214) `def compute_vertex_areas(self, vertices, faces)` - *Compute approximate area associated with each vertex.*
- `project_mesh` (line 229) `def project_mesh(self, vertices, faces, use_rbf)` - *Project mesh onto spherical grid with proper area weighting.*
- `_area_weighted_projection` (line 267) `def _area_weighted_projection(self, theta, phi, r, areas)` - *Project using area-weighted averaging.*
- `_rbf_interpolation` (line 300) `def _rbf_interpolation(self, theta, phi, r)` - *Use RBF interpolation for smooth reconstruction.*
- `_apply_spherical_smoothing` (line 330) `def _apply_spherical_smoothing(self, r_grid)` - *Apply Gaussian smoothing adapted to spherical coordinates.*
- `to_cartesian` (line 352) `def to_cartesian(self, r_grid, scale)` - *Convert spherical grid back to 3D vertices.*
- `__init__` (line 385) `def __init__(self, grid_size, smoothing_sigma)`
- `project_mesh` (line 393) `def project_mesh(self, vertices, faces)` - *Project mesh using cylindrical coordinates.*
- `to_cartesian` (line 442) `def to_cartesian(self, rho_grid, z_scale, rho_scale)` - *Convert cylindrical grid back to 3D vertices.*
- `__init__` (line 472) `def __init__(self, grid_size)`
- `create_sphere` (line 478) `def create_sphere(self, radius)`
- `create_biconcave` (line 481) `def create_biconcave(self, radius, dimple_depth)` - *Create biconcave disc shape using Evans-Fung model.*
- `create_evans_fung_rbc` (line 487) `def create_evans_fung_rbc(self, radius, dimple_depth, thickness)` - *Create RBC shape using Evans-Fung parametrization.

The RBC cross-section follows:
r(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)

This creates the characteristic biconcave shape.*
- `__init__` (line 517) `def __init__(self, grid_size)`
- `compute_willmore` (line 520) `def compute_willmore(self, surface)`
- `compute_curvature_stats` (line 524) `def compute_curvature_stats(self, surface)`
- `__init__` (line 545) `def __init__(self, model, config)`
- `evolve` (line 553) `def evolve(self, initial_surface)`
- `save_obj` (line 593) `def save_obj(vertices, faces, filepath)`
- `save_html_comparison` (line 602) `def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolved_faces, biconcave_vertices, biconcave_faces, metrics, output_path)`
- `__init__` (line 760) `def __init__(self, config)`
- `run` (line 771) `def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)`

#### `rbc_willmore_analysis.py`
**Path:** `rbc_willmore_analysis.py`

**Classes:**
- `RBCAnalysisConfig` (line 55) `class RBCAnalysisConfig` - *Configuration container for RBC Willmore analysis.

This dataclass holds all configuration parameters for the analysis
pipeline, including mesh processing, model loading, and visualization
settings.*
- `ILogger` (line 102) `class ILogger(ABC)` - *Abstract interface for logging implementations.*
- `StandardLogger` (line 122) `class StandardLogger(ILogger)` - *Standard logging implementation using Python logging module.*
- `IFileSystem` (line 149) `class IFileSystem(ABC)` - *Abstract interface for file system operations.*
- `StandardFileSystem` (line 169) `class StandardFileSystem(IFileSystem)` - *Standard file system implementation.*
- `MeshData` (line 188) `class MeshData` - *Container for 3D mesh data.

Attributes:
    vertices: Nx3 numpy array of vertex positions
    faces: Mx3 numpy array of triangle face indices
    bonds: Kx2 numpy array of bond edge indices
    normals: Nx3 numpy array of vertex normals (computed)
    areas: M numpy array of face areas (computed)*
- `IMeshLoader` (line 228) `class IMeshLoader(ABC)` - *Abstract interface for mesh loading implementations.*
- `OpenRBCMeshLoader` (line 236) `class OpenRBCMeshLoader(IMeshLoader)` - *Mesh loader for OpenRBC format data files.

OpenRBC stores mesh data in three separate text files:
- rbc.vert.txt: Vertex positions (x, y, z per line)
- rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)
- rbc.bond.txt: Bond edges (2 vertex indices per line)*
- `SyntheticMeshGenerator` (line 375) `class SyntheticMeshGenerator` - *Generator for synthetic comparison surfaces.

Creates reference surfaces (sphere, torus) for comparison with
RBC morphology analysis.*
- `ICurvatureCalculator` (line 545) `class ICurvatureCalculator(ABC)` - *Abstract interface for curvature calculation implementations.*
- `DiscreteCurvatureCalculator` (line 563) `class DiscreteCurvatureCalculator(ICurvatureCalculator)` - *Discrete curvature calculation using the cotangent formula.

Implements the discrete differential geometry approach for computing
mean and Gaussian curvature on triangle meshes based on the work by
Meyer et al. (2003) and others.

The mean curvature at a vertex is computed using the Laplace-Beltrami
operator applied to the vertex positions:

    H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)

where A_i is the Voronoi area around vertex i.*
- `SpectralLayer` (line 799) `class SpectralLayer` - *Spectral convolution layer for surface processing.

Implements convolution in the frequency domain using FFT,
allowing the network to learn global surface patterns.*
- `MinimalSurfaceSpectralNetwork` (line 848) `class MinimalSurfaceSpectralNetwork` - *Neural network for minimal surface detection and Willmore energy learning.

This network learns to predict mean curvature fields and identify
minimal surface configurations through spectral convolution layers.*
- `IModelLoader` (line 894) `class IModelLoader(ABC)` - *Abstract interface for model loading implementations.*
- `CheckpointModelLoader` (line 902) `class CheckpointModelLoader(IModelLoader)` - *Model loader that loads from PyTorch checkpoint files.*
- `SurfaceAnalysisEngine` (line 1002) `class SurfaceAnalysisEngine` - *Main engine for RBC surface analysis using Willmore energy model.

This class orchestrates the complete analysis pipeline, from mesh loading
to curvature computation and shape emergence testing.*

**Functions:**
- `parse_arguments` (line 1376) `def parse_arguments()`
- `create_config_from_args` (line 1470) `def create_config_from_args(args)`
- `main` (line 1488) `def main()`
- `info` (line 106) `def info(self, message)`
- `warning` (line 110) `def warning(self, message)`
- `error` (line 114) `def error(self, message)`
- `debug` (line 118) `def debug(self, message)`
- `__init__` (line 125) `def __init__(self, name, level)`
- `info` (line 136) `def info(self, message)`
- `warning` (line 139) `def warning(self, message)`
- `error` (line 142) `def error(self, message)`
- `debug` (line 145) `def debug(self, message)`
- `exists` (line 153) `def exists(self, path)`
- `read_text` (line 157) `def read_text(self, path)`
- `write_text` (line 161) `def write_text(self, path, content)`
- `makedirs` (line 165) `def makedirs(self, path)`
- `exists` (line 172) `def exists(self, path)`
- `read_text` (line 175) `def read_text(self, path)`
- `write_text` (line 179) `def write_text(self, path, content)`
- `makedirs` (line 183) `def makedirs(self, path)`
- `num_vertices` (line 206) `def num_vertices(self)`
- `num_faces` (line 210) `def num_faces(self)`
- `num_bonds` (line 214) `def num_bonds(self)`
- `to_dict` (line 217) `def to_dict(self)`
- `load` (line 232) `def load(self, vert_path, face_path, bond_path)`
- `__init__` (line 245) `def __init__(self, filesystem, logger)`
- `load` (line 249) `def load(self, vert_path, face_path, bond_path)`
- `_load_vertices` (line 267) `def _load_vertices(self, path)`
- `_load_faces` (line 286) `def _load_faces(self, path)`
- `_load_bonds` (line 308) `def _load_bonds(self, path)`
- `_compute_normals` (line 330) `def _compute_normals(self, mesh)`
- `_compute_areas` (line 355) `def _compute_areas(self, mesh)`
- `__init__` (line 382) `def __init__(self, logger)`
- `generate_sphere` (line 385) `def generate_sphere(self, radius, resolution)`
- `generate_torus` (line 424) `def generate_torus(self, R, r, resolution)`
- `generate_biconcave_disc` (line 467) `def generate_biconcave_disc(self, radius, thickness, resolution)`
- `_compute_mesh_properties` (line 511) `def _compute_mesh_properties(self, mesh)`
- `compute_mean_curvature` (line 549) `def compute_mean_curvature(self, mesh)`
- `compute_gaussian_curvature` (line 553) `def compute_gaussian_curvature(self, mesh)`
- `compute_willmore_energy` (line 557) `def compute_willmore_energy(self, mesh, mean_curvature)`
- `__init__` (line 578) `def __init__(self, logger)`
- `compute_mean_curvature` (line 581) `def compute_mean_curvature(self, mesh)`
- `compute_gaussian_curvature` (line 616) `def compute_gaussian_curvature(self, mesh)`
- `compute_willmore_energy` (line 664) `def compute_willmore_energy(self, mesh, mean_curvature)`
- `_compute_edge_cotangents` (line 682) `def _compute_edge_cotangents(self, mesh)`
- `_get_vertex_neighbors` (line 737) `def _get_vertex_neighbors(self, vertex_idx, faces)`
- `_compute_mixed_voronoi_area` (line 748) `def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)`
- `__init__` (line 806) `def __init__(self, channels, grid_size)`
- `forward` (line 820) `def forward(self, x)`
- `__init__` (line 855) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- `forward` (line 880) `def forward(self, x)`
- `load` (line 898) `def load(self, checkpoint_path, device, config)`
- `__init__` (line 905) `def __init__(self, filesystem, logger)`
- `_detect_model_params` (line 909) `def _detect_model_params(self, state_dict)`
- `load` (line 947) `def load(self, checkpoint_path, device, config)`
- `__init__` (line 1009) `def __init__(self, config, logger, filesystem)`
- `initialize` (line 1028) `def initialize(self)`
- `_load_rbc_mesh` (line 1048) `def _load_rbc_mesh(self)`
- `_generate_synthetic_meshes` (line 1060) `def _generate_synthetic_meshes(self)`
- `analyze_mesh` (line 1076) `def analyze_mesh(self, mesh, name)`
- `_compute_surface_area` (line 1125) `def _compute_surface_area(self, mesh)`
- `_compute_volume` (line 1130) `def _compute_volume(self, mesh)`
- `_compute_asphericity` (line 1141) `def _compute_asphericity(self, mesh)`
- `_compute_biconcavity_index` (line 1161) `def _compute_biconcavity_index(self, mesh, mean_curvature)`
- `_compute_histogram` (line 1186) `def _compute_histogram(self, data, bins)`
- `run_shape_emergence_test` (line 1192) `def run_shape_emergence_test(self)`
- `_analyze_rbc_morphology` (line 1235) `def _analyze_rbc_morphology(self)`
- `_verify_gauss_bonnet` (line 1277) `def _verify_gauss_bonnet(self)`
- `run_mean_curvature_flow` (line 1318) `def run_mean_curvature_flow(self, mesh, steps, dt)`
- `save_results` (line 1357) `def save_results(self, results, filename)`
- `save_mesh_obj` (line 1362) `def save_mesh_obj(self, mesh, filename)`

#### `rbc_willmore_analysis2.py`
**Path:** `rbc_willmore_analysis2.py`

**Classes:**
- `RBCAnalysisConfig` (line 55) `class RBCAnalysisConfig` - *Configuration container for RBC Willmore analysis.

This dataclass holds all configuration parameters for the analysis
pipeline, including mesh processing, model loading, and visualization
settings.*
- `ILogger` (line 102) `class ILogger(ABC)` - *Abstract interface for logging implementations.*
- `StandardLogger` (line 122) `class StandardLogger(ILogger)` - *Standard logging implementation using Python logging module.*
- `IFileSystem` (line 149) `class IFileSystem(ABC)` - *Abstract interface for file system operations.*
- `StandardFileSystem` (line 169) `class StandardFileSystem(IFileSystem)` - *Standard file system implementation.*
- `MeshData` (line 188) `class MeshData` - *Container for 3D mesh data.

Attributes:
    vertices: Nx3 numpy array of vertex positions
    faces: Mx3 numpy array of triangle face indices
    bonds: Kx2 numpy array of bond edge indices
    normals: Nx3 numpy array of vertex normals (computed)
    areas: M numpy array of face areas (computed)*
- `IMeshLoader` (line 228) `class IMeshLoader(ABC)` - *Abstract interface for mesh loading implementations.*
- `OpenRBCMeshLoader` (line 236) `class OpenRBCMeshLoader(IMeshLoader)` - *Mesh loader for OpenRBC format data files.

OpenRBC stores mesh data in three separate text files:
- rbc.vert.txt: Vertex positions (x, y, z per line)
- rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)
- rbc.bond.txt: Bond edges (2 vertex indices per line)*
- `SyntheticMeshGenerator` (line 375) `class SyntheticMeshGenerator` - *Generator for synthetic comparison surfaces.

Creates reference surfaces (sphere, torus) for comparison with
RBC morphology analysis.*
- `ICurvatureCalculator` (line 545) `class ICurvatureCalculator(ABC)` - *Abstract interface for curvature calculation implementations.*
- `DiscreteCurvatureCalculator` (line 563) `class DiscreteCurvatureCalculator(ICurvatureCalculator)` - *Discrete curvature calculation using the cotangent formula.

Implements the discrete differential geometry approach for computing
mean and Gaussian curvature on triangle meshes based on the work by
Meyer et al. (2003) and others.

The mean curvature at a vertex is computed using the Laplace-Beltrami
operator applied to the vertex positions:

    H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)

where A_i is the Voronoi area around vertex i.*
- `SpectralLayer` (line 799) `class SpectralLayer` - *Spectral convolution layer for surface processing.

Implements convolution in the frequency domain using FFT,
allowing the network to learn global surface patterns.*
- `MinimalSurfaceSpectralNetwork` (line 848) `class MinimalSurfaceSpectralNetwork` - *Neural network for minimal surface detection and Willmore energy learning.

This network learns to predict mean curvature fields and identify
minimal surface configurations through spectral convolution layers.*
- `IModelLoader` (line 894) `class IModelLoader(ABC)` - *Abstract interface for model loading implementations.*
- `CheckpointModelLoader` (line 902) `class CheckpointModelLoader(IModelLoader)` - *Model loader that loads from PyTorch checkpoint files.*
- `SurfaceAnalysisEngine` (line 1002) `class SurfaceAnalysisEngine` - *Main engine for RBC surface analysis using Willmore energy model.

This class orchestrates the complete analysis pipeline, from mesh loading
to curvature computation and shape emergence testing.*

**Functions:**
- `parse_arguments` (line 1394) `def parse_arguments()`
- `create_config_from_args` (line 1488) `def create_config_from_args(args)`
- `main` (line 1506) `def main()`
- `info` (line 106) `def info(self, message)`
- `warning` (line 110) `def warning(self, message)`
- `error` (line 114) `def error(self, message)`
- `debug` (line 118) `def debug(self, message)`
- `__init__` (line 125) `def __init__(self, name, level)`
- `info` (line 136) `def info(self, message)`
- `warning` (line 139) `def warning(self, message)`
- `error` (line 142) `def error(self, message)`
- `debug` (line 145) `def debug(self, message)`
- `exists` (line 153) `def exists(self, path)`
- `read_text` (line 157) `def read_text(self, path)`
- `write_text` (line 161) `def write_text(self, path, content)`
- `makedirs` (line 165) `def makedirs(self, path)`
- `exists` (line 172) `def exists(self, path)`
- `read_text` (line 175) `def read_text(self, path)`
- `write_text` (line 179) `def write_text(self, path, content)`
- `makedirs` (line 183) `def makedirs(self, path)`
- `num_vertices` (line 206) `def num_vertices(self)`
- `num_faces` (line 210) `def num_faces(self)`
- `num_bonds` (line 214) `def num_bonds(self)`
- `to_dict` (line 217) `def to_dict(self)`
- `load` (line 232) `def load(self, vert_path, face_path, bond_path)`
- `__init__` (line 245) `def __init__(self, filesystem, logger)`
- `load` (line 249) `def load(self, vert_path, face_path, bond_path)`
- `_load_vertices` (line 267) `def _load_vertices(self, path)`
- `_load_faces` (line 286) `def _load_faces(self, path)`
- `_load_bonds` (line 308) `def _load_bonds(self, path)`
- `_compute_normals` (line 330) `def _compute_normals(self, mesh)`
- `_compute_areas` (line 355) `def _compute_areas(self, mesh)`
- `__init__` (line 382) `def __init__(self, logger)`
- `generate_sphere` (line 385) `def generate_sphere(self, radius, resolution)`
- `generate_torus` (line 424) `def generate_torus(self, R, r, resolution)`
- `generate_biconcave_disc` (line 467) `def generate_biconcave_disc(self, radius, thickness, resolution)`
- `_compute_mesh_properties` (line 511) `def _compute_mesh_properties(self, mesh)`
- `compute_mean_curvature` (line 549) `def compute_mean_curvature(self, mesh)`
- `compute_gaussian_curvature` (line 553) `def compute_gaussian_curvature(self, mesh)`
- `compute_willmore_energy` (line 557) `def compute_willmore_energy(self, mesh, mean_curvature)`
- `__init__` (line 578) `def __init__(self, logger)`
- `compute_mean_curvature` (line 581) `def compute_mean_curvature(self, mesh)`
- `compute_gaussian_curvature` (line 616) `def compute_gaussian_curvature(self, mesh)`
- `compute_willmore_energy` (line 664) `def compute_willmore_energy(self, mesh, mean_curvature)`
- `_compute_edge_cotangents` (line 682) `def _compute_edge_cotangents(self, mesh)`
- `_get_vertex_neighbors` (line 737) `def _get_vertex_neighbors(self, vertex_idx, faces)`
- `_compute_mixed_voronoi_area` (line 748) `def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)`
- `__init__` (line 806) `def __init__(self, channels, grid_size)`
- `forward` (line 820) `def forward(self, x)`
- `__init__` (line 855) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- `forward` (line 880) `def forward(self, x)`
- `load` (line 898) `def load(self, checkpoint_path, device, config)`
- `__init__` (line 905) `def __init__(self, filesystem, logger)`
- `_detect_model_params` (line 909) `def _detect_model_params(self, state_dict)`
- `load` (line 947) `def load(self, checkpoint_path, device, config)`
- `__init__` (line 1009) `def __init__(self, config, logger, filesystem)`
- `initialize` (line 1028) `def initialize(self)`
- `_load_rbc_mesh` (line 1048) `def _load_rbc_mesh(self)`
- `_generate_synthetic_meshes` (line 1060) `def _generate_synthetic_meshes(self)`
- `analyze_mesh` (line 1076) `def analyze_mesh(self, mesh, name)`
- `_compute_surface_area` (line 1125) `def _compute_surface_area(self, mesh)`
- `_compute_volume` (line 1130) `def _compute_volume(self, mesh)`
- `_compute_asphericity` (line 1141) `def _compute_asphericity(self, mesh)`
- `_compute_biconcavity_index` (line 1161) `def _compute_biconcavity_index(self, mesh, mean_curvature)`
- `_compute_histogram` (line 1186) `def _compute_histogram(self, data, bins)`
- `run_shape_emergence_test` (line 1192) `def run_shape_emergence_test(self)`
- `_analyze_rbc_morphology` (line 1235) `def _analyze_rbc_morphology(self)`
- `_verify_gauss_bonnet` (line 1277) `def _verify_gauss_bonnet(self)`
- `run_mean_curvature_flow` (line 1318) `def run_mean_curvature_flow(self, mesh, steps, dt)`
- `save_results` (line 1357) `def save_results(self, results, filename)`
- `save_mesh_obj` (line 1380) `def save_mesh_obj(self, mesh, filename)`
- `convert_to_native` (line 1360) `def convert_to_native(obj)`

#### `test.py`
**Path:** `test.py`

**Functions:**
- `load_model` (line 20) `def load_model(checkpoint_path, device)`
- `test_model_behavior` (line 45) `def test_model_behavior(model, config, device)` - *Test que respeta la escala pequeña del modelo.*
- `main` (line 154) `def main()`

#### `willmore_crsital2.py`
**Path:** `willmore_crsital2.py`

**Classes:**
- `Config` (line 53) `class Config`
- `IPhaseDetector` (line 201) `class IPhaseDetector(ABC)`
- `IMetricCalculator` (line 207) `class IMetricCalculator(ABC)`
- `SeedManager` (line 213) `class SeedManager`
- `LoggerFactory` (line 227) `class LoggerFactory`
- `MinimalSurfaceOperator` (line 242) `class MinimalSurfaceOperator`
- `SpectralLayer` (line 307) `class SpectralLayer`
- `MinimalSurfaceBackbone` (line 331) `class MinimalSurfaceBackbone`
- `MinimalSurfaceInferenceEngine` (line 351) `class MinimalSurfaceInferenceEngine`
- `SurfacePotentialGenerator` (line 399) `class SurfacePotentialGenerator`
- `MinimalSurfaceDataset` (line 452) `class MinimalSurfaceDataset(Dataset)`
- `MinimalSurfaceSpectralNetwork` (line 539) `class MinimalSurfaceSpectralNetwork`
- `WillmoreEnergyCalculator` (line 567) `class WillmoreEnergyCalculator(IMetricCalculator)`
- `RicciFlowCalculator` (line 622) `class RicciFlowCalculator(IMetricCalculator)`
- `FullFourierAnalyzer` (line 668) `class FullFourierAnalyzer`
- `FourierMassCenterAnalyzer` (line 711) `class FourierMassCenterAnalyzer`
- `TopologicalPhaseDetector` (line 751) `class TopologicalPhaseDetector(IPhaseDetector)`
- `SpectralFieldExtractor` (line 780) `class SpectralFieldExtractor`
- `TopologicalMetricsCalculator` (line 798) `class TopologicalMetricsCalculator(IMetricCalculator)`
- `LocalComplexityAnalyzer` (line 818) `class LocalComplexityAnalyzer`
- `SuperpositionAnalyzer` (line 833) `class SuperpositionAnalyzer`
- `CrystallographyMetricsCalculator` (line 851) `class CrystallographyMetricsCalculator(IMetricCalculator)`
- `ThermodynamicMetricsCalculator` (line 965) `class ThermodynamicMetricsCalculator(IMetricCalculator)`
- `SpectralGeometryCalculator` (line 1021) `class SpectralGeometryCalculator(IMetricCalculator)`
- `RicciCurvatureCalculator` (line 1044) `class RicciCurvatureCalculator(IMetricCalculator)`
- `SpectroscopyMetricsCalculator` (line 1065) `class SpectroscopyMetricsCalculator(IMetricCalculator)`
- `LambdaPressureScheduler` (line 1082) `class LambdaPressureScheduler`
- `AdaptiveLambdaScheduler` (line 1114) `class AdaptiveLambdaScheduler(LambdaPressureScheduler)`
- `QuadruplePrecisionLambdaScheduler` (line 1129) `class QuadruplePrecisionLambdaScheduler`
- `AnnealingScheduler` (line 1161) `class AnnealingScheduler`
- `TopologicalAnnealingScheduler` (line 1186) `class TopologicalAnnealingScheduler(AnnealingScheduler)`
- `TrainingMetricsMonitor` (line 1202) `class TrainingMetricsMonitor`
- `CheckpointManager` (line 1261) `class CheckpointManager`
- `Phase5CheckpointManager` (line 1291) `class Phase5CheckpointManager`
- `WeightIntegrityChecker` (line 1322) `class WeightIntegrityChecker`
- `TrainingEngine` (line 1338) `class TrainingEngine`
- `BatchSizeProspector` (line 1447) `class BatchSizeProspector`
- `SeedMiner` (line 1483) `class SeedMiner`
- `FullTrainingOrchestrator` (line 1533) `class FullTrainingOrchestrator`
- `RefinementOrchestrator` (line 1599) `class RefinementOrchestrator`
- `Phase5Orchestrator` (line 1663) `class Phase5Orchestrator`
- `ExperimentOrchestrator` (line 1725) `class ExperimentOrchestrator`

**Functions:**
- `build_argument_parser` (line 1839) `def build_argument_parser()`
- `main` (line 1868) `def main()`
- `detect` (line 203) `def detect(self, spectral_field)`
- `compute` (line 209) `def compute(self, model)`
- `set_seed` (line 215) `def set_seed(seed, device)`
- `create_logger` (line 229) `def create_logger(name, level)`
- `__init__` (line 243) `def __init__(self, grid_size)`
- `_precompute_spectral_operators` (line 249) `def _precompute_spectral_operators(self)`
- `apply_laplacian` (line 257) `def apply_laplacian(self, field)`
- `compute_mean_curvature` (line 262) `def compute_mean_curvature(self, surface)`
- `compute_gaussian_curvature` (line 273) `def compute_gaussian_curvature(self, surface)`
- `compute_willmore_energy` (line 284) `def compute_willmore_energy(self, surface)`
- `compute_surface_area` (line 290) `def compute_surface_area(self, surface)`
- `mean_curvature_flow` (line 297) `def mean_curvature_flow(self, surface, dt)`
- `__init__` (line 308) `def __init__(self, channels, grid_size)`
- `forward` (line 315) `def forward(self, x)`
- `__init__` (line 332) `def __init__(self, grid_size, hidden_dim, num_spectral_layers)`
- `forward` (line 342) `def forward(self, x)`
- `__init__` (line 352) `def __init__(self, config)`
- `_try_load_backbone` (line 359) `def _try_load_backbone(self)`
- `apply_mean_curvature` (line 382) `def apply_mean_curvature(self, surface)`
- `mean_curvature_evolve` (line 388) `def mean_curvature_evolve(self, surface, dt)`
- `__init__` (line 400) `def __init__(self, config)`
- `pyramid_potential` (line 404) `def pyramid_potential(self)`
- `cube_potential` (line 411) `def cube_potential(self)`
- `dodecahedron_potential` (line 418) `def dodecahedron_potential(self)`
- `torus_potential` (line 426) `def torus_potential(self)`
- `hyperbolic_potential` (line 434) `def hyperbolic_potential(self)`
- `generate_mixed_potential` (line 442) `def generate_mixed_potential(self, seed)`
- `__init__` (line 453) `def __init__(self, config, surface_engine, seed)`
- `_solve_minimal_surface` (line 487) `def _solve_minimal_surface(self, potential, sample_seed)`
- `_evolve_minimal_surface` (line 513) `def _evolve_minimal_surface(self, surface_real, surface_imag, potential, energy)`
- `__len__` (line 534) `def __len__(self)`
- `__getitem__` (line 535) `def __getitem__(self, idx)`
- `get_validation_batch` (line 536) `def get_validation_batch(self)`
- `__init__` (line 540) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- `forward` (line 557) `def forward(self, x)`
- `__init__` (line 568) `def __init__(self, config)`
- `compute` (line 573) `def compute(self, model)`
- `compute_surface_metrics` (line 590) `def compute_surface_metrics(self, surface)`
- `_empty_metrics` (line 618) `def _empty_metrics()`
- `__init__` (line 623) `def __init__(self, config)`
- `compute` (line 627) `def compute(self, model)`
- `_compute_ricci_scalar` (line 640) `def _compute_ricci_scalar(self, metric)`
- `_estimate_sectional_curvatures` (line 647) `def _estimate_sectional_curvatures(self, metric)`
- `_compute_flow_velocity` (line 659) `def _compute_flow_velocity(self, metric)`
- `_empty_metrics` (line 664) `def _empty_metrics()`
- `__init__` (line 669) `def __init__(self, config)`
- `compute_full_spectrum` (line 677) `def compute_full_spectrum(self, spectral_field)`
- `compute_resonance_metrics` (line 701) `def compute_resonance_metrics(self, spectral_field)`
- `__init__` (line 712) `def __init__(self, config)`
- `_get_freq_grids` (line 720) `def _get_freq_grids(self, H, W, device)`
- `compute_mass_center` (line 728) `def compute_mass_center(self, spectral_field)`
- `__init__` (line 752) `def __init__(self, config)`
- `detect` (line 759) `def detect(self, spectral_field)`
- `extract` (line 782) `def extract(model, grid_size)`
- `__init__` (line 799) `def __init__(self, config)`
- `compute` (line 804) `def compute(self, model)`
- `_empty_metrics` (line 814) `def _empty_metrics()`
- `compute_local_complexity` (line 820) `def compute_local_complexity(weights, epsilon)`
- `compute_superposition` (line 835) `def compute_superposition(weights)`
- `__init__` (line 852) `def __init__(self, config)`
- `compute` (line 856) `def compute(self, model)`
- `compute_kappa` (line 861) `def compute_kappa(self, model, val_x, val_y, num_batches)`
- `compute_discretization_margin` (line 903) `def compute_discretization_margin(self, model)`
- `compute_alpha_purity` (line 911) `def compute_alpha_purity(self, model)`
- `compute_kappa_quantum` (line 916) `def compute_kappa_quantum(self, model)`
- `compute_poynting_vector` (line 935) `def compute_poynting_vector(self, model)`
- `compute_hbar_effective` (line 946) `def compute_hbar_effective(self, model, lambda_pressure)`
- `compute_all_metrics` (line 953) `def compute_all_metrics(self, model, val_x, val_y)`
- `__init__` (line 966) `def __init__(self, config)`
- `compute` (line 969) `def compute(self, model)`
- `compute_effective_temperature` (line 983) `def compute_effective_temperature(self, gradient_buffer, learning_rate)`
- `compute_specific_heat` (line 1001) `def compute_specific_heat(self, loss_history, temp_history)`
- `compute_gibbs_free_energy` (line 1010) `def compute_gibbs_free_energy(self, delta, alpha, temperature)`
- `compute_critical_temperature` (line 1017) `def compute_critical_temperature(self, alpha)`
- `__init__` (line 1022) `def __init__(self, config)`
- `compute` (line 1025) `def compute(self, model)`
- `__init__` (line 1045) `def __init__(self, config)`
- `compute` (line 1048) `def compute(self, model)`
- `__init__` (line 1066) `def __init__(self, config)`
- `compute` (line 1069) `def compute(self, model)`
- `__init__` (line 1083) `def __init__(self, config)`
- `current_lambda` (line 1092) `def current_lambda(self)`
- `step` (line 1095) `def step(self, epoch)`
- `compute_regularization_loss` (line 1102) `def compute_regularization_loss(self, model)`
- `set_lambda` (line 1110) `def set_lambda(self, value)`
- `__init__` (line 1115) `def __init__(self, config)`
- `step_adaptive` (line 1120) `def step_adaptive(self, epoch, topo_phase_state)`
- `__init__` (line 1130) `def __init__(self, config)`
- `current_lambda` (line 1139) `def current_lambda(self)`
- `step` (line 1142) `def step(self, epoch, improvement)`
- `compute_regularization_loss` (line 1149) `def compute_regularization_loss(self, model)`
- `set_lambda` (line 1157) `def set_lambda(self, value)`
- `__init__` (line 1162) `def __init__(self, config)`
- `temperature` (line 1170) `def temperature(self)`
- `step` (line 1173) `def step(self)`
- `accept_perturbation` (line 1176) `def accept_perturbation(self, delta_loss)`
- `should_restart` (line 1182) `def should_restart(self, current_delta, best_delta)`
- `__init__` (line 1187) `def __init__(self, config)`
- `step_adaptive` (line 1191) `def step_adaptive(self, alignment_trend, resonance_score)`
- `__init__` (line 1203) `def __init__(self, config)`
- `update_metrics` (line 1210) `def update_metrics(self)`
- `compute_delta_slope` (line 1219) `def compute_delta_slope(self)`
- `format_progress_bar` (line 1229) `def format_progress_bar(self, epoch, total_epochs, phase)`
- `__init__` (line 1262) `def __init__(self, config, checkpoint_dir)`
- `should_save_checkpoint` (line 1271) `def should_save_checkpoint(self)`
- `save_checkpoint` (line 1276) `def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)`
- `__init__` (line 1292) `def __init__(self, config)`
- `should_save` (line 1302) `def should_save(self, current_delta, current_alpha, current_acc)`
- `save_checkpoint` (line 1307) `def save_checkpoint(self, model, optimizer, epoch, metrics, lambda_value)`
- `check` (line 1324) `def check(model)`
- `__init__` (line 1339) `def __init__(self, config)`
- `compute_weight_metrics` (line 1354) `def compute_weight_metrics(self, model)`
- `compute_norm_conservation_error` (line 1364) `def compute_norm_conservation_error(self, model, val_x)`
- `train_single_epoch` (line 1373) `def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler)`
- `validate` (line 1398) `def validate(self, model, val_x, val_y)`
- `collect_all_metrics` (line 1408) `def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)`
- `__init__` (line 1448) `def __init__(self, config, surface_engine)`
- `prospect` (line 1453) `def prospect(self)`
- `__init__` (line 1484) `def __init__(self, config, surface_engine, batch_size)`
- `mine` (line 1490) `def mine(self)`
- `__init__` (line 1534) `def __init__(self, config, surface_engine, seed, batch_size)`
- `run_phase3_training` (line 1541) `def run_phase3_training(self)`
- `__init__` (line 1600) `def __init__(self, config, surface_engine, model, optimizer, monitor, seed, batch_size)`
- `run_phase4_refinement` (line 1610) `def run_phase4_refinement(self)`
- `__init__` (line 1664) `def __init__(self, config, surface_engine, model, monitor, seed, batch_size)`
- `run_phase5_crystallization` (line 1674) `def run_phase5_crystallization(self)`
- `__init__` (line 1726) `def __init__(self, config)`
- `run` (line 1730) `def run(self)`
- `_save_final_results` (line 1789) `def _save_final_results(self, model, monitor, seed, batch_size)`
- `safe_get` (line 1231) `def safe_get(key)`

#### `willmore_crystallography_suite.py.py`
**Path:** `willmore_crystallography_suite.py.py`

**Classes:**
- `WillmoreSuiteConfig` (line 52) `class WillmoreSuiteConfig` - *Master configuration for Willmore crystallography suite.*
- `SpectralLayer` (line 92) `class SpectralLayer` - *Spectral convolution layer with learnable frequency-domain kernels.*
- `MinimalSurfaceSpectralNetwork` (line 138) `class MinimalSurfaceSpectralNetwork` - *Willmore minimal surface spectral network architecture.*
- `MinimalSurfaceOperator` (line 181) `class MinimalSurfaceOperator` - *Analytical minimal surface operations for ground truth generation.*
- `SurfacePotentialGenerator` (line 237) `class SurfacePotentialGenerator` - *Generate various surface potential configurations.*
- `MinimalSurfaceDataset` (line 298) `class MinimalSurfaceDataset(Dataset)` - *Dataset for minimal surface evolution problems.*
- `WeightIntegrityCalculator` (line 374) `class WeightIntegrityCalculator` - *Validate weight tensor integrity (NaN/Inf detection).*
- `DiscretizationCalculator` (line 410) `class DiscretizationCalculator` - *Compute weight discretization metrics (delta, alpha).*
- `SpectralGeometryCalculator` (line 440) `class SpectralGeometryCalculator` - *Compute spectral geometry properties of weight matrices.*
- `RicciCurvatureCalculator` (line 500) `class RicciCurvatureCalculator` - *Compute Ricci curvature of weight space metric.*
- `WillmoreEnergyCalculator` (line 547) `class WillmoreEnergyCalculator` - *Compute Willmore energy and curvature metrics from weights.*
- `TopologicalPhaseDetector` (line 619) `class TopologicalPhaseDetector` - *Detect topological phase state via Fourier mass center analysis.*
- `BerryPhaseCalculator` (line 709) `class BerryPhaseCalculator` - *Compute Berry phase from checkpoint trajectory.*
- `FunctionalTest` (line 787) `class FunctionalTest(ABC)` - *Abstract base class for functional validation tests.*
- `AccuracyTest` (line 799) `class AccuracyTest(FunctionalTest)` - *Test 1: Model accuracy on validation set.*
- `SurfaceReconstructionTest` (line 823) `class SurfaceReconstructionTest(FunctionalTest)` - *Test 2: Surface reconstruction quality via Willmore energy.*
- `GeneralizationTest` (line 866) `class GeneralizationTest(FunctionalTest)` - *Test 3: Generalization to unseen potential configurations.*
- `CheckpointAnalyzer` (line 900) `class CheckpointAnalyzer` - *Main analyzer orchestrating all metrics and functional tests.*
- `ComprehensiveVisualizer` (line 1035) `class ComprehensiveVisualizer` - *Generate comprehensive visualization of all metrics.*
- `BatchProcessor` (line 1321) `class BatchProcessor` - *Process multiple checkpoints and find the best one.*

**Functions:**
- `setup_logging` (line 1444) `def setup_logging(log_level)` - *Configure logging for the suite.*
- `main` (line 1452) `def main()`
- `__init__` (line 95) `def __init__(self, channels, grid_size)`
- `forward` (line 112) `def forward(self, x)`
- `__init__` (line 141) `def __init__(self, config)`
- `forward` (line 160) `def forward(self, x)`
- `get_spectral_representation` (line 171) `def get_spectral_representation(self, x)` - *Extract spectral features for analysis.*
- `__init__` (line 184) `def __init__(self, grid_size)`
- `_precompute_spectral_operators` (line 188) `def _precompute_spectral_operators(self)`
- `apply_laplacian` (line 196) `def apply_laplacian(self, field)`
- `compute_mean_curvature` (line 201) `def compute_mean_curvature(self, surface)`
- `compute_gaussian_curvature` (line 212) `def compute_gaussian_curvature(self, surface)`
- `compute_willmore_energy` (line 223) `def compute_willmore_energy(self, surface)`
- `compute_surface_area` (line 229) `def compute_surface_area(self, surface)`
- `__init__` (line 240) `def __init__(self, config)`
- `pyramid_potential` (line 244) `def pyramid_potential(self)`
- `cube_potential` (line 251) `def cube_potential(self)`
- `dodecahedron_potential` (line 258) `def dodecahedron_potential(self)`
- `torus_potential` (line 266) `def torus_potential(self)`
- `hyperbolic_potential` (line 274) `def hyperbolic_potential(self)`
- `generate_mixed_potential` (line 282) `def generate_mixed_potential(self, seed)`
- `__init__` (line 301) `def __init__(self, config, seed, num_samples)`
- `_generate_surface_pair` (line 331) `def _generate_surface_pair(self, potential, sample_seed)`
- `__len__` (line 364) `def __len__(self)`
- `__getitem__` (line 367) `def __getitem__(self, idx)`
- `get_validation_batch` (line 370) `def get_validation_batch(self)`
- `__init__` (line 377) `def __init__(self, config)`
- `compute` (line 380) `def compute(self, model)`
- `__init__` (line 413) `def __init__(self, config)`
- `compute` (line 416) `def compute(self, model)`
- `__init__` (line 443) `def __init__(self, config)`
- `compute` (line 446) `def compute(self, model)`
- `__init__` (line 503) `def __init__(self, config)`
- `compute` (line 506) `def compute(self, model)`
- `__init__` (line 550) `def __init__(self, config)`
- `compute` (line 554) `def compute(self, model)`
- `_compute_surface_metrics` (line 575) `def _compute_surface_metrics(self, surface)`
- `_empty_metrics` (line 605) `def _empty_metrics()`
- `__init__` (line 622) `def __init__(self, config)`
- `detect` (line 628) `def detect(self, spectral_field)`
- `__init__` (line 712) `def __init__(self, config)`
- `load_checkpoints` (line 715) `def load_checkpoints(self, checkpoint_dir)`
- `_extract_epoch` (line 734) `def _extract_epoch(self, filepath)`
- `flatten_spectral_kernels` (line 738) `def flatten_spectral_kernels(self, state_dict)`
- `calculate_berry_phase` (line 751) `def calculate_berry_phase(self, checkpoint_dir)`
- `__init__` (line 790) `def __init__(self, config)`
- `run` (line 795) `def run(self, model, dataset)`
- `run` (line 802) `def run(self, model, dataset)`
- `__init__` (line 826) `def __init__(self, config)`
- `run` (line 830) `def run(self, model, dataset)`
- `run` (line 869) `def run(self, model, dataset)`
- `__init__` (line 903) `def __init__(self, config)`
- `analyze_checkpoint` (line 918) `def analyze_checkpoint(self, checkpoint_path, dataset)`
- `_extract_spectral_field` (line 997) `def _extract_spectral_field(self, model)`
- `_compute_health_score` (line 1012) `def _compute_health_score(self, results)`
- `__init__` (line 1038) `def __init__(self, config)`
- `visualize_analysis` (line 1041) `def visualize_analysis(self, results, output_path)`
- `_plot_weight_integrity` (line 1067) `def _plot_weight_integrity(self, results, ax)`
- `_plot_discretization` (line 1085) `def _plot_discretization(self, results, ax)`
- `_plot_spectral_geometry` (line 1111) `def _plot_spectral_geometry(self, results, ax)`
- `_plot_ricci_curvature` (line 1132) `def _plot_ricci_curvature(self, results, ax)`
- `_plot_functional_test_1` (line 1145) `def _plot_functional_test_1(self, results, ax)`
- `_plot_functional_test_2` (line 1165) `def _plot_functional_test_2(self, results, ax)`
- `_plot_functional_test_3` (line 1188) `def _plot_functional_test_3(self, results, ax)`
- `_plot_health_summary` (line 1210) `def _plot_health_summary(self, results, ax)`
- `_plot_layer_deltas` (line 1240) `def _plot_layer_deltas(self, results, ax)`
- `_plot_phase_diagram` (line 1259) `def _plot_phase_diagram(self, results, ax)`
- `_plot_crystal_verdict` (line 1279) `def _plot_crystal_verdict(self, results, ax)`
- `__init__` (line 1324) `def __init__(self, config)`
- `process_directory` (line 1331) `def process_directory(self, checkpoint_dir, output_dir, dataset)`
- `_rank_checkpoints` (line 1381) `def _rank_checkpoints(self, all_results)`
- `_generate_summary` (line 1407) `def _generate_summary(self, ranked, output_dir)`

#### `willmore_zero_shot_scaler.py`
**Path:** `willmore_zero_shot_scaler.py`

**Classes:**
- `ScalerConfig` (line 115) `class ScalerConfig` - *Configuration dataclass for the zero-shot scaler.*
- `IConfigurationLoader` (line 144) `class IConfigurationLoader(ABC)` - *Abstract interface for configuration loading.*
- `TOMLConfigurationLoader` (line 153) `class TOMLConfigurationLoader(IConfigurationLoader)` - *TOML-based configuration loader.*
- `ICheckpointManager` (line 207) `class ICheckpointManager(ABC)` - *Abstract interface for checkpoint management.*
- `WillmoreCheckpointManager` (line 221) `class WillmoreCheckpointManager(ICheckpointManager)` - *Checkpoint manager for Willmore Crystal models.*
- `ISpectralWeightInterpolator` (line 260) `class ISpectralWeightInterpolator(ABC)` - *Abstract interface for spectral weight interpolation.*
- `FourierSpectralInterpolator` (line 274) `class FourierSpectralInterpolator(ISpectralWeightInterpolator)` - *Fourier-based spectral weight interpolation.*
- `BilinearSpectralInterpolator` (line 387) `class BilinearSpectralInterpolator(ISpectralWeightInterpolator)` - *Bilinear interpolation for spectral weights.*
- `IGridScaler` (line 445) `class IGridScaler(ABC)` - *Abstract interface for grid scaling.*
- `WillmoreGridScaler` (line 458) `class WillmoreGridScaler(IGridScaler)` - *Grid scaler for Willmore Crystal networks.*
- `IMetricsEvaluator` (line 583) `class IMetricsEvaluator(ABC)` - *Abstract interface for metrics evaluation.*
- `WillmoreMetricsEvaluator` (line 597) `class WillmoreMetricsEvaluator(IMetricsEvaluator)` - *Metrics evaluator for Willmore Crystal models.*
- `ScalingPipeline` (line 776) `class ScalingPipeline` - *Orchestrates the complete progressive scaling process.*

**Functions:**
- `create_default_config_file` (line 1046) `def create_default_config_file(path)` - *Create a default configuration file.*
- `build_argument_parser` (line 1053) `def build_argument_parser()` - *Build the command-line argument parser.*
- `main` (line 1129) `def main()` - *Main entry point for the zero-shot scaler.*
- `load` (line 148) `def load(self, source)` - *Load configuration from the specified source.*
- `load` (line 156) `def load(self, source)`
- `_from_toml` (line 161) `def _from_toml(self, path)`
- `_from_dict` (line 170) `def _from_dict(self, data)`
- `load_checkpoint` (line 211) `def load_checkpoint(self, path, device)` - *Load a model checkpoint from disk.*
- `save_checkpoint` (line 216) `def save_checkpoint(self, model, metrics, path)` - *Save a model checkpoint to disk.*
- `__init__` (line 224) `def __init__(self, config)`
- `load_checkpoint` (line 228) `def load_checkpoint(self, path, device)`
- `save_checkpoint` (line 246) `def save_checkpoint(self, model, metrics, path)`
- `interpolate` (line 264) `def interpolate(self, source_weight, target_shape)` - *Interpolate spectral weights to a new shape.*
- `__init__` (line 277) `def __init__(self, config)`
- `interpolate` (line 281) `def interpolate(self, source_weight, target_shape)`
- `_interpolate_2d_spectral` (line 294) `def _interpolate_2d_spectral(self, source, target_shape)`
- `_interpolate_4d_spectral` (line 314) `def _interpolate_4d_spectral(self, source, target_shape)`
- `_pad_spectrum_2d` (line 332) `def _pad_spectrum_2d(self, spectrum, target_h, target_w)`
- `_interpolate_generic` (line 369) `def _interpolate_generic(self, source, target_shape)`
- `__init__` (line 390) `def __init__(self, config)`
- `interpolate` (line 394) `def interpolate(self, source_weight, target_shape)`
- `_interpolate_generic` (line 419) `def _interpolate_generic(self, source, target_shape)`
- `scale_model` (line 449) `def scale_model(self, source_model, target_grid_size)` - *Scale a model to a new grid resolution.*
- `__init__` (line 461) `def __init__(self, config, interpolator)`
- `scale_model` (line 470) `def scale_model(self, source_model, target_grid_size)`
- `_extract_hidden_dim` (line 495) `def _extract_hidden_dim(self, model)`
- `_extract_expansion_dim` (line 500) `def _extract_expansion_dim(self, model)`
- `_count_spectral_layers` (line 505) `def _count_spectral_layers(self, model)`
- `_transfer_weights` (line 510) `def _transfer_weights(self, source, target, source_grid, target_grid)`
- `_scale_spectral_kernel` (line 535) `def _scale_spectral_kernel(self, kernel, target_shape, source_grid, target_grid)`
- `_scale_conv_weight` (line 549) `def _scale_conv_weight(self, weight, target_shape)`
- `_validate_weight_transfer` (line 570) `def _validate_weight_transfer(self, source, target)`
- `evaluate` (line 587) `def evaluate(self, model, grid_size, num_samples)` - *Evaluate model performance and metrics.*
- `__init__` (line 600) `def __init__(self, config)`
- `evaluate` (line 606) `def evaluate(self, model, grid_size, num_samples)`
- `_construct_weight_surface` (line 639) `def _construct_weight_surface(self, model, grid_size)`
- `_compute_willmore_metrics` (line 661) `def _compute_willmore_metrics(self, surface)`
- `_compute_curvature_metrics` (line 677) `def _compute_curvature_metrics(self, surface)`
- `_compute_spectral_metrics` (line 702) `def _compute_spectral_metrics(self, model)`
- `_evaluate_inference_quality` (line 735) `def _evaluate_inference_quality(self, model, grid_size, num_samples)`
- `__init__` (line 779) `def __init__(self, config)`
- `execute` (line 796) `def execute(self)`
- `_load_source_model` (line 888) `def _load_source_model(self)`
- `_log_metrics` (line 914) `def _log_metrics(self, metrics, grid_size)`
- `_check_degradation` (line 930) `def _check_degradation(self, source_metrics, current_metrics)`
- `_is_better_metrics` (line 946) `def _is_better_metrics(self, current, best)`
- `_save_scaled_model` (line 961) `def _save_scaled_model(self, model, metrics, grid_size)`
- `_compile_final_results` (line 971) `def _compile_final_results(self)`
- `_save_final_results` (line 985) `def _save_final_results(self, results)`
- `_write_detailed_report` (line 997) `def _write_detailed_report(self, results, path)`

#### `wilmore_rbc.py`
**Path:** `wilmore_rbc.py`

**Classes:**
- `ReconstructionConfig` (line 37) `class ReconstructionConfig` - *Configuration for RBC reconstruction.*
- `SpectralLayer` (line 54) `class SpectralLayer` - *Spectral convolution layer for minimal surface processing.*
- `MinimalSurfaceSpectralNetwork` (line 88) `class MinimalSurfaceSpectralNetwork` - *Spectral network for minimal surface computation.*
- `CheckpointLoader` (line 123) `class CheckpointLoader` - *Handles loading of model checkpoints.*
- `ModelBuilder` (line 133) `class ModelBuilder` - *Builds and initializes models from configuration.*
- `RBCMeshLoader` (line 172) `class RBCMeshLoader` - *Loads RBC mesh data from OpenRBC format files.*
- `ImprovedSphericalProjector` (line 198) `class ImprovedSphericalProjector` - *Improved spherical projection with proper handling of biconcave geometry.

Key improvements:
1. Area-weighted averaging to avoid oversampling at poles
2. RBF interpolation for smooth reconstruction
3. Proper handling of the dimple regions
4. Gaussian smoothing in parameter space*
- `CylindricalProjector` (line 380) `class CylindricalProjector` - *Cylindrical projection - often better for biconcave shapes.

The RBC is naturally more cylindrical than spherical,
with the dimples on top and bottom.*
- `SyntheticShapeGenerator` (line 472) `class SyntheticShapeGenerator` - *Generates synthetic shapes for comparison.*
- `WillmoreMetricsCalculator` (line 517) `class WillmoreMetricsCalculator` - *Calculates Willmore energy and curvature metrics.*
- `SurfaceEvolver` (line 545) `class SurfaceEvolver` - *Evolves surfaces using the trained model with LR schedule and volume conservation.*
- `MeshExporter` (line 623) `class MeshExporter` - *Exports meshes to various formats.*
- `RBCReconstructionPipeline` (line 791) `class RBCReconstructionPipeline` - *Main pipeline for RBC reconstruction using scaled model.*

**Functions:**
- `build_argument_parser` (line 960) `def build_argument_parser()`
- `main` (line 1046) `def main()`
- `__init__` (line 57) `def __init__(self, channels, grid_size)`
- `forward` (line 68) `def forward(self, x)`
- `__init__` (line 91) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)`
- `forward` (line 112) `def forward(self, x)`
- `load` (line 127) `def load(checkpoint_path, device)`
- `build` (line 137) `def build(config)`
- `load_from_checkpoint` (line 148) `def load_from_checkpoint(checkpoint_path, config)`
- `load` (line 176) `def load(vert_path, face_path)`
- `__init__` (line 209) `def __init__(self, grid_size, smoothing_sigma)`
- `compute_vertex_areas` (line 217) `def compute_vertex_areas(self, vertices, faces)` - *Compute approximate area associated with each vertex.*
- `project_mesh` (line 232) `def project_mesh(self, vertices, faces, use_rbf)` - *Project mesh onto spherical grid with proper area weighting.*
- `_area_weighted_projection` (line 270) `def _area_weighted_projection(self, theta, phi, r, areas)` - *Project using area-weighted averaging.*
- `_rbf_interpolation` (line 303) `def _rbf_interpolation(self, theta, phi, r)` - *Use RBF interpolation for smooth reconstruction.*
- `_apply_spherical_smoothing` (line 333) `def _apply_spherical_smoothing(self, r_grid)` - *Apply Gaussian smoothing adapted to spherical coordinates.*
- `to_cartesian` (line 355) `def to_cartesian(self, r_grid, scale)` - *Convert spherical grid back to 3D vertices.*
- `__init__` (line 388) `def __init__(self, grid_size, smoothing_sigma)`
- `project_mesh` (line 396) `def project_mesh(self, vertices, faces)` - *Project mesh using cylindrical coordinates.*
- `to_cartesian` (line 445) `def to_cartesian(self, rho_grid, z_scale, rho_scale)` - *Convert cylindrical grid back to 3D vertices.*
- `__init__` (line 475) `def __init__(self, grid_size)`
- `create_sphere` (line 481) `def create_sphere(self, radius)`
- `create_biconcave` (line 484) `def create_biconcave(self, radius, dimple_depth)` - *Create biconcave disc shape using Evans-Fung model.*
- `create_evans_fung_rbc` (line 490) `def create_evans_fung_rbc(self, radius, dimple_depth, thickness)` - *Create RBC shape using Evans-Fung parametrization.

The RBC cross-section follows:
r(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)

This creates the characteristic biconcave shape.*
- `__init__` (line 520) `def __init__(self, grid_size)`
- `compute_willmore` (line 523) `def compute_willmore(self, surface)`
- `compute_curvature_stats` (line 527) `def compute_curvature_stats(self, surface)`
- `__init__` (line 548) `def __init__(self, model, config)`
- `_compute_lr` (line 556) `def _compute_lr(self, step)` - *Compute learning rate with cosine schedule.*
- `_compute_volume` (line 567) `def _compute_volume(self, surface)` - *Estimate volume from surface grid.*
- `_normalize_volume` (line 571) `def _normalize_volume(self, surface, target_volume)` - *Normalize surface to preserve volume.*
- `evolve` (line 579) `def evolve(self, initial_surface)`
- `save_obj` (line 627) `def save_obj(vertices, faces, filepath)`
- `save_html_comparison` (line 636) `def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolved_faces, biconcave_vertices, biconcave_faces, metrics, output_path)`
- `__init__` (line 794) `def __init__(self, config)`
- `run` (line 805) `def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)`

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
