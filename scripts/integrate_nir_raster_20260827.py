from pathlib import Path
import re

TITLE = "Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength"
DOI = "10.1109/ICEE67339.2025.11213924"
KEY = "roueinfarNIRRaster2025"
STAGING_KEY = "roueinfarNIRRasterNLOS2025"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {n}")
    return text.replace(old, new, 1)


def doi_field_count(text):
    return len(re.findall(r"(?mi)^\s*doi\s*=\s*\{" + re.escape(DOI) + r"\}\s*,?\s*$", text))


# README: the timeline already mentions the method; close the missing Latest Additions entry.
readme = read("README.md")
if DOI not in readme:
    row = (
        "| 2025 | [Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength]"
        "(https://doi.org/10.1109/ICEE67339.2025.11213924) — Roueinfar and Salmanian | "
        "IEEE ICEE 2025, 1175–1179 | "
        "Demonstrates a low-complexity active NIR NLOS system using an 808-nm, 500-mW laser raster-scanned "
        "over a relay wall by a pan–tilt unit; an NIR camera records three-bounce returns for three simple hidden "
        "targets, with reconstruction error evaluated by MSE/RMSE. The final IEEE venue supersedes the later "
        "arXiv:2607.04183 upload. |\n"
    )
    anchor = "|------|-------|----------------|----------------|\n"
    readme = replace_once(readme, anchor, anchor + row, "README Latest Additions")
readme = re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*", "**Update run: 27 August 2026.**", readme, count=1)
write("README.md", readme)


# Public V2 wrapper date.
index = read("index.html")
index = re.sub(r"Updated \d{1,2} Aug 2026", "Updated 27 Aug 2026", index, count=1)
write("index.html", index)


# Canonical paper corpus / Paper Explorer. The 2025 timeline already contains this lineage; do not duplicate it.
corpus = read("data/papers-source.html")
if DOI not in corpus:
    obj = (
        '      {cat:"latest active optical steady-state nir raster-scan conventional-camera hardware",'
        'title:"Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength",'
        'authors:"Roueinfar and Salmanian",year:2025,venue:"IEEE ICEE 2025, 1175–1179",'
        'url:"https://doi.org/10.1109/ICEE67339.2025.11213924",'
        'key:"Uses an 808-nm, 500-mW NIR laser on a pan–tilt raster scan and an NIR camera to recover simple hidden targets from three-bounce relay-wall returns; the final IEEE ICEE 2025 publication supersedes the later arXiv upload."},\n'
    )
    anchor = "    const papers=[\n"
    corpus = replace_once(corpus, anchor, anchor + obj, "canonical paper array")

arr_start = corpus.find("    const papers=[")
arr_end = corpus.find("\n    ];", arr_start)
if arr_start < 0 or arr_end < 0:
    raise RuntimeError("canonical paper array boundaries not found")
tracked = corpus[arr_start:arr_end].count("{cat:")
corpus, n = re.subn(
    r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)',
    rf'\g<1>{tracked}\g<2>', corpus, count=1,
)
if n != 1:
    raise RuntimeError("tracked-entry counter not found")
corpus = re.sub(r"Updated \d{1,2} August 2026", "Updated 27 August 2026", corpus, count=1)
corpus = re.sub(r"Last updated: \d{1,2} August 2026", "Last updated: 27 August 2026", corpus, count=1)
write("data/papers-source.html", corpus)


# Survey body already uses this canonical key. Fail closed if that integration regressed.
active = read("article/2active.tex")
if KEY not in active or "raster" not in active.lower():
    raise RuntimeError("existing NIR survey integration/canonical citation key is missing")


# Canonical bibliography: normalize any staging-key form to the survey's already-used key.
bib = read("egbib_merged_20260711.bib")
if STAGING_KEY in bib and KEY not in bib:
    bib = bib.replace(STAGING_KEY, KEY)

key_n = len(re.findall(r"@[A-Za-z]+\{" + re.escape(KEY) + r",", bib, flags=re.I))
doi_n = doi_field_count(bib)
if key_n == 0 and doi_n == 0:
    stage = read("egbib_20260827_nir_raster_scan_gap.bib")
    stage = stage.replace(STAGING_KEY, KEY)
    bib = bib.rstrip() + "\n\n" + stage.strip() + "\n"
elif key_n != 1 or doi_n != 1:
    raise RuntimeError(f"bibliography inconsistent before normalization: key={key_n}, doi_field={doi_n}")

key_n = len(re.findall(r"@[A-Za-z]+\{" + re.escape(KEY) + r",", bib, flags=re.I))
doi_n = doi_field_count(bib)
if key_n != 1 or doi_n != 1:
    raise RuntimeError(f"bibliography normalization failed: key={key_n}, doi_field={doi_n}")
write("egbib_merged_20260711.bib", bib)


# Survey provenance/date marker; no duplicate literature prose is added because article/2active.tex already contains it.
tex = read("bare_jrnl.tex")
note = "% 27 August 2026 consistency pass: finalized IEEE ICEE venue and synchronized the NIR raster-scan NLOS record across public artifacts.\n"
if note not in tex:
    tex = note + tex
tex = re.sub(r"through \d{1,2} August 2026", "through 27 August 2026", tex, count=1)
write("bare_jrnl.tex", tex)


# Final source-level assertions.
checks = {
    "README.md": [TITLE, DOI],
    "data/papers-source.html": [TITLE, DOI],
    "article/2active.tex": [KEY],
    "egbib_merged_20260711.bib": [KEY, DOI],
    "bare_jrnl.tex": ["27 August 2026 consistency pass"],
}
for path, needles in checks.items():
    text = read(path)
    for needle in needles:
        if needle not in text:
            raise RuntimeError(f"missing {needle!r} from {path}")
if "raster" not in read("article/2active.tex").lower():
    raise RuntimeError("NIR raster-scan survey semantics not found")

print(f"Integrated {TITLE}; canonical key={KEY}; tracked={tracked}")
