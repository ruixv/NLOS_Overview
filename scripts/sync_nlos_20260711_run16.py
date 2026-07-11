#!/usr/bin/env python3
"""Integrate the verified SSCR paper into the active-NLOS survey narrative.

This run closes a public-surface/survey consistency gap identified by forward
citation tracing. The script is idempotent and uses an exact anchor so it fails
rather than modifying a large hand-maintained TeX file at an uncertain location.
"""
from __future__ import annotations

from pathlib import Path

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
        raise RuntimeError(f"Missing anchor for {label}: {old[:160]!r}")
    if count != 1:
        raise RuntimeError(f"Expected one anchor for {label}, found {count}")
    return text.replace(old, new, 1)


KEY = "liuFewShotSSCR2022"
TITLE = "Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization"

active = read("article/2active.tex")
anchor = (
    "Similarly, Liu~\\etal~introduced a Bayesian framework with confocal-complemented "
    "signal-object collaborative regularization (CC-SOCR) that handles arbitrary illumination "
    "and detection patterns on the relay surface without requiring a regular grid~"
    "\\cite{liuNLOSArbitraryIllumination2023}, greatly broadening the applicability of NLOS "
    "systems to irregular or partial relay surfaces encountered in real-world scenarios.\n"
)
paragraph = anchor + (
    "\nMoving from arbitrary relay sampling toward extreme measurement sparsity, "
    "Liu~\\etal~introduced signal-surface collaborative regularization (SSCR), which jointly "
    "regularizes the photon-event signal, a three-dimensional voxel representation, and a "
    "two-dimensional hidden-surface representation~\\cite{liuFewShotSSCR2022}. The method "
    "supports both confocal and non-confocal acquisition and reconstructs complex hidden "
    "geometry from as few as $5\\times5$ confocal measurements, showing how mixed-dimensional "
    "physical priors can replace much of the dense raster scan required by earlier transient "
    "NLOS systems.\n"
)
if KEY not in active:
    active = replace_once(active, anchor, paragraph, "SSCR active-survey paragraph")
write("article/2active.tex", active)

bib = read("egbib_20260711_sscr_updates.bib")
if KEY not in bib or TITLE not in bib:
    raise RuntimeError("Verified SSCR BibTeX record is missing or incomplete")

note = f'''# SSCR citation-tracing and survey consistency update (11 July 2026)

## Search result

Fresh keyword searches and a forward-citation tracing pass from the repository's core active NLOS papers did not reveal a newer high-confidence July 2026 frontier paper beyond the entries already surfaced in the repository.

The tracing pass did expose one survey-source consistency gap for a directly relevant active transient NLOS paper:

- **{TITLE}** — Xintong Liu, Jianyu Wang, Leping Xiao, Xing Fu, Lingyun Qiu, and Zuoqiang Shi, arXiv:2211.15367 (2022).
- SSCR jointly regularizes the measured/estimated transient signal, a 3D voxel representation, and a 2D hidden-surface representation.
- It supports confocal and non-confocal measurements and reports reconstruction from only `5 x 5` confocal measurements on public data.
- No final conference or journal venue was verified, so the status remains **arXiv 2022**.

## Synchronized artifacts

- `README.md` and `index.html` already contained the verified paper entry.
- `article/2active.tex` now integrates SSCR directly after CC-SOCR in the arbitrary-relay/sparse-measurement discussion.
- `egbib_20260711_sscr_updates.bib` contains the verified citation key `{KEY}`.
- `scripts/merge_nlos_bibliography.py` regenerates `egbib_merged_20260711.bib` from all `egbib*.bib` sources before the survey build.

## PDF status

The GitHub Actions workflow performs a clean LaTeX/BibTeX rebuild, rejects undefined or repeated citation records, validates the PDF with `pdfinfo` and `pdftotext`, and confirms that the SSCR title is present in the generated survey. The workflow records the final build result below.
'''
write("updates/2026-07-11-sscr-survey-consistency-gap.md", note)

if KEY not in read("article/2active.tex"):
    raise RuntimeError("SSCR survey integration check failed")

print("Run-16 SSCR survey integration completed successfully")
