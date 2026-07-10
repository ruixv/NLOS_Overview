#!/usr/bin/env python3
"""Anchor-checked 11 July 2026 NLOS literature sync.

Adds two verified missing NLOS papers, integrates them across README, homepage,
survey prose and BibTeX, and fixes the active survey bibliography command. The
script is idempotent and aborts rather than replacing a large file when an
expected anchor is absent.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 0:
        if new in text:
            return text
        raise RuntimeError(f"Missing anchor for {label}: {old[:140]!r}")
    if count != 1:
        raise RuntimeError(f"Expected one anchor for {label}, found {count}")
    return text.replace(old, new, 1)


XBAND_TITLE = "X-band Radar Non-Line-of-Sight Imaging"
NIF_TITLE = (
    "Neural illumination fields: High-fidelity and ambient-robust stereo "
    "reconstruction for two-bounce non-line-of-sight imaging"
)

# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------
readme = read("README.md")
header = "|------|-------|----------------|----------------|\n"
rows = (
    "| 2026 | [X-band Radar Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html) — Du et al. | CVPR 2026 | Introduces a learned, geometry-aware X-band radar NLOS reconstruction system; converts normally diffuse optical transport into predominantly specular long-wavelength transport and experimentally reconstructs hidden objects at ranges up to 40 m. |\n"
    "| 2026 | [Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging](https://doi.org/10.1016/j.optlaseng.2025.109514) — Zhang et al. | Optics and Lasers in Engineering 2026 | Uses a self-supervised continuous neural illumination field and differentiable intensity rendering for two-bounce NLOS reconstruction without binary shadow segmentation, reaching centimeter-scale detail in large hidden spaces under low-contrast and ambient-light interference. |\n"
)
if XBAND_TITLE not in readme and NIF_TITLE not in readme:
    readme = replace_once(readme, header, header + rows, "README latest-additions rows")
elif XBAND_TITLE not in readme or NIF_TITLE not in readme:
    raise RuntimeError("README contains only one of the two synchronized papers")
write("README.md", readme)

# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
index = read("index.html")
missing_titles = [title for title in (XBAND_TITLE, NIF_TITLE) if title not in index]
if missing_titles:
    stat_pattern = re.compile(
        r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>'
    )
    match = stat_pattern.search(index)
    if not match:
        raise RuntimeError("Homepage latest-count anchor not found")
    new_count = int(match.group(1)) + len(missing_titles)
    index = stat_pattern.sub(
        f'<div class="stat"><b>{new_count}</b><span>tracked latest entries</span></div>',
        index,
        count=1,
    )

objects = (
    '      {cat:"latest modality learning",title:"X-band Radar Non-Line-of-Sight Imaging",authors:"Du et al.",year:2026,venue:"CVPR 2026",url:"https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html",key:"Learned dense prediction plus geometry-aware X-band radar reconstruction for long-range hidden-scene imaging, demonstrated up to 40 m."},\n'
    '      {cat:"latest passive learning",title:"Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging",authors:"Zhang et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",url:"https://doi.org/10.1016/j.optlaseng.2025.109514",key:"Self-supervised continuous neural illumination fields and differentiable intensity rendering recover two-bounce hidden geometry without binary shadow segmentation."},\n'
)
if XBAND_TITLE not in index and NIF_TITLE not in index:
    index = replace_once(index, "    const papers=[\n", "    const papers=[\n" + objects, "homepage paper objects")
elif XBAND_TITLE not in index or NIF_TITLE not in index:
    raise RuntimeError("Homepage contains only one of the two synchronized papers")

old_timeline = (
    '<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>Arbitrary relay surfaces, consumer LiDAR, RIS, RF geometry, and distributed MIMO imaging</strong><p>The frontier moves toward real-world geometry: arbitrary and irregular relay surfaces with CUDA acceleration and Gaussian transient rendering, low-cost NIR raster scanning, smartphone-grade LiDAR motion sampling, RF/radar neural reconstruction, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.</p></div></div>'
)
new_timeline = (
    '<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>Arbitrary relays, consumer LiDAR, long-range radar, neural two-bounce fields, and distributed MIMO</strong><p>The frontier moves toward real-world scale and geometry: arbitrary and irregular relay surfaces with CUDA acceleration and Gaussian transient rendering, low-cost NIR and smartphone LiDAR capture, X-band radar reconstruction demonstrated up to 40 m, neural illumination fields for robust two-bounce shadow inversion, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.</p></div></div>'
)
index = replace_once(index, old_timeline, new_timeline, "2026 homepage timeline")
write("index.html", index)

# ---------------------------------------------------------------------------
# Survey prose: semantically integrate two-bounce and radar developments
# ---------------------------------------------------------------------------
newscenes = read("article/5newscenes.tex")
if "zhangNeuralIlluminationFields2026" not in newscenes:
    anchor = (
        "This analytical framework provides design guidelines for future NLOS systems that incorporate time-gating in two-bounce configurations.\n"
    )
    addition = anchor + (
        "\nA complementary steady-state trajectory replaces binary shadow carving with a continuous learned scene model. Zhang~\\etal~introduced Neural Illumination Fields (NIF)~\\cite{zhangNeuralIlluminationFields2026}, which jointly represents hidden-space density and illumination-dependent image formation with multilayer perceptrons and optimizes the representation through differentiable intensity rendering. Because NIF synthesizes measured shadow images directly, it avoids error-prone binary shadow segmentation and remains effective under low shadow contrast and ambient-light interference. This work shifts two-bounce NLOS from discrete occupancy carving toward self-supervised neural inverse rendering for large hidden volumes.\n"
    )
    newscenes = replace_once(newscenes, anchor, addition, "two-bounce NIF survey paragraph")

if "duXBandRadarNLOS2026" not in newscenes:
    anchor = (
        "The radar approach is complementary to optical NLOS: it operates through walls and in total darkness, but at lower spatial resolution than optical methods.\n"
    )
    addition = anchor + (
        "\nDu~\\etal~extended radar NLOS from room-scale mmWave perception toward long-range X-band imaging~\\cite{duXBandRadarNLOS2026}. Their system exploits the longer wavelength to make relay interactions predominantly specular and combines learned dense prediction with geometry-aware reconstruction to compensate for the low native spatial resolution of radar. Prototype experiments reconstruct hidden objects at distances up to 40~m, demonstrating that modality selection can change not only robustness but also the practical range envelope of NLOS imaging.\n"
    )
    newscenes = replace_once(newscenes, anchor, addition, "X-band radar survey paragraph")
write("article/5newscenes.tex", newscenes)

# ---------------------------------------------------------------------------
# BibTeX and active bibliography command
# ---------------------------------------------------------------------------
bib = r'''@inproceedings{duXBandRadarNLOS2026,
  author    = {Dongyu Du and Mingkun Zhao and Yutong Yang and Dominik Scheuble and Xiaolong Huang and Zijian Shao and Mario Bijelic and Kaushik Sengupta and Felix Heide},
  title     = {X-band Radar Non-Line-of-Sight Imaging},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages     = {5647--5658},
  month     = jun,
  year      = {2026},
  url       = {https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html}
}

@article{zhangNeuralIlluminationFields2026,
  author  = {Jingyuan Zhang and Bochao Zhang and Zijin Wang and Chao Qu and Lianfa Bai and Xiaoyu Chen and Jing Han and Baohui Guo},
  title   = {Neural Illumination Fields: High-Fidelity and Ambient-Robust Stereo Reconstruction for Two-Bounce Non-Line-of-Sight Imaging},
  journal = {Optics and Lasers in Engineering},
  volume  = {198},
  pages   = {109514},
  month   = mar,
  year    = {2026},
  doi     = {10.1016/j.optlaseng.2025.109514},
  url     = {https://doi.org/10.1016/j.optlaseng.2025.109514}
}
'''
write("egbib_20260711_run15_updates.bib", bib)

tex = read("bare_jrnl.tex")
bib_sources = (
    "egbib,egbib_20260701_updates,egbib_20260702_updates,"
    "egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,"
    "egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates,"
    "egbib_20260709_updates,egbib_20260711_updates,"
    "egbib_20260711_run15_updates,egbib_2026_updates"
)
new_bibliography = rf"\bibliography{{{bib_sources}}}"
active_pattern = re.compile(r"(?m)^\\bibliography\{[^}]+\}\s*$")
active = active_pattern.findall(tex)
if len(active) != 1:
    raise RuntimeError(f"Expected exactly one active bibliography command, found {len(active)}")
tex = active_pattern.sub(lambda _m: new_bibliography, tex, count=1)
write("bare_jrnl.tex", tex)

# ---------------------------------------------------------------------------
# Consistency checks and update note
# ---------------------------------------------------------------------------
for title in (XBAND_TITLE, NIF_TITLE):
    if title not in read("README.md") or title not in read("index.html"):
        raise RuntimeError(f"Public-surface consistency check failed for {title}")
for key in ("duXBandRadarNLOS2026", "zhangNeuralIlluminationFields2026"):
    if key not in read("article/5newscenes.tex") or key not in bib:
        raise RuntimeError(f"Survey/BibTeX consistency check failed for {key}")
if "egbib_20260711_run15_updates" not in read("bare_jrnl.tex"):
    raise RuntimeError("Active bibliography command does not include run-15 BibTeX")

note = '''# 11 July 2026 X-band radar, neural two-bounce, and bibliography sync

Fresh keyword search and forward-citation tracing from core optical NLOS, phasor-field, and two-bounce papers identified two verified missing works that are directly about NLOS imaging rather than incidental citations:

- **X-band Radar Non-Line-of-Sight Imaging** — Du et al., CVPR 2026. A neural, geometry-aware X-band radar pipeline for long-range hidden-scene reconstruction, experimentally demonstrated up to 40 m.
- **Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging** — Zhang et al., Optics and Lasers in Engineering 198:109514 (2026), DOI 10.1016/j.optlaseng.2025.109514. A self-supervised continuous neural field and differentiable-rendering method for robust two-bounce shadow inversion without binary segmentation.

## Synchronized artifacts

- `README.md`: both papers added with final verified venues and concise contribution summaries.
- `index.html`: both paper objects added; latest-entry count increased from 81 to 83; the 2026 timeline now includes long-range X-band radar and neural two-bounce fields.
- `article/5newscenes.tex`: NIF integrated in the two-bounce section and X-band radar integrated in the radar-NLOS section.
- `egbib_20260711_run15_updates.bib`: final-venue BibTeX records added.
- `bare_jrnl.tex`: the active bibliography command was corrected to include every supplemental `egbib*.bib` source, including this run. The previous active command still pointed only to `egbib`, despite a commented all-supplements example.

## PDF status

The GitHub Actions workflow performs a clean LaTeX/BibTeX rebuild, checks for undefined citations/references, validates the resulting PDF with `pdfinfo` and `pdftotext`, and confirms that both newly integrated paper titles appear in the generated survey text. The workflow records the final result below.
'''
write("updates/2026-07-11-xband-nif-and-bibliography-sync.md", note)

print("Run-15 NLOS sync completed successfully")
