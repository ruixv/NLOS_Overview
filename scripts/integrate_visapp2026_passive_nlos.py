#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
PASSIVE = ROOT / "article" / "3passive.tex"
ABSTRACT = ROOT / "article" / "0abstract.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

MATSUBARA_TITLE = "3D Reconstruction of Hidden Objects from Simultaneous Recovery of Light Source and Environment"
MATSUBARA_DOI = "10.5220/0014435000004084"
KOZAWA_TITLE = "Estimating the 3D Position of Hidden Humans Using Reflections on Vehicle Bodies"
KOZAWA_DOI = "10.5220/0014434900004084"


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
    if MATSUBARA_DOI not in text:
        rows = (
            f"| 2026 | [{MATSUBARA_TITLE}](https://doi.org/{MATSUBARA_DOI}) — Matsubara et al. | VISAPP 2026 | Uses far-infrared reflections from walls and floors to reconstruct moving hidden luminous objects while jointly estimating unknown scene parameters. Self-supervised reprojection on real measurements is combined with supervised synthetic training, extending passive thermal NLOS from known calibrated environments toward joint scene-and-target recovery. |\n"
            f"| 2026 | [{KOZAWA_TITLE}](https://doi.org/{KOZAWA_DOI}) — Kozawa et al. | VISAPP 2026 | Treats curved vehicle bodies as opportunistic convex mirrors: a video detector finds distorted pedestrian reflections, while monocular depth, surface normals, and a specular-reflection loss recover the hidden pedestrian's 3D road position. This is passive NLOS localization rather than full hidden-scene reconstruction. |\n"
        )
        text = replace_once(text, separator, separator + rows, "README latest-additions table")

    if "Matsubara et al.: joint hidden thermal-source and environment recovery" not in text:
        pattern = re.compile(r"(2026 ──[^\n]*\n)")
        match = pattern.search(text)
        if not match:
            die("README 2026 timeline anchor not found")
        addition = (
            "   │     Matsubara et al.: joint hidden thermal-source and environment recovery combines real-image reprojection with supervised synthetic learning [VISAPP]\n"
            "   │     Kozawa et al.: curved vehicle bodies become opportunistic mirrors for camera-only hidden-pedestrian 3D localization [VISAPP]\n"
        )
        text = text[: match.end()] + addition + text[match.end() :]

    text = text.replace("**Update run: 25 July 2026.**", "**Update run: 26 July 2026.**")
    README.write_text(text, encoding="utf-8")


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    if MATSUBARA_DOI not in text:
        objects = (
            f'      {{cat:"latest passive thermal learned inverse-rendering",title:"{MATSUBARA_TITLE}",authors:"Matsubara et al.",year:2026,venue:"VISAPP 2026",url:"https://doi.org/{MATSUBARA_DOI}",key:"Reconstructs moving hidden far-infrared light-source points while jointly recovering unknown relay-environment parameters, combining self-supervised reprojection on real measurements with supervised synthetic learning."}},\n'
            f'      {{cat:"latest passive specular localization automotive",title:"{KOZAWA_TITLE}",authors:"Kozawa et al.",year:2026,venue:"VISAPP 2026",url:"https://doi.org/{KOZAWA_DOI}",key:"Uses distorted pedestrian reflections on curved vehicle bodies, monocular depth and surface normals, and a specular-reflection constraint to estimate hidden pedestrians in 3D from an in-vehicle camera."}},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")

    if "vehicle bodies as opportunistic mirrors" not in text:
        pattern = re.compile(
            r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            die("website 2026 timeline block not found")
        sentence = (
            " Passive thermal NLOS also moved toward joint target-and-environment recovery from far-infrared wall and floor reflections, while curved vehicle bodies were used as opportunistic mirrors for monocular hidden-pedestrian 3D localization."
        )
        text = text[: match.start()] + match.group(1) + match.group(2) + sentence + match.group(3) + text[match.end() :]

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
'''.strip() + "\n"


def patch_bib() -> None:
    text = BIB.read_text(encoding="utf-8")
    if MATSUBARA_DOI not in text:
        text = text.rstrip() + "\n\n" + bib_entries()
    for doi in (MATSUBARA_DOI, KOZAWA_DOI):
        if text.lower().count(doi.lower()) != 2:
            die(f"bibliography DOI {doi} should occur in doi and url exactly twice")
    BIB.write_text(text, encoding="utf-8")


def patch_master_and_abstract() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 26 July 2026 citation trace: passive far-infrared joint reconstruction and vehicle-reflection hidden-human localization synchronized.\n"
    if marker not in text:
        text = replace_once(text, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "master update marker")
    text = text.replace("through 24 July 2026", "through 26 July 2026")
    MASTER.write_text(text, encoding="utf-8")

    abstract = ABSTRACT.read_text(encoding="utf-8")
    abstract = abstract.replace("A curated list of 190+ NLOS papers", "A curated list of 200+ NLOS papers")
    ABSTRACT.write_text(abstract, encoding="utf-8")


def validate() -> None:
    artifacts = {
        "README": README.read_text(encoding="utf-8"),
        "index": INDEX.read_text(encoding="utf-8"),
        "passive": PASSIVE.read_text(encoding="utf-8"),
        "bibliography": BIB.read_text(encoding="utf-8"),
    }
    for name, text in artifacts.items():
        for doi in (MATSUBARA_DOI, KOZAWA_DOI):
            if doi not in text:
                die(f"{name} is missing {doi}")
    for key in ("matsubaraJointThermalNLOS2026", "kozawaVehicleReflectionNLOS2026"):
        if artifacts["passive"].count(key) < 2:
            die(f"passive survey does not use {key} in prose and table")
        if artifacts["bibliography"].count("{" + key + ",") != 1:
            die(f"bibliography key count mismatch for {key}")


def main() -> None:
    patch_readme()
    patch_index()
    patch_passive()
    patch_bib()
    patch_master_and_abstract()
    validate()
    print("VISAPP 2026 passive NLOS integration completed and validated")


if __name__ == "__main__":
    main()
