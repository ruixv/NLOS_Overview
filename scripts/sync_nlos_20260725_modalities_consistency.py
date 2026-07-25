#!/usr/bin/env python3
"""Finish the 25 July 2026 NLOS modality/hardware consistency pass.

The script is idempotent, preserves existing BibTeX keys when a DOI-equivalent
record already exists, and fails closed when a semantic insertion anchor is
ambiguous.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
DATA = ROOT / "article" / "4datadriven.tex"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-25-modalities-consistency.md"
KEYS = ROOT / "updates" / "2026-07-25-modalities-consistency-keys.txt"
TRACE = "% 25 July 2026 modality trace: rough-wall thermal NLOS, compact eye-safe SPAD localization, NIR raster scanning, all-day Si-SPAD operation, and common-model ToF benchmarking synchronized."

PAPERS = [
    dict(
        key="yeThermalRoughNLOS2026",
        title="Thermal Non-Line-of-Sight Imaging through Rough Surfaces",
        authors="Ye et al.", year=2026, venue="ACM TOG 2026",
        url="https://doi.org/10.1145/3811030", doi="10.1145/3811030",
        cats="latest passive thermal learning depth rough-relay",
        summary="NLOSFormer embeds a thermal transport model and scene-dependent kernel estimation into reconstruction, jointly recovering hidden thermal appearance and relative depth through rough relay surfaces and supporting dynamic inference at about 4 fps.",
        readme=False,
        bib=r'''@article{yeThermalRoughNLOS2026,
  author = {Ye, Ruilin and Zhou, Yijun and Zeng, Jianwei and Dai, Chen and Hong, Wenqing and Li, Wenwen and Zhao, Jun and Xu, Feihu},
  title = {Thermal Non-Line-of-Sight Imaging through Rough Surfaces},
  journal = {ACM Transactions on Graphics}, volume = {45}, number = {5}, articleno = {41}, pages = {1--21}, year = {2026},
  publisher = {Association for Computing Machinery}, doi = {10.1145/3811030}, url = {https://doi.org/10.1145/3811030}
}'''),
    dict(
        key="albertEyeSafeNLOS2026",
        title="Eye-Safe Non-Line-of-Sight Localization Using Compact Nanosecond Laser Diodes and Single-Photon-Avalanche-Diode Arrays",
        authors="Albert et al.", year=2026, venue="JEOS-RP 2026",
        url="https://doi.org/10.1051/jeos/2026019", doi="10.1051/jeos/2026019",
        cats="latest active hardware spad eye-safe localization",
        summary="Combines inexpensive nanosecond laser diodes with a parallel SPAD array, dual off-axis illumination, matched temporal filtering, and ellipsoidal backprojection for compact eye-safe hidden-target localization.",
        readme=True,
        bib=r'''@article{albertEyeSafeNLOS2026,
  author = {Albert, Konstantin and Klein, Julian and Ligges, Manuel and Grabmaier, Anton},
  title = {Eye-Safe Non-Line-of-Sight Localization Using Compact Nanosecond Laser Diodes and Single-Photon-Avalanche-Diode Arrays},
  journal = {Journal of the European Optical Society-Rapid Publications}, volume = {22}, number = {1}, pages = {40}, year = {2026},
  doi = {10.1051/jeos/2026019}, url = {https://doi.org/10.1051/jeos/2026019}
}'''),
    dict(
        key="roueinfarNIRRasterNLOS2025",
        title="Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength",
        authors="Roueinfar, Salmanian", year=2025, venue="IEEE ICEE 2025",
        url="https://doi.org/10.1109/ICEE67339.2025.11213924", doi="10.1109/ICEE67339.2025.11213924",
        cats="latest active nir hardware steady-state raster",
        summary="Demonstrates a low-cost measured three-bounce baseline using an 808 nm laser, pan-tilt relay-wall raster scanning, and an NIR camera; the final IEEE conference venue supersedes the later arXiv upload.",
        readme=False,
        bib=r'''@inproceedings{roueinfarNIRRasterNLOS2025,
  author = {Roueinfar, Mohammad and Salmanian, Mahdi},
  title = {Non-Line-of-Sight Imaging Using Raster Scanning at {NIR} Wavelength},
  booktitle = {2025 33rd International Conference on Electrical Engineering (ICEE)}, pages = {1--5}, year = {2025}, publisher = {IEEE},
  doi = {10.1109/ICEE67339.2025.11213924}, url = {https://doi.org/10.1109/ICEE67339.2025.11213924}, note = {Also available as arXiv:2607.04183}
}'''),
    dict(
        key="marcoComprehensiveToFNLOS2026",
        title="A comprehensive study of time-of-flight non-line-of-sight imaging",
        authors="Marco et al.", year=2026, venue="arXiv 2026",
        url="https://arxiv.org/abs/2603.09548", doi="",
        cats="latest survey benchmark active transient tof",
        summary="Places representative ToF NLOS methods under a common forward model and compares Radon-, frequency-domain-, and phasor-field inverses under controlled hardware and photon-count assumptions; no final venue is yet verified.",
        readme=False,
        bib=r'''@misc{marcoComprehensiveToFNLOS2026,
  author = {Marco, Julio and Jarabo, Adri{\'a}n and Nam, Ji Hyun and Tosi, Alberto and Guti{\'e}rrez, Diego and Velten, Andreas},
  title = {A Comprehensive Study of Time-of-Flight Non-Line-of-Sight Imaging}, year = {2026},
  eprint = {2603.09548}, archivePrefix = {arXiv}, primaryClass = {cs.CV}, url = {https://arxiv.org/abs/2603.09548}
}'''),
    dict(
        key="yinAllDayNLOS2026",
        title="All-day non-line-of-sight imaging based on Si-SPAD and phase-congruency-based structured ε-regularization",
        authors="Yin et al.", year=2026, venue="Optics and Lasers in Engineering 2026",
        url="https://doi.org/10.1016/j.optlaseng.2026.109919", doi="10.1016/j.optlaseng.2026.109919",
        cats="latest active spad daylight long-range phasor-field",
        summary="Co-designs Si-SPAD selection and phase-congruency structured regularization for extreme ambient light, demonstrating 200 m NLOS imaging under 94,314 lx with 4 cm lateral and 1 cm axial resolution.",
        readme=False,
        bib=r'''@article{yinAllDayNLOS2026,
  author = {Yin, Yuyang and Shi, Yingjie and Wu, Chenyang and Qin, Taotao and Bai, Lianfa and Zhang, Yi and Guo, Enlai and Han, Jing},
  title = {All-Day Non-Line-of-Sight Imaging Based on {Si-SPAD} and Phase-Congruency-Based Structured $\epsilon$-Regularization},
  journal = {Optics and Lasers in Engineering}, volume = {205}, pages = {109919}, year = {2026},
  doi = {10.1016/j.optlaseng.2026.109919}, url = {https://doi.org/10.1016/j.optlaseng.2026.109919}
}'''),
]


def read(path):
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write(path, text):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def bib_entry_span(text, key):
    m = re.search(r"(?mi)^@(article|inproceedings|misc|incollection)\{" + re.escape(key) + r",", text)
    if not m:
        return None
    pos, depth = m.end(), 1
    while pos < len(text) and depth:
        depth += (text[pos] == "{") - (text[pos] == "}")
        pos += 1
    if depth:
        raise SystemExit(f"Unbalanced BibTeX entry: {key}")
    return m.start(), pos


def key_for_doi(text, doi):
    if not doi:
        return None
    for m in re.finditer(r"(?mi)^@(article|inproceedings|misc|incollection)\{([^,]+),", text):
        key = m.group(2)
        span = bib_entry_span(text, key)
        if span and doi.lower() in text[span[0]:span[1]].lower():
            return key
    return None


def key_for_title(text, title):
    needle = re.sub(r"[^a-z0-9]", "", title.lower())
    for m in re.finditer(r"(?mi)^@(article|inproceedings|misc|incollection)\{([^,]+),", text):
        key = m.group(2)
        span = bib_entry_span(text, key)
        if not span:
            continue
        block = text[span[0]:span[1]]
        tm = re.search(r"(?is)\btitle\s*=\s*\{(.*?)\}\s*,", block)
        if tm and re.sub(r"[^a-z0-9]", "", tm.group(1).lower()) == needle:
            return key
    return None


def upsert_bib(text, paper):
    key = key_for_doi(text, paper["doi"]) or key_for_title(text, paper["title"]) or paper["key"]
    span = bib_entry_span(text, key)
    if span:
        if key == paper["key"]:
            text = text[:span[0]] + paper["bib"] + text[span[1]:]
    else:
        text = text.rstrip() + "\n\n" + paper["bib"] + "\n"
    return text, key


readme, index = read(README), read(INDEX)
active, data, newscenes = read(ACTIVE), read(DATA), read(NEWSCENES)
survey, bib = read(SURVEY), read(BIB)

resolved = {}
for paper in PAPERS:
    bib, resolved[paper["key"]] = upsert_bib(bib, paper)

# README: only add genuinely absent public rows; retain existing final-venue rows.
header = "|------|-------|----------------|----------------|\n"
if readme.count(header) != 1:
    raise SystemExit("README Latest Additions header is ambiguous")
rows = []
for paper in PAPERS:
    count = readme.lower().count(paper["title"].lower())
    if count == 0 and paper["readme"]:
        rows.append(f'| {paper["year"]} | [{paper["title"]}]({paper["url"]}) — {paper["authors"]} | {paper["venue"]} | {paper["summary"]} |')
    elif count > 1:
        raise SystemExit(f'Duplicate README title: {paper["title"]}')
if rows:
    readme = readme.replace(header, header + "\n".join(rows) + "\n", 1)
readme = re.sub(r"\*\*Update run: (?:24|25) July 2026\.\*\*", "**Update run: 25 July 2026.**", readme, count=1)

# Website explorer and timeline.
anchor = "    const papers=[\n" if "    const papers=[\n" in index else "    const papers = [\n"
if index.count(anchor) != 1:
    raise SystemExit("Website paper-array anchor is ambiguous")
objects, inserted = [], 0
for paper in PAPERS:
    count = index.lower().count(paper["title"].lower())
    if count == 0:
        objects.append(f'      {{cat:"{paper["cats"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{paper["summary"]}"}},')
        inserted += 1
    elif count > 1:
        raise SystemExit(f'Duplicate website title: {paper["title"]}')
if objects:
    index = index.replace(anchor, anchor + "\n".join(objects) + "\n", 1)
counts = re.findall(r'<b>(\d+)</b><span>tracked latest entries</span>', index)
if len(counts) != 1:
    raise SystemExit("Website tracked-entry count is ambiguous")
new_count = int(counts[0]) + inserted
index = re.sub(r'<b>\d+</b><span>tracked latest entries</span>', f'<b>{new_count}</b><span>tracked latest entries</span>', index, count=1)
index = index.replace("Updated 24 July 2026", "Updated 25 July 2026")
index = index.replace("Last updated: 24 July 2026", "Last updated: 25 July 2026")
timeline_sentence = " Compact eye-safe SPAD-array localization, all-day Si-SPAD capture, rough-wall thermal reconstruction, accessible NIR scanning, and common-model ToF benchmarking broadened NLOS deployment and evaluation conditions."
pat = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body">.*?<p>)(.*?)(</p>)', re.S)
m = pat.search(index)
if not m:
    raise SystemExit("Website 2026 timeline anchor is missing")
if timeline_sentence.strip() not in m.group(2):
    index = index[:m.start()] + m.group(1) + m.group(2) + timeline_sentence + m.group(3) + index[m.end():]

# Active survey: eye-safe SPAD arrays and a common-model comparison reference.
eye_key = resolved["albertEyeSafeNLOS2026"]
if "Compact eye-safe nanosecond SPAD-array localization" not in active:
    insert_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Miniaturized TCSPC electronics.}"
    if active.count(insert_anchor) != 1:
        raise SystemExit("Eye-safe SPAD insertion anchor is ambiguous")
    prose = f'''\\vspace{{0.8mm}}
\\noindent \\textbf{{Compact eye-safe nanosecond SPAD-array localization.}}
Albert~\\etal~replace bulky picosecond sources with inexpensive nanosecond laser diodes and observe the relay wall in parallel using a SPAD array with integrated timing~\\cite{{{eye_key}}}. Two off-axis illumination positions mitigate first-photon saturation, while matched temporal filtering and ellipsoidal backprojection localize the hidden target despite the extended pulse width. This result complements miniaturized TCSPC and scan-free arrays by showing that deployment cost and eye safety can be improved at the illumination source, provided the acquisition geometry and temporal filtering are co-designed.

'''
    active = active.replace(insert_anchor, prose + insert_anchor, 1)
# Add the eye-safe paper to the SPAD-array system table without replacing existing keys.
if eye_key not in active.split("\\end{table*}", 1)[0]:
    row = r"\cite{nam_real-time_2020,jinScannerlessNonlineofsightThree2020,zhangRealTimeScanFreeNLOS2024,zhangSpatialCorrelationNLOS2025}"
    if active.count(row) != 1:
        raise SystemExit("SPAD-array table row is ambiguous")
    active = active.replace(row, row[:-1] + "," + eye_key + "}", 1)

benchmark_key = resolved["marcoComprehensiveToFNLOS2026"]
if "Common-model benchmarking of ToF NLOS inverses" not in active:
    insert_anchor = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Challenges and Prospects}"
    if active.count(insert_anchor) != 1:
        raise SystemExit("Active challenges anchor is ambiguous")
    prose = f'''\\vspace{{0.8mm}}
\\noindent \\textbf{{Common-model benchmarking of ToF NLOS inverses.}}
Marco~\\etal~place representative ToF NLOS methods under a shared forward model and controlled hardware and photon-count assumptions~\\cite{{{benchmark_key}}}. Their analysis relates Radon-style, frequency-domain, and phasor-field formulations and shows that apparent method differences must be separated from common aperture, visibility, resolution, and noise limits. This benchmark-oriented viewpoint complements algorithm-by-algorithm summaries and provides a reproducible basis for evaluating future inverse operators.

'''
    active = active.replace(insert_anchor, prose + insert_anchor, 1)

# Thermal modality in the new-scenes chapter.
thermal_key = resolved["yeThermalRoughNLOS2026"]
if "Thermal NLOS through rough relay surfaces" not in newscenes:
    insert_anchor = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Radar-Based NLOS Imaging}"
    if newscenes.count(insert_anchor) != 1:
        raise SystemExit("Thermal-modality insertion anchor is ambiguous")
    prose = f'''\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{{Thermal NLOS through rough relay surfaces}}
\\subsection{{Thermal NLOS through rough relay surfaces}}
Ye~\\etal~extend passive long-wave-infrared NLOS beyond conveniently smooth relay materials with NLOSFormer~\\cite{{{thermal_key}}}. A physics-embedded network estimates a scene-dependent thermal convolution kernel and jointly recovers hidden appearance and relative depth, while the ThermalNLOS dataset covers rough-wall conditions and dynamic sequences. Reported operation at approximately 4~fps shows that learned thermal transport can relax idealized relay-surface assumptions while retaining physical structure, expanding NLOS toward darkness, adverse visible illumination, and practical building materials.

'''
    newscenes = newscenes.replace(insert_anchor, prose + insert_anchor, 1)

# Cross-reference NLOSFormer from the physics-guided learning chapter.
if "Physics-embedded thermal transport learning" not in data:
    insert_anchor = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Challenges and Prospects}"
    if data.count(insert_anchor) != 1:
        raise SystemExit("Data-driven challenges anchor is ambiguous")
    prose = f'''\\vspace{{0.8mm}}
\\noindent \\textbf{{Physics-embedded thermal transport learning.}}
NLOSFormer provides a modality-specific example of a network learning an effective transport operator rather than treating the relay observation as an unconstrained image-to-image mapping~\\cite{{{thermal_key}}}. Its kernel-estimation branch encodes rough-surface thermal propagation and supports joint appearance and relative-depth inference; the primary modality discussion appears in Sec.~\\ref{{sec5}}.

'''
    data = data.replace(insert_anchor, prose + insert_anchor, 1)

if TRACE not in survey:
    marker = "%% bare_jrnl.tex\n"
    if survey.count(marker) != 1:
        raise SystemExit("Survey trace anchor is ambiguous")
    survey = survey.replace(marker, marker + TRACE + "\n", 1)

# Final checks before writing.
for paper in PAPERS:
    if index.lower().count(paper["title"].lower()) != 1:
        raise SystemExit(f'Website title count invalid: {paper["title"]}')
    if paper["readme"] and readme.lower().count(paper["title"].lower()) != 1:
        raise SystemExit(f'README title count invalid: {paper["title"]}')
for key in dict.fromkeys(resolved.values()):
    if not bib_entry_span(bib, key):
        raise SystemExit(f"Missing bibliography key: {key}")

note = f'''# NLOS modality and hardware consistency update — 25 July 2026

No direct NLOS publication with verified publication metadata later than 22 July 2026 was found. The newest remains *Iterating the transient light transport matrix for non-line-of-sight imaging* in Nature Communications.

This run completes cross-artifact integration for rough-wall thermal NLOS, compact eye-safe nanosecond/SPAD localization, final-venue NIR raster scanning, all-day Si-SPAD NLOS, and the common-model ToF benchmark. It adds only the genuinely absent README entry, inserts missing website explorer records, places literature-review prose in the active, learning, and new-modality sections, merges canonical bibliography metadata while preserving stable keys, and rebuilds the survey PDF. Website tracked-entry count after synchronization: {new_count}.
'''

for path, text in ((README, readme), (INDEX, index), (ACTIVE, active), (DATA, data), (NEWSCENES, newscenes), (SURVEY, survey), (BIB, bib), (NOTE, note)):
    write(path, text)
write(KEYS, "\n".join(dict.fromkeys(resolved.values())) + "\n")
print(f"NLOS modality consistency synchronized; website count={new_count}.")
