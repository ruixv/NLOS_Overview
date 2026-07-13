#!/usr/bin/env python3
"""Idempotently synchronize the Plack et al. WACV 2023 NLOS paper."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Fast Differentiable Transient Rendering for Non-Line-of-Sight Reconstruction"
URL = "https://openaccess.thecvf.com/content/WACV2023/html/Plack_Fast_Differentiable_Transient_Rendering_for_Non-Line-of-Sight_Reconstruction_WACV_2023_paper.html"
KEY = "plackFastDifferentiableTransient2023"


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
    row = (
        f"| 2023 | [{TITLE}]({URL}) — Plack et al. | WACV 2023 | "
        "Introduces a fast differentiable transient renderer that reduces analysis-by-synthesis NLOS inverse-rendering runtimes from hours to minutes on consumer hardware, improves optimization stability, and enables self-supervised transient reconstruction. |"
    )
    if TITLE not in text:
        anchor = "| 2023 | [Virtual Mirrors: Non-Line-of-Sight Imaging Beyond the Third Bounce](https://doi.org/10.1145/3592429) — Royo et al. | ACM TOG / SIGGRAPH 2023 | Treats planar diffuse hidden surfaces as computational phasor-domain ‘virtual mirrors’, builds secondary virtual apertures from higher-order bounces, and reconstructs limited-visibility geometry and objects hidden behind a second corner without requiring physical specular reflectors. |"
        text = replace_once(text, anchor, anchor + "\n" + row, "README latest-additions")

    old_timeline = "2023 ── Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]"
    new_timeline = (
        "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]\n"
        "   │     Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]"
    )
    text = replace_once(text, old_timeline, new_timeline, "README 2023 timeline")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '<div class="stat"><b>93</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>94</b><span>tracked latest entries</span></div>',
        "homepage latest-count",
    )

    paper = (
        '      {cat:"latest active learning",title:"Fast Differentiable Transient Rendering for Non-Line-of-Sight Reconstruction",'
        'authors:"Plack et al.",year:2023,venue:"WACV 2023",'
        f'url:"{URL}",'
        'key:"A physically based differentiable transient renderer cuts analysis-by-synthesis NLOS optimization from hours to minutes on consumer hardware, improves stability, and supports self-supervised reconstruction."},'
    )
    if TITLE not in text:
        marker = "    const papers=[\n"
        text = replace_once(text, marker, marker + paper + "\n", "homepage paper array")

    old_tl = '<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, self-calibrating inverse rendering, and active corner cameras</strong><p>NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor fields, and active corner cameras broadened reconstruction settings; Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging.</p></div></div>'
    new_tl = '<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Fast differentiable transient rendering, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, self-calibration, and active corner cameras</strong><p>Plack et al. reduced physically based analysis-by-synthesis NLOS reconstruction from hours to minutes on consumer hardware; NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor fields, and active corner cameras broadened reconstruction settings; Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging.</p></div></div>'
    text = replace_once(text, old_tl, new_tl, "homepage 2023 timeline")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Fast differentiable transient rendering.}\n"
        "Plack~\\etal~introduced a physically based differentiable transient renderer tailored to NLOS reconstruction~\\cite{plackFastDifferentiableTransient2023}. By making gradients through time-resolved light transport efficient enough for consumer hardware, their analysis-by-synthesis pipeline reduces inverse-rendering runtimes from hours to minutes while improving optimization stability. The same renderer also supports self-supervised learning, forming an important bridge between explicit transient inverse rendering and later self-calibrating or learned NLOS reconstruction pipelines."
    )
    if KEY not in text:
        anchor = "Compared with voxel-based inverse methods, inverse rendering can reconstruct more details, but often requires higher temporal complexity\\cite{Young:2020:dlct,heideNonlineofsightImagingPartial2017}."
        text = replace_once(text, anchor, anchor + paragraph, "survey inverse-rendering paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE}")


if __name__ == "__main__":
    main()
