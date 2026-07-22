#!/usr/bin/env python3
"""Synchronize the 2026 experimental NLOS micro-Doppler drone-detection paper.

The update is fail-closed: it only edits unique structural anchors, refuses
partial duplication, and validates every public/survey artifact after writing.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ARXIV_ID = "2607.11868"
KEY = "liyanageSUASNLOSRadar2026"
MARKER = "% 22 July 2026 citation trace: experimental NLOS micro-Doppler drone detection integrated."


def load(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def save(name: str, text: str) -> None:
    (ROOT / name).write_text(text, encoding="utf-8")


def sub_once(pattern: str, repl: str | callable, text: str, label: str, flags: int = 0) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return out


def already_integrated() -> bool:
    readme = load("README.md")
    if ARXIV_ID not in readme:
        return False
    checks = {
        "README.md": ARXIV_ID,
        "index.html": ARXIV_ID,
        "article/5newscenes.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    missing = [name for name, needle in checks.items() if needle not in load(name)]
    if missing:
        raise RuntimeError(
            "Partial prior integration detected; refusing unsafe repair: " + ", ".join(missing)
        )
    return True


def update_readme() -> None:
    name = "README.md"
    text = load(name)
    if ARXIV_ID in text:
        raise RuntimeError("README already contains the sUAS paper")

    row = (
        "| 2026 | [Detection of sUAS in Urban Environments using Multi-Antenna Micro-Doppler Radar]"
        "(https://arxiv.org/abs/2607.11868) — Liyanage et al. | IEEE VTC2026-Fall (accepted) | "
        "Uses a hardware-validated 2.47 GHz four-receiver CW MIMO radar and cyclostationary "
        "propeller micro-Doppler features for hidden-drone detection in indoor and semi-urban NLOS "
        "settings. A compact EfficientNet-B0 model reaches 86.11% overall accuracy; the result is "
        "detection-only, with stationary airframes and no hidden-target localization or 3D reconstruction. |\n"
    )
    text = sub_once(
        r"(?m)^(\|------\|-------\|----------------\|----------------\|\s*)$",
        lambda m: m.group(1) + "\n" + row.rstrip("\n"),
        text,
        "README latest-additions header",
    )

    anchor = (
        "    │     Lin and Chen: urban-intersection FMCW NLOS perception — chirp-level residual "
        "learning suppresses simulated interference before conventional range/angle estimation "
        "[Computer Modeling in Engineering & Sciences]"
    )
    milestone = (
        "    │     Liyanage et al.: multi-antenna micro-Doppler radar preserves cyclostationary rotor "
        "cues through cabinets, doors, and walls for experimental NLOS drone detection "
        "[IEEE VTC2026-Fall, accepted]"
    )
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one README radar milestone anchor, found {text.count(anchor)}")
    text = text.replace(anchor, anchor + "\n" + milestone, 1)
    save(name, text)


def update_index() -> None:
    name = "index.html"
    text = load(name)
    if ARXIV_ID in text:
        raise RuntimeError("Homepage already contains the sUAS paper")

    text = sub_once(
        r'<div class="stat"><b>182</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>183</b><span>tracked latest entries</span></div>',
        text,
        "homepage tracked-entry count",
    )

    paper = (
        '      {cat:"latest modality radar rf detection learned",'
        'title:"Detection of sUAS in Urban Environments using Multi-Antenna Micro-Doppler Radar",'
        'authors:"Liyanage et al.",year:2026,venue:"IEEE VTC2026-Fall (accepted)",'
        'url:"https://arxiv.org/abs/2607.11868",'
        'key:"A hardware-validated 2.47 GHz 1×4 CW MIMO radar converts propeller micro-Doppler into '
        'spectral-correlation images for experimental NLOS drone detection. Four-channel EfficientNet-B0 '
        'reaches 86.11% accuracy; it is detection-only and does not reconstruct or localize the hidden target."},\n'
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
        " A hardware-validated multi-antenna CW radar also showed that cyclostationary drone-rotor "
        "micro-Doppler remains discriminative through cabinets, doors, and walls, extending RF NLOS "
        "toward experimental hidden-UAS detection while stopping short of localization or 3D imaging."
    )
    if "cyclostationary drone-rotor" in match.group(2):
        raise RuntimeError("Homepage 2026 timeline already contains the sUAS milestone")
    replacement = match.group(1) + match.group(2).rstrip() + addition + match.group(3)
    text = text[: match.start()] + replacement + text[match.end() :]
    save(name, text)


def update_radar_survey() -> None:
    name = "article/5newscenes.tex"
    text = load(name)
    if KEY in text:
        raise RuntimeError("Radar survey already cites the sUAS paper")

    anchor = (
        "Lin and Chen studied an application-facing 77~GHz automotive-radar setting in which specular "
        "reflections from buildings provide around-corner observations at occluded urban intersections~"
        "\\cite{linDeepLearningFMCWRadar2026}. Their compact one-dimensional, AlexNet-derived regression "
        "network restores interference-corrupted chirps before standard range and angular estimation, "
        "reducing simulated severe-interference errors from $5.48$~m/$18.95^{\\circ}$/$10.77^{\\circ}$ "
        "to $0.56$~m/$0.46^{\\circ}$/$0.73^{\\circ}$ for range, angle, and azimuth deviation, respectively. "
        "Unlike measured radar geometry reconstruction systems, the study is evaluated entirely in MATLAB "
        "simulation; its value is therefore as a learned signal-restoration and autonomous-driving NLOS "
        "perception branch, with real-road multipath and material validation remaining open."
    )
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one urban-radar paragraph anchor, found {text.count(anchor)}")

    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Cyclostationary micro-Doppler detection in fully NLOS scenes.}\n"
        "Liyanage~\\etal~built a 2.47~GHz continuous-wave MIMO radar with one transmitter and four "
        "receivers and used spectral correlation density images of propeller micro-Doppler as inputs "
        "to a compact EfficientNet-B0 detector~\\cite{liyanageSUASNLOSRadar2026}. Measurements collected "
        "in indoor and semi-urban settings used cabinets, doors, and walls to block the direct path; "
        "cyclic rotor features remained visible under multipath, and the four-channel model achieved "
        "86.11\\% overall accuracy compared with 73.77\\% for a single-channel baseline. This result "
        "broadens NLOS radar from vehicles, pedestrians, and static hidden geometry toward low-altitude "
        "aerial-threat sensing. It should nevertheless be distinguished from imaging: the airframes were "
        "stationary while the propellers rotated, and the reported task was binary detection rather than "
        "localization, tracking, or hidden-shape reconstruction."
    )
    text = text.replace(anchor, anchor + paragraph, 1)
    save(name, text)


def update_master() -> None:
    name = "bare_jrnl.tex"
    text = load(name)
    if MARKER in text:
        raise RuntimeError("Master survey already contains the sUAS integration marker")
    text = sub_once(
        r"(?m)^%% bare_jrnl\.tex\s*$",
        "%% bare_jrnl.tex\n" + MARKER,
        text,
        "master survey header",
    )
    save(name, text)


def validate() -> None:
    checks = {
        "README.md": ARXIV_ID,
        "index.html": ARXIV_ID,
        "article/5newscenes.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    for name, needle in checks.items():
        text = load(name)
        if text.count(needle) != 1:
            raise RuntimeError(f"Postcondition failed for {name}: expected one {needle!r}")
    if '<div class="stat"><b>183</b><span>tracked latest entries</span></div>' not in load("index.html"):
        raise RuntimeError("Homepage tracked-entry count was not updated to 183")


def main() -> None:
    if already_integrated():
        print("sUAS NLOS radar paper is already fully integrated; no changes needed.")
        return
    update_readme()
    update_index()
    update_radar_survey()
    update_master()
    validate()
    print("Integrated experimental NLOS micro-Doppler drone detection across public and survey sources.")


if __name__ == "__main__":
    main()
