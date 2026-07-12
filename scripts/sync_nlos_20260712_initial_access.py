#!/usr/bin/env python3
"""Synchronize the 6G initial-access NLOS imaging citation-tracing update.

Edits are marker-based and idempotent. The script aborts rather than replacing a
large hand-maintained file when an expected marker is absent or ambiguous.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Enabling NLOS Imaging Capabilities at the Initial Access of 6G Base Stations"
KEY = "tornielliInitialAccessNLOS2025"
URL = "https://arxiv.org/abs/2511.15416"


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
        marker = (
            "| 2025 | [MITO: Enabling Non-Line-of-Sight Perception using Millimeter-waves through "
            "Real-World Datasets and Simulation Tools](https://arxiv.org/abs/2502.10259) — Dodds et al. "
            "| arXiv 2025 | Dataset and simulation tooling for mmWave NLOS perception with paired LOS/NLOS "
            "captures and RGB-D/mask supervision. |\n"
        )
        row = (
            f"| 2025 | [{TITLE}]({URL}) — Tornielli Bellini et al. | arXiv 2025 | "
            "Integrates coherent reflector-assisted NLOS imaging into the standard initial-access beam sweep "
            "of a next-generation base station; jointly designs a static modular reflector and imaging-specific "
            "codebook, derives near-field resolution/effective-aperture and moving-target trade-offs, and "
            "validates the system experimentally. |\n"
        )
        text = replace_once(text, marker, row + marker, "README MITO row")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"README should contain one full-title entry, found {text.count(TITLE)}")
    write("README.md", text)


def update_homepage() -> None:
    text = read("index.html")
    if '<b>88</b><span>tracked latest entries</span>' in text:
        text = text.replace(
            '<b>88</b><span>tracked latest entries</span>',
            '<b>89</b><span>tracked latest entries</span>',
            1,
        )
    elif '<b>89</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage tracked-entry count is neither 88 nor 89")

    if TITLE not in text:
        object_line = (
            '      {cat:"latest modality active",title:"Enabling NLOS Imaging Capabilities at the Initial Access of 6G Base Stations",'
            'authors:"Tornielli Bellini et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2511.15416",'
            'key:"Integrates coherent reflector-assisted NLOS imaging into a 5G/6G base-station initial-access beam sweep, deriving effective-aperture and moving-target trade-offs and validating the system experimentally."},\n'
        )
        marker = '      {cat:"latest modality dataset",title:"MITO: Enabling Non-Line-of-Sight Perception using Millimeter-waves through Real-World Datasets and Simulation Tools"'
        text = replace_once(text, marker, object_line + marker, "homepage MITO insertion")

    old_timeline = (
        '      <div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, graph models, pretraining, radar, acoustic, and robotic NLOS</strong><p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, MITO, N2LoS, mmMirror, and relay-free acoustic NLOS broadened the toolbox.</p></div></div>'
    )
    new_timeline = (
        '      <div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, graph models, pretraining, radar, acoustic, 6G initial-access imaging, and robotic NLOS</strong><p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, MITO, N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and relay-free acoustic NLOS broadened the toolbox.</p></div></div>'
    )
    if "reflector-assisted base-station initial-access imaging" not in text:
        text = replace_once(text, old_timeline, new_timeline, "homepage 2025 timeline")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"Homepage should contain one full-title entry, found {text.count(TITLE)}")
    if '<b>89</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage count did not update to 89")
    write("index.html", text)


def update_survey() -> None:
    text = read("article/5newscenes.tex")
    paragraph = r'''Tornielli Bellini~\etal~push reflector-assisted RF NLOS imaging toward communication infrastructure by embedding a monostatic hidden-scene imaging mode into the initial-access beam sweep of a next-generation base station~\cite{tornielliInitialAccessNLOS2025}. A low-cost non-reconfigurable modular reflector and imaging-specific codebook extend the standard communication beams; coherent processing across the resulting viewpoints forms an effective aperture for near-field reflectivity imaging, while a maximum-likelihood velocity estimator compensates moving targets. By deriving resolution, aperture, latency, SNR, and communication--imaging trade-offs and validating the design experimentally, this work connects earlier electromagnetic-skin NLOS prototypes to standard-aware 6G ISAC deployment.

'''
    if f"\\cite{{{KEY}}}" not in text:
        marker = r'''\bookmark[dest=\HyperLocalCurrentHref,level=2]{Acoustic NLOS Imaging}
'''
        text = replace_once(text, marker, paragraph + marker, "survey acoustic-section marker")

    if text.count(f"\\cite{{{KEY}}}") != 1:
        raise RuntimeError(f"Survey should cite {KEY} exactly once")
    write("article/5newscenes.tex", text)


def main() -> None:
    source_bib = ROOT / "egbib_20260712_initial_access_updates.bib"
    if not source_bib.exists() or KEY not in source_bib.read_text(encoding="utf-8"):
        raise RuntimeError("6G initial-access source BibTeX record is missing")
    update_readme()
    update_homepage()
    update_survey()
    print("Synchronized 6G initial-access NLOS imaging across README, homepage, timeline, and survey source.")


if __name__ == "__main__":
    main()
