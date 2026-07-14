#!/usr/bin/env python3
"""Synchronize Occlusion Fields across the NLOS Overview public artifacts.

Edits are marker-based and idempotent. The script aborts rather than guessing
when an expected insertion anchor is missing or duplicated.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction"
KEY = "grauOcclusionFields2022"

README_ROW = (
    "| 2022 | [Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction]"
    "(https://arxiv.org/abs/2203.08657) — Grau et al. | arXiv 2022 | "
    "Represents a hidden surface as the decision boundary between relay-wall-visible and target-occluded "
    "3D space; the learned implicit field yields adaptive meshes, recovers geometry beyond conservative "
    "Fermat-path visibility, and remains robust to substantial self-occlusion. |"
)
README_ANCHOR = (
    "| 2022 | [Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization]"
    "(https://arxiv.org/abs/2211.15367) — Liu et al. | arXiv 2022 | Extends sparse active NLOS reconstruction "
    "with mixed-dimensional priors over measured signals, virtual confocal signals, and hidden surfaces; "
    "demonstrates few-shot recovery from very coarse confocal grids. |"
)
README_MILESTONE_OLD = (
    "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n"
    "   │\n"
    "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]"
)
README_MILESTONE_NEW = (
    "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n"
    "   │\n"
    "2022 ── Grau et al.: Occlusion Fields — implicit recoverability and self-occlusion-aware hidden meshes [arXiv]\n"
    "   │\n"
    "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]"
)

INDEX_STAT = '<b>96</b><span>tracked latest entries</span>'
INDEX_EXISTING_OBJECT = (
    '{cat:"latest learning active",title:"Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction",'
    'authors:"Grau et al.",year:2022,venue:"arXiv 2022",url:"https://arxiv.org/abs/2203.08657",'
    'key:"Implicit surface representation for NLOS recoverability, self-occlusion, and adaptive mesh recovery."},'
)
INDEX_OBJECT = (
    '{cat:"latest learning active",title:"Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction",'
    'authors:"Grau et al.",year:2022,venue:"arXiv 2022",url:"https://arxiv.org/abs/2203.08657",'
    'key:"Models the hidden surface as the boundary between relay-wall-visible and target-occluded 3D space; '
    'learned implicit occlusion fields yield adaptive meshes, recover beyond conservative Fermat-path visibility, '
    'and tolerate substantial self-occlusion."},'
)
INDEX_TIMELINE_MARKER = "differentiable transient rendering and Occlusion Fields broadened inverse-rendering and implicit-surface recovery"

TABLE_OLD = "wuMiniaturizedTCSPC2024,liuGeometricConstrainedNLOS2025} & Pulsed laser & SPAD"
TABLE_NEW = "wuMiniaturizedTCSPC2024,liuGeometricConstrainedNLOS2025,grauOcclusionFields2022} & Pulsed laser & SPAD"
SURFACE_ANCHOR = (
    "Tsai \\etal~found that the first-returning photons contain the shortest length information to the hidden object, "
    "from which the boundary and the surface normal vector of the hidden object can be reconstructed\\cite{tsaiGeometryFirstreturningPhotons2017}. "
    "Xin \\etal~showed that the discontinuities of ToF measurement are produced by special light paths (Fermat Paths), "
    "which contain the surface information of the hidden scene\\cite{xinTheoryFermatPaths2019}. Since these discontinuities "
    "are independent of photon intensity, this approach is robust to different BRDFs."
)
SURFACE_PARAGRAPH = r"""

\vspace{0.8mm}
\noindent \textbf{Implicit occlusion fields beyond Fermat-visible surfaces.}
Grau~\etal~linked recoverability analysis with neural implicit surface reconstruction by representing the hidden object as the decision boundary between points that are visible from at least one relay-wall sample and points occluded behind the target~\cite{grauOcclusionFields2022}. In contrast to memory-intensive voxel albedo and the conservative specular Fermat-path criterion, the learned occlusion field can be converted into an adaptively tessellated mesh, recovers surface portions outside the Fermat-visible set, and remains robust when the target self-occludes across parts of the relay aperture. This direction shifts the role of learning from directly regressing a predefined shape representation toward learning which regions of hidden space are geometrically recoverable, providing an early bridge between physical visibility constraints and later neural implicit NLOS surfaces.
""".rstrip()


def replace_exactly_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    if README_ROW not in text:
        text = replace_exactly_once(text, README_ANCHOR, README_ROW + "\n" + README_ANCHOR, "README paper row")
    if "Occlusion Fields — implicit recoverability and self-occlusion-aware hidden meshes" not in text:
        text = replace_exactly_once(text, README_MILESTONE_OLD, README_MILESTONE_NEW, "README milestone")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if INDEX_OBJECT not in text:
        text = replace_exactly_once(text, INDEX_EXISTING_OBJECT, INDEX_OBJECT, "homepage paper object")
    if INDEX_STAT not in text:
        raise RuntimeError("Occlusion Fields already exists on the homepage, so the tracked-entry count must remain 96")
    if INDEX_TIMELINE_MARKER not in text:
        raise RuntimeError("The existing 2022 homepage timeline no longer mentions Occlusion Fields")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if TABLE_NEW not in text:
        text = replace_exactly_once(text, TABLE_OLD, TABLE_NEW, "active-method table citation")
    if "Implicit occlusion fields beyond Fermat-visible surfaces" not in text:
        text = replace_exactly_once(text, SURFACE_ANCHOR, SURFACE_ANCHOR + SURFACE_PARAGRAPH, "surface-section paragraph")
    if text.count(KEY) != 2:
        raise RuntimeError(f"Expected exactly two survey citations to {KEY}, found {text.count(KEY)}")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print("Occlusion Fields artifacts are synchronized.")


if __name__ == "__main__":
    main()
