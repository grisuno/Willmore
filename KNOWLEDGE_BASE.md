# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. 15 files, 652 symbols, 169 imports. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Start here:** Statistics Dashboard for scope, God Nodes for blast radius, Architecture Reference for per-file API. Agents: prefer `readmenator-agent/INDEX.md` + `SYMBOLS.md`.

**Wiki:** prefer `readmenator-wiki/index.md` for progressive disclosure: one synthesis page per community, `connections.json` with EXTRACTED vs INFERRED confidence, `queries.md` log, `REPORT.md` audit.

**Confidence:** EXTRACTED = parsed from source, INFERRED = heuristic bridge, AMBIGUOUS = reported, never hidden. See `readmenator-wiki/REPORT.md`.

**Total Files Parsed:** 15 | **Total Symbols Extracted:** 652 | **Total Imports:** 169
 | **Resolved Imports:** 8

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:b3ca3bb | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Community Analysis](#community-analysis)
6. [Suggested Questions](#suggested-questions)
7. [Hotspot Analysis](#hotspot-analysis)
8. [Change Impact Analysis](#change-impact-analysis)
9. [Suggested Linting Rules](#suggested-linting-rules)
10. [Orphans](#orphans)
11. [Query Recipes](#query-recipes)
12. [Structural Knowledge Map](#structural-knowledge-map)
13. [UML Class Diagram](#uml-class-diagram)
14. [Code Property Graph](#code-property-graph)
15. [Architecture Reference](#architecture-reference)
    - [PY (14 files)](#py-14-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 15 |
| Total Symbols | 652 |
| Total Imports | 169 |
| Call Edges | 5377 |
| Inheritance Edges | 63 |
| Languages | 2 |
| Avg Symbols/File | 43.5 |
| Avg Imports/File | 11.3 |
| Resolved Imports | 8 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `willmore_crystallography_suite.py.py` | 32 | 92 | py |
| `willmore_crsital2.py` | 19 | 174 | py |
| `willmore_zero_shot_scaler.py` | 19 | 63 | py |
| `rbc_willmore_analysis.py` | 16 | 87 | py |
| `rbc_willmore_analysis2.py` | 16 | 88 | py |
| `rbc_model_reconstruction_128.py` | 14 | 46 | py |
| `wilmore_rbc.py` | 14 | 49 | py |
| `model_Reco.py` | 9 | 10 | py |
| `rbc.py` | 7 | 11 | py |
| `rbc_model_reconstruction (1).py` | 7 | 11 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 9 |
| business_logic | 4 |
| testing | 1 |
| presentation | 1 |

### utility

- `app.py` (py, 0 symbols)
- `install.sh` (sh, 0 symbols)
- `lol.py` (py, 8 symbols)
- `rbc.py` (py, 11 symbols)
- `rbc_willmore_analysis.py` (py, 87 symbols)
- `rbc_willmore_analysis2.py` (py, 88 symbols)
- `willmore_crsital2.py` (py, 174 symbols)
- `willmore_zero_shot_scaler.py` (py, 63 symbols)
- `wilmore_rbc.py` (py, 49 symbols)

### business_logic

- `model_Reco.py` (py, 10 symbols)
- `rbc_model_reconstruction (1).py` (py, 11 symbols)
- `rbc_model_reconstruction.py` (py, 10 symbols)
- `rbc_model_reconstruction_128.py` (py, 46 symbols)

### testing

- `test.py` (py, 3 symbols)

### presentation

- `willmore_crystallography_suite.py.py` (py, 92 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `willmore_crsital2.py` | 0.3215 | 0.4937 | 0.4937 | 0.00 | 0.01 |
| 2 | `rbc.py` | 0.1411 | 0.0633 | 0.0633 | 0.00 | 1.00 |
| 3 | `rbc_model_reconstruction (1).py` | 0.1411 | 0.0633 | 0.0633 | 0.00 | 1.00 |
| 4 | `rbc_model_reconstruction.py` | 0.1411 | 0.0633 | 0.0633 | 0.00 | 1.00 |
| 5 | `test.py` | 0.1078 | 0.0633 | 0.0633 | 0.00 | 0.67 |
| 6 | `app.py` | 0.1000 | 0.0000 | 0.0000 | 0.00 | 1.00 |
| 7 | `wilmore_rbc.py` | 0.0962 | 0.0633 | 0.0633 | 0.00 | 0.55 |
| 8 | `rbc_model_reconstruction_128.py` | 0.0933 | 0.0633 | 0.0633 | 0.00 | 0.52 |
| 9 | `lol.py` | 0.0875 | 0.0000 | 0.0000 | 0.00 | 0.88 |
| 10 | `willmore_zero_shot_scaler.py` | 0.0776 | 0.0633 | 0.0633 | 0.00 | 0.37 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `willmore_crsital2.py` | 33.4 | | 0.4937 |
| `willmore_crystallography_suite.py.py` | 9.2 | | 0.0000 |
| `rbc_willmore_analysis2.py` | 8.8 | | 0.0000 |
| `rbc_willmore_analysis.py` | 8.7 | | 0.0000 |
| `willmore_zero_shot_scaler.py` | 8.3 | | 0.0633 |
| `wilmore_rbc.py` | 6.9 | | 0.0633 |
| `rbc_model_reconstruction_128.py` | 6.6 | | 0.0633 |
| `rbc.py` | 3.1 | | 0.0633 |
| `rbc_model_reconstruction (1).py` | 3.1 | | 0.0633 |
| `model_Reco.py` | 3.0 | | 0.0000 |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### root (Cohesion: 1.00)

**9 files** in this community:

- `model_Reco.py` (py, 10 symbols)
- `rbc.py` (py, 11 symbols)
- `rbc_model_reconstruction (1).py` (py, 11 symbols)
- `rbc_model_reconstruction.py` (py, 10 symbols)
- `rbc_model_reconstruction_128.py` (py, 46 symbols)
- `test.py` (py, 3 symbols)
- `willmore_crsital2.py` (py, 174 symbols)
- `willmore_zero_shot_scaler.py` (py, 63 symbols)
- `wilmore_rbc.py` (py, 49 symbols)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does willmore_crsital2.py depend on, and what depends on it? (8 connections)
- What does willmore_crystallography_suite.py.py depend on, and what depends on it? (0 connections)
- What does rbc_willmore_analysis2.py depend on, and what depends on it? (0 connections)
- How are the 9 files in 'root' related to each other?
- What is the overall architecture of this codebase?

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `willmore_crsital2.py` | 1.000 | 0.844 | 0.906 | 174 | 27 |
| `rbc.py` | 0.063 | 0.250 | 0.175 | 11 | 8 |
| `rbc_model_reconstruction (1).py` | 0.063 | 0.250 | 0.175 | 11 | 8 |
| `rbc_model_reconstruction.py` | 0.058 | 0.250 | 0.173 | 10 | 8 |
| `test.py` | 0.017 | 0.219 | 0.138 | 3 | 7 |
| `app.py` | 0.000 | 0.000 | 0.000 | 0 | 0 |
| `wilmore_rbc.py` | 0.282 | 0.469 | 0.394 | 49 | 15 |
| `rbc_model_reconstruction_128.py` | 0.264 | 0.469 | 0.387 | 46 | 15 |
| `lol.py` | 0.046 | 0.094 | 0.075 | 8 | 3 |
| `willmore_zero_shot_scaler.py` | 0.362 | 0.625 | 0.520 | 63 | 20 |
| `willmore_crystallography_suite.py.py` | 0.529 | 1.000 | 0.811 | 92 | 32 |
| `rbc_willmore_analysis2.py` | 0.506 | 0.500 | 0.502 | 88 | 16 |
| `rbc_willmore_analysis.py` | 0.500 | 0.500 | 0.500 | 87 | 16 |
| `model_Reco.py` | 0.058 | 0.312 | 0.210 | 10 | 10 |
| `install.sh` | 0.000 | 0.000 | 0.000 | 0 | 0 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `willmore_crsital2.py` | 8 | 0 | 8 |
| `app.py` | 0 | 0 | 0 |
| `install.sh` | 0 | 0 | 0 |
| `lol.py` | 0 | 0 | 0 |
| `model_Reco.py` | 0 | 0 | 0 |
| `rbc.py` | 0 | 0 | 0 |
| `rbc_model_reconstruction (1).py` | 0 | 0 | 0 |
| `rbc_model_reconstruction.py` | 0 | 0 | 0 |
| `rbc_model_reconstruction_128.py` | 0 | 0 | 0 |
| `rbc_willmore_analysis.py` | 0 | 0 | 0 |
| `rbc_willmore_analysis2.py` | 0 | 0 | 0 |
| `test.py` | 0 | 0 | 0 |
| `willmore_crystallography_suite.py.py` | 0 | 0 | 0 |
| `willmore_zero_shot_scaler.py` | 0 | 0 | 0 |
| `wilmore_rbc.py` | 0 | 0 | 0 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 519 total | py | 519 |
| `RM002` | info | Print statement found (consider logging instead) | python | 343 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `install.sh` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

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
    subgraph community_0 ["root"]
    willmore_zero_shot_scaler_py["willmore_zero_shot_scaler.py (py)"]
    class willmore_zero_shot_scaler_py mod;
    willmore_crsital2_py["willmore_crsital2.py (py)"]
    class willmore_crsital2_py mod;
    rbc_willmore_analysis2_py["rbc_willmore_analysis2.py (py)"]
    class rbc_willmore_analysis2_py mod;
    rbc_willmore_analysis_py["rbc_willmore_analysis.py (py)"]
    class rbc_willmore_analysis_py mod;
    wilmore_rbc_py["wilmore_rbc.py (py)"]
    class wilmore_rbc_py mod;
    rbc_model_reconstruction_128_py["rbc_model_reconstruction_128.py (py)"]
    class rbc_model_reconstruction_128_py mod;
    model_Reco_py["model_Reco.py (py)"]
    class model_Reco_py mod;
    rbc_py["rbc.py (py)"]
    class rbc_py mod;
    rbc_model_reconstruction__1__py["rbc_model_reconstruction (1).py (py)"]
    class rbc_model_reconstruction__1__py mod;
    rbc_model_reconstruction_py["rbc_model_reconstruction.py (py)"]
    class rbc_model_reconstruction_py mod;
    test_py["test.py (py)"]
    class test_py mod;
    lol_py["lol.py (py)"]
    class lol_py mod;
    app_py["app.py (py)"]
    class app_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    end
    model_Reco_py -- resolved_imports --> willmore_crsital2_py
    rbc_py -- resolved_imports --> willmore_crsital2_py
    rbc_model_reconstruction__1__py -- resolved_imports --> willmore_crsital2_py
    rbc_model_reconstruction_py -- resolved_imports --> willmore_crsital2_py
    rbc_model_reconstruction_128_py -- resolved_imports --> willmore_crsital2_py
    test_py -- resolved_imports --> willmore_crsital2_py
    willmore_zero_shot_scaler_py -- resolved_imports --> willmore_crsital2_py
    wilmore_rbc_py -- resolved_imports --> willmore_crsital2_py
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

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class rbc_model_reconstruction_128_py_ReconstructionConfig {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_SpectralLayer {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_MinimalSurfaceSpectralNetwork {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_CheckpointLoader {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_ModelBuilder {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_RBCMeshLoader {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_ImprovedSphericalProjector {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_CylindricalProjector {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_SyntheticShapeGenerator {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_WillmoreMetricsCalculator {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_SurfaceEvolver {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_MeshExporter {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_model_reconstruction_128_py_RBCReconstructionPipeline {
    <<class>>
    +build_argument_parser()
    +main()
    +__init__(self, channels, grid_size)
    +forward(self, x)
    +__init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)
    +forward(self, x)
    +load(checkpoint_path, device)
    +build(config)
    +load_from_checkpoint(checkpoint_path, config)
    +load(vert_path, face_path)
  }
  class rbc_willmore_analysis_py_RBCAnalysisConfig {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_ILogger {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_StandardLogger {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_IFileSystem {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_StandardFileSystem {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_MeshData {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_IMeshLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_OpenRBCMeshLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_SyntheticMeshGenerator {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_ICurvatureCalculator {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_DiscreteCurvatureCalculator {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_SpectralLayer {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_MinimalSurfaceSpectralNetwork {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_IModelLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_CheckpointModelLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis_py_SurfaceAnalysisEngine {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_RBCAnalysisConfig {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_ILogger {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_StandardLogger {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_IFileSystem {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_StandardFileSystem {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_MeshData {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_IMeshLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_OpenRBCMeshLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_SyntheticMeshGenerator {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_ICurvatureCalculator {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_DiscreteCurvatureCalculator {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_SpectralLayer {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_MinimalSurfaceSpectralNetwork {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_IModelLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_CheckpointModelLoader {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class rbc_willmore_analysis2_py_SurfaceAnalysisEngine {
    <<class>>
    +parse_arguments()
    +create_config_from_args(args)
    +main()
    +info(self, message)
    +warning(self, message)
    +error(self, message)
    +debug(self, message)
    +__init__(self, name, level)
    +info(self, message)
    +warning(self, message)
  }
  class willmore_crsital2_py_Config {
    <<class>>
    +build_argument_parser()
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, grid_size)
    +_precompute_spectral_operators(self)
    +apply_laplacian(self, field)
    +compute_mean_curvature(self, surface)
  }
  class willmore_crsital2_py_IPhaseDetector {
    <<class>>
    +build_argument_parser()
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, grid_size)
    +_precompute_spectral_operators(self)
    +apply_laplacian(self, field)
    +compute_mean_curvature(self, surface)
  }
  class willmore_crsital2_py_IMetricCalculator {
    <<class>>
    +build_argument_parser()
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, grid_size)
    +_precompute_spectral_operators(self)
    +apply_laplacian(self, field)
    +compute_mean_curvature(self, surface)
  }
  class willmore_crsital2_py_SeedManager {
    <<class>>
    +build_argument_parser()
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, grid_size)
    +_precompute_spectral_operators(self)
    +apply_laplacian(self, field)
    +compute_mean_curvature(self, surface)
  }
  class willmore_crsital2_py_LoggerFactory {
    <<class>>
    +build_argument_parser()
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, grid_size)
    +_precompute_spectral_operators(self)
    +apply_laplacian(self, field)
    +compute_mean_curvature(self, surface)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [{"cohesion": 1.0, "id": 0, "label": "root", "size": 9}], "god_nodes": [{"node_id": "willmore_crsital2.py", "score": 33.4}, {"node_id": "willmore_crystallography_suite.py.py", "score": 9.2}, {"node_id": "rbc_willmore_analysis2.py", "score": 8.8}, {"node_id": "rbc_willmore_analysis.py", "score": 8.7}, {"node_id": "willmore_zero_shot_scaler.py", "score": 8.3}, {"node_id": "wilmore_rbc.py", "score": 6.9}, {"node_id": "rbc_model_reconstruction_128.py", "score": 6.6}, {"node_id": "rbc.py", "score": 3.1}, {"node_id": "rbc_model_reconstruction (1).py", "score": 3.1}, {"node_id": "model_Reco.py", "score": 3.0}], "surprising_connections": []}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "lol.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "lol.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "lol.py", "target": "scipy.ndimage"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "model_Reco.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction (1).py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "scipy.interpolate"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_model_reconstruction_128.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "rbc_willmore_analysis2.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "torch.optim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "torch.utils.data"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crsital2.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "matplotlib.gridspec"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "seaborn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "torch.optim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "torch.utils.data"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "scipy.stats"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "scipy.linalg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "scipy.optimize"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "sklearn.decomposition"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_crystallography_suite.py.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "tomli"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "willmore_zero_shot_scaler.py", "target": "tomllib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "scipy.interpolate"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "willmore_crsital2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wilmore_rbc.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "model_Reco.py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "rbc.py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "rbc_model_reconstruction (1).py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "rbc_model_reconstruction.py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "rbc_model_reconstruction_128.py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "test.py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "willmore_zero_shot_scaler.py", "target": "willmore_crsital2.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "wilmore_rbc.py", "target": "willmore_crsital2.py"}], "generator": "readmenator", "metadata": {"edge_count": 5617, "file_count": 15, "language_count": 2, "symbol_count": 652}, "nodes": [{"doc": "app.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:", "id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "57b21bdb023585b8", "symbol_count": 0, "symbols": []}, {"id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}, {"doc": "demo_cylindrical_vs_spherical.py  DEMO HONESTA: Comparación de proyección esférica vs cilíndrica.  CONCLUSIÓN ANTICIPADA: - Esférica: NO funciona bien para RBC (dimples en polos) - Cilíndrica: SÍ funciona (el RBC es naturalmente cilíndrico)", "id": "lol.py", "kind": "module", "label": "lol.py", "language": "py", "sha256": "9982cd1b681de4b9", "symbol_count": 8, "symbols": [{"doc": "RBC sintético con forma bicóncava.", "kind": "function", "line": 16, "name": "create_synthetic_rbc", "signature": "def create_synthetic_rbc(n_vertices)"}, {"doc": "Proyección esférica - tiene problemas con dimples.", "kind": "function", "line": 44, "name": "spherical_projection", "signature": "def spherical_projection(vertices, grid_size)"}, {"doc": "Proyección cilíndrica - NATURAL para RBC.\n\nCoordenadas:\n- z: altura (-z_max a +z_max)\n- phi: ángulo azimutal (-π a π)\n- rho: radio en el plano xy\n\nEl RBC es naturalmente cilíndrico: los dimples están en z=±z_max,\nno en direcciones angulares.", "kind": "function", "line": 76, "name": "cylindrical_projection", "signature": "def cylindrical_projection(vertices, grid_size)"}, {"doc": "Convierte grilla esférica a 3D.", "kind": "function", "line": 123, "name": "spherical_to_cartesian", "signature": "def spherical_to_cartesian(r_grid, grid_size)"}, {"doc": "Convierte grilla cilíndrica a 3D.", "kind": "function", "line": 144, "name": "cylindrical_to_cartesian", "signature": "def cylindrical_to_cartesian(rho_grid, z_min, z_max, grid_size)"}, {"doc": "Computa métricas de calidad.", "kind": "function", "line": 164, "name": "compute_metrics", "signature": "def compute_metrics(r_grid, mask, original_r)"}, {"kind": "function", "line": 181, "name": "save_obj", "signature": "def save_obj(vertices, faces, filepath)"}, {"kind": "function", "line": 189, "name": "main", "signature": "def main()"}]}, {"doc": "rbc_model_reconstruction.py  EVALUACIÓN PUNTO A PUNTO: Modelo evaluado en cada uno de los 9128 vértices sin pasar por grilla 16x16. Preserva la densidad irregular del malla original.", "id": "model_Reco.py", "kind": "module", "label": "model_Reco.py", "language": "py", "sha256": "13719263d8e6a6fb", "symbol_count": 10, "symbols": [{"kind": "function", "line": 27, "name": "load_rbc_mesh", "signature": "def load_rbc_mesh(vert_path, face_path)"}, {"kind": "function", "line": 49, "name": "center_mesh", "signature": "def center_mesh(vertices)"}, {"kind": "function", "line": 54, "name": "cartesian_to_spherical", "signature": "def cartesian_to_spherical(vertices)"}, {"kind": "function", "line": 63, "name": "spherical_to_cartesian", "signature": "def spherical_to_cartesian(r, theta, phi)"}, {"doc": "Evalúa el modelo en puntos arbitrarios (no en grilla regular).\n\nEstrategia: Para cada punto, encontrar su celda en la grilla 16x16,\nevaluar el modelo en esa celda, y usar el valor como predicción.", "kind": "function", "line": 70, "name": "evaluate_model_at_points", "signature": "def evaluate_model_at_points(model, r_values, theta_values, phi_values, grid_size, device, r_global_mean)"}, {"kind": "function", "line": 134, "name": "load_model", "signature": "def load_model(checkpoint_path, device, config)"}, {"doc": "Compute curvatures using the same operator as training.", "kind": "function", "line": 159, "name": "compute_curvatures", "signature": "def compute_curvatures(vertices, faces, grid_size)"}, {"kind": "function", "line": 189, "name": "save_obj", "signature": "def save_obj(vertices, faces, filepath)"}, {"kind": "function", "line": 197, "name": "save_html_viewer", "signature": "def save_html_viewer(orig_verts, orig_faces, pred_verts, pred_faces, output_path)"}, {"kind": "function", "line": 338, "name": "main", "signature": "def main()"}]}, {"doc": "rbc_model_reconstruction.py  Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.  The model processes 16x16 grids. We project the ENTIRE RBC mesh onto a single 16x16 spherical parametrization and run inference.  This shows what the model \"sees\" when given the RBC shape.", "id": "rbc.py", "kind": "module", "label": "rbc.py", "language": "py", "sha256": "e831b53be5be4a96", "symbol_count": 11, "symbols": [{"doc": "Load RBC mesh from OpenRBC files.", "kind": "function", "line": 30, "name": "load_rbc_mesh", "signature": "def load_rbc_mesh(vert_path, face_path)"}, {"doc": "Load the trained Willmore model from checkpoint.", "kind": "function", "line": 53, "name": "load_model", "signature": "def load_model(checkpoint_path, device, config)"}, {"doc": "Project entire RBC mesh onto a spherical coordinate grid.\n\nThis creates a single grid_size x grid_size representation\nthat the model can process.", "kind": "function", "line": 94, "name": "project_rbc_to_spherical_grid", "signature": "def project_rbc_to_spherical_grid(vertices, grid_size)"}, {"doc": "Convert spherical grid back to 3D vertices.", "kind": "function", "line": 139, "name": "spherical_grid_to_cartesian", "signature": "def spherical_grid_to_cartesian(r_grid, grid_size, scale)"}, {"doc": "Run model iteratively to evolve the surface.\n\nReturns the evolution trajectory.", "kind": "function", "line": 164, "name": "run_model_evolution", "signature": "def run_model_evolution(model, input_grid, steps, device)"}, {"doc": "Create a perfect sphere grid for comparison.", "kind": "function", "line": 202, "name": "create_sphere_grid", "signature": "def create_sphere_grid(grid_size, radius)"}, {"doc": "Create a biconcave disc shape on spherical grid.", "kind": "function", "line": 212, "name": "create_biconcave_grid", "signature": "def create_biconcave_grid(grid_size, radius)"}, {"doc": "Compute Willmore energy using MinimalSurfaceOperator.", "kind": "function", "line": 224, "name": "compute_willmore_on_grid", "signature": "def compute_willmore_on_grid(surface, grid_size)"}, {"doc": "Save mesh as OBJ file.", "kind": "function", "line": 231, "name": "save_obj", "signature": "def save_obj(vertices, faces, filepath)"}, {"doc": "Create interactive HTML comparing all shapes.", "kind": "function", "line": 240, "name": "save_html_comparison", "signature": "def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved_faces, sphere_vertices, sphere_faces, biconcave_vertices, biconcave_faces, willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave, output_path)"}, {"kind": "function", "line": 393, "name": "main", "signature": "def main()"}]}, {"doc": "rbc_model_reconstruction.py  Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.  The model processes 16x16 grids. We project the ENTIRE RBC mesh onto a single 16x16 spherical parametrization and run inference.  This shows what the model \"sees\" when given the RBC shape.", "id": "rbc_model_reconstruction (1).py", "kind": "module", "label": "rbc_model_reconstruction (1).py", "language": "py", "sha256": "0d7f35f7222dc9c2", "symbol_count": 11, "symbols": [{"doc": "Load RBC mesh from OpenRBC files.", "kind": "function", "line": 30, "name": "load_rbc_mesh", "signature": "def load_rbc_mesh(vert_path, face_path)"}, {"doc": "Load the trained Willmore model from checkpoint.", "kind": "function", "line": 53, "name": "load_model", "signature": "def load_model(checkpoint_path, device, config)"}, {"doc": "Project entire RBC mesh onto a spherical coordinate grid.\n\nThis creates a single grid_size x grid_size representation\nthat the model can process.", "kind": "function", "line": 94, "name": "project_rbc_to_spherical_grid", "signature": "def project_rbc_to_spherical_grid(vertices, grid_size)"}, {"doc": "Convert spherical grid back to 3D vertices.", "kind": "function", "line": 139, "name": "spherical_grid_to_cartesian", "signature": "def spherical_grid_to_cartesian(r_grid, grid_size, scale)"}, {"doc": "Run model iteratively to evolve the surface.\n\nReturns the evolution trajectory.", "kind": "function", "line": 164, "name": "run_model_evolution", "signature": "def run_model_evolution(model, input_grid, steps, device)"}, {"doc": "Create a perfect sphere grid for comparison.", "kind": "function", "line": 202, "name": "create_sphere_grid", "signature": "def create_sphere_grid(grid_size, radius)"}, {"doc": "Create a biconcave disc shape on spherical grid.", "kind": "function", "line": 212, "name": "create_biconcave_grid", "signature": "def create_biconcave_grid(grid_size, radius)"}, {"doc": "Compute Willmore energy using MinimalSurfaceOperator.", "kind": "function", "line": 224, "name": "compute_willmore_on_grid", "signature": "def compute_willmore_on_grid(surface, grid_size)"}, {"doc": "Save mesh as OBJ file.", "kind": "function", "line": 231, "name": "save_obj", "signature": "def save_obj(vertices, faces, filepath)"}, {"doc": "Create interactive HTML comparing all shapes.", "kind": "function", "line": 240, "name": "save_html_comparison", "signature": "def save_html_comparison(original_vertices, original_faces, rbc_grid_vertices, rbc_grid_faces, evolved_vertices, evolved_faces, sphere_vertices, sphere_faces, biconcave_vertices, biconcave_faces, willmore_rbc, willmore_evolved, willmore_sphere, willmore_biconcave, output_path)"}, {"kind": "function", "line": 393, "name": "main", "signature": "def main()"}]}, {"doc": "rbc_model_reconstruction.py  Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.  Uses the model to predict curvature/energy values for each vertex in the original RBC mesh from OpenRBC.  The visualization shows the ACTUAL RBC mesh colored by model predictions.", "id": "rbc_model_reconstruction.py", "kind": "module", "label": "rbc_model_reconstruction.py", "language": "py", "sha256": "4f7c592ba0b5db71", "symbol_count": 10, "symbols": [{"doc": "Load RBC mesh from OpenRBC files.", "kind": "function", "line": 31, "name": "load_rbc_mesh", "signature": "def load_rbc_mesh(vert_path, face_path)"}, {"doc": "Compute vertex normals.", "kind": "function", "line": 54, "name": "compute_vertex_normals", "signature": "def compute_vertex_normals(vertices, faces)"}, {"doc": "Compute face areas.", "kind": "function", "line": 75, "name": "compute_face_areas", "signature": "def compute_face_areas(vertices, faces)"}, {"doc": "Load the trained Willmore model from checkpoint.", "kind": "function", "line": 84, "name": "load_model", "signature": "def load_model(checkpoint_path, device, config)"}, {"doc": "Create local surface patches around each vertex for model input.\n\nFor each vertex, we create a small 2D grid representing the local\nsurface neighborhood, which can be processed by the model.", "kind": "function", "line": 124, "name": "create_local_patches_for_vertices", "signature": "def create_local_patches_for_vertices(vertices, faces, normals, grid_size)"}, {"doc": "Run the model on all vertex patches and extract predictions.\n\nReturns predicted curvature-like values for each vertex.", "kind": "function", "line": 215, "name": "run_model_on_patches", "signature": "def run_model_on_patches(model, patches_real, patches_imag, device, grid_size, batch_size)"}, {"doc": "Compute analytical mean curvature for comparison.", "kind": "function", "line": 252, "name": "compute_analytical_curvature", "signature": "def compute_analytical_curvature(vertices, faces)"}, {"doc": "Save mesh as PLY with scalar values as vertex colors.", "kind": "function", "line": 284, "name": "save_ply_with_values", "signature": "def save_ply_with_values(vertices, faces, normals, values, filepath, value_name)"}, {"doc": "Create interactive HTML viewer with model predictions on actual RBC mesh.", "kind": "function", "line": 319, "name": "save_html_viewer", "signature": "def save_html_viewer(vertices, faces, normals, model_curvature, analytical_curvature, output_path)"}, {"kind": "function", "line": 530, "name": "main", "signature": "def main()"}]}, {"doc": "rbc_model_reconstruction_128_v2.py  Red Blood Cell 3D Reconstruction USING THE SCALED WILLMORE MODEL at 128x128.  Improved version with better spherical parametrization that avoids artificial lobes and properly handles the biconcave RBC geometry.  Key improvements: - Area-weighted projection to avoid polar artifacts - Gaussian smoothing in spherical coordinates - Proper handling of the dimple regions - Better interpolation for sparse data", "id": "rbc_model_reconstruction_128.py", "kind": "module", "label": "rbc_model_reconstruction_128.py", "language": "py", "sha256": "6ea3fd3b853fac9d", "symbol_count": 46, "symbols": [{"doc": "Configuration for RBC reconstruction.", "kind": "class", "line": 37, "name": "ReconstructionConfig", "signature": "class ReconstructionConfig"}, {"doc": "Spectral convolution layer for minimal surface processing.", "kind": "class", "line": 51, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Spectral network for minimal surface computation.", "kind": "class", "line": 85, "name": "MinimalSurfaceSpectralNetwork", "signature": "class MinimalSurfaceSpectralNetwork(Module)"}, {"doc": "Handles loading of model checkpoints.", "kind": "class", "line": 120, "name": "CheckpointLoader", "signature": "class CheckpointLoader"}, {"doc": "Builds and initializes models from configuration.", "kind": "class", "line": 130, "name": "ModelBuilder", "signature": "class ModelBuilder"}, {"doc": "Loads RBC mesh data from OpenRBC format files.", "kind": "class", "line": 169, "name": "RBCMeshLoader", "signature": "class RBCMeshLoader"}, {"doc": "Improved spherical projection with proper handling of biconcave geometry.\n\nKey improvements:\n1. Area-weighted averaging to avoid oversampling at poles\n2. RBF interpolation for smooth reconstruction\n3. Proper handling of the dimple regions\n4. Gaussian smoothing in parameter space", "kind": "class", "line": 195, "name": "ImprovedSphericalProjector", "signature": "class ImprovedSphericalProjector"}, {"doc": "Cylindrical projection - often better for biconcave shapes.\n\nThe RBC is naturally more cylindrical than spherical,\nwith the dimples on top and bottom.", "kind": "class", "line": 377, "name": "CylindricalProjector", "signature": "class CylindricalProjector"}, {"doc": "Generates synthetic shapes for comparison.", "kind": "class", "line": 469, "name": "SyntheticShapeGenerator", "signature": "class SyntheticShapeGenerator"}, {"doc": "Calculates Willmore energy and curvature metrics.", "kind": "class", "line": 514, "name": "WillmoreMetricsCalculator", "signature": "class WillmoreMetricsCalculator"}, {"doc": "Evolves surfaces using the trained model.", "kind": "class", "line": 542, "name": "SurfaceEvolver", "signature": "class SurfaceEvolver"}, {"doc": "Exports meshes to various formats.", "kind": "class", "line": 589, "name": "MeshExporter", "signature": "class MeshExporter"}, {"doc": "Main pipeline for RBC reconstruction using scaled model.", "kind": "class", "line": 757, "name": "RBCReconstructionPipeline", "signature": "class RBCReconstructionPipeline"}, {"kind": "method", "line": 926, "name": "build_argument_parser", "signature": "def build_argument_parser()"}, {"kind": "method", "line": 989, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 54, "name": "__init__", "signature": "def __init__(self, channels, grid_size)"}, {"kind": "method", "line": 65, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 88, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)"}, {"kind": "method", "line": 109, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 124, "name": "load", "signature": "def load(checkpoint_path, device)"}, {"kind": "method", "line": 134, "name": "build", "signature": "def build(config)"}, {"kind": "method", "line": 145, "name": "load_from_checkpoint", "signature": "def load_from_checkpoint(checkpoint_path, config)"}, {"kind": "method", "line": 173, "name": "load", "signature": "def load(vert_path, face_path)"}, {"kind": "method", "line": 206, "name": "__init__", "signature": "def __init__(self, grid_size, smoothing_sigma)"}, {"doc": "Compute approximate area associated with each vertex.", "kind": "method", "line": 214, "name": "compute_vertex_areas", "signature": "def compute_vertex_areas(self, vertices, faces)"}, {"doc": "Project mesh onto spherical grid with proper area weighting.", "kind": "method", "line": 229, "name": "project_mesh", "signature": "def project_mesh(self, vertices, faces, use_rbf)"}, {"doc": "Project using area-weighted averaging.", "kind": "method", "line": 267, "name": "_area_weighted_projection", "signature": "def _area_weighted_projection(self, theta, phi, r, areas)"}, {"doc": "Use RBF interpolation for smooth reconstruction.", "kind": "method", "line": 300, "name": "_rbf_interpolation", "signature": "def _rbf_interpolation(self, theta, phi, r)"}, {"doc": "Apply Gaussian smoothing adapted to spherical coordinates.", "kind": "method", "line": 330, "name": "_apply_spherical_smoothing", "signature": "def _apply_spherical_smoothing(self, r_grid)"}, {"doc": "Convert spherical grid back to 3D vertices.", "kind": "method", "line": 352, "name": "to_cartesian", "signature": "def to_cartesian(self, r_grid, scale)"}, {"kind": "method", "line": 385, "name": "__init__", "signature": "def __init__(self, grid_size, smoothing_sigma)"}, {"doc": "Project mesh using cylindrical coordinates.", "kind": "method", "line": 393, "name": "project_mesh", "signature": "def project_mesh(self, vertices, faces)"}, {"doc": "Convert cylindrical grid back to 3D vertices.", "kind": "method", "line": 442, "name": "to_cartesian", "signature": "def to_cartesian(self, rho_grid, z_scale, rho_scale)"}, {"kind": "method", "line": 472, "name": "__init__", "signature": "def __init__(self, grid_size)"}, {"kind": "method", "line": 478, "name": "create_sphere", "signature": "def create_sphere(self, radius)"}, {"doc": "Create biconcave disc shape using Evans-Fung model.", "kind": "method", "line": 481, "name": "create_biconcave", "signature": "def create_biconcave(self, radius, dimple_depth)"}, {"doc": "Create RBC shape using Evans-Fung parametrization.\n\nThe RBC cross-section follows:\nr(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)\n\nThis creates the characteristic biconcave shape.", "kind": "method", "line": 487, "name": "create_evans_fung_rbc", "signature": "def create_evans_fung_rbc(self, radius, dimple_depth, thickness)"}, {"kind": "method", "line": 517, "name": "__init__", "signature": "def __init__(self, grid_size)"}, {"kind": "method", "line": 520, "name": "compute_willmore", "signature": "def compute_willmore(self, surface)"}, {"kind": "method", "line": 524, "name": "compute_curvature_stats", "signature": "def compute_curvature_stats(self, surface)"}, {"kind": "method", "line": 545, "name": "__init__", "signature": "def __init__(self, model, config)"}, {"kind": "method", "line": 553, "name": "evolve", "signature": "def evolve(self, initial_surface)"}, {"kind": "method", "line": 593, "name": "save_obj", "signature": "def save_obj(vertices, faces, filepath)"}, {"kind": "method", "line": 602, "name": "save_html_comparison", "signature": "def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolved_faces, biconcave_vertices, biconcave_faces, metrics, output_path)"}, {"kind": "method", "line": 760, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 771, "name": "run", "signature": "def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)"}]}, {"doc": "rbc_willmore_analysis.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3  Description: Red Blood Cell Morphology Analysis via Willmore Energy Minimization.  This script analyzes Red Blood Cell (RBC) membrane geometry using the Willmore energy model. The biconcave disc shape of healthy RBCs emerges naturally from minimizing the Willmore energy functional:  W = integral((H - H0)^2 dA)  where H is the mean curvature and H0 is the spontaneous curvature.  The analysis uses real RBC mesh data from OpenRBC (protein-resolution simulator) to validate whether the trained Willmore model can detect the characteristic biconcave shape and distinguish healthy from pathological morphologies.  Scientific basis: - Helfrich-Canham membrane bending energy model - Gauss-Bonnet theorem for closed surfaces - Mean curvature flow as shape relaxation dynamics - Differential geometry of membrane surfaces", "id": "rbc_willmore_analysis.py", "kind": "module", "label": "rbc_willmore_analysis.py", "language": "py", "sha256": "302ec998ee2c0e8a", "symbol_count": 87, "symbols": [{"doc": "Configuration container for RBC Willmore analysis.\n\nThis dataclass holds all configuration parameters for the analysis\npipeline, including mesh processing, model loading, and visualization\nsettings.", "kind": "class", "line": 55, "name": "RBCAnalysisConfig", "signature": "class RBCAnalysisConfig"}, {"doc": "Abstract interface for logging implementations.", "kind": "class", "line": 102, "name": "ILogger", "signature": "class ILogger(ABC)"}, {"doc": "Standard logging implementation using Python logging module.", "kind": "class", "line": 122, "name": "StandardLogger", "signature": "class StandardLogger(ILogger)"}, {"doc": "Abstract interface for file system operations.", "kind": "class", "line": 149, "name": "IFileSystem", "signature": "class IFileSystem(ABC)"}, {"doc": "Standard file system implementation.", "kind": "class", "line": 169, "name": "StandardFileSystem", "signature": "class StandardFileSystem(IFileSystem)"}, {"doc": "Container for 3D mesh data.\n\nAttributes:\n    vertices: Nx3 numpy array of vertex positions\n    faces: Mx3 numpy array of triangle face indices\n    bonds: Kx2 numpy array of bond edge indices\n    normals: Nx3 numpy array of vertex normals (computed)\n    areas: M numpy array of face areas (computed)", "kind": "class", "line": 188, "name": "MeshData", "signature": "class MeshData"}, {"doc": "Abstract interface for mesh loading implementations.", "kind": "class", "line": 228, "name": "IMeshLoader", "signature": "class IMeshLoader(ABC)"}, {"doc": "Mesh loader for OpenRBC format data files.\n\nOpenRBC stores mesh data in three separate text files:\n- rbc.vert.txt: Vertex positions (x, y, z per line)\n- rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)\n- rbc.bond.txt: Bond edges (2 vertex indices per line)", "kind": "class", "line": 236, "name": "OpenRBCMeshLoader", "signature": "class OpenRBCMeshLoader(IMeshLoader)"}, {"doc": "Generator for synthetic comparison surfaces.\n\nCreates reference surfaces (sphere, torus) for comparison with\nRBC morphology analysis.", "kind": "class", "line": 375, "name": "SyntheticMeshGenerator", "signature": "class SyntheticMeshGenerator"}, {"doc": "Abstract interface for curvature calculation implementations.", "kind": "class", "line": 545, "name": "ICurvatureCalculator", "signature": "class ICurvatureCalculator(ABC)"}, {"doc": "Discrete curvature calculation using the cotangent formula.\n\nImplements the discrete differential geometry approach for computing\nmean and Gaussian curvature on triangle meshes based on the work by\nMeyer et al. (2003) and others.\n\nThe mean curvature at a vertex is computed using the Laplace-Beltrami\noperator applied to the vertex positions:\n\n    H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)\n\nwhere A_i is the Voronoi area around vertex i.", "kind": "class", "line": 563, "name": "DiscreteCurvatureCalculator", "signature": "class DiscreteCurvatureCalculator(ICurvatureCalculator)"}, {"doc": "Spectral convolution layer for surface processing.\n\nImplements convolution in the frequency domain using FFT,\nallowing the network to learn global surface patterns.", "kind": "class", "line": 799, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for minimal surface detection and Willmore energy learning.\n\nThis network learns to predict mean curvature fields and identify\nminimal surface configurations through spectral convolution layers.", "kind": "class", "line": 848, "name": "MinimalSurfaceSpectralNetwork", "signature": "class MinimalSurfaceSpectralNetwork(Module)"}, {"doc": "Abstract interface for model loading implementations.", "kind": "class", "line": 894, "name": "IModelLoader", "signature": "class IModelLoader(ABC)"}, {"doc": "Model loader that loads from PyTorch checkpoint files.", "kind": "class", "line": 902, "name": "CheckpointModelLoader", "signature": "class CheckpointModelLoader(IModelLoader)"}, {"doc": "Main engine for RBC surface analysis using Willmore energy model.\n\nThis class orchestrates the complete analysis pipeline, from mesh loading\nto curvature computation and shape emergence testing.", "kind": "class", "line": 1002, "name": "SurfaceAnalysisEngine", "signature": "class SurfaceAnalysisEngine"}, {"kind": "method", "line": 1376, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 1470, "name": "create_config_from_args", "signature": "def create_config_from_args(args)"}, {"kind": "method", "line": 1488, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 106, "name": "info", "signature": "def info(self, message)"}, {"kind": "method", "line": 110, "name": "warning", "signature": "def warning(self, message)"}, {"kind": "method", "line": 114, "name": "error", "signature": "def error(self, message)"}, {"kind": "method", "line": 118, "name": "debug", "signature": "def debug(self, message)"}, {"kind": "method", "line": 125, "name": "__init__", "signature": "def __init__(self, name, level)"}, {"kind": "method", "line": 136, "name": "info", "signature": "def info(self, message)"}, {"kind": "method", "line": 139, "name": "warning", "signature": "def warning(self, message)"}, {"kind": "method", "line": 142, "name": "error", "signature": "def error(self, message)"}, {"kind": "method", "line": 145, "name": "debug", "signature": "def debug(self, message)"}, {"kind": "method", "line": 153, "name": "exists", "signature": "def exists(self, path)"}, {"kind": "method", "line": 157, "name": "read_text", "signature": "def read_text(self, path)"}, {"kind": "method", "line": 161, "name": "write_text", "signature": "def write_text(self, path, content)"}, {"kind": "method", "line": 165, "name": "makedirs", "signature": "def makedirs(self, path)"}, {"kind": "method", "line": 172, "name": "exists", "signature": "def exists(self, path)"}, {"kind": "method", "line": 175, "name": "read_text", "signature": "def read_text(self, path)"}, {"kind": "method", "line": 179, "name": "write_text", "signature": "def write_text(self, path, content)"}, {"kind": "method", "line": 183, "name": "makedirs", "signature": "def makedirs(self, path)"}, {"kind": "method", "line": 206, "name": "num_vertices", "signature": "def num_vertices(self)"}, {"kind": "method", "line": 210, "name": "num_faces", "signature": "def num_faces(self)"}, {"kind": "method", "line": 214, "name": "num_bonds", "signature": "def num_bonds(self)"}, {"kind": "method", "line": 217, "name": "to_dict", "signature": "def to_dict(self)"}, {"kind": "method", "line": 232, "name": "load", "signature": "def load(self, vert_path, face_path, bond_path)"}, {"kind": "method", "line": 245, "name": "__init__", "signature": "def __init__(self, filesystem, logger)"}, {"kind": "method", "line": 249, "name": "load", "signature": "def load(self, vert_path, face_path, bond_path)"}, {"kind": "method", "line": 267, "name": "_load_vertices", "signature": "def _load_vertices(self, path)"}, {"kind": "method", "line": 286, "name": "_load_faces", "signature": "def _load_faces(self, path)"}, {"kind": "method", "line": 308, "name": "_load_bonds", "signature": "def _load_bonds(self, path)"}, {"kind": "method", "line": 330, "name": "_compute_normals", "signature": "def _compute_normals(self, mesh)"}, {"kind": "method", "line": 355, "name": "_compute_areas", "signature": "def _compute_areas(self, mesh)"}, {"kind": "method", "line": 382, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 385, "name": "generate_sphere", "signature": "def generate_sphere(self, radius, resolution)"}, {"kind": "method", "line": 424, "name": "generate_torus", "signature": "def generate_torus(self, R, r, resolution)"}, {"kind": "method", "line": 467, "name": "generate_biconcave_disc", "signature": "def generate_biconcave_disc(self, radius, thickness, resolution)"}, {"kind": "method", "line": 511, "name": "_compute_mesh_properties", "signature": "def _compute_mesh_properties(self, mesh)"}, {"kind": "method", "line": 549, "name": "compute_mean_curvature", "signature": "def compute_mean_curvature(self, mesh)"}, {"kind": "method", "line": 553, "name": "compute_gaussian_curvature", "signature": "def compute_gaussian_curvature(self, mesh)"}, {"kind": "method", "line": 557, "name": "compute_willmore_energy", "signature": "def compute_willmore_energy(self, mesh, mean_curvature)"}, {"kind": "method", "line": 578, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 581, "name": "compute_mean_curvature", "signature": "def compute_mean_curvature(self, mesh)"}, {"kind": "method", "line": 616, "name": "compute_gaussian_curvature", "signature": "def compute_gaussian_curvature(self, mesh)"}, {"kind": "method", "line": 664, "name": "compute_willmore_energy", "signature": "def compute_willmore_energy(self, mesh, mean_curvature)"}, {"kind": "method", "line": 682, "name": "_compute_edge_cotangents", "signature": "def _compute_edge_cotangents(self, mesh)"}, {"kind": "method", "line": 737, "name": "_get_vertex_neighbors", "signature": "def _get_vertex_neighbors(self, vertex_idx, faces)"}, {"kind": "method", "line": 748, "name": "_compute_mixed_voronoi_area", "signature": "def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)"}, {"kind": "method", "line": 806, "name": "__init__", "signature": "def __init__(self, channels, grid_size)"}, {"kind": "method", "line": 820, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 855, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)"}, {"kind": "method", "line": 880, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 898, "name": "load", "signature": "def load(self, checkpoint_path, device, config)"}, {"kind": "method", "line": 905, "name": "__init__", "signature": "def __init__(self, filesystem, logger)"}, {"kind": "method", "line": 909, "name": "_detect_model_params", "signature": "def _detect_model_params(self, state_dict)"}, {"kind": "method", "line": 947, "name": "load", "signature": "def load(self, checkpoint_path, device, config)"}, {"kind": "method", "line": 1009, "name": "__init__", "signature": "def __init__(self, config, logger, filesystem)"}, {"kind": "method", "line": 1028, "name": "initialize", "signature": "def initialize(self)"}, {"kind": "method", "line": 1048, "name": "_load_rbc_mesh", "signature": "def _load_rbc_mesh(self)"}, {"kind": "method", "line": 1060, "name": "_generate_synthetic_meshes", "signature": "def _generate_synthetic_meshes(self)"}, {"kind": "method", "line": 1076, "name": "analyze_mesh", "signature": "def analyze_mesh(self, mesh, name)"}, {"kind": "method", "line": 1125, "name": "_compute_surface_area", "signature": "def _compute_surface_area(self, mesh)"}, {"kind": "method", "line": 1130, "name": "_compute_volume", "signature": "def _compute_volume(self, mesh)"}, {"kind": "method", "line": 1141, "name": "_compute_asphericity", "signature": "def _compute_asphericity(self, mesh)"}, {"kind": "method", "line": 1161, "name": "_compute_biconcavity_index", "signature": "def _compute_biconcavity_index(self, mesh, mean_curvature)"}, {"kind": "method", "line": 1186, "name": "_compute_histogram", "signature": "def _compute_histogram(self, data, bins)"}, {"kind": "method", "line": 1192, "name": "run_shape_emergence_test", "signature": "def run_shape_emergence_test(self)"}, {"kind": "method", "line": 1235, "name": "_analyze_rbc_morphology", "signature": "def _analyze_rbc_morphology(self)"}, {"kind": "method", "line": 1277, "name": "_verify_gauss_bonnet", "signature": "def _verify_gauss_bonnet(self)"}, {"kind": "method", "line": 1318, "name": "run_mean_curvature_flow", "signature": "def run_mean_curvature_flow(self, mesh, steps, dt)"}, {"kind": "method", "line": 1357, "name": "save_results", "signature": "def save_results(self, results, filename)"}, {"kind": "method", "line": 1362, "name": "save_mesh_obj", "signature": "def save_mesh_obj(self, mesh, filename)"}]}, {"doc": "rbc_willmore_analysis.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3  Description: Red Blood Cell Morphology Analysis via Willmore Energy Minimization.  This script analyzes Red Blood Cell (RBC) membrane geometry using the Willmore energy model. The biconcave disc shape of healthy RBCs emerges naturally from minimizing the Willmore energy functional:  W = integral((H - H0)^2 dA)  where H is the mean curvature and H0 is the spontaneous curvature.  The analysis uses real RBC mesh data from OpenRBC (protein-resolution simulator) to validate whether the trained Willmore model can detect the characteristic biconcave shape and distinguish healthy from pathological morphologies.  Scientific basis: - Helfrich-Canham membrane bending energy model - Gauss-Bonnet theorem for closed surfaces - Mean curvature flow as shape relaxation dynamics - Differential geometry of membrane surfaces", "id": "rbc_willmore_analysis2.py", "kind": "module", "label": "rbc_willmore_analysis2.py", "language": "py", "sha256": "5acf56f8a9693537", "symbol_count": 88, "symbols": [{"doc": "Configuration container for RBC Willmore analysis.\n\nThis dataclass holds all configuration parameters for the analysis\npipeline, including mesh processing, model loading, and visualization\nsettings.", "kind": "class", "line": 55, "name": "RBCAnalysisConfig", "signature": "class RBCAnalysisConfig"}, {"doc": "Abstract interface for logging implementations.", "kind": "class", "line": 102, "name": "ILogger", "signature": "class ILogger(ABC)"}, {"doc": "Standard logging implementation using Python logging module.", "kind": "class", "line": 122, "name": "StandardLogger", "signature": "class StandardLogger(ILogger)"}, {"doc": "Abstract interface for file system operations.", "kind": "class", "line": 149, "name": "IFileSystem", "signature": "class IFileSystem(ABC)"}, {"doc": "Standard file system implementation.", "kind": "class", "line": 169, "name": "StandardFileSystem", "signature": "class StandardFileSystem(IFileSystem)"}, {"doc": "Container for 3D mesh data.\n\nAttributes:\n    vertices: Nx3 numpy array of vertex positions\n    faces: Mx3 numpy array of triangle face indices\n    bonds: Kx2 numpy array of bond edge indices\n    normals: Nx3 numpy array of vertex normals (computed)\n    areas: M numpy array of face areas (computed)", "kind": "class", "line": 188, "name": "MeshData", "signature": "class MeshData"}, {"doc": "Abstract interface for mesh loading implementations.", "kind": "class", "line": 228, "name": "IMeshLoader", "signature": "class IMeshLoader(ABC)"}, {"doc": "Mesh loader for OpenRBC format data files.\n\nOpenRBC stores mesh data in three separate text files:\n- rbc.vert.txt: Vertex positions (x, y, z per line)\n- rbc.face.txt: Triangle faces (3 vertex indices per line, 1-indexed)\n- rbc.bond.txt: Bond edges (2 vertex indices per line)", "kind": "class", "line": 236, "name": "OpenRBCMeshLoader", "signature": "class OpenRBCMeshLoader(IMeshLoader)"}, {"doc": "Generator for synthetic comparison surfaces.\n\nCreates reference surfaces (sphere, torus) for comparison with\nRBC morphology analysis.", "kind": "class", "line": 375, "name": "SyntheticMeshGenerator", "signature": "class SyntheticMeshGenerator"}, {"doc": "Abstract interface for curvature calculation implementations.", "kind": "class", "line": 545, "name": "ICurvatureCalculator", "signature": "class ICurvatureCalculator(ABC)"}, {"doc": "Discrete curvature calculation using the cotangent formula.\n\nImplements the discrete differential geometry approach for computing\nmean and Gaussian curvature on triangle meshes based on the work by\nMeyer et al. (2003) and others.\n\nThe mean curvature at a vertex is computed using the Laplace-Beltrami\noperator applied to the vertex positions:\n\n    H_i * n_i = (1 / 2A_i) * sum_j (cot(alpha_j) + cot(beta_j)) * (v_i - v_j)\n\nwhere A_i is the Voronoi area around vertex i.", "kind": "class", "line": 563, "name": "DiscreteCurvatureCalculator", "signature": "class DiscreteCurvatureCalculator(ICurvatureCalculator)"}, {"doc": "Spectral convolution layer for surface processing.\n\nImplements convolution in the frequency domain using FFT,\nallowing the network to learn global surface patterns.", "kind": "class", "line": 799, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for minimal surface detection and Willmore energy learning.\n\nThis network learns to predict mean curvature fields and identify\nminimal surface configurations through spectral convolution layers.", "kind": "class", "line": 848, "name": "MinimalSurfaceSpectralNetwork", "signature": "class MinimalSurfaceSpectralNetwork(Module)"}, {"doc": "Abstract interface for model loading implementations.", "kind": "class", "line": 894, "name": "IModelLoader", "signature": "class IModelLoader(ABC)"}, {"doc": "Model loader that loads from PyTorch checkpoint files.", "kind": "class", "line": 902, "name": "CheckpointModelLoader", "signature": "class CheckpointModelLoader(IModelLoader)"}, {"doc": "Main engine for RBC surface analysis using Willmore energy model.\n\nThis class orchestrates the complete analysis pipeline, from mesh loading\nto curvature computation and shape emergence testing.", "kind": "class", "line": 1002, "name": "SurfaceAnalysisEngine", "signature": "class SurfaceAnalysisEngine"}, {"kind": "method", "line": 1394, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 1488, "name": "create_config_from_args", "signature": "def create_config_from_args(args)"}, {"kind": "method", "line": 1506, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 106, "name": "info", "signature": "def info(self, message)"}, {"kind": "method", "line": 110, "name": "warning", "signature": "def warning(self, message)"}, {"kind": "method", "line": 114, "name": "error", "signature": "def error(self, message)"}, {"kind": "method", "line": 118, "name": "debug", "signature": "def debug(self, message)"}, {"kind": "method", "line": 125, "name": "__init__", "signature": "def __init__(self, name, level)"}, {"kind": "method", "line": 136, "name": "info", "signature": "def info(self, message)"}, {"kind": "method", "line": 139, "name": "warning", "signature": "def warning(self, message)"}, {"kind": "method", "line": 142, "name": "error", "signature": "def error(self, message)"}, {"kind": "method", "line": 145, "name": "debug", "signature": "def debug(self, message)"}, {"kind": "method", "line": 153, "name": "exists", "signature": "def exists(self, path)"}, {"kind": "method", "line": 157, "name": "read_text", "signature": "def read_text(self, path)"}, {"kind": "method", "line": 161, "name": "write_text", "signature": "def write_text(self, path, content)"}, {"kind": "method", "line": 165, "name": "makedirs", "signature": "def makedirs(self, path)"}, {"kind": "method", "line": 172, "name": "exists", "signature": "def exists(self, path)"}, {"kind": "method", "line": 175, "name": "read_text", "signature": "def read_text(self, path)"}, {"kind": "method", "line": 179, "name": "write_text", "signature": "def write_text(self, path, content)"}, {"kind": "method", "line": 183, "name": "makedirs", "signature": "def makedirs(self, path)"}, {"kind": "method", "line": 206, "name": "num_vertices", "signature": "def num_vertices(self)"}, {"kind": "method", "line": 210, "name": "num_faces", "signature": "def num_faces(self)"}, {"kind": "method", "line": 214, "name": "num_bonds", "signature": "def num_bonds(self)"}, {"kind": "method", "line": 217, "name": "to_dict", "signature": "def to_dict(self)"}, {"kind": "method", "line": 232, "name": "load", "signature": "def load(self, vert_path, face_path, bond_path)"}, {"kind": "method", "line": 245, "name": "__init__", "signature": "def __init__(self, filesystem, logger)"}, {"kind": "method", "line": 249, "name": "load", "signature": "def load(self, vert_path, face_path, bond_path)"}, {"kind": "method", "line": 267, "name": "_load_vertices", "signature": "def _load_vertices(self, path)"}, {"kind": "method", "line": 286, "name": "_load_faces", "signature": "def _load_faces(self, path)"}, {"kind": "method", "line": 308, "name": "_load_bonds", "signature": "def _load_bonds(self, path)"}, {"kind": "method", "line": 330, "name": "_compute_normals", "signature": "def _compute_normals(self, mesh)"}, {"kind": "method", "line": 355, "name": "_compute_areas", "signature": "def _compute_areas(self, mesh)"}, {"kind": "method", "line": 382, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 385, "name": "generate_sphere", "signature": "def generate_sphere(self, radius, resolution)"}, {"kind": "method", "line": 424, "name": "generate_torus", "signature": "def generate_torus(self, R, r, resolution)"}, {"kind": "method", "line": 467, "name": "generate_biconcave_disc", "signature": "def generate_biconcave_disc(self, radius, thickness, resolution)"}, {"kind": "method", "line": 511, "name": "_compute_mesh_properties", "signature": "def _compute_mesh_properties(self, mesh)"}, {"kind": "method", "line": 549, "name": "compute_mean_curvature", "signature": "def compute_mean_curvature(self, mesh)"}, {"kind": "method", "line": 553, "name": "compute_gaussian_curvature", "signature": "def compute_gaussian_curvature(self, mesh)"}, {"kind": "method", "line": 557, "name": "compute_willmore_energy", "signature": "def compute_willmore_energy(self, mesh, mean_curvature)"}, {"kind": "method", "line": 578, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 581, "name": "compute_mean_curvature", "signature": "def compute_mean_curvature(self, mesh)"}, {"kind": "method", "line": 616, "name": "compute_gaussian_curvature", "signature": "def compute_gaussian_curvature(self, mesh)"}, {"kind": "method", "line": 664, "name": "compute_willmore_energy", "signature": "def compute_willmore_energy(self, mesh, mean_curvature)"}, {"kind": "method", "line": 682, "name": "_compute_edge_cotangents", "signature": "def _compute_edge_cotangents(self, mesh)"}, {"kind": "method", "line": 737, "name": "_get_vertex_neighbors", "signature": "def _get_vertex_neighbors(self, vertex_idx, faces)"}, {"kind": "method", "line": 748, "name": "_compute_mixed_voronoi_area", "signature": "def _compute_mixed_voronoi_area(self, vertex_idx, neighbors, vertices, faces)"}, {"kind": "method", "line": 806, "name": "__init__", "signature": "def __init__(self, channels, grid_size)"}, {"kind": "method", "line": 820, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 855, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)"}, {"kind": "method", "line": 880, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 898, "name": "load", "signature": "def load(self, checkpoint_path, device, config)"}, {"kind": "method", "line": 905, "name": "__init__", "signature": "def __init__(self, filesystem, logger)"}, {"kind": "method", "line": 909, "name": "_detect_model_params", "signature": "def _detect_model_params(self, state_dict)"}, {"kind": "method", "line": 947, "name": "load", "signature": "def load(self, checkpoint_path, device, config)"}, {"kind": "method", "line": 1009, "name": "__init__", "signature": "def __init__(self, config, logger, filesystem)"}, {"kind": "method", "line": 1028, "name": "initialize", "signature": "def initialize(self)"}, {"kind": "method", "line": 1048, "name": "_load_rbc_mesh", "signature": "def _load_rbc_mesh(self)"}, {"kind": "method", "line": 1060, "name": "_generate_synthetic_meshes", "signature": "def _generate_synthetic_meshes(self)"}, {"kind": "method", "line": 1076, "name": "analyze_mesh", "signature": "def analyze_mesh(self, mesh, name)"}, {"kind": "method", "line": 1125, "name": "_compute_surface_area", "signature": "def _compute_surface_area(self, mesh)"}, {"kind": "method", "line": 1130, "name": "_compute_volume", "signature": "def _compute_volume(self, mesh)"}, {"kind": "method", "line": 1141, "name": "_compute_asphericity", "signature": "def _compute_asphericity(self, mesh)"}, {"kind": "method", "line": 1161, "name": "_compute_biconcavity_index", "signature": "def _compute_biconcavity_index(self, mesh, mean_curvature)"}, {"kind": "method", "line": 1186, "name": "_compute_histogram", "signature": "def _compute_histogram(self, data, bins)"}, {"kind": "method", "line": 1192, "name": "run_shape_emergence_test", "signature": "def run_shape_emergence_test(self)"}, {"kind": "method", "line": 1235, "name": "_analyze_rbc_morphology", "signature": "def _analyze_rbc_morphology(self)"}, {"kind": "method", "line": 1277, "name": "_verify_gauss_bonnet", "signature": "def _verify_gauss_bonnet(self)"}, {"kind": "method", "line": 1318, "name": "run_mean_curvature_flow", "signature": "def run_mean_curvature_flow(self, mesh, steps, dt)"}, {"kind": "method", "line": 1357, "name": "save_results", "signature": "def save_results(self, results, filename)"}, {"kind": "method", "line": 1380, "name": "save_mesh_obj", "signature": "def save_mesh_obj(self, mesh, filename)"}, {"kind": "method", "line": 1360, "name": "convert_to_native", "signature": "def convert_to_native(obj)"}]}, {"doc": "diagnose_model.py  Diagnóstico CORREGIDO: El modelo SÍ aprendió, pero trabaja en escala pequeña. La forma emerge de la estructura, no del valor absoluto.", "id": "test.py", "kind": "module", "label": "test.py", "language": "py", "sha256": "80a5c802b3251b05", "symbol_count": 3, "symbols": [{"kind": "function", "line": 20, "name": "load_model", "signature": "def load_model(checkpoint_path, device)"}, {"doc": "Test que respeta la escala pequeña del modelo.", "kind": "function", "line": 45, "name": "test_model_behavior", "signature": "def test_model_behavior(model, config, device)"}, {"kind": "function", "line": 154, "name": "main", "signature": "def main()"}]}, {"doc": "willmore_crystal.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date of creation: 2026 License: AGPL v3  Description: Surface Tension and Willmore Energy Grokking via Minimal Surface Topological Crystallization. Based on the physical law that governs soap bubble formation: - Mean Curvature H = 0 (minimal surfaces) - Willmore Energy: W = integral(H^2 dA) - Surface Tension minimization  The training of neural networks is modeled as a Ricci flow in weight space, where regularization acts as surface tension and discrete algorithms are minimal surfaces (hyperspheres of Perelman) that emerge as low-entropy attractors.  Five-phase protocol: Phase 1 - Batch size prospecting Phase 2 - Seed mining with decreasing delta criterion Phase 3 - Full training of best seed + batch size until grokking Phase 4 - Refinement via simulated annealing toward crystal state Phase 5 - Quadruple precision (float128) high-pressure crystallization", "id": "willmore_crsital2.py", "kind": "module", "label": "willmore_crsital2.py", "language": "py", "sha256": "c9daaa78320a675c", "symbol_count": 174, "symbols": [{"kind": "class", "line": 53, "name": "Config", "signature": "class Config"}, {"kind": "class", "line": 201, "name": "IPhaseDetector", "signature": "class IPhaseDetector(ABC)"}, {"kind": "class", "line": 207, "name": "IMetricCalculator", "signature": "class IMetricCalculator(ABC)"}, {"kind": "class", "line": 213, "name": "SeedManager", "signature": "class SeedManager"}, {"kind": "class", "line": 227, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"kind": "class", "line": 242, "name": "MinimalSurfaceOperator", "signature": "class MinimalSurfaceOperator"}, {"kind": "class", "line": 307, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"kind": "class", "line": 331, "name": "MinimalSurfaceBackbone", "signature": "class MinimalSurfaceBackbone(Module)"}, {"kind": "class", "line": 351, "name": "MinimalSurfaceInferenceEngine", "signature": "class MinimalSurfaceInferenceEngine"}, {"kind": "class", "line": 399, "name": "SurfacePotentialGenerator", "signature": "class SurfacePotentialGenerator"}, {"kind": "class", "line": 452, "name": "MinimalSurfaceDataset", "signature": "class MinimalSurfaceDataset(Dataset)"}, {"kind": "class", "line": 539, "name": "MinimalSurfaceSpectralNetwork", "signature": "class MinimalSurfaceSpectralNetwork(Module)"}, {"kind": "class", "line": 567, "name": "WillmoreEnergyCalculator", "signature": "class WillmoreEnergyCalculator(IMetricCalculator)"}, {"kind": "class", "line": 622, "name": "RicciFlowCalculator", "signature": "class RicciFlowCalculator(IMetricCalculator)"}, {"kind": "class", "line": 668, "name": "FullFourierAnalyzer", "signature": "class FullFourierAnalyzer"}, {"kind": "class", "line": 711, "name": "FourierMassCenterAnalyzer", "signature": "class FourierMassCenterAnalyzer"}, {"kind": "class", "line": 751, "name": "TopologicalPhaseDetector", "signature": "class TopologicalPhaseDetector(IPhaseDetector)"}, {"kind": "class", "line": 780, "name": "SpectralFieldExtractor", "signature": "class SpectralFieldExtractor"}, {"kind": "class", "line": 798, "name": "TopologicalMetricsCalculator", "signature": "class TopologicalMetricsCalculator(IMetricCalculator)"}, {"kind": "class", "line": 818, "name": "LocalComplexityAnalyzer", "signature": "class LocalComplexityAnalyzer"}, {"kind": "class", "line": 833, "name": "SuperpositionAnalyzer", "signature": "class SuperpositionAnalyzer"}, {"kind": "class", "line": 851, "name": "CrystallographyMetricsCalculator", "signature": "class CrystallographyMetricsCalculator(IMetricCalculator)"}, {"kind": "class", "line": 965, "name": "ThermodynamicMetricsCalculator", "signature": "class ThermodynamicMetricsCalculator(IMetricCalculator)"}, {"kind": "class", "line": 1021, "name": "SpectralGeometryCalculator", "signature": "class SpectralGeometryCalculator(IMetricCalculator)"}, {"kind": "class", "line": 1044, "name": "RicciCurvatureCalculator", "signature": "class RicciCurvatureCalculator(IMetricCalculator)"}, {"kind": "class", "line": 1065, "name": "SpectroscopyMetricsCalculator", "signature": "class SpectroscopyMetricsCalculator(IMetricCalculator)"}, {"kind": "class", "line": 1082, "name": "LambdaPressureScheduler", "signature": "class LambdaPressureScheduler"}, {"kind": "class", "line": 1114, "name": "AdaptiveLambdaScheduler", "signature": "class AdaptiveLambdaScheduler(LambdaPressureScheduler)"}, {"kind": "class", "line": 1129, "name": "QuadruplePrecisionLambdaScheduler", "signature": "class QuadruplePrecisionLambdaScheduler"}, {"kind": "class", "line": 1161, "name": "AnnealingScheduler", "signature": "class AnnealingScheduler"}, {"kind": "class", "line": 1186, "name": "TopologicalAnnealingScheduler", "signature": "class TopologicalAnnealingScheduler(AnnealingScheduler)"}, {"kind": "class", "line": 1202, "name": "TrainingMetricsMonitor", "signature": "class TrainingMetricsMonitor"}, {"kind": "class", "line": 1261, "name": "CheckpointManager", "signature": "class CheckpointManager"}, {"kind": "class", "line": 1291, "name": "Phase5CheckpointManager", "signature": "class Phase5CheckpointManager"}, {"kind": "class", "line": 1322, "name": "WeightIntegrityChecker", "signature": "class WeightIntegrityChecker"}, {"kind": "class", "line": 1338, "name": "TrainingEngine", "signature": "class TrainingEngine"}, {"kind": "class", "line": 1447, "name": "BatchSizeProspector", "signature": "class BatchSizeProspector"}, {"kind": "class", "line": 1483, "name": "SeedMiner", "signature": "class SeedMiner"}, {"kind": "class", "line": 1533, "name": "FullTrainingOrchestrator", "signature": "class FullTrainingOrchestrator"}, {"kind": "class", "line": 1599, "name": "RefinementOrchestrator", "signature": "class RefinementOrchestrator"}, {"kind": "class", "line": 1663, "name": "Phase5Orchestrator", "signature": "class Phase5Orchestrator"}, {"kind": "class", "line": 1725, "name": "ExperimentOrchestrator", "signature": "class ExperimentOrchestrator"}, {"kind": "method", "line": 1839, "name": "build_argument_parser", "signature": "def build_argument_parser()"}, {"kind": "method", "line": 1868, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 203, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"kind": "method", "line": 209, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 215, "name": "set_seed", "signature": "def set_seed(seed, device)"}, {"kind": "method", "line": 229, "name": "create_logger", "signature": "def create_logger(name, level)"}, {"kind": "method", "line": 243, "name": "__init__", "signature": "def __init__(self, grid_size)"}, {"kind": "method", "line": 249, "name": "_precompute_spectral_operators", "signature": "def _precompute_spectral_operators(self)"}, {"kind": "method", "line": 257, "name": "apply_laplacian", "signature": "def apply_laplacian(self, field)"}, {"kind": "method", "line": 262, "name": "compute_mean_curvature", "signature": "def compute_mean_curvature(self, surface)"}, {"kind": "method", "line": 273, "name": "compute_gaussian_curvature", "signature": "def compute_gaussian_curvature(self, surface)"}, {"kind": "method", "line": 284, "name": "compute_willmore_energy", "signature": "def compute_willmore_energy(self, surface)"}, {"kind": "method", "line": 290, "name": "compute_surface_area", "signature": "def compute_surface_area(self, surface)"}, {"kind": "method", "line": 297, "name": "mean_curvature_flow", "signature": "def mean_curvature_flow(self, surface, dt)"}, {"kind": "method", "line": 308, "name": "__init__", "signature": "def __init__(self, channels, grid_size)"}, {"kind": "method", "line": 315, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 332, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, num_spectral_layers)"}, {"kind": "method", "line": 342, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 352, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 359, "name": "_try_load_backbone", "signature": "def _try_load_backbone(self)"}, {"kind": "method", "line": 382, "name": "apply_mean_curvature", "signature": "def apply_mean_curvature(self, surface)"}, {"kind": "method", "line": 388, "name": "mean_curvature_evolve", "signature": "def mean_curvature_evolve(self, surface, dt)"}, {"kind": "method", "line": 400, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 404, "name": "pyramid_potential", "signature": "def pyramid_potential(self)"}, {"kind": "method", "line": 411, "name": "cube_potential", "signature": "def cube_potential(self)"}, {"kind": "method", "line": 418, "name": "dodecahedron_potential", "signature": "def dodecahedron_potential(self)"}, {"kind": "method", "line": 426, "name": "torus_potential", "signature": "def torus_potential(self)"}, {"kind": "method", "line": 434, "name": "hyperbolic_potential", "signature": "def hyperbolic_potential(self)"}, {"kind": "method", "line": 442, "name": "generate_mixed_potential", "signature": "def generate_mixed_potential(self, seed)"}, {"kind": "method", "line": 453, "name": "__init__", "signature": "def __init__(self, config, surface_engine, seed)"}, {"kind": "method", "line": 487, "name": "_solve_minimal_surface", "signature": "def _solve_minimal_surface(self, potential, sample_seed)"}, {"kind": "method", "line": 513, "name": "_evolve_minimal_surface", "signature": "def _evolve_minimal_surface(self, surface_real, surface_imag, potential, energy)"}, {"kind": "method", "line": 534, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 535, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 536, "name": "get_validation_batch", "signature": "def get_validation_batch(self)"}, {"kind": "method", "line": 540, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)"}, {"kind": "method", "line": 557, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 568, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 573, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 590, "name": "compute_surface_metrics", "signature": "def compute_surface_metrics(self, surface)"}, {"kind": "method", "line": 618, "name": "_empty_metrics", "signature": "def _empty_metrics()"}, {"kind": "method", "line": 623, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 627, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 640, "name": "_compute_ricci_scalar", "signature": "def _compute_ricci_scalar(self, metric)"}, {"kind": "method", "line": 647, "name": "_estimate_sectional_curvatures", "signature": "def _estimate_sectional_curvatures(self, metric)"}, {"kind": "method", "line": 659, "name": "_compute_flow_velocity", "signature": "def _compute_flow_velocity(self, metric)"}, {"kind": "method", "line": 664, "name": "_empty_metrics", "signature": "def _empty_metrics()"}, {"kind": "method", "line": 669, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 677, "name": "compute_full_spectrum", "signature": "def compute_full_spectrum(self, spectral_field)"}, {"kind": "method", "line": 701, "name": "compute_resonance_metrics", "signature": "def compute_resonance_metrics(self, spectral_field)"}, {"kind": "method", "line": 712, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 720, "name": "_get_freq_grids", "signature": "def _get_freq_grids(self, H, W, device)"}, {"kind": "method", "line": 728, "name": "compute_mass_center", "signature": "def compute_mass_center(self, spectral_field)"}, {"kind": "method", "line": 752, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 759, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"kind": "method", "line": 782, "name": "extract", "signature": "def extract(model, grid_size)"}, {"kind": "method", "line": 799, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 804, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 814, "name": "_empty_metrics", "signature": "def _empty_metrics()"}, {"kind": "method", "line": 820, "name": "compute_local_complexity", "signature": "def compute_local_complexity(weights, epsilon)"}, {"kind": "method", "line": 835, "name": "compute_superposition", "signature": "def compute_superposition(weights)"}, {"kind": "method", "line": 852, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 856, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 861, "name": "compute_kappa", "signature": "def compute_kappa(self, model, val_x, val_y, num_batches)"}, {"kind": "method", "line": 903, "name": "compute_discretization_margin", "signature": "def compute_discretization_margin(self, model)"}, {"kind": "method", "line": 911, "name": "compute_alpha_purity", "signature": "def compute_alpha_purity(self, model)"}, {"kind": "method", "line": 916, "name": "compute_kappa_quantum", "signature": "def compute_kappa_quantum(self, model)"}, {"kind": "method", "line": 935, "name": "compute_poynting_vector", "signature": "def compute_poynting_vector(self, model)"}, {"kind": "method", "line": 946, "name": "compute_hbar_effective", "signature": "def compute_hbar_effective(self, model, lambda_pressure)"}, {"kind": "method", "line": 953, "name": "compute_all_metrics", "signature": "def compute_all_metrics(self, model, val_x, val_y)"}, {"kind": "method", "line": 966, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 969, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 983, "name": "compute_effective_temperature", "signature": "def compute_effective_temperature(self, gradient_buffer, learning_rate)"}, {"kind": "method", "line": 1001, "name": "compute_specific_heat", "signature": "def compute_specific_heat(self, loss_history, temp_history)"}, {"kind": "method", "line": 1010, "name": "compute_gibbs_free_energy", "signature": "def compute_gibbs_free_energy(self, delta, alpha, temperature)"}, {"kind": "method", "line": 1017, "name": "compute_critical_temperature", "signature": "def compute_critical_temperature(self, alpha)"}, {"kind": "method", "line": 1022, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1025, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 1045, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1048, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 1066, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1069, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 1083, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1092, "name": "current_lambda", "signature": "def current_lambda(self)"}, {"kind": "method", "line": 1095, "name": "step", "signature": "def step(self, epoch)"}, {"kind": "method", "line": 1102, "name": "compute_regularization_loss", "signature": "def compute_regularization_loss(self, model)"}, {"kind": "method", "line": 1110, "name": "set_lambda", "signature": "def set_lambda(self, value)"}, {"kind": "method", "line": 1115, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1120, "name": "step_adaptive", "signature": "def step_adaptive(self, epoch, topo_phase_state)"}, {"kind": "method", "line": 1130, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1139, "name": "current_lambda", "signature": "def current_lambda(self)"}, {"kind": "method", "line": 1142, "name": "step", "signature": "def step(self, epoch, improvement)"}, {"kind": "method", "line": 1149, "name": "compute_regularization_loss", "signature": "def compute_regularization_loss(self, model)"}, {"kind": "method", "line": 1157, "name": "set_lambda", "signature": "def set_lambda(self, value)"}, {"kind": "method", "line": 1162, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1170, "name": "temperature", "signature": "def temperature(self)"}, {"kind": "method", "line": 1173, "name": "step", "signature": "def step(self)"}, {"kind": "method", "line": 1176, "name": "accept_perturbation", "signature": "def accept_perturbation(self, delta_loss)"}, {"kind": "method", "line": 1182, "name": "should_restart", "signature": "def should_restart(self, current_delta, best_delta)"}, {"kind": "method", "line": 1187, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1191, "name": "step_adaptive", "signature": "def step_adaptive(self, alignment_trend, resonance_score)"}, {"kind": "method", "line": 1203, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1210, "name": "update_metrics", "signature": "def update_metrics(self)"}, {"kind": "method", "line": 1219, "name": "compute_delta_slope", "signature": "def compute_delta_slope(self)"}, {"kind": "method", "line": 1229, "name": "format_progress_bar", "signature": "def format_progress_bar(self, epoch, total_epochs, phase)"}, {"kind": "method", "line": 1262, "name": "__init__", "signature": "def __init__(self, config, checkpoint_dir)"}, {"kind": "method", "line": 1271, "name": "should_save_checkpoint", "signature": "def should_save_checkpoint(self)"}, {"kind": "method", "line": 1276, "name": "save_checkpoint", "signature": "def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)"}, {"kind": "method", "line": 1292, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1302, "name": "should_save", "signature": "def should_save(self, current_delta, current_alpha, current_acc)"}, {"kind": "method", "line": 1307, "name": "save_checkpoint", "signature": "def save_checkpoint(self, model, optimizer, epoch, metrics, lambda_value)"}, {"kind": "method", "line": 1324, "name": "check", "signature": "def check(model)"}, {"kind": "method", "line": 1339, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1354, "name": "compute_weight_metrics", "signature": "def compute_weight_metrics(self, model)"}, {"kind": "method", "line": 1364, "name": "compute_norm_conservation_error", "signature": "def compute_norm_conservation_error(self, model, val_x)"}, {"kind": "method", "line": 1373, "name": "train_single_epoch", "signature": "def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler)"}, {"kind": "method", "line": 1398, "name": "validate", "signature": "def validate(self, model, val_x, val_y)"}, {"kind": "method", "line": 1408, "name": "collect_all_metrics", "signature": "def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)"}, {"kind": "method", "line": 1448, "name": "__init__", "signature": "def __init__(self, config, surface_engine)"}, {"kind": "method", "line": 1453, "name": "prospect", "signature": "def prospect(self)"}, {"kind": "method", "line": 1484, "name": "__init__", "signature": "def __init__(self, config, surface_engine, batch_size)"}, {"kind": "method", "line": 1490, "name": "mine", "signature": "def mine(self)"}, {"kind": "method", "line": 1534, "name": "__init__", "signature": "def __init__(self, config, surface_engine, seed, batch_size)"}, {"kind": "method", "line": 1541, "name": "run_phase3_training", "signature": "def run_phase3_training(self)"}, {"kind": "method", "line": 1600, "name": "__init__", "signature": "def __init__(self, config, surface_engine, model, optimizer, monitor, seed, batch_size)"}, {"kind": "method", "line": 1610, "name": "run_phase4_refinement", "signature": "def run_phase4_refinement(self)"}, {"kind": "method", "line": 1664, "name": "__init__", "signature": "def __init__(self, config, surface_engine, model, monitor, seed, batch_size)"}, {"kind": "method", "line": 1674, "name": "run_phase5_crystallization", "signature": "def run_phase5_crystallization(self)"}, {"kind": "method", "line": 1726, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1730, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 1789, "name": "_save_final_results", "signature": "def _save_final_results(self, model, monitor, seed, batch_size)"}, {"kind": "method", "line": 1231, "name": "safe_get", "signature": "def safe_get(key)"}]}, {"doc": "willmore_crystallography_suite.py  Comprehensive crystallographic analysis suite for Willmore energy neural network checkpoints. Integrates spectral geometry, Ricci curvature, thermodynamic metrics, topological phase detection, and functional validation tests to validate crystal purity and model performance.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: AGPL v3", "id": "willmore_crystallography_suite.py.py", "kind": "module", "label": "willmore_crystallography_suite.py.py", "language": "py", "sha256": "54ad8574a5aedc67", "symbol_count": 92, "symbols": [{"doc": "Master configuration for Willmore crystallography suite.", "kind": "class", "line": 52, "name": "WillmoreSuiteConfig", "signature": "class WillmoreSuiteConfig"}, {"doc": "Spectral convolution layer with learnable frequency-domain kernels.", "kind": "class", "line": 92, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Willmore minimal surface spectral network architecture.", "kind": "class", "line": 138, "name": "MinimalSurfaceSpectralNetwork", "signature": "class MinimalSurfaceSpectralNetwork(Module)"}, {"doc": "Analytical minimal surface operations for ground truth generation.", "kind": "class", "line": 181, "name": "MinimalSurfaceOperator", "signature": "class MinimalSurfaceOperator"}, {"doc": "Generate various surface potential configurations.", "kind": "class", "line": 237, "name": "SurfacePotentialGenerator", "signature": "class SurfacePotentialGenerator"}, {"doc": "Dataset for minimal surface evolution problems.", "kind": "class", "line": 298, "name": "MinimalSurfaceDataset", "signature": "class MinimalSurfaceDataset(Dataset)"}, {"doc": "Validate weight tensor integrity (NaN/Inf detection).", "kind": "class", "line": 374, "name": "WeightIntegrityCalculator", "signature": "class WeightIntegrityCalculator"}, {"doc": "Compute weight discretization metrics (delta, alpha).", "kind": "class", "line": 410, "name": "DiscretizationCalculator", "signature": "class DiscretizationCalculator"}, {"doc": "Compute spectral geometry properties of weight matrices.", "kind": "class", "line": 440, "name": "SpectralGeometryCalculator", "signature": "class SpectralGeometryCalculator"}, {"doc": "Compute Ricci curvature of weight space metric.", "kind": "class", "line": 500, "name": "RicciCurvatureCalculator", "signature": "class RicciCurvatureCalculator"}, {"doc": "Compute Willmore energy and curvature metrics from weights.", "kind": "class", "line": 547, "name": "WillmoreEnergyCalculator", "signature": "class WillmoreEnergyCalculator"}, {"doc": "Detect topological phase state via Fourier mass center analysis.", "kind": "class", "line": 619, "name": "TopologicalPhaseDetector", "signature": "class TopologicalPhaseDetector"}, {"doc": "Compute Berry phase from checkpoint trajectory.", "kind": "class", "line": 709, "name": "BerryPhaseCalculator", "signature": "class BerryPhaseCalculator"}, {"doc": "Abstract base class for functional validation tests.", "kind": "class", "line": 787, "name": "FunctionalTest", "signature": "class FunctionalTest(ABC)"}, {"doc": "Test 1: Model accuracy on validation set.", "kind": "class", "line": 799, "name": "AccuracyTest", "signature": "class AccuracyTest(FunctionalTest)"}, {"doc": "Test 2: Surface reconstruction quality via Willmore energy.", "kind": "class", "line": 823, "name": "SurfaceReconstructionTest", "signature": "class SurfaceReconstructionTest(FunctionalTest)"}, {"doc": "Test 3: Generalization to unseen potential configurations.", "kind": "class", "line": 866, "name": "GeneralizationTest", "signature": "class GeneralizationTest(FunctionalTest)"}, {"doc": "Main analyzer orchestrating all metrics and functional tests.", "kind": "class", "line": 900, "name": "CheckpointAnalyzer", "signature": "class CheckpointAnalyzer"}, {"doc": "Generate comprehensive visualization of all metrics.", "kind": "class", "line": 1035, "name": "ComprehensiveVisualizer", "signature": "class ComprehensiveVisualizer"}, {"doc": "Process multiple checkpoints and find the best one.", "kind": "class", "line": 1321, "name": "BatchProcessor", "signature": "class BatchProcessor"}, {"doc": "Configure logging for the suite.", "kind": "method", "line": 1444, "name": "setup_logging", "signature": "def setup_logging(log_level)"}, {"kind": "method", "line": 1452, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 95, "name": "__init__", "signature": "def __init__(self, channels, grid_size)"}, {"kind": "method", "line": 112, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 141, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 160, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Extract spectral features for analysis.", "kind": "method", "line": 171, "name": "get_spectral_representation", "signature": "def get_spectral_representation(self, x)"}, {"kind": "method", "line": 184, "name": "__init__", "signature": "def __init__(self, grid_size)"}, {"kind": "method", "line": 188, "name": "_precompute_spectral_operators", "signature": "def _precompute_spectral_operators(self)"}, {"kind": "method", "line": 196, "name": "apply_laplacian", "signature": "def apply_laplacian(self, field)"}, {"kind": "method", "line": 201, "name": "compute_mean_curvature", "signature": "def compute_mean_curvature(self, surface)"}, {"kind": "method", "line": 212, "name": "compute_gaussian_curvature", "signature": "def compute_gaussian_curvature(self, surface)"}, {"kind": "method", "line": 223, "name": "compute_willmore_energy", "signature": "def compute_willmore_energy(self, surface)"}, {"kind": "method", "line": 229, "name": "compute_surface_area", "signature": "def compute_surface_area(self, surface)"}, {"kind": "method", "line": 240, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 244, "name": "pyramid_potential", "signature": "def pyramid_potential(self)"}, {"kind": "method", "line": 251, "name": "cube_potential", "signature": "def cube_potential(self)"}, {"kind": "method", "line": 258, "name": "dodecahedron_potential", "signature": "def dodecahedron_potential(self)"}, {"kind": "method", "line": 266, "name": "torus_potential", "signature": "def torus_potential(self)"}, {"kind": "method", "line": 274, "name": "hyperbolic_potential", "signature": "def hyperbolic_potential(self)"}, {"kind": "method", "line": 282, "name": "generate_mixed_potential", "signature": "def generate_mixed_potential(self, seed)"}, {"kind": "method", "line": 301, "name": "__init__", "signature": "def __init__(self, config, seed, num_samples)"}, {"kind": "method", "line": 331, "name": "_generate_surface_pair", "signature": "def _generate_surface_pair(self, potential, sample_seed)"}, {"kind": "method", "line": 364, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 367, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 370, "name": "get_validation_batch", "signature": "def get_validation_batch(self)"}, {"kind": "method", "line": 377, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 380, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 413, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 416, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 443, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 446, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 503, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 506, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 550, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 554, "name": "compute", "signature": "def compute(self, model)"}, {"kind": "method", "line": 575, "name": "_compute_surface_metrics", "signature": "def _compute_surface_metrics(self, surface)"}, {"kind": "method", "line": 605, "name": "_empty_metrics", "signature": "def _empty_metrics()"}, {"kind": "method", "line": 622, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 628, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"kind": "method", "line": 712, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 715, "name": "load_checkpoints", "signature": "def load_checkpoints(self, checkpoint_dir)"}, {"kind": "method", "line": 734, "name": "_extract_epoch", "signature": "def _extract_epoch(self, filepath)"}, {"kind": "method", "line": 738, "name": "flatten_spectral_kernels", "signature": "def flatten_spectral_kernels(self, state_dict)"}, {"kind": "method", "line": 751, "name": "calculate_berry_phase", "signature": "def calculate_berry_phase(self, checkpoint_dir)"}, {"kind": "method", "line": 790, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 795, "name": "run", "signature": "def run(self, model, dataset)"}, {"kind": "method", "line": 802, "name": "run", "signature": "def run(self, model, dataset)"}, {"kind": "method", "line": 826, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 830, "name": "run", "signature": "def run(self, model, dataset)"}, {"kind": "method", "line": 869, "name": "run", "signature": "def run(self, model, dataset)"}, {"kind": "method", "line": 903, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 918, "name": "analyze_checkpoint", "signature": "def analyze_checkpoint(self, checkpoint_path, dataset)"}, {"kind": "method", "line": 997, "name": "_extract_spectral_field", "signature": "def _extract_spectral_field(self, model)"}, {"kind": "method", "line": 1012, "name": "_compute_health_score", "signature": "def _compute_health_score(self, results)"}, {"kind": "method", "line": 1038, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1041, "name": "visualize_analysis", "signature": "def visualize_analysis(self, results, output_path)"}, {"kind": "method", "line": 1067, "name": "_plot_weight_integrity", "signature": "def _plot_weight_integrity(self, results, ax)"}, {"kind": "method", "line": 1085, "name": "_plot_discretization", "signature": "def _plot_discretization(self, results, ax)"}, {"kind": "method", "line": 1111, "name": "_plot_spectral_geometry", "signature": "def _plot_spectral_geometry(self, results, ax)"}, {"kind": "method", "line": 1132, "name": "_plot_ricci_curvature", "signature": "def _plot_ricci_curvature(self, results, ax)"}, {"kind": "method", "line": 1145, "name": "_plot_functional_test_1", "signature": "def _plot_functional_test_1(self, results, ax)"}, {"kind": "method", "line": 1165, "name": "_plot_functional_test_2", "signature": "def _plot_functional_test_2(self, results, ax)"}, {"kind": "method", "line": 1188, "name": "_plot_functional_test_3", "signature": "def _plot_functional_test_3(self, results, ax)"}, {"kind": "method", "line": 1210, "name": "_plot_health_summary", "signature": "def _plot_health_summary(self, results, ax)"}, {"kind": "method", "line": 1240, "name": "_plot_layer_deltas", "signature": "def _plot_layer_deltas(self, results, ax)"}, {"kind": "method", "line": 1259, "name": "_plot_phase_diagram", "signature": "def _plot_phase_diagram(self, results, ax)"}, {"kind": "method", "line": 1279, "name": "_plot_crystal_verdict", "signature": "def _plot_crystal_verdict(self, results, ax)"}, {"kind": "method", "line": 1324, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1331, "name": "process_directory", "signature": "def process_directory(self, checkpoint_dir, output_dir, dataset)"}, {"kind": "method", "line": 1381, "name": "_rank_checkpoints", "signature": "def _rank_checkpoints(self, all_results)"}, {"kind": "method", "line": 1407, "name": "_generate_summary", "signature": "def _generate_summary(self, ranked, output_dir)"}]}, {"doc": "willmore_zero_shot_scaler.py  Zero-shot grid scaling for Willmore Crystal Minimal Surface Networks.  This module implements progressive grid resolution scaling from a trained model at grid_size=16 to higher resolutions (32, 64, 128, 256, 512, 1024, 2048) using spectral weight interpolation and zero-shot transfer.  The scaling approach preserves the learned spectral representations while adapting the spatial discretization, enabling the model to generalize to finer grid resolutions without retraining.  Architecture: - ConfigurationLoader: TOML-based configuration management - CheckpointManager: Model checkpoint loading and validation - SpectralWeightInterpolator: Fourier-space weight interpolation - GridScaler: Core scaling logic with progressive resolution increase - ScalingPipeline: Orchestrates the complete scaling process - MetricsEvaluator: Performance evaluation at each scale level  Usage: python willmore_zero_shot_scaler.py --config scaler_config.toml", "id": "willmore_zero_shot_scaler.py", "kind": "module", "label": "willmore_zero_shot_scaler.py", "language": "py", "sha256": "a28b062f2a1eba4e", "symbol_count": 63, "symbols": [{"doc": "Configuration dataclass for the zero-shot scaler.", "kind": "class", "line": 115, "name": "ScalerConfig", "signature": "class ScalerConfig"}, {"doc": "Abstract interface for configuration loading.", "kind": "class", "line": 144, "name": "IConfigurationLoader", "signature": "class IConfigurationLoader(ABC)"}, {"doc": "TOML-based configuration loader.", "kind": "class", "line": 153, "name": "TOMLConfigurationLoader", "signature": "class TOMLConfigurationLoader(IConfigurationLoader)"}, {"doc": "Abstract interface for checkpoint management.", "kind": "class", "line": 207, "name": "ICheckpointManager", "signature": "class ICheckpointManager(ABC)"}, {"doc": "Checkpoint manager for Willmore Crystal models.", "kind": "class", "line": 221, "name": "WillmoreCheckpointManager", "signature": "class WillmoreCheckpointManager(ICheckpointManager)"}, {"doc": "Abstract interface for spectral weight interpolation.", "kind": "class", "line": 260, "name": "ISpectralWeightInterpolator", "signature": "class ISpectralWeightInterpolator(ABC)"}, {"doc": "Fourier-based spectral weight interpolation.", "kind": "class", "line": 274, "name": "FourierSpectralInterpolator", "signature": "class FourierSpectralInterpolator(ISpectralWeightInterpolator)"}, {"doc": "Bilinear interpolation for spectral weights.", "kind": "class", "line": 387, "name": "BilinearSpectralInterpolator", "signature": "class BilinearSpectralInterpolator(ISpectralWeightInterpolator)"}, {"doc": "Abstract interface for grid scaling.", "kind": "class", "line": 445, "name": "IGridScaler", "signature": "class IGridScaler(ABC)"}, {"doc": "Grid scaler for Willmore Crystal networks.", "kind": "class", "line": 458, "name": "WillmoreGridScaler", "signature": "class WillmoreGridScaler(IGridScaler)"}, {"doc": "Abstract interface for metrics evaluation.", "kind": "class", "line": 583, "name": "IMetricsEvaluator", "signature": "class IMetricsEvaluator(ABC)"}, {"doc": "Metrics evaluator for Willmore Crystal models.", "kind": "class", "line": 597, "name": "WillmoreMetricsEvaluator", "signature": "class WillmoreMetricsEvaluator(IMetricsEvaluator)"}, {"doc": "Orchestrates the complete progressive scaling process.", "kind": "class", "line": 776, "name": "ScalingPipeline", "signature": "class ScalingPipeline"}, {"doc": "Create a default configuration file.", "kind": "method", "line": 1046, "name": "create_default_config_file", "signature": "def create_default_config_file(path)"}, {"doc": "Build the command-line argument parser.", "kind": "method", "line": 1053, "name": "build_argument_parser", "signature": "def build_argument_parser()"}, {"doc": "Main entry point for the zero-shot scaler.", "kind": "method", "line": 1129, "name": "main", "signature": "def main()"}, {"doc": "Load configuration from the specified source.", "kind": "method", "line": 148, "name": "load", "signature": "def load(self, source)"}, {"kind": "method", "line": 156, "name": "load", "signature": "def load(self, source)"}, {"kind": "method", "line": 161, "name": "_from_toml", "signature": "def _from_toml(self, path)"}, {"kind": "method", "line": 170, "name": "_from_dict", "signature": "def _from_dict(self, data)"}, {"doc": "Load a model checkpoint from disk.", "kind": "method", "line": 211, "name": "load_checkpoint", "signature": "def load_checkpoint(self, path, device)"}, {"doc": "Save a model checkpoint to disk.", "kind": "method", "line": 216, "name": "save_checkpoint", "signature": "def save_checkpoint(self, model, metrics, path)"}, {"kind": "method", "line": 224, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 228, "name": "load_checkpoint", "signature": "def load_checkpoint(self, path, device)"}, {"kind": "method", "line": 246, "name": "save_checkpoint", "signature": "def save_checkpoint(self, model, metrics, path)"}, {"doc": "Interpolate spectral weights to a new shape.", "kind": "method", "line": 264, "name": "interpolate", "signature": "def interpolate(self, source_weight, target_shape)"}, {"kind": "method", "line": 277, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 281, "name": "interpolate", "signature": "def interpolate(self, source_weight, target_shape)"}, {"kind": "method", "line": 294, "name": "_interpolate_2d_spectral", "signature": "def _interpolate_2d_spectral(self, source, target_shape)"}, {"kind": "method", "line": 314, "name": "_interpolate_4d_spectral", "signature": "def _interpolate_4d_spectral(self, source, target_shape)"}, {"kind": "method", "line": 332, "name": "_pad_spectrum_2d", "signature": "def _pad_spectrum_2d(self, spectrum, target_h, target_w)"}, {"kind": "method", "line": 369, "name": "_interpolate_generic", "signature": "def _interpolate_generic(self, source, target_shape)"}, {"kind": "method", "line": 390, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 394, "name": "interpolate", "signature": "def interpolate(self, source_weight, target_shape)"}, {"kind": "method", "line": 419, "name": "_interpolate_generic", "signature": "def _interpolate_generic(self, source, target_shape)"}, {"doc": "Scale a model to a new grid resolution.", "kind": "method", "line": 449, "name": "scale_model", "signature": "def scale_model(self, source_model, target_grid_size)"}, {"kind": "method", "line": 461, "name": "__init__", "signature": "def __init__(self, config, interpolator)"}, {"kind": "method", "line": 470, "name": "scale_model", "signature": "def scale_model(self, source_model, target_grid_size)"}, {"kind": "method", "line": 495, "name": "_extract_hidden_dim", "signature": "def _extract_hidden_dim(self, model)"}, {"kind": "method", "line": 500, "name": "_extract_expansion_dim", "signature": "def _extract_expansion_dim(self, model)"}, {"kind": "method", "line": 505, "name": "_count_spectral_layers", "signature": "def _count_spectral_layers(self, model)"}, {"kind": "method", "line": 510, "name": "_transfer_weights", "signature": "def _transfer_weights(self, source, target, source_grid, target_grid)"}, {"kind": "method", "line": 535, "name": "_scale_spectral_kernel", "signature": "def _scale_spectral_kernel(self, kernel, target_shape, source_grid, target_grid)"}, {"kind": "method", "line": 549, "name": "_scale_conv_weight", "signature": "def _scale_conv_weight(self, weight, target_shape)"}, {"kind": "method", "line": 570, "name": "_validate_weight_transfer", "signature": "def _validate_weight_transfer(self, source, target)"}, {"doc": "Evaluate model performance and metrics.", "kind": "method", "line": 587, "name": "evaluate", "signature": "def evaluate(self, model, grid_size, num_samples)"}, {"kind": "method", "line": 600, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 606, "name": "evaluate", "signature": "def evaluate(self, model, grid_size, num_samples)"}, {"kind": "method", "line": 639, "name": "_construct_weight_surface", "signature": "def _construct_weight_surface(self, model, grid_size)"}, {"kind": "method", "line": 661, "name": "_compute_willmore_metrics", "signature": "def _compute_willmore_metrics(self, surface)"}, {"kind": "method", "line": 677, "name": "_compute_curvature_metrics", "signature": "def _compute_curvature_metrics(self, surface)"}, {"kind": "method", "line": 702, "name": "_compute_spectral_metrics", "signature": "def _compute_spectral_metrics(self, model)"}, {"kind": "method", "line": 735, "name": "_evaluate_inference_quality", "signature": "def _evaluate_inference_quality(self, model, grid_size, num_samples)"}, {"kind": "method", "line": 779, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 796, "name": "execute", "signature": "def execute(self)"}, {"kind": "method", "line": 888, "name": "_load_source_model", "signature": "def _load_source_model(self)"}, {"kind": "method", "line": 914, "name": "_log_metrics", "signature": "def _log_metrics(self, metrics, grid_size)"}, {"kind": "method", "line": 930, "name": "_check_degradation", "signature": "def _check_degradation(self, source_metrics, current_metrics)"}, {"kind": "method", "line": 946, "name": "_is_better_metrics", "signature": "def _is_better_metrics(self, current, best)"}, {"kind": "method", "line": 961, "name": "_save_scaled_model", "signature": "def _save_scaled_model(self, model, metrics, grid_size)"}, {"kind": "method", "line": 971, "name": "_compile_final_results", "signature": "def _compile_final_results(self)"}, {"kind": "method", "line": 985, "name": "_save_final_results", "signature": "def _save_final_results(self, results)"}, {"kind": "method", "line": 997, "name": "_write_detailed_report", "signature": "def _write_detailed_report(self, results, path)"}]}, {"doc": "rbc_model_reconstruction_128_v2.py  Red Blood Cell 3D Reconstruction USING THE SCALED WILLMORE MODEL at 128x128.  Improved version with better spherical parametrization that avoids artificial lobes and properly handles the biconcave RBC geometry.  Key improvements: - Area-weighted projection to avoid polar artifacts - Gaussian smoothing in spherical coordinates - Proper handling of the dimple regions - Better interpolation for sparse data", "id": "wilmore_rbc.py", "kind": "module", "label": "wilmore_rbc.py", "language": "py", "sha256": "a6adf5225a9f5418", "symbol_count": 49, "symbols": [{"doc": "Configuration for RBC reconstruction.", "kind": "class", "line": 37, "name": "ReconstructionConfig", "signature": "class ReconstructionConfig"}, {"doc": "Spectral convolution layer for minimal surface processing.", "kind": "class", "line": 54, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Spectral network for minimal surface computation.", "kind": "class", "line": 88, "name": "MinimalSurfaceSpectralNetwork", "signature": "class MinimalSurfaceSpectralNetwork(Module)"}, {"doc": "Handles loading of model checkpoints.", "kind": "class", "line": 123, "name": "CheckpointLoader", "signature": "class CheckpointLoader"}, {"doc": "Builds and initializes models from configuration.", "kind": "class", "line": 133, "name": "ModelBuilder", "signature": "class ModelBuilder"}, {"doc": "Loads RBC mesh data from OpenRBC format files.", "kind": "class", "line": 172, "name": "RBCMeshLoader", "signature": "class RBCMeshLoader"}, {"doc": "Improved spherical projection with proper handling of biconcave geometry.\n\nKey improvements:\n1. Area-weighted averaging to avoid oversampling at poles\n2. RBF interpolation for smooth reconstruction\n3. Proper handling of the dimple regions\n4. Gaussian smoothing in parameter space", "kind": "class", "line": 198, "name": "ImprovedSphericalProjector", "signature": "class ImprovedSphericalProjector"}, {"doc": "Cylindrical projection - often better for biconcave shapes.\n\nThe RBC is naturally more cylindrical than spherical,\nwith the dimples on top and bottom.", "kind": "class", "line": 380, "name": "CylindricalProjector", "signature": "class CylindricalProjector"}, {"doc": "Generates synthetic shapes for comparison.", "kind": "class", "line": 472, "name": "SyntheticShapeGenerator", "signature": "class SyntheticShapeGenerator"}, {"doc": "Calculates Willmore energy and curvature metrics.", "kind": "class", "line": 517, "name": "WillmoreMetricsCalculator", "signature": "class WillmoreMetricsCalculator"}, {"doc": "Evolves surfaces using the trained model with LR schedule and volume conservation.", "kind": "class", "line": 545, "name": "SurfaceEvolver", "signature": "class SurfaceEvolver"}, {"doc": "Exports meshes to various formats.", "kind": "class", "line": 623, "name": "MeshExporter", "signature": "class MeshExporter"}, {"doc": "Main pipeline for RBC reconstruction using scaled model.", "kind": "class", "line": 791, "name": "RBCReconstructionPipeline", "signature": "class RBCReconstructionPipeline"}, {"kind": "method", "line": 960, "name": "build_argument_parser", "signature": "def build_argument_parser()"}, {"kind": "method", "line": 1046, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 57, "name": "__init__", "signature": "def __init__(self, channels, grid_size)"}, {"kind": "method", "line": 68, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 91, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, input_channels, output_channels)"}, {"kind": "method", "line": 112, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 127, "name": "load", "signature": "def load(checkpoint_path, device)"}, {"kind": "method", "line": 137, "name": "build", "signature": "def build(config)"}, {"kind": "method", "line": 148, "name": "load_from_checkpoint", "signature": "def load_from_checkpoint(checkpoint_path, config)"}, {"kind": "method", "line": 176, "name": "load", "signature": "def load(vert_path, face_path)"}, {"kind": "method", "line": 209, "name": "__init__", "signature": "def __init__(self, grid_size, smoothing_sigma)"}, {"doc": "Compute approximate area associated with each vertex.", "kind": "method", "line": 217, "name": "compute_vertex_areas", "signature": "def compute_vertex_areas(self, vertices, faces)"}, {"doc": "Project mesh onto spherical grid with proper area weighting.", "kind": "method", "line": 232, "name": "project_mesh", "signature": "def project_mesh(self, vertices, faces, use_rbf)"}, {"doc": "Project using area-weighted averaging.", "kind": "method", "line": 270, "name": "_area_weighted_projection", "signature": "def _area_weighted_projection(self, theta, phi, r, areas)"}, {"doc": "Use RBF interpolation for smooth reconstruction.", "kind": "method", "line": 303, "name": "_rbf_interpolation", "signature": "def _rbf_interpolation(self, theta, phi, r)"}, {"doc": "Apply Gaussian smoothing adapted to spherical coordinates.", "kind": "method", "line": 333, "name": "_apply_spherical_smoothing", "signature": "def _apply_spherical_smoothing(self, r_grid)"}, {"doc": "Convert spherical grid back to 3D vertices.", "kind": "method", "line": 355, "name": "to_cartesian", "signature": "def to_cartesian(self, r_grid, scale)"}, {"kind": "method", "line": 388, "name": "__init__", "signature": "def __init__(self, grid_size, smoothing_sigma)"}, {"doc": "Project mesh using cylindrical coordinates.", "kind": "method", "line": 396, "name": "project_mesh", "signature": "def project_mesh(self, vertices, faces)"}, {"doc": "Convert cylindrical grid back to 3D vertices.", "kind": "method", "line": 445, "name": "to_cartesian", "signature": "def to_cartesian(self, rho_grid, z_scale, rho_scale)"}, {"kind": "method", "line": 475, "name": "__init__", "signature": "def __init__(self, grid_size)"}, {"kind": "method", "line": 481, "name": "create_sphere", "signature": "def create_sphere(self, radius)"}, {"doc": "Create biconcave disc shape using Evans-Fung model.", "kind": "method", "line": 484, "name": "create_biconcave", "signature": "def create_biconcave(self, radius, dimple_depth)"}, {"doc": "Create RBC shape using Evans-Fung parametrization.\n\nThe RBC cross-section follows:\nr(z) = R0 * sqrt(1 - (z/z0)^2) * (1 + c*(z/z0)^2)\n\nThis creates the characteristic biconcave shape.", "kind": "method", "line": 490, "name": "create_evans_fung_rbc", "signature": "def create_evans_fung_rbc(self, radius, dimple_depth, thickness)"}, {"kind": "method", "line": 520, "name": "__init__", "signature": "def __init__(self, grid_size)"}, {"kind": "method", "line": 523, "name": "compute_willmore", "signature": "def compute_willmore(self, surface)"}, {"kind": "method", "line": 527, "name": "compute_curvature_stats", "signature": "def compute_curvature_stats(self, surface)"}, {"kind": "method", "line": 548, "name": "__init__", "signature": "def __init__(self, model, config)"}, {"doc": "Compute learning rate with cosine schedule.", "kind": "method", "line": 556, "name": "_compute_lr", "signature": "def _compute_lr(self, step)"}, {"doc": "Estimate volume from surface grid.", "kind": "method", "line": 567, "name": "_compute_volume", "signature": "def _compute_volume(self, surface)"}, {"doc": "Normalize surface to preserve volume.", "kind": "method", "line": 571, "name": "_normalize_volume", "signature": "def _normalize_volume(self, surface, target_volume)"}, {"kind": "method", "line": 579, "name": "evolve", "signature": "def evolve(self, initial_surface)"}, {"kind": "method", "line": 627, "name": "save_obj", "signature": "def save_obj(vertices, faces, filepath)"}, {"kind": "method", "line": 636, "name": "save_html_comparison", "signature": "def save_html_comparison(original_vertices, original_faces, projected_vertices, projected_faces, evolved_vertices, evolved_faces, biconcave_vertices, biconcave_faces, metrics, output_path)"}, {"kind": "method", "line": 794, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 805, "name": "run", "signature": "def run(self, checkpoint_path, vert_path, face_path, output_dir, projection_type)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (14 files)

#### `app.py`
**Path:** `app.py`
**File Doc:** *app.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:*

*No symbols extracted*

#### `lol.py`
**Path:** `lol.py`
**File Doc:** *demo_cylindrical_vs_spherical.py  DEMO HONESTA: Comparación de proyección esférica vs cilíndrica.  CONCLUSIÓN ANTICIPADA: - Esférica: NO funciona bien para RBC (dimples en polos) - Cilíndrica: SÍ funciona (el RBC es naturalmente cilíndrico)*

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
**File Doc:** *rbc_model_reconstruction.py  EVALUACIÓN PUNTO A PUNTO: Modelo evaluado en cada uno de los 9128 vértices sin pasar por grilla 16x16. Preserva la densidad irregular del malla original.*

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
**File Doc:** *rbc_model_reconstruction.py  Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.  The model processes 16x16 grids. We project the ENTIRE RBC mesh onto a single 16x16 spherical parametrization and run inference.  This shows what the model "sees" when given the RBC shape.*

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
**File Doc:** *rbc_model_reconstruction.py  Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.  The model processes 16x16 grids. We project the ENTIRE RBC mesh onto a single 16x16 spherical parametrization and run inference.  This shows what the model "sees" when given the RBC shape.*

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
**File Doc:** *rbc_model_reconstruction.py  Red Blood Cell 3D Reconstruction USING THE TRAINED WILLMORE MODEL.  Uses the model to predict curvature/energy values for each vertex in the original RBC mesh from OpenRBC.  The visualization shows the ACTUAL RBC mesh colored by model predictions.*

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
**File Doc:** *rbc_model_reconstruction_128_v2.py  Red Blood Cell 3D Reconstruction USING THE SCALED WILLMORE MODEL at 128x128.  Improved version with better spherical parametrization that avoids artificial lobes and properly handles the biconcave RBC geometry.  Key improvements: - Area-weighted projection to avoid polar artifacts - Gaussian smoothing in spherical coordinates - Proper handling of the dimple regions - Better interpolation for sparse data*

**Classes:**
- `ReconstructionConfig` (line 37) `class ReconstructionConfig` - *Configuration for RBC reconstruction.*
- `SpectralLayer` (line 51) `class SpectralLayer(Module)` - *Spectral convolution layer for minimal surface processing.*
- `MinimalSurfaceSpectralNetwork` (line 85) `class MinimalSurfaceSpectralNetwork(Module)` - *Spectral network for minimal surface computation.*
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

**Methods:**
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
**File Doc:** *rbc_willmore_analysis.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3  Description: Red Blood Cell Morphology Analysis via Willmore Energy Minimization.  This script analyzes Red Blood Cell (RBC) membrane geometry using the Willmore energy model. The biconcave disc shape of healthy RBCs emerges naturally from minimizing the Willmore energy functional:  W = integral((H - H0)^2 dA)  where H is the mean curvature and H0 is the spontaneous curvature.  The analysis uses real RBC mesh data from OpenRBC (protein-resolution simulator) to validate whether the trained Willmore model can detect the characteristic biconcave shape and distinguish healthy from pathological morphologies.  Scientific basis: - Helfrich-Canham membrane bending energy model - Gauss-Bonnet theorem for closed surfaces - Mean curvature flow as shape relaxation dynamics - Differential geometry of membrane surfaces*

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
- `SpectralLayer` (line 799) `class SpectralLayer(Module)` - *Spectral convolution layer for surface processing.

Implements convolution in the frequency domain using FFT,
allowing the network to learn global surface patterns.*
- `MinimalSurfaceSpectralNetwork` (line 848) `class MinimalSurfaceSpectralNetwork(Module)` - *Neural network for minimal surface detection and Willmore energy learning.

This network learns to predict mean curvature fields and identify
minimal surface configurations through spectral convolution layers.*
- `IModelLoader` (line 894) `class IModelLoader(ABC)` - *Abstract interface for model loading implementations.*
- `CheckpointModelLoader` (line 902) `class CheckpointModelLoader(IModelLoader)` - *Model loader that loads from PyTorch checkpoint files.*
- `SurfaceAnalysisEngine` (line 1002) `class SurfaceAnalysisEngine` - *Main engine for RBC surface analysis using Willmore energy model.

This class orchestrates the complete analysis pipeline, from mesh loading
to curvature computation and shape emergence testing.*

**Methods:**
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
**File Doc:** *rbc_willmore_analysis.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3  Description: Red Blood Cell Morphology Analysis via Willmore Energy Minimization.  This script analyzes Red Blood Cell (RBC) membrane geometry using the Willmore energy model. The biconcave disc shape of healthy RBCs emerges naturally from minimizing the Willmore energy functional:  W = integral((H - H0)^2 dA)  where H is the mean curvature and H0 is the spontaneous curvature.  The analysis uses real RBC mesh data from OpenRBC (protein-resolution simulator) to validate whether the trained Willmore model can detect the characteristic biconcave shape and distinguish healthy from pathological morphologies.  Scientific basis: - Helfrich-Canham membrane bending energy model - Gauss-Bonnet theorem for closed surfaces - Mean curvature flow as shape relaxation dynamics - Differential geometry of membrane surfaces*

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
- `SpectralLayer` (line 799) `class SpectralLayer(Module)` - *Spectral convolution layer for surface processing.

Implements convolution in the frequency domain using FFT,
allowing the network to learn global surface patterns.*
- `MinimalSurfaceSpectralNetwork` (line 848) `class MinimalSurfaceSpectralNetwork(Module)` - *Neural network for minimal surface detection and Willmore energy learning.

This network learns to predict mean curvature fields and identify
minimal surface configurations through spectral convolution layers.*
- `IModelLoader` (line 894) `class IModelLoader(ABC)` - *Abstract interface for model loading implementations.*
- `CheckpointModelLoader` (line 902) `class CheckpointModelLoader(IModelLoader)` - *Model loader that loads from PyTorch checkpoint files.*
- `SurfaceAnalysisEngine` (line 1002) `class SurfaceAnalysisEngine` - *Main engine for RBC surface analysis using Willmore energy model.

This class orchestrates the complete analysis pipeline, from mesh loading
to curvature computation and shape emergence testing.*

**Methods:**
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
**File Doc:** *diagnose_model.py  Diagnóstico CORREGIDO: El modelo SÍ aprendió, pero trabaja en escala pequeña. La forma emerge de la estructura, no del valor absoluto.*

**Functions:**
- `load_model` (line 20) `def load_model(checkpoint_path, device)`
- `test_model_behavior` (line 45) `def test_model_behavior(model, config, device)` - *Test que respeta la escala pequeña del modelo.*
- `main` (line 154) `def main()`

#### `willmore_crsital2.py`
**Path:** `willmore_crsital2.py`
**File Doc:** *willmore_crystal.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date of creation: 2026 License: AGPL v3  Description: Surface Tension and Willmore Energy Grokking via Minimal Surface Topological Crystallization. Based on the physical law that governs soap bubble formation: - Mean Curvature H = 0 (minimal surfaces) - Willmore Energy: W = integral(H^2 dA) - Surface Tension minimization  The training of neural networks is modeled as a Ricci flow in weight space, where regularization acts as surface tension and discrete algorithms are minimal surfaces (hyperspheres of Perelman) that emerge as low-entropy attractors.  Five-phase protocol: Phase 1 - Batch size prospecting Phase 2 - Seed mining with decreasing delta criterion Phase 3 - Full training of best seed + batch size until grokking Phase 4 - Refinement via simulated annealing toward crystal state Phase 5 - Quadruple precision (float128) high-pressure crystallization*

**Classes:**
- `Config` (line 53) `class Config`
- `IPhaseDetector` (line 201) `class IPhaseDetector(ABC)`
- `IMetricCalculator` (line 207) `class IMetricCalculator(ABC)`
- `SeedManager` (line 213) `class SeedManager`
- `LoggerFactory` (line 227) `class LoggerFactory`
- `MinimalSurfaceOperator` (line 242) `class MinimalSurfaceOperator`
- `SpectralLayer` (line 307) `class SpectralLayer(Module)`
- `MinimalSurfaceBackbone` (line 331) `class MinimalSurfaceBackbone(Module)`
- `MinimalSurfaceInferenceEngine` (line 351) `class MinimalSurfaceInferenceEngine`
- `SurfacePotentialGenerator` (line 399) `class SurfacePotentialGenerator`
- `MinimalSurfaceDataset` (line 452) `class MinimalSurfaceDataset(Dataset)`
- `MinimalSurfaceSpectralNetwork` (line 539) `class MinimalSurfaceSpectralNetwork(Module)`
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

**Methods:**
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
**File Doc:** *willmore_crystallography_suite.py  Comprehensive crystallographic analysis suite for Willmore energy neural network checkpoints. Integrates spectral geometry, Ricci curvature, thermodynamic metrics, topological phase detection, and functional validation tests to validate crystal purity and model performance.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: AGPL v3*

**Classes:**
- `WillmoreSuiteConfig` (line 52) `class WillmoreSuiteConfig` - *Master configuration for Willmore crystallography suite.*
- `SpectralLayer` (line 92) `class SpectralLayer(Module)` - *Spectral convolution layer with learnable frequency-domain kernels.*
- `MinimalSurfaceSpectralNetwork` (line 138) `class MinimalSurfaceSpectralNetwork(Module)` - *Willmore minimal surface spectral network architecture.*
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

**Methods:**
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
**File Doc:** *willmore_zero_shot_scaler.py  Zero-shot grid scaling for Willmore Crystal Minimal Surface Networks.  This module implements progressive grid resolution scaling from a trained model at grid_size=16 to higher resolutions (32, 64, 128, 256, 512, 1024, 2048) using spectral weight interpolation and zero-shot transfer.  The scaling approach preserves the learned spectral representations while adapting the spatial discretization, enabling the model to generalize to finer grid resolutions without retraining.  Architecture: - ConfigurationLoader: TOML-based configuration management - CheckpointManager: Model checkpoint loading and validation - SpectralWeightInterpolator: Fourier-space weight interpolation - GridScaler: Core scaling logic with progressive resolution increase - ScalingPipeline: Orchestrates the complete scaling process - MetricsEvaluator: Performance evaluation at each scale level  Usage: python willmore_zero_shot_scaler.py --config scaler_config.toml*

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

**Methods:**
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
**File Doc:** *rbc_model_reconstruction_128_v2.py  Red Blood Cell 3D Reconstruction USING THE SCALED WILLMORE MODEL at 128x128.  Improved version with better spherical parametrization that avoids artificial lobes and properly handles the biconcave RBC geometry.  Key improvements: - Area-weighted projection to avoid polar artifacts - Gaussian smoothing in spherical coordinates - Proper handling of the dimple regions - Better interpolation for sparse data*

**Classes:**
- `ReconstructionConfig` (line 37) `class ReconstructionConfig` - *Configuration for RBC reconstruction.*
- `SpectralLayer` (line 54) `class SpectralLayer(Module)` - *Spectral convolution layer for minimal surface processing.*
- `MinimalSurfaceSpectralNetwork` (line 88) `class MinimalSurfaceSpectralNetwork(Module)` - *Spectral network for minimal surface computation.*
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

**Methods:**
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
