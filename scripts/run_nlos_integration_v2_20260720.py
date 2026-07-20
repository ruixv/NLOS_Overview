#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "nlos_sync", ROOT / "scripts/sync_nlos_20260720_scanfree_event.py"
)
if spec is None or spec.loader is None:
    raise RuntimeError("Cannot load guarded synchronizer")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")
    key = "wangEventEnhancedPassiveNLOS2024"
    if key not in text:
        row_anchor = (
            "    \\cite{sunAdaptiveMotionNLOS2025} & Ambient light & Conventional RGB camera & "
            "Temporal relay-wall motion & Action recognition\\\\%%%% Table body\n"
        )
        event_row = (
            "    \\cite{wangEventEnhancedPassiveNLOS2024} & Ambient/incoherent illumination & "
            "Event camera + conventional camera & Asynchronous diffusion-pattern motion with "
            "physics-embedded learning & Dynamic 2D reconstruction\\\\%%%% Table body\n"
        )
        if text.count(row_anchor) != 1:
            raise RuntimeError(f"Passive table anchor count: {text.count(row_anchor)}")
        text = text.replace(row_anchor, row_anchor + event_row, 1)

    heading = "\\noindent \\textbf{Event-camera passive NLOS for moving objects.}"
    if heading not in text:
        next_heading = (
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Structure-guided adaptive total variation.}"
        )
        prose = (
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Event-camera passive NLOS for moving objects.}\n"
            "Wang~\\etal~introduced an event-enhanced passive NLOS prototype that records "
            "asynchronous changes in the relay-wall diffusion pattern and combines them with a "
            "physics-embedded reconstruction network~\\cite{wangEventEnhancedPassiveNLOS2024}. "
            "Simulation-based pretraining captures dynamic light transport and sensor characteristics, "
            "while limited measured data are used for fine-tuning. This work extends ordinary-frame "
            "passive NLOS toward neuromorphic acquisition: the event stream emphasizes weak "
            "motion-induced changes that would otherwise be temporally aliased or attenuated in "
            "conventional video.\n\n"
        )
        if text.count(next_heading) != 1:
            raise RuntimeError(f"Passive prose anchor count: {text.count(next_heading)}")
        text = text.replace(next_heading, prose + next_heading, 1)

    path.write_text(text, encoding="utf-8")


def validate_sources() -> None:
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


if __name__ == "__main__":
    sync.update_readme()
    sync.update_index()
    sync.update_active_tex()
    update_passive()
    sync.update_master_and_bib()
    sync.update_notes()
    validate_sources()
    print("Stable source integration completed and validated.")
