#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "visapp_integrator", HERE / "integrate_visapp2026_passive_nlos.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load VISAPP integration module")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

mod.patch_readme()
mod.patch_index()
mod.patch_passive()
mod.patch_bib()
mod.patch_master_and_abstract()

readme = mod.README.read_text(encoding="utf-8")
index = mod.INDEX.read_text(encoding="utf-8")
passive = mod.PASSIVE.read_text(encoding="utf-8")
bib = mod.BIB.read_text(encoding="utf-8")
for doi in (mod.MATSUBARA_DOI, mod.KOZAWA_DOI):
    for label, text in (("README", readme), ("website", index), ("bibliography", bib)):
        if doi not in text:
            raise RuntimeError(f"{label} is missing {doi}")
for key in ("matsubaraJointThermalNLOS2026", "kozawaVehicleReflectionNLOS2026"):
    if passive.count(key) < 2:
        raise RuntimeError(f"passive survey does not cite {key} in prose and table")
    if bib.count("{" + key + ",") != 1:
        raise RuntimeError(f"bibliography key count mismatch for {key}")
print("VISAPP 2026 passive NLOS integration completed and validated")
