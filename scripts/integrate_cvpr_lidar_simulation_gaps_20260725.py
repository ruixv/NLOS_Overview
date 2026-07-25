#!/usr/bin/env python3
"""Synchronize three citation-traced cross-artifact NLOS gaps.

The bibliography and parts of the survey already contain these records. This
script adds only missing public-facing records, inserts the missing GeRaF 2.0
survey discussion, preserves stable BibTeX keys, and fails closed on ambiguous
anchors or duplicate titles.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
DATA = ROOT / "article" / "4datadriven.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-25-cvpr-radar-lidar-simulation-gaps.md"
TRACE = "% 25 July 2026 cross-artifact trace: GeRaF 2.0 radar reconstruction, DENALI low-cost LiDAR data, and open transient simulation benchmark synchronized."

PAPERS = [
    dict(
        title="Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals",
        authors="Lu, Shanbhag, Al Hassanieh", year=2026, venue="CVPR 2026",
        url="https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_Radar_Signals_CVPR_2026_paper.html",
        key="luSeeingThroughBoxes2026",
        cats="latest modality radar rf learning neural-field sdf reconstruction cvpr",
        summary="Introduces GeRaF 2.0, a unified LOS/NLOS neural geometry model that uses visually observed exterior geometry to constrain RF propagation into enclosed hidden regions, stabilizing SDF optimization and jointly recovering visible and concealed surfaces."
    ),
    dict(
        title="DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs",
        authors="Behari et al.", year=2026, venue="CVPR 2026 (Highlight)",
        url="https://openaccess.thecvf.com/CVPR2026?day=2026-06-05",
        key="behariDENALI2026",
        cats="latest dataset modality lidar consumer-lidar spatial-reasoning cvpr",
        summary="Releases 72,000 real time-resolved low-cost-LiDAR histograms with paired RGB and digital twins across 60 hidden-object configurations, 100 sensor positions, two lighting conditions, and two LiDAR resolutions for localization, classification, and sim-to-real study."
    ),
    dict(
        title="Fast non-line-of-sight transient data simulation and an open benchmark dataset",
        authors="Shi et al.", year=2025, venue="Optics Express 2025",
        url="https://doi.org/10.1364/OE.575753",
        key="shiFastNLOSTransientSimulation2025",
        cats="latest dataset benchmark active transient simulation open-data",
        summary="Uses a fully parameterized light-intensity transport simulator rather than conventional path tracing to generate transient NLOS data efficiently, exposing relay geometry, stand-off distance, timing resolution, acquisition window, jitter, and noise for reproducible algorithm and system evaluation."
    ),
]


def read(path):
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write(path, text):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


readme = read(README)
index = read(INDEX)
newscenes = read(NEWSCENES)
data = read(DATA)
survey = read(SURVEY)
bib = read(BIB)

# Verify canonical bibliography records already present and unique.
for p in PAPERS:
    count = len(re.findall(r"(?mi)^@\w+\{" + re.escape(p["key"]) + r",", bib))
    if count != 1:
        raise SystemExit(f"BibTeX key {p['key']} occurs {count} times")

# README latest-additions table.
header = "|------|-------|----------------|----------------|\n"
if readme.count(header) != 1:
    raise SystemExit("README Latest Additions header is ambiguous")
rows = []
for p in PAPERS:
    count = readme.lower().count(p["title"].lower())
    if count == 0:
        rows.append(f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["summary"]} |')
    elif count != 1:
        raise SystemExit(f"README title is not unique: {p['title']}")
if rows:
    readme = readme.replace(header, header + "\n".join(rows) + "\n", 1)

# Website searchable explorer.
array_anchor = "    const papers=[\n" if "    const papers=[\n" in index else "    const papers = [\n"
if index.count(array_anchor) != 1:
    raise SystemExit("Website paper-array anchor is ambiguous")
objects = []
inserted = 0
for p in PAPERS:
    count = index.lower().count(p["title"].lower())
    if count == 0:
        objects.append(
            f'      {{cat:"{p["cats"]}",title:"{p["title"]}",authors:"{p["authors"]}",year:{p["year"]},venue:"{p["venue"]}",url:"{p["url"]}",key:"{p["summary"]}"}},'
        )
        inserted += 1
    elif count != 1:
        raise SystemExit(f"Website title is not unique: {p['title']}")
if objects:
    index = index.replace(array_anchor, array_anchor + "\n".join(objects) + "\n", 1)

count_matches = re.findall(r'<b>(\d+)</b><span>tracked latest entries</span>', index)
if len(count_matches) != 1:
    raise SystemExit("Website tracked-entry count is ambiguous")
if inserted:
    new_count = int(count_matches[0]) + inserted
    index = re.sub(r'<b>\d+</b><span>tracked latest entries</span>', f'<b>{new_count}</b><span>tracked latest entries</span>', index, count=1)

# Timeline: avoid repeating the existing 2025 simulator milestone; add explicit
# CVPR 2026 radar and low-cost-LiDAR milestones only.
timeline_sentence = " GeRaF 2.0 used visually observed exterior geometry to constrain penetrative RF neural fields inside enclosed regions, while DENALI supplied 72,000 real low-cost-LiDAR histograms and paired digital twins for NLOS spatial reasoning and sim-to-real evaluation."
pat = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body">.*?<p>)(.*?)(</p>)', re.S)
m = pat.search(index)
if not m:
    raise SystemExit("Website 2026 timeline anchor is missing")
if timeline_sentence.strip() not in m.group(2):
    index = index[:m.start()] + m.group(1) + m.group(2) + timeline_sentence + m.group(3) + index[m.end():]

# Survey: DENALI and the transient simulator are already integrated. GeRaF 2.0
# is missing from the radar narrative and is inserted before adjacent RF work.
geraf_heading = "Visually constrained penetrative RF neural reconstruction."
if geraf_heading not in newscenes:
    anchor = "Recent RF/mmWave work further expands the meaning of NLOS perception beyond monostatic reconstruction."
    if newscenes.count(anchor) != 1:
        raise SystemExit("Radar-survey insertion anchor is ambiguous")
    paragraph = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{" + geraf_heading + "}\n"
        "Lu~\\etal~introduced GeRaF~2.0 for joint line-of-sight and non-line-of-sight geometry reconstruction from penetrative radar measurements~\\cite{luSeeingThroughBoxes2026}. Rather than optimizing the hidden signed-distance field in isolation, the method uses visually observed exterior geometry to constrain RF propagation from the visible region into an enclosed hidden volume. These line-of-sight priors stabilize the zero-level set, reduce surface ambiguity, and permit physically consistent recovery of both visible and concealed geometry. This direction complements mirror-path mmWave systems such as HoloRadar: instead of relying only on environmental specular relays, it combines penetrative RF transport with cross-modal geometric evidence to regularize a neural implicit scene representation.\n\n"
    )
    newscenes = newscenes.replace(anchor, paragraph + anchor, 1)

# Existing semantic placements must remain present.
if "\\cite{behariDENALI2026}" not in newscenes:
    raise SystemExit("DENALI is not integrated in article/5newscenes.tex")
if "\\cite{shiFastNLOSTransientSimulation2025}" not in data:
    raise SystemExit("Transient simulation benchmark is not integrated in article/4datadriven.tex")

# Trace the consistency pass in the survey master without changing structure.
if TRACE not in survey:
    anchor = "%% bare_jrnl.tex\n"
    if survey.count(anchor) != 1:
        raise SystemExit("Survey trace anchor is ambiguous")
    survey = survey.replace(anchor, anchor + TRACE + "\n", 1)

# End-to-end uniqueness checks.
for text, label in ((readme, "README"), (index, "index.html")):
    for p in PAPERS:
        if text.lower().count(p["title"].lower()) != 1:
            raise SystemExit(f"{label}: title not unique after update: {p['title']}")
if "\\cite{luSeeingThroughBoxes2026}" not in newscenes:
    raise SystemExit("GeRaF 2.0 citation insertion failed")

note = """# CVPR radar/LiDAR and transient-simulation consistency pass — 25 July 2026

Citation tracing and repository-wide comparison found three records that already had canonical bibliography support but were not consistently exposed across public artifacts:

1. **Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals** — CVPR 2026 (GeRaF 2.0). Added to README, website explorer/timeline, and the radar survey narrative.
2. **DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs** — CVPR 2026 Highlight. It was already discussed and cited in the low-cost-LiDAR survey subsection; added to README and website explorer/timeline.
3. **Fast non-line-of-sight transient data simulation and an open benchmark dataset** — Optics Express 2025, DOI 10.1364/OE.575753. It was already integrated in the dataset discussion and bibliography; added to README and website explorer.

The update preserves the existing BibTeX keys, adds no duplicate bibliography entries, and requires a clean LaTeX/BibTeX rebuild before the PDF is committed.
"""

for path, text in ((README, readme), (INDEX, index), (NEWSCENES, newscenes), (SURVEY, survey), (NOTE, note)):
    write(path, text)
print(f"Synchronized {inserted} missing website records and three README records.")
