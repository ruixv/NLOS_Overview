#!/usr/bin/env python3
"""Synchronize D-NeSF across the NLOS overview artifacts.

This update is fail-closed: it edits only unique structural anchors, refuses
partial duplication, and validates every public/survey artifact after writing.
"""
from __future__ import annotations

from pathlib import Path
import re
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1117/12.3095236"
KEY = "zhangDynamicNeuralShadowFields2026"
MARKER = "% 22 July 2026 citation trace: dynamic neural shadow fields for moving two-bounce NLOS integrated."


def load(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def save(name: str, text: str) -> None:
    (ROOT / name).write_text(text, encoding="utf-8")


def sub_once(pattern: str, repl: str | Callable[[re.Match[str]], str], text: str,
             label: str, flags: int = 0) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return out


def already_integrated() -> bool:
    if DOI not in load("README.md"):
        return False
    checks = {
        "README.md": DOI,
        "index.html": DOI,
        "article/5newscenes.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    missing = [name for name, needle in checks.items() if needle not in load(name)]
    if missing:
        raise RuntimeError(
            "Partial prior D-NeSF integration detected; refusing unsafe repair: "
            + ", ".join(missing)
        )
    return True


def update_readme() -> None:
    name = "README.md"
    text = load(name)
    if DOI in text:
        raise RuntimeError("README already contains D-NeSF")

    row = (
        "| 2026 | [D-NeSF: Dynamic Neural Shadow Fields for Two-bounce Non-line-of-sight "
        "Stereo Reconstruction](https://doi.org/10.1117/12.3095236) — Zhang et al. | "
        "ICGIP 2025 / Proceedings of SPIE 14124 (2026) | Extends two-bounce shadow-based "
        "NLOS from static occupancy or illumination fields to moving hidden geometry. A "
        "spatiotemporally disentangled six-plane neural field, cyclic multi-position illumination, "
        "and self-supervised cumulative-transmittance constraints reconstruct temporally consistent "
        "dynamic 3D targets from shadow sequences. |\n"
    )
    text = sub_once(
        r"(?m)^(\|------\|-------\|----------------\|----------------\|\s*)$",
        lambda m: m.group(1) + "\n" + row.rstrip("\n"),
        text,
        "README latest-additions header",
    )

    anchor = (
        "   │     Wang et al.: GenPIE — generative geometry priors and differentiable transient "
        "transport recover a time-resolved plenoptic representation [SIGGRAPH / ACM TOG]"
    )
    milestone = (
        "   │     Zhang et al.: D-NeSF — spatiotemporally disentangled neural shadow fields extend "
        "two-bounce NLOS stereo reconstruction from static scenes to moving hidden targets "
        "[ICGIP / Proceedings of SPIE]"
    )
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one README 2026 milestone anchor, found {text.count(anchor)}")
    text = text.replace(anchor, anchor + "\n" + milestone, 1)
    save(name, text)


def update_index() -> None:
    name = "index.html"
    text = load(name)
    if DOI in text:
        raise RuntimeError("Homepage already contains D-NeSF")

    text = sub_once(
        r'<div class="stat"><b>183</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>184</b><span>tracked latest entries</span></div>',
        text,
        "homepage tracked-entry count",
    )

    paper = (
        '      {cat:"latest newscenes active shadow two-bounce dynamic learned neural",'
        'title:"D-NeSF: Dynamic Neural Shadow Fields for Two-bounce Non-line-of-sight Stereo Reconstruction",'
        'authors:"Zhang et al.",year:2026,venue:"ICGIP 2025 / Proceedings of SPIE 14124 (2026)",'
        'url:"https://doi.org/10.1117/12.3095236",'
        'key:"A six-plane spatiotemporally disentangled neural shadow field combines cyclic multi-position '
        'illumination with self-supervised cumulative-transmittance constraints to reconstruct temporally '
        'consistent moving 3D targets in two-bounce NLOS scenes."},\n'
    )
    text = sub_once(
        r"(?m)^(\s*const papers=\[\s*)$",
        lambda m: m.group(1) + "\n" + paper.rstrip("\n"),
        text,
        "homepage paper array",
    )

    pattern = r'(<div class="tl"><div class="year">2026</div>.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError("Could not locate homepage 2026 timeline")
    addition = (
        " D-NeSF then extended the two-bounce neural-shadow trajectory from static hidden volumes "
        "to moving targets through a six-plane spatiotemporal representation and cyclic shadow capture."
    )
    if "D-NeSF then extended" in match.group(2):
        raise RuntimeError("Homepage 2026 timeline already contains D-NeSF")
    replacement = match.group(1) + match.group(2).rstrip() + addition + match.group(3)
    text = text[:match.start()] + replacement + text[match.end():]
    save(name, text)


def update_survey_section() -> None:
    name = "article/5newscenes.tex"
    text = load(name)
    if KEY in text:
        raise RuntimeError("New-scenes survey already cites D-NeSF")

    anchor = (
        "A complementary steady-state trajectory replaces binary shadow carving with a continuous learned "
        "scene model. Zhang~\\etal~introduced Neural Illumination Fields (NIF)~"
        "\\cite{zhangNeuralIlluminationFields2026}, which jointly represents hidden-space density and "
        "illumination-dependent image formation with multilayer perceptrons and optimizes the representation "
        "through differentiable intensity rendering. Because NIF synthesizes measured shadow images directly, "
        "it avoids error-prone binary shadow segmentation and remains effective under low shadow contrast and "
        "ambient-light interference. This work shifts two-bounce NLOS from discrete occupancy carving toward "
        "self-supervised neural inverse rendering for large hidden volumes."
    )
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one NIF survey anchor, found {text.count(anchor)}")

    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Dynamic neural shadow fields for moving two-bounce scenes.}\n"
        "The static-scene assumption remains restrictive when hidden people or objects move during a cyclic "
        "multi-position scan. Zhang~\\etal~addressed this regime with D-NeSF~"
        "\\cite{zhangDynamicNeuralShadowFields2026}, decomposing the four-dimensional hidden volume into six "
        "spatiotemporal feature planes whose interpolated features are mapped by an MLP to time-varying voxel "
        "density. A cyclic acquisition strategy aligns repeated illumination positions with periodic shadow "
        "observations, while a cumulative-transmittance constraint enables self-supervised fitting to captured "
        "binary shadow sequences. This work extends the two-bounce neural-field trajectory from high-fidelity "
        "static geometry to temporally consistent reconstruction of moving hidden targets, and exposes motion "
        "modeling and scan-time synchronization as central design variables for dynamic shadow-based NLOS."
    )
    text = text.replace(anchor, anchor + paragraph, 1)
    save(name, text)


def update_master() -> None:
    name = "bare_jrnl.tex"
    text = load(name)
    if MARKER in text:
        raise RuntimeError("Master survey already contains D-NeSF marker")
    text = sub_once(
        r"(?m)^%% bare_jrnl\.tex\s*$",
        "%% bare_jrnl.tex\n" + MARKER,
        text,
        "master survey header",
    )
    if "extends coverage to include significant advances from 2022 through 21 July 2026" in text:
        text = text.replace(
            "extends coverage to include significant advances from 2022 through 21 July 2026",
            "extends coverage to include significant advances from 2022 through 22 July 2026",
            1,
        )
    save(name, text)


def validate() -> None:
    checks = {
        "README.md": DOI,
        "index.html": DOI,
        "article/5newscenes.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    for name, needle in checks.items():
        count = load(name).count(needle)
        if count != 1:
            raise RuntimeError(f"Postcondition failed for {name}: expected one {needle!r}, found {count}")
    if '<div class="stat"><b>184</b><span>tracked latest entries</span></div>' not in load("index.html"):
        raise RuntimeError("Homepage tracked-entry count was not updated to 184")
    if "through 22 July 2026" not in load("bare_jrnl.tex"):
        raise RuntimeError("Survey coverage date was not synchronized to 22 July 2026")


def main() -> None:
    if already_integrated():
        print("D-NeSF is already fully integrated; no changes needed.")
        return
    update_readme()
    update_index()
    update_survey_section()
    update_master()
    validate()
    print("Integrated D-NeSF across README, homepage, survey source, and master metadata.")


if __name__ == "__main__":
    main()
