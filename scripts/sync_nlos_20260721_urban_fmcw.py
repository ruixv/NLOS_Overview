#!/usr/bin/env python3
"""Synchronize a verified urban-intersection FMCW NLOS paper across public artifacts.

The edits are idempotent and fail closed when an expected unique anchor changes.
"""
from __future__ import annotations

from pathlib import Path
import re

DOI = "10.32604/cmes.2026.078862"
KEY = "linDeepLearningFMCWRadar2026"
TITLE = (
    "Deep Learning--Aided Frequency-Modulated Continuous-Wave Radar for "
    "Around-the-Corner Non-Line-of-Sight Perception at Urban Intersections"
)


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    if DOI not in text:
        header = "|------|-------|----------------|----------------|\n"
        row = (
            "| 2026 | [Deep Learning–Aided Frequency-Modulated Continuous-Wave Radar for "
            "Around-the-Corner Non-Line-of-Sight Perception at Urban Intersections]"
            "(https://doi.org/10.32604/cmes.2026.078862) — Lin, Chen | "
            "Computer Modeling in Engineering & Sciences 2026 | Uses simulated 77 GHz automotive "
            "FMCW echoes and a compact residual AlexNet-derived chirp-restoration network to exploit "
            "building specular reflections for around-corner range and angle estimation at urban "
            "intersections. The paper is an application-facing NLOS radar-perception result; all "
            "reported evaluations are simulation-only, with measured-data validation left for future work. |\n"
        )
        text = replace_once(text, header, header + row, "README latest-additions table")

        timeline_anchor = (
            "   │     Lu et al. and Behari et al.: RF geometry reconstruction and low-cost-LiDAR "
            "spatial-reasoning benchmarks [CVPR]\n"
        )
        timeline_line = (
            "   │     Lin and Chen: urban-intersection FMCW NLOS perception — chirp-level residual "
            "learning suppresses simulated interference before conventional range/angle estimation "
            "[Computer Modeling in Engineering & Sciences]\n"
        )
        text = replace_once(
            text, timeline_anchor, timeline_anchor + timeline_line, "README 2026 timeline"
        )
        write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    if DOI not in text:
        papers_anchor = "    const papers=[\n"
        paper = (
            "      {cat:\"latest modality learning radar fmcw automotive perception simulation\","
            "title:\"Deep Learning–Aided Frequency-Modulated Continuous-Wave Radar for Around-the-Corner "
            "Non-Line-of-Sight Perception at Urban Intersections\",authors:\"Lin and Chen\",year:2026,"
            "venue:\"Computer Modeling in Engineering & Sciences 2026\","
            "url:\"https://doi.org/10.32604/cmes.2026.078862\","
            "key:\"Uses a simulated 77 GHz urban-intersection radar model and a compact residual "
            "AlexNet-derived 1D network to restore interference-corrupted chirps before conventional "
            "range and angle estimation; the reported validation is simulation-only.\"},\n"
        )
        text = replace_once(text, papers_anchor, papers_anchor + paper, "website paper array")
        text = replace_once(
            text,
            '<div class="stat"><b>178</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>179</b><span>tracked latest entries</span></div>',
            "website tracked-paper count",
        )
        old = (
            "CUDA-filtered back projection operated directly on non-planar relay geometry and arbitrary "
            "nonuniform scans, removing the planarization and resampling requirement. Polarization-speckle "
            "modulation added a scanning-free single-pixel keyhole branch with millimeter-scale recovery. "
            "GenPIE linked sparse transient capture, generative geometry priors, and differentiable plenoptic "
            "inverse rendering.</p>"
        )
        new = (
            "CUDA-filtered back projection operated directly on non-planar relay geometry and arbitrary "
            "nonuniform scans, removing the planarization and resampling requirement. Polarization-speckle "
            "modulation added a scanning-free single-pixel keyhole branch with millimeter-scale recovery. "
            "GenPIE linked sparse transient capture, generative geometry priors, and differentiable plenoptic "
            "inverse rendering. Urban-intersection FMCW perception additionally used chirp-level residual "
            "learning to suppress simulated interference before conventional around-corner range and angle "
            "estimation, while explicitly leaving measured-road validation open.</p>"
        )
        text = replace_once(text, old, new, "website 2026 timeline")
        write(path, text)


def update_survey_section() -> None:
    path = "article/5newscenes.tex"
    text = read(path)
    if KEY not in text:
        anchor = (
            "Tornielli Bellini~\\etal~push reflector-assisted RF NLOS imaging toward communication "
            "infrastructure"
        )
        index = text.find(anchor)
        if index < 0 or text.find(anchor, index + 1) >= 0:
            raise RuntimeError("radar survey anchor was not found uniquely")
        paragraph = (
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Urban-intersection FMCW radar perception.}\n"
            "Lin and Chen studied an application-facing 77~GHz automotive-radar setting in which "
            "specular reflections from buildings provide around-corner observations at occluded urban "
            "intersections~\\cite{linDeepLearningFMCWRadar2026}. Their compact one-dimensional, "
            "AlexNet-derived regression network restores interference-corrupted chirps before standard "
            "range and angular estimation, reducing simulated severe-interference errors from "
            "$5.48$~m/$18.95^{\\circ}$/$10.77^{\\circ}$ to $0.56$~m/$0.46^{\\circ}$/$0.73^{\\circ}$ "
            "for range, angle, and azimuth deviation, respectively. Unlike measured radar geometry "
            "reconstruction systems, the study is evaluated entirely in MATLAB simulation; its value is "
            "therefore as a learned signal-restoration and autonomous-driving NLOS perception branch, "
            "with real-road multipath and material validation remaining open.\n\n"
        )
        text = text[:index] + paragraph + text[index:]
        write(path, text)


def update_master() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    marker = "% 21 July 2026: integrated urban-intersection FMCW radar NLOS perception.\n"
    if marker not in text:
        anchor = "\\begin{document}\n"
        text = replace_once(text, anchor, marker + anchor, "bare_jrnl document start")
        write(path, text)


def merge_bibliography() -> None:
    merged_path = "egbib_merged_20260711.bib"
    supplement_path = "egbib_20260721_urban_fmcw_updates.bib"
    merged = read(merged_path)
    supplement = read(supplement_path).strip() + "\n"
    if KEY not in merged and DOI not in merged:
        if not merged.endswith("\n"):
            merged += "\n"
        merged += "\n" + supplement
        write(merged_path, merged)
    elif not (KEY in merged and DOI in merged):
        raise RuntimeError("merged bibliography contains only a partial matching record")


def main() -> None:
    update_readme()
    update_index()
    update_survey_section()
    update_master()
    merge_bibliography()


if __name__ == "__main__":
    main()
