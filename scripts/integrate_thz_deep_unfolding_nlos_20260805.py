#!/usr/bin/env python3
"""Boundedly integrate one verified THz radar NLOS reconstruction paper."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging"
KEY = "chenDeepUnfoldingTHzNLOS2026"
DOI = "10.3390/photonics13050440"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected one anchor, found {count}: {old[:120]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def require_absent(path: Path, needle: str) -> None:
    if needle in path.read_text(encoding="utf-8"):
        raise RuntimeError(f"{path.relative_to(ROOT)} already contains {needle!r}")


readme = ROOT / "README.md"
index = ROOT / "index.html"
section = ROOT / "article/5newscenes.tex"
tex = ROOT / "bare_jrnl.tex"
bib_source = ROOT / "egbib_20260805_thz_deep_unfolding.bib"
note = ROOT / "updates/2026-08-05-thz-deep-unfolding-nlos.md"

for path in (readme, index, section, tex):
    require_absent(path, DOI)
require_absent(section, KEY)

# README: freshness stamp, Latest Additions, and 2026 trajectory.
replace_once(readme, "**Update run: 3 August 2026.**", "**Update run: 5 August 2026.**")
readme_row = (
    "| 2026 | [Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging]"
    "(https://doi.org/10.3390/photonics13050440) — Chen et al. | Photonics 13(5), 440 (2026) | "
    "Builds a measured 121 GHz sub-THz around-corner imaging platform and unfolds a FISTA sparse solver around a fast "
    "holographic forward/adjoint operator. The model-driven network suppresses phase-error, aperture-shadowing, and multipath "
    "artifacts while reconstructing hidden 3D metal targets with roughly two orders of magnitude faster inference than iterative baselines. |\n"
)
readme_table_anchor = "|------|-------|----------------|----------------|\n"
replace_once(readme, readme_table_anchor, readme_table_anchor + readme_row)
readme_text = readme.read_text(encoding="utf-8")
match = re.search(r"(?m)^2026 ──", readme_text)
if not match:
    raise RuntimeError("README.md: 2026 timeline anchor not found")
readme_line = (
    "2026 ── Chen et al.: measured 121 GHz holographic imaging and FISTA deep unfolding enable efficient around-corner "
    "THz radar 3D reconstruction [Photonics]\n"
)
readme.write_text(readme_text[:match.start()] + readme_line + readme_text[match.start():], encoding="utf-8")

# Website: freshness labels, explorer record, derived count, and 2026 timeline.
replace_once(index, "Updated 3 August 2026 · 210+ papers", "Updated 5 August 2026 · 210+ papers")
replace_once(index, "Last updated: 3 August 2026", "Last updated: 5 August 2026")
paper_object = (
    '      {cat:"latest modality radar rf thz active learning reconstruction deep-unfolding measured",'
    'title:"Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging",'
    'authors:"Chen et al.",year:2026,venue:"Photonics 13(5), 440",'
    'url:"https://doi.org/10.3390/photonics13050440",'
    'key:"A measured 121 GHz sub-THz platform combines a fast holographic forward/adjoint operator with FISTA-Net deep unfolding, '
    'reconstructing hidden 3D metal targets while reducing artifacts and accelerating sparse inversion by roughly two orders of magnitude."},\n'
)
replace_once(index, "    const papers=[\n", "    const papers=[\n" + paper_object)
html = index.read_text(encoding="utf-8")
pattern = re.compile(
    r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
    re.DOTALL,
)
match = pattern.search(html)
if not match:
    raise RuntimeError("index.html: 2026 timeline block not found")
sentence = (
    " Chen et al. additionally combined a measured 121 GHz around-corner radar with a fast holographic operator and FISTA "
    "deep unfolding, extending THz NLOS from mirror-folding reconstruction toward model-driven learned 3D inversion under "
    "phase errors, aperture shadowing, and multipath."
)
html = html[:match.start(2)] + match.group(2) + sentence + html[match.end(2):]
actual_count = html.count("{cat:")
count_pattern = re.compile(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>')
if len(count_pattern.findall(html)) != 1:
    raise RuntimeError("index.html: tracked-entry counter is not unique")
html = count_pattern.sub(
    f'<div class="stat"><b>{actual_count}</b><span>tracked latest entries</span></div>', html, count=1
)
index.write_text(html, encoding="utf-8")

# Survey prose: extend the dedicated Terahertz NLOS Imaging subsection.
article_anchor = (
    "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{NLOS Human Pose Estimation}\n"
    "\\subsection{NLOS Human Pose Estimation}\n"
)
article_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Model-driven learned THz reconstruction.}
Chen~\etal~extend this modality from geometric mirror folding to learned sparse 3D inversion with a measured 121~GHz platform~\cite{chenDeepUnfoldingTHzNLOS2026}. Their formulation represents near-field around-corner transport with efficient holographic forward and adjoint operators, then unfolds FISTA into a fixed-depth network whose step, threshold, and momentum parameters are learned from simulated NLOS echoes. Measurements of hidden metal letters, a resolution chart, and scissors show that the physics-guided network suppresses phase-error, aperture-shadowing, and multipath artifacts while avoiding the memory cost of an explicit large sensing matrix. This work marks a transition in the THz branch from direct geometric relocation toward interpretable model-driven learning, while retaining coherent measured-data validation.

'''
replace_once(section, article_anchor, article_paragraph + article_anchor)

replace_once(
    tex,
    "%% bare_jrnl.tex\n",
    "%% bare_jrnl.tex\n% 5 August 2026 modality/citation trace: measured THz radar deep unfolding integrated across public artifacts.\n",
)

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
note.write_text(f'''# 5 August 2026 THz deep-unfolding NLOS update

## Verified addition

**{TITLE}** — Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, and Xiaolin Mi; *Photonics* 13(5), 440 (2026). DOI: `{DOI}`.

The publisher record gives publication on 30 April 2026. The paper builds a measured 121 GHz near-field around-corner radar platform and embeds fast holographic forward/adjoint operators in a FISTA-derived deep-unfolding network. Experiments reconstruct hidden metal letters, a resolution chart, and scissors while addressing phase errors, aperture shadowing, and multipath artifacts.

## Scope and citation-tracing decision

This is genuine NLOS imaging rather than propagation-condition classification: coherent wall-reflected radar echoes are inverted into hidden three-dimensional scattering geometry. It extends the THz lineage from geometric mirror folding to physics-guided learned reconstruction and connects directly to the repository's radar/RF, model-driven learning, and sparse-inversion milestones. Exact-title, DOI, author/title-fragment, THz, and deep-unfolding searches found no existing repository record before insertion.

## Artifact placement

- `README.md`: Latest Additions and the 2026 milestone timeline.
- `index.html`: searchable explorer/latest feed, 2026 development narrative, update stamp, and derived explorer count.
- `article/5newscenes.tex`: Terahertz NLOS Imaging subsection.
- `bare_jrnl.tex`: synchronized entry-point update marker.
- `egbib_20260805_thz_deep_unfolding.bib`: canonical publisher-verified BibTeX source.
- `egbib_merged_20260711.bib`: regenerated by `scripts/merge_nlos_bibliography.py`.
- `bare_jrnl.pdf`: rebuilt after a clean LaTeX/BibTeX pass.
''', encoding="utf-8")

print(f"Integrated {TITLE}; website explorer now contains {actual_count} records.")
