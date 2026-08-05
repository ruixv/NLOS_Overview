#!/usr/bin/env python3
"""Synchronize one verified 228 GHz polarimetric radar NLOS paper.

The updater is deliberately bounded and idempotent.  It refuses ambiguous
anchors and never rewrites a large public artifact unless the expected current
structure is present.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System"
KEY = "alburadiPolarimetric228GHzNLOS2025"
DOI = "10.1109/TGRS.2025.3564230"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def require_absent(path: Path, needle: str) -> None:
    if needle in read(path):
        raise RuntimeError(f"{path.relative_to(ROOT)} already contains {needle!r}")


def replace_once(path: Path, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected one anchor {old!r}, found {count}")
    write(path, text.replace(old, new, 1))


readme = ROOT / "README.md"
index = ROOT / "index.html"
section = ROOT / "article/5newscenes.tex"
tex = ROOT / "bare_jrnl.tex"
bib_source = ROOT / "egbib_20260806_polarimetric_228ghz_nlos.bib"
note = ROOT / "updates/2026-08-06-polarimetric-228ghz-nlos.md"

for path in (readme, index, section, tex):
    require_absent(path, TITLE)
require_absent(section, KEY)

# README: add a publisher-verified row and a modality-timeline milestone.
readme_text = read(readme)
readme_text, n = re.subn(
    r"\*\*Update run: \d{1,2} [A-Za-z]+ 2026\.\*\*",
    "**Update run: 6 August 2026.**",
    readme_text,
    count=1,
)
if n != 1:
    raise RuntimeError("README.md: update-run label not found uniquely")
header = "|------|-------|----------------|----------------|\n"
if readme_text.count(header) != 1:
    raise RuntimeError("README.md: Latest Additions table header is not unique")
row = (
    "| 2025 | [Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System]"
    "(https://doi.org/10.1109/TGRS.2025.3564230) — Alburadi et al. | IEEE TGRS 63, 1–9 (2025) | "
    "Uses a mechanically scanned 222–228 GHz polarimetric FMCW radar with 0.3° azimuth resolution for corridor mapping and around-corner obstacle localization. "
    "Measured drywall reflection coefficients support polarization discrimination of NLOS returns from ghost targets, followed by a mirror transformation in an L-shaped corridor; this is measured sub-THz/RF hidden-target imaging and localization rather than generic NLOS channel classification. |\n"
)
readme_text = readme_text.replace(header, header + row, 1)
tl_anchor = "2025 ── Wei et al.: multi-surface waveform deposition"
if readme_text.count(tl_anchor) != 1:
    raise RuntimeError("README.md: 2025 timeline anchor is not unique")
tl_line = (
    "2025 ── Alburadi et al.: a 222–228 GHz polarimetric FMCW imager maps corridors and uses polarization discrimination plus mirror relocation to identify and localize around-corner obstacles [IEEE TGRS]\n"
)
readme_text = readme_text.replace(tl_anchor, tl_line + tl_anchor, 1)
write(readme, readme_text)

# Website: add a first-class searchable/latest record, a timeline item, and
# derive the displayed explorer count from the actual records.
html = read(index)
html, n = re.subn(
    r"Updated \d{1,2} [A-Za-z]+ 2026 · 210\+ papers",
    "Updated 6 August 2026 · 210+ papers",
    html,
    count=1,
)
if n != 1:
    raise RuntimeError("index.html: hero freshness label not found uniquely")
html, n = re.subn(
    r"Last updated: \d{1,2} [A-Za-z]+ 2026",
    "Last updated: 6 August 2026",
    html,
    count=1,
)
if n != 1:
    raise RuntimeError("index.html: footer freshness label not found uniquely")
papers_anchor = "    const papers=[\n"
if html.count(papers_anchor) != 1:
    raise RuntimeError("index.html: paper-array anchor is not unique")
record = (
    "      {cat:\"latest modality radar rf mmwave sub-thz polarimetric mapping localization measured\","
    "title:\"Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System\","
    "authors:\"Alburadi et al.\",year:2025,venue:\"IEEE TGRS 63, 1–9\","
    "url:\"https://doi.org/10.1109/TGRS.2025.3564230\","
    "key:\"A mechanically scanned 222–228 GHz polarimetric FMCW radar produces LiDAR-like corridor maps; measured drywall polarization response separates around-corner targets from ghost returns, and mirror relocation localizes obstacles in an L-shaped corridor.\"},\n"
)
html = html.replace(papers_anchor, papers_anchor + record, 1)
timeline_anchor = '      <div class="tl"><div class="year">2026</div>'
if html.count(timeline_anchor) < 1:
    raise RuntimeError("index.html: first 2026 timeline anchor is missing")
timeline_item = (
    '      <div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Polarimetric 228 GHz around-corner mapping</strong>'
    '<p>Alburadi et al. combine sub-THz FMCW corridor mapping, measured drywall polarization response, ghost-target discrimination, and mirror relocation for experimental NLOS obstacle detection and localization.</p></div></div>\n'
)
html = html.replace(timeline_anchor, timeline_item + timeline_anchor, 1)
actual = html.count("{cat:")
html, n = re.subn(
    r'<b>\d+</b><span>tracked latest entries</span>',
    f'<b>{actual}</b><span>tracked latest entries</span>',
    html,
    count=1,
)
if n != 1:
    raise RuntimeError("index.html: tracked-entry counter is not unique")
write(index, html)

# Survey narrative: place the work in the radar modality section, before the
# next subsection, and explicitly distinguish localization from full 3D shape.
section_text = read(section)
article_anchor = (
    "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Low-Cost LiDAR NLOS Spatial Reasoning}\n"
    "\\subsection{Low-Cost LiDAR NLOS Spatial Reasoning}\n"
)
if section_text.count(article_anchor) != 1:
    raise RuntimeError("article/5newscenes.tex: low-cost LiDAR anchor is not unique")
paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Polarimetric sub-terahertz corridor imaging.}
Alburadi~\etal~demonstrated measured indoor mapping and around-corner obstacle localization with a mechanically scanned 222--228~GHz polarimetric FMCW radar~\cite{alburadiPolarimetric228GHzNLOS2025}. A fan-beam reflector provides a $360^\circ$ field of view and approximately $0.3^\circ$ azimuthal resolution, while measured co-polarized reflection coefficients of painted drywall reveal a polarization signature that distinguishes wall-mediated NLOS targets from strong multipath ghosts. After this polarization discrimination, a mirror transformation relocates detections into the physical hidden corridor in an L-shaped experiment. The work expands radar NLOS from lower-frequency multipath imaging toward LiDAR-like sub-terahertz mapping and shows that polarization can serve as a physical path-validity cue; its output is obstacle detection and localization rather than complete hidden-surface reconstruction.

'''
write(section, section_text.replace(article_anchor, paragraph + article_anchor, 1))

# Main source marker makes cross-artifact integration auditable.
marker = "% 6 August 2026 modality trace: 228 GHz polarimetric radar NLOS mapping integrated across public artifacts.\n"
tex_text = read(tex)
if tex_text.count("%% bare_jrnl.tex\n") != 1:
    raise RuntimeError("bare_jrnl.tex: header anchor is not unique")
write(tex, tex_text.replace("%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, 1))

bib_source.write_text(r'''@article{alburadiPolarimetric228GHzNLOS2025,
  author  = {Alburadi, Abdullah and Muppala, Aditya Varma and Nashashibi, Adib Y. and Shaman, Hussein N. and Sarabandi, Kamal},
  title   = {Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-{GHz} {FMCW} Polarimetric Radar System},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  year    = {2025},
  volume  = {63},
  pages   = {1--9},
  doi     = {10.1109/TGRS.2025.3564230},
  url     = {https://doi.org/10.1109/TGRS.2025.3564230}
}
''', encoding="utf-8")

note.parent.mkdir(parents=True, exist_ok=True)
note.write_text(f'''# 6 August 2026 polarimetric 228 GHz radar NLOS update

## Verified paper

**{TITLE}** — Abdullah Alburadi, Aditya Varma Muppala, Adib Y. Nashashibi, Hussein N. Shaman, and Kamal Sarabandi; *IEEE Transactions on Geoscience and Remote Sensing* 63, 1–9 (2025). DOI: `{DOI}`.

The final IEEE journal record supersedes any early-access or secondary-index status. The measured system operates over 222–228 GHz, mechanically scans a fan-beam antenna over 360 degrees, and reports approximately 0.3-degree azimuthal resolution.

## Scope decision

This is genuine NLOS sensing/imaging rather than a paper that merely studies NLOS propagation. It forms two-dimensional radar maps, identifies wall-mediated hidden returns using measured polarization-dependent drywall reflection, rejects ghost targets, and relocates detections through a mirror transformation in an L-shaped corridor. The output is hidden-obstacle detection and localization, not complete 3D shape reconstruction, and the survey text states that boundary explicitly.

## Discovery and lineage

The record was recovered during the radar/sub-THz modality pass and independently verified through the DOI, IEEE metadata, DBLP, and author ORCID metadata. It is also cited by the newer cost-effective FMCW-interferometry NLOS literature, confirming that it has entered the published modality-expansion lineage.

## Synchronized artifacts

- `README.md`: Latest Additions row, final venue/DOI, contribution summary, and 2025 modality timeline.
- `index.html`: latest/searchable explorer record, 2025 development-timeline item, freshness labels, and derived explorer count.
- `article/5newscenes.tex`: semantically placed radar-modality literature-review paragraph.
- `bare_jrnl.tex`: auditable synchronization marker.
- `egbib_20260806_polarimetric_228ghz_nlos.bib`: canonical final-venue BibTeX.
- `egbib_merged_20260711.bib`: regenerated by the repository bibliography merger.
- `bare_jrnl.pdf`: rebuilt after clean LaTeX/BibTeX passes.
''', encoding="utf-8")

print(f"Integrated {TITLE}; website explorer now contains {actual} records.")
