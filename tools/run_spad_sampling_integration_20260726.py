#!/usr/bin/env python3
"""Run the July 26 SPAD/sampling synchronizer with a uniquely scoped table anchor."""
from __future__ import annotations

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("integrate_spad_sampling_20260726.py")
spec = importlib.util.spec_from_file_location("nlos_spad_integrator", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load {SCRIPT}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

_original_replace_once = module.replace_once


def _scoped_replace_once(text: str, old: str, new: str, label: str) -> str:
    if label == "active-system table citation" and text.count(old) == 2:
        scoped_old = old + " & Pulsed laser & SPAD"
        scoped_new = new + " & Pulsed laser & SPAD"
        return _original_replace_once(text, scoped_old, scoped_new, label)
    return _original_replace_once(text, old, new, label)


module.replace_once = _scoped_replace_once
raise SystemExit(module.main())
