from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATE_LONG = "22 August 2026"

PAPERS = [
    {
        "title": "Corner Occluder Computational Periscopy: Estimating a Hidden Scene from a Single Photograph",
        "key": "DBLP:conf/iccp/SeidelMMSFYG19",
        "doi": "10.1109/ICCPHOT.2019.8747342",
        "url": "https://doi.org/10.1109/ICCPHOT.2019.8747342",
        "year": 2019,
        "authors": "Seidel et al.",
        "venue": "IEEE ICCP 2019",
        "cat": "passive computational periscopy occlusion edge ordinary camera",
        "summary": "Uses a known wall edge as a natural aperture so one ordinary-camera penumbra photograph can jointly estimate floor albedo and a 1-D angular representation of the hidden scene.",
    },
    {
        "title": "Multi-Depth Computational Periscopy with an Ordinary Camera",
        "key": "saundersMultiDepthPeriscopy2020",
        "doi": "10.1109/ICASSP40776.2020.9054518",
        "url": "https://doi.org/10.1109/ICASSP40776.2020.9054518",
        "year": 2020,
        "authors": "Saunders et al.",
        "venue": "IEEE ICASSP 2020, 9299–9305",
        "cat": "passive computational periscopy occlusion multi-depth ordinary camera",
        "summary": "Extends ordinary-camera computational periscopy to a multi-depth hidden scene, recovering two hidden images and their wall-relative depths from a single photograph.",
    },
    {
        "title": "Two-Dimensional Non-Line-of-Sight Scene Estimation From a Single Edge Occluder",
        "key": "seidelTwoDimensionalNonLineofSightScene2020",
        "doi": "10.1109/TCI.2020.3037405",
        "url": "https://doi.org/10.1109/TCI.2020.3037405",
        "year": 2021,
        "authors": "Seidel et al.",
        "venue": "IEEE Transactions on Computational Imaging 7, 58–72 (2021)",
        "cat": "passive computational periscopy occlusion edge 2d range ordinary camera",
        "summary": "Adds range to edge-occluder angular sensing, reconstructing a 2-D hidden scene from one penumbra photograph with radial-falloff modeling, inversion algorithms, and Cramér–Rao analysis.",
    },
    {
        "title": "Fast Computational Periscopy in Challenging Ambient Light Conditions through Optimized Preconditioning",
        "key": "saundersFastPeriscopy2021",
        "doi": "10.1109/ICCP51581.2021.9466264",
        "url": "https://doi.org/10.1109/ICCP51581.2021.9466264",
        "year": 2021,
        "authors": "Saunders and Goyal",
        "venue": "IEEE ICCP 2021, 1–9",
        "cat": "passive computational periscopy ambient light preconditioning ordinary camera",
        "summary": "Uses optimized preconditioning to reject strong ambient background while improving inverse conditioning, making passive computational periscopy substantially more robust and faster.",
    },
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:160]}")


def esc_js(value):
    return str(value).replace("\\", "\\\\").replace('"', '\\"')


# README: add only records that are genuinely absent from the public paper list.
readme = read("README.md")
readme = re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*", f"**Update run: {DATE_LONG}.**", readme, count=1)
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README Latest Additions")
for p in reversed(PAPERS):
    if p["doi"].casefold() not in readme.casefold() and p["title"] not in readme:
        row = f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["summary"]} |\n'
        readme = readme.replace(header, header + row, 1)

# Historical trajectory: append concise lineage statements to the first year line in the text timeline.
readme_year_sentences = {
    2019: "   │     Seidel et al.: a single wall edge becomes a natural aperture, enabling one-photograph angular hidden-scene estimation [IEEE ICCP]",
    2020: "   │     Saunders et al.: multi-depth computational periscopy recovers two hidden images together with their wall-relative depths from one ordinary photograph [IEEE ICASSP]",
    2021: "   │     Seidel et al. add angle-and-range 2-D edge-camera reconstruction, while Saunders and Goyal improve strong-background robustness with optimized preconditioning [IEEE TCI / IEEE ICCP]",
}
for year, sentence in readme_year_sentences.items():
    if sentence not in readme:
        pat = re.compile(rf"(?m)^(?P<line>{year}\s+──.*)$")
        m = pat.search(readme)
        if not m:
            raise RuntimeError(f"README timeline year {year} not found")
        readme = readme[:m.end()] + "\n" + sentence + readme[m.end():]
write("README.md", readme)

# Canonical V2 paper corpus and timeline.
data = read("data/papers-source.html")
array_anchor = "    const papers=[\n"
require(data, array_anchor, "V2 papers array")
for p in PAPERS:
    if p["doi"].casefold() in data.casefold() or p["title"] in data:
        continue
    obj = (
        f'      {{cat:"{esc_js(p["cat"])}",title:"{esc_js(p["title"])}",authors:"{esc_js(p["authors"])}",'
        f'year:{p["year"]},venue:"{esc_js(p["venue"])}",url:"{esc_js(p["url"])}",key:"{esc_js(p["summary"])}"}},\n'
    )
    data = data.replace(array_anchor, array_anchor + obj, 1)

v2_sentences = {
    2019: " Seidel et al. turned a single wall edge into a natural aperture for one-photograph angular computational periscopy.",
    2020: " Multi-depth computational periscopy then recovered two hidden images together with their wall-relative depths from one ordinary photograph.",
    2021: " Edge-occluder periscopy expanded to two-dimensional angle/range estimation and optimized preconditioning improved recovery under strong ambient background.",
}
for year, sentence in v2_sentences.items():
    if sentence.strip() not in data:
        year_pat = re.compile(rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)', re.S)
        m = year_pat.search(data)
        if not m:
            raise RuntimeError(f"V2 {year} timeline block not found")
        data = data[:m.start(2)] + m.group(2) + sentence + data[m.end(2):]

# Recompute the V2 tracked-entry counter from the canonical object array rather than guessing.
count_pat = re.compile(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>')
m = count_pat.search(data)
if not m:
    raise RuntimeError("V2 tracked-entry counter not found")
actual = data.count('{cat:')
data = data[:m.start()] + m.group(0).replace(f">{m.group(1)}<", f">{actual}<") + data[m.end():]
write("data/papers-source.html", data)

# Survey prose: place the lineage in the conventional-camera computational-periscopy discussion.
survey = read("article/3passive.tex")
insert_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{White-light and single-shot speckle correlation.}"
require(survey, insert_anchor, "computational-periscopy prose insertion")
if "saundersMultiDepthPeriscopy2020" not in survey or "saundersFastPeriscopy2021" not in survey:
    block = r"""\vspace{0.8mm}
\noindent \textbf{From edge apertures to multi-depth and background-robust computational periscopy.}
Ordinary-camera computational periscopy first showed that a partial occluder can turn steady-state wall intensity into an informative coded measurement of a hidden scene~\cite{saundersComputationalPeriscopyOrdinary2019}. Seidel~\etal~then specialized this idea to the ubiquitous edge of a wall: a single photograph of its floor penumbra supports joint estimation of floor albedo and a one-dimensional angular hidden-scene representation~\cite{DBLP:conf/iccp/SeidelMMSFYG19}. Saunders~\etal~extended the same ordinary-camera setting to multiple hidden depths, recovering two hidden images together with their distances from the visible wall from one photograph~\cite{saundersMultiDepthPeriscopy2020}. Seidel~\etal~subsequently added range to the edge-camera model, producing a two-dimensional angle--range hidden-scene estimate with radial falloff modeling and statistical performance analysis~\cite{seidelTwoDimensionalNonLineofSightScene2020}. Finally, Saunders and Goyal replaced simple background cancellation with optimized preconditioning that jointly suppresses plausible ambient components and improves inverse conditioning, making computational periscopy more practical in challenging illumination~\cite{saundersFastPeriscopy2021}. This sequence fills the transition from the original passive periscope to later learned, diffusion-based, long-range, spectral, and geometry-aware occluder-aided methods.

"""
    survey = survey.replace(insert_anchor, block + insert_anchor, 1)

# Expand the partial-occluder table row with the two previously missing successors.
old = r"DBLP:conf/iccp/SeidelMMSFYG19,saundersComputationalPeriscopyOrdinary2019,seidelTwoDimensionalNonLineofSightScene2020}"
new = r"DBLP:conf/iccp/SeidelMMSFYG19,saundersComputationalPeriscopyOrdinary2019,saundersMultiDepthPeriscopy2020,seidelTwoDimensionalNonLineofSightScene2020,saundersFastPeriscopy2021}"
if "saundersMultiDepthPeriscopy2020" not in survey.split("\\begin{table*}",1)[-1]:
    require(survey, old, "passive-method table citation list")
    survey = survey.replace(old, new, 1)
write("article/3passive.tex", survey)

# Merge verified BibTeX records. Preserve the existing ICCP-2019 DBLP record; replace the
# existing arXiv-only TCI key in place and add the two missing conference records.
staging_path = ROOT / "egbib_20260822_computational_periscopy_gap.bib"
if not staging_path.exists():
    raise RuntimeError("Missing computational-periscopy staging bibliography")
staging = staging_path.read_text(encoding="utf-8")
entry_re = re.compile(r"(?ms)^@\w+\{([^,]+),.*?^\}\s*")
staged_entries = {m.group(1).strip(): m.group(0).strip() for m in entry_re.finditer(staging)}
bib = read("egbib_merged_20260711.bib")
for key in ["saundersMultiDepthPeriscopy2020", "seidelTwoDimensionalNonLineofSightScene2020", "saundersFastPeriscopy2021"]:
    if key not in staged_entries:
        raise RuntimeError(f"Missing staged BibTeX entry: {key}")
    entry = staged_entries[key]
    matches = list(entry_re.finditer(bib))
    existing = next((m for m in matches if m.group(1).strip().casefold() == key.casefold()), None)
    if existing:
        bib = bib[:existing.start()] + entry + "\n\n" + bib[existing.end():]
    else:
        bib = bib.rstrip() + "\n\n" + entry + "\n"
write("egbib_merged_20260711.bib", bib)

# Survey provenance marker.
tex = read("bare_jrnl.tex")
marker = "% 22 August 2026 computational-periscopy citation trace: edge-aperture, multi-depth, final TCI metadata, and optimized-preconditioning lineage synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)

# Mark the historical gap note integrated, preserving it as provenance.
note_path = ROOT / "updates/2026-08-22-computational-periscopy-citation-gap.md"
if note_path.exists():
    note = note_path.read_text(encoding="utf-8")
    status = "**Integrated on 22 August 2026.** README, the canonical V2 corpus/timeline, passive-survey prose/table, final-venue BibTeX, and the rebuilt survey PDF are synchronized by the guarded integration workflow.\n\n"
    if status not in note:
        note = note.replace("# 22 August 2026 — computational-periscopy forward-citation gap\n\n", "# 22 August 2026 — computational-periscopy forward-citation gap\n\n" + status, 1)
        note_path.write_text(note, encoding="utf-8")

# Staging bibliography can be removed only after its entries have been merged.
staging_path.unlink()

# Source-level assertions. PDF/citation/render checks are performed by the workflow.
readme = read("README.md"); data = read("data/papers-source.html"); survey = read("article/3passive.tex"); bib = read("egbib_merged_20260711.bib")
for p in PAPERS:
    assert p["doi"].casefold() in readme.casefold(), (p["title"], "README")
    assert p["doi"].casefold() in data.casefold(), (p["title"], "V2 corpus")
    assert p["key"] in survey, (p["key"], "survey")
for key, doi in [
    ("saundersMultiDepthPeriscopy2020", "10.1109/ICASSP40776.2020.9054518"),
    ("seidelTwoDimensionalNonLineofSightScene2020", "10.1109/TCI.2020.3037405"),
    ("saundersFastPeriscopy2021", "10.1109/ICCP51581.2021.9466264"),
]:
    assert len(re.findall(r"(?mi)^@\w+\{" + re.escape(key) + r",", bib)) == 1, (key, "BibTeX key")
    assert bib.casefold().count(doi.casefold()) == 2, (doi, "expected DOI field + DOI URL within one canonical entry")
assert data.count('{cat:') == int(re.search(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', data).group(1))
print("Computational-periscopy source integration complete")
