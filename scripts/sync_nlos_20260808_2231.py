from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {n}")
    return text.replace(old, new, 1)


def replace_line_by_title(text, title, new_line, label):
    pattern = re.compile(r'^.*' + re.escape(title) + r'.*$', re.M)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one line for {title!r}, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + new_line + text[m.end():]


def replace_html_record(text, title, new_line):
    pattern = re.compile(r'^\s*\{cat:.*?title:"' + re.escape(title) + r'".*?\},\s*$', re.M)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"website record {title!r}: expected one match, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + new_line + text[m.end():]


def bib_replace(text, key, entry):
    pattern = re.compile(r'^@\w+\s*\{\s*' + re.escape(key) + r'\s*,.*?^\}\s*$', re.M | re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"BibTeX key {key!r}: expected one existing entry, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + entry.rstrip() + "\n" + text[m.end():].lstrip("\n")


def bib_add_if_missing(text, key, entry):
    pattern = re.compile(r'^@\w+\s*\{\s*' + re.escape(key) + r'\s*,', re.M)
    n = len(pattern.findall(text))
    if n > 1:
        raise RuntimeError(f"BibTeX key {key!r}: duplicate count {n}")
    if n == 1:
        return text
    return text.rstrip() + "\n\n" + entry.strip() + "\n"


def append_readme_year(text, year, phrase):
    if phrase in text:
        return text
    pattern = re.compile(rf'^{year} ──.*$', re.M)
    m = pattern.search(text)
    if not m:
        raise RuntimeError(f"README timeline year {year} not found")
    return text[:m.end()] + "\n   │     " + phrase + text[m.end():]


def append_html_year(text, year, sentence):
    if sentence in text:
        return text
    pattern = re.compile(r'(<div class="tl"><div class="year">' + str(year) + r'</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"website timeline year {year}: expected one block, found {len(matches)}")
    m = matches[0]
    body = m.group(2)
    sep = " " if body and not body.endswith(" ") else ""
    return text[:m.start()] + m.group(1) + body + sep + sentence + m.group(3) + text[m.end():]


TITLE_TOSI_PRE = "Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave"
TITLE_TOSI_ICT = "Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware"
TITLE_N2 = "N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization"
TITLE_MINE = "Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion"

# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------
readme = read("README.md")
header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
new_rows = """| 2026 | [Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion](https://doi.org/10.3390/s26144615) — Yang et al. | Sensors 26(14), 4615 (2026) | BSCF aligns 3D LiDAR and 4D mmWave radar, suppresses mining-scene multipath, identifies LiDAR blind regions, and injects only spatially consistent radar evidence. Under complete occlusion it supplies existence-level hidden-target risk cues and a Volume Recovery Rate proxy, complementing reconstruction-oriented radar NLOS with safety-driven blind-zone perception. |
| 2024 | [Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave](https://doi.org/10.1109/SPAWC60668.2024.10694426) — Tosi et al. | IEEE SPAWC 2024, 331–335 | Demonstrates fully NLOS target detection with a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment; CSI-processing strategies mitigate TDD-induced spectral replicas and establish the experimental precursor to the 2026 ICT intrusion-monitoring system. |
"""
if TITLE_MINE not in readme or TITLE_TOSI_PRE not in readme:
    missing_rows = ""
    if TITLE_MINE not in readme:
        missing_rows += new_rows.splitlines(True)[0]
    if TITLE_TOSI_PRE not in readme:
        missing_rows += new_rows.splitlines(True)[1]
    readme = replace_once(readme, header, header + missing_rows, "README latest-additions header")

readme = replace_line_by_title(
    readme,
    TITLE_TOSI_ICT,
    "| 2026 | [Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware](https://arxiv.org/abs/2604.07032) — Tosi et al. | International Conference on Telecommunications (ICT 2026), 25–30 | Uses a mmWave ISAC proof-of-concept and large-surface reflections for fully occluded industrial intrusion sensing; range–Doppler processing and probability-hypothesis-density tracking improve persistence and false-alarm robustness beyond the 2024 feasibility study. |",
    "README ICT final venue",
)
readme = replace_line_by_title(
    readme,
    TITLE_N2,
    "| 2026 | [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://doi.org/10.1109/TMC.2025.3634623) — Shi et al. | IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026) | Uses one 24-GHz mmWave radar plus a single backscatter tag, HFD modulation, correlation gain, and FS-MUSIC to separate and exploit multipath for robust around-corner localization; the final journal issue reports roughly 11 cm median axis-wise error at 5 m in the laboratory setting. |",
    "README N2LoS final venue",
)
readme = append_readme_year(readme, 2024, "Tosi et al. demonstrate 27.4-GHz cellular ISAC target detection in a fully NLOS industrial setting, including compensation for TDD sensing artifacts [IEEE SPAWC]")
readme = append_readme_year(readme, 2026, "Tosi et al. extend cellular ISAC to tracked, false-alarm-robust industrial intrusion monitoring; N2LoS reaches its final TMC record; Yang et al. fuse 4D radar with LiDAR to provide hidden-target risk evidence in mining blind zones [ICT / IEEE TMC / Sensors]")
write("README.md", readme)

# ---------------------------------------------------------------------------
# Website
# ---------------------------------------------------------------------------
html = read("index.html")
if TITLE_MINE not in html or TITLE_TOSI_PRE not in html:
    anchor = "    const papers=[\n"
    records = ""
    if TITLE_MINE not in html:
        records += '      {cat:"latest modality radar rf mmwave lidar fusion autonomous-driving safety",title:"Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion",authors:"Yang et al.",year:2026,venue:"Sensors 26(14), 4615",url:"https://doi.org/10.3390/s26144615",key:"Blind-Spot Complementary Fusion suppresses 4D-radar multipath, aligns radar with LiDAR, and injects verified radar evidence into LiDAR blind zones, providing existence-level hidden-target risk cues under complete occlusion rather than full hidden-shape reconstruction."},\n'
    if TITLE_TOSI_PRE not in html:
        records += '      {cat:"latest modality radar rf mmwave isac 5g 6g",title:"Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",authors:"Tosi et al.",year:2024,venue:"IEEE SPAWC 2024, 331–335",url:"https://doi.org/10.1109/SPAWC60668.2024.10694426",key:"A commercial 27.4-GHz 5G/mmWave ISAC proof-of-concept detects fully NLOS targets in a factory-like environment; CSI processing mitigates TDD-induced spectral replicas and establishes the precursor to the 2026 ICT tracking system."},\n'
    html = replace_once(html, anchor, anchor + records, "website papers-array anchor")

html = replace_html_record(
    html,
    TITLE_TOSI_ICT,
    '      {cat:"latest modality radar rf mmwave isac 5g 6g tracking",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al.",year:2026,venue:"ICT 2026, 25–30",url:"https://arxiv.org/abs/2604.07032",key:"5G/mmWave ISAC hardware uses large-surface reflections, range-Doppler processing, and PHD-based tracking for reliable fully NLOS intrusion detection with explicit false-alarm stress tests in an industrial environment."},',
)
html = replace_html_record(
    html,
    TITLE_N2,
    '      {cat:"latest modality radar rf mmwave localization backscatter",title:"N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization",authors:"Shi et al.",year:2026,venue:"IEEE TMC 25(5), 6002–6016",url:"https://doi.org/10.1109/TMC.2025.3634623",key:"A single 24-GHz radar and backscatter tag exploit multipath using HFD modulation, correlation gain, and FS-MUSIC for robust NLOS localization; the final TMC issue reports roughly 11 cm median axis-wise error at 5 m in the laboratory setting."},',
)
html = append_html_year(html, 2024, " A 27.4-GHz cellular ISAC prototype also established experimentally that communication hardware can detect fully NLOS targets after compensating TDD-induced sensing artifacts.")
html = append_html_year(html, 2026, " Cellular ISAC progressed from feasibility to tracked industrial intrusion monitoring, N2LoS reached its final IEEE TMC record, and 4D-radar/LiDAR fusion supplied verified hidden-target risk evidence in mining blind zones.")
actual = html.count('{cat:')
if actual != 269:
    raise RuntimeError(f"website expected 269 paper objects after update, found {actual}")
html, n = re.subn(r'<b>\d+</b><span>tracked latest entries</span>', '<b>269</b><span>tracked latest entries</span>', html, count=1)
if n != 1:
    raise RuntimeError("website tracked-latest counter not found exactly once")
write("index.html", html)

# ---------------------------------------------------------------------------
# Survey prose and maintenance date.
# ---------------------------------------------------------------------------
a5 = read("article/5newscenes.tex")
if "tosiFeasibilityISACNLOS2024" not in a5:
    anchor = "\n\nA parallel RF/mmWave lineage has progressively broadened the task"
    block = """

\vspace{0.8mm}
\noindent \textbf{Cellular ISAC hardware for NLOS sensing.}
A complementary 5G/6G ISAC trajectory asks whether communication hardware can use multipath as an around-corner sensor rather than treating it only as a channel impairment. Tosi~\etal~first demonstrated fully NLOS target detection with a 27.4~GHz commercial mmWave ISAC proof-of-concept, including channel-state-information processing that suppresses spectral replicas caused by time-division-duplex gaps~\cite{tosiFeasibilityISACNLOS2024}. Their later ICT study moved from feasibility to reliable intrusion monitoring of fully occluded moving targets, adding range--Doppler detection and probability-hypothesis-density filtering for tracking and false-alarm rejection in an industrial testbed~\cite{tosiReliableISACNLOS2026}. Together, these works connect radar NLOS with standards-compatible cellular infrastructure and show a deployment path in which communication radios become opportunistic hidden-region sensors.
"""
    a5 = replace_once(a5, anchor, block + anchor, "article/5 ISAC insertion anchor")
if "yangMiningRadarLiDARNLOS2026" not in a5:
    raise RuntimeError("article/5 is unexpectedly missing the already integrated mining radar-LiDAR NLOS paragraph")
if "shiN2LoS2025" not in a5:
    raise RuntimeError("article/5 is unexpectedly missing the N2LoS citation")
write("article/5newscenes.tex", a5)

bare = read("bare_jrnl.tex")
comment = "% 8 August 2026 citation trace: cellular-ISAC precursor/follow-up, N2LoS final TMC venue, and mining radar-LiDAR public-artifact consistency synchronized.\n"
if comment.strip() not in bare:
    bare = comment + bare
bare = bare.replace("This update extends coverage to include significant advances from 2022 through 6 August 2026.", "This update extends coverage to include significant advances from 2022 through 8 August 2026.")
if "through 8 August 2026" not in bare:
    raise RuntimeError("bare_jrnl.tex update-date correction failed")
write("bare_jrnl.tex", bare)

# ---------------------------------------------------------------------------
# Bibliography used directly by bare_jrnl.tex.
# ---------------------------------------------------------------------------
bib = read("egbib_merged_20260711.bib")
entry_n2 = r'''@article{shiN2LoS2025,
  author = {Shi, Zhenguo and Yan, Yihe and Wang, Yanxiang and Hu, Wen and Chou, Chun Tung and Cheng, Qingqing and Yuan, Weijie},
  title = {N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization},
  journal = {IEEE Transactions on Mobile Computing},
  volume = {25},
  number = {5},
  pages = {6002--6016},
  year = {2026},
  month = {May},
  doi = {10.1109/TMC.2025.3634623},
  url = {https://doi.org/10.1109/TMC.2025.3634623},
  note = {Published online 19 November 2025}
}'''
bib = bib_replace(bib, "shiN2LoS2025", entry_n2)
entry_tosi_pre = r'''@inproceedings{tosiFeasibilityISACNLOS2024,
  author = {Tosi, Paolo and Henninger, Marcus and Giroto de Oliveira, Lucas and Mandelli, Silvio},
  title = {Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave},
  booktitle = {2024 IEEE 25th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)},
  pages = {331--335},
  year = {2024},
  address = {Lucca, Italy},
  month = {September},
  doi = {10.1109/SPAWC60668.2024.10694426},
  url = {https://doi.org/10.1109/SPAWC60668.2024.10694426}
}'''
entry_tosi_ict = r'''@inproceedings{tosiReliableISACNLOS2026,
  author = {Tosi, Paolo and Bauhofer, Maximilian and Henninger, Marcus and Schmalen, Laurent and Mandelli, Silvio},
  title = {Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware},
  booktitle = {32nd International Conference on Telecommunications (ICT 2026)},
  pages = {25--30},
  year = {2026},
  address = {Thessaloniki, Greece},
  month = {May},
  note = {Also available as arXiv:2604.07032},
  url = {https://arxiv.org/abs/2604.07032}
}'''
entry_mine = r'''@article{yangMiningRadarLiDARNLOS2026,
  author = {Yang, Jianjian and Zhang, Yuyu and Zheng, Zhiyao and Zhang, Yuyuan},
  title = {Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion},
  journal = {Sensors},
  volume = {26},
  number = {14},
  pages = {4615},
  year = {2026},
  doi = {10.3390/s26144615},
  url = {https://doi.org/10.3390/s26144615}
}'''
bib = bib_add_if_missing(bib, "tosiFeasibilityISACNLOS2024", entry_tosi_pre)
bib = bib_add_if_missing(bib, "tosiReliableISACNLOS2026", entry_tosi_ict)
bib = bib_add_if_missing(bib, "yangMiningRadarLiDARNLOS2026", entry_mine)
write("egbib_merged_20260711.bib", bib)

# ---------------------------------------------------------------------------
# Resolve the previous patch note and write an integration log.
# ---------------------------------------------------------------------------
old_note = read("updates/2026-08-08-isac-nlos-final-venue-citation-trace.md")
status_line = "> **Resolved 8 August 2026:** the SPAWC/ICT changes described below were applied in the follow-up synchronized public-artifact integration. The historical patch instructions are retained for auditability.\n\n"
if not old_note.startswith("> **Resolved 8 August 2026:**"):
    old_note = status_line + old_note
write("updates/2026-08-08-isac-nlos-final-venue-citation-trace.md", old_note)

log = """# NLOS citation-trace and consistency integration — 8 August 2026

This follow-up closes the outstanding cellular-ISAC patch and a cross-artifact radar/LiDAR consistency gap found in the same fresh keyword and forward-citation pass.

- Added **Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave** as IEEE SPAWC 2024 (331–335), DOI `10.1109/SPAWC60668.2024.10694426`.
- Corrected **Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware** from arXiv-only metadata to its final ICT 2026 proceedings record (25–30); the arXiv link is retained for public full text.
- Corrected **N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization** to IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026), DOI `10.1109/TMC.2025.3634623`.
- Added the already survey-integrated but README/website-missing **Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion**, Sensors 26(14), 4615, DOI `10.3390/s26144615`.
- Integrated the cellular-ISAC lineage into the Radar-Based NLOS Imaging survey narrative and updated the survey coverage date to 8 August 2026.
- Expected searchable website explorer count after the two new public records: **269**.

The mining paper is categorized as tightly adjacent NLOS perception rather than hidden-shape reconstruction: it provides validated existence/envelope evidence in LiDAR blind zones under complete occlusion. The cellular-ISAC papers are categorized in the RF/mmWave NLOS sensing branch.
"""
write("updates/2026-08-08-isac-radar-lidar-consistency-integration.md", log)

print("Bounded NLOS update applied successfully.")
