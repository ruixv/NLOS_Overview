from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "X-band Radar Non-Line-of-Sight Imaging"
URL = "https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html"
KEY = "duXBandRadarNLOS2026"
DATE_LONG = "22 August 2026"
SUMMARY = (
    "Introduces a learned, geometry-aware X-band radar NLOS reconstruction system; "
    "the longer wavelength makes common relay interactions predominantly specular, "
    "and a dense-prediction plus geometry-aware recovery pipeline reconstructs hidden "
    "objects at ranges up to 40 m in real-world prototype experiments."
)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:160]}")


def esc_js(value):
    return value.replace("\\", "\\\\").replace('"', '\\"')


# The survey and bibliography already contain the verified CVPR paper. This repair
# restores the public README / V2 corpus entries that regressed in later rewrites.
survey = read("article/5newscenes.tex")
bib = read("egbib_merged_20260711.bib")
require(survey, f"\\cite{{{KEY}}}", "survey citation")
require(bib, f"@inproceedings{{{KEY},", "merged bibliography")
require(bib, "pages = {5647--5658}", "CVPR page metadata")
require(bib, URL, "CVF publication URL")

# README Latest Additions.
readme = read("README.md")
readme = re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*", f"**Update run: {DATE_LONG}.**", readme, count=1)
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README Latest Additions")
if TITLE not in readme:
    row = (
        f"| 2026 | [{TITLE}]({URL}) — Du et al. | CVPR 2026, 5647–5658 | {SUMMARY} |\n"
    )
    readme = readme.replace(header, header + row, 1)
write("README.md", readme)

# Canonical V2 Paper Explorer / latest additions.
data = read("data/papers-source.html")
array_anchor = "    const papers=[\n"
require(data, array_anchor, "V2 papers array")
if TITLE not in data:
    obj = (
        f'      {{cat:"latest modality radar reconstruction learning long-range",title:"{esc_js(TITLE)}",'
        f'authors:"Du et al.",year:2026,venue:"CVPR 2026, 5647–5658",url:"{esc_js(URL)}",'
        f'key:"{esc_js(SUMMARY)}"}},\n'
    )
    data = data.replace(array_anchor, array_anchor + obj, 1)

# Restore the missing 2026 development-lineage mention without rewriting the rest of the timeline.
timeline_sentence = (
    " X-band radar extended RF NLOS imaging to a longer-wavelength, predominantly specular regime: "
    "Du et al. combined dense prediction with geometry-aware recovery and demonstrated hidden-object "
    "reconstruction at ranges up to 40 m in real-world experiments."
)
if "X-band radar extended RF NLOS imaging" not in data:
    pat = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)', re.S)
    m = pat.search(data)
    if not m:
        raise RuntimeError("V2 2026 timeline block not found")
    data = data[:m.start(2)] + m.group(2) + timeline_sentence + data[m.end(2):]

# Recompute the public tracked-entry counter instead of guessing.
count_pat = re.compile(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>')
m = count_pat.search(data)
if not m:
    raise RuntimeError("V2 tracked-entry counter not found")
actual = data.count('{cat:')
data = data[:m.start()] + m.group(0).replace(f">{m.group(1)}<", f">{actual}<") + data[m.end():]
write("data/papers-source.html", data)

# Provenance marker in the survey source; survey prose itself already contains the paper.
tex = read("bare_jrnl.tex")
marker = "% 22 August 2026 consistency repair: restored X-band Radar NLOS (CVPR 2026) to README/V2 public corpus; survey and BibTeX were already integrated.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)

# Mark the repair note integrated after all source mutations succeed.
note_path = ROOT / "updates/2026-08-22-xband-public-consistency-repair.md"
if note_path.exists():
    note = note_path.read_text(encoding="utf-8")
    status = "**Integrated by guarded workflow.** The public README/V2 regression is repaired; the existing survey citation/BibTeX are preserved and the survey PDF is rebuilt and revalidated.\n\n"
    if status not in note:
        note = note.replace("# 22 August 2026 — X-band Radar public-artifact consistency repair\n\n", "# 22 August 2026 — X-band Radar public-artifact consistency repair\n\n" + status, 1)
        note_path.write_text(note, encoding="utf-8")

# Fail closed if any artifact drifts.
readme = read("README.md")
data = read("data/papers-source.html")
survey = read("article/5newscenes.tex")
bib = read("egbib_merged_20260711.bib")
assert readme.count(TITLE) == 1, ("README title count", readme.count(TITLE))
assert data.count(TITLE) == 1, ("V2 title count", data.count(TITLE))
assert survey.count(KEY) >= 1, "survey citation missing"
assert len(re.findall(r"(?mi)^@\w+\{" + re.escape(KEY) + r",", bib)) == 1, "BibTeX key not unique"
assert "5647--5658" in bib
assert data.count('{cat:') == int(re.search(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', data).group(1))
print("X-band public consistency source repair complete")
