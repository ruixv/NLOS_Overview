#!/usr/bin/env python3
"""Repair the HP-CDT homepage anchor, then execute the guarded synchronizer."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
script = root / "scripts/sync_nlos_20260723_hybrid_perceptron.py"
text = script.read_text(encoding="utf-8")
bad = '"      const papers=["'
good = '"    const papers=["'
count = text.count(bad)
if count == 2:
    script.write_text(text.replace(bad, good), encoding="utf-8")
elif count == 0 and text.count(good) == 2:
    pass
else:
    raise SystemExit(f"Unexpected homepage-anchor spelling count: old={count}, new={text.count(good)}")
subprocess.run([sys.executable, str(script)], cwd=root, check=True)
