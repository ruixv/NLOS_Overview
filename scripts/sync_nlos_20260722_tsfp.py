#!/usr/bin/env python3
"""Synchronize the 2022 time-sequential first-photon NLOS milestone.

The script is fail-closed but tolerant of harmless whitespace changes: every
edit uses a structurally unique regex anchor and validates the final state.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1364/OL.446079"
KEY = "liFirstPhotonStamping2022"


def load(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def save(name: str, text: str) -> None:
    (ROOT / name).write_text(text, encoding="utf-8")


def sub_once(pattern: str, repl: str, text: str, label: str, flags: int = 0) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return out


def assert_absent(text: str, needle: str, label: str) -> None:
    if needle.casefold() in text.casefold():
        raise RuntimeError(f"{label} already contains {needle!r}; refusing duplication")


def update_readme() -> None:
    name = "README.md"
    text = load(name)
    assert_absent(text, DOI, name)
    row = (
        "| 2022 | [Fast non-line-of-sight imaging based on first photon event stamping]"
        "(https://doi.org/10.1364/OL.446079) — Li et al. | Optics Letters 2022 | "
        "Introduces time-sequential first-photon (TSFP) acquisition for active transient NLOS, "
        "modeling the detection process rather than changing the downstream inverse operator. "
        "Synthetic and measured experiments retain comparable reconstruction quality with "
        "substantially shorter acquisition, making the method relevant to photon-starved and "
        "real-time systems. |\n"
    )
    text = sub_once(
        r"(?m)^(\|------\|-------\|----------------\|----------------\|\s*)$",
        lambda m: m.group(1) + "\n" + row.rstrip("\n"),
        text,
        "README latest-additions header",
    )
    text = sub_once(
        r"(?m)^(2022 ── Grau et al\.: Occlusion Fields[^\n]*)(\n)",
        lambda m: m.group(1) + m.group(2)
        + "   │     Li et al.: time-sequential first-photon stamping — detection-aware acquisition reduces photon collection time for active transient NLOS [Optics Letters]\n",
        text,
        "README 2022 milestone",
    )
    save(name, text)


def update_index() -> None:
    name = "index.html"
    text = load(name)
    assert_absent(text, DOI, name)
    text = sub_once(
        r'<div class="stat"><b>181</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>182</b><span>tracked latest entries</span></div>',
        text,
        "homepage tracked-entry count",
    )
    paper = (
        '      {cat:"latest active acquisition hardware photon-starved",'
        'title:"Fast non-line-of-sight imaging based on first photon event stamping",'
        'authors:"Li et al.",year:2022,venue:"Optics Letters 2022",'
        'url:"https://doi.org/10.1364/OL.446079",'
        'key:"Time-sequential first-photon acquisition models the SPAD detection process directly, '
        'preserving comparable hidden-scene reconstruction with substantially shorter acquisition '
        'for photon-starved and prospective real-time transient NLOS."},\n'
    )
    text = sub_once(
        r"(?m)^(\s*const papers=\[\s*)$",
        lambda m: m.group(1) + "\n" + paper.rstrip("\n"),
        text,
        "homepage paper array",
    )
    timeline_pattern = r'(<div class="tl"><div class="year">2022</div>.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(timeline_pattern, text, flags=re.S)
    if not match:
        raise RuntimeError("Could not locate homepage 2022 timeline")
    if "time-sequential first-photon" in match.group(2).casefold():
        raise RuntimeError("Homepage 2022 timeline already contains TSFP")
    replacement = (
        match.group(1) + match.group(2).rstrip()
        + " Time-sequential first-photon stamping additionally moved acquisition design into the detector model, reducing the photon-collection burden without replacing established LCT, f-k, or phasor-field reconstruction back ends."
        + match.group(3)
    )
    text = text[:match.start()] + replacement + text[match.end():]
    save(name, text)


def update_active() -> None:
    name = "article/2active.tex"
    text = load(name)
    assert_absent(text, KEY, name)
    table_pattern = r"(?m)^(\s*\\cite\{[^\n}]*marcoVirtualLightTransport2021)(\}\s*& Pulsed laser & SPAD & Time of fight &\s*3D reconstruction.*)$"
    text = sub_once(
        table_pattern,
        lambda m: m.group(1) + "," + KEY + m.group(2),
        text,
        "active SPAD reconstruction table",
    )
    spad_sentence = (
        "Moreover, SPAD has been widely used in commercial LiDAR systems, and the SPAD array, "
        "which can avoid the mechanical raster scan process, has the potential to save scanning "
        "time and realize real-time data collection for active NLOS imaging."
    )
    pos = text.find(spad_sentence)
    if pos < 0:
        raise RuntimeError("Could not locate SPAD-array discussion")
    end = pos + len(spad_sentence)
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Time-sequential first-photon acquisition.}\n"
        "Most transient NLOS work optimizes the forward model or inverse solver after accumulating a photon-arrival histogram. Li~\\etal~instead examined the detector process and represented each measurement by time-sequential first-photon events~\\cite{liFirstPhotonStamping2022}. Their TSFP likelihood uses the earliest detection in successive laser periods and was validated on synthetic and measured hidden scenes, obtaining reconstruction quality comparable to conventional histogram acquisition with substantially less collection time. This detection-aware branch is complementary to LCT, $f$-$k$ migration, and phasor-field propagation: it reduces the photon and acquisition budget before those inverse operators are applied, and therefore provides an early link between single-photon statistics, photon-starved operation, and later real-time NLOS systems."
    )
    text = text[:end] + paragraph + text[end:]
    save(name, text)


def update_master() -> None:
    name = "bare_jrnl.tex"
    text = load(name)
    marker = "% 22 July 2026 citation trace: time-sequential first-photon NLOS acquisition integrated."
    assert_absent(text, marker, name)
    text = sub_once(
        r"(?m)^%% bare_jrnl\.tex\s*$",
        "%% bare_jrnl.tex\n" + marker,
        text,
        "master survey header",
    )
    save(name, text)


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_master()
    for name in ("README.md", "index.html", "article/2active.tex"):
        text = load(name)
        if DOI not in text and KEY not in text:
            raise RuntimeError(f"Postcondition failed for {name}")
    print("Integrated TSFP NLOS acquisition across README, homepage, survey, and master source.")


if __name__ == "__main__":
    main()
