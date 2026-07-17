#!/usr/bin/env python3
"""Repair legacy synchronizer literals before applying the 17 July updates."""
from pathlib import Path

root = Path(__file__).resolve().parent

optics = root / "sync_nlos_20260717_optics_followup.py"
text = optics.read_text(encoding="utf-8")
count_vspace = text.count(r"\n\vspace")
count_noindent = text.count(r"\n\noindent")
text = text.replace(r"\n\vspace", r"\n\\vspace")
text = text.replace(r"\n\noindent", r"\n\\noindent")
optics.write_text(text, encoding="utf-8")

frontier = root / "sync_nlos_20260717_frontier.py"
text = frontier.read_text(encoding="utf-8")
old = 'table_anchor = "    \\\\cite{zhang2025passive}'
new = 'table_anchor = "   \\\\cite{zhang2025passive}'
count_table = text.count(old)
text = text.replace(old, new)
frontier.write_text(text, encoding="utf-8")

print(
    "Repaired legacy synchronizer literals: "
    f"vspace={count_vspace}, noindent={count_noindent}, passive_table={count_table}."
)
