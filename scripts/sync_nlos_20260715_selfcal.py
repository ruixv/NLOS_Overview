#!/usr/bin/env python3
"""Synchronize the self-calibrating differentiable NLOS inverse-rendering paper.

The paper was already present in README.md and the homepage, but its publisher
metadata and contribution summary were incomplete and it had not been integrated
into the LaTeX survey or consolidated bibliography. Edits are marker-based,
idempotent, and abort rather than guessing when an expected anchor changes.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Self-Calibrating, Fully Differentiable NLOS Inverse Rendering"
KEY = "choiSelfCalibratingNLOS2023"
DOI_URL = "https://doi.org/10.1145/3610548.3618140"

README_DATE_OLD = "**Update run: 14 July 2026.**"
README_DATE_NEW = "**Update run: 15 July 2026.**"
README_OLD = (
    "| 2023 | [Self-Calibrating, Fully Differentiable NLOS Inverse Rendering]"
    "(https://arxiv.org/abs/2309.12047) — Choi et al. | SIGGRAPH Asia 2023 | "
    "Couples diffraction-based volumetric NLOS reconstruction with differentiable transient rendering "
    "and self-calibrates imaging parameters directly from measured transients. |"
)
README_NEW = (
    "| 2023 | [Self-Calibrating, Fully Differentiable NLOS Inverse Rendering]"
    "(https://doi.org/10.1145/3610548.3618140) — Choi et al. | ACM TOG / SIGGRAPH Asia 2023 | "
    "Combines phasor-field volumetric reconstruction with differentiable path-space transient rendering, "
    "jointly optimizing virtual-illumination filters, laser–sensor temporal response, hidden geometry, normals, "
    "and albedo directly from measured transients for noise-robust self-calibrated reconstruction. |"
)
README_TIMELINE_OLD = (
    "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]\n"
    "   │     Huang et al.: Omni-LOS — joint LOS/NLOS neural transients for near-360° single-position shape [arXiv]"
)
README_TIMELINE_NEW = (
    "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]\n"
    "   │     Choi et al.: self-calibrating differentiable NLOS inverse rendering — jointly optimizes imaging and scene parameters [SIGGRAPH Asia / TOG]\n"
    "   │     Huang et al.: Omni-LOS — joint LOS/NLOS neural transients for near-360° single-position shape [arXiv]"
)

INDEX_HEADER_OLD = '<div class="eyebrow">Updated 14 July 2026 · 190+ papers</div>'
INDEX_HEADER_NEW = '<div class="eyebrow">Updated 15 July 2026 · 190+ papers</div>'
INDEX_FOOTER_OLD = "Last updated: 14 July 2026"
INDEX_FOOTER_NEW = "Last updated: 15 July 2026"
INDEX_STAT = '<b>96</b><span>tracked latest entries</span>'
INDEX_OLD = (
    '{cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",'
    'authors:"Choi et al.",year:2023,venue:"SIGGRAPH Asia 2023",url:"https://arxiv.org/abs/2309.12047",'
    'key:"Differentiable transient rendering and self-calibration of imaging parameters from measured NLOS transients."},'
)
INDEX_NEW = (
    '{cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",'
    'authors:"Choi et al.",year:2023,venue:"ACM TOG / SIGGRAPH Asia 2023",url:"https://doi.org/10.1145/3610548.3618140",'
    'key:"Couples phasor-field reconstruction with differentiable path-space transient rendering and jointly optimizes '
    'virtual-illumination filters, laser–sensor response, geometry, normals, and albedo from measured transients."},'
)
INDEX_TIMELINE_OLD = (
    '<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Fast differentiable rendering, '
    'joint LOS/NLOS holistic shape, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, '
    'self-calibration, and active corner cameras</strong><p>Plack et al. reduced physically based analysis-by-synthesis '
    'NLOS reconstruction from hours to minutes on consumer hardware; Omni-LOS unified straight-ray LOS and '
    'spherical-wavefront NLOS transients in a neural level-set model for near-360° shape recovery from one fixed '
    'scan position; NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity '
    'regularization, scattering-media phasor fields, and active corner cameras broadened reconstruction settings; '
    'Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and '
    'two-corner NLOS imaging.</p></div></div>'
)
INDEX_TIMELINE_NEW = (
    '<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Fast and self-calibrating differentiable '
    'rendering, joint LOS/NLOS holistic shape, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, '
    'and active corner cameras</strong><p>Plack et al. reduced physically based analysis-by-synthesis NLOS reconstruction '
    'from hours to minutes on consumer hardware; Choi et al. coupled phasor-field reconstruction with differentiable '
    'transient transport to jointly self-calibrate imaging filters, sensor response, geometry, normals, and albedo; '
    'Omni-LOS unified straight-ray LOS and spherical-wavefront NLOS transients in a neural level-set model for '
    'near-360° shape recovery from one fixed scan position; NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection '
    'reconstruction, structure-sparsity regularization, scattering-media phasor fields, and active corner cameras '
    'broadened reconstruction settings; Virtual Mirrors turned higher-order phasor transport into secondary apertures '
    'for limited-visibility and two-corner NLOS imaging.</p></div></div>'
)

TABLE_OLD = "wuMiniaturizedTCSPC2024,liuGeometricConstrainedNLOS2025,grauOcclusionFields2022} & Pulsed laser & SPAD"
TABLE_NEW = "wuMiniaturizedTCSPC2024,liuGeometricConstrainedNLOS2025,grauOcclusionFields2022,choiSelfCalibratingNLOS2023} & Pulsed laser & SPAD"
SURVEY_ANCHOR = (
    "Plack~\\etal~introduced a physically based differentiable transient renderer tailored to NLOS reconstruction~"
    "\\cite{plackFastDifferentiableTransient2023}. By making gradients through time-resolved light transport efficient "
    "enough for consumer hardware, their analysis-by-synthesis pipeline reduces inverse-rendering runtimes from hours "
    "to minutes while improving optimization stability. The same renderer also supports self-supervised learning, "
    "forming an important bridge between explicit transient inverse rendering and later self-calibrating or learned "
    "NLOS reconstruction pipelines."
)
SURVEY_PARAGRAPH = r"""

\vspace{0.8mm}
\noindent \textbf{Self-calibrating differentiable NLOS inverse rendering.}
Choi~\etal~closed a complementary deployment gap by coupling phasor-field volumetric reconstruction in the frequency domain with differentiable path-space transient rendering in the temporal domain~\cite{choiSelfCalibratingNLOS2023}. Starting only from measured transients, the end-to-end pipeline ray-marches the reconstructed volume to extract hidden surface points and normals, then jointly optimizes virtual-illumination and diffraction-filter parameters, the combined laser--sensor temporal response, and per-surface albedo by minimizing the discrepancy between rendered and measured transients. This self-calibration removes much of the manual filter and hardware-response tuning required by earlier wave-based pipelines, improves geometry and reflectance recovery under substantial noise, and forms a direct methodological bridge from efficient differentiable transient rendering to later neural-field and Gaussian transient representations.
""".rstrip()


def replace_exactly_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    if README_DATE_NEW not in text:
        text = replace_exactly_once(text, README_DATE_OLD, README_DATE_NEW, "README update date")
    if README_NEW not in text:
        text = replace_exactly_once(text, README_OLD, README_NEW, "README paper row")
    if "Choi et al.: self-calibrating differentiable NLOS inverse rendering" not in text:
        text = replace_exactly_once(text, README_TIMELINE_OLD, README_TIMELINE_NEW, "README milestone")
    if text.count(TITLE) != 1:
        raise RuntimeError(f"README must contain exactly one public entry for {TITLE}, found {text.count(TITLE)}")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if INDEX_HEADER_NEW not in text:
        text = replace_exactly_once(text, INDEX_HEADER_OLD, INDEX_HEADER_NEW, "homepage header date")
    if INDEX_FOOTER_NEW not in text:
        text = replace_exactly_once(text, INDEX_FOOTER_OLD, INDEX_FOOTER_NEW, "homepage footer date")
    if INDEX_NEW not in text:
        text = replace_exactly_once(text, INDEX_OLD, INDEX_NEW, "homepage paper object")
    if INDEX_TIMELINE_NEW not in text:
        text = replace_exactly_once(text, INDEX_TIMELINE_OLD, INDEX_TIMELINE_NEW, "homepage 2023 timeline")
    if INDEX_STAT not in text:
        raise RuntimeError("This is a consistency repair for an existing homepage entry; tracked count must remain 96")
    if text.count(TITLE) != 1:
        raise RuntimeError(f"Homepage must contain exactly one public entry for {TITLE}, found {text.count(TITLE)}")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if TABLE_NEW not in text:
        text = replace_exactly_once(text, TABLE_OLD, TABLE_NEW, "active-method table citation")
    if "Self-calibrating differentiable NLOS inverse rendering." not in text:
        text = replace_exactly_once(text, SURVEY_ANCHOR, SURVEY_ANCHOR + SURVEY_PARAGRAPH, "inverse-rendering paragraph")
    if text.count(KEY) != 2:
        raise RuntimeError(f"Expected exactly two survey citations to {KEY}, found {text.count(KEY)}")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print("Self-calibrating NLOS inverse-rendering metadata and survey coverage are synchronized.")


if __name__ == "__main__":
    main()
