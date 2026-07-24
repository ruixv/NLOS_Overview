#!/usr/bin/env python3
"""Synchronize two verified NLOS cross-artifact gaps: NIF and SCISA-Net.

The script is idempotent across the known 201-entry pre-update state, a possible
202-entry NIF-only intermediate state, and the final 203-entry state. It fails
closed on ambiguous titles, DOIs, bibliography keys, or insertion anchors.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
DATA = ROOT / "article" / "4datadriven.tex"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-25-nif-scisa-consistency.md"
KEYS = ROOT / "updates" / "2026-07-25-nif-scisa-keys.txt"
TRACE = "% 25 July 2026 consistency trace: Neural Illumination Fields and SCISA-Net synchronized across public and survey artifacts."

NIF = {
    "title": "Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging",
    "doi": "10.1016/j.optlaseng.2025.109514",
    "key": "zhangNeuralIlluminationFields2026",
    "row": "| 2026 | [Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging](https://doi.org/10.1016/j.optlaseng.2025.109514) — Zhang et al. | Optics and Lasers in Engineering 2026 | Introduces self-supervised Neural Illumination Fields for two-bounce shadow imaging: continuous hidden density and illumination-dependent intensity are optimized through differentiable rendering, eliminating binary shadow segmentation and reaching 1 cm resolution in a 144 m³ volume under low-contrast and ambient-light interference. |",
    "obj": '      {cat:"latest newscenes active shadow two-bounce learning neural implicit",title:"Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging",authors:"Zhang et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",url:"https://doi.org/10.1016/j.optlaseng.2025.109514",key:"Self-supervised Neural Illumination Fields parameterize continuous hidden density and illumination-dependent transport, synthesize measured two-bounce shadows through differentiable intensity rendering, avoid binary segmentation, and recover 1 cm detail in a 144 m³ volume under ambient interference."},',
}

SCISA = {
    "title": "SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations",
    "doi": "10.3390/photonics13060575",
    "key": "daiSCISANet2026",
    "row": "| 2026 | [SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations](https://doi.org/10.3390/photonics13060575) — Dai et al. | Photonics 2026 | Treats hidden-display category inference as calibrated wall-mediated NLOS recognition rather than full image or geometry recovery. Scene-aware regularized inversion reorganizes weak indirect evidence, and multi-stage Haar-subband attention preserves discriminative mid/high-frequency cues on a paired 31-class benchmark under attenuation, ambient background, and matched scene re-parameterization tests. |",
    "obj": '      {cat:"latest learning recognition passive semantic security",title:"SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations",authors:"Dai et al.",year:2026,venue:"Photonics 2026",url:"https://doi.org/10.3390/photonics13060575",key:"A calibrated wall-mediated NLOS recognition system combines scene-aware regularized inverse encoding with multi-stage Haar-subband attention to infer 31 hidden display categories while testing attenuation, ambient background, and matched scene re-parameterization robustness; it performs semantic inference rather than full reconstruction."},',
}

PAPERS = [NIF, SCISA]

NIF_BIB = r'''@article{zhangNeuralIlluminationFields2026,
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

SCISA_BIB = r'''@article{daiSCISANet2026,
  author = {Dai, Jihao and Qin, Hongshuai and Li, Guowen and Liu, Jin and Zhang, Xiaoshuai and Qi, Huiyu and Zheng, Zhiwen and Huang, Xingru},
  title = {{SCISA-Net}: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations},
  journal = {Photonics},
  volume = {13},
  number = {6},
  pages = {575},
  month = {June},
  note = {Published 11 June 2026},
  year = {2026},
  doi = {10.3390/photonics13060575},
  url = {https://doi.org/10.3390/photonics13060575}
}'''

SCISA_PROSE = r'''
\vspace{0.8mm}
\noindent \textbf{Calibrated wall-mediated semantic inference.}
Dai~\etal~consider a security-oriented NLOS recognition setting in which a hidden display never enters the camera field of view and only its weak, scene-dependent wall response is observed~\cite{daiSCISANet2026}. Their SCISA-Net first applies scene-aware regularized inverse encoding to reorganize diluted class evidence under a calibrated transport operator, then uses multi-stage Haar-subband attention to accumulate the mid- and high-frequency cues needed for 31-way semantic discrimination. Robustness tests cover illumination attenuation, ambient background interference, and matched scene-operator re-parameterization. Unlike reconstruction methods that recover a hidden image, depth map, or geometry, this work establishes controlled category-level semantic leakage from indirect optical measurements; it therefore extends the recognition branch of NLOS while making calibration dependence and task scope explicit.
'''

NIF_README_TIMELINE = "    │     Zhang et al.: Neural Illumination Fields — continuous self-supervised intensity rendering replaces binary shadow carving for ambient-robust two-bounce 3D reconstruction [Optics and Lasers in Engineering]\n"
SCISA_README_TIMELINE = "   |     Dai et al.: SCISA-Net — calibrated wall-mediated inversion and Haar-subband attention infer hidden-display semantics without full reconstruction [Photonics]\n"
NIF_INDEX_SENTENCE = "Neural Illumination Fields replaced binary two-bounce shadow carving with continuous self-supervised differentiable intensity rendering, providing the static neural-field foundation later extended by D-NeSF to moving scenes."
SCISA_INDEX_SENTENCE = "SCISA-Net further expanded semantic NLOS from reconstructed-scene classification to calibrated wall-mediated category inference, combining regularized physical inversion with Haar-subband attention while explicitly stopping short of full hidden-image or geometry recovery."


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def bib_span(text: str, key: str):
    start_re = re.compile(r"(?m)^@(article|inproceedings|misc|incollection)\{" + re.escape(key) + r",\s*$")
    matches = list(start_re.finditer(text))
    if len(matches) != 1:
        return None if len(matches) == 0 else (_ for _ in ()).throw(SystemExit(f"Bibliography key {key} appears {len(matches)} times"))
    start = matches[0].start()
    pos = matches[0].end()
    depth = 1
    while pos < len(text) and depth:
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
        pos += 1
    if depth:
        raise SystemExit(f"Unbalanced BibTeX entry for {key}")
    return start, pos


def upsert_bib(text: str, key: str, entry: str) -> str:
    span = bib_span(text, key)
    if span is None:
        return text.rstrip() + "\n\n" + entry + "\n"
    return text[:span[0]] + entry + text[span[1]:]


readme = read(README)
index = read(INDEX)
data = read(DATA)
newscenes = read(NEWSCENES)
survey = read(SURVEY)
bib = read(BIB)

# NIF already has a semantically correct survey discussion. Retain it uniquely.
if newscenes.count(r"\cite{" + NIF["key"] + "}") != 1:
    raise SystemExit("Expected exactly one NIF citation in article/5newscenes.tex")
if newscenes.lower().count("neural illumination fields") != 1 or "binary shadow segmentation" not in newscenes.lower():
    raise SystemExit("Existing NIF survey discussion is missing or ambiguous")

# Add SCISA-Net to the recognition trajectory, not as a detached recent-work list.
if r"\cite{" + SCISA["key"] + "}" not in data:
    anchor = "Together with learned feature embeddings and NLOS-R$^2$, these studies establish recognition, action understanding, and clustering as a parallel trajectory to hidden-scene reconstruction."
    if data.count(anchor) != 1:
        raise SystemExit("Recognition-trajectory anchor is not unique")
    data = data.replace(anchor, anchor + "\n" + SCISA_PROSE, 1)
if data.count(r"\cite{" + SCISA["key"] + "}") != 1:
    raise SystemExit("SCISA-Net citation is not unique in article/4datadriven.tex")
if data.count(r"\noindent \textbf{Calibrated wall-mediated semantic inference.}") != 1:
    raise SystemExit("SCISA-Net survey paragraph is not unique")

# README Latest Additions: insert missing public records in the verified order.
header = "|------|-------|----------------|----------------|\n"
if readme.count(header) != 1:
    raise SystemExit("README Latest Additions header is not unique")
missing_rows = []
for paper in PAPERS:
    count = readme.lower().count(paper["title"].lower())
    if count == 0:
        missing_rows.append(paper["row"])
    elif count != 1:
        raise SystemExit(f"README contains {count} copies of {paper['title']}")
if missing_rows:
    readme = readme.replace(header, header + "\n".join(missing_rows) + "\n", 1)

# README timeline: static NIF immediately precedes dynamic D-NeSF; SCISA follows QSS-Net.
if NIF_README_TIMELINE not in readme:
    anchor = "    │     Zhang et al.: D-NeSF — spatiotemporally disentangled neural shadow fields extend two-bounce NLOS stereo reconstruction from static scenes to moving hidden targets [ICGIP / Proceedings of SPIE]\n"
    if readme.count(anchor) != 1:
        raise SystemExit("README D-NeSF anchor is not unique")
    readme = readme.replace(anchor, NIF_README_TIMELINE + anchor, 1)
if SCISA_README_TIMELINE not in readme:
    anchor = "   |     QSS-Net: recognition-oriented quanta-state-slot modeling advances efficient NLOS semantic classification [FLINS-ISKE / Springer LNCS]\n"
    if readme.count(anchor) != 1:
        raise SystemExit("README QSS-Net anchor is not unique")
    readme = readme.replace(anchor, anchor + SCISA_README_TIMELINE, 1)
if readme.count(NIF_README_TIMELINE) != 1 or readme.count(SCISA_README_TIMELINE) != 1:
    raise SystemExit("README timeline records are not unique")

readme = re.sub(r"\*\*Update run: (?:24|25) July 2026\.\*\*", "**Update run: 25 July 2026.**", readme, count=1)
if readme.count("**Update run: 25 July 2026.**") != 1:
    raise SystemExit("README update date was not synchronized")

# Website objects.
papers_anchor = "    const papers=[\n" if "    const papers=[\n" in index else "    const papers = [\n"
if index.count(papers_anchor) != 1:
    raise SystemExit("Website paper-array anchor is not unique")
missing_objects = []
for paper in PAPERS:
    count = index.lower().count(paper["title"].lower())
    if count == 0:
        missing_objects.append(paper["obj"])
    elif count != 1:
        raise SystemExit(f"Website contains {count} copies of {paper['title']}")
if missing_objects:
    index = index.replace(papers_anchor, papers_anchor + "\n".join(missing_objects) + "\n", 1)

# Accept pre-update, NIF-only, or final count; normalize to 203.
count_matches = re.findall(r'<b>(\d+)</b><span>tracked latest entries</span>', index)
if len(count_matches) != 1 or int(count_matches[0]) not in (201, 202, 203):
    raise SystemExit(f"Unexpected website tracked-entry count: {count_matches}")
index = re.sub(r'<b>(?:201|202|203)</b><span>tracked latest entries</span>', '<b>203</b><span>tracked latest entries</span>', index, count=1)

if NIF_INDEX_SENTENCE not in index:
    anchor = "D-NeSF then extended the two-bounce neural-shadow trajectory from static hidden volumes to moving targets"
    if index.count(anchor) != 1:
        raise SystemExit("Website D-NeSF timeline anchor is not unique")
    index = index.replace(anchor, NIF_INDEX_SENTENCE + " " + anchor, 1)
if SCISA_INDEX_SENTENCE not in index:
    anchor = "QSS-Net broadened learned NLOS from reconstruction toward photon-robust clustering and efficient semantic classification."
    if index.count(anchor) != 1:
        raise SystemExit("Website QSS-Net timeline anchor is not unique")
    index = index.replace(anchor, anchor + " " + SCISA_INDEX_SENTENCE, 1)
if index.count(NIF_INDEX_SENTENCE) != 1 or index.count(SCISA_INDEX_SENTENCE) != 1:
    raise SystemExit("Website timeline sentences are not unique")

index = index.replace("Updated 24 July 2026 · 190+ papers", "Updated 25 July 2026 · 190+ papers")
index = index.replace("Last updated: 24 July 2026", "Last updated: 25 July 2026")
if index.count("Updated 25 July 2026 · 190+ papers") != 1 or index.count("Last updated: 25 July 2026") != 1:
    raise SystemExit("Website dates were not synchronized")

# Normalize NIF final venue and add the new SCISA-Net record.
bib = upsert_bib(bib, NIF["key"], NIF_BIB)
bib = upsert_bib(bib, SCISA["key"], SCISA_BIB)
for paper in PAPERS:
    if bib.lower().count("{" + paper["key"].lower() + ",") != 1:
        raise SystemExit(f"Bibliography key is not unique: {paper['key']}")
    if bib.lower().count("doi = {" + paper["doi"].lower() + "}") != 1:
        raise SystemExit(f"Bibliography DOI is not unique: {paper['doi']}")

if TRACE not in survey:
    anchor = "%% bare_jrnl.tex\n"
    if survey.count(anchor) != 1:
        raise SystemExit("bare_jrnl.tex marker anchor is not unique")
    survey = survey.replace(anchor, anchor + TRACE + "\n", 1)
if survey.count(TRACE) != 1:
    raise SystemExit("Combined consistency marker is not unique")

# Final public uniqueness checks.
for paper in PAPERS:
    if readme.lower().count(paper["title"].lower()) != 1:
        raise SystemExit(f"README final title count invalid: {paper['title']}")
    if index.lower().count(paper["title"].lower()) != 1:
        raise SystemExit(f"Website final title count invalid: {paper['title']}")
    if readme.count(paper["doi"]) != 1 or index.count(paper["doi"]) != 1:
        raise SystemExit(f"Public DOI count invalid: {paper['doi']}")
if '<b>203</b><span>tracked latest entries</span>' not in index:
    raise SystemExit("Website count is not 203")

note = f"""# NIF and SCISA-Net cross-artifact synchronization — 25 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found. The newest date-verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

The current citation/keyword pass identified two genuine consistency gaps:

1. *{NIF['title']}* was already cited and discussed in the two-bounce survey section and already had a stable bibliography key, but was absent from the README, website explorer, and public timeline.
2. *{SCISA['title']}* was absent repository-wide. It qualifies as tightly scoped NLOS semantic sensing: a hidden display remains outside the field of view, and only a calibrated wall-mediated indirect observation is used for 31-class category inference. It is explicitly labeled recognition rather than full image, depth, or geometry reconstruction.

## Verified metadata and contribution

- NIF: Optics and Lasers in Engineering 198, 109514 (March 2026), DOI `{NIF['doi']}`. Continuous neural density and illumination-dependent intensity, differentiable shadow rendering, no binary segmentation, 1 cm resolution in 144 m³, simulation and real measurements, ambient/low-contrast robustness.
- SCISA-Net: Photonics 13(6), 575 (published 11 June 2026), DOI `{SCISA['doi']}`. Scene-aware regularized inverse encoding plus multi-stage Haar-subband attention on a paired 31-class benchmark, with attenuation, ambient-background, and matched operator re-parameterization tests.

## Completed changes

1. Added both papers to README Latest Additions and the historical timeline.
2. Added searchable website records, linked NIF to D-NeSF and SCISA-Net to the recognition/clustering trajectory, changed tracked entries from 201 through any NIF-only intermediate state to 203, and advanced public dates to 25 July 2026.
3. Preserved the existing NIF paragraph in `article/5newscenes.tex`; inserted SCISA-Net into the semantic-recognition discussion in `article/4datadriven.tex`.
4. Normalized NIF's stable BibTeX record and added a DOI-verified SCISA-Net record to the bibliography used by `bare_jrnl.tex`.
5. Added a survey trace marker and rebuilt `bare_jrnl.pdf`.

## Validation

- Unique title, DOI, and bibliography-key checks.
- Semantically placed NIF and SCISA-Net citations retained in their respective survey sections.
- Clean `pdflatex → bibtex → pdflatex ×2` build.
- Both generated bibliography items verified in `.bbl`.
- PDF metadata, extracted text, and every rendered page validated.
"""

write_if_changed(README, readme)
write_if_changed(INDEX, index)
write_if_changed(DATA, data)
write_if_changed(NEWSCENES, newscenes)
write_if_changed(SURVEY, survey)
write_if_changed(BIB, bib)
write_if_changed(NOTE, note)
write_if_changed(KEYS, NIF["key"] + "\n" + SCISA["key"] + "\n")
print("NIF and SCISA-Net synchronized and validated.")
