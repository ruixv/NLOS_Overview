#!/usr/bin/env python3
"""Synchronize the efficient transient-rendering NLOS milestone across public artifacts."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Non-Line-of-Sight Reconstruction Using Efficient Transient Rendering"
KEY = "iseringhausen:2018"
HEADING = "Physically based transient analysis-by-synthesis."


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
            "| 2020 | [Non-Line-of-Sight Reconstruction Using Efficient Transient Rendering]"
            "(https://doi.org/10.1145/3368314) — Iseringhausen, Hullin | ACM TOG 2020 | "
            "Establishes a physically grounded analysis-by-synthesis route for active transient NLOS: "
            "a custom millisecond three-bounce renderer, implicit level-set surface geometry, BRDF and visibility terms, "
            "and global optimization recover detailed hidden surfaces under noise and non-diffuse reflectance, "
            "forming a direct precursor to differentiable, neural-field, and Gaussian transient rendering. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    old_milestone = (
        "2020 ── Isogawa et al.: C2NLOS transient sinograms — 1D circular confocal scanning with far fewer measurements [ECCV]\n"
    )
    new_milestone = (
        "2020 ── Iseringhausen & Hullin: physically based transient analysis-by-synthesis — surface-, BRDF-, and visibility-aware NLOS inverse rendering [ACM TOG]\n"
        "   │     Isogawa et al.: C2NLOS transient sinograms — 1D circular confocal scanning with far fewer measurements [ECCV]\n"
    )
    if "Iseringhausen & Hullin: physically based transient analysis-by-synthesis" not in text:
        text = replace_once(text, old_milestone, new_milestone, "README 2020 milestone")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if TITLE not in text:
        paper = (
            '      {cat:"latest active",title:"Non-Line-of-Sight Reconstruction Using Efficient Transient Rendering",'
            'authors:"Iseringhausen and Hullin",year:2020,venue:"ACM TOG 2020",url:"https://doi.org/10.1145/3368314",'
            'key:"Foundational analysis-by-synthesis NLOS reconstruction with a custom millisecond three-bounce transient renderer, implicit surface geometry, BRDF-aware transport, and explicit visibility/self-occlusion; a precursor to later differentiable and neural transient methods."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>99</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>100</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_heading = "Structured sparse scanning and edge-resolved transients"
    new_heading = "Physically based inverse rendering, structured sparse scanning, and edge-resolved transients"
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2020 timeline heading")

    old_text = (
        "Isogawa et al. showed that a one-dimensional circular confocal scan forms a transient sinogram and preserves enough information for hidden localization and image reconstruction with far fewer measurements; "
    )
    new_text = (
        "Iseringhausen and Hullin introduced a physically based analysis-by-synthesis reconstruction that optimizes implicit hidden-surface geometry through a custom millisecond transient renderer with BRDF, shading, visibility, and self-occlusion terms; "
        "Isogawa et al. showed that a one-dimensional circular confocal scan forms a transient sinogram and preserves enough information for hidden localization and image reconstruction with far fewer measurements; "
    )
    if old_text in text and new_text not in text:
        text = replace_once(text, old_text, new_text, "homepage 2020 timeline text")

    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if HEADING not in text:
        anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Fast differentiable transient rendering.}\n"
        paragraph = (
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Physically based transient analysis-by-synthesis.}\n"
            "Iseringhausen and Hullin established an early physically grounded inverse-rendering formulation for transient NLOS surface reconstruction~\\cite{iseringhausen:2018}. "
            "Instead of backprojecting measurements into an unoriented voxel volume, their method represents the hidden object as an implicit level-set surface, renders wall--object--wall transport with a custom GPU transient renderer, and globally optimizes the scene to match measured transients. "
            "The forward model explicitly includes surface orientation, BRDF-dependent scattering, shading, visibility, and self-occlusion, allowing detailed recovery under substantial noise and non-diffuse reflectance. "
            "This analysis-by-synthesis milestone supplied the conceptual and computational bridge from surface optimization to later differentiable transient renderers, neural transient fields, self-calibrating inverse rendering, and Gaussian transient scene representations.\n\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "survey fast-rendering subsection")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE} across README, homepage, and survey source using {KEY}.")


if __name__ == "__main__":
    main()
