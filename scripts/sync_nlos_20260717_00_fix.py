#!/usr/bin/env python3
"""Repair legacy synchronizer literals before validated source and PDF export."""
from pathlib import Path

root = Path(__file__).resolve().parent


def repair_latex_escapes(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    count_vspace = text.count(r"\n\vspace")
    count_noindent = text.count(r"\n\noindent")
    text = text.replace(r"\n\vspace", r"\n\\vspace")
    text = text.replace(r"\n\noindent", r"\n\\noindent")
    path.write_text(text, encoding="utf-8")
    return count_vspace, count_noindent


optics_counts = repair_latex_escapes(root / "sync_nlos_20260717_optics_followup.py")
stereo_path = root / "sync_nlos_20260717_stereo_longrange.py"
stereo_counts = repair_latex_escapes(stereo_path)
text = stereo_path.read_text(encoding="utf-8")
heading = "Model-decomposition reconstruction from sparse transients."
count_heading = text.count(heading)
text = text.replace(heading, r"\\mbox{Model-decomposition reconstruction from sparse transients}.")
stereo_path.write_text(text, encoding="utf-8")

frontier = root / "sync_nlos_20260717_frontier.py"
text = frontier.read_text(encoding="utf-8")
old = 'table_anchor = "    \\\\cite{zhang2025passive}'
new = 'table_anchor = "   \\\\cite{zhang2025passive}'
count_table = text.count(old)
text = text.replace(old, new)
frontier.write_text(text, encoding="utf-8")

print(
    "Repaired legacy synchronizer literals: "
    f"optics={optics_counts}, stereo={stereo_counts}, heading={count_heading}, "
    f"passive_table={count_table}."
)
