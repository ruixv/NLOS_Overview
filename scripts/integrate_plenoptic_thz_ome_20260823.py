from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATE_LONG = "23 August 2026"

PAPERS = [
    {
        "title": "Single-shot imaging through scattering media and around the corner beyond the OME range via polarization-encoded spatial multiplexing",
        "key": "weiPolarizationEncodedOMEMultiplexing2026",
        "doi": "10.1016/j.optlaseng.2026.109602",
        "url": "https://doi.org/10.1016/j.optlaseng.2026.109602",
        "year": 2026,
        "authors": "Wei et al.",
        "venue": "Optics and Lasers in Engineering 200, 109602 (2026)",
        "cat": "passive speckle polarization optical memory effect single-shot around-corner scattering",
        "summary": "Uses polarization-encoded spatial multiplexing and robust speckle demultiplexing to reconstruct multiple around-corner targets in one exposure beyond the conventional optical-memory-effect field of view.",
    },
    {
        "title": "Combined geometric and physical optics analysis of passive non-line-of-sight light-field measurement",
        "key": "sasakiCombinedOpticsPassiveNLOS2025",
        "doi": "10.1364/OE.568818",
        "url": "https://doi.org/10.1364/OE.568818",
        "year": 2025,
        "authors": "Sasaki, Grossman, Leger",
        "venue": "Optics Express 33(19), 39194–39217 (2025)",
        "cat": "passive light-field plenoptic thermal infrared terahertz rough wall BRDF Wigner",
        "summary": "Unifies geometric-optics BRDF and physical-optics Wigner analyses to predict how roughness, wavelength, diffraction, and lens focusing govern retrievable passive NLOS light-field information in LWIR and THz regimes.",
    },
    {
        "title": "Estimation of the 3D spatial location of non-line-of-sight objects using passive THz plenoptic measurements",
        "key": "sasakiPassiveTHzPlenoptic2022",
        "doi": "10.1364/OE.472069",
        "url": "https://doi.org/10.1364/OE.472069",
        "year": 2022,
        "authors": "Sasaki, Grossman, Leger",
        "venue": "Optics Express 30(23), 41911–41921 (2022)",
        "cat": "passive terahertz THz light-field plenoptic 3D localization rough wall",
        "summary": "Measures spatial and angular THz radiation reflected from rough walls with a room-temperature sensor and refocuses the resulting plenoptic data to recover the 3D location of hidden human-like thermal targets.",
    },
    {
        "title": "Passive Terahertz Non-Line-of-Sight Imaging",
        "key": "grossmanPassiveTHzNLOS2022",
        "doi": "10.1109/TTHZ.2022.3173168",
        "url": "https://doi.org/10.1109/TTHZ.2022.3173168",
        "year": 2022,
        "authors": "Grossman, Sasaki, Leger",
        "venue": "IEEE Transactions on Terahertz Science and Technology 12(5), 489–498 (2022)",
        "cat": "passive terahertz THz NLOS imaging human rough surface single-pixel",
        "summary": "Demonstrates passive 336-GHz NLOS human imaging from ordinary rough-surface reflections using uncooled direct-detection hardware, recovering target location, orientation, and pose even for weak specular components.",
    },
    {
        "title": "Passive 3D location estimation of non-line-of-sight objects from a scattered thermal infrared light field",
        "key": "sasakiThermalIRPlenopticNLOS2021",
        "doi": "10.1364/OE.445181",
        "url": "https://doi.org/10.1364/OE.445181",
        "year": 2021,
        "authors": "Sasaki, Hashemi, Leger",
        "venue": "Optics Express 29(26), 43642–43661 (2021)",
        "cat": "passive thermal infrared LWIR light-field plenoptic 3D localization",
        "summary": "Scans an infrared camera to form a scattered LWIR light-field cube, separates the weak information-bearing component, and localizes human-temperature hidden objects in 3D in a life-size diffusive hallway.",
    },
    {
        "title": "Non-line-of-sight object location estimation from scattered light using plenoptic data",
        "key": "sasakiPlenopticNLOSLocation2021",
        "doi": "10.1364/JOSAA.394846",
        "url": "https://doi.org/10.1364/JOSAA.394846",
        "year": 2021,
        "authors": "Sasaki, Leger",
        "venue": "Journal of the Optical Society of America A 38(2), 211–228 (2021)",
        "cat": "passive light-field plenoptic NLOS localization rough wall spatial frequency",
        "summary": "Derives depth/transverse localization limits from scattering physics and noise, then uses a projection-slice/light-field formulation and mixed-space-frequency filtering to estimate hidden-object location near the theoretical resolution limit.",
    },
    {
        "title": "Light field reconstruction from scattered light using plenoptic data",
        "key": "sasakiPlenopticScatteredLight2020",
        "doi": "10.1364/JOSAA.378714",
        "url": "https://doi.org/10.1364/JOSAA.378714",
        "year": 2020,
        "authors": "Sasaki, Leger",
        "venue": "Journal of the Optical Society of America A 37(4), 653–670 (2020)",
        "cat": "passive light-field plenoptic scattering BRDF inverse problem",
        "summary": "Provides the scattered-light plenoptic inverse foundation: a BRDF-aware Fredholm light-field model, regularized reconstruction, and limits on retrievable hidden-scene information after wall scattering.",
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


# README: add verified missing papers, refresh update date, and extend the historical trajectory.
readme = read("README.md")
readme = re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*", f"**Update run: {DATE_LONG}.**", readme, count=1)
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README Latest Additions")
for p in reversed(PAPERS):
    if p["doi"].casefold() not in readme.casefold() and p["title"] not in readme:
        row = f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["summary"]} |\n'
        readme = readme.replace(header, header + row, 1)

readme_year_sentences = {
    2020: "   │     Sasaki and Leger formulate wall-scattered plenoptic inversion with a BRDF-aware Fredholm model and explicit limits on retrievable hidden-scene information [JOSA A]",
    2021: "   │     Plenoptic passive NLOS gains quantitative depth/transverse localization and then life-size 3D LWIR hidden-object localization from scattered thermal light fields [JOSA A / Optics Express]",
    2022: "   │     Passive THz NLOS uses rough-wall specular components for hidden-human imaging and plenoptic refocusing for 3D localization with room-temperature sensing [IEEE T-THz / Optics Express]",
    2025: "   │     A unified geometric-/physical-optics light-field analysis connects roughness, wavelength, diffraction, and focusing across passive LWIR and THz NLOS [Optics Express]",
    2026: "   │     Polarization-encoded spatial multiplexing pushes single-shot speckle around-corner imaging beyond the conventional optical-memory-effect field of view [Optics and Lasers in Engineering]",
}
for year, sentence in readme_year_sentences.items():
    if sentence not in readme:
        pat = re.compile(rf"(?m)^(?P<line>{year}\s+──.*)$")
        m = pat.search(readme)
        if not m:
            raise RuntimeError(f"README timeline year {year} not found")
        readme = readme[:m.end()] + "\n" + sentence + readme[m.end():]
write("README.md", readme)

# Canonical V2 corpus: add objects, timeline context, date, and recompute entry counter.
data = read("data/papers-source.html")
data = data.replace("Updated 22 August 2026", "Updated 23 August 2026")
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
    2020: " Sasaki and Leger established BRDF-aware plenoptic inversion of wall-scattered hidden-scene light fields and quantified retrievable-information limits.",
    2021: " The same plenoptic branch progressed from scattering-limited depth/transverse localization to passive 3D LWIR localization of human-temperature targets in a life-size hallway.",
    2022: " Passive THz NLOS then exploited rough-wall specular components for hidden-human imaging and spatial-angular plenoptic refocusing for 3D localization.",
    2025: " A combined BRDF/Wigner analysis unified scattering- and diffraction-limited passive light-field design across LWIR and THz wavelengths.",
    2026: " Polarization-encoded spatial multiplexing enabled single-shot around-corner speckle demultiplexing beyond the conventional optical-memory-effect field of view.",
}
for year, sentence in v2_sentences.items():
    if sentence.strip() not in data:
        year_pat = re.compile(rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)', re.S)
        m = year_pat.search(data)
        if not m:
            raise RuntimeError(f"V2 {year} timeline block not found")
        data = data[:m.start(2)] + m.group(2) + sentence + data[m.end(2):]
count_pat = re.compile(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>')
m = count_pat.search(data)
if not m:
    raise RuntimeError("V2 tracked-entry counter not found")
actual = data.count('{cat:')
data = data[:m.start()] + m.group(0).replace(f">{m.group(1)}<", f">{actual}<") + data[m.end():]
write("data/papers-source.html", data)

# Survey prose: (1) close the optical-memory-effect FOV gap; (2) restore the passive plenoptic thermal/THz lineage.
survey = read("article/3passive.tex")
ome_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Room-scale real-time passive reconstruction.}"
require(survey, ome_anchor, "OME-lineage insertion")
if "weiPolarizationEncodedOMEMultiplexing2026" not in survey:
    ome_block = r"""\vspace{0.8mm}
\noindent \textbf{Single-shot speckle imaging beyond the optical-memory-effect range.}
Speckle-correlation NLOS is attractive because it avoids ultrafast timing, but its usable field of view is normally bounded by the optical memory effect. Wei~\etal~addressed this limitation with polarization-encoded spatial multiplexing, establishing a linear mapping between the polarization-resolved camera measurement and speckles associated with distinct memory-effect regions~\cite{weiPolarizationEncodedOMEMultiplexing2026}. A two-stage N-FINDR and robust non-negative matrix-factorization demultiplexer separates those components before conventional speckle reconstruction. The method is demonstrated in both transmissive scattering and reflective around-corner configurations within a single exposure, extending earlier multi-frame component-separation approaches toward fast large-field passive NLOS.

"""
    survey = survey.replace(ome_anchor, ome_block + ome_anchor, 1)

plenoptic_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Thermal NLOS through rough relay surfaces.}"
require(survey, plenoptic_anchor, "thermal/plenoptic lineage insertion")
if "sasakiPlenopticScatteredLight2020" not in survey:
    plenoptic_block = r"""\vspace{0.8mm}
\noindent \textbf{Passive plenoptic light fields from visible scattering to thermal and THz sensing.}
A distinct passive branch preserves both spatial and angular information instead of collapsing the wall observation to a single intensity image. Sasaki and Leger first formulated reconstruction from wall-scattered plenoptic data as a BRDF-aware system of Fredholm integral equations and analyzed regularization together with fundamental limits on retrievable hidden-scene information~\cite{sasakiPlenopticScatteredLight2020}. They then connected the light field to a full spatial-frequency representation, deriving scattering- and noise-limited depth/transverse resolution and a mixed-space-frequency filter for NLOS object localization~\cite{sasakiPlenopticNLOSLocation2021}. Moving to naturally emitted radiation removed the need for visible illumination: Sasaki~\etal~scanned an LWIR camera to build a scattered light-field cube and demonstrated passive 3-D localization of human-temperature objects in a life-size diffusive hallway~\cite{sasakiThermalIRPlenopticNLOS2021}. At submillimeter wavelengths, Grossman~\etal~showed that ordinary building materials retain enough specular reflection at 336~GHz for passive one- and two-dimensional hidden-human imaging with uncooled direct-detection hardware~\cite{grossmanPassiveTHzNLOS2022}; spatial--angular THz plenoptic measurements and refocusing subsequently enabled explicit 3-D localization with a room-temperature sensor~\cite{sasakiPassiveTHzPlenoptic2022}. More recently, Sasaki~\etal~unified the scattering-limited geometric-optics regime and diffraction-limited physical-optics regime using BRDF and Wigner descriptions, respectively, yielding a design analysis that predicts how roughness, wavelength, and focusing determine recoverable passive NLOS information from LWIR through THz~\cite{sasakiCombinedOpticsPassiveNLOS2025}. This lineage broadens passive NLOS from RGB wall intensity to wavelength-dependent light-field sensing and provides a physical bridge to recent rough-wall thermal reconstruction.

"""
    survey = survey.replace(plenoptic_anchor, plenoptic_block + plenoptic_anchor, 1)
write("article/3passive.tex", survey)

# Merge only verified canonical BibTeX records; fail on DOI/key conflicts instead of silently duplicating them.
staging_path = ROOT / "egbib_20260823_plenoptic_thz_ome_gap.bib"
if not staging_path.exists():
    raise RuntimeError("Missing plenoptic/THz/OME staging bibliography")
staging = staging_path.read_text(encoding="utf-8")
entry_re = re.compile(r"(?ms)^@\w+\{([^,]+),.*?^\}\s*")
staged_entries = {m.group(1).strip(): m.group(0).strip() for m in entry_re.finditer(staging)}
bib = read("egbib_merged_20260711.bib")
for p in PAPERS:
    key, doi = p["key"], p["doi"]
    if key not in staged_entries:
        raise RuntimeError(f"Missing staged BibTeX entry: {key}")
    key_match = re.search(r"(?mi)^@\w+\{" + re.escape(key) + r",", bib)
    doi_present = doi.casefold() in bib.casefold()
    if doi_present and not key_match:
        raise RuntimeError(f"DOI already exists under another key: {doi}")
    if not key_match:
        bib = bib.rstrip() + "\n\n" + staged_entries[key] + "\n"
write("egbib_merged_20260711.bib", bib)

# Survey provenance/date marker. Preserve older provenance while making this run explicit.
tex = read("bare_jrnl.tex")
marker = "% 23 August 2026 citation/modality trace: passive plenoptic LWIR/THz light-field lineage and single-shot polarization-multiplexed beyond-OME around-corner imaging synchronized.\n"
if marker not in tex:
    tex = marker + tex
tex = re.sub(r"through 22 August 2026", "through 23 August 2026", tex, count=1)
tex = re.sub(r"Updated 22 August 2026", "Updated 23 August 2026", tex, count=1)
write("bare_jrnl.tex", tex)

# Mark update note integrated only inside the guarded checkout; it reaches master only after PDF validation succeeds.
note_path = ROOT / "updates/2026-08-23-plenoptic-thz-ome-lineage.md"
if note_path.exists():
    note = note_path.read_text(encoding="utf-8")
    status = "**Integrated on 23 August 2026.** README, canonical V2 corpus/timeline, passive-survey prose, final-venue BibTeX, and the rebuilt survey PDF were synchronized by the guarded workflow.\n\n"
    if status not in note:
        note = note.replace("# 23 August 2026 — passive plenoptic / THz / beyond-OME gap\n\n", "# 23 August 2026 — passive plenoptic / THz / beyond-OME gap\n\n" + status, 1)
        note_path.write_text(note, encoding="utf-8")

staging_path.unlink()

# Fail-closed source-level assertions. PDF/citation/render checks are performed by GitHub Actions.
readme = read("README.md"); data = read("data/papers-source.html"); survey = read("article/3passive.tex"); bib = read("egbib_merged_20260711.bib"); tex = read("bare_jrnl.tex")
for p in PAPERS:
    assert p["doi"].casefold() in readme.casefold(), (p["title"], "README")
    assert p["doi"].casefold() in data.casefold(), (p["title"], "V2 corpus")
    assert p["key"] in survey, (p["key"], "survey")
    assert len(re.findall(r"(?mi)^@\w+\{" + re.escape(p["key"]) + r",", bib)) == 1, (p["key"], "BibTeX key")
    assert bib.casefold().count(p["doi"].casefold()) == 2, (p["doi"], "expected DOI field + DOI URL")
assert "Updated 23 August 2026" in data
assert marker in tex
m = re.search(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', data)
assert m and int(m.group(1)) == data.count('{cat:'), (m.group(1) if m else None, data.count('{cat:'))
print("Passive plenoptic/THz/beyond-OME source integration complete")
