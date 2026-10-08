# orphans

*Community 1 | 6 files | cohesion 0.00*

## Definition

This community groups 6 file(s) rooted at `root` with dominant language py (cohesion 0.00). Central symbols: `AccuracyTest`, `BatchProcessor`, `BerryPhaseCalculator`, `CheckpointAnalyzer`, `CheckpointModelLoader`, `ComprehensiveVisualizer`, `DiscreteCurvatureCalculator`, `DiscretizationCalculator`. Core file: `willmore_crystallography_suite.py.py` (92 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 0 | yes |
| `install.sh` | sh | utility | 0 | no |
| `lol.py` | py | utility | 8 | yes |
| `rbc_willmore_analysis.py` | py | utility | 87 | yes |
| `rbc_willmore_analysis2.py` | py | utility | 88 | yes |
| `willmore_crystallography_suite.py.py` | py | utility | 92 | yes |

## Key Symbols

- `create_synthetic_rbc` (function, `lol.py:16`) `def create_synthetic_rbc(n_vertices)` - RBC sintético con forma bicóncava.
- `spherical_projection` (function, `lol.py:44`) `def spherical_projection(vertices, grid_size)` - Proyección esférica - tiene problemas con dimples.
- `cylindrical_projection` (function, `lol.py:76`) `def cylindrical_projection(vertices, grid_size)` - Proyección cilíndrica - NATURAL para RBC.
- `spherical_to_cartesian` (function, `lol.py:123`) `def spherical_to_cartesian(r_grid, grid_size)` - Convierte grilla esférica a 3D.
- `cylindrical_to_cartesian` (function, `lol.py:144`) `def cylindrical_to_cartesian(rho_grid, z_min, z_max, grid_size)` - Convierte grilla cilíndrica a 3D.
- `compute_metrics` (function, `lol.py:164`) `def compute_metrics(r_grid, mask, original_r)` - Computa métricas de calidad.
- `save_obj` (function, `lol.py:181`) `def save_obj(vertices, faces, filepath)`
- `main` (function, `lol.py:189`) `def main()`
- `RBCAnalysisConfig` (class, `rbc_willmore_analysis.py:55`) `class RBCAnalysisConfig` - Configuration container for RBC Willmore analysis.
- `ILogger` (class, `rbc_willmore_analysis.py:102`) `class ILogger(ABC)` - Abstract interface for logging implementations.
- `info` (method, `rbc_willmore_analysis.py:106`) `def info(self, message)`
- `warning` (method, `rbc_willmore_analysis.py:110`) `def warning(self, message)`
- `error` (method, `rbc_willmore_analysis.py:114`) `def error(self, message)`
- `debug` (method, `rbc_willmore_analysis.py:118`) `def debug(self, message)`
- `StandardLogger` (class, `rbc_willmore_analysis.py:122`) `class StandardLogger(ILogger)` - Standard logging implementation using Python logging module.
- `__init__` (method, `rbc_willmore_analysis.py:125`) `def __init__(self, name, level)`
- `info` (method, `rbc_willmore_analysis.py:136`) `def info(self, message)`
- `warning` (method, `rbc_willmore_analysis.py:139`) `def warning(self, message)`
- `error` (method, `rbc_willmore_analysis.py:142`) `def error(self, message)`
- `debug` (method, `rbc_willmore_analysis.py:145`) `def debug(self, message)`
- `IFileSystem` (class, `rbc_willmore_analysis.py:149`) `class IFileSystem(ABC)` - Abstract interface for file system operations.
- `exists` (method, `rbc_willmore_analysis.py:153`) `def exists(self, path)`
- `read_text` (method, `rbc_willmore_analysis.py:157`) `def read_text(self, path)`
- `write_text` (method, `rbc_willmore_analysis.py:161`) `def write_text(self, path, content)`
- `makedirs` (method, `rbc_willmore_analysis.py:165`) `def makedirs(self, path)`
- `StandardFileSystem` (class, `rbc_willmore_analysis.py:169`) `class StandardFileSystem(IFileSystem)` - Standard file system implementation.
- `exists` (method, `rbc_willmore_analysis.py:172`) `def exists(self, path)`
- `read_text` (method, `rbc_willmore_analysis.py:175`) `def read_text(self, path)`
- `write_text` (method, `rbc_willmore_analysis.py:179`) `def write_text(self, path, content)`
- `makedirs` (method, `rbc_willmore_analysis.py:183`) `def makedirs(self, path)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (root) and community 1 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `app.py`
- `install.sh`
- `lol.py`
- `rbc_willmore_analysis.py`
- `rbc_willmore_analysis2.py`
- `willmore_crystallography_suite.py.py`
