#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

# Combined July 2026 citation-trace runner.
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "nlos_integrator", HERE / "integrate_visapp2026_passive_nlos.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load NLOS integration module")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

mod.patch_readme()
mod.patch_index()
mod.patch_active()
mod.patch_passive()
mod.patch_modalities()
mod.patch_bib()
mod.patch_master_and_abstract()
mod.validate()
print("Combined July 2026 NLOS citation-trace integration completed and validated")
