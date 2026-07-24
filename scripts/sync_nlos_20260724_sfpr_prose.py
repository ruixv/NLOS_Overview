#!/usr/bin/env python3
"""Integrate the already-listed SFPR paper into the survey prose, fail closed."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "article" / "2active.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
NOTE = ROOT / "updates" / "2026-07-24-sfpr-survey-integration.md"

TITLE = "Nonconfocal non-line-of-sight imaging with specular-flight-path regularization for complex multi-orientation objects"
DOI = "10.1364/PRJ.579183"
KEY = "shiSpecularFlightPathNLOS2026"
HEADING = r"\noindent \textbf{Specular-flight-path regularization for nonconfocal multi-orientation scenes.}"
TRACE = "% 24 July 2026 consistency follow-up: specular-flight-path nonconfocal reconstruction integrated into survey prose."

PARAGRAPH = r"""\vspace{0.8mm}
\noindent \textbf{Specular-flight-path regularization for nonconfocal multi-orientation scenes.}
Shi~\etal~examined why nonconfocal measurements can become poorly conditioned when a single illumination point and a finite detector aperture observe tilted or mutually occluding surfaces~\cite{shiSpecularFlightPathNLOS2026}. Local transport-matrix analysis shows that relay samples associated with approximate specular flight paths have lower column similarity and less redundant hidden-voxel responses than nonspecular regions. Their SFPR formulation converts this geometry into voxel-wise specular weights and alternates albedo and weight updates with total-variation regularization in an ADMM solver. Simulated scenes achieve reported SSIM above 0.85, while public and measured experiments improve completeness for multiple objects with different orientations. The result complements frequency-domain phase compensation and artifact correction by using hidden-surface orientation to improve the conditioning of the inverse problem itself.

"""


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file is missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> None:
    old = read(path) if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


readme = read(README)
index = read(INDEX)
active = read(ACTIVE)
survey = read(SURVEY)
bib = read(BIB)

# The public artifacts and bibliography already list the paper; do not add a duplicate.
for name, text in (("README.md", readme), ("index.html", index)):
    if TITLE.lower() not in text.lower() or DOI not in text:
        raise SystemExit(f"{name} does not contain the verified SFPR record; refusing a prose-only update")
if readme.count(DOI) != 1:
    raise SystemExit(f"README DOI count is {readme.count(DOI)}, expected exactly 1")
if index.count(DOI) != 1:
    raise SystemExit(f"index DOI count is {index.count(DOI)}, expected exactly 1")
if index.count('tracked latest entries') != 1 or '<b>193</b><span>tracked latest entries</span>' not in index:
    raise SystemExit("Website count is not the expected pre-update value 193; refusing to guess")

# Insert a semantically placed literature-review paragraph once.
if HEADING not in active:
    anchor = r"""\vspace{0.8mm}
\noindent \textbf{Inverse Rendering.}"""
    if active.count(anchor) != 1:
        raise SystemExit(f"Active-section insertion anchor count is {active.count(anchor)}, expected exactly 1")
    active = active.replace(anchor, PARAGRAPH + anchor, 1)
if active.count(HEADING) != 1:
    raise SystemExit(f"Dedicated SFPR heading count is {active.count(HEADING)}, expected exactly 1")
if active.count(r"\cite{" + KEY + "}") < 1:
    raise SystemExit("Dedicated SFPR prose does not cite the canonical key")

# Add a trace marker without changing the public coverage date.
if TRACE not in survey:
    anchor = "%% bare_jrnl.tex\n"
    if survey.count(anchor) != 1:
        raise SystemExit(f"Survey trace anchor count is {survey.count(anchor)}, expected exactly 1")
    survey = survey.replace(anchor, anchor + TRACE + "\n", 1)
if survey.count(TRACE) != 1:
    raise SystemExit("Survey trace marker is not unique")

# Normalize final-publication metadata while preserving the stable citation key.
entry_pattern = re.compile(r"@article\{" + re.escape(KEY) + r",\n.*?\n\}", re.DOTALL)
entries = entry_pattern.findall(bib)
if len(entries) != 1:
    raise SystemExit(f"Canonical bibliography entry count is {len(entries)}, expected exactly 1")
entry = entries[0]
if f"doi = {{{DOI}}}" not in entry:
    raise SystemExit("Canonical entry does not contain the verified DOI")
if "  month = {March}," not in entry:
    entry = entry.replace("  journal = {Photonics Research},\n", "  journal = {Photonics Research},\n  month = {March},\n", 1)
if "  note = {Published 19 March 2026}," not in entry:
    entry = entry.replace("  number = {4},\n", "  note = {Published 19 March 2026},\n  number = {4},\n", 1)
bib = entry_pattern.sub(entry, bib, count=1)
if bib.count("@article{" + KEY) != 1:
    raise SystemExit("Canonical bibliography key is duplicated after normalization")
if bib.count(f"doi = {{{DOI}}}") != 1:
    raise SystemExit("Canonical DOI field is missing or duplicated after normalization")

note = f"""# SFPR survey-prose consistency integration — 24 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found in this run. The newest date-verified direct NLOS publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

The citation-tracing and cross-artifact audit instead found one semantic integration gap. The following final-venue paper was already present in `README.md`, the website explorer/timeline, the active-system table, and the consolidated bibliography, but it lacked a dedicated literature-review discussion in the LaTeX survey:

- **{TITLE}** — Xiaojie Shi, Jie Yang, Xiaorui Tian, Zhou Yang, Kai Qiao, Meng Tang, Siqi Zhang, and Chenfei Jin; *Photonics Research* 14(4), 1125–1134 (2026); DOI `{DOI}`; published 19 March 2026.

## Changes made

1. Added a dedicated paragraph to `article/2active.tex` after reference-free artifact correction and before inverse rendering. It explains local transport-matrix conditioning, specular-flight-path regions, voxel-wise specular weights, TV/ADMM optimization, and the paper's role in nonconfocal multi-orientation reconstruction.
2. Preserved the stable citation key `{KEY}` and added the verified March publication month/date to `egbib_merged_20260711.bib`.
3. Added a trace marker to `bare_jrnl.tex` without changing the already-current 24 July 2026 public coverage date.
4. Left `README.md`, `index.html`, the 193-entry explorer count, and the timeline unchanged because they already contained the correct record and contribution summary.
5. Rebuilt and validated `bare_jrnl.pdf` in the guarded workflow.

## Consistency checks

- Exactly one DOI record in README and website, plus one canonical DOI field in the consolidated bibliography.
- Exactly one canonical BibTeX key and one dedicated survey heading.
- Existing active-system-table citation retained.
- Clean `pdflatex → bibtex → pdflatex ×2` build.
- No undefined citations or multiply defined BibTeX entries.
- PDF page metadata and extracted text checked; the new SFPR discussion is present in the regenerated PDF.
"""

write_if_changed(ACTIVE, active)
write_if_changed(SURVEY, survey)
write_if_changed(BIB, bib)
write_if_changed(NOTE, note)

print("SFPR survey-prose integration synchronized and validated.")
