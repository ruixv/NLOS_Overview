#!/usr/bin/env python3
"""Synchronize the Virtual Mirrors higher-order NLOS citation-tracing update.

Edits are marker-based and idempotent. The script aborts rather than replacing a
large hand-maintained file when an expected marker is absent or ambiguous.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Virtual Mirrors: Non-Line-of-Sight Imaging Beyond the Third Bounce"
KEY = "royoVirtualMirrors2023"
DOI_URL = "https://doi.org/10.1145/3592429"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} marker, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    text = read("README.md")
    if TITLE not in text:
        separator = "|------|-------|----------------|----------------|\n"
        row = (
            f"| 2023 | [{TITLE}]({DOI_URL}) — Royo et al. | ACM TOG / SIGGRAPH 2023 | "
            "Treats planar diffuse hidden surfaces as computational phasor-domain ‘virtual mirrors’, builds secondary virtual apertures from higher-order bounces, and reconstructs limited-visibility geometry and objects hidden behind a second corner without requiring physical specular reflectors. |\n"
        )
        text = replace_once(text, separator, separator + row, "README latest-table separator")

    milestone = (
        "2023 ── Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]\n"
        "   │\n"
    )
    if "2023 ── Royo et al.: virtual mirrors" not in text:
        marker = "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n   │\n```"
        replacement = (
            "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n"
            "   │\n"
            + milestone
            + "```"
        )
        text = replace_once(text, marker, replacement, "README timeline terminator")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"README should contain one full-title entry, found {text.count(TITLE)}")
    write("README.md", text)


def update_homepage() -> None:
    text = read("index.html")
    if '<b>87</b><span>tracked latest entries</span>' in text:
        text = text.replace(
            '<b>87</b><span>tracked latest entries</span>',
            '<b>88</b><span>tracked latest entries</span>',
            1,
        )
    elif '<b>88</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage tracked-entry count is neither 87 nor 88")

    if TITLE not in text:
        object_line = (
            '      {cat:"latest active",title:"Virtual Mirrors: Non-Line-of-Sight Imaging Beyond the Third Bounce",'
            'authors:"Royo et al.",year:2023,venue:"ACM TOG / SIGGRAPH 2023",'
            'url:"https://doi.org/10.1145/3592429",'
            'key:"Planar diffuse hidden surfaces become computational phasor-domain mirrors; secondary virtual apertures use higher-order transport to recover limited-visibility geometry and objects hidden behind a second corner."},\n'
        )
        marker = '      {cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering"'
        text = replace_once(text, marker, object_line + marker, "homepage 2023 paper insertion")

    old_timeline = (
        '      <div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Transformers, arbitrary patterns, neural implicit NLOS, self-calibrating inverse rendering, and active corner cameras</strong><p>NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor fields, passive acoustic corners, and active corner-camera background mapping broadened reconstruction settings.</p></div></div>'
    )
    new_timeline = (
        '      <div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, self-calibrating inverse rendering, and active corner cameras</strong><p>NLOST, PAC-Net, NLOS-NeuS, arbitrary illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor fields, and active corner cameras broadened reconstruction settings; Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging.</p></div></div>'
    )
    if "Virtual Mirrors turned higher-order phasor transport" not in text:
        text = replace_once(text, old_timeline, new_timeline, "homepage 2023 timeline")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"Homepage should contain one full-title entry, found {text.count(TITLE)}")
    if '<b>88</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage count did not update to 88")
    write("index.html", text)


def update_survey() -> None:
    text = read("article/2active.tex")
    old_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Higher-Order Bounce Imaging.}
Standard NLOS methods consider exactly three-bounce light (relay wall $\to$ hidden object $\to$ relay wall). Royo~\etal~extended the imaging model to exploit fourth-bounce reflections caused by vertical specular surfaces (``virtual mirrors'') inside the hidden scene, allowing NLOS systems to observe parts of the scene that are completely invisible to three-bounce methods~\cite{royoVirtualMirrors2023}. This work demonstrates that leveraging higher-order light interactions can significantly increase the completeness of hidden scene reconstruction.'''
    new_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Higher-Order Bounce Imaging.}
Standard transient NLOS reconstruction usually truncates transport at the third bounce, which limits visibility for unfavorably oriented surfaces and confines most systems to a single corner. Royo~\etal~showed that planar diffuse surfaces behave specularly at the computational wavelengths of the phasor-field domain and can therefore act as ``virtual mirrors''~\cite{royoVirtualMirrors2023}. By propagating measured transients to these surfaces and constructing secondary virtual apertures, their method recovers limited-visibility geometry and objects hidden behind a second corner without requiring physical specular reflectors. This result shifts higher-order light transport from a discarded nuisance to an additional imaging resource.'''

    if "This result shifts higher-order light transport" not in text:
        text = replace_once(text, old_paragraph, new_paragraph, "survey higher-order-bounce paragraph")

    if text.count(f"\\cite{{{KEY}}}") != 1:
        raise RuntimeError(f"Survey should cite {KEY} exactly once")
    write("article/2active.tex", text)


def main() -> None:
    source_bib = ROOT / "egbib_20260712_virtual_mirrors_updates.bib"
    if not source_bib.exists() or KEY not in source_bib.read_text(encoding="utf-8"):
        raise RuntimeError("Virtual Mirrors source BibTeX record is missing")
    update_readme()
    update_homepage()
    update_survey()
    print("Synchronized Virtual Mirrors across README, homepage, timeline, and survey source.")


if __name__ == "__main__":
    main()
