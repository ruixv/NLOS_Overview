#!/usr/bin/env python3
"""Synchronize the NeurIPS 2024 ST-Mamba dynamic-NLOS milestone."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Toward Dynamic Non-Line-of-Sight Imaging with Mamba Enforced Temporal Consistency"
KEY = "liMambaTemporalConsistency2024"
URL = "https://doi.org/10.52202/079017-4016"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        row = (
            f"| 2024 | [{TITLE}]({URL}) — Li et al. | NeurIPS 2024 | "
            "Introduces ST-Mamba, a spatial--temporal state-space architecture for dynamic active NLOS reconstruction; interleaved Mamba blocks model long transient/video dependencies efficiently, while a phasor-field wave-domain loss enforces measurement physics and improves temporal consistency under noise. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    milestone = (
        "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
        "   │\n"
    )
    if milestone not in text:
        anchor = "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
        text = replace_once(text, anchor, milestone + anchor, "README 2024 milestone")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        paper = (
            f'      {{cat:"latest learning active",title:"{TITLE}",authors:"Li et al.",year:2024,'
            f'venue:"NeurIPS 2024",url:"{URL}",'
            'key:"ST-Mamba uses interleaved spatial--temporal state-space blocks to model long dependencies in dynamic transient measurements efficiently; a phasor-field wave-domain loss ties the learned video reconstruction to NLOS physics and improves frame-to-frame consistency under noise."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>104</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>105</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_heading = "Real-time video, commodity iToF, compact TCSPC, LEAP, HDPS, TLTM iteration, ptychography, robotics, and EM skins"
    new_heading = "Real-time video, state-space temporal reconstruction, commodity iToF, compact TCSPC, LEAP, HDPS, TLTM iteration, ptychography, robotics, and EM skins"
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2024 timeline heading")

    old_phrase = "plug-and-play reconstruction, Virtual Scanning, domain reduction, Mamba-style temporal modeling, phasor-field enhancement"
    new_phrase = "plug-and-play reconstruction, Virtual Scanning, domain reduction, ST-Mamba state-space reconstruction with phasor-domain wave supervision for temporal consistency, phasor-field enhancement"
    if old_phrase in text:
        text = replace_once(text, old_phrase, new_phrase, "homepage 2024 timeline paragraph")

    path.write_text(text, encoding="utf-8")


def update_active_table() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if KEY not in text:
        anchor = "mannaNonlineofsightimagingUsingDynamic2020,chen_learned_2020"
        text = replace_once(
            text,
            anchor,
            f"mannaNonlineofsightimagingUsingDynamic2020,{KEY},chen_learned_2020",
            "active-SPAD citation list",
        )
    path.write_text(text, encoding="utf-8")


def verify_learning_survey() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    heading = r"\noindent \textbf{State-space model (Mamba) for video NLOS.}"
    if heading not in text:
        raise RuntimeError("The existing ST-Mamba survey paragraph is missing")
    if text.count(KEY) != 1:
        raise RuntimeError(f"Expected one ST-Mamba survey citation, found {text.count(KEY)}")


def main() -> None:
    update_readme()
    update_index()
    update_active_table()
    verify_learning_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, active table, and existing survey narrative.")


if __name__ == "__main__":
    main()
