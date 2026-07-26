#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

# Combined July 2026 citation-trace runner.
HERE = Path(__file__).resolve().parent


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load NLOS integration module: {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_module("nlos_integrator", "integrate_visapp2026_passive_nlos.py")
base.patch_readme()
base.patch_index()
base.patch_active()
base.patch_passive()
base.patch_modalities()
base.patch_bib()
base.patch_master_and_abstract()
base.validate()

lineage = load_module(
    "spectral_polarization_nlos_integrator",
    "integrate_spectral_polarization_nlos_lineage.py",
)
lineage.patch_readme()
lineage.patch_index()
lineage.patch_active()
lineage.patch_bib()
lineage.patch_master()
lineage.validate()

print("Combined July 2026 NLOS citation-trace integration completed and validated")
