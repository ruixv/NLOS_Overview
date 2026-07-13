#!/usr/bin/env python3
"""Idempotently synchronize the Omni-LOS holistic-shape NLOS paper."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Omni-Line-of-Sight Imaging for Holistic Shape Reconstruction"
URL = "https://arxiv.org/abs/2304.10780"
KEY = "huangOmniLOS2023"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("**Update run: 13 July 2026.**", "**Update run: 14 July 2026.**", 1)

    row = (
        f"| 2023 | [{TITLE}]({URL}) — Huang et al. | arXiv 2023 | "
        "Unifies straight-ray LOS and spherical-wavefront NLOS transient rendering in a neural level-set model, using nearby diffuse walls as virtual mirrors to recover near-360° object geometry from one fixed scan position; validated with a SPAD/laser prototype. |"
    )
    if TITLE not in text:
        anchor = "| 2023 | [Fast Differentiable Transient Rendering for Non-Line-of-Sight Reconstruction](https://openaccess.thecvf.com/content/WACV2023/html/Plack_Fast_Differentiable_Transient_Rendering_for_Non-Line-of-Sight_Reconstruction_WACV_2023_paper.html) — Plack et al. | WACV 2023 | Introduces a fast differentiable transient renderer that reduces analysis-by-synthesis NLOS inverse-rendering runtimes from hours to minutes on consumer hardware, improves optimization stability, and enables self-supervised transient reconstruction. |"
        text = replace_once(text, anchor, anchor + "\n" + row, "README latest-additions")

    old_timeline = (
        "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]\n"
        "   │     Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]"
    )
    new_timeline = (
        "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]\n"
        "   │     Huang et al.: Omni-LOS — joint LOS/NLOS neural transients for near-360° single-position shape [arXiv]\n"
        "   │     Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]"
    )
    text = replace_once(text, old_timeline, new_timeline, "README 2023 timeline")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("Updated 13 July 2026 · 190+ papers", "Updated 14 July 2026 · 190+ papers", 1)
    text = text.replace("Last updated: 13 July 2026", "Last updated: 14 July 2026", 1)
    text = replace_once(
        text,
        '<div class="stat"><b>94</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>95</b><span>tracked latest entries</span></div>',
        "homepage latest-count",
    )

    paper = (
        '      {cat:"latest active learning",title:"Omni-Line-of-Sight Imaging for Holistic Shape Reconstruction",'
        'authors:"Huang et al.",year:2023,venue:"arXiv 2023",'
        f'url:"{URL}",'
        'key:"Unifies straight-ray LOS and spherical-wavefront NLOS transients in a neural level-set model, using diffuse walls as virtual mirrors for near-360° single-position shape recovery."},'
    )
    if TITLE not in text:
        marker = "    const papers=[\n"
        text = replace_once(text, marker, marker + paper + "\n", "homepage paper array")

    old_tl = '<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Fast differentiable transient rendering, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, self-calibration, and active corner cameras</strong><p>Plack et al. reduced physically based analysis-by-synthesis NLOS reconstruction from hours to minutes on consumer hardware; NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor fields, and active corner cameras broadened reconstruction settings; Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging.</p></div></div>'
    new_tl = '<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Fast differentiable rendering, joint LOS/NLOS holistic shape, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, self-calibration, and active corner cameras</strong><p>Plack et al. reduced physically based analysis-by-synthesis NLOS reconstruction from hours to minutes on consumer hardware; Omni-LOS unified straight-ray LOS and spherical-wavefront NLOS transients in a neural level-set model for near-360° shape recovery from one fixed scan position; NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor fields, and active corner cameras broadened reconstruction settings; Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging.</p></div></div>'
    text = replace_once(text, old_tl, new_tl, "homepage 2023 timeline")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Joint LOS/NLOS holistic shape reconstruction.}\n"
        "Huang~\\etal~introduced Omni-LOS, which combines direct LOS transients and diffuse-wall NLOS transients in a unified neural level-set representation~\\cite{huangOmniLOS2023}. The method derives differentiable rendering models for straight LOS rays and spherical NLOS wavefronts, jointly optimizing visible front surfaces and self-occluded back geometry from a fixed scan position. With nearby walls acting as diffuse virtual mirrors and a SPAD--laser prototype, Omni-LOS recovers near-$360^\\circ$ object shape without a surrounding camera or mirror rig, extending neural transient imaging from hidden-scene reconstruction toward holistic single-position 3D scanning."
    )
    if KEY not in text:
        anchor = "Fujimura~\\etal~proposed NLOS-NeuS, extending neural transient fields to neural implicit surfaces with a signed distance function (SDF) representation~\\cite{fujimuraNLOSNeuS2023}. By incorporating SDF constraints derived from first-returning photon geometry, NLOS-NeuS enables smooth yet detailed 3D surface reconstruction in NLOS scenes, overcoming the voxel resolution limitation of volumetric methods. This represents the first neural implicit surface approach with volume rendering for NLOS scenes."
        text = replace_once(text, anchor, anchor + paragraph, "survey neural-surface paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE}")


if __name__ == "__main__":
    main()
