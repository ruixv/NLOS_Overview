#!/usr/bin/env python3
"""Synchronize the NeurIPS 2024 ST-Mamba dynamic-NLOS milestone."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Toward Dynamic Non-Line-of-Sight Imaging with Mamba Enforced Temporal Consistency"
KEY = "liMambaTemporalConsistency2024"
URL = "https://doi.org/10.52202/079017-4016"


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    row = (
        f"| 2024 | [{TITLE}]({URL}) — Li et al. | NeurIPS 2024 | "
        "Introduces ST-Mamba, a spatial--temporal state-space architecture for dynamic active NLOS reconstruction; interleaved Mamba blocks model long transient/video dependencies efficiently, while a phasor-field wave-domain loss enforces measurement physics and improves temporal consistency under noise. |\n"
    )
    if TITLE not in text:
        marker = "|------|-------|----------------|----------------|\n"
        if marker in text:
            text = text.replace(marker, marker + row, 1)
        else:
            text = re.sub(r"(\|\s*Year\s*\|\s*Paper\s*\|[^\n]*\n\|[^\n]*\|\n)", r"\1" + row, text, count=1)

    milestone = "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n   │\n"
    if "Li et al.: ST-Mamba" not in text:
        text = re.sub(r"(?m)^(2025 ── Shi et al\.:)", milestone + r"\1", text, count=1)

    path.write_text(text, encoding="utf-8")
    print(f"README title count: {text.count(TITLE)}")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if TITLE not in text:
        paper = (
            f'      {{cat:"latest learning active",title:"{TITLE}",authors:"Li et al.",year:2024,'
            f'venue:"NeurIPS 2024",url:"{URL}",'
            'key:"ST-Mamba uses interleaved spatial--temporal state-space blocks to model long dependencies in dynamic transient measurements efficiently; a phasor-field wave-domain loss ties the learned video reconstruction to NLOS physics and improves frame-to-frame consistency under noise."},\n'
        )
        text = text.replace("    const papers=[\n", "    const papers=[\n" + paper, 1)
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
        match = pattern.search(text)
        if match:
            text = pattern.sub(lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), text, count=1)

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
    print(f"Homepage title count: {text.count(TITLE)}")


def update_active_table() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if KEY not in text:
        preferred = "mannaNonlineofsightimagingUsingDynamic2020,chen_learned_2020"
        if preferred in text:
            text = text.replace(preferred, f"mannaNonlineofsightimagingUsingDynamic2020,{KEY},chen_learned_2020", 1)
        else:
            text = text.replace("mannaNonlineofsightimagingUsingDynamic2020", f"mannaNonlineofsightimagingUsingDynamic2020,{KEY}", 1)
    path.write_text(text, encoding="utf-8")
    print(f"Active-table key count: {text.count(KEY)}")


def report_learning_survey() -> None:
    text = (ROOT / "article/4datadriven.tex").read_text(encoding="utf-8")
    print(f"Survey key count: {text.count(KEY)}")
    print(f"Survey heading present: {'State-space model (Mamba) for video NLOS' in text}")


def main() -> None:
    update_readme()
    update_index()
    update_active_table()
    report_learning_survey()
    print(f"Synchronization pass finished for {TITLE}.")


if __name__ == "__main__":
    main()
