#!/usr/bin/env python3
"""Synchronize polarization differential correlography NLOS across artifacts.

The update is fail-closed: every replacement requires a unique structural
anchor, partial prior integrations are rejected, and all edited artifacts are
validated before the script exits successfully.
"""
from __future__ import annotations

from pathlib import Path
import re
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.3788/COL202523.081104"
KEY = "liuPolarizationDifferentialCorrelography2025"
MARKER = "% 23 July 2026 citation trace: polarization differential correlography NLOS integrated."


def load(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def save(name: str, text: str) -> None:
    (ROOT / name).write_text(text, encoding="utf-8")


def sub_once(pattern: str, repl: str | Callable[[re.Match[str]], str], text: str,
             label: str, flags: int = 0) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return out


def already_integrated() -> bool:
    if DOI not in load("README.md"):
        return False
    checks = {
        "README.md": DOI,
        "index.html": DOI,
        "article/2active.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    missing = [name for name, needle in checks.items() if needle not in load(name)]
    if missing:
        raise RuntimeError(
            "Partial PDC-NLOS integration detected; refusing unsafe repair: "
            + ", ".join(missing)
        )
    return True


def update_readme() -> None:
    name = "README.md"
    text = load(name)
    if DOI in text:
        raise RuntimeError("README already contains PDC-NLOS")

    text = sub_once(
        r"\*\*Update run: 22 July 2026\.\*\*",
        "**Update run: 23 July 2026.**",
        text,
        "README update date",
    )

    row = (
        "| 2025 | [High-resolution non-line-of-sight imaging via polarization differential "
        "correlography](https://doi.org/10.3788/COL202523.081104) — Liu et al. | "
        "Chinese Optics Letters 2025 | Introduces PDC-NLOS, a single-shot steady-state "
        "system that encodes hidden objects with independently polarized laser speckles and "
        "uses polarization differencing before correlographic phase retrieval. It removes "
        "mechanical relay scanning, improves perturbation robustness, and demonstrates "
        "millimeter-level resolution with an average reported SSIM of about 0.76. |\n"
    )
    text = sub_once(
        r"(?m)^(\|------\|-------\|----------------\|----------------\|\s*)$",
        lambda m: m.group(1) + "\n" + row.rstrip("\n"),
        text,
        "README latest-additions header",
    )

    anchor = (
        "   │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D blur-kernel model "
        "and correlation resampling recover 2-cm detail at 5 fps from a 16×16 detector "
        "[Optics and Lasers in Engineering]"
    )
    milestone = (
        "   │     Liu et al.: polarization differential correlography — single-shot polarized "
        "speckle encoding removes mechanical scanning and achieves millimeter-scale steady-state "
        "NLOS reconstruction [Chinese Optics Letters]"
    )
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one README 2025 milestone anchor, found {text.count(anchor)}")
    text = text.replace(anchor, anchor + "\n" + milestone, 1)
    save(name, text)


def update_index() -> None:
    name = "index.html"
    text = load(name)
    if DOI in text:
        raise RuntimeError("Homepage already contains PDC-NLOS")

    text = sub_once(
        r'<div class="stat"><b>184</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>185</b><span>tracked latest entries</span></div>',
        text,
        "homepage tracked-entry count",
    )
    text = sub_once(
        r"Updated 22 July 2026 · 190\+ papers",
        "Updated 23 July 2026 · 190+ papers",
        text,
        "homepage hero date",
    )
    text = sub_once(
        r"Last updated: 22 July 2026",
        "Last updated: 23 July 2026",
        text,
        "homepage footer date",
    )

    paper = (
        '      {cat:"latest active steady-state polarization speckle correlography single-shot",'
        'title:"High-resolution non-line-of-sight imaging via polarization differential correlography",'
        'authors:"Liu et al.",year:2025,venue:"Chinese Optics Letters 2025",'
        'url:"https://doi.org/10.3788/COL202523.081104",'
        'key:"PDC-NLOS uses independently polarized speckle illumination and polarization differencing '
        'for single-shot steady-state correlographic reconstruction, avoiding mechanical scanning '
        'and demonstrating millimeter-level resolution with an average reported SSIM near 0.76."},\n'
    )
    text = sub_once(
        r"(?m)^(\s*const papers=\[\s*)$",
        lambda m: m.group(1) + "\n" + paper.rstrip("\n"),
        text,
        "homepage paper array",
    )

    pattern = r'(<div class="tl"><div class="year">2025</div>.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError("Could not locate homepage 2025 timeline")
    addition = (
        " Polarization differential correlography additionally replaced mechanical relay scanning "
        "with single-shot polarized-speckle encoding, adding a millimeter-resolution steady-state branch."
    )
    if "Polarization differential correlography additionally" in match.group(2):
        raise RuntimeError("Homepage 2025 timeline already contains PDC-NLOS")
    replacement = match.group(1) + match.group(2).rstrip() + addition + match.group(3)
    text = text[:match.start()] + replacement + text[match.end():]
    save(name, text)


def update_active_section() -> None:
    name = "article/2active.tex"
    text = load(name)
    if KEY in text:
        raise RuntimeError("Active survey already cites PDC-NLOS")

    old_cites = (
        r"\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,"
        r"roueinfarNIRRaster2025}"
    )
    new_cites = (
        r"\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,"
        r"roueinfarNIRRaster2025,liuPolarizationDifferentialCorrelography2025}"
    )
    if text.count(old_cites) != 1:
        raise RuntimeError(f"Expected one active-table steady-state citation anchor, found {text.count(old_cites)}")
    text = text.replace(old_cites, new_cites, 1)

    anchor = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Low-cost NIR steady-state raster scanning.}\n"
        "Roueinfar and Salmanian demonstrated a deliberately simple active NLOS acquisition baseline "
        "using a 500~mW, 808~nm laser mounted on a pan--tilt unit to raster scan the relay wall and a "
        "conventional NIR camera to record the three-bounce steady-state response~"
        "\\cite{roueinfarNIRRaster2025}. Experiments on three hidden targets quantify image error with "
        "MSE and RMSE. The method does not recover transient depth or introduce a new inverse operator, "
        "but it shows how near-infrared illumination and commodity spatial capture can lower hardware "
        "complexity. Although uploaded to arXiv in July 2026, the work had already appeared in the 2025 "
        "IEEE International Conference on Electrical Engineering; the survey therefore cites the final "
        "conference version."
    )
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one steady-state NIR survey anchor, found {text.count(anchor)}")

    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Single-shot polarization differential correlography.}\n"
        "Liu~\\etal~introduced PDC-NLOS, a steady-state active system that illuminates the relay wall "
        "with independently polarized laser speckles and forms a polarization-difference correlogram "
        "before phase retrieval~\\cite{liuPolarizationDifferentialCorrelography2025}. Polarization "
        "modulation replaces repeated mechanical scanning, while differential speckle statistics add "
        "redundancy against vibration and coloured perturbations. Experiments on horizontal and vertical "
        "stripe targets demonstrate millimeter-level resolution, and the reported average SSIM of about "
        "0.76 improves on the authors' earlier chromato-axial single-shot correlography baseline. This "
        "work connects steady-state NLOS, speckle correlation, and polarization coding, providing a "
        "low-complexity high-resolution alternative to transient time-of-flight inversion."
    )
    text = text.replace(anchor, anchor + paragraph, 1)
    save(name, text)


def update_master() -> None:
    name = "bare_jrnl.tex"
    text = load(name)
    if MARKER in text:
        raise RuntimeError("Master survey already contains PDC-NLOS marker")
    text = sub_once(
        r"(?m)^%% bare_jrnl\.tex\s*$",
        "%% bare_jrnl.tex\n" + MARKER,
        text,
        "master survey header",
    )
    text = sub_once(
        r"extends coverage to include significant advances from 2022 through 22 July 2026",
        "extends coverage to include significant advances from 2022 through 23 July 2026",
        text,
        "survey coverage date",
    )
    save(name, text)


def validate() -> None:
    checks = {
        "README.md": DOI,
        "index.html": DOI,
        "article/2active.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    for name, needle in checks.items():
        count = load(name).count(needle)
        if count != 1:
            raise RuntimeError(f"Postcondition failed for {name}: expected one {needle!r}, found {count}")
    if '<b>185</b><span>tracked latest entries</span>' not in load("index.html"):
        raise RuntimeError("Homepage tracked-entry count was not updated to 185")
    if "through 23 July 2026" not in load("bare_jrnl.tex"):
        raise RuntimeError("Survey coverage date was not synchronized to 23 July 2026")
    if "**Update run: 23 July 2026.**" not in load("README.md"):
        raise RuntimeError("README update date was not synchronized")


def main() -> None:
    if already_integrated():
        print("PDC-NLOS is already fully integrated; no changes needed.")
        return
    update_readme()
    update_index()
    update_active_section()
    update_master()
    validate()
    print("Integrated PDC-NLOS across README, homepage, active survey, and master metadata.")


if __name__ == "__main__":
    main()
