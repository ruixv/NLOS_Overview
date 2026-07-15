#!/usr/bin/env python3
"""Synchronize the CVPR 2019 surface-optimization NLOS milestone.

This script is intentionally marker-based and idempotent: it refuses to guess if
expected anchors are absent and never replaces an entire public-facing file from
an external payload.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Beyond Volumetric Albedo -- A Surface Optimization Framework for Non-Line-of-Sight Imaging"
URL = "https://openaccess.thecvf.com/content_CVPR_2019/html/Tsai_Beyond_Volumetric_Albedo_--_A_Surface_Optimization_Framework_for_Non-Line-Of-Sight_CVPR_2019_paper.html"
KEY = "tsaiVolumetricAlbedoSurface2019"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def insert_before_once(text: str, anchor: str, block: str, label: str) -> str:
    if block.strip() in text:
        return text
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected exactly one {label} anchor, found {text.count(anchor)}")
    return text.replace(anchor, block + anchor, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    row = (
        f'| 2019 | [{TITLE}]({URL}) — Tsai, Sankaranarayanan, Gkioulekas | CVPR 2019 | '
        'Moves active transient NLOS beyond voxelized albedo by directly optimizing a hidden surface and reflectance. '
        'Its differentiable radiometric renderer supplies geometry- and reflectance-aware gradients, while stochastic optimization '
        'and geometry processing recover substantially finer surfaces than prior volumetric methods. |\n'
    )
    anchor = "| 2020 | [Non-Line-of-Sight Reconstruction Using Efficient Transient Rendering]"
    if f"[{TITLE}]" not in text:
        text = insert_before_once(text, anchor, row, "README latest-additions")

    milestone = (
        "2019 ── Tsai et al.: Beyond Volumetric Albedo — direct hidden-surface and reflectance optimization [CVPR]\n"
        "   │\n"
    )
    milestone_anchor = "2020 ── Iseringhausen & Hullin: physically based transient analysis-by-synthesis"
    if "2019 ── Tsai et al.: Beyond Volumetric Albedo" not in text:
        text = insert_before_once(text, milestone_anchor, milestone, "README timeline")

    if text.count(f"[{TITLE}]") != 1:
        raise RuntimeError("README surface-optimization title is missing or duplicated")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)

    old_stat = '<div class="stat"><b>100</b><span>tracked latest entries</span></div>'
    new_stat = '<div class="stat"><b>101</b><span>tracked latest entries</span></div>'
    if old_stat in text:
        if text.count(old_stat) != 1:
            raise RuntimeError("Unexpected number of old homepage count markers")
        text = text.replace(old_stat, new_stat, 1)
    elif new_stat not in text:
        raise RuntimeError("Homepage tracked-entry count is neither 100 nor 101")

    paper = (
        '      {cat:"latest active",title:"' + TITLE + '",authors:"Tsai, Sankaranarayanan, Gkioulekas",'
        'year:2019,venue:"CVPR 2019",url:"' + URL + '",'
        'key:"A foundational analysis-by-synthesis framework that replaces volumetric albedo with direct hidden-surface and reflectance optimization; '
        'an efficient differentiable radiometric renderer, stochastic optimization, and geometry processing recover substantially finer NLOS geometry."},\n'
    )
    paper_anchor = '      {cat:"latest active",title:"Non-Line-of-Sight Reconstruction Using Efficient Transient Rendering"'
    if f'title:"{TITLE}"' not in text:
        text = insert_before_once(text, paper_anchor, paper, "homepage paper explorer")

    old_timeline = (
        '      <div class="tl"><div class="year">2019</div><div class="tl-body"><strong>f-k migration, feature visibility, passive periscopy and polarization, coherent control, and single-path/scannerless NLOS</strong>'
        '<p>The field split into wave-based active NLOS, principled recoverability analysis, ordinary-camera computational periscopy, polarization-conditioned passive light transport, keyhole imaging, coherent recognition, scannerless single-pixel acquisition, and wavefront-shaping active focusing.</p></div></div>'
    )
    new_timeline = (
        '      <div class="tl"><div class="year">2019</div><div class="tl-body"><strong>f-k migration, feature visibility, direct surface optimization, passive periscopy, and coherent/scannerless NLOS</strong>'
        '<p>The field split into wave-based active NLOS, principled recoverability analysis, ordinary-camera computational periscopy, polarization-conditioned passive light transport, keyhole imaging, coherent recognition, scannerless single-pixel acquisition, and wavefront-shaping active focusing. Tsai et al. additionally moved transient reconstruction beyond volumetric albedo by directly optimizing hidden surface geometry and reflectance through a differentiable radiometric model.</p></div></div>'
    )
    if old_timeline in text:
        text = text.replace(old_timeline, new_timeline, 1)
    elif new_timeline not in text:
        raise RuntimeError("Expected 2019 homepage timeline marker was not found")

    if text.count(f'title:"{TITLE}"') != 1:
        raise RuntimeError("Homepage surface-optimization title is missing or duplicated")
    if new_stat not in text:
        raise RuntimeError("Homepage tracked-entry count was not updated to 101")
    write(path, text)


def update_survey() -> None:
    path = "article/2active.tex"
    text = read(path)
    paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Beyond volumetric albedo: direct surface optimization.}
Tsai~\etal~introduced a foundational analysis-by-synthesis framework that optimizes hidden surface geometry and reflectance directly, rather than first recovering an unoriented volumetric albedo field~\cite{tsaiVolumetricAlbedoSurface2019}. Their radiometric rendering formulation efficiently computes derivatives of transient measurements with respect to both NLOS shape and reflectance while retaining the underlying multi-bounce transport physics. Coupled with stochastic optimization and geometry-processing regularization, this surface representation reconstructs substantially finer geometric detail than earlier volumetric inversions. It established the explicit surface-optimization branch that later progressed toward physically based transient renderers, analytical differentiable rendering, neural implicit surfaces, self-calibration, and Gaussian transient representations.

"""
    anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Physically based transient analysis-by-synthesis.}"
    if "Beyond volumetric albedo: direct surface optimization" not in text:
        text = insert_before_once(text, anchor, paragraph, "survey inverse-rendering")
    if text.count("Beyond volumetric albedo: direct surface optimization") != 1:
        raise RuntimeError("Survey surface-optimization paragraph is missing or duplicated")
    if f"\\cite{{{KEY}}}" not in text:
        raise RuntimeError("Survey surface-optimization citation key is missing")
    write(path, text)


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print("Synchronized CVPR 2019 surface-optimization NLOS coverage.")


if __name__ == "__main__":
    main()
