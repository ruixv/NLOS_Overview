#!/usr/bin/env python3
"""Synchronize the geometric-constrained NLOS paper across public artifacts.

The edits are marker-based and idempotent: a second run must leave every file
unchanged. The script aborts instead of guessing when an expected anchor is
missing or duplicated.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Geometric Constrained Non-Line-of-Sight Imaging"
KEY = "liuGeometricConstrainedNLOS2025"

README_ROW = (
    "| 2025 | [Geometric Constrained Non-Line-of-Sight Imaging]"
    "(https://arxiv.org/abs/2503.17992) — Liu et al. | arXiv 2025 | "
    "Jointly reconstructs volumetric albedo, depth, and hidden-surface geometry; "
    "a Frobenius-norm shape-operator prior regularizes surface-normal variation, "
    "improving sparse/short-exposure reconstruction while reporting roughly 30× "
    "lower optimization time than an existing surface-reconstruction baseline. |"
)
README_ANCHOR = (
    "| 2025 | [Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset]"
    "(https://arxiv.org/abs/2506.03747) — Shi et al. | arXiv 2025 | Provides a configurable "
    "FFT/LCT-based transient simulator from depth and optional albedo maps, models detector jitter "
    "and Poisson noise, releases seven ShapeNet-category datasets, and benchmarks LCT, phasor-field, "
    "f-k, and backprojection reconstruction baselines. |"
)
README_MILESTONE_ANCHOR = (
    "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
    "   │"
)
README_MILESTONE_NEW = (
    "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
    "   │     Liu et al.: geometric constraints on hidden surface normals for fast sparse-transient reconstruction [arXiv]\n"
    "   │"
)

INDEX_STAT_OLD = '<b>96</b><span>tracked latest entries</span>'
INDEX_STAT_NEW = '<b>97</b><span>tracked latest entries</span>'
INDEX_OBJECT_ANCHOR = (
    '{cat:"latest dataset active",title:"Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset",'
    'authors:"Shi et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2506.03747",'
    'key:"A configurable FFT/LCT simulator generates noisy transient volumes from depth and albedo maps, '
    'releases seven ShapeNet-category datasets, and benchmarks LCT, phasor-field, f-k, and backprojection baselines."},'
)
INDEX_OBJECT = (
    '{cat:"latest active",title:"Geometric Constrained Non-Line-of-Sight Imaging",authors:"Liu et al.",'
    'year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2503.17992",'
    'key:"Joint albedo-surface reconstruction uses a Frobenius-norm shape-operator prior to regularize hidden '
    'surface-normal variation, improving sparse/short-exposure detail while reporting about 30× faster '
    'optimization than a prior surface method."},'
)
INDEX_TIMELINE_OLD = (
    '<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, graph models, '
    'pretraining, open transient benchmarks, radar, acoustic, 6G initial-access imaging, and robotic NLOS</strong>'
    '<p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, '
    'HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, fast configurable transient simulation with an open '
    'ShapeNet benchmark, MITO, N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and '
    'relay-free acoustic NLOS broadened the toolbox.</p></div></div>'
)
INDEX_TIMELINE_NEW = (
    '<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, geometric surface '
    'priors, graph models, pretraining, open transient benchmarks, radar, acoustic, 6G initial-access imaging, and '
    'robotic NLOS</strong><p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, '
    'TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, fast configurable transient '
    'simulation with an open ShapeNet benchmark, shape-operator regularization for hidden surface normals, MITO, '
    'N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and relay-free acoustic NLOS '
    'broadened the toolbox.</p></div></div>'
)

TABLE_OLD = "isogawaTransientSinograms2020,wuMiniaturizedTCSPC2024} & Pulsed laser & SPAD"
TABLE_NEW = "isogawaTransientSinograms2020,wuMiniaturizedTCSPC2024,liuGeometricConstrainedNLOS2025} & Pulsed laser & SPAD"
SURFACE_ANCHOR = (
    "Similarly, fusing the surface reconstruction into the convolution kernel of the LCT~"
    "\\cite{otooleConfocalNonlineofsightImaging2018} can also achieve better reconstruction results than using "
    "only the volumetric albedo representation~\\cite{Young:2020:dlct}."
)
SURFACE_PARAGRAPH = r"""

\vspace{0.8mm}
\noindent \textbf{Geometric constraints on hidden surface normals.}
Liu~\etal~extended the LCT/DLCT line toward sparse and short-exposure surface reconstruction by jointly optimizing transient consistency, volumetric albedo, and projected depth/albedo maps~\cite{liuGeometricConstrainedNLOS2025}. Instead of estimating a free three-dimensional normal field, their model regularizes the Frobenius norm of the shape operator of the depth map, directly constraining spatial variation of hidden-surface normals while retaining geometric detail. This reduces the dimensional burden of joint albedo--normal estimation and, on measurements acquired within 15 seconds, was reported to recover more accurate surfaces with roughly a thirty-fold speedup over a prior surface-reconstruction baseline. The method marks a model-based trajectory complementary to neural implicit surfaces: stronger geometric priors can make under-sampled transient inversion both more detailed and computationally practical.
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
        text = replace_exactly_once(text, README_ANCHOR, README_ANCHOR + "\n" + README_ROW, "README paper-row")
    if "geometric constraints on hidden surface normals for fast sparse-transient reconstruction" not in text:
        text = replace_exactly_once(text, README_MILESTONE_ANCHOR, README_MILESTONE_NEW, "README milestone")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if TITLE not in text:
        text = replace_exactly_once(text, INDEX_STAT_OLD, INDEX_STAT_NEW, "homepage count")
        text = replace_exactly_once(text, INDEX_OBJECT_ANCHOR, INDEX_OBJECT_ANCHOR + "\n      " + INDEX_OBJECT, "homepage paper object")
    elif INDEX_STAT_NEW not in text:
        raise RuntimeError("Paper exists in homepage but tracked-entry count is not 97")
    if "shape-operator regularization for hidden surface normals" not in text:
        text = replace_exactly_once(text, INDEX_TIMELINE_OLD, INDEX_TIMELINE_NEW, "homepage 2025 timeline")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if TABLE_NEW not in text:
        text = replace_exactly_once(text, TABLE_OLD, TABLE_NEW, "active-method table citation")
    if "Geometric constraints on hidden surface normals" not in text:
        text = replace_exactly_once(text, SURFACE_ANCHOR, SURFACE_ANCHOR + SURFACE_PARAGRAPH, "surface-section paragraph")
    if text.count(KEY) != 2:
        raise RuntimeError(f"Expected exactly two survey citations to {KEY}, found {text.count(KEY)}")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print("Geometric-constrained NLOS artifacts are synchronized.")


if __name__ == "__main__":
    main()
