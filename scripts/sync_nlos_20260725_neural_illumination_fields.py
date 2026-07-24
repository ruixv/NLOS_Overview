#!/usr/bin/env python3
"""Synchronize Neural Illumination Fields across public NLOS survey artifacts.

This update is intentionally fail-closed: it accepts either the known pre-update
state or an already synchronized state, but refuses duplicate titles, DOI records,
or ambiguous insertion anchors.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-25-neural-illumination-fields.md"
KEYS = ROOT / "updates" / "2026-07-25-neural-illumination-keys.txt"

TITLE = "Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging"
DOI = "10.1016/j.optlaseng.2025.109514"
KEY = "zhangNeuralIlluminationFields2026"
TRACE = "% 25 July 2026 consistency trace: Neural Illumination Fields synchronized across public artifacts."
OLD_COUNT = 201
NEW_COUNT = 202

README_ROW = (
    "| 2026 | [Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce "
    "non-line-of-sight imaging](https://doi.org/10.1016/j.optlaseng.2025.109514) — Zhang et al. | "
    "Optics and Lasers in Engineering 2026 | Introduces self-supervised Neural Illumination Fields for two-bounce "
    "shadow imaging: continuous hidden density and illumination-dependent intensity are optimized through differentiable "
    "rendering, eliminating binary shadow segmentation and reaching 1 cm resolution in a 144 m³ volume under low-contrast "
    "and ambient-light interference. |"
)

INDEX_OBJECT = (
    '      {cat:"latest newscenes active shadow two-bounce learning neural implicit",'
    'title:"Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging",'
    'authors:"Zhang et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",'
    'url:"https://doi.org/10.1016/j.optlaseng.2025.109514",'
    'key:"Self-supervised Neural Illumination Fields parameterize continuous hidden density and illumination-dependent transport, '
    'synthesize measured two-bounce shadows through differentiable intensity rendering, avoid binary segmentation, and recover '
    '1 cm detail in a 144 m³ volume under ambient interference."},'
)

README_TIMELINE = (
    "    │     Zhang et al.: Neural Illumination Fields — continuous self-supervised intensity rendering replaces binary "
    "shadow carving for ambient-robust two-bounce 3D reconstruction [Optics and Lasers in Engineering]\n"
)

INDEX_TIMELINE_SENTENCE = (
    "Neural Illumination Fields replaced binary two-bounce shadow carving with continuous self-supervised differentiable "
    "intensity rendering, providing the static neural-field foundation later extended by D-NeSF to moving scenes."
)

CANONICAL_BIB = r'''@article{zhangNeuralIlluminationFields2026,
  author = {Zhang, Jingyuan and Zhang, Bochao and Wang, Zijin and Qu, Chao and Bai, Lianfa and Chen, Xiaoyu and Han, Jing and Guo, Baohui},
  title = {Neural Illumination Fields: High-Fidelity and Ambient-Robust Stereo Reconstruction for Two-Bounce Non-Line-of-Sight Imaging},
  journal = {Optics and Lasers in Engineering},
  volume = {198},
  pages = {109514},
  month = {March},
  year = {2026},
  doi = {10.1016/j.optlaseng.2025.109514},
  url = {https://doi.org/10.1016/j.optlaseng.2025.109514}
}'''


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def replace_bib_entry(text: str, key: str, replacement: str) -> str:
    start_re = re.compile(r"(?m)^@(article|inproceedings|misc|incollection)\{" + re.escape(key) + r",\s*$")
    matches = list(start_re.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f"Bibliography key {key} count is {len(matches)}, expected 1")
    start = matches[0].start()
    pos = matches[0].end()
    depth = 1
    while pos < len(text) and depth:
        char = text[pos]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        pos += 1
    if depth != 0:
        raise SystemExit(f"Unbalanced BibTeX entry for {key}")
    return text[:start] + replacement + text[pos:]


readme = read(README)
index = read(INDEX)
newscenes = read(NEWSCENES)
survey = read(SURVEY)
bib = read(BIB)

# The survey already contains the semantically placed NIF discussion. Require it
# rather than appending a detached duplicate.
if newscenes.count(r"\cite{" + KEY + "}") != 1:
    raise SystemExit("Expected exactly one Neural Illumination Fields citation in article/5newscenes.tex")
if newscenes.lower().count("neural illumination fields") != 1:
    raise SystemExit("Expected exactly one Neural Illumination Fields survey discussion")
if "binary shadow segmentation" not in newscenes.lower():
    raise SystemExit("Existing NIF survey paragraph lacks its central binary-segmentation contribution")

# Public README row.
readme_title_count = readme.lower().count(TITLE.lower())
if readme_title_count == 0:
    header = "|------|-------|----------------|----------------|\n"
    if readme.count(header) != 1:
        raise SystemExit("README Latest Additions header is not unique")
    readme = readme.replace(header, header + README_ROW + "\n", 1)
elif readme_title_count != 1:
    raise SystemExit(f"README contains {readme_title_count} copies of the NIF title")

# Public README timeline, placed immediately before the dynamic D-NeSF extension.
if README_TIMELINE not in readme:
    anchor = "    │     Zhang et al.: D-NeSF — spatiotemporally disentangled neural shadow fields extend two-bounce NLOS stereo reconstruction from static scenes to moving hidden targets [ICGIP / Proceedings of SPIE]\n"
    if readme.count(anchor) != 1:
        raise SystemExit("README D-NeSF timeline anchor is not unique")
    readme = readme.replace(anchor, README_TIMELINE + anchor, 1)
if readme.count(README_TIMELINE) != 1:
    raise SystemExit("README NIF timeline entry is not unique")

# Public update date.
readme = re.sub(r"\*\*Update run: (?:24|25) July 2026\.\*\*", "**Update run: 25 July 2026.**", readme, count=1)
if readme.count("**Update run: 25 July 2026.**") != 1:
    raise SystemExit("README update date was not synchronized")

# Website explorer object and tracked-entry count.
index_title_count = index.lower().count(TITLE.lower())
if index_title_count == 0:
    anchor = "    const papers=[\n"
    if index.count(anchor) != 1:
        # Current site uses spaces around '='; support only that one known variant.
        anchor = "    const papers = [\n"
    if index.count(anchor) != 1:
        raise SystemExit("Website paper-array anchor is not unique")
    index = index.replace(anchor, anchor + INDEX_OBJECT + "\n", 1)
elif index_title_count != 1:
    raise SystemExit(f"Website contains {index_title_count} copies of the NIF title")

old_count_html = f'<b>{OLD_COUNT}</b><span>tracked latest entries</span>'
new_count_html = f'<b>{NEW_COUNT}</b><span>tracked latest entries</span>'
if old_count_html in index:
    index = index.replace(old_count_html, new_count_html, 1)
elif new_count_html not in index:
    raise SystemExit("Website tracked-entry count is neither the expected pre- nor post-update value")
if index.count(new_count_html) != 1:
    raise SystemExit("Website tracked-entry count was not updated uniquely")

# Connect NIF to its later dynamic extension in the historical-development text.
if INDEX_TIMELINE_SENTENCE not in index:
    anchor = "D-NeSF then extended the two-bounce neural-shadow trajectory from static hidden volumes to moving targets"
    if index.count(anchor) != 1:
        raise SystemExit("Website D-NeSF timeline anchor is not unique")
    index = index.replace(anchor, INDEX_TIMELINE_SENTENCE + " " + anchor, 1)
if index.count(INDEX_TIMELINE_SENTENCE) != 1:
    raise SystemExit("Website NIF timeline sentence is not unique")

index = index.replace("Updated 24 July 2026 · 190+ papers", "Updated 25 July 2026 · 190+ papers")
index = index.replace("Last updated: 24 July 2026", "Last updated: 25 July 2026")
if index.count("Updated 25 July 2026 · 190+ papers") != 1 or index.count("Last updated: 25 July 2026") != 1:
    raise SystemExit("Website update dates were not synchronized")

# Preserve the stable citation key while normalizing its canonical final-venue metadata.
bib = replace_bib_entry(bib, KEY, CANONICAL_BIB)
if bib.lower().count("{" + KEY.lower() + ",") != 1:
    raise SystemExit("Canonical NIF bibliography key is not unique")
if bib.lower().count("doi = {" + DOI.lower() + "}") != 1:
    raise SystemExit("Canonical NIF DOI is not unique")

# Add a trace marker to the master survey source.
if TRACE not in survey:
    anchor = "%% bare_jrnl.tex\n"
    if survey.count(anchor) != 1:
        raise SystemExit("bare_jrnl.tex marker anchor is not unique")
    survey = survey.replace(anchor, anchor + TRACE + "\n", 1)
if survey.count(TRACE) != 1:
    raise SystemExit("NIF survey trace marker is not unique")

# Final cross-artifact checks before writes.
if readme.lower().count(TITLE.lower()) != 1 or index.lower().count(TITLE.lower()) != 1:
    raise SystemExit("NIF title is not unique across public artifacts")
if readme.count(DOI) != 1 or index.count(DOI) != 1:
    raise SystemExit("NIF DOI is not unique across public artifacts")

note = f"""# Neural Illumination Fields public-artifact synchronization — 25 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found. The newest date-verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

Citation tracing through the two-bounce NLOS, computational-shadow, and neural implicit-reconstruction lineages exposed one cross-artifact gap. *{TITLE}* was already cited and discussed in `article/5newscenes.tex`, and its stable BibTeX key already existed, but the paper was absent from `README.md`, the website paper explorer, and the public development timeline.

## Verified metadata

- Jingyuan Zhang, Bochao Zhang, Zijin Wang, Chao Qu, Lianfa Bai, Xiaoyu Chen, Jing Han, and Baohui Guo.
- *Optics and Lasers in Engineering*, volume 198, article 109514, March 2026.
- DOI `{DOI}`.
- Direct two-bounce NLOS reconstruction: a self-supervised continuous neural field models hidden density and illumination-dependent intensity, synthesizes measured shadows through differentiable rendering, removes binary shadow segmentation, and reports 1 cm resolution within a 144 m³ hidden volume under low contrast and ambient interference.

## Completed changes

1. Added a DOI-linked README Latest Additions row and a 2026 timeline milestone immediately before D-NeSF.
2. Added a searchable website explorer record, linked NIF to the static-to-dynamic neural-shadow trajectory, changed the tracked-entry count from {OLD_COUNT} to {NEW_COUNT}, and advanced public dates to 25 July 2026.
3. Preserved the existing semantically placed survey paragraph and stable citation key; normalized the final-venue BibTeX record in place rather than creating a duplicate.
4. Added a trace marker to `bare_jrnl.tex` and regenerated `bare_jrnl.pdf` through a clean LaTeX/BibTeX build.

## Validation

- One title and DOI occurrence in each public artifact.
- One stable bibliography key and DOI record.
- Existing NIF discussion and citation retained in the two-bounce NLOS section.
- Clean `pdflatex → bibtex → pdflatex ×2` build and resolved generated bibliography item.
- PDF metadata, extracted text, and rendered pages validated.
"""

write_if_changed(README, readme)
write_if_changed(INDEX, index)
write_if_changed(NEWSCENES, newscenes)
write_if_changed(SURVEY, survey)
write_if_changed(BIB, bib)
write_if_changed(NOTE, note)
write_if_changed(KEYS, KEY + "\n")
print("Neural Illumination Fields synchronized across public artifacts.")
