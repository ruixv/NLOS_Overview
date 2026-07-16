#!/usr/bin/env python3
"""Synchronize the Optics Express 2017 fast back-projection NLOS milestone."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Fast Back-Projection for Non-Line of Sight Reconstruction"
KEY = "arellanoFastBackprojectionNonline2017"
URL = "https://doi.org/10.1364/OE.25.011574"


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
            f"| 2017 | [{TITLE}]({URL}) — Arellano, Gutierrez, Jarabo | Optics Express 2017 | "
            "Recasts classical transient back-projection as GPU voxelization of the ellipsoidal space--time manifolds induced by three-bounce measurements, reducing redundant voxel-wise evaluation and delivering up to three orders of magnitude faster reconstruction with negligible quality loss. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    milestone = (
        "2017 ── Arellano et al.: fast GPU back-projection — ellipsoidal space-time manifold voxelization brings classic transient reconstruction from hours toward seconds [Optics Express]\n"
        "   │\n"
    )
    if milestone not in text:
        anchor = "2018 ── O'Toole et al.: confocal NLOS + LCT — real-time O(N³logN) [Nature]\n"
        text = replace_once(text, anchor, milestone + anchor, "README 2017 milestone")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        paper = (
            f'      {{cat:"latest active",title:"{TITLE}",authors:"Arellano, Gutierrez, Jarabo",year:2017,'
            f'venue:"Optics Express 2017",url:"{URL}",'
            'key:"Reformulates three-bounce transient back-projection as GPU voxelization of ellipsoidal space--time manifolds, avoiding redundant voxel-wise evaluation and accelerating hidden-geometry probability-map construction by up to three orders of magnitude with negligible quality loss."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")

        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
        match = pattern.search(text)
        if not match:
            raise RuntimeError("Homepage tracked-count anchor is missing")
        count = int(match.group(2)) + 1
        text = pattern.sub(lambda m: f"{m.group(1)}{count}{m.group(3)}", text, count=1)

    old_heading = "Natural-occluder coding and occlusion-aware active NLOS"
    new_heading = "Fast GPU back-projection and natural-occluder coding"
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2017 timeline heading")

    old_paragraph = "Partial occluders, surface normals, and a formal visibility-mask model showed that hidden-scene occlusion can improve transport conditioning and enable static reconstruction without picosecond time resolution."
    new_paragraph = "Arellano et al. converted ellipsoidal three-bounce back-projection into GPU manifold voxelization, removing a major computational bottleneck while preserving reconstruction quality. In parallel, partial occluders, surface normals, and formal visibility masks showed that hidden-scene occlusion can improve transport conditioning and enable static reconstruction without picosecond time resolution."
    if old_paragraph in text:
        text = replace_once(text, old_paragraph, new_paragraph, "homepage 2017 timeline paragraph")

    path.write_text(text, encoding="utf-8")


def update_active_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")

    table_end = text.index(r"\end{table*}")
    if KEY not in text[:table_end]:
        anchor = "mannaErrorBackprojectionAlgorithms2018,otooleConfocalNonlineofsightImaging2018"
        text = replace_once(
            text,
            anchor,
            f"{KEY},mannaErrorBackprojectionAlgorithms2018,otooleConfocalNonlineofsightImaging2018",
            "active-SPAD citation list",
        )

    old = (
        "Afterward, researches such as the use of GPU acceleration\\cite{arellanoFastBackprojectionNonline2017} "
        "and error back projection using iterative algorithms\\cite{mannaErrorBackprojectionAlgorithms2018} have also been proposed."
    )
    new = (
        "Arellano~\\etal~reformulated back projection as the voxelization of ellipsoidal space--time manifolds induced by individual three-bounce measurements~\\cite{arellanoFastBackprojectionNonline2017}. "
        "Rather than evaluating every candidate voxel against every captured sample, the algorithm projects only signal-bearing ellipsoids into the reconstruction volume using the GPU rasterization pipeline. "
        "This ellipsoidal-manifold voxelization lowers the dominant computation from voxel-wise accumulation toward measurement-driven processing, scales far more gently with output resolution, and reports speedups of up to three orders of magnitude with negligible reconstruction error. "
        "Subsequent iterative error-backprojection methods further refined the residual between simulated and measured transients~\\cite{mannaErrorBackprojectionAlgorithms2018}."
    )
    if old in text:
        text = replace_once(text, old, new, "back-projection survey sentence")
    elif "ellipsoidal-manifold voxelization" not in text:
        raise RuntimeError("Back-projection narrative anchor changed unexpectedly")

    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, active table, and survey narrative.")


if __name__ == "__main__":
    main()
