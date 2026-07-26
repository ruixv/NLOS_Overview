#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

MULTISPECTRAL_TITLE = "Multispectral imaging through scattering media and around corners via spectral component separation"
MULTISPECTRAL_DOI = "10.1364/OE.541410"
POLARIZATION_TITLE = "Single-shot multitarget imaging beyond the OME range around the corner through polarization component extraction"
POLARIZATION_DOI = "10.1117/12.3093680"


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
    if MULTISPECTRAL_DOI not in text:
        rows += (
            f"| 2024 | [{MULTISPECTRAL_TITLE}](https://doi.org/{MULTISPECTRAL_DOI}) — Wei et al. | Optics Express 2024 | Builds a multispectral-speckle simplex from wavelength-decorrelated components and combines spectral intensity modulation, wavelength-count estimation, vertex-component initialization, constrained non-negative matrix factorization, and phase retrieval. Experiments recover up to six spectral channels and validate multispectral hidden-object imaging around a diffuse corner. |\n"
        )
    if POLARIZATION_DOI not in text:
        rows += (
            f"| 2025 | [{POLARIZATION_TITLE}](https://doi.org/{POLARIZATION_DOI}) — Zhao et al. | Proc. SPIE / OYSS 2025 | Introduces polarization-component extraction for one-shot recovery of multiple around-corner targets located in distinct optical-memory-effect regions. This short conference precursor establishes the polarization-separation idea later generalized into the 2026 spatial-multiplexing journal system. |\n"
        )
    if rows:
        text = replace_once(text, separator, separator + rows, "README latest-additions table")

    if "Wei et al.: multispectral speckle component separation" not in text:
        anchor = "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
        addition = (
            "   │     Wei et al.: multispectral speckle component separation recovers up to six wavelength channels and validates spectral hidden-object imaging around corners [Optics Express]\n"
        )
        text = replace_once(text, anchor, anchor + addition, "README 2024 timeline")
    if "Zhao et al.: polarization-component extraction" not in text:
        anchor = "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics move steady-state NLOS toward inexpensive white-light and ambient-light operation [Applied Optics / Optics Communications]\n"
        addition = (
            "     │     Zhao et al.: polarization-component extraction separates multiple around-corner targets beyond one optical memory-effect region in a single exposure [Proc. SPIE / OYSS]\n"
        )
        text = replace_once(text, anchor, anchor + addition, "README 2025 timeline")

    text = text.replace("**Update run: 25 July 2026.**", "**Update run: 26 July 2026.**")
    README.write_text(text, encoding="utf-8")


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    objects = ""
    if MULTISPECTRAL_DOI not in text:
        objects += (
            f'      {{cat:"latest active steady-state multispectral speckle scattering around-corner",title:"{MULTISPECTRAL_TITLE}",authors:"Wei et al.",year:2024,venue:"Optics Express 2024",url:"https://doi.org/{MULTISPECTRAL_DOI}",key:"Constructs a wavelength-component simplex and combines spectral modulation, channel-count estimation, vertex initialization, constrained NMF, and phase retrieval to recover as many as six spectral channels, including measured hidden multispectral objects around a diffuse corner."}},\n'
        )
    if POLARIZATION_DOI not in text:
        objects += (
            f'      {{cat:"latest active steady-state polarization speckle memory-effect multi-target",title:"{POLARIZATION_TITLE}",authors:"Zhao et al.",year:2025,venue:"Proc. SPIE / OYSS 2025",url:"https://doi.org/{POLARIZATION_DOI}",key:"Uses polarization-component extraction for single-shot recovery of multiple around-corner targets in distinct optical-memory-effect regions; this conference precursor motivates the later polarization-encoded spatial-multiplexing journal method."}},\n'
        )
    if objects:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")

    year_sentences = {
        2024: (
            " Multispectral speckle component separation recovered up to six wavelength channels and demonstrated spectral hidden-object reconstruction around a diffuse corner."
        ),
        2025: (
            " Polarization-component extraction then separated multiple around-corner targets beyond one optical-memory-effect region in a single exposure, forming the conference precursor to polarization-encoded spatial multiplexing."
        ),
    }
    markers = {
        2024: "Multispectral speckle component separation recovered up to six wavelength channels",
        2025: "Polarization-component extraction then separated multiple around-corner targets",
    }
    for year, sentence in year_sentences.items():
        if markers[year] in text:
            continue
        pattern = re.compile(
            rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            die(f"website {year} timeline block not found")
        text = (
            text[: match.start()]
            + match.group(1)
            + match.group(2)
            + sentence
            + match.group(3)
            + text[match.end() :]
        )

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
    if "weiMultispectralComponentSeparation2024" not in text:
        table_anchor = "    \\cite{weiPolarizationSpatialMultiplexing2026} & Polarization-encoded coherent illumination & Polarization-sensitive camera & Multiplexed speckle correlations & Multi-target 2D reconstruction\\\\%%%% Table body\n"
        rows = (
            "    \\cite{weiMultispectralComponentSeparation2024} & Spectrally modulated broadband illumination & Camera & Spectral speckle separation and phase retrieval & Multispectral 2D reconstruction\\\\%%%% Table body\n"
            "    \\cite{zhaoPolarizationComponentExtraction2025} & Polarization-multiplexed illumination & Polarization-sensitive camera & Polarization-component extraction & Multi-target 2D reconstruction\\\\%%%% Table body\n"
        )
        text = replace_once(text, table_anchor, rows + table_anchor, "active table spectral-polarization rows")

        prose_anchor = r'''\vspace{0.8mm}
\noindent \textbf{Single-shot imaging beyond the optical memory-effect range.}
'''
        prose = r'''\vspace{0.8mm}
\noindent \textbf{Spectral and polarization component separation for steady-state NLOS.}
Wei~\etal~extend speckle-correlation imaging from grayscale recovery to multispectral hidden scenes by treating wavelength-decorrelated speckles as the vertices of a multispectral simplex~\cite{weiMultispectralComponentSeparation2024}. Random spectral-intensity modulation, wavelength-count estimation, vertex-component initialization, constrained non-negative matrix factorization, and phase retrieval separate and reconstruct as many as six wavelength channels; reflective experiments verify multispectral imaging around a diffuse corner. Zhao~\etal~subsequently replace spectral diversity with polarization-component extraction to recover multiple targets that occupy distinct optical memory-effect regions from one exposure~\cite{zhaoPolarizationComponentExtraction2025}. This conference precursor establishes the channel-separation principle later generalized by polarization-encoded spatial multiplexing, connecting spectral-content recovery and beyond-memory-effect field-of-view expansion within a common steady-state speckle framework.

'''
        text = replace_once(text, prose_anchor, prose + prose_anchor, "active spectral-polarization prose")
    ACTIVE.write_text(text, encoding="utf-8")


def bib_entries() -> str:
    return r'''
@article{weiMultispectralComponentSeparation2024,
  author = {Wei, Yi and Zhao, Yan and Liu, Lingfeng and Hu, Jinfei and Bai, Lianfa and Guo, Enlai and Han, Jing},
  title = {Multispectral Imaging through Scattering Media and around Corners via Spectral Component Separation},
  journal = {Optics Express},
  volume = {32},
  number = {27},
  pages = {48786--48802},
  year = {2024},
  publisher = {Optica Publishing Group},
  doi = {10.1364/OE.541410},
  url = {https://doi.org/10.1364/OE.541410},
  note = {Published 23 December 2024}
}

@inproceedings{zhaoPolarizationComponentExtraction2025,
  author = {Zhao, Yan and Wei, Yi and Shi, Yingjie and Qin, Taotao and Bai, Lianfa and Han, Jing and Guo, Enlai},
  title = {Single-Shot Multitarget Imaging beyond the {OME} Range around the Corner through Polarization Component Extraction},
  booktitle = {Proceedings of SPIE: 8th Optics Young Scientist Summit (OYSS 2025)},
  volume = {13966},
  pages = {139660V},
  year = {2025},
  publisher = {SPIE},
  doi = {10.1117/12.3093680},
  url = {https://doi.org/10.1117/12.3093680}
}
'''.strip() + "\n"


def patch_bib() -> None:
    text = BIB.read_text(encoding="utf-8")
    entries = bib_entries()
    blocks = {
        MULTISPECTRAL_DOI: re.search(
            r"@article\{weiMultispectralComponentSeparation2024,.*?\n\}", entries, re.DOTALL
        ).group(0),
        POLARIZATION_DOI: re.search(
            r"@inproceedings\{zhaoPolarizationComponentExtraction2025,.*?\n\}", entries, re.DOTALL
        ).group(0),
    }
    for doi, block in blocks.items():
        if doi not in text:
            text = text.rstrip() + "\n\n" + block + "\n"
    for doi in blocks:
        if text.lower().count(doi.lower()) != 2:
            die(f"bibliography DOI {doi} should occur in doi and url exactly twice")
    BIB.write_text(text, encoding="utf-8")


def patch_master() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 26 July 2026 citation trace: multispectral and polarization-component separation lineage for steady-state around-corner imaging synchronized.\n"
    if marker not in text:
        text = replace_once(text, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "master update marker")
    MASTER.write_text(text, encoding="utf-8")


def validate() -> None:
    artifacts = {
        "README": README.read_text(encoding="utf-8"),
        "index": INDEX.read_text(encoding="utf-8"),
        "active": ACTIVE.read_text(encoding="utf-8"),
        "bibliography": BIB.read_text(encoding="utf-8"),
    }
    placements = {
        MULTISPECTRAL_DOI: ("weiMultispectralComponentSeparation2024", 2),
        POLARIZATION_DOI: ("zhaoPolarizationComponentExtraction2025", 2),
    }
    for doi, (key, minimum) in placements.items():
        for name in ("README", "index", "bibliography"):
            if doi not in artifacts[name]:
                die(f"{name} is missing {doi}")
        if artifacts["active"].count(key) < minimum:
            die(f"active survey does not use {key} enough times")
        if artifacts["bibliography"].count("{" + key + ",") != 1:
            die(f"bibliography key count mismatch for {key}")


def main() -> None:
    patch_readme()
    patch_index()
    patch_active()
    patch_bib()
    patch_master()
    validate()
    print("Spectral and polarization-component NLOS lineage integration completed and validated")


if __name__ == "__main__":
    main()
