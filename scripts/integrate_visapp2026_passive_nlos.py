#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
PASSIVE = ROOT / "article" / "3passive.tex"
MODALITIES = ROOT / "article" / "5newscenes.tex"
ABSTRACT = ROOT / "article" / "0abstract.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

MATSUBARA_TITLE = "3D Reconstruction of Hidden Objects from Simultaneous Recovery of Light Source and Environment"
MATSUBARA_DOI = "10.5220/0014435000004084"
KOZAWA_TITLE = "Estimating the 3D Position of Hidden Humans Using Reflections on Vehicle Bodies"
KOZAWA_DOI = "10.5220/0014434900004084"
WEI_TITLE = "Single-shot imaging through scattering media and around the corner beyond the OME range via polarization-encoded spatial multiplexing"
WEI_DOI = "10.1016/j.optlaseng.2026.109602"
MINING_TITLE = "Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion"
MINING_DOI = "10.3390/s26144615"


def die(message: str) -> None:
    raise RuntimeError(message)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        die(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    separator = "|------|-------|----------------|----------------|\n"
    rows = ""
    if MATSUBARA_DOI not in text:
        rows += (
            f"| 2026 | [{MATSUBARA_TITLE}](https://doi.org/{MATSUBARA_DOI}) — Matsubara et al. | VISAPP 2026 | Uses far-infrared reflections from walls and floors to reconstruct moving hidden luminous objects while jointly estimating unknown scene parameters. Self-supervised reprojection on real measurements is combined with supervised synthetic training, extending passive thermal NLOS from known calibrated environments toward joint scene-and-target recovery. |\n"
            f"| 2026 | [{KOZAWA_TITLE}](https://doi.org/{KOZAWA_DOI}) — Kozawa et al. | VISAPP 2026 | Treats curved vehicle bodies as opportunistic convex mirrors: a video detector finds distorted pedestrian reflections, while monocular depth, surface normals, and a specular-reflection loss recover the hidden pedestrian's 3D road position. This is passive NLOS localization rather than full hidden-scene reconstruction. |\n"
        )
    if WEI_DOI not in text:
        rows += (
            f"| 2026 | [{WEI_TITLE}](https://doi.org/{WEI_DOI}) — Wei et al. | Optics and Lasers in Engineering 2026 | Polarization-encoded spatial multiplexing demultiplexes speckles from distinct optical-memory-effect regions in one exposure, enabling multi-target hidden-scene recovery beyond the conventional memory-effect field of view; experiments report 32 dB demultiplexing fidelity and 3.75× field-of-view expansion. |\n"
        )
    if MINING_DOI not in text:
        rows += (
            f"| 2026 | [{MINING_TITLE}](https://doi.org/{MINING_DOI}) — Yang et al. | Sensors 2026 | BSCF geometrically filters multipath-corrupted 4D radar and selectively injects high-confidence radar points into 3D-LiDAR blind regions in real open-pit-mine data. It provides hidden-target existence and envelope-level risk cues rather than full semantic detection or 3D reconstruction. |\n"
        )
    if rows:
        text = replace_once(text, separator, separator + rows, "README latest-additions table")

    timeline_additions = []
    if "Matsubara et al.: joint hidden thermal-source and environment recovery" not in text:
        timeline_additions.extend([
            "   │     Matsubara et al.: joint hidden thermal-source and environment recovery combines real-image reprojection with supervised synthetic learning [VISAPP]\n",
            "   │     Kozawa et al.: curved vehicle bodies become opportunistic mirrors for camera-only hidden-pedestrian 3D localization [VISAPP]\n",
        ])
    if "Wei et al.: polarization-encoded spatial multiplexing" not in text:
        timeline_additions.append(
            "   │     Wei et al.: polarization-encoded spatial multiplexing demultiplexes multiple speckle regions for single-shot around-corner imaging beyond the optical memory-effect range [Optics and Lasers in Engineering]\n"
        )
    if "Yang et al.: radar-LiDAR blind-spot complementary fusion" not in text:
        timeline_additions.append(
            "   │     Yang et al.: radar-LiDAR blind-spot complementary fusion supplies measured hidden-target risk cues under complete haul-truck occlusion [Sensors]\n"
        )
    if timeline_additions:
        match = re.search(r"(2026 ──[^\n]*\n)", text)
        if not match:
            die("README 2026 timeline anchor not found")
        text = text[: match.end()] + "".join(timeline_additions) + text[match.end() :]

    text = text.replace("**Update run: 25 July 2026.**", "**Update run: 26 July 2026.**")
    README.write_text(text, encoding="utf-8")


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    objects = ""
    if MATSUBARA_DOI not in text:
        objects += (
            f'      {{cat:"latest passive thermal learned inverse-rendering",title:"{MATSUBARA_TITLE}",authors:"Matsubara et al.",year:2026,venue:"VISAPP 2026",url:"https://doi.org/{MATSUBARA_DOI}",key:"Reconstructs moving hidden far-infrared light-source points while jointly recovering unknown relay-environment parameters, combining self-supervised reprojection on real measurements with supervised synthetic learning."}},\n'
            f'      {{cat:"latest passive specular localization automotive",title:"{KOZAWA_TITLE}",authors:"Kozawa et al.",year:2026,venue:"VISAPP 2026",url:"https://doi.org/{KOZAWA_DOI}",key:"Uses distorted pedestrian reflections on curved vehicle bodies, monocular depth and surface normals, and a specular-reflection constraint to estimate hidden pedestrians in 3D from an in-vehicle camera."}},\n'
        )
    if WEI_DOI not in text:
        objects += (
            f'      {{cat:"latest active steady-state polarization speckle scattering memory-effect",title:"{WEI_TITLE}",authors:"Wei et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",url:"https://doi.org/{WEI_DOI}",key:"Uses polarization-encoded spatial multiplexing and robust graph-regularized speckle demultiplexing to recover multiple hidden targets from one exposure across distinct optical-memory-effect regions, reporting 32 dB fidelity and 3.75× field-of-view expansion."}},\n'
        )
    if MINING_DOI not in text:
        objects += (
            f'      {{cat:"latest modality radar lidar fusion autonomous mining nlos perception",title:"{MINING_TITLE}",authors:"Yang et al.",year:2026,venue:"Sensors 2026",url:"https://doi.org/{MINING_DOI}",key:"Blind-Spot Complementary Fusion suppresses multipath artifacts and injects geometrically verified 4D-radar points into 3D-LiDAR blind regions on real mining data, providing existence-level and envelope-level hidden-target risk cues rather than full reconstruction."}},\n'
        )
    if objects:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")

    timeline_sentences = []
    if "vehicle bodies were used as opportunistic mirrors" not in text:
        timeline_sentences.append(
            " Passive thermal NLOS also moved toward joint target-and-environment recovery from far-infrared wall and floor reflections, while curved vehicle bodies were used as opportunistic mirrors for monocular hidden-pedestrian 3D localization."
        )
    if "polarization-encoded spatial multiplexing separated speckles" not in text:
        timeline_sentences.append(
            " Polarization-encoded spatial multiplexing separated speckles from multiple optical-memory-effect regions in a single exposure, expanding steady-state around-corner imaging beyond the conventional memory-effect field of view."
        )
    if "open-pit radar-LiDAR fusion supplied existence-level" not in text:
        timeline_sentences.append(
            " Real open-pit radar-LiDAR fusion supplied existence-level hidden-target risk cues inside LiDAR blind zones after geometric multipath suppression."
        )
    if timeline_sentences:
        pattern = re.compile(
            r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            die("website 2026 timeline block not found")
        text = text[: match.start()] + match.group(1) + match.group(2) + "".join(timeline_sentences) + match.group(3) + text[match.end() :]

    count = len(re.findall(r'\{cat:"', text))
    stat = re.compile(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>')
    text, n = stat.subn(
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        die("website tracked-entry counter not found")
    INDEX.write_text(text, encoding="utf-8")


def patch_active() -> None:
    text = ACTIVE.read_text(encoding="utf-8")
    if "weiPolarizationSpatialMultiplexing2026" not in text:
        table_anchor = "    \\cite{liuPtychographyCorrelographyNLOS2026} & Continuous laser & Polarization-sensitive camera & Speckle correlation / Fourier amplitude & 2D reconstruction\\\\%%%% Table body\n"
        table_row = "    \\cite{weiPolarizationSpatialMultiplexing2026} & Polarization-encoded coherent illumination & Polarization-sensitive camera & Multiplexed speckle correlations & Multi-target 2D reconstruction\\\\%%%% Table body\n"
        text = replace_once(text, table_anchor, table_anchor + table_row, "active table polarization row")

        prose_anchor = "This study provides important design guidelines for practical NLOS systems operating in non-ideal environments.\n"
        prose = r'''

\vspace{0.8mm}
\noindent \textbf{Single-shot imaging beyond the optical memory-effect range.}
Speckle-correlation NLOS imaging is normally limited to one optical memory-effect region, so targets separated beyond that angular range produce mutually decorrelated speckles that cannot be inverted together. Wei~\etal~encode different regions into polarization-dependent channels and formulate a linear spatial-multiplexing model that demultiplexes their speckles from one camera exposure~\cite{weiPolarizationSpatialMultiplexing2026}. Their two-stage recovery combines endmember estimation with truncated-Cauchy non-negative matrix factorization, local-neighborhood weights, and graph-Laplacian regularization. Reflective around-corner and transmissive scattering experiments recover multiple hidden targets across distinct memory-effect regions, reporting 32~dB demultiplexing fidelity and a 3.75-fold field-of-view expansion. This result extends steady-state correlography from single-region hidden imaging toward single-shot multi-target recovery without relay scanning, while remaining distinct from time-resolved transient inversion.
'''
        text = replace_once(text, prose_anchor, prose_anchor + prose, "active polarization prose")
    ACTIVE.write_text(text, encoding="utf-8")


def patch_passive() -> None:
    text = PASSIVE.read_text(encoding="utf-8")
    if "matsubaraJointThermalNLOS2026" not in text:
        prose = r'''
\vspace{0.8mm}
\noindent \textbf{Joint hidden thermal-source and environment recovery.}
Most passive thermal NLOS methods assume that the relay geometry or its transport parameters are calibrated before reconstruction. Matsubara~\etal~instead represent a moving hidden infrared emitter as a set of three-dimensional luminous points and jointly optimize those points with unknown scene parameters from wall- and floor-reflected far-infrared images~\cite{matsubaraJointThermalNLOS2026}. A reprojection loss supplies self-supervision on real measurements, while synthetic scenes provide supervised geometric guidance. This work extends thermal NLOS from reconstructing through a learned but fixed relay model toward inverse rendering in which the hidden target and its environment are recovered together.

\vspace{0.8mm}
\noindent \textbf{Specular vehicle bodies as opportunistic NLOS mirrors.}
Kozawa~\etal~use reflections on curved vehicle bodies to detect pedestrians hidden from an in-vehicle camera and estimate their three-dimensional road positions~\cite{kozawaVehicleReflectionNLOS2026}. A temporal detector first identifies strongly distorted human reflections; monocular depth supplies the reflection point and local surface normal, and a specular-reflection loss constrains the predicted hidden position to the physically valid reflected ray. Unlike diffuse-wall computational periscopy, this setting exploits uncontrolled glossy objects already present in traffic. The output is task-oriented passive NLOS localization rather than a complete hidden image or surface reconstruction.

'''
        anchor = "\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Interferometer}\n"
        text = replace_once(text, anchor, prose + anchor, "passive prose insertion")

        row_anchor = "   \\cite{boger-lombardPassiveOpticalTimeofflight2019}"
        rows = (
            "   \\cite{matsubaraJointThermalNLOS2026} & Hidden-object far-infrared emission & Thermal camera & Reprojection consistency; jointly estimated scene parameters; synthetic supervision & 3D reconstruction\\\\\n"
            "   \\cite{kozawaVehicleReflectionNLOS2026} & Ambient visible illumination & In-vehicle RGB camera & Curved specular vehicle relay; monocular depth and reflection geometry & 3D localization\\\\\n"
        )
        text = replace_once(text, row_anchor, rows + row_anchor, "passive table insertion")
    PASSIVE.write_text(text, encoding="utf-8")


def patch_modalities() -> None:
    text = MODALITIES.read_text(encoding="utf-8")
    if "yangMiningRadarLiDARNLOS2026" not in text:
        anchor = r'''\vspace{0.8mm}
\noindent \textbf{Measured multipath radar recognition and activity understanding.}
'''
        prose = r'''\vspace{0.8mm}
\noindent \textbf{Radar--LiDAR blind-spot fusion in open-pit mines.}
Yang~\etal~studied a deployment-oriented NLOS perception problem in which haul trucks and mining structures fully occlude rear targets from roof-mounted LiDAR~\cite{yangMiningRadarLiDARNLOS2026}. Their Blind-Spot Complementary Fusion framework calibrates 3D LiDAR and 4D mmWave radar, suppresses ground-coupled multipath artifacts, identifies physical LiDAR blind regions, and injects only radar points that pass local-density and spatial-consistency tests. Real measurements at 35~m and 70~m and a fully occluded test-field target show improved cross-modal proximity and nonzero envelope-level evidence where LiDAR alone misses the target. The proposed Volume Recovery Rate is explicitly a proxy for hidden-target existence and coarse envelope coverage, not complete shape reconstruction or semantic detection. By citing HoloRadar as the reconstruction-oriented radar milestone while pursuing training-free safety cues, this work adds a complementary branch in which NLOS sensing is evaluated by downstream blind-zone risk coverage.

'''
        text = replace_once(text, anchor, prose + anchor, "radar-LiDAR fusion prose")
    MODALITIES.write_text(text, encoding="utf-8")


def bib_entries() -> str:
    return r'''
@inproceedings{matsubaraJointThermalNLOS2026,
  author = {Matsubara, Yuma and Sakaue, Fumihiko and Sato, Jun},
  title = {{3D} Reconstruction of Hidden Objects from Simultaneous Recovery of Light Source and Environment},
  booktitle = {Proceedings of the 21st International Conference on Computer Vision Theory and Applications (VISAPP)},
  volume = {3},
  pages = {576--583},
  year = {2026},
  publisher = {SciTePress},
  organization = {INSTICC},
  isbn = {978-989-758-804-4},
  doi = {10.5220/0014435000004084},
  url = {https://doi.org/10.5220/0014435000004084}
}

@inproceedings{kozawaVehicleReflectionNLOS2026,
  author = {Kozawa, Hiroto and Sakaue, Fumihiko and Sato, Jun},
  title = {Estimating the {3D} Position of Hidden Humans Using Reflections on Vehicle Bodies},
  booktitle = {Proceedings of the 21st International Conference on Computer Vision Theory and Applications (VISAPP)},
  volume = {3},
  pages = {568--575},
  year = {2026},
  publisher = {SciTePress},
  organization = {INSTICC},
  isbn = {978-989-758-804-4},
  doi = {10.5220/0014434900004084},
  url = {https://doi.org/10.5220/0014434900004084}
}

@article{weiPolarizationSpatialMultiplexing2026,
  author = {Wei, Yi and Zhao, Yan and Qin, Taotao and Liu, Lingfeng and Bai, Lianfa and Han, Jing and Shi, Yingjie and Guo, Enlai},
  title = {Single-Shot Imaging through Scattering Media and around the Corner beyond the {OME} Range via Polarization-Encoded Spatial Multiplexing},
  journal = {Optics and Lasers in Engineering},
  volume = {200},
  pages = {109602},
  year = {2026},
  publisher = {Elsevier},
  doi = {10.1016/j.optlaseng.2026.109602},
  url = {https://doi.org/10.1016/j.optlaseng.2026.109602}
}

@article{yangMiningRadarLiDARNLOS2026,
  author = {Yang, Jianjian and Zhang, Yuyu and Zheng, Zhiyao and Zhang, Yuyuan},
  title = {Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on {4D} mmWave Radar and {LiDAR} Fusion},
  journal = {Sensors},
  volume = {26},
  number = {14},
  pages = {4615},
  year = {2026},
  publisher = {MDPI},
  doi = {10.3390/s26144615},
  url = {https://doi.org/10.3390/s26144615},
  note = {Published 21 July 2026}
}
'''.strip() + "\n"


def patch_bib() -> None:
    text = BIB.read_text(encoding="utf-8")
    entries = bib_entries()
    blocks = {
        MATSUBARA_DOI: re.search(r"@inproceedings\{matsubaraJointThermalNLOS2026,.*?\n\}", entries, re.DOTALL).group(0),
        KOZAWA_DOI: re.search(r"@inproceedings\{kozawaVehicleReflectionNLOS2026,.*?\n\}", entries, re.DOTALL).group(0),
        WEI_DOI: re.search(r"@article\{weiPolarizationSpatialMultiplexing2026,.*?\n\}", entries, re.DOTALL).group(0),
        MINING_DOI: re.search(r"@article\{yangMiningRadarLiDARNLOS2026,.*?\n\}", entries, re.DOTALL).group(0),
    }
    for doi, block in blocks.items():
        if doi not in text:
            text = text.rstrip() + "\n\n" + block + "\n"
    for doi in blocks:
        if text.lower().count(doi.lower()) != 2:
            die(f"bibliography DOI {doi} should occur in doi and url exactly twice")
    BIB.write_text(text, encoding="utf-8")


def patch_master_and_abstract() -> None:
    text = MASTER.read_text(encoding="utf-8")
    markers = [
        "% 26 July 2026 citation trace: passive far-infrared joint reconstruction and vehicle-reflection hidden-human localization synchronized.\n",
        "% 26 July 2026 citation trace: polarization-multiplexed beyond-memory-effect imaging and radar-LiDAR mining blind-spot perception synchronized.\n",
    ]
    for marker in reversed(markers):
        if marker not in text:
            text = replace_once(text, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "master update marker")
    text = text.replace("through 24 July 2026", "through 26 July 2026")
    text = text.replace("through 25 July 2026", "through 26 July 2026")
    MASTER.write_text(text, encoding="utf-8")

    abstract = ABSTRACT.read_text(encoding="utf-8")
    abstract = abstract.replace("A curated list of 190+ NLOS papers", "A curated list of 210+ NLOS papers")
    abstract = abstract.replace("A curated list of 200+ NLOS papers", "A curated list of 210+ NLOS papers")
    ABSTRACT.write_text(abstract, encoding="utf-8")


def validate() -> None:
    artifacts = {
        "README": README.read_text(encoding="utf-8"),
        "index": INDEX.read_text(encoding="utf-8"),
        "active": ACTIVE.read_text(encoding="utf-8"),
        "passive": PASSIVE.read_text(encoding="utf-8"),
        "modalities": MODALITIES.read_text(encoding="utf-8"),
        "bibliography": BIB.read_text(encoding="utf-8"),
    }
    placements = {
        MATSUBARA_DOI: ("matsubaraJointThermalNLOS2026", "passive", 2),
        KOZAWA_DOI: ("kozawaVehicleReflectionNLOS2026", "passive", 2),
        WEI_DOI: ("weiPolarizationSpatialMultiplexing2026", "active", 2),
        MINING_DOI: ("yangMiningRadarLiDARNLOS2026", "modalities", 1),
    }
    for doi, (key, survey_name, minimum) in placements.items():
        for name in ("README", "index", "bibliography"):
            if doi not in artifacts[name]:
                die(f"{name} is missing {doi}")
        if artifacts[survey_name].count(key) < minimum:
            die(f"{survey_name} does not use {key} enough times")
        if artifacts["bibliography"].count("{" + key + ",") != 1:
            die(f"bibliography key count mismatch for {key}")


def main() -> None:
    patch_readme()
    patch_index()
    patch_active()
    patch_passive()
    patch_modalities()
    patch_bib()
    patch_master_and_abstract()
    validate()
    print("July 2026 NLOS citation-trace integration completed and validated")


if __name__ == "__main__":
    main()
