#!/usr/bin/env python3
"""Synchronize verified passive soft-shadow, edge-resolved, and commodity-iToF NLOS records.

The update is fail-closed: every replacement uses a unique title/section anchor, and
new paper objects are counted only when they are genuinely absent.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

NIGHT_TITLE = "NIGHT -- Non-Line-of-Sight Imaging from Indirect Time of Flight Data"
NIGHT_DOI = "10.1007/978-3-031-93806-1_12"
SSD_TITLE = "Soft Shadow Diffusion (SSD): Physics-Inspired Learning for 3D Computational Periscopy"
SSD_DOI = "10.1007/978-3-031-72989-8_22"
SNLLS_TITLE = "Towards 3D Computational Persicopy with an Ordinary Camera: A Separable Non-Linear Least Squares Formulation"
SNLLS_DOI = "10.1109/ICASSP48485.2024.10446230"
FISHER_TITLE = "Two-Edge-Resolved 3D Non-Line-of-Sight Imaging: A Fisher Information Equalized Discretization"
FISHER_DOI = "10.1109/ICASSP48485.2024.10446406"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_title_line(text: str, title_fragment: str, replacement: str, label: str) -> str:
    rx = re.compile(rf"(?m)^.*{re.escape(title_fragment)}.*$")
    matches = list(rx.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one title line, found {len(matches)}")
    return rx.sub(lambda _m: replacement, text, count=1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = read(path)

    night_row = (
        f"| 2024 | [{NIGHT_TITLE}](https://doi.org/{NIGHT_DOI}) — Caligiuri et al. | "
        "ECCV 2024 Workshops, Part XIX | Uses an off-the-shelf indirect-ToF sensor and a learned virtual-mirror representation to infer hidden-scene depth without custom direct-ToF hardware; the accompanying synthetic dataset supports the first consumer-iToF NLOS benchmark. |"
    )
    if text.count(NIGHT_DOI) == 0:
        text = replace_title_line(text, "NIGHT -- Non-Line-of-Sight Imaging from Indirect Time of Flight Data", night_row, "README NIGHT row")
    elif text.count(NIGHT_DOI) != 1:
        raise RuntimeError("README NIGHT DOI is duplicated")

    ssd_row = (
        f"| 2024 | [{SSD_TITLE}](https://doi.org/{SSD_DOI}) — Raji, Murray-Bruce | ECCV 2024 | "
        "Decomposes a hidden scene into light-occluding 3D geometry and non-occluding radiosity, yielding a separable nonlinear least-squares inverse; a physics-inspired diffusion network trained only in simulation transfers to real soft-shadow measurements. |"
    )
    if text.count(SSD_DOI) == 0:
        if "Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy" in text:
            text = replace_title_line(text, "Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy", ssd_row, "README SSD row")
        else:
            anchor = night_row
            if text.count(anchor) != 1:
                raise RuntimeError("README NIGHT anchor unavailable for SSD insertion")
            text = text.replace(anchor, anchor + "\n" + ssd_row, 1)
    elif text.count(SSD_DOI) != 1:
        raise RuntimeError("README SSD DOI is duplicated")

    new_rows = []
    if SNLLS_DOI not in text:
        new_rows.append(
            f"| 2024 | [{SNLLS_TITLE}](https://doi.org/{SNLLS_DOI}) — Raji, Murray-Bruce | IEEE ICASSP 2024 | "
            "Introduces the separable nonlinear least-squares formulation that jointly estimates coarse 3D light-occluding geometry and a 2D non-occluding reflectance plane from one ordinary soft-shadow photograph, providing the optimization foundation later used by SSD. |"
        )
    if FISHER_DOI not in text:
        new_rows.append(
            f"| 2024 | [{FISHER_TITLE}](https://doi.org/{FISHER_DOI}) — Czajkowski, Murray-Bruce | IEEE ICASSP 2024 | "
            "Uses Fisher-information-equalized range discretization for two-edge-resolved ordinary-camera NLOS, allocating depth samples according to measurement sensitivity and refining the numerical conditioning of the TERI reconstruction pipeline. |"
        )
    if new_rows:
        if text.count(ssd_row) != 1:
            raise RuntimeError("README SSD anchor unavailable for companion-paper insertion")
        text = text.replace(ssd_row, ssd_row + "\n" + "\n".join(new_rows), 1)

    milestone = (
        "   │     Raji & Murray-Bruce: SNLLS and Soft Shadow Diffusion — ordinary soft shadows jointly reveal hidden 3D occluders and 2D radiosity [ICASSP / ECCV]"
    )
    fisher_milestone = (
        "   │     Czajkowski & Murray-Bruce: Fisher-equalized TERI discretization — depth bins follow edge-resolved measurement sensitivity [ICASSP]"
    )
    if milestone not in text:
        anchor = "   │     Czajkowski and Murray-Bruce: TERI — two doorway edges and one ordinary image enable passive full-colour 3D NLOS [Nature Communications]"
        if text.count(anchor) != 1:
            raise RuntimeError("README 2024 TERI timeline anchor not unique")
        text = text.replace(anchor, anchor + "\n" + fisher_milestone + "\n" + milestone, 1)

    write(path, text)


def replace_homepage_object(text: str, title_fragment: str, replacement: str, label: str) -> str:
    rx = re.compile(rf'(?m)^\s*\{{cat:"[^"]*",title:"{re.escape(title_fragment)}".*?\}},\s*$')
    matches = list(rx.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one paper object, found {len(matches)}")
    return rx.sub(lambda _m: replacement, text, count=1)


def update_homepage() -> None:
    path = ROOT / "index.html"
    text = read(path)

    night_obj = (
        f'      {{cat:"latest active learning consumer itof",title:"{NIGHT_TITLE}",authors:"Caligiuri, Simonetto, Zanuttigh",year:2024,'
        f'venue:"ECCV 2024 Workshops",url:"https://doi.org/{NIGHT_DOI}",key:"Off-the-shelf indirect-ToF capture plus a learned virtual-mirror representation recovers hidden depth and supplies a first consumer-iToF NLOS synthetic benchmark."}},'
    )
    if text.count(NIGHT_DOI) == 0:
        text = replace_homepage_object(text, NIGHT_TITLE, night_obj, "Homepage NIGHT object")
    elif text.count(NIGHT_DOI) != 1:
        raise RuntimeError("Homepage NIGHT DOI is duplicated")

    ssd_old_title = "Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy"
    ssd_obj = (
        f'      {{cat:"latest passive learning ordinary camera soft shadow",title:"{SSD_TITLE}",authors:"Raji and Murray-Bruce",year:2024,'
        f'venue:"ECCV 2024",url:"https://doi.org/{SSD_DOI}",key:"A separable soft-shadow transport model and physics-inspired diffusion network jointly recover hidden 3D occluders and 2D radiosity from one ordinary photograph, with simulation-to-real transfer."}},'
    )
    if text.count(SSD_DOI) == 0:
        text = replace_homepage_object(text, ssd_old_title, ssd_obj, "Homepage SSD object")
    elif text.count(SSD_DOI) != 1:
        raise RuntimeError("Homepage SSD DOI is duplicated")

    additions = []
    if SNLLS_DOI not in text:
        additions.append(
            f'      {{cat:"latest passive optimization ordinary camera soft shadow",title:"{SNLLS_TITLE}",authors:"Raji and Murray-Bruce",year:2024,venue:"IEEE ICASSP 2024",url:"https://doi.org/{SNLLS_DOI}",key:"Separable nonlinear least squares jointly estimates a coarse 3D occluder and a 2D radiosity plane from an ordinary soft-shadow NLOS photograph."}},'
        )
    if FISHER_DOI not in text:
        additions.append(
            f'      {{cat:"latest passive information theory ordinary camera edge",title:"{FISHER_TITLE}",authors:"Czajkowski and Murray-Bruce",year:2024,venue:"IEEE ICASSP 2024",url:"https://doi.org/{FISHER_DOI}",key:"Fisher-information-equalized depth discretization improves the numerical allocation and conditioning of two-edge-resolved ordinary-camera 3D NLOS reconstruction."}},'
        )
    inserted = len(additions)
    if additions:
        anchor = "    const papers=[\n"
        if text.count(anchor) != 1:
            raise RuntimeError("Homepage paper-array anchor not unique")
        text = text.replace(anchor, anchor + "\n".join(additions) + "\n", 1)

    timeline_sentence = (
        " Raji and Murray-Bruce formulated ordinary-camera 3D computational periscopy as separable nonlinear least squares and then introduced Soft Shadow Diffusion for simulation-trained, real-measurement reconstruction of occluding geometry and radiosity. Czajkowski and Murray-Bruce complemented TERI with Fisher-information-equalized depth discretization."
    )
    if timeline_sentence.strip() not in text:
        rx = re.compile(r'(<div class="tl"><div class="year">2024</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.DOTALL)
        matches = list(rx.finditer(text))
        if len(matches) != 1:
            raise RuntimeError("Homepage 2024 timeline block not unique")
        m = matches[0]
        text = text[:m.start()] + m.group(1) + m.group(2) + timeline_sentence + m.group(3) + text[m.end():]

    if inserted:
        rx = re.compile(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>')
        matches = list(rx.finditer(text))
        if len(matches) != 1:
            raise RuntimeError("Homepage tracked-entry count not unique")
        old = int(matches[0].group(1))
        text = rx.sub(f'<div class="stat"><b>{old + inserted}</b><span>tracked latest entries</span></div>', text, count=1)

    write(path, text)


def update_passive_survey() -> None:
    path = ROOT / "article/3passive.tex"
    text = read(path)

    heading = r"\noindent \textbf{From separable soft-shadow inversion to diffusion.}"
    if heading not in text:
        anchor = r"\noindent \textbf{Long-range passive NLOS under severe background.}"
        if text.count(anchor) != 1:
            raise RuntimeError("Passive prose anchor not unique")
        paragraphs = (
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{From separable soft-shadow inversion to diffusion.}\n"
            "Raji and Murray-Bruce generalized ordinary-camera computational periscopy from low-dimensional hidden images to joint three-dimensional occluder geometry and two-dimensional non-occluding radiosity. Their ICASSP formulation separates these unknowns into a nonlinear least-squares block and a conditionally linear block, enabling alternating optimization from a single soft-shadow photograph~\\cite{rajiSNLLSComputationalPersicopy2024}. The subsequent Soft Shadow Diffusion framework retains this transport decomposition but learns a physics-inspired solver from simulation, transferring to unseen simulated classes and real measurements while remaining robust to ambient illumination and noise~\\cite{rajiSoftShadowDiffusion2024}. Together, these works provide the methodological bridge from computational periscopy to the later multimodal MDUNet architecture.\n\n"
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Fisher-equalized edge-resolved depth sampling.}\n"
            "The two-edge-resolved doorway camera gains depth information because orthogonal penumbrae encode complementary hidden coordinates, but uniform range discretization wastes variables where the measurement is insensitive. Czajkowski and Murray-Bruce used Fisher information to equalize the discretization of the hidden range axis~\\cite{czajkowskiFisherTERI2024}, providing a compact conditioning-oriented companion to their full-colour TERI system. This analysis clarifies how computational-aperture geometry should determine the numerical representation rather than only the forward model.\n\n"
        )
        text = text.replace(anchor, paragraphs + anchor, 1)

    if "rajiSNLLSComputationalPersicopy2024" not in text.split(r"\begin{table*}", 1)[-1]:
        table_anchor = r"    \cite{rajiMDUNet2026}"
        if text.count(table_anchor) != 1:
            raise RuntimeError("Passive table MDUNet anchor not unique")
        rows = (
            "    \\cite{rajiSNLLSComputationalPersicopy2024,rajiSoftShadowDiffusion2024} & Ambient/incoherent illumination & Conventional camera & Soft-shadow intensity with separable occluder/radiosity model & Joint 3D geometry and 2D reconstruction\\\\%%%% Table body\n"
            "    \\cite{czajkowskiFisherTERI2024} & Ambient light & Conventional camera & Two orthogonal edge penumbrae with Fisher-equalized depth discretization & 3D reconstruction\\\\%%%% Table body\n"
        )
        text = text.replace(table_anchor, rows + table_anchor, 1)

    write(path, text)


def update_master_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = read(path)
    marker = "% 22 July 2026 citation trace corrects NIGHT and Soft Shadow Diffusion to final venues and integrates SNLLS and Fisher-equalized passive 3D computational periscopy."
    if marker not in text:
        anchor = r"\input{article/3passive.tex}"
        if text.count(anchor) != 1:
            raise RuntimeError("Master passive-section anchor not unique")
        text = text.replace(anchor, marker + "\n" + anchor, 1)
    write(path, text)


def validate() -> None:
    readme = read(ROOT / "README.md")
    home = read(ROOT / "index.html")
    active = read(ROOT / "article/2active.tex")
    passive = read(ROOT / "article/3passive.tex")
    master = read(ROOT / "bare_jrnl.tex")
    for doi in (NIGHT_DOI, SSD_DOI, SNLLS_DOI, FISHER_DOI):
        if readme.count(doi) != 1:
            raise RuntimeError(f"README DOI validation failed for {doi}")
        if home.count(doi) != 1:
            raise RuntimeError(f"Homepage DOI validation failed for {doi}")
    if "https://arxiv.org/abs/2403.19376" in readme or "https://arxiv.org/abs/2601.12257" in readme:
        raise RuntimeError("README still exposes a corrected preprint link")
    if "https://arxiv.org/abs/2403.19376" in home or "https://arxiv.org/abs/2601.12257" in home:
        raise RuntimeError("Homepage still exposes a corrected preprint link")
    if active.count("caligiuriNIGHT2024") < 2:
        raise RuntimeError("NIGHT must be cited in the active table and prose")
    for key in ("rajiSNLLSComputationalPersicopy2024", "rajiSoftShadowDiffusion2024", "czajkowskiFisherTERI2024"):
        if passive.count(key) < 2:
            raise RuntimeError(f"Passive survey integration incomplete for {key}")
    if "22 July 2026 citation trace corrects NIGHT" not in master:
        raise RuntimeError("Master integration marker missing")


def main() -> None:
    update_readme()
    update_homepage()
    update_passive_survey()
    update_master_tex()
    validate()
    print("Synchronized final venues and passive/iToF citation-trace additions.")


if __name__ == "__main__":
    main()
