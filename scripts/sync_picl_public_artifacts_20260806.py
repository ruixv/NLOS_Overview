from pathlib import Path
import re

README = Path("README.md")
INDEX = Path("index.html")
TEX = Path("bare_jrnl.tex")
NOTE = Path("updates/2026-08-06-picl-public-artifact-sync.md")

TITLE = "Non-line-of-sight imaging via physics-informed cascade learning"
DOI = "10.1364/JOSAA.593401"
PICL_KEY = "zhaoPICL2026"
FINAL_TITLE = "Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors"
FINAL_URL = "https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Generalizable_Non-Line-of-Sight_Imaging_with_Learnable_Physical_Priors_ICCV_2025_paper.html"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


readme = README.read_text(encoding="utf-8")
readme = replace_once(
    readme,
    "**Update run: 3 August 2026.**",
    "**Update run: 6 August 2026.**",
    "README update date",
)
header = "|------|-------|----------------|----------------|\n"
picl_row = (
    "| 2026 | [Non-line-of-sight imaging via physics-informed cascade learning]"
    "(https://doi.org/10.1364/JOSAA.593401) — Zhao et al. | "
    "Journal of the Optical Society of America A 43(9), E9–E18 (2026) | "
    "PICL cascades a lightweight SPAD-specific noise-separation network with a reconstruction network that embeds a differentiable NLOS forward model. The self-supervised physical-consistency objective avoids dependence on large paired datasets and improves robustness under mixed dark-count, timing-jitter, and low-SNR interference. |\n"
)
if picl_row not in readme:
    readme = replace_once(readme, header, header + picl_row, "README latest-additions header")

old_generalizable = (
    "| 2024 | [Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors]"
    "(https://arxiv.org/abs/2409.14011) — Sun et al. | arXiv 2024 | "
    "Learns path-compensation and adaptive phasor-field priors for cross-system and low-SNR NLOS generalization. |"
)
new_generalizable = (
    "| 2025 | [Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors]"
    f"({FINAL_URL}) — Sun et al. | ICCV 2025, 25040–25049 | "
    "Learns path-compensation and adaptive phasor-field priors for cross-system and low-SNR NLOS generalization. |"
)
readme = replace_once(readme, old_generalizable, new_generalizable, "README Generalizable final venue")
README.write_text(readme, encoding="utf-8")

html = INDEX.read_text(encoding="utf-8")
html = replace_once(html, "Updated 3 August 2026 · 210+ papers", "Updated 6 August 2026 · 210+ papers", "website hero date")
html = replace_once(html, "Last updated: 3 August 2026", "Last updated: 6 August 2026", "website footer date")
html = replace_once(html, '<b>256</b><span>tracked latest entries</span>', '<b>257</b><span>tracked latest entries</span>', "website explorer counter")

papers_marker = "    const papers=[\n"
picl_object = (
    "      {cat:\"latest active learning transient spad physics-informed self-supervised denoising\","
    "title:\"Non-line-of-sight imaging via physics-informed cascade learning\","
    "authors:\"Zhao et al.\",year:2026,venue:\"JOSA A 43(9), E9–E18\","
    "url:\"https://doi.org/10.1364/JOSAA.593401\","
    "key:\"PICL cascades SPAD-specific mixed-noise separation with differentiable-physics self-supervised reconstruction, avoiding large paired NLOS datasets while improving low-SNR robustness.\"},\n"
)
if TITLE not in html:
    html = replace_once(html, papers_marker, papers_marker + picl_object, "website paper-array marker")

old_object = (
    '      {cat:"latest learning active",title:"Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors",'
    'authors:"Sun et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2409.14011",'
    'key:"Learnable path compensation and adaptive phasor-field priors for cross-system and low-SNR generalization."},'
)
new_object = (
    '      {cat:"latest learning active",title:"Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors",'
    'authors:"Sun et al.",year:2025,venue:"ICCV 2025, 25040–25049",'
    f'url:"{FINAL_URL}",'
    'key:"Learnable path compensation and adaptive phasor-field priors for cross-system and low-SNR generalization."},'
)
html = replace_once(html, old_object, new_object, "website Generalizable final venue")

dup_sentence = (
    "Polarization-encoded spatial multiplexing separated speckles from multiple optical-memory-effect regions in a single exposure, "
    "expanding steady-state around-corner imaging beyond the conventional memory-effect field of view."
)
if html.count(dup_sentence) != 3:
    raise RuntimeError(f"website duplicate sentence: expected 3 matches, found {html.count(dup_sentence)}")
first = html.find(dup_sentence)
prefix = html[: first + len(dup_sentence)]
suffix = html[first + len(dup_sentence):].replace(" " + dup_sentence, "", 2)
html = prefix + suffix
INDEX.write_text(html, encoding="utf-8")

tex = TEX.read_text(encoding="utf-8")
marker = "% 6 August 2026 consistency audit: PICL public records and final ICCV metadata synchronized; survey citation and bibliography revalidated.\n"
if marker not in tex:
    tex = marker + tex
tex = replace_once(
    tex,
    "This update extends coverage to include significant advances from 2022 through 26 July 2026.",
    "This update extends coverage to include significant advances from 2022 through 6 August 2026.",
    "survey coverage date",
)
TEX.write_text(tex, encoding="utf-8")

NOTE.parent.mkdir(parents=True, exist_ok=True)
NOTE.write_text(
    """# 6 August 2026 PICL and final-venue consistency audit

## Public-artifact synchronization

- Added **Non-line-of-sight imaging via physics-informed cascade learning** (Zhao et al., *Journal of the Optical Society of America A* 43(9), E9–E18, 2026; DOI `10.1364/JOSAA.593401`) to the README Latest Additions table and website paper explorer.
- Retained its existing semantically integrated survey discussion and canonical bibliography entry under `zhaoPICL2026`.
- Corrected **Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors** from arXiv-only 2024 metadata to its final ICCV 2025 record (pp. 25040–25049) in README and website.
- Removed two duplicate copies of the polarization-encoded spatial-multiplexing sentence in the 2026 website timeline.
- Advanced the public update date to 6 August 2026 and rebuilt the survey PDF after revalidating the source, bibliography, and rendered references.

## Scope decision

The current search and forward-citation pass did not verify another high-confidence missing direct NLOS paper newer than the repository's latest covered publications. PICL was already present in the survey source, merged bibliography, and PDF, but missing from the two main discovery surfaces; this update closes that inconsistency rather than duplicating the survey prose.
""",
    encoding="utf-8",
)

# Source-level invariants before the workflow compiles the PDF.
readme = README.read_text(encoding="utf-8")
html = INDEX.read_text(encoding="utf-8")
tex = TEX.read_text(encoding="utf-8")
bib = Path("egbib_merged_20260711.bib").read_text(encoding="utf-8")
article = Path("article/4datadriven.tex").read_text(encoding="utf-8")
assert readme.count(TITLE) == 1
assert html.count(TITLE) == 1
assert DOI in readme and DOI in html
assert html.count(dup_sentence) == 1
assert FINAL_URL in readme and FINAL_URL in html
assert "year:2024,venue:\"arXiv 2024\"" not in html[html.find(FINAL_TITLE):html.find(FINAL_TITLE) + 500]
assert len(re.findall(r"@article\{zhaoPICL2026,", bib, flags=re.I)) == 1
assert article.count(PICL_KEY) == 1
assert "through 6 August 2026" in tex
print("PICL public-artifact synchronization applied successfully")
