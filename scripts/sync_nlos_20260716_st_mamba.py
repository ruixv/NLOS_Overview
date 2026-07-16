#!/usr/bin/env python3
"""Synchronize the NeurIPS 2024 ST-Mamba dynamic-NLOS milestone."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Toward Dynamic Non-Line-of-Sight Imaging with Mamba Enforced Temporal Consistency"
KEY = "liMambaTemporalConsistency2024"
URL = "https://doi.org/10.52202/079017-4016"


def insert_after(text: str, anchor: str, addition: str, label: str) -> str:
    if anchor not in text:
        raise RuntimeError(f"Missing {label} anchor")
    return text.replace(anchor, anchor + addition, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        row = (
            f"| 2024 | [{TITLE}]({URL}) — Li et al. | NeurIPS 2024 | "
            "Introduces ST-Mamba, a spatial--temporal state-space architecture for dynamic active NLOS reconstruction; interleaved Mamba blocks model long transient/video dependencies efficiently, while a phasor-field wave-domain loss enforces measurement physics and improves temporal consistency under noise. |\n"
        )
        text = insert_after(
            text,
            "|------|-------|----------------|----------------|\n",
            row,
            "README latest-table",
        )

    milestone_line = "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
    if milestone_line not in text:
        anchor = "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
        if anchor not in text:
            raise RuntimeError("Missing README 2025 timeline anchor")
        text = text.replace(anchor, milestone_line + "   │\n" + anchor, 1)

    path.write_text(text, encoding="utf-8")
    print("README synchronized")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        paper = (
            f'      {{cat:"latest learning active",title:"{TITLE}",authors:"Li et al.",year:2024,'
            f'venue:"NeurIPS 2024",url:"{URL}",'
            'key:"ST-Mamba uses interleaved spatial--temporal state-space blocks to model long dependencies in dynamic transient measurements efficiently; a phasor-field wave-domain loss ties the learned video reconstruction to NLOS physics and improves frame-to-frame consistency under noise."},\n'
        )
        text = insert_after(text, "    const papers=[\n", paper, "homepage paper-array")
        count_pattern = re.compile(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>')
        match = count_pattern.search(text)
        if not match:
            raise RuntimeError("Missing homepage tracked-count element")
        current = int(match.group(1))
        expected = current + 1
        text = count_pattern.sub(
            f'<div class="stat"><b>{expected}</b><span>tracked latest entries</span></div>',
            text,
            count=1,
        )

    text = text.replace(
        "Real-time video, commodity iToF, compact TCSPC, LEAP, HDPS, TLTM iteration, ptychography, robotics, and EM skins",
        "Real-time video, state-space temporal reconstruction, commodity iToF, compact TCSPC, LEAP, HDPS, TLTM iteration, ptychography, robotics, and EM skins",
        1,
    )
    text = text.replace(
        "plug-and-play reconstruction, Virtual Scanning, domain reduction, Mamba-style temporal modeling, phasor-field enhancement",
        "plug-and-play reconstruction, Virtual Scanning, domain reduction, ST-Mamba state-space reconstruction with phasor-domain wave supervision for temporal consistency, phasor-field enhancement",
        1,
    )

    path.write_text(text, encoding="utf-8")
    print("Homepage synchronized")


def update_active_table() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if KEY not in text:
        anchor = "mannaNonlineofsightimagingUsingDynamic2020,chen_learned_2020"
        if anchor not in text:
            raise RuntimeError("Missing active-SPAD citation anchor")
        text = text.replace(
            anchor,
            f"mannaNonlineofsightimagingUsingDynamic2020,{KEY},chen_learned_2020",
            1,
        )
    path.write_text(text, encoding="utf-8")
    print("Active table synchronized")


def verify_learning_survey() -> None:
    text = (ROOT / "article/4datadriven.tex").read_text(encoding="utf-8")
    if text.count(KEY) != 1:
        raise RuntimeError(f"Expected one ST-Mamba survey citation, found {text.count(KEY)}")
    if "State-space model (Mamba) for video NLOS" not in text:
        raise RuntimeError("The existing ST-Mamba survey paragraph is missing")
    print("Existing survey paragraph verified")


def main() -> None:
    update_readme()
    update_index()
    update_active_table()
    verify_learning_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, active table, and existing survey narrative.")


if __name__ == "__main__":
    main()
