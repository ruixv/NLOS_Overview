#!/usr/bin/env python3
"""Repair legacy escape sequences before running the 17 July Optica synchronizer."""
from pathlib import Path

path = Path(__file__).resolve().with_name("sync_nlos_20260717_optics_followup.py")
text = path.read_text(encoding="utf-8")
count_vspace = text.count(r"\n\vspace")
count_noindent = text.count(r"\n\noindent")
text = text.replace(r"\n\vspace", r"\n\\vspace")
text = text.replace(r"\n\noindent", r"\n\\noindent")
path.write_text(text, encoding="utf-8")
print(f"Repaired legacy LaTeX escapes: vspace={count_vspace}, noindent={count_noindent}.")
