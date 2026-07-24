#!/usr/bin/env python3
"""Integrate the citation-traced PEC-NLOS paper across repository artifacts.

Every edit is fail-closed and idempotent. Large public files are changed only through
unique semantic anchors, and the bibliography rejects duplicate citation keys or DOIs.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
SURVEY = ROOT / "bare_jrnl.tex"
ACTIVE = ROOT / "article/2active.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

KEY = "liuPtychographyCorrelography2026"
DOI = "10.1117/1.APN.5.2.026001"

README_ROW = (
    "| 2026 | [Ptychography-enhanced correlography for non-line-of-sight imaging]"
    "(https://doi.org/10.1117/1.APN.5.2.026001) — Liu et al. | Advanced Photonics Nexus 2026 | "
    "Introduces PEC-NLOS, which scans overlapping indirect speckle probes across the relay wall "
    "and applies ptychographic phase retrieval to jointly refine the hidden object and probe. "
    "A geometry-based 3D data-correction stage compensates scan-position and probe distortion, "
    "extending steady-state correlography from simple targets to high-spatial-frequency, high-entropy hidden scenes. |"
)

README_TIMELINE = (
    "   │     Liu et al.: ptychography-enhanced correlography — overlapping indirect speckle probes "
    "and geometry-corrected ptychographic phase retrieval recover complex high-frequency steady-state hidden scenes "
    "[Advanced Photonics Nexus]"
)

INDEX_OBJECT = (
    '      {cat:"latest active steady-state correlography ptychography speckle",'
    'title:"Ptychography-enhanced correlography for non-line-of-sight imaging",'
    'authors:"Liu et al.",year:2026,venue:"Advanced Photonics Nexus 2026",'
    'url:"https://doi.org/10.1117/1.APN.5.2.026001",'
    'key:"PEC-NLOS scans overlapping indirect speckle probes and uses ptychographic phase retrieval '
    'to jointly refine the hidden object and illumination probe; geometry-based 3D data correction '
    'compensates scan and probe distortion, enabling complex high-frequency hidden-scene reconstruction."},'
)

INDEX_TIMELINE_SENTENCE = (
    " Ptychography-enhanced correlography then used overlapping speckle probes and geometry-corrected "
    "ptychographic phase retrieval to recover complex high-frequency steady-state hidden scenes, trading "
    "additional measurements for improved Fourier coverage and conditioning."
)

TABLE_ROW = (
    f"    \\cite{{{KEY}}} & Continuous laser & Polarization-sensitive camera & "
    "Speckle correlation / Fourier amplitude & 2D reconstruction\\\\%%%% Table body"
)

ARTICLE_PARAGRAPH = (
    "\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Ptychography-enhanced correlography.}\n"
    "Liu~\\etal~subsequently addressed the incomplete Fourier-amplitude sampling and phase ambiguity "
    "that limit conventional NLOS correlography by introducing PEC-NLOS~\\cite{liuPtychographyCorrelography2026}. "
    "A continuous-wave laser scans overlapping indirect speckle probes across the relay wall, while a "
    "polarization-sensitive camera records local correlation measurements; ptychographic phase retrieval "
    "jointly refines the hidden object and probe. A geometry-derived three-dimensional data-correction stage "
    "uses non-invasive positional priors to compensate probe and scan distortion. Unlike the scanning-free "
    "polarization methods above, PEC-NLOS deliberately trades additional overlapping measurements for redundancy "
    "and conditioning, extending steady-state correlography from simple sparse targets to high-spatial-frequency, "
    "high-entropy hidden scenes and establishing a bridge between NLOS speckle imaging and coherent-diffraction-style "
    "ptychographic reconstruction.\n"
)

BIB_ENTRY = """@article{liuPtychographyCorrelography2026,
  author = {Liu, Lingfeng and Zhu, Shuo and Qin, Taotao and Bai, Lianfa and Shi, Yingjie and Guo, Enlai and Han, Jing},
  doi = {10.1117/1.APN.5.2.026001},
  journal = {Advanced Photonics Nexus},
  month = {January},
  number = {2},
  pages = {026001},
  publisher = {SPIE and Chinese Laser Press},
  title = {Ptychography-Enhanced Correlography for Non-Line-of-Sight Imaging},
  url = {https://doi.org/10.1117/1.APN.5.2.026001},
  volume = {5},
  year = {2026}
}"""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def insert_after_unique_line(text: str, needle: str, addition: str, label: str) -> str:
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise SystemExit(f"{label}: expected one matching line, found {len(matches)}")
    lines.insert(matches[0] + 1, addition)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def normalize_bib_entry(text: str) -> str:
    pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(KEY)},\n.*?^\}}\s*\n?")
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        raise SystemExit(f"bibliography: duplicate key {KEY}")
    if matches:
        text = text[: matches[0].start()] + BIB_ENTRY.rstrip() + "\n\n" + text[matches[0].end() :]
    else:
        if DOI.lower() in text.lower():
            raise SystemExit(f"bibliography: DOI {DOI} exists under a different key")
        text = text.rstrip() + "\n\n" + BIB_ENTRY.rstrip() + "\n"
    if text.lower().count(DOI.lower()) != 2:
        raise SystemExit("bibliography: canonical DOI/URL count failed")
    return text


# README latest entry and milestone timeline.
readme = read(README)
if DOI.lower() not in readme.lower():
    readme = insert_after_unique_line(
        readme,
        "10.1038/s41467-026-75177-4",
        README_ROW,
        "README Latest Additions insertion",
    )
if "ptychography-enhanced correlography — overlapping indirect speckle probes" not in readme:
    readme = insert_after_unique_line(
        readme,
        "Sultan et al.: iterated transient light transport matrices",
        README_TIMELINE,
        "README 2026 timeline insertion",
    )
write(README, readme)

# Website paper explorer, count, and 2026 timeline.
index = read(INDEX)
if DOI.lower() not in index.lower():
    index = replace_once(index, "    const papers=[\n", "    const papers=[\n" + INDEX_OBJECT + "\n", "index paper insertion")
    count_pattern = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    match = count_pattern.search(index)
    if not match:
        raise SystemExit("index: tracked-entry counter not found")
    old_count = int(match.group(1))
    index = index[: match.start(1)] + str(old_count + 1) + index[match.end(1) :]
if "Ptychography-enhanced correlography then used overlapping speckle probes" not in index:
    timeline_pattern = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
    )
    timeline_match = timeline_pattern.search(index)
    if not timeline_match:
        raise SystemExit("index: 2026 timeline block not found")
    new_body = timeline_match.group(2).rstrip() + INDEX_TIMELINE_SENTENCE
    index = index[: timeline_match.start(2)] + new_body + index[timeline_match.end(2) :]
write(INDEX, index)

# Active-system table and semantically adjacent survey paragraph.
active = read(ACTIVE)
if TABLE_ROW not in active:
    active = insert_after_unique_line(
        active,
        "liuPolarizationDifferentialCorrelography2025} & Continuous laser & Conventional camera",
        TABLE_ROW,
        "active table insertion",
    )
if "\\noindent \\textbf{Ptychography-enhanced correlography.}" not in active:
    anchor = (
        "This work connects steady-state NLOS, speckle correlation, and polarization coding, providing a "
        "low-complexity high-resolution alternative to transient time-of-flight inversion.\n"
    )
    active = replace_once(active, anchor, anchor + "\n" + ARTICLE_PARAGRAPH, "active prose insertion")
write(ACTIVE, active)

# Master wrapper marker; the coverage date is already current.
survey = read(SURVEY)
marker = "% 24 July 2026 citation trace: ptychography-enhanced steady-state correlography integrated.\n"
if marker not in survey:
    survey = replace_once(survey, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "survey marker")
write(SURVEY, survey)

# Canonical bibliography normalization.
bib = normalize_bib_entry(read(BIB))
write(BIB, bib)

# Final cross-artifact assertions.
readme = read(README)
index = read(INDEX)
active = read(ACTIVE)
survey = read(SURVEY)
bib = read(BIB)
if readme.lower().count(DOI.lower()) != 1:
    raise SystemExit("README DOI count failed")
if index.lower().count(DOI.lower()) != 1:
    raise SystemExit("index DOI count failed")
if bib.lower().count(DOI.lower()) != 2:
    raise SystemExit("bibliography DOI/URL count failed")
if active.count(KEY) < 2:
    raise SystemExit("active survey must cite PEC-NLOS in the table and prose")
if marker not in survey:
    raise SystemExit("survey integration marker missing")
count_match = re.search(r'<b>(\d+)</b><span>tracked latest entries</span>', index)
if not count_match or int(count_match.group(1)) < 193:
    raise SystemExit("website tracked-entry count was not incremented")

print("Integrated ptychography-enhanced NLOS correlography across source artifacts.")
