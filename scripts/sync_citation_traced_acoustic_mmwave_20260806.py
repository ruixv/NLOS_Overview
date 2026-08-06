from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ACOUSTIC_TITLE = "Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction"
ACOUSTIC_DOI = "10.1016/j.apacoust.2024.110369"
ACOUSTIC_KEY = "zhaiSecondOrderAcousticNLOS2025"
RADAR_TITLE = "Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar"
RADAR_DOI = "10.1109/IV64158.2025.11097630"
RADAR_KEY = "jeonRayTracingMmWaveNLOS2025"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def ensure_absent(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise RuntimeError(f"{label}: already contains {needle!r}")


# README: add both verified final-venue records to the public table and timeline.
readme = read("README.md")
for needle in (ACOUSTIC_DOI, RADAR_DOI):
    ensure_absent(readme, needle, "README")
readme_header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
readme_rows = (
    "| 2025 | [Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar](https://doi.org/10.1109/IV64158.2025.11097630) — Jeon et al. | IEEE Intelligent Vehicles Symposium (IV), 1779–1786 (2025) | Uses static 2D mmWave radar points to infer T-junction layout, ray-traces dynamic multipath points, and clusters the unfolded returns to localize multiple hidden pedestrians in an outdoor custom test bed. It extends around-corner automotive radar from controlled single-target demonstrations toward measured multi-target localization. |\n"
    "| 2025 | [Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction](https://doi.org/10.1016/j.apacoust.2024.110369) — Zhai et al. | Applied Acoustics 228, 110369 (2025) | Models second-order Biot–Tolstoy–Medwin edge diffraction as the acoustic sensing matrix and solves the hidden-source inverse problem with fast marginalized block sparse Bayesian learning. Simulations and a 32-channel microphone-array experiment recover source position and strength when direct and first-order paths are unavailable. |\n"
)
readme = replace_once(readme, readme_header, readme_header + readme_rows, "README table header")
readme_timeline_anchor = "2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning [IEEE ICEE]\n"
readme_timeline_lines = (
    "2025 ── Zhai et al.: second-order edge-diffraction transfer modeling and block sparse Bayesian inversion localize hidden acoustic sources without direct or first-order paths [Applied Acoustics]\n"
    "   │     Jeon et al.: ray tracing and clustering of measured 2D mmWave radar point clouds enable outdoor multi-pedestrian localization at T-junctions [IEEE IV]\n"
)
readme = replace_once(readme, readme_timeline_anchor, readme_timeline_lines + readme_timeline_anchor, "README 2025 timeline")
write("README.md", readme)


# Website: add searchable records, increase the self-checked explorer count, and extend 2025 history.
html = read("index.html")
for needle in (ACOUSTIC_DOI, RADAR_DOI):
    ensure_absent(html, needle, "index.html")
html = replace_once(
    html,
    '<div class="stat"><b>257</b><span>tracked latest entries</span></div>',
    '<div class="stat"><b>259</b><span>tracked latest entries</span></div>',
    "website record count",
)
papers_anchor = "    const papers=[\n"
paper_records = (
    '      {cat:"latest modality radar rf mmwave automotive localization tracking ray-tracing measured",title:"Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar",authors:"Jeon et al.",year:2025,venue:"IEEE IV 2025, 1779–1786",url:"https://doi.org/10.1109/IV64158.2025.11097630",key:"Infers T-junction geometry from static 2D mmWave radar points, ray-traces dynamic multipath returns, and applies filtering and clustering to localize multiple hidden pedestrians in an outdoor custom test bed."},\n'
    '      {cat:"latest modality acoustic localization diffraction sparse-bayesian microphone-array measured",title:"Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction",authors:"Zhai et al.",year:2025,venue:"Applied Acoustics 228, 110369",url:"https://doi.org/10.1016/j.apacoust.2024.110369",key:"Builds a sensing matrix from the Biot–Tolstoy–Medwin second-order edge-diffraction response and uses fast marginalized block sparse Bayesian learning to recover hidden-source position and strength when direct and first-order paths are absent; validated with a 32-channel array."},\n'
)
html = replace_once(html, papers_anchor, papers_anchor + paper_records, "website papers array")
# Extend the single 2025 timeline paragraph without disturbing the surrounding dense historical prose.
pattern = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>\n\s*<div class="tl"><div class="year">2026</div>)', re.S)
match = pattern.search(html)
if not match:
    raise RuntimeError("website 2025 timeline block not found")
addition = (
    " Second-order acoustic edge-diffraction inversion combined Biot–Tolstoy–Medwin transport with block sparse Bayesian learning for measured hidden-source localization when stronger paths were unavailable."
    " Outdoor T-junction experiments then used ray tracing, filtering, and clustering of 2D mmWave point clouds to move automotive NLOS radar toward multi-pedestrian localization."
)
html = html[:match.start()] + match.group(1) + match.group(2) + addition + match.group(3) + html[match.end():]
write("index.html", html)


# Survey prose: place each contribution in its modality lineage.
article = read("article/5newscenes.tex")
for key in (ACOUSTIC_KEY, RADAR_KEY):
    ensure_absent(article, key, "article/5newscenes.tex")
radar_anchor = "\\href{https://arxiv.org/abs/2508.02348}{Park~\\etal} use camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, connecting around-corner radar perception to autonomous-driving scene understanding. "
radar_sentence = (
    "Jeon~\\etal~subsequently demonstrated measured outdoor multi-target localization without requiring the camera-derived layout prior~\\cite{jeonRayTracingMmWaveNLOS2025}: static radar points estimate the T-junction geometry, dynamic points are unfolded by ray tracing, and noise filtering plus clustering recover multiple hidden pedestrian positions. "
)
article = replace_once(article, radar_anchor, radar_anchor + radar_sentence, "radar survey anchor")
acoustic_anchor = "Boger-Lombard, Slobodkin, and Katz first showed that acoustic interferometry can retrieve effective Green functions from cross-correlations of uncontrolled broadband noise, enabling passive localization and tracking of a human hidden around a corner without controlled active probing~\\cite{bogerLombardPassiveAcousticCorners2023}.\n\n"
acoustic_para = (
    "Zhai~\\etal~considered the complementary regime in which the direct path and first-order diffraction are both unavailable~\\cite{zhaiSecondOrderAcousticNLOS2025}. They compute a second-order edge-diffraction transfer function with the Biot--Tolstoy--Medwin model, use it as the sensing matrix of a block-sparse inverse problem, and apply fast marginalized block sparse Bayesian learning to estimate source location and strength. Simulation and a 32-channel microphone-array experiment show that diffraction orders normally treated as weak residual transport can support high-resolution NLOS localization when stronger propagation paths are blocked.\n\n"
)
article = replace_once(article, acoustic_anchor, acoustic_anchor + acoustic_para, "acoustic survey anchor")
write("article/5newscenes.tex", article)


# Survey wrapper audit note.
tex = read("bare_jrnl.tex")
for key in (ACOUSTIC_KEY, RADAR_KEY):
    ensure_absent(tex, key, "bare_jrnl.tex")
tex_note = "% 6 August 2026 citation trace: second-order acoustic diffraction inversion and measured outdoor multi-target mmWave localization synchronized.\n"
tex = tex_note + tex
write("bare_jrnl.tex", tex)


# Canonical bibliography used by the survey.
bib = read("egbib_merged_20260711.bib")
for key in (ACOUSTIC_KEY, RADAR_KEY):
    ensure_absent(bib, "{" + key + ",", "merged bibliography")
bib_entries = r'''

@article{zhaiSecondOrderAcousticNLOS2025,
  author  = {Zhai, Qingbo and Ning, Fangli and Wei, Juan and Su, Zhaojing},
  title   = {Non-line-of-sight sound source localization based on block sparse {Bayesian} learning and second-order edge diffraction},
  journal = {Applied Acoustics},
  volume  = {228},
  pages   = {110369},
  year    = {2025},
  doi     = {10.1016/j.apacoust.2024.110369},
  url     = {https://doi.org/10.1016/j.apacoust.2024.110369}
}

@inproceedings{jeonRayTracingMmWaveNLOS2025,
  author    = {Jeon, Mingu and Park, Byeonggyu and Kim, Hee Yeun and Kang, Yujeong and Choi, Byonghyok and Cho, Hansang and Kim, Byungkwan and Lee, Soomok and Seo, Seung Woo and Kim, Seong Woo},
  title     = {Non-Line-of-Sight Multi-Target Localization in {T}-Junctions Using Ray Tracing of mmWave Radar},
  booktitle = {2025 IEEE Intelligent Vehicles Symposium (IV)},
  pages     = {1779--1786},
  year      = {2025},
  publisher = {IEEE},
  doi       = {10.1109/IV64158.2025.11097630},
  url       = {https://doi.org/10.1109/IV64158.2025.11097630}
}
'''
bib = bib.rstrip() + bib_entries + "\n"
write("egbib_merged_20260711.bib", bib)


# Traceable update record.
update_path = ROOT / "updates/2026-08-06-second-order-acoustic-and-mmwave-tjunction-citation-trace.md"
if update_path.exists():
    raise RuntimeError(f"update note already exists: {update_path}")
update_path.write_text(
    """# Citation-traced acoustic and mmWave NLOS additions — 6 August 2026

## Added

- **Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction** — *Applied Acoustics* 228, 110369 (2025), DOI `10.1016/j.apacoust.2024.110369`. The Biot–Tolstoy–Medwin second-order diffraction response forms a block-sparse sensing model, validated with a 32-channel array when direct and first-order paths are unavailable.
- **Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar** — IEEE Intelligent Vehicles Symposium 2025, pp. 1779–1786, DOI `10.1109/IV64158.2025.11097630`. Static and dynamic 2D mmWave point clouds support layout inference, ray tracing, and measured outdoor multi-pedestrian localization.

## Scope and placement

Both papers perform genuine hidden-target inference rather than merely classifying a channel as NLOS. The acoustic paper extends the diffraction-aware localization lineage from first-order beamforming to second-order sparse inversion. The radar paper extends automotive around-corner sensing from single-target or layout-assisted studies toward measured multi-target localization. They are integrated into the README, website explorer and timeline, the corresponding survey modality discussions, and the compiled bibliography/PDF.
""",
    encoding="utf-8",
)

print("Applied bounded synchronization for two citation-traced NLOS papers.")
