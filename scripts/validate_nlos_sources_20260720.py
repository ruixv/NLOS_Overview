#!/usr/bin/env python3
"""Cross-artifact validator for the final 20 July 2026 source integration run."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT / "README.md").read_text(encoding="utf-8")
index = (ROOT / "index.html").read_text(encoding="utf-8")
active = (ROOT / "article/2active.tex").read_text(encoding="utf-8")
passive = (ROOT / "article/3passive.tex").read_text(encoding="utf-8")
master = (ROOT / "bare_jrnl.tex").read_text(encoding="utf-8")
bib = (ROOT / "egbib_merged_20260711.bib").read_text(encoding="utf-8")

for doi in ("10.1063/5.0235687", "10.1016/j.optlaseng.2025.109100"):
    if readme.count(doi) != 1 or index.count(doi) != 1 or doi not in bib:
        raise RuntimeError(f"Cross-artifact DOI validation failed: {doi}")

event_doi = "10.1109/jsen.2024.3468909"
if (
    readme.lower().count(event_doi) != 1
    or index.lower().count(event_doi) != 1
    or event_doi not in bib.lower()
):
    raise RuntimeError("Cross-artifact event-camera DOI validation failed")
if any("2404.05977" in item for item in (readme, index, bib)):
    raise RuntimeError("Obsolete event-camera preprint metadata remains")

for key, source in (
    ("zhangRealTimeScanFreeNLOS2024", active),
    ("zhangSpatialCorrelationNLOS2025", active),
    ("wangEventEnhancedPassiveNLOS2024", passive),
):
    if key not in source or bib.count("{" + key + ",") != 1:
        raise RuntimeError(f"Citation/BibTeX consistency failed: {key}")

if "through 20 July 2026" not in master:
    raise RuntimeError("Survey coverage date was not advanced")

papers = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", index, flags=re.DOTALL)
stat = re.search(
    r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', index
)
if not papers or not stat:
    raise RuntimeError("Website paper-array or statistic missing")
count = len(re.findall(r'\{cat:"', papers.group(1)))
if int(stat.group(1)) != count:
    raise RuntimeError(f"Website count mismatch: stat={stat.group(1)}, objects={count}")

print("All synchronized source artifacts are mutually consistent.")
