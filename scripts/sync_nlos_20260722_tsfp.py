#!/usr/bin/env python3
"""Synchronize the 2022 time-sequential first-photon NLOS acquisition milestone.

The script is deliberately fail-closed: every insertion uses a unique verified
anchor and refuses to run if the DOI is already present or repository structure
has drifted. This avoids blind replacement of the large public-facing files.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1364/OL.446079"
KEY = "liFirstPhotonStamping2022"
TITLE = "Fast non-line-of-sight imaging based on first photon event stamping"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def ensure_absent(text: str, needle: str, label: str) -> None:
    if needle.lower() in text.lower():
        raise RuntimeError(f"{label} already contains {needle!r}; refusing duplicate insertion")


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    ensure_absent(text, DOI, path)
    row = (
        "| 2022 | [Fast non-line-of-sight imaging based on first photon event stamping]"
        "(https://doi.org/10.1364/OL.446079) — Li et al. | Optics Letters 2022 | "
        "Introduces time-sequential first-photon (TSFP) acquisition for active transient NLOS, "
        "modeling the detection process rather than changing the downstream inverse operator. "
        "Synthetic and measured experiments retain comparable reconstruction quality with "
        "substantially shorter acquisition, making the method relevant to photon-starved and "
        "real-time systems. |\n"
    )
    header = "|------|-------|----------------|----------------|\n"
    text = replace_once(text, header, header + row, "README latest-additions table")
    milestone = (
        "2022 ── Grau et al.: Occlusion Fields — implicit recoverability and self-occlusion-aware hidden meshes [arXiv]\n"
    )
    addition = (
        milestone
        + "   │     Li et al.: time-sequential first-photon stamping — detection-aware acquisition reduces photon collection time for active transient NLOS [Optics Letters]\n"
    )
    text = replace_once(text, milestone, addition, "README 2022 milestone")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    ensure_absent(text, DOI, path)
    text = replace_once(
        text,
        '<div class="stat"><b>181</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>182</b><span>tracked latest entries</span></div>',
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
    text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper array")
    old_2022 = (
        "differentiable transient rendering and Occlusion Fields broadened inverse-rendering and implicit-surface recovery.</p>"
    )
    new_2022 = (
        "differentiable transient rendering and Occlusion Fields broadened inverse-rendering and implicit-surface recovery. "
        "Time-sequential first-photon stamping additionally moved acquisition design into the detector model, reducing the photon-collection burden without replacing established LCT, f-k, or phasor-field reconstruction back ends.</p>"
    )
    text = replace_once(text, old_2022, new_2022, "homepage 2022 timeline")
    write(path, text)


def update_active_survey() -> None:
    path = "article/2active.tex"
    text = read(path)
    ensure_absent(text, KEY, path)
    text = replace_once(
        text,
        "marcoVirtualLightTransport2021}",
        "marcoVirtualLightTransport2021,liFirstPhotonStamping2022}",
        "active SPAD reconstruction table citation",
    )
    anchor = (
        "Moreover, SPAD has been widely used in commercial LiDAR systems, and the SPAD array, which can avoid the mechanical raster scan process, has the potential to save scanning time and realize real-time data collection for active NLOS imaging. \n"
    )
    paragraph = (
        anchor
        + "\n\\vspace{0.8mm}\n"
        + "\\noindent \\textbf{Time-sequential first-photon acquisition.}\n"
        + "Most transient NLOS work optimizes the forward model or inverse solver after accumulating a photon-arrival histogram. Li~\\etal~instead examined the detector process and represented each measurement by time-sequential first-photon events~\\cite{liFirstPhotonStamping2022}. Their TSFP likelihood uses the earliest detection in successive laser periods and was validated on synthetic and measured hidden scenes, obtaining reconstruction quality comparable to conventional histogram acquisition with substantially less collection time. This detection-aware branch is complementary to LCT, $f$-$k$ migration, and phasor-field propagation: it reduces the photon and acquisition budget before those inverse operators are applied, and therefore provides an early link between single-photon statistics, photon-starved operation, and later real-time NLOS systems.\n"
    )
    text = replace_once(text, anchor, paragraph, "SPAD hardware discussion")
    write(path, text)


def update_master_tex() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    marker = "% 22 July 2026 citation trace: time-sequential first-photon NLOS acquisition integrated.\n"
    ensure_absent(text, marker.strip(), path)
    text = replace_once(text, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "master survey header")
    write(path, text)


def main() -> None:
    update_readme()
    update_index()
    update_active_survey()
    update_master_tex()
    print(f"Integrated {TITLE} ({DOI}) across public and survey sources.")


if __name__ == "__main__":
    main()
