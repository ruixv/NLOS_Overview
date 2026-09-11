from pathlib import Path
import re

TITLE = "Automatic calibration under non-planar illumination wall in two-bounce non-line-of-sight imaging"
DOI = "10.1016/j.optlastec.2026.116183"
KEY = "chenAutoCalibrationTwoBounce2026"
DATE_LONG = "11 September 2026"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {n}")
    return text.replace(old, new, 1)


def insert_after_matching_line(text, needle, new_line):
    if new_line.strip() in text:
        return text, True
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if needle in line:
            ending = "\n" if line.endswith("\n") else ""
            lines.insert(i + 1, new_line.rstrip("\n") + ending)
            return "".join(lines), True
    return text, False


# README: latest addition + milestone timeline + update date.
readme = read("README.md")
if DOI not in readme:
    row = (
        "| 2026 | [Automatic calibration under non-planar illumination wall in two-bounce non-line-of-sight imaging]"
        "(https://doi.org/10.1016/j.optlastec.2026.116183) — Chen et al. | "
        "Optics & Laser Technology 204, 116183 (2026) | "
        "Removes the pre-calibrated planar-wall assumption from two-bounce shadow NLOS by automatically estimating "
        "the relative mapping between two relay surfaces and refining ray/shadow geometry with a full-link MLP; "
        "real experiments cover a 2.37 m × 4.6 m × 3.1 m scene with 2 cm lateral resolution. |\n"
    )
    anchor = "|------|-------|----------------|----------------|\n"
    readme = replace_once(readme, anchor, anchor + row, "README latest-additions table")

milestone = (
    "2026 ── Chen et al.: automatic calibration for non-planar two-bounce relay walls removes a major geometric-"
    "calibration barrier [Optics & Laser Technology]\n"
)
if "automatic calibration for non-planar two-bounce relay walls" not in readme:
    readme, inserted = insert_after_matching_line(readme, "Neural Illumination Fields", milestone)
    if not inserted:
        heading = "## Milestone Timeline\n"
        readme = replace_once(readme, heading, heading + "\n" + milestone, "README milestone heading")
readme = re.sub(
    r"\*\*Update run: [^*]+\.\*\*",
    f"**Update run: {DATE_LONG}.**",
    readme,
    count=1,
)
write("README.md", readme)


# Two-bounce survey prose: place after the dynamic neural-field discussion and before Keyhole Imaging.
newscenes = read("article/5newscenes.tex")
if KEY not in newscenes:
    paragraph = r'''
\vspace{0.8mm}
\noindent \textbf{Self-calibrating two-bounce imaging on non-planar relay walls.}
Moving two-bounce NLOS toward less controlled deployment, Chen~\etal~remove the assumption that the illumination wall is planar and pre-calibrated~\cite{chenAutoCalibrationTwoBounce2026}. Their method automatically estimates the relative coordinate mapping between the two relay surfaces and then jointly refines ray vectors and shadow formation with a full-link MLP optimization, compensating for spot-position errors and wall unevenness. Real experiments cover a $2.37\,\mathrm{m}\times4.6\,\mathrm{m}\times3.1\,\mathrm{m}$ scene and report $2\,\mathrm{cm}$ lateral resolution. This shifts the two-bounce trajectory from increasingly expressive neural scene representations toward self-calibrating acquisition on irregular real relay geometry.

'''
    marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Keyhole Imaging}\n"
    if marker not in newscenes:
        raise RuntimeError("could not locate Keyhole Imaging boundary in article/5newscenes.tex")
    newscenes = newscenes.replace(marker, paragraph + marker, 1)
write("article/5newscenes.tex", newscenes)


# Canonical V2 paper corpus / explorer source.
corpus = read("data/papers-source.html")
if DOI not in corpus:
    obj = (
        '      {cat:"latest active two-bounce shadow calibration irregular-relay neural",'
        'title:"Automatic calibration under non-planar illumination wall in two-bounce non-line-of-sight imaging",'
        'authors:"Chen et al.",year:2026,venue:"Optics & Laser Technology 204, 116183 (2026)",'
        'url:"https://doi.org/10.1016/j.optlastec.2026.116183",'
        'key:"Automatically estimates the relative mapping between two relay surfaces and refines ray/shadow geometry '
        'with a full-link MLP, enabling two-bounce NLOS on a non-planar illumination wall without prior planar calibration."},\n'
    )
    corpus = replace_once(corpus, "    const papers=[\n", "    const papers=[\n" + obj, "canonical paper array")

if "automatic calibration for non-planar two-bounce relay walls" not in corpus:
    marker = "</main>"
    note = (
        '<div class="internalOnly" data-update="2026-09-11">2026: Chen et al. automatic calibration for '
        'non-planar two-bounce relay walls removes a major geometric-calibration barrier.</div>\n'
    )
    corpus = replace_once(corpus, marker, note + marker, "V2 timeline provenance")

arr_start = corpus.find("    const papers=[")
arr_end = corpus.find("\n    ];", arr_start)
if arr_start < 0 or arr_end < 0:
    raise RuntimeError("could not locate canonical paper array boundaries")
tracked = corpus[arr_start:arr_end].count("{cat:")
corpus, n = re.subn(
    r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)',
    rf'\g<1>{tracked}\g<2>',
    corpus,
    count=1,
)
if n == 0:
    raise RuntimeError("could not update tracked-entry count")
corpus = re.sub(r"Last updated: [^<]+", f"Last updated: {DATE_LONG}", corpus, count=1)
write("data/papers-source.html", corpus)


# Public homepage wrapper. Its explorer content is sourced from data/papers-source.html;
# keep date/provenance synchronized without assuming an inline paper array exists here.
index = read("index.html")
if DOI not in index:
    marker = "</main>"
    metadata = (
        '<div class="internalOnly" data-paper-update="2026-09-11">'
        'Automatic calibration under non-planar illumination wall in two-bounce non-line-of-sight imaging — '
        'Optics &amp; Laser Technology 204, 116183 (2026), DOI 10.1016/j.optlastec.2026.116183. '
        'Automatic calibration for non-planar two-bounce relay walls removes a major geometric-calibration barrier.'
        '</div>\n'
    )
    index = replace_once(index, marker, metadata + marker, "homepage update provenance")
index = re.sub(r"Updated \d{1,2} [A-Z][a-z]{2} 2026", "Updated 11 Sep 2026", index)
write("index.html", index)


# Survey provenance and date. Bibliography merge is performed by the workflow afterwards.
tex = read("bare_jrnl.tex")
note = "% 11 September 2026 forward-citation trace: non-planar two-bounce auto-calibration synchronized across public artifacts.\n"
if note not in tex:
    tex = note + tex
tex = tex.replace("through 2 September 2026", "through 11 September 2026")
write("bare_jrnl.tex", tex)


# Source-level assertions before bibliography merge/build.
for path, needle in [
    ("README.md", DOI),
    ("data/papers-source.html", DOI),
    ("index.html", DOI),
    ("article/5newscenes.tex", KEY),
]:
    if needle not in read(path):
        raise RuntimeError(f"missing {needle} from {path}")

print("Two-bounce auto-calibration source integration complete")
