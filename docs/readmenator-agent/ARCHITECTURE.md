# Architecture

## Internal Dependencies

- `model_Reco.py` -> `willmore_crsital2.py`
- `rbc.py` -> `willmore_crsital2.py`
- `rbc_model_reconstruction (1).py` -> `willmore_crsital2.py`
- `rbc_model_reconstruction.py` -> `willmore_crsital2.py`
- `rbc_model_reconstruction_128.py` -> `willmore_crsital2.py`
- `test.py` -> `willmore_crsital2.py`
- `willmore_zero_shot_scaler.py` -> `willmore_crsital2.py`
- `wilmore_rbc.py` -> `willmore_crsital2.py`

## External Imports

- `lol.py` -> numpy, os, scipy.ndimage
- `model_Reco.py` -> argparse, json, numpy, os, sys, torch, torch.nn.functional
- `rbc.py` -> argparse, json, numpy, os, sys, torch
- `rbc_model_reconstruction (1).py` -> argparse, json, numpy, os, sys, torch
- `rbc_model_reconstruction.py` -> argparse, json, numpy, os, sys, torch
- `rbc_model_reconstruction_128.py` -> argparse, dataclasses, json, numpy, os, scipy, scipy.interpolate, sys, torch, torch.nn, torch.nn.functional, traceback, typing
- `rbc_willmore_analysis.py` -> abc, argparse, dataclasses, datetime, json, logging, math, numpy, os, pathlib, sys, torch, torch.nn, torch.nn.functional, typing, warnings
- `rbc_willmore_analysis2.py` -> abc, argparse, dataclasses, datetime, json, logging, math, numpy, os, pathlib, sys, torch, torch.nn, torch.nn.functional, typing, warnings
- `test.py` -> argparse, numpy, os, sys, torch
- `willmore_crsital2.py` -> abc, argparse, collections, copy, dataclasses, datetime, json, logging, math, numpy, os, time, torch, torch.nn, torch.nn.functional, torch.optim, torch.utils.data, typing, warnings
- `willmore_crystallography_suite.py.py` -> abc, argparse, collections, copy, dataclasses, datetime, glob, json, logging, math, matplotlib, matplotlib.gridspec, matplotlib.pyplot, numpy, os, pathlib, re, scipy, scipy.linalg, scipy.optimize, scipy.stats, seaborn, sklearn.decomposition, time, torch, torch.nn, torch.nn.functional, torch.optim, torch.utils.data, traceback, typing, warnings
- `willmore_zero_shot_scaler.py` -> abc, argparse, dataclasses, datetime, json, logging, math, numpy, os, pathlib, sys, time, tomli, tomllib, torch, torch.nn, torch.nn.functional, typing
- `wilmore_rbc.py` -> argparse, dataclasses, json, numpy, os, scipy, scipy.interpolate, sys, torch, torch.nn, torch.nn.functional, traceback, typing
