#!/usr/bin/env python3
"""Cross-artifact validation for the coherent FMCW NLOS update."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOIS = (
    "10.1103/PhysRevLett.132.233802",
    "10.1002/lpor.202401250",
    "10.1109/JLT.2024.3523206",
)
KEYS = (
    "huangCombCalibratedNLOS2024",
    "yeCombCalibratedFMCWTracking2025",
    "chenVectorEnhancedFMCWNLOS2025",
)


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    readme = text("README.md")
    index = text("index.html")
    active = text("article/2active.tex")
    bib = text("egbib_merged_20260711.bib")
    master = text("bare_jrnl.tex")

    for doi in DOIS:
        if readme.count(doi) != 1:
            raise RuntimeError(f"README DOI coverage error: {doi}")
        if index.count(doi) != 1:
            raise RuntimeError(f"website DOI coverage error: {doi}")
        if bib.lower().count(("doi = {" + doi + "}").lower()) != 1:
            raise RuntimeError(f"bibliography DOI coverage error: {doi}")

    for key in KEYS:
        if active.count(key) < 2:
            raise RuntimeError(f"active survey must cite {key} in the table and prose")
        if bib.count("{" + key + ",") != 1:
            raise RuntimeError(f"bibliography key coverage error: {key}")

    coherent_lines = [line for line in active.splitlines() if "Coherent FMCW interferometer" in line]
    if len(coherent_lines) != 1:
        raise RuntimeError(f"expected one coherent-FMCW table row, found {len(coherent_lines)}")
    for key in (*KEYS, "liangFMCWNLOS2026"):
        if key not in coherent_lines[0]:
            raise RuntimeError(f"coherent table row is missing {key}")

    spad_lines = [line for line in active.splitlines() if "& Pulsed laser & SPAD &" in line and "3D reconstruction" in line]
    if len(spad_lines) != 1:
        raise RuntimeError(f"expected one pulsed-SPAD reconstruction row, found {len(spad_lines)}")
    if "liangFMCWNLOS2026" in spad_lines[0]:
        raise RuntimeError("the FMCW endpoint remains incorrectly classified as pulsed-SPAD")

    if "Coherent FMCW NLOS ranging, imaging, tracking, and vibrometry" not in active:
        raise RuntimeError("coherent-FMCW literature-review paragraph is missing")
    if "through 21 July 2026" not in master:
        raise RuntimeError("master survey coverage date was not updated")
    if '<div class="stat"><b>178</b><span>tracked latest entries</span></div>' not in index:
        raise RuntimeError("website tracked-entry count is inconsistent")

    print("Coherent FMCW DOI, classification, citation, and timeline validation passed.")


if __name__ == "__main__":
    main()
