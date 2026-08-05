#!/usr/bin/env python3
"""Synchronize one verified THz radar NLOS paper across the survey artifacts.

The README and website already contain the publisher-verified paper record.
This bounded update fills the remaining survey/bibliography/PDF gap without
creating duplicate public records.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging"
KEY = "chenDeepUnfoldingTHzNLOS2026"
DOI = "10.3390/photonics13050440"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_optional_once(path: Path, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count > 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: non-unique anchor {old!r}")
    if count == 1:
        write(path, text.replace(old, new, 1))


def require_count(path: Path, needle: str, expected: int) -> None:
    count = read(path).count(needle)
    if count != expected:
        raise RuntimeError(
            f"{path.relative_to(ROOT)}: expected {expected} occurrences of {needle!r}, found {count}"
        )


readme = ROOT / "README.md"
index = ROOT / "index.html"
section = ROOT / "article/5newscenes.tex"
tex = ROOT / "bare_jrnl.tex"
bib_source = ROOT / "egbib_20260805_thz_deep_unfolding.bib"
note = ROOT / "updates/2026-08-05-thz-deep-unfolding-nlos.md"

# The paper is already public in README and the website explorer/timeline.
# Guard against duplicate insertion and only refresh the run labels.
require_count(readme, TITLE, 1)
require_count(readme, DOI, 1)
require_count(index, TITLE, 1)
require_count(index, DOI, 1)
if "121 GHz holographic operators" not in read(readme):
    raise RuntimeError("README.md: verified THz milestone sentence is missing")
if "Range-migration and 121 GHz holographic operators" not in read(index):
    raise RuntimeError("index.html: verified THz timeline sentence is missing")
replace_optional_once(readme, "**Update run: 3 August 2026.**", "**Update run: 5 August 2026.**")
replace_optional_once(index, "Updated 3 August 2026 · 210+ papers", "Updated 5 August 2026 · 210+ papers")
replace_optional_once(index, "Last updated: 3 August 2026", "Last updated: 5 August 2026")

# Survey prose: extend the dedicated Terahertz NLOS Imaging subsection once.
article_anchor = (
    "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{NLOS Human Pose Estimation}\n"
    "\\subsection{NLOS Human Pose Estimation}\n"
)
article_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Model-driven learned THz reconstruction.}
Chen~\etal~extend this modality from geometric mirror folding to learned sparse 3D inversion with a measured 121~GHz platform~\cite{chenDeepUnfoldingTHzNLOS2026}. Their formulation represents near-field around-corner transport with efficient holographic forward and adjoint operators, then unfolds FISTA into a fixed-depth network whose step, threshold, and momentum parameters are learned from simulated NLOS echoes. Measurements of hidden metal letters, a resolution chart, and scissors show that the physics-guided network suppresses phase-error, aperture-shadowing, and multipath artifacts while avoiding the memory cost of an explicit large sensing matrix. This work marks a transition in the THz branch from direct geometric relocation toward interpretable model-driven learning, while retaining coherent measured-data validation.

'''
section_text = read(section)
if KEY not in section_text:
    if section_text.count(article_anchor) != 1:
        raise RuntimeError("article/5newscenes.tex: NLOS human-pose anchor is not unique")
    write(section, section_text.replace(article_anchor, article_paragraph + article_anchor, 1))
require_count(section, KEY, 1)

marker = "% 5 August 2026 modality/citation trace: measured THz radar deep unfolding integrated across public artifacts.\n"
tex_text = read(tex)
if marker not in tex_text:
    if tex_text.count("%% bare_jrnl.tex\n") != 1:
        raise RuntimeError("bare_jrnl.tex: header anchor is not unique")
    write(tex, tex_text.replace("%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, 1))
require_count(tex, marker, 1)

bib_source.write_text(r'''@article{chenDeepUnfoldingTHzNLOS2026,
  author  = {Chen, Kun and Wei, Shunjun and Wang, Mou and Chen, Juran and Han, Bingyu and Li, Jin and Liu, Zhe and Zhang, Xiaoling and Liao, Yi and Gao, Pengcheng and Mi, Xiaolin},
  title   = {Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging},
  journal = {Photonics},
  year    = {2026},
  volume  = {13},
  number  = {5},
  pages   = {440},
  doi     = {10.3390/photonics13050440},
  url     = {https://doi.org/10.3390/photonics13050440}
}
''', encoding="utf-8")

note.parent.mkdir(parents=True, exist_ok=True)
note.write_text(f'''# 5 August 2026 THz deep-unfolding NLOS consistency update

## Verified paper

**{TITLE}** — Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, and Xiaolin Mi; *Photonics* 13(5), 440 (2026). DOI: `{DOI}`.

The publisher record reports publication on 30 April 2026. The study builds a measured 121 GHz near-field around-corner radar platform and embeds fast holographic forward/adjoint operators in a FISTA-derived deep-unfolding network. Experiments reconstruct hidden metal letters, a resolution chart, and scissors while addressing phase errors, aperture shadowing, and multipath artifacts.

## Scope and citation-lineage decision

This is genuine NLOS imaging rather than propagation-condition classification: coherent wall-reflected radar echoes are inverted into hidden three-dimensional scattering geometry. It extends the repository's THz lineage from geometric mirror folding to physics-guided learned reconstruction and connects the radar/RF, sparse-inversion, and model-driven-learning branches.

## Consistency gap fixed in this run

The paper and its 2026 trajectory were already present once in `README.md` and `index.html`, including the website's `latest` category, but the paper was absent from the LaTeX survey and bibliography. This update therefore preserves the existing public records, refreshes the run stamps, inserts a literature-review paragraph in the Terahertz NLOS Imaging subsection, adds publisher-verified BibTeX, regenerates the merged bibliography, and rebuilds `bare_jrnl.pdf`.

## Synchronized artifacts

- `README.md`: existing unique paper record and THz timeline retained; update-run stamp refreshed.
- `index.html`: existing unique explorer/latest record and 2026 timeline retained; freshness labels refreshed.
- `article/5newscenes.tex`: model-driven learned THz reconstruction paragraph added.
- `bare_jrnl.tex`: synchronization marker added.
- `egbib_20260805_thz_deep_unfolding.bib`: canonical publisher-verified entry added.
- `egbib_merged_20260711.bib`: regenerated by `scripts/merge_nlos_bibliography.py`.
- `bare_jrnl.pdf`: rebuilt after a clean LaTeX/BibTeX pass.
''', encoding="utf-8")

actual_count = read(index).count("{cat:")
print(f"Synchronized {TITLE}; website explorer remains at {actual_count} records.")
