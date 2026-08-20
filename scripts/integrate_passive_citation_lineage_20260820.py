from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATE_LONG = "20 August 2026"
DATE_SHORT = "20 Aug 2026"

PAPERS = [
    {
        "title": "Hyper-NLOS: hyperspectral passive non-line-of-sight imaging",
        "key": "chenHyperNLOS2024",
        "doi": "10.1364/OE.532699",
        "url": "https://doi.org/10.1364/OE.532699",
        "year": 2024,
        "authors": "Chen et al.",
        "venue": "Optics Express 32(20), 34807–34824 (2024)",
        "cat": "latest passive hyperspectral learned reconstruction spectral fusion",
        "summary": "HFN-Net exploits wavelength-resolved relay-wall measurements with a hyperspectral full-color autoencoder and spatial–spectral attention, improving passive-NLOS color/structure recovery and introducing the HS-NLOS dataset.",
    },
    {
        "title": "Turning rough surfaces into non-line-of-sight cameras",
        "key": "liRoughSurfaceCameraNLOS2025",
        "doi": "10.1364/OPTICA.544275",
        "url": "https://doi.org/10.1364/OPTICA.544275",
        "year": 2025,
        "authors": "Li et al.",
        "venue": "Optica 12(5), 626–634 (2025)",
        "cat": "latest passive rough relay surface physical model computational periscopy keyhole",
        "summary": "Models microscale rough-wall scattering as an invertible passive encoding rather than a nuisance, enabling ordinary-camera high-resolution real-time NLOS imaging, near-90° field of view, full-color recovery, keyhole imaging, and non-invasive calibration.",
    },
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:180]}")


def esc_js(value):
    return str(value).replace("\\", "\\\\").replace('"', '\\"')


# README Latest Additions and milestone trajectory.
readme = read("README.md")
readme = re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*", f"**Update run: {DATE_LONG}.**", readme, count=1)
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README Latest Additions")
for p in reversed(PAPERS):
    if p["doi"].casefold() not in readme.casefold() and p["title"] not in readme:
        row = (
            f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | '
            f'{p["venue"]} | {p["summary"]} |\n'
        )
        readme = readme.replace(header, header + row, 1)

hyper_line = (
    "    │     Chen et al.: Hyper-NLOS introduces wavelength-resolved hyperspectral conditioning, a full-color autoencoder, "
    "and spatial–spectral attention for passive hidden-scene reconstruction [Optics Express]\n"
)
if "Chen et al.: Hyper-NLOS introduces wavelength-resolved hyperspectral conditioning" not in readme:
    anchor = (
        "    │     Hashemi et al. and Chen et al.: multispectral clutter separation and learned hyperspectral band selection "
        "strengthen passive NLOS under realistic backgrounds [IEEE TPAMI / Expert Systems with Applications]\n"
    )
    require(readme, anchor, "README hyperspectral trajectory")
    readme = readme.replace(anchor, hyper_line + anchor, 1)

rough_line = (
    "   │     Li et al.: a microscale rough-surface scattering model turns an ordinary rough relay wall into a well-conditioned "
    "passive camera, enabling real-time high-resolution and keyhole NLOS recovery [Optica]\n"
)
if "Li et al.: a microscale rough-surface scattering model" not in readme:
    anchor = (
        "2025 ── Zhou et al.: 10 m passive NLOS — pattern calibration and low-rank background separation move ordinary-camera "
        "computational periscopy to long range [Optics Letters]\n"
    )
    require(readme, anchor, "README rough-surface trajectory")
    readme = readme.replace(anchor, anchor + rough_line, 1)
write("README.md", readme)

# Canonical V2 corpus / Paper Explorer and timeline.
data = read("data/papers-source.html")
data = re.sub(r"Updated \d{1,2} August 2026", f"Updated {DATE_LONG}", data)
data = re.sub(r"Last updated: \d{1,2} August 2026", f"Last updated: {DATE_LONG}", data)
array_anchor = "    const papers=[\n"
require(data, array_anchor, "V2 papers array")
added = 0
for p in PAPERS:
    if p["doi"].casefold() in data.casefold() or p["title"] in data:
        continue
    obj = (
        f'      {{cat:"{esc_js(p["cat"])}",title:"{esc_js(p["title"])}",'
        f'authors:"{esc_js(p["authors"])}",year:{p["year"]},venue:"{esc_js(p["venue"])}",'
        f'url:"{esc_js(p["url"])}",key:"{esc_js(p["summary"])}"}},\n'
    )
    data = data.replace(array_anchor, array_anchor + obj, 1)
    added += 1
if added:
    count_pat = re.compile(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>')
    m = count_pat.search(data)
    if not m:
        raise RuntimeError("V2 tracked-entry counter not found")
    old = int(m.group(1))
    replacement = m.group(0).replace(f">{old}<", f">{old + added}<")
    data = data[:m.start()] + replacement + data[m.end():]

if "Hyper-NLOS makes wavelength-resolved hyperspectral diversity" not in data:
    year_pat = re.compile(r'(<div class="tl"><div class="year">2024</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)', re.S)
    m = year_pat.search(data)
    if not m:
        raise RuntimeError("V2 2024 timeline block not found")
    sentence = (
        " Hyper-NLOS makes wavelength-resolved hyperspectral diversity an explicit conditioning dimension for passive reconstruction, "
        "combining a full-color autoencoder with spatial–spectral attention and the HS-NLOS dataset."
    )
    data = data[:m.start(2)] + m.group(2) + sentence + data[m.end(2):]

if "rough relay wall into an ordinary-camera passive NLOS encoder" not in data:
    year_pat = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)', re.S)
    m = year_pat.search(data)
    if not m:
        raise RuntimeError("V2 2025 timeline block not found")
    sentence = (
        " Li et al. turn the microscale scattering of a rough relay wall into an ordinary-camera passive NLOS encoder, "
        "showing that realistic roughness can improve inverse conditioning rather than merely degrade image formation."
    )
    data = data[:m.start(2)] + m.group(2) + sentence + data[m.end(2):]
write("data/papers-source.html", data)

# Keep the shell homepage date synchronized with the canonical V2 corpus.
index = read("index.html")
index = re.sub(r"Updated \d{1,2} Aug 2026", f"Updated {DATE_SHORT}", index)
write("index.html", index)

# Survey prose: integrate into the passive learned/physical lineage, not as a detached list.
survey = read("article/3passive.tex")
insert_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Joint passive imaging and localization from speckle.}"
require(survey, insert_anchor, "passive learned-reconstruction insertion")
blocks = ""
if "chenHyperNLOS2024" not in survey:
    blocks += r"""\vspace{0.8mm}
\noindent \textbf{Hyperspectral conditioning for passive NLOS.}
Chen~\etal~extended steady-state passive reconstruction beyond RGB or intensity-only relay measurements by treating wavelength-resolved observations as an additional sensing dimension~\cite{chenHyperNLOS2024}. Their HFN-Net combines a hyperspectral full-color autoencoder with spatial--spectral attention so that complementary bands provide additional conditioning for the otherwise ill-posed wall-to-hidden-scene inverse, while the accompanying HS-NLOS dataset supplies wavelength-resolved training and evaluation data. This work establishes hyperspectral diversity as a direct reconstruction cue and provides a clear precursor to later band-selection, multispectral-clutter separation, polarization-assisted, and dual-spectral passive NLOS systems.

"""
if "liRoughSurfaceCameraNLOS2025" not in survey:
    blocks += r"""\vspace{0.8mm}
\noindent \textbf{Rough relay surfaces as passive cameras.}
Li~\etal~reframed realistic relay-wall roughness from a source of spatial mixing into a useful physical encoding~\cite{liRoughSurfaceCameraNLOS2025}. By modeling the wall's microscale scattering properties, they obtain a well-conditioned passive inverse and recover hidden scenes with an ordinary monochrome camera, reporting sub-millimeter spatial resolution, 25-fps temporal resolution, a field of view approaching $90^{\circ}$, full-color recovery, and millimeter-scale keyhole imaging. The same formulation supports non-invasive wall calibration without manipulating the hidden scene. This result changes the passive-NLOS trajectory from compensating for rough relays to deliberately exploiting their microscopic structure, and it supplies an optical precursor to later rough-wall thermal reconstruction.

"""
if blocks:
    survey = survey.replace(insert_anchor, blocks + insert_anchor, 1)
write("article/3passive.tex", survey)

# Merge verified BibTeX records exactly once. If an older canonical key is already
# present without final DOI metadata, replace that whole entry with the verified
# staging record instead of skipping it.
bib = read("egbib_merged_20260711.bib")
entry_pattern = re.compile(r"(?ms)^@\w+\{([^,]+),.*?^\}\s*")
for staging_rel, key, doi in [
    ("egbib_20260819_hyperspectral_passive_gap.bib", "chenHyperNLOS2024", "10.1364/OE.532699"),
    ("egbib_20260820_passive_rough_surface_gap.bib", "liRoughSurfaceCameraNLOS2025", "10.1364/OPTICA.544275"),
]:
    staging = ROOT / staging_rel
    if not staging.exists():
        raise RuntimeError(f"Missing verified staging bibliography: {staging_rel}")
    entry = staging.read_text(encoding="utf-8").strip()
    matches = list(entry_pattern.finditer(bib))
    key_match = next((m for m in matches if m.group(1).strip().casefold() == key.casefold()), None)
    doi_match = next((m for m in matches if doi.casefold() in m.group(0).casefold()), None)
    target = key_match or doi_match
    if target:
        bib = bib[:target.start()] + entry + "\n\n" + bib[target.end():]
    else:
        bib = bib.rstrip() + "\n\n" + entry + "\n"
write("egbib_merged_20260711.bib", bib)

# Provenance marker; coverage date is already 20 August for this run.
tex = read("bare_jrnl.tex")
tex = re.sub(r"through \d{1,2} August 2026\.", f"through {DATE_LONG}.", tex, count=1)
marker = "% 20 August 2026 citation trace: hyperspectral and rough-relay passive NLOS milestones synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)

# Update historical gap note so future runs do not mistake the staged record for still-pending work.
hyper_note = ROOT / "updates/2026-08-19-hyperspectral-passive-gap.md"
if hyper_note.exists():
    note_text = hyper_note.read_text(encoding="utf-8")
    if "**Integrated on 20 August 2026.**" not in note_text:
        note_text = note_text.replace(
            "## Status\n\n",
            "## Status\n\n**Integrated on 20 August 2026.** The verified paper is now synchronized across README, the canonical V2 corpus/timeline, passive survey prose, merged bibliography, and rebuilt survey PDF. The remainder of this note is retained as provenance for the earlier gap analysis.\n\n",
            1,
        )
        hyper_note.write_text(note_text, encoding="utf-8")

# Persistent audit note for this citation-lineage integration.
updates = ROOT / "updates"
updates.mkdir(exist_ok=True)
(updates / "2026-08-20-passive-citation-lineage.md").write_text(
    """# 20 August 2026 — passive NLOS citation-lineage integration

Two high-confidence missing passive-NLOS works were synchronized after keyword search and Core-paper / milestone citation tracing:

1. Mingyang Chen et al., **Hyper-NLOS: hyperspectral passive non-line-of-sight imaging**, *Optics Express* 32(20), 34807–34824 (2024), DOI `10.1364/OE.532699`. HFN-Net uses wavelength-resolved relay observations, a hyperspectral full-color autoencoder, and spatial–spectral attention; the work also introduces HS-NLOS.
2. Wenwen Li et al., **Turning rough surfaces into non-line-of-sight cameras**, *Optica* 12(5), 626–634 (2025), DOI `10.1364/OPTICA.544275`. A microscale rough-wall scattering model turns realistic relay roughness into an invertible passive encoding and supports ordinary-camera real-time/high-resolution, wide-FoV, full-color, keyhole, and non-invasive-calibration demonstrations.

The rough-surface paper is especially relevant to forward citation tracing because it sits directly downstream of the classical active-NLOS/light-transport literature and is itself a predecessor of later rough-wall thermal NLOS. Hyper-NLOS closes a different lineage gap between intensity/RGB passive reconstruction and the repository's later hyperspectral band-selection / multispectral-fusion works.

Guarded integration updates README, canonical V2 `data/papers-source.html`, the shell homepage date, `article/3passive.tex`, merged BibTeX, and survey provenance, then rebuilds and validates `bare_jrnl.pdf` before committing public artifacts.
""",
    encoding="utf-8",
)

# Remove staging BibTeX only after it has been merged into the canonical bibliography.
for rel in ["egbib_20260819_hyperspectral_passive_gap.bib", "egbib_20260820_passive_rough_surface_gap.bib"]:
    p = ROOT / rel
    if p.exists():
        p.unlink()

# Source-level assertions; the workflow performs the clean PDF validation.
assert all(p["doi"].casefold() in read("README.md").casefold() for p in PAPERS)
assert all(p["doi"].casefold() in read("data/papers-source.html").casefold() for p in PAPERS)
assert all(p["key"] in read("article/3passive.tex") for p in PAPERS)
assert all(read("egbib_merged_20260711.bib").count(p["key"]) == 1 for p in PAPERS)
assert all(read("egbib_merged_20260711.bib").casefold().count(p["doi"].casefold()) >= 1 for p in PAPERS)
assert f"through {DATE_LONG}." in read("bare_jrnl.tex")
print("Passive citation-lineage source integration complete")
