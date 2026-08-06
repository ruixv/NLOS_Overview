from pathlib import Path
import re

README = Path("README.md")
INDEX = Path("index.html")
ARTICLE_NEW = Path("article/5newscenes.tex")
ARTICLE_LEARN = Path("article/4datadriven.tex")
TEX = Path("bare_jrnl.tex")
BIB = Path("egbib_merged_20260711.bib")
NOTE = Path("updates/2026-08-06-citation-and-public-artifact-sync.md")

PICL = "Non-line-of-sight imaging via physics-informed cascade learning"
SOMMER = "Passive acoustic non-line-of-sight localization without a relay surface"
BOGER = "Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources"
RADAR = "Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System"
GENERAL = "Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors"


def insert_after(text: str, anchor: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"{label}: anchor not found")
    return text.replace(anchor, anchor + addition, 1)


def replace_entry(text: str, key: str, entry: str) -> str:
    pattern = rf"@[A-Za-z]+\{{{re.escape(key)},.*?\n\}}"
    if re.search(pattern, text, flags=re.S):
        return re.sub(pattern, entry.rstrip(), text, count=1, flags=re.S)
    return text.rstrip() + "\n\n" + entry.rstrip() + "\n"


# README: synchronize discovery surface, final venues, and timeline.
readme = README.read_text(encoding="utf-8")
readme, n = re.subn(r"\*\*Update run: [^*]+\.\*\*", "**Update run: 6 August 2026.**", readme, count=1)
if n != 1:
    raise RuntimeError("README update date not found")

latest_start = readme.index("## Latest Additions")
latest_end = readme.find("\n---", latest_start)
latest = readme[latest_start: latest_end if latest_end != -1 else len(readme)]
rows = [
    (PICL, "| 2026 | [Non-line-of-sight imaging via physics-informed cascade learning](https://doi.org/10.1364/JOSAA.593401) — Zhao et al. | Journal of the Optical Society of America A 43(9), E9–E18 (2026) | Cascades SPAD-specific mixed-noise separation with a self-supervised reconstruction network containing a differentiable NLOS forward model, improving low-SNR robustness without requiring a large paired dataset. |\n"),
    (SOMMER, "| 2026 | [Passive acoustic non-line-of-sight localization without a relay surface](https://doi.org/10.1103/p97k-sf71) — Sommer and Katz | Physical Review Applied 25(2), 024064 (2026) | Uses doorway edges as virtual detector arrays and the frequency signature of knife-edge diffraction at convex corners for passive 3D hidden-source localization without a conventional relay wall. |\n"),
    (RADAR, "| 2025 | [Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System](https://doi.org/10.1109/TGRS.2025.3564230) — Alburadi et al. | IEEE Transactions on Geoscience and Remote Sensing 63, 1–9 (2025) | A 222–228 GHz polarimetric FMCW radar with a mechanically scanned fan beam produces high-resolution indoor maps and exploits double-bounce specular paths for around-corner detection; polarization diversity helps separate useful NLOS returns from leakage and clutter. |\n"),
    (BOGER, "| 2023 | [Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources](https://doi.org/10.1038/s41598-023-31490-2) — Boger-Lombard, Slobodkin and Katz | Scientific Reports 13, 4952 (2023) | Uses acoustic interferometry and cross-correlations of uncontrolled broadband noise to retrieve effective Green functions and passively localize or track a human hidden around a corner. |\n"),
]
missing_rows = [row for title, row in rows if title not in latest]
if missing_rows:
    header = "|------|-------|----------------|----------------|\n"
    if header not in latest:
        raise RuntimeError("README Latest Additions table header not found")
    pos = readme.index(header, latest_start) + len(header)
    readme = readme[:pos] + "".join(missing_rows) + readme[pos:]

old_general = "| 2024 | [Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors](https://arxiv.org/abs/2409.14011) — Sun et al. | arXiv 2024 | Learns path-compensation and adaptive phasor-field priors for cross-system and low-SNR NLOS generalization. |"
new_general = "| 2025 | [Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors](https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Generalizable_Non-Line-of-Sight_Imaging_with_Learnable_Physical_Priors_ICCV_2025_paper.html) — Sun et al. | ICCV 2025, 25040–25049 | Learns path-compensation and adaptive phasor-field priors for cross-system and low-SNR NLOS generalization. |"
if old_general in readme:
    readme = readme.replace(old_general, new_general, 1)

if "Sommer and Katz: knife-edge diffraction" not in readme:
    anchor = "2026 ── Zhao et al.: PICL — SPAD-aware denoising cascaded with self-supervised differentiable-physics reconstruction [JOSA A]\n"
    readme = insert_after(readme, anchor, "   │     Sommer and Katz: knife-edge diffraction removes the relay-wall requirement for passive 3D acoustic NLOS localization [Physical Review Applied]\n", "README 2026 timeline")
if "Alburadi et al.: 228 GHz polarimetric" not in readme:
    anchor = "   │     Lai et al.: HoloRadar reconstructs complete LOS/NLOS 3D scenes with one mobile mmWave radar [NeurIPS]\n"
    readme = insert_after(readme, anchor, "   │     Alburadi et al.: 228 GHz polarimetric FMCW mapping exploits double-bounce specular paths for measured around-corner imaging [IEEE TGRS]\n", "README 2025 timeline")
if "Boger-Lombard et al.: acoustic daylight" not in readme:
    anchor = "2023 ── Wang et al.: Signal Superresolution Network — plug-and-play 16× sparse-scan acceleration [CVPR]\n"
    readme = insert_after(readme, anchor, "   │     Boger-Lombard et al.: acoustic daylight interferometry retrieves Green functions from uncontrolled noise for passive around-corner localization [Scientific Reports]\n", "README 2023 timeline")
README.write_text(readme, encoding="utf-8")

# Website: add only genuinely absent records, correct metadata, and set the counter from data.
html = INDEX.read_text(encoding="utf-8")
html = re.sub(r"Updated \d+ [A-Za-z]+ 2026 · 210\+ papers", "Updated 6 August 2026 · 210+ papers", html, count=1)
html = re.sub(r"Last updated: \d+ [A-Za-z]+ 2026", "Last updated: 6 August 2026", html, count=1)
papers_marker = "    const papers=[\n"
objects = [
    (SOMMER, '      {cat:"latest modality acoustic passive localization diffraction",title:"Passive acoustic non-line-of-sight localization without a relay surface",authors:"Sommer and Katz",year:2026,venue:"Physical Review Applied 25(2), 024064",url:"https://doi.org/10.1103/p97k-sf71",key:"Uses doorway edges as virtual arrays and knife-edge diffraction signatures at convex corners for passive 3D hidden-source localization without a relay wall."},\n'),
    (RADAR, '      {cat:"latest modality radar rf mmwave sub-thz active mapping",title:"Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System",authors:"Alburadi et al.",year:2025,venue:"IEEE TGRS 63, 1–9",url:"https://doi.org/10.1109/TGRS.2025.3564230",key:"A 222–228 GHz polarimetric FMCW system combines LiDAR-like indoor mapping with double-bounce around-corner imaging; polarization diversity suppresses leakage and clutter."},\n'),
]
if papers_marker not in html:
    raise RuntimeError("website paper-array marker not found")
for title, obj in reversed(objects):
    if title not in html:
        html = html.replace(papers_marker, papers_marker + obj, 1)

boger_pattern = re.compile(r'\{cat:"latest modality",title:"Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources",.*?\},')
boger_obj = '{cat:"latest modality acoustic passive localization",title:"Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources",authors:"Boger-Lombard, Slobodkin and Katz",year:2023,venue:"Scientific Reports 13, 4952",url:"https://doi.org/10.1038/s41598-023-31490-2",key:"Acoustic daylight interferometry uses cross-correlations of uncontrolled broadband noise to retrieve effective Green functions and passively localize or track hidden targets around a corner."},'
if boger_pattern.search(html):
    html = boger_pattern.sub(boger_obj, html, count=1)

old_obj = '{cat:"latest learning active",title:"Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors",authors:"Sun et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2409.14011",key:"Learnable path compensation and adaptive phasor-field priors for cross-system and low-SNR generalization."},'
new_obj = '{cat:"latest learning active",title:"Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors",authors:"Sun et al.",year:2025,venue:"ICCV 2025, 25040–25049",url:"https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Generalizable_Non-Line-of-Sight_Imaging_with_Learnable_Physical_Priors_ICCV_2025_paper.html",key:"Learnable path compensation and adaptive phasor-field priors for cross-system and low-SNR generalization."},'
if old_obj in html:
    html = html.replace(old_obj, new_obj, 1)


def append_timeline(page: str, year: int, sentence: str, token: str) -> str:
    if token in page:
        return page
    pattern = re.compile(rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p>)', re.S)
    match = pattern.search(page)
    if not match:
        raise RuntimeError(f"website {year} timeline block not found")
    return page[:match.start(2)] + match.group(2).rstrip() + " " + sentence + page[match.end(2):]

html = append_timeline(html, 2026, "Sommer and Katz then removed the relay-wall requirement in passive acoustic localization by treating doorway edges and knife-edge diffraction as virtual apertures.", "removed the relay-wall requirement in passive acoustic localization")
html = append_timeline(html, 2025, "Alburadi et al. extended measured RF NLOS to 228 GHz polarimetric FMCW mapping, using double-bounce specular paths for around-corner imaging.", "extended measured RF NLOS to 228 GHz")
html = append_timeline(html, 2023, "Boger-Lombard, Slobodkin, and Katz established passive acoustic daylight localization from uncontrolled-noise cross-correlations.", "established passive acoustic daylight localization")
actual = html.count('{cat:')
html, n = re.subn(r'<b>\d+</b><span>tracked latest entries</span>', f'<b>{actual}</b><span>tracked latest entries</span>', html, count=1)
if n != 1:
    raise RuntimeError("website tracked-entry counter not found")
INDEX.write_text(html, encoding="utf-8")

# Survey prose: integrate the missing acoustic lineage and measured 228-GHz branch semantically.
article = ARTICLE_NEW.read_text(encoding="utf-8")
if "bogerLombardPassiveAcousticCorners2023" not in article:
    anchor = "More recently, Sommer and Katz showed"
    sentence = "Boger-Lombard, Slobodkin, and Katz first showed that acoustic interferometry can retrieve effective Green functions from cross-correlations of uncontrolled broadband noise, enabling passive localization and tracking of a human hidden around a corner without controlled active probing~\\cite{bogerLombardPassiveAcousticCorners2023}. "
    if anchor not in article:
        raise RuntimeError("acoustic survey insertion anchor not found")
    article = article.replace(anchor, sentence + anchor, 1)
if "alburadiPolarimetricRadarNLOS2025" not in article:
    anchor = "\\subsection{Acoustic NLOS Imaging}"
    paragraph = "\\vspace{0.8mm}\n\\noindent \\textbf{Sub-terahertz polarimetric indoor mapping.}\nAlburadi~\\etal~demonstrated that a 222--228~GHz polarimetric FMCW radar with a mechanically scanned fan-beam antenna can combine rapid high-resolution indoor mapping with measured around-corner imaging~\\cite{alburadiPolarimetricRadarNLOS2025}. The system interprets double-bounce specular paths as hidden-scene evidence, while co- and cross-polarized channels help distinguish useful NLOS returns from direct leakage and environmental clutter. This work extends the measured mmWave lineage toward sub-terahertz carrier frequencies and emphasizes polarization as an additional physical cue for practical RF NLOS imaging.\n\n"
    if anchor not in article:
        raise RuntimeError("radar survey insertion anchor not found")
    article = article.replace(anchor, paragraph + anchor, 1)
ARTICLE_NEW.write_text(article, encoding="utf-8")

# Bibliography: correct the 2023 acoustic metadata and add the verified radar record.
bib = BIB.read_text(encoding="utf-8")
boger_entry = """@article{bogerLombardPassiveAcousticCorners2023,
  author = {Boger-Lombard, Jeremy and Slobodkin, Yevgeny and Katz, Ori},
  title = {Towards Passive Non-Line-of-Sight Acoustic Localization around Corners Using Uncontrolled Random Noise Sources},
  journal = {Scientific Reports},
  volume = {13},
  pages = {4952},
  year = {2023},
  doi = {10.1038/s41598-023-31490-2},
  url = {https://doi.org/10.1038/s41598-023-31490-2}
}"""
radar_entry = """@article{alburadiPolarimetricRadarNLOS2025,
  author = {Alburadi, Abdullah and Muppala, Aditya Varma and Nashashibi, Adib Y. and Shaman, Hussein N. and Sarabandi, Kamal},
  title = {Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-{GHz} {FMCW} Polarimetric Radar System},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {63},
  pages = {1--9},
  year = {2025},
  doi = {10.1109/TGRS.2025.3564230},
  url = {https://doi.org/10.1109/TGRS.2025.3564230}
}"""
bib = replace_entry(bib, "bogerLombardPassiveAcousticCorners2023", boger_entry)
bib = replace_entry(bib, "alburadiPolarimetricRadarNLOS2025", radar_entry)
BIB.write_text(bib, encoding="utf-8")

# The root survey file includes the section sources; update its declared coverage date.
tex = TEX.read_text(encoding="utf-8")
marker = "% 6 August 2026 citation and consistency audit: passive acoustic diffraction/interferometry, 228 GHz polarimetric radar, PICL discovery metadata, and ICCV final venue synchronized.\n"
if marker not in tex:
    tex = marker + tex
tex = re.sub(r"This update extends coverage to include significant advances from 2022 through \d+ [A-Za-z]+ 2026\.", "This update extends coverage to include significant advances from 2022 through 6 August 2026.", tex, count=1)
TEX.write_text(tex, encoding="utf-8")

NOTE.parent.mkdir(parents=True, exist_ok=True)
NOTE.write_text("""# 6 August 2026 citation-tracing and consistency update

## Integrated and corrected records

- Synchronized **Non-line-of-sight imaging via physics-informed cascade learning** (JOSA A 43(9), E9–E18, 2026; DOI `10.1364/JOSAA.593401`) across the README discovery surface, website explorer, existing survey discussion, bibliography, and rebuilt PDF.
- Added the missing public/survey lineage for **Passive acoustic non-line-of-sight localization without a relay surface** (Physical Review Applied 25(2), 024064, 2026; DOI `10.1103/p97k-sf71`).
- Corrected **Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources** to the verified three-author Scientific Reports record, volume 13, article 4952 (2023), and integrated its acoustic-daylight contribution into the survey prose.
- Added **Rapid Indoor Mapping and Non-Line-of-Sight Imaging Using a 228-GHz FMCW Polarimetric Radar System** (IEEE TGRS 63, 1–9, 2025; DOI `10.1109/TGRS.2025.3564230`) to the radar/RF trajectory.
- Corrected **Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors** from arXiv-only metadata to its final ICCV 2025 record, pp. 25040–25049.

## Scope decisions

All citation-traced candidates were checked for genuine hidden-scene imaging, localization, or tightly adjacent NLOS reconstruction. Propagation-condition classifiers that merely label an RF/acoustic link as LOS/NLOS were excluded. No newer high-confidence direct NLOS publication beyond the repository's already covered July 2026 frontier was verified in this pass.
""", encoding="utf-8")

# Source-level invariants.
readme = README.read_text(encoding="utf-8")
html = INDEX.read_text(encoding="utf-8")
article = ARTICLE_NEW.read_text(encoding="utf-8")
learn = ARTICLE_LEARN.read_text(encoding="utf-8")
bib = BIB.read_text(encoding="utf-8")
tex = TEX.read_text(encoding="utf-8")
for title in (PICL, SOMMER, BOGER, RADAR):
    assert title in readme, title
    assert title in html, title
assert "ICCV 2025, 25040–25049" in readme and "ICCV 2025, 25040–25049" in html
assert "zhaoPICL2026" in learn
for key in ("sommerPassiveAcousticNLOS2026", "bogerLombardPassiveAcousticCorners2023", "alburadiPolarimetricRadarNLOS2025"):
    assert key in article
    assert len(re.findall(rf"@[A-Za-z]+\{{{key},", bib, flags=re.I)) == 1
assert "pages = {4952}" in bib and "Boger-Lombard, Jeremy and Slobodkin, Yevgeny and Katz, Ori" in bib
assert "through 6 August 2026" in tex
assert int(re.search(r'<b>(\d+)</b><span>tracked latest entries</span>', html).group(1)) == html.count('{cat:')
print(f"Applied NLOS consistency update with {html.count('{cat:')} website records")
