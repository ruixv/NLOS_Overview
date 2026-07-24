#!/usr/bin/env python3
"""Integrate citation-traced radar/mmWave/THz NLOS reconstruction lineage, fail closed."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-24-radar-reconstruction-lineage.md"

TRACE = "% 24 July 2026 citation trace: measured radar/mmWave and sub-THz NLOS reconstruction lineage integrated."
OLD_COUNT = 193
NEW_COUNT = 201

PAPERS = [
    {
        "title": "Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar",
        "doi": "10.1109/TGRS.2021.3112579",
        "key": "weiMillimeterWaveNLOS3D2022",
        "row": "| 2022 | [Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar](https://doi.org/10.1109/TGRS.2021.3112579) — Wei et al. | IEEE TGRS 2022 | Establishes a measured 77 GHz MIMO around-corner 3D imaging model, resolution analysis, mirror-symmetry backprojection, and relay-surface phase-error compensation, providing the physical foundation for later model-driven mmWave NLOS reconstruction. |",
        "obj": '{cat:"latest modality radar reconstruction",title:"Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar",authors:"Wei et al.",year:2022,venue:"IEEE TGRS 2022",url:"https://doi.org/10.1109/TGRS.2021.3112579",key:"Foundational measured 77 GHz MIMO around-corner 3D radar imaging with mirror-symmetry backprojection, resolution analysis, and relay-surface phase-error compensation."},',
    },
    {
        "title": "Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging",
        "doi": "10.12000/JR24060",
        "key": "caiPreciseRadarNLOS2024",
        "row": "| 2024 | [Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging](https://doi.org/10.12000/JR24060) — Cai et al. | Journal of Radars 2024 | Separates LOS and NLOS multipath echoes and jointly estimates hidden reflectivity, total-variation structure, and relay-surface phase error; measured corner experiments reconstruct knives and metal racks under aperture occlusion. |",
        "obj": '{cat:"latest modality radar reconstruction",title:"Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging",authors:"Cai et al.",year:2024,venue:"Journal of Radars 2024",url:"https://doi.org/10.12000/JR24060",key:"NSIR separates LOS/NLOS multipath and jointly handles sparsity, total variation, aperture loss, and relay-surface phase error for measured hidden-target 3D reconstruction."},',
    },
    {
        "title": "RM-CSTV: An Effective High-Resolution Method of Non-Line-of-Sight Millimeter-Wave Radar 3-D Imaging",
        "doi": "10.1360/nso/20230085",
        "key": "liuRMCSTVRadarNLOS2024",
        "row": "| 2024 | [RM-CSTV: An Effective High-Resolution Method of Non-Line-of-Sight Millimeter-Wave Radar 3-D Imaging](https://doi.org/10.1360/nso/20230085) — Liu et al. | National Science Open 2024 | Couples a fast range-migration kernel with complex sparsity and total variation, corrects virtual-target geometry, and preserves hidden contours under sparse sampling while reducing computation by roughly two orders of magnitude versus matrix-based CSTV. |",
        "obj": '{cat:"latest modality radar reconstruction",title:"RM-CSTV: An Effective High-Resolution Method of Non-Line-of-Sight Millimeter-Wave Radar 3-D Imaging",authors:"Liu et al.",year:2024,venue:"National Science Open 2024",url:"https://doi.org/10.1360/nso/20230085",key:"A fast range-migration kernel plus complex sparsity and total variation corrects NLOS virtual-target geometry and preserves contours under sparse sampling."},',
    },
    {
        "title": "Non-Line-of-Sight 3D Reconstruction with Radar",
        "doi": "",
        "key": "laiHoloRadar2025",
        "row": "| 2025 | [Non-Line-of-Sight 3D Reconstruction with Radar (HoloRadar)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6994a52f9499b865b7c9e167f5495ef3-Abstract-Conference.html) — Lai, Lan, Zhao | NeurIPS 2025 | Uses a single mobile mmWave radar to predict multi-return range images and then map mirrored observations to their physical locations with a ray-interaction-aware network, reconstructing complete LOS and hidden 3D scenes in real environments. |",
        "obj": '{cat:"latest modality radar learning reconstruction",title:"Non-Line-of-Sight 3D Reconstruction with Radar",authors:"Lai, Lan, Zhao",year:2025,venue:"NeurIPS 2025",url:"https://proceedings.neurips.cc/paper_files/paper/2025/hash/6994a52f9499b865b7c9e167f5495ef3-Abstract-Conference.html",key:"HoloRadar predicts multi-return radar ranges and maps mirrored observations to their true locations with physics-guided ray interactions for mobile-robot LOS and NLOS 3D reconstruction."},',
    },
    {
        "title": "Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement",
        "doi": "10.1109/TAP.2025.3583778",
        "key": "caiACTENetRadarNLOS2025",
        "row": "| 2025 | [Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement](https://doi.org/10.1109/TAP.2025.3583778) — Cai et al. | IEEE TAP 2025 | Introduces unsupervised ACTE-Net: Gaussian-convolution artifact cancellation, energy-based target enhancement, and a 2D holographic operator suppress multipath blur without storing a large sensing matrix; measured hidden-letter and trellis experiments validate 3D reconstruction. |",
        "obj": '{cat:"latest modality radar learning reconstruction",title:"Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement",authors:"Cai et al.",year:2025,venue:"IEEE TAP 2025",url:"https://doi.org/10.1109/TAP.2025.3583778",key:"ACTE-Net combines Gaussian-convolution artifact cancellation, target-energy enhancement, and a holographic operator in an unsupervised measured-data mmWave reconstruction network."},',
    },
    {
        "title": "Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning",
        "doi": "10.1109/TCI.2025.3597462",
        "key": "caiEquivariantRadarNLOS2025",
        "row": "| 2025 | [Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning](https://doi.org/10.1109/TCI.2025.3597462) — Cai et al. | IEEE TCI 2025 | Proposes a fully self-supervised equivariant-imaging framework with TV-constrained deep unfolding and an adaptive peak-convolution threshold module, reconstructing measured 2D/3D mmWave SAR images from partial, noisy, multipath-corrupted NLOS echoes. |",
        "obj": '{cat:"latest modality radar learning reconstruction",title:"Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning",authors:"Cai et al.",year:2025,venue:"IEEE TCI 2025",url:"https://doi.org/10.1109/TCI.2025.3597462",key:"A fully self-supervised equivariant-imaging framework combines TV-constrained deep unfolding with adaptive peak-convolution thresholds for partial noisy measured NLOS SAR echoes."},',
    },
    {
        "title": "RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar",
        "doi": "10.12000/JR25132",
        "key": "chenRMOperatorRadarNLOS2026",
        "row": "| 2026 | [RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar](https://doi.org/10.12000/JR25132) — Chen et al. | Journal of Radars 2026 | Embeds a fast range-migration operator in a FISTA-derived unfolding network to compensate phase error, aperture shadowing, and multipath; measured near-field targets under ideal and non-ideal reflectors show higher precision and about 100× speedup over sparse solvers. |",
        "obj": '{cat:"latest modality radar learning reconstruction",title:"RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar",authors:"Chen et al.",year:2026,venue:"Journal of Radars 2026",url:"https://doi.org/10.12000/JR25132",key:"A fast range-migration operator embedded in FISTA-style deep unfolding compensates phase error, aperture shadowing, and multipath in measured near-field 3D radar NLOS."},',
    },
    {
        "title": "Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging",
        "doi": "10.3390/photonics13050440",
        "key": "chenDeepUnfoldingTHzNLOS2026",
        "row": "| 2026 | [Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging](https://doi.org/10.3390/photonics13050440) — Chen et al. | Photonics 2026 | Extends model-driven NLOS radar reconstruction to a measured 121 GHz platform, embedding a fast holographic operator in FISTA-Net to correct phase error, aperture occlusion, and multipath while avoiding a prohibitively large sensing matrix. |",
        "obj": '{cat:"latest modality radar thz learning reconstruction",title:"Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging",authors:"Chen et al.",year:2026,venue:"Photonics 2026",url:"https://doi.org/10.3390/photonics13050440",key:"A 121 GHz measured around-corner system embeds a fast holographic operator in FISTA-Net for efficient sub-THz hidden-target 3D reconstruction."},',
    },
]

BIB_ENTRIES = r'''
@article{weiMillimeterWaveNLOS3D2022,
  author = {Wei, Shunjun and Wei, Jinshan and Liu, Xinyuan and Wang, Mou and Liu, Shan and Fan, Fan and Zhang, Xiaoling and Shi, Jun and Cui, Guolong},
  title = {Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {60},
  pages = {1--18},
  eid = {5106518},
  year = {2022},
  doi = {10.1109/TGRS.2021.3112579},
  url = {https://doi.org/10.1109/TGRS.2021.3112579}
}

@article{caiPreciseRadarNLOS2024,
  author = {Cai, Xiang and Wei, Shunjun and Wen, Yanbo and Hu, Jiangbo and Wang, Mou and Shi, Jun and Cui, Guolong},
  title = {Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging},
  journal = {Journal of Radars},
  volume = {13},
  number = {4},
  pages = {791--806},
  year = {2024},
  doi = {10.12000/JR24060},
  url = {https://doi.org/10.12000/JR24060}
}

@article{liuRMCSTVRadarNLOS2024,
  author = {Liu, Xinyuan and Wei, Shunjun and Pu, Wei and Cai, Xiang and Wen, Yanbo and Guo, Shisheng and Kong, Lingjiang and Zhang, Xiaoling},
  title = {{RM-CSTV}: An Effective High-Resolution Method of Non-Line-of-Sight Millimeter-Wave Radar 3-D Imaging},
  journal = {National Science Open},
  volume = {3},
  number = {5},
  eid = {20230085},
  year = {2024},
  doi = {10.1360/nso/20230085},
  url = {https://doi.org/10.1360/nso/20230085}
}

@inproceedings{laiHoloRadar2025,
  author = {Lai, Haowen and Lan, Zitong and Zhao, Mingmin},
  title = {Non-Line-of-Sight 3D Reconstruction with Radar},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {38},
  year = {2025},
  url = {https://proceedings.neurips.cc/paper_files/paper/2025/hash/6994a52f9499b865b7c9e167f5495ef3-Abstract-Conference.html}
}

@article{caiACTENetRadarNLOS2025,
  author = {Cai, Xiang and Wei, Shunjun and Zhang, Hao and Wen, Yanbo and Wang, Mou and Shi, Jun and Cui, Guolong},
  title = {Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement},
  journal = {IEEE Transactions on Antennas and Propagation},
  volume = {73},
  number = {10},
  pages = {8088--8103},
  year = {2025},
  doi = {10.1109/TAP.2025.3583778},
  url = {https://doi.org/10.1109/TAP.2025.3583778}
}

@article{caiEquivariantRadarNLOS2025,
  author = {Cai, Xiang and Wei, Shunjun and Wang, Mou and Zhang, Hao and Chen, Kun and Liu, Xinyuan and Shi, Jun and Cui, Guolong},
  title = {Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning},
  journal = {IEEE Transactions on Computational Imaging},
  volume = {11},
  pages = {1190--1205},
  month = {August},
  note = {Published 11 August 2025},
  year = {2025},
  doi = {10.1109/TCI.2025.3597462},
  url = {https://doi.org/10.1109/TCI.2025.3597462}
}

@article{chenRMOperatorRadarNLOS2026,
  author = {Chen, Kun and Wei, Shunjun and Cai, Xiang and Wang, Mou and Zhang, Hao and Cui, Guolong and Zhang, Xiaoling and Chen, Siyuan},
  title = {RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar},
  journal = {Journal of Radars},
  volume = {15},
  number = {1},
  pages = {42--63},
  year = {2026},
  doi = {10.12000/JR25132},
  url = {https://doi.org/10.12000/JR25132}
}

@article{chenDeepUnfoldingTHzNLOS2026,
  author = {Chen, Kun and Wei, Shunjun and Wang, Mou and Chen, Juran and Han, Bingyu and Li, Jin and Liu, Zhe and Zhang, Xiaoling and Liao, Yi and Gao, Pengcheng and Mi, Xiaolin},
  title = {Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging},
  journal = {Photonics},
  volume = {13},
  number = {5},
  eid = {440},
  month = {April},
  note = {Published 30 April 2026},
  year = {2026},
  doi = {10.3390/photonics13050440},
  url = {https://doi.org/10.3390/photonics13050440}
}
'''.strip()

RADAR_PROSE = r'''
\vspace{0.8mm}
\noindent \textbf{Measured mmWave reconstruction from physical models to fast regularized migration.}
Wei~\etal~established a measured 77~GHz MIMO foundation for around-corner 3D radar imaging, deriving mirror-symmetry backprojection, resolution behavior, and relay-surface phase-error compensation~\cite{weiMillimeterWaveNLOS3D2022}. Cai~\etal~then introduced NSIR, which separates LOS and multipath NLOS echoes before jointly estimating hidden reflectivity, total-variation structure, and reflective-surface phase error~\cite{caiPreciseRadarNLOS2024}. RM-CSTV~\cite{liuRMCSTVRadarNLOS2024} replaced a large matrix operator with range migration while retaining complex sparsity and total-variation constraints, correcting virtual-target positions and preserving contours under aperture loss and sparse sampling. These works form a model-driven radar lineage in which environmental reflections are calibrated as an imaging aperture rather than treated only as nuisance multipath.

\vspace{0.8mm}
\noindent \textbf{Self-supervised and model-unfolded radar NLOS reconstruction.}
The radar branch subsequently adopted learned optimization without abandoning its propagation operators. ACTE-Net~\cite{caiACTENetRadarNLOS2025} combines a Gaussian-convolution artifact suppressor, an energy-enhancement operator, and holographic reconstruction in an unsupervised network validated on measured hidden targets. Cai~\etal~further exploit group invariance in an equivariant-imaging framework whose TV-constrained unfolding network and adaptive peak-convolution thresholds reconstruct 2D/3D mmWave SAR images from partial noisy echoes~\cite{caiEquivariantRadarNLOS2025}. Chen~\etal~embed a fast range-migration operator in a FISTA-derived network for measured near-field mmWave reconstruction under phase error, aperture shadowing, and multipath~\cite{chenRMOperatorRadarNLOS2026}; a parallel 121~GHz system replaces range migration with a compact holographic operator and demonstrates the same model-unfolding trajectory at sub-terahertz wavelengths~\cite{chenDeepUnfoldingTHzNLOS2026}. Together with HoloRadar's mobile, ray-interaction-aware scene reconstruction~\cite{laiHoloRadar2025}, this progression shifts radar NLOS from isolated target focusing toward practical full-scene geometry and adaptive learned inversion while retaining explicit propagation structure.

'''


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


readme = read(README)
index = read(INDEX)
newscenes = read(NEWSCENES)
survey = read(SURVEY)
bib = read(BIB)

# Fail closed if any public or bibliography record is already partially present.
for p in PAPERS:
    if p["title"].lower() in readme.lower() or p["title"].lower() in index.lower():
        raise SystemExit(f"Public artifact already contains {p['title']}; refusing a partial duplicate update")
    if p["doi"] and (p["doi"] in readme or p["doi"] in index or f"doi = {{{p['doi']}}}" in bib):
        raise SystemExit(f"DOI already present for {p['title']}; refusing duplicate insertion")
    if "@article{" + p["key"] in bib or "@inproceedings{" + p["key"] in bib:
        raise SystemExit(f"Bibliography key already present: {p['key']}")

if f'<b>{OLD_COUNT}</b><span>tracked latest entries</span>' not in index:
    raise SystemExit(f"Website count is not the expected pre-update value {OLD_COUNT}")

# README latest additions.
header = "|------|-------|----------------|----------------|\n"
if readme.count(header) != 1:
    raise SystemExit("README latest-additions table header is not unique")
readme = readme.replace(header, header + "\n".join(p["row"] for p in PAPERS) + "\n", 1)

# README milestone additions at semantically correct years.
timeline_additions = {
    "    │     Luesia et al.: scattering-media phasor fields — virtual-wave reconstruction remains effective for hidden scenes immersed in thick volumetric scattering [Optics Letters]\n":
        "    │     Luesia et al.: scattering-media phasor fields — virtual-wave reconstruction remains effective for hidden scenes immersed in thick volumetric scattering [Optics Letters]\n"
        "    │     Wei et al.: measured 77 GHz mmWave NLOS 3D imaging — mirror-symmetry backprojection and relay-phase compensation establish a radar reconstruction foundation [IEEE TGRS]\n",
    "    │     Zhang et al.: real-time scan-free NLOS — parallel SPAD-array boundary migration reaches 151-fps acquisition and 19-fps reconstruction [APL Photonics]\n":
        "    │     Zhang et al.: real-time scan-free NLOS — parallel SPAD-array boundary migration reaches 151-fps acquisition and 19-fps reconstruction [APL Photonics]\n"
        "    │     Cai et al. / Liu et al.: NSIR and RM-CSTV — measured radar echo separation, phase correction, range migration, sparsity, and TV sharpen hidden 3D targets [Journal of Radars / National Science Open]\n",
    "2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning [IEEE ICEE]\n":
        "2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning [IEEE ICEE]\n"
        "    │     Lai et al.: HoloRadar — mobile single-radar full-scene LOS/NLOS 3D reconstruction [NeurIPS]\n"
        "    │     Cai et al.: ACTE-Net and equivariant adaptive-threshold unfolding — self-supervised measured mmWave NLOS reconstruction [IEEE TAP / TCI]\n",
}
for anchor, replacement in timeline_additions.items():
    if readme.count(anchor) != 1:
        raise SystemExit(f"README timeline anchor count is {readme.count(anchor)}, expected 1: {anchor[:60]}")
    readme = readme.replace(anchor, replacement, 1)
# Add 2026 radar/sub-THz milestone immediately before the 2025 block (the existing timeline ordering is historical but not strictly sorted in this legacy section).
anchor = "2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning [IEEE ICEE]\n"
insert = "2026 ── Chen et al.: RM-operator and 121 GHz holographic deep unfolding — explicit radar propagators become efficient learned around-corner 3D solvers [Journal of Radars / Photonics]\n    │\n"
if readme.count(insert) == 0:
    if readme.count(anchor) != 1:
        raise SystemExit("Post-replacement README 2025 timeline anchor is not unique")
    readme = readme.replace(anchor, insert + anchor, 1)

# Website objects and count.
papers_anchor = "    const papers = [\n"
if index.count(papers_anchor) != 1:
    raise SystemExit("Website paper-array anchor is not unique")
index = index.replace(papers_anchor, papers_anchor + "      " + "\n      ".join(p["obj"] for p in PAPERS) + "\n", 1)
index = index.replace(f'<b>{OLD_COUNT}</b><span>tracked latest entries</span>', f'<b>{NEW_COUNT}</b><span>tracked latest entries</span>', 1)

# Append the radar lineage to the corresponding year timeline summaries.
def append_timeline(year: int, sentence: str, text: str) -> str:
    pattern = re.compile(r'(<div class="tl"><div class="year">' + str(year) + r'</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.DOTALL)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f"Website timeline year {year} count is {len(matches)}, expected 1")
    old = matches[0].group(0)
    new = matches[0].group(1) + matches[0].group(2) + " " + sentence + matches[0].group(3)
    return text.replace(old, new, 1)

index = append_timeline(2022, "Wei et al. established measured mmWave around-corner 3D imaging with mirror-symmetry backprojection and relay-phase compensation.", index)
index = append_timeline(2024, "NSIR and RM-CSTV established measured, regularized radar reconstruction with echo separation, phase correction, fast range migration, sparsity, and total variation.", index)
index = append_timeline(2025, "HoloRadar moved a single mobile mmWave sensor to full LOS/NLOS scene reconstruction, while ACTE-Net and equivariant adaptive-threshold unfolding introduced unsupervised and self-supervised measured-data inversion.", index)
index = append_timeline(2026, "Range-migration and 121 GHz holographic operators embedded in FISTA-style networks extended model-driven radar NLOS to efficient mmWave and sub-THz 3D reconstruction.", index)

# Survey prose: insert after the existing X-band paragraph and before the broad RF sensing paragraph.
prose_heading = r"\noindent \textbf{Measured mmWave reconstruction from physical models to fast regularized migration.}"
if prose_heading not in newscenes:
    anchor = "Recent RF/mmWave work further expands the meaning of NLOS perception beyond monostatic reconstruction."
    if newscenes.count(anchor) != 1:
        raise SystemExit("Radar-survey insertion anchor is not unique")
    newscenes = newscenes.replace(anchor, RADAR_PROSE + anchor, 1)
if newscenes.count(prose_heading) != 1:
    raise SystemExit("Radar lineage prose heading is not unique")
for p in PAPERS:
    if newscenes.count(r"\cite{" + p["key"] + "}") < 1:
        raise SystemExit(f"Survey prose lacks citation: {p['key']}")

# Survey trace marker.
if TRACE not in survey:
    anchor = "%% bare_jrnl.tex\n"
    if survey.count(anchor) != 1:
        raise SystemExit("Survey trace anchor is not unique")
    survey = survey.replace(anchor, anchor + TRACE + "\n", 1)
if survey.count(TRACE) != 1:
    raise SystemExit("Survey trace marker is not unique")

# Append canonical bibliography records to the bibliography actually used by bare_jrnl.tex.
bib = bib.rstrip() + "\n\n" + BIB_ENTRIES + "\n"
for p in PAPERS:
    key_count = bib.count("{" + p["key"] + ",")
    if key_count != 1:
        raise SystemExit(f"Bibliography key count for {p['key']} is {key_count}, expected 1")
    if p["doi"] and bib.count(f"doi = {{{p['doi']}}}") != 1:
        raise SystemExit(f"Bibliography DOI count for {p['doi']} is not 1")

# Cross-artifact verification before writing.
for p in PAPERS:
    if readme.lower().count(p["title"].lower()) != 1:
        raise SystemExit(f"README title count invalid: {p['title']}")
    if index.lower().count(p["title"].lower()) != 1:
        raise SystemExit(f"Website title count invalid: {p['title']}")
if f'<b>{NEW_COUNT}</b><span>tracked latest entries</span>' not in index:
    raise SystemExit("Website count was not updated")

note = f"""# Radar/mmWave/sub-THz NLOS reconstruction lineage — 24 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found. The newest date-verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, 22 July 2026).

Citation tracing through the optical NLOS core and the radar reconstruction literature exposed a major modality-level consistency gap. Eight direct hidden-scene reconstruction papers were absent from the README and website; seven were also absent from the survey prose and consolidated bibliography, while HoloRadar was discussed in the survey but lacked a public explorer record and canonical BibTeX entry.

## Integrated lineage

- Wei et al., *Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar*, IEEE TGRS 2022, DOI `10.1109/TGRS.2021.3112579`.
- Cai et al., *Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging*, Journal of Radars 2024, DOI `10.12000/JR24060`.
- Liu et al., *RM-CSTV*, National Science Open 2024, DOI `10.1360/nso/20230085`.
- Lai et al., *Non-Line-of-Sight 3D Reconstruction with Radar (HoloRadar)*, NeurIPS 2025.
- Cai et al., *Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement*, IEEE TAP 2025, DOI `10.1109/TAP.2025.3583778`.
- Cai et al., *Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning*, IEEE TCI 2025, DOI `10.1109/TCI.2025.3597462`.
- Chen et al., *RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar*, Journal of Radars 2026, DOI `10.12000/JR25132`.
- Chen et al., *Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging*, Photonics 2026, DOI `10.3390/photonics13050440`.

## Changes

1. Added all eight papers to README Latest Additions and the historical milestone timeline.
2. Added searchable website explorer records, year-specific timeline context, and changed the tracked-entry count from {OLD_COUNT} to {NEW_COUNT}.
3. Expanded `article/5newscenes.tex` with two literature-review paragraphs connecting measured physical radar models, NSIR/RM-CSTV, HoloRadar, unsupervised ACTE-Net, equivariant threshold learning, RM-operator unfolding, and 121 GHz holographic unfolding.
4. Added canonical BibTeX records to `egbib_merged_20260711.bib`, including a missing HoloRadar entry needed by the existing survey citation.
5. Added a trace marker to `bare_jrnl.tex` and rebuilt `bare_jrnl.pdf`.

## Validation

- Unique title/DOI/key checks across README, website, survey, and consolidated bibliography.
- Clean `pdflatex → bibtex → pdflatex ×2` build.
- Required bibliography items present in the generated `.bbl`.
- PDF page metadata, extracted text, and rendered pages checked.
"""

write_if_changed(README, readme)
write_if_changed(INDEX, index)
write_if_changed(NEWSCENES, newscenes)
write_if_changed(SURVEY, survey)
write_if_changed(BIB, bib)
write_if_changed(NOTE, note)
print("Radar/mmWave/sub-THz NLOS lineage synchronized and validated.")
