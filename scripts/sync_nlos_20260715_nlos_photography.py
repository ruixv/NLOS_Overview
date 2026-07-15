#!/usr/bin/env python3
"""Synchronize the citation-traced NLOS-photography paper across public artifacts."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Towards Non-Line-of-Sight Photography"
KEY = "pengTowardsNLOSPhotography2021"


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
            "| 2021 | [Towards Non-Line-of-Sight Photography](https://arxiv.org/abs/2109.07783) "
            "— Peng et al. | arXiv 2021 | Reframes active transient NLOS as direct image synthesis: "
            "a data-driven model maps measured transients to a high-resolution 2D photograph from the relay-wall viewpoint, "
            "bypassing an explicit intermediate 3D reconstruction and emphasizing hidden appearance and texture rather than geometry alone. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    milestone = "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n"
    addition = "   │     Peng et al.: NLOS photography — direct high-resolution hidden-view image synthesis from transients [arXiv]\n"
    if addition not in text:
        text = replace_once(text, milestone, milestone + addition, "README 2021 milestone")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if TITLE not in text:
        paper = (
            '      {cat:"latest learning active",title:"Towards Non-Line-of-Sight Photography",'
            'authors:"Peng et al.",year:2021,venue:"arXiv 2021",url:"https://arxiv.org/abs/2109.07783",'
            'key:"Directly synthesizes a high-resolution 2D photograph of the hidden scene from active transient measurements, '
            'bypassing explicit intermediate 3D geometry and shifting the objective from shape-only recovery toward texture and appearance."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>98</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>99</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_heading = "Real-time diffuse NLOS video, kilometer range, neural fields, virtual transport matrices, commercial LiDAR, picosecond timing, and self-calibration"
    new_heading = "Real-time diffuse NLOS video, NLOS photography, kilometer range, neural fields, virtual transport matrices, commercial LiDAR, picosecond timing, and self-calibration"
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2021 timeline heading")

    old_tail = "calibration-aware ToF reconstruction, and two-step LiDAR deep remapping further expanded scale and acquisition regimes.</p>"
    new_tail = (
        "calibration-aware ToF reconstruction, and two-step LiDAR deep remapping further expanded scale and acquisition regimes; "
        "Peng et al. additionally reframed the output as a directly synthesized high-resolution hidden-view photograph, prioritizing texture and appearance over an intermediate geometric volume.</p>"
    )
    if old_tail in text:
        text = replace_once(text, old_tail, new_tail, "homepage 2021 timeline text")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if KEY not in text:
        anchor = (
            "For ToF-based transient NLOS imaging scenes, Chopite \\etal~synthesized a large number of training images through rendering and noise models, and modified part of the input and output in U-Net from 2D tensor to 3D tensor using $L_2$ loss\\cite{chopiteDeepNonLineofSightReconstruction2020}. Finally, based on the end-to-end deep neural network, \\cite{chopiteDeepNonLineofSightReconstruction2020} completed the mapping from transient measurement to depth map.\n"
        )
        paragraph = (
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Direct NLOS photography.}\n"
            "Most active transient methods optimize an intermediate hidden volume, depth map, or surface before producing a human-interpretable image. Peng~\\etal~instead formulated NLOS photography as direct synthesis of a two-dimensional view from the relay-wall viewpoint~\\cite{pengTowardsNLOSPhotography2021}. Their data-driven model maps measured transient transport directly to a high-resolution photograph, bypassing explicit three-dimensional geometry and allowing a relatively small training set. This change of target complements LCT, $f$--$k$, phasor-field, and neural-field reconstruction: it treats hidden texture and appearance as first-class outputs rather than secondary attributes of a recovered volume, anticipating later learned systems that optimize perceptual fidelity in addition to geometric accuracy.\n"
        )
        text = replace_once(text, anchor, anchor + paragraph, "survey end-to-end transient paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE} across README, homepage, and survey source.")


if __name__ == "__main__":
    main()
