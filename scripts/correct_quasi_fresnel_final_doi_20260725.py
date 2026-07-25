#!/usr/bin/env python3
"""Replace the Quasi-Fresnel preprint-facing metadata with its verified Optica DOI.

This update is intentionally narrow and fail-closed: every public artifact must
contain exactly one old record or already contain exactly one corrected record.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
BIB = ROOT / "egbib_merged_20260711.bib"
SURVEY = ROOT / "bare_jrnl.tex"
NOTE = ROOT / "updates" / "2026-07-25-quasi-fresnel-final-doi.md"

TITLE = "Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform"
OLD_URL = "https://arxiv.org/abs/2508.02003"
NEW_URL = "https://doi.org/10.1364/OPTICA.604217"
DOI = "10.1364/OPTICA.604217"
TRACE = "% 25 July 2026 venue correction: Quasi-Fresnel NLOS updated from arXiv-only metadata to its registered Optica DOI."


def read(path):
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write(path, text):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def replace_exact_once(text, old, new, label):
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise SystemExit(f"{label}: expected one old record or one corrected record; old count={count}")


readme = read(README)
index = read(INDEX)
bib = read(BIB)
survey = read(SURVEY)

old_readme = f"| 2025 | [{TITLE}]({OLD_URL}) — Wei et al. | arXiv 2025 | Recasts hidden scenes as 2D functions and reduces runtime/memory by orders of magnitude for lightweight NLOS. |"
new_readme = f"| 2026 | [{TITLE}]({NEW_URL}) — Wei et al. | Optica 2026 (accepted) | Recasts common hidden surfaces and aggregated measurements as two-dimensional functions and derives a direct Quasi-Fresnel inverse with substantially lower runtime and memory. The Optica DOI is registered; arXiv:2508.02003 remains the auxiliary preprint source. |"
readme = replace_exact_once(readme, old_readme, new_readme, "README")

old_index = f'{{cat:"latest active",title:"{TITLE}",authors:"Wei et al.",year:2025,venue:"arXiv 2025",url:"{OLD_URL}",key:"2D hidden-scene representation and Quasi-Fresnel direct inversion for lightweight/mobile NLOS."}}'
new_index = f'{{cat:"latest active reconstruction efficient transform accepted",title:"{TITLE}",authors:"Wei et al.",year:2026,venue:"Optica 2026 (accepted)",url:"{NEW_URL}",key:"Represents common hidden surfaces and aggregated measurements as two-dimensional functions and derives a direct Quasi-Fresnel inverse with substantially lower runtime and memory; the final Optica DOI is registered."}}'
index = replace_exact_once(index, old_index, new_index, "index.html")

entry_re = re.compile(r"(?ms)^@article\{weiQuasiFresnel2026,.*?^\}\s*")
m = entry_re.search(bib)
new_entry = r'''@article{weiQuasiFresnel2026,
  author = {Wei, Yijun and Wang, Jianyu and Xiao, Leping and Shi, Zuoqiang and Fu, Xing and Qiu, Lingyun},
  title = {Fast and Memory-Efficient Non-Line-of-Sight Imaging with Quasi-Fresnel Transform},
  journal = {Optica},
  year = {2026},
  note = {Accepted for publication; also available as arXiv:2508.02003},
  doi = {10.1364/OPTICA.604217},
  url = {https://doi.org/10.1364/OPTICA.604217},
  eprint = {2508.02003},
  archivePrefix = {arXiv}
}
'''
if m:
    bib = bib[:m.start()] + new_entry + bib[m.end():]
elif DOI.lower() not in bib.lower():
    raise SystemExit("Bibliography entry weiQuasiFresnel2026 is missing")

if TRACE not in survey:
    anchor = "%% bare_jrnl.tex\n"
    if survey.count(anchor) != 1:
        raise SystemExit("Survey trace anchor is ambiguous")
    survey = survey.replace(anchor, anchor + TRACE + "\n", 1)

# Final uniqueness and metadata checks.
for text, label in ((readme, "README"), (index, "index.html")):
    if text.lower().count(TITLE.lower()) != 1:
        raise SystemExit(f"{label}: title is not unique")
    if NEW_URL not in text:
        raise SystemExit(f"{label}: final DOI URL missing")
if bib.lower().count(DOI.lower()) != 2:  # doi field + URL field in one entry
    raise SystemExit("Bibliography DOI occurrence count is not exactly two")

note = '''# Quasi-Fresnel NLOS final-DOI correction — 25 July 2026

The Optica publisher page now confirms that *Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform* has been accepted and that DOI `10.1364/OPTICA.604217` is registered. README, website, and bibliography now use the Optica accepted-paper record rather than labeling the work only as arXiv 2025. The arXiv identifier is retained as auxiliary metadata because volume, issue, and page details are not yet public.
'''

for path, text in ((README, readme), (INDEX, index), (BIB, bib), (SURVEY, survey), (NOTE, note)):
    write(path, text)
print("Quasi-Fresnel Optica DOI synchronized.")
