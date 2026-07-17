#!/usr/bin/env python3
"""Repair legacy escape sequences before running the 17 July Optica synchronizer."""
from pathlib import Path

path = Path(__file__).resolve().with_name("sync_nlos_20260717_optics_followup.py")
text = path.read_text(encoding="utf-8")
count_vspace = text.count(r"\n\vspace")
count_noindent = text.count(r"\n\noindent")
if count_vspace not in (0, 4):
    raise RuntimeError(f"Unexpected legacy vspace escape count: {count_vspace}")
if count_noindent not in (0, 1):
    raise RuntimeError(f"Unexpected legacy noindent escape count: {count_noindent}")
text = text.replace(r"\n\vspace", r"\n\\vspace")
text = text.replace(r"\n\noindent", r"\n\\noindent")
path.write_text(text, encoding="utf-8")
print("Repaired legacy LaTeX string escapes in the Optica synchronizer.")
