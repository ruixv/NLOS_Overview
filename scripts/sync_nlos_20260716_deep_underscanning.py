#!/usr/bin/env python3
"""Synchronize the NeurIPS under-scanning NLOS milestone across public artifacts."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Deep Non-line-of-sight Imaging from Under-scanning Measurements"
KEY = "liDeepNLOSUnderscanning2023"
URL = "https://proceedings.neurips.cc/paper_files/paper/2023/hash/b91cc0a242e6518ee731f74e82b2eebd-Abstract-Conference.html"


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
            f"| 2023 | [{TITLE}]({URL}) — Li et al. | NeurIPS 2023 | "
            "Introduces the first deep-learning pipeline designed specifically for under-scanned active confocal transients: "
            "a transient-recovery network restores a dense measurement grid and a physics-aware volume-reconstruction network "
            "recovers hidden 3D geometry; it remains effective at 8×8 scans and reports 50× faster inference than the iterative baseline. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    milestone = (
        "   │     Li et al.: deep under-scanning reconstruction — learned transient recovery plus physics-aware volumetric inversion from grids as sparse as 8×8 [NeurIPS]\n"
    )
    if milestone not in text:
        anchor = "   │     Liu et al.: SSCR — mixed-dimensional regularization from 5×5 confocal measurements [CVPR]\n"
        text = replace_once(text, anchor, anchor + milestone, "README 2023 milestone")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        paper = (
            f'      {{cat:"latest learning active",title:"{TITLE}",authors:"Li et al.",year:2023,'
            f'venue:"NeurIPS 2023",url:"{URL}",'
            'key:"First deep NLOS pipeline tailored to under-scanned confocal transients: TRN restores dense measurements, '
            'VRN embeds linear light-path physics for hidden-volume reconstruction, and the method remains robust at 8×8 scans '
            'with 50× faster inference than an iterative baseline."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>101</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>102</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_heading = (
        "Sparse transient recovery, differentiable rendering, joint LOS/NLOS shape, transformers, arbitrary patterns, "
        "virtual mirrors, neural implicit NLOS, and active corner cameras"
    )
    new_heading = (
        "Sparse and deep under-scanned transient recovery, differentiable rendering, joint LOS/NLOS shape, transformers, "
        "arbitrary patterns, virtual mirrors, neural implicit NLOS, and active corner cameras"
    )
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2023 timeline heading")

    timeline_sentence = (
        "SSN learned a plug-and-play measurement-space superresolution operator for 16× faster sparse scanning, while SSCR "
        "combined signal, voxel, and surface priors to reconstruct from only 5×5 confocal measurements."
    )
    timeline_addition = (
        " Li et al. paired learned transient densification with a physics-aware volume reconstruction network, retaining "
        "robustness at 8×8 scans and delivering 50× faster inference than an iterative under-scanning solver."
    )
    if timeline_addition.strip() not in text:
        text = replace_once(
            text,
            timeline_sentence,
            timeline_sentence + timeline_addition,
            "homepage 2023 timeline paragraph",
        )

    path.write_text(text, encoding="utf-8")


def update_active_table() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    old = ",sultanOptimizedSamplingNLOS2025} & Pulsed laser & SPAD & Time of fight &  3D reconstruction"
    new = ",sultanOptimizedSamplingNLOS2025,liDeepNLOSUnderscanning2023} & Pulsed laser & SPAD & Time of fight &  3D reconstruction"
    if KEY not in text:
        text = replace_once(text, old, new, "active-SPAD table citation")
    path.write_text(text, encoding="utf-8")


def update_learning_survey() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    heading = r"\noindent \textbf{Learning from under-scanned transients.}"
    if heading not in text:
        anchor = "Recent works have significantly extended this paradigm of combining physical constraints with deep learning.\n"
        paragraph = r'''

\vspace{0.8mm}
\noindent \textbf{Learning from under-scanned transients.}
Dense relay-wall scanning remained a practical acquisition bottleneck even after analytic reconstruction became fast. Li~\etal~introduced the first deep pipeline designed specifically for under-scanning measurements, coupling a transient recovery network that maps sparse scans to a dense measurement grid with a volume reconstruction network that embeds the linear light-path transport operator~\cite{liDeepNLOSUnderscanning2023}. Multi-kernel feature extraction and fusion recover measurement structure, while regularized constraints preserve local detail and suppress oversmoothing. The method remains effective for $8\times8$ confocal scans and reports approximately $50\times$ faster inference than an iterative under-scanning baseline. This work shifts learned active NLOS from post-reconstruction refinement toward joint measurement completion and physics-aware inversion, preceding later signal-superresolution, virtual-scanning, diffusion, and transient-transformer approaches.
'''
        text = replace_once(text, anchor, anchor + paragraph, "deep-learning survey insertion")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active_table()
    update_learning_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, survey, and citations.")


if __name__ == "__main__":
    main()
