#!/usr/bin/env python3
"""Synchronize the verified IEEE ICEE 2025 record for the NIR raster-scan paper.

The paper was uploaded to arXiv in July 2026, but its DOI resolves to a peer-reviewed
2025 IEEE conference publication. This script is deliberately fail-closed: it only
updates unique, known anchors and validates all public artifacts before returning.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength"
TITLE_RE = re.compile(
    r"Non-Line-of-Sight imaging using raster scanning at NIR wavelength",
    re.IGNORECASE,
)
DOI = "10.1109/ICEE67339.2025.11213924"
DOI_URL = f"https://doi.org/{DOI}"
KEY = "roueinfarNIRRaster2025"
SUPPLEMENT = ROOT / "egbib_20260722_nir_final_venue_updates.bib"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, pattern: str | re.Pattern[str], replacement: str, label: str, flags: int = 0) -> str:
    rx = re.compile(pattern, flags) if isinstance(pattern, str) else pattern
    matches = list(rx.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {len(matches)}")
    return rx.sub(lambda _m: replacement, text, count=1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = read(path)
    old_row = re.compile(
        r"^\|\s*2026\s*\|\s*\[Non-Line-of-Sight imaging using raster scanning at NIR wavelength\]"
        r"\(https://arxiv\.org/abs/2607\.04183\)\s*—\s*Roueinfar, Salmanian\s*\|\s*arXiv 2026\s*\|"
        r"\s*Demonstrates a low-cost 808 nm NIR raster-scanning active NLOS setup with pan-tilt illumination and NIR-camera capture over three hidden targets; useful as a simple hardware/acquisition baseline rather than a new inverse-model frontier\.\s*\|$",
        re.MULTILINE,
    )
    new_row = (
        f"| 2025 | [{TITLE}]({DOI_URL}) — Roueinfar, Salmanian | IEEE ICEE 2025 | "
        "Uses a 500 mW, 808 nm laser on a pan-tilt raster scanner and an NIR camera to recover three hidden targets through steady-state three-bounce transport. It is a low-cost acquisition baseline rather than a new inverse-model frontier; the repository uses the final IEEE conference record instead of the later arXiv upload. |"
    )
    if DOI not in text:
        text = replace_once(text, old_row, new_row, "README NIR arXiv row")
    elif text.count(DOI) != 1:
        raise RuntimeError(f"README DOI count is {text.count(DOI)}, expected one")

    if "**Update run: 21 July 2026.**" in text:
        text = text.replace("**Update run: 21 July 2026.**", "**Update run: 22 July 2026.**", 1)
    elif "**Update run: 22 July 2026.**" not in text:
        raise RuntimeError("README update-run date anchor not found")

    milestone = "2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning [IEEE ICEE]"
    if milestone not in text:
        anchor = "   │     Chen et al.: learned NLOS feature embeddings — a shared physics-aware representation for reconstruction, detection, and recognition [SIGGRAPH Asia / TOG]"
        if text.count(anchor) != 1:
            raise RuntimeError(f"README timeline anchor count is {text.count(anchor)}, expected one")
        text = text.replace(anchor, anchor + "\n   │\n" + milestone, 1)

    write(path, text)


def update_homepage() -> None:
    path = ROOT / "index.html"
    text = read(path)

    object_rx = re.compile(
        r'(?m)^\s*\{cat:"[^"]*",title:"Non-Line-of-Sight imaging using raster scanning at NIR wavelength",'
        r'authors:"[^"]*",year:2026,venue:"arXiv 2026",url:"https://arxiv\.org/abs/2607\.04183",key:"[^"]*"\},\s*$'
    )
    replacement = (
        '      {cat:"latest active steady-state nir raster scanning conventional camera",'
        f'title:"{TITLE}",authors:"Roueinfar and Salmanian",year:2025,venue:"IEEE ICEE 2025",'
        f'url:"{DOI_URL}",key:"Uses a 500 mW 808 nm laser, pan-tilt relay-wall raster scanning, and an NIR camera for low-cost steady-state three-bounce imaging; final IEEE conference metadata replaces the later arXiv upload."}},'
    )
    if DOI not in text:
        text = replace_once(text, object_rx, replacement, "homepage NIR paper object")
    elif text.count(DOI) != 1:
        raise RuntimeError(f"Homepage DOI count is {text.count(DOI)}, expected one")

    timeline_sentence = (
        " Roueinfar and Salmanian provided a low-cost 808 nm steady-state raster-scanning baseline with pan-tilt illumination and NIR-camera capture, formally published at IEEE ICEE 2025."
    )
    if timeline_sentence.strip() not in text:
        block_rx = re.compile(
            r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        matches = list(block_rx.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"Homepage 2025 timeline block count is {len(matches)}, expected one")
        m = matches[0]
        text = text[: m.start()] + m.group(1) + m.group(2) + timeline_sentence + m.group(3) + text[m.end() :]

    if "21 July 2026" in text:
        text = text.replace("21 July 2026", "22 July 2026")
    if "22 July 2026" not in text:
        raise RuntimeError("Homepage date was not updated")

    write(path, text)


def update_active_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = read(path)

    old_cites = r"\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020}"
    new_cites = rf"\cite{{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,{KEY}}}"
    if KEY not in text:
        if text.count(old_cites) != 1:
            raise RuntimeError(f"Active-table steady-state citation anchor count is {text.count(old_cites)}, expected one")
        text = text.replace(old_cites, new_cites, 1)

    heading = r"\noindent \textbf{Low-cost NIR steady-state raster scanning.}"
    if heading not in text:
        anchor = (
            "Due to the lack of distance information, it is not easy to complete high-precision three-dimensional reconstruction only using conventional cameras."
        )
        if text.count(anchor) != 1:
            raise RuntimeError(f"Active-survey conventional-camera anchor count is {text.count(anchor)}, expected one")
        paragraph = (
            "\n\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Low-cost NIR steady-state raster scanning.}\n"
            "Roueinfar and Salmanian demonstrated a deliberately simple active NLOS acquisition baseline using a 500~mW, 808~nm laser mounted on a pan--tilt unit to raster scan the relay wall and a conventional NIR camera to record the three-bounce steady-state response~\\cite{roueinfarNIRRaster2025}. Experiments on three hidden targets quantify image error with MSE and RMSE. The method does not recover transient depth or introduce a new inverse operator, but it shows how near-infrared illumination and commodity spatial capture can lower hardware complexity. Although uploaded to arXiv in July 2026, the work had already appeared in the 2025 IEEE International Conference on Electrical Engineering; the survey therefore cites the final conference version."
        )
        text = text.replace(anchor, anchor + paragraph, 1)

    write(path, text)


def update_master_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = read(path)
    marker = "% 22 July 2026 venue audit corrects the NIR raster-scanning paper to IEEE ICEE 2025 and integrates it into the active steady-state discussion."
    if marker not in text:
        anchor = r"\input{article/2active.tex}"
        if text.count(anchor) != 1:
            raise RuntimeError(f"bare_jrnl active-section anchor count is {text.count(anchor)}, expected one")
        text = text.replace(anchor, marker + "\n" + anchor, 1)
    write(path, text)


def update_bibliography_source() -> None:
    canonical = f"""@inproceedings{{{KEY},
  author = {{Roueinfar, Mohammad and Salmanian, Mahdi}},
  title = {{{{Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength}}}},
  booktitle = {{2025 33rd International Conference on Electrical Engineering (ICEE)}},
  year = {{2025}},
  pages = {{1--5}},
  doi = {{{DOI}}},
  url = {{{DOI_URL}}},
  publisher = {{IEEE}}
}}
"""
    # The consolidated file is generated; source supplements are authoritative.
    matching_sources: list[Path] = []
    for path in sorted(ROOT.glob("egbib*.bib")):
        if path.name == "egbib_merged_20260711.bib":
            continue
        text = path.read_text(encoding="utf-8-sig")
        if DOI.lower() in text.lower() or "2607.04183" in text or TITLE_RE.search(text):
            matching_sources.append(path)

    if len(matching_sources) > 1:
        names = ", ".join(p.name for p in matching_sources)
        raise RuntimeError(f"Multiple source BibTeX records match the NIR paper: {names}")
    if len(matching_sources) == 1:
        source = matching_sources[0]
        text = source.read_text(encoding="utf-8-sig")
        # Fail closed instead of trying to parse nested BibTeX braces in place.
        if DOI.lower() not in text.lower() or "booktitle" not in text.lower() or "2025" not in text:
            raise RuntimeError(
                f"An older source record exists in {source.name}; replace it manually rather than risking a malformed BibTeX edit"
            )
        return

    if SUPPLEMENT.exists():
        existing = SUPPLEMENT.read_text(encoding="utf-8")
        if existing.strip() != canonical.strip():
            raise RuntimeError(f"Existing {SUPPLEMENT.name} does not match the verified canonical record")
    else:
        SUPPLEMENT.write_text(canonical, encoding="utf-8")


def validate_sources() -> None:
    readme = read(ROOT / "README.md")
    homepage = read(ROOT / "index.html")
    active = read(ROOT / "article/2active.tex")
    master = read(ROOT / "bare_jrnl.tex")

    if readme.count(DOI) != 1 or "| IEEE ICEE 2025 |" not in readme:
        raise RuntimeError("README final-venue validation failed")
    if "https://arxiv.org/abs/2607.04183" in readme:
        raise RuntimeError("README still exposes the arXiv link for the corrected entry")
    if homepage.count(DOI) != 1 or 'venue:"IEEE ICEE 2025"' not in homepage:
        raise RuntimeError("Homepage final-venue validation failed")
    if "https://arxiv.org/abs/2607.04183" in homepage:
        raise RuntimeError("Homepage still exposes the arXiv link for the corrected entry")
    if active.count(KEY) < 2:
        raise RuntimeError("Active survey must cite the corrected paper in both table and prose")
    if "22 July 2026 venue audit" not in master:
        raise RuntimeError("Master survey integration marker is missing")
    if "**Update run: 22 July 2026.**" not in readme or "22 July 2026" not in homepage:
        raise RuntimeError("Public update dates are inconsistent")


def main() -> None:
    update_readme()
    update_homepage()
    update_active_survey()
    update_master_tex()
    update_bibliography_source()
    validate_sources()
    print("Synchronized the NIR raster-scanning paper to its verified IEEE ICEE 2025 record.")


if __name__ == "__main__":
    main()
