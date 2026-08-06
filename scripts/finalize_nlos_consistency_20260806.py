from pathlib import Path

ARTICLE = Path("article/5newscenes.tex")
INDEX = Path("index.html")
NOTE = Path("updates/2026-08-06-citation-and-public-artifact-sync.md")

article = ARTICLE.read_text(encoding="utf-8")
bookmark = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Acoustic NLOS Imaging}\n"
radar = "\\vspace{0.8mm}\n\\noindent \\textbf{Sub-terahertz polarimetric indoor mapping.}\nAlburadi~\\etal~demonstrated that a 222--228~GHz polarimetric FMCW radar with a mechanically scanned fan-beam antenna can combine rapid high-resolution indoor mapping with measured around-corner imaging~\\cite{alburadiPolarimetricRadarNLOS2025}. The system interprets double-bounce specular paths as hidden-scene evidence, while co- and cross-polarized channels help distinguish useful NLOS returns from direct leakage and environmental clutter. This work extends the measured mmWave lineage toward sub-terahertz carrier frequencies and emphasizes polarization as an additional physical cue for practical RF NLOS imaging.\n\n"
wrong = bookmark + radar + "\\subsection{Acoustic NLOS Imaging}\n"
right = radar + bookmark + "\\subsection{Acoustic NLOS Imaging}\n"
if wrong in article:
    article = article.replace(wrong, right, 1)
elif right not in article:
    raise RuntimeError("Could not verify the radar-to-acoustic section boundary")
if article.index(radar) > article.index(bookmark):
    raise RuntimeError("Radar paragraph still follows the acoustic bookmark")
ARTICLE.write_text(article, encoding="utf-8")

html = INDEX.read_text(encoding="utf-8")
sentence = "Polarization-encoded spatial multiplexing separated speckles from multiple optical-memory-effect regions in a single exposure, expanding steady-state around-corner imaging beyond the conventional memory-effect field of view."
while html.count(sentence) > 1:
    first = html.find(sentence)
    later = html.find(sentence, first + len(sentence))
    start = later - 1 if later > 0 and html[later - 1] == " " else later
    html = html[:start] + html[later + len(sentence):]
if html.count(sentence) != 1:
    raise RuntimeError(f"Unexpected polarization timeline sentence count: {html.count(sentence)}")
INDEX.write_text(html, encoding="utf-8")

note = NOTE.read_text(encoding="utf-8")nnote = note.replace(
    "- Synchronized **Non-line-of-sight imaging via physics-informed cascade learning** (JOSA A 43(9), E9–E18, 2026; DOI `10.1364/JOSAA.593401`) across the README discovery surface, website explorer, existing survey discussion, bibliography, and rebuilt PDF.\n",
    "- Revalidated **Non-line-of-sight imaging via physics-informed cascade learning** (JOSA A 43(9), E9–E18, 2026; DOI `10.1364/JOSAA.593401`) across its existing README, website, survey, bibliography, and rebuilt-PDF records.\n",
)
note = note.replace(
    "- Added the missing public/survey lineage for **Passive acoustic non-line-of-sight localization without a relay surface** (Physical Review Applied 25(2), 024064, 2026; DOI `10.1103/p97k-sf71`).\n",
    "- Revalidated the existing final-venue record for **Passive acoustic non-line-of-sight localization without a relay surface** (Physical Review Applied 25(2), 024064, 2026; DOI `10.1103/p97k-sf71`) and used it to place the preceding acoustic-daylight lineage in context.\n",
)
if "Removed duplicate copies" not in note:
    note = note.replace(
        "- Corrected **Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors** from arXiv-only metadata to its final ICCV 2025 record, pp. 25040–25049.\n",
        "- Corrected **Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors** from arXiv-only metadata to its final ICCV 2025 record, pp. 25040–25049.\n- Removed duplicate copies of the polarization-encoded spatial-multiplexing sentence from the 2026 website timeline.\n",
    )
NOTE.write_text(note, encoding="utf-8")

print("Final survey placement, update-note wording, and website deduplication applied")
