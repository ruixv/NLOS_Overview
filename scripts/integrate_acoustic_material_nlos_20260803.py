#!/usr/bin/env python3
"""Boundedly integrate one verified acoustic NLOS material-sensing paper.

Every edit is guarded by an exact single-match assertion so that a changed
repository layout fails closed instead of truncating or broadly rewriting a
public artifact.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion"
KEY = "alakusAcousticMaterialNLOS2026"
DOI = "10.3390/s26051577"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected one anchor, found {count}: {old[:100]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def require_absent(path: Path, needle: str) -> None:
    if needle in path.read_text(encoding="utf-8"):
        raise RuntimeError(f"{path.relative_to(ROOT)} already contains {needle!r}")


readme = ROOT / "README.md"
index = ROOT / "index.html"
section = ROOT / "article/5newscenes.tex"
tex = ROOT / "bare_jrnl.tex"
bib_source = ROOT / "egbib_20260803_acoustic_material.bib"
note = ROOT / "updates/2026-08-03-acoustic-material-nlos.md"

for path in (readme, index, section, tex):
    require_absent(path, TITLE)
require_absent(section, KEY)

# README: update stamp, Latest Additions, and the development timeline.
replace_once(readme, "**Update run: 1 August 2026.**", "**Update run: 3 August 2026.**")
readme_row = (
    "| 2026 | [Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion]"
    "(https://doi.org/10.3390/s26051577) — Alakuş and Türkoğlu | Sensors 26(5), 1577 (2026) | "
    "Uses chirp echoes reaching nine hidden materials only through wall-mediated acoustic paths. A 70-dimensional fusion of "
    "classical acoustic and multi-scale wavelet features, classified by recurrent networks, reaches 0.99 balanced accuracy and "
    "macro-F1; SHAP links predictions to interpretable material properties. This is semantic acoustic NLOS sensing rather than "
    "hidden geometry reconstruction. |\n"
)
readme_table_anchor = "|------|-------|----------------|----------------|\n"
replace_once(readme, readme_table_anchor, readme_table_anchor + readme_row)
readme_timeline_anchor = (
    "   │     Wang et al.: scene-aware audio–visual fusion conditions acoustic spectra on BEV geometry for semantic detection "
    "of fully occluded vehicles [IEEE ICASSP]\n"
)
readme_timeline_line = (
    "   │     Alakuş and Türkoğlu: wall-mediated chirp echoes and wavelet–acoustic feature fusion enable interpretable "
    "nine-class hidden-material recognition [Sensors]\n"
)
replace_once(readme, readme_timeline_anchor, readme_timeline_anchor + readme_timeline_line)

# Website: update freshness labels, add one explorer record, extend 2026 trajectory,
# and derive the displayed count from the actual object list after insertion.
replace_once(index, "Updated 1 August 2026 · 210+ papers", "Updated 3 August 2026 · 210+ papers")
replace_once(index, "Last updated: 1 August 2026", "Last updated: 3 August 2026")
replace_once(index, "June–July 2026 update cycle", "June–August 2026 update cycle")
paper_object = (
    '      {cat:"latest modality acoustic semantic recognition material wavelet dataset",'
    'title:"Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion",'
    'authors:"Alakuş and Türkoğlu",year:2026,venue:"Sensors 26(5), 1577",'
    'url:"https://doi.org/10.3390/s26051577",'
    'key:"Wall-mediated chirp echoes from nine hidden materials form ANLOS-R; classical acoustic and multi-scale wavelet features '
    'feed recurrent classifiers reaching 0.99 balanced accuracy and macro-F1, while SHAP relates decisions to material acoustics. '
    'Semantic acoustic NLOS sensing rather than geometry reconstruction."},\n'
)
replace_once(index, "    const papers=[\n", "    const papers=[\n" + paper_object)
html_timeline_anchor = (
    "Scene-aware audio-visual acoustic fusion further extends this trajectory to semantic detection of fully occluded vehicles "
    "by conditioning acoustic spectra on BEV scene geometry.</p>"
)
html_timeline_addition = (
    " Alakuş and Türkoğlu further use wall-mediated chirp echoes, wavelet–acoustic feature fusion, and explainable recurrent "
    "learning to identify nine hidden material classes, extending acoustic NLOS semantics from people and vehicles to physical "
    "surface properties.</p>"
)
replace_once(index, html_timeline_anchor, html_timeline_anchor[:-4] + html_timeline_addition)
html = index.read_text(encoding="utf-8")
actual_count = html.count("{cat:")
count_pattern = re.compile(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>')
matches = count_pattern.findall(html)
if len(matches) != 1:
    raise RuntimeError(f"index.html: expected one tracked-entry counter, found {len(matches)}")
html = count_pattern.sub(
    f'<div class="stat"><b>{actual_count}</b><span>tracked latest entries</span></div>', html, count=1
)
index.write_text(html, encoding="utf-8")

# Survey prose: place the work inside Acoustic NLOS Imaging, after the existing
# semantic audio-visual paragraph and before the robotics subsection.
article_anchor = (
    "At the task level, Wang~\\etal~combine bird's-eye-view scene geometry with time--frequency and spatiotemporal acoustic "
    "spectra for detecting vehicles that are fully occluded from the camera~\\cite{wangAudioVisualNLOS2026}. Their scene-aware "
    "network uses CNN, LSTM, and Conformer modules to model local spectral structure, temporal evolution, and long-range "
    "cross-modal context, reporting 94.1\\% and 97.0\\% accuracy on the OVAD and AOVD datasets, respectively. Unlike acoustic "
    "echo tomography or diffraction-based source localization, this work does not reconstruct hidden geometry; it establishes "
    "a complementary semantic branch in which visible environment layout conditions the interpretation of sound propagated "
    "from an unseen traffic participant.\n"
)
article_paragraph = r'''
\vspace{0.8mm}
\noindent \textbf{Material recognition from wall-mediated acoustic echoes.}
Alaku{\c{s}} and T{\"u}rko{\u{g}}lu extend this semantic branch from hidden-agent inference to physical material recognition~\cite{alakusAcousticMaterialNLOS2026}. Their ANLOS-R acquisition places eight loudspeakers and eight microphones toward a relay wall while blocking the direct path to nine target materials, so the classifier operates on indirect chirp echoes shaped by reflection, absorption, and scattering. Classical spectral and temporal descriptors are fused with multi-scale wavelet energy and entropy into a 70-dimensional representation; recurrent models reach a reported balanced accuracy and macro-F1 of 0.99, and SHAP analysis relates the decision features to properties such as hardness, density, and porosity. Although the output is a material label rather than an image or 3D surface, the experiment demonstrates that NLOS transport can encode interpretable hidden-surface attributes and broadens acoustic NLOS from localization and action recognition toward material-aware environmental perception.
'''
replace_once(section, article_anchor, article_anchor + article_paragraph)

# bare_jrnl.tex is the survey entry point; record the synchronized integration
# while substantive prose remains in its semantically included section file.
replace_once(
    tex,
    "%% bare_jrnl.tex\n",
    "%% bare_jrnl.tex\n% 3 August 2026 modality trace: wall-mediated acoustic material recognition integrated across public artifacts.\n",
)

bib_source.write_text(r'''@article{alakusAcousticMaterialNLOS2026,
  author  = {Alaku{\c{s}}, Dilan Onat and T{\"u}rko{\u{g}}lu, {\.{I}}brahim},
  title   = {Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion},
  journal = {Sensors},
  year    = {2026},
  volume  = {26},
  number  = {5},
  pages   = {1577},
  doi     = {10.3390/s26051577},
  url     = {https://doi.org/10.3390/s26051577}
}
''', encoding="utf-8")

note.parent.mkdir(parents=True, exist_ok=True)
note.write_text(f'''# 3 August 2026 acoustic-material NLOS update

## Verified addition

**{TITLE}** — Dilan Onat Alakuş and İbrahim Türkoğlu, *Sensors* 26(5), article 1577 (3 March 2026). DOI: `{DOI}`.

The experiment blocks the direct path between an eight-speaker/eight-microphone array and nine target materials, leaving wall-mediated chirp echoes as the sensing signal. The paper introduces the ANLOS-R dataset, fuses classical acoustic descriptors with multi-scale wavelet energy/entropy features, compares recurrent classifiers, and reports 0.99 balanced accuracy and macro-F1 for CNN–LSTM. SHAP analysis connects the learned decisions to physically interpretable material characteristics.

This record is included as **semantic acoustic NLOS sensing**, not as hidden-image or geometry reconstruction. It is relevant to the repository's expanding task-oriented branch alongside hidden-human orientation, acoustic vehicle localization/detection, and radar target/activity recognition.

## Artifact placement

- `README.md`: Latest Additions plus the 2026 milestone timeline.
- `index.html`: searchable paper explorer, 2026 development narrative, update stamp, and derived explorer count.
- `article/5newscenes.tex`: Acoustic NLOS Imaging subsection, after scene-aware audio–visual detection.
- `bare_jrnl.tex`: synchronized entry-point update marker; the prose is included through the section source.
- `egbib_20260803_acoustic_material.bib`: canonical DOI-verified BibTeX source.
- `egbib_merged_20260711.bib`: regenerated by `scripts/merge_nlos_bibliography.py`.
- `bare_jrnl.pdf`: rebuilt after a clean LaTeX/BibTeX pass.

## Scope and citation-tracing decision

The work was verified from the publisher, PubMed/PMC, and DOI metadata. It is genuinely NLOS because the direct acoustic path to the target materials is physically blocked and only indirect wall-mediated echoes are recorded. A related IEEE TIM paper on LOS/NLOS-condition classification for indoor localization was reviewed but not added: it identifies propagation conditions to correct localization rather than sensing a hidden object, scene, or material, and is therefore outside the tighter imaging/sensing scope used here.
''', encoding="utf-8")

print(f"Integrated {TITLE}; website explorer now contains {actual_count} records.")
