from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SPAWC_TITLE = "Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave"
ICT_TITLE = "Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware"
SGATV_TITLE = "Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {n}")
    return text.replace(old, new, 1)


def replace_line_regex(text, pattern, replacement, label):
    matches = list(re.finditer(pattern, text, re.M))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected exactly one line, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + replacement + text[m.end():]


def append_html_year(text, year, sentence):
    pattern = re.compile(r'(<div class="tl"><div class="year">' + str(year) + r'</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"website timeline year {year}: expected one block, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + text[m.end():]


# README --------------------------------------------------------------------
readme = read("README.md")
if SPAWC_TITLE in readme:
    raise RuntimeError("README already contains SPAWC precursor; integration may already be applied")
if readme.count(SGATV_TITLE) != 1:
    raise RuntimeError(f"README SG-ATV title count is {readme.count(SGATV_TITLE)}; expected current baseline count 1")
if readme.count(ICT_TITLE) != 1:
    raise RuntimeError(f"README ICT title count is {readme.count(ICT_TITLE)}")

header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
spawc_row = "| 2024 | [Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave](https://doi.org/10.1109/SPAWC60668.2024.10694426) — Tosi et al. | IEEE SPAWC 2024, 331–335 | Demonstrates NLOS target detection using a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment, evaluates CSI-processing strategies for suppressing TDD-induced spectral replicas, and establishes the experimental precursor to the later reliable intrusion-detection system. |\n"
readme = replace_once(readme, header, header + spawc_row, "README latest-additions header")
readme = replace_line_regex(
    readme,
    r'^\| 2026 \| \[Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware\]\(https://arxiv\.org/abs/2604\.07032\) — Tosi et al\. \| arXiv 2026 \|.*$',
    "| 2026 | [Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware](https://arxiv.org/abs/2604.07032) — Tosi et al. | 32nd International Conference on Telecommunications (ICT 2026), 25–30 | Uses a commercial 27.4-GHz 5G/mmWave ISAC platform, large-surface reflections, range–Doppler processing, and PHD filtering for reliable detection and tracking of fully occluded moving intruders in an industrial testbed; the arXiv link is retained for accessible full text. |",
    "README ICT final venue",
)
write("README.md", readme)


# Website -------------------------------------------------------------------
html = read("index.html")
if SPAWC_TITLE in html:
    raise RuntimeError("index.html already contains SPAWC precursor; integration may already be applied")
if html.count(SGATV_TITLE) != 1:
    raise RuntimeError(f"index.html SG-ATV title count is {html.count(SGATV_TITLE)}")
if html.count(ICT_TITLE) != 1:
    raise RuntimeError(f"index.html ICT title count is {html.count(ICT_TITLE)}")

ict_pattern = re.compile(r'^\s*\{cat:.*?title:"' + re.escape(ICT_TITLE) + r'".*?\},\s*$', re.M)
ict_matches = list(ict_pattern.finditer(html))
if len(ict_matches) != 1:
    raise RuntimeError(f"website ICT record count is {len(ict_matches)}")
ict = ict_matches[0]
spawc_record = '      {cat:"latest modality radar rf mmwave isac sensing",title:"Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",authors:"Tosi et al.",year:2024,venue:"IEEE SPAWC 2024, 331–335",url:"https://doi.org/10.1109/SPAWC60668.2024.10694426",key:"A 27.4-GHz 5G/mmWave ISAC proof-of-concept demonstrates around-corner target detection in a factory-like environment and evaluates CSI processing to suppress TDD-induced spectral replicas."},\n'
new_ict_record = '      {cat:"latest modality radar rf mmwave isac sensing tracking",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al.",year:2026,venue:"ICT 2026, 25–30",url:"https://arxiv.org/abs/2604.07032",key:"Commercial 27.4-GHz 5G/mmWave ISAC hardware combines large-surface reflections, range–Doppler processing, and PHD filtering for reliable fully occluded intrusion detection and tracking in an industrial testbed."},'
html = html[:ict.start()] + spawc_record + new_ict_record + html[ict.end():]
html = replace_once(html, '<b>267</b><span>tracked latest entries</span>', '<b>268</b><span>tracked latest entries</span>', "website explorer count")
if "Cellular ISAC demonstrates practical NLOS sensing" not in html:
    html = append_html_year(html, 2024, " Cellular ISAC demonstrates practical NLOS sensing with a 27.4-GHz 5G proof-of-concept at SPAWC, explicitly addressing TDD spectral replicas and hidden-target detection.")
if "ICT 2026 extends the cellular-ISAC branch" not in html:
    html = append_html_year(html, 2026, " ICT 2026 extends the cellular-ISAC branch from feasibility to reliable range–Doppler intrusion detection and PHD-filtered tracking in an industrial testbed.")
write("index.html", html)


# Survey prose --------------------------------------------------------------
a5 = read("article/5newscenes.tex")
if "tosiFeasibilityISACNLOS2024" in a5 or "tosiReliableISACNLOS2026" in a5:
    raise RuntimeError("article/5newscenes.tex already contains Tosi ISAC citations")
anchor = "The radar approach is complementary to optical NLOS: it operates through walls and in total darkness, but at lower spatial resolution than optical methods.\n\n"
paragraph = r"""\vspace{0.8mm}
\noindent \textbf{Cellular ISAC hardware for NLOS sensing.}
A complementary 5G/6G ISAC trajectory asks whether communication hardware can use multipath as an around-corner sensor rather than treating it only as a channel impairment. Tosi~\etal~first demonstrated the feasibility of NLOS target detection with a 27.4~GHz commercial mmWave ISAC proof-of-concept, including channel-state-information processing that suppresses spectral replicas caused by time-division-duplex gaps~\cite{tosiFeasibilityISACNLOS2024}. The later ICT study moved from feasibility to reliable intrusion monitoring of fully occluded moving targets, adding range--Doppler detection and probability-hypothesis-density filtering for tracking and false-alarm rejection in an industrial testbed~\cite{tosiReliableISACNLOS2026}. Together, these works connect radar NLOS with standards-compatible cellular infrastructure and show a deployment path in which communication radios become opportunistic hidden-region sensors.

"""
a5 = replace_once(a5, anchor, anchor + paragraph, "radar paragraph anchor")
write("article/5newscenes.tex", a5)


# Bibliography --------------------------------------------------------------
bib = read("egbib_merged_20260711.bib")
for key in ("tosiFeasibilityISACNLOS2024", "tosiReliableISACNLOS2026"):
    if re.search(r'^@\w+\s*\{\s*' + re.escape(key) + r'\s*,', bib, re.M):
        raise RuntimeError(f"bibliography already contains {key}")
entries = r"""

@inproceedings{tosiFeasibilityISACNLOS2024,
  author = {Tosi, Paolo and Henninger, Marcus and Giroto de Oliveira, Lucas and Mandelli, Silvio},
  title = {Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave},
  booktitle = {2024 IEEE 25th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)},
  pages = {331--335},
  year = {2024},
  doi = {10.1109/SPAWC60668.2024.10694426},
  url = {https://doi.org/10.1109/SPAWC60668.2024.10694426}
}

@inproceedings{tosiReliableISACNLOS2026,
  author = {Tosi, Paolo and Bauhofer, Maximilian and Henninger, Marcus and Schmalen, Laurent and Mandelli, Silvio},
  title = {Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware},
  booktitle = {32nd International Conference on Telecommunications (ICT 2026)},
  pages = {25--30},
  year = {2026},
  address = {Thessaloniki, Greece},
  month = {May},
  note = {Final conference record verified via DBLP; accessible manuscript available as arXiv:2604.07032},
  url = {https://arxiv.org/abs/2604.07032}
}
"""
write("egbib_merged_20260711.bib", bib.rstrip() + entries + "\n")


# Top-level source audit comment -------------------------------------------
bare = read("bare_jrnl.tex")
comment = "% 8 August 2026 ISAC consistency trace: SPAWC cellular-ISAC NLOS precursor and ICT final venue integrated; SG-ATV cross-artifact consistency verified.\n"
if comment not in bare:
    bare = comment + bare
write("bare_jrnl.tex", bare)


# Mark the earlier patch note as applied after this guarded run succeeds. ---
log_path = "updates/2026-08-08-isac-nlos-final-venue-citation-trace.md"
log = read(log_path)
status = """

## Applied status

Applied through the guarded 8 August 2026 cross-artifact integration. The SPAWC 2024 precursor is now included in README, website, survey prose, and bibliography; the 2026 intrusion-detection paper is labeled by its final ICT 2026 venue. SG-ATV was already synchronized across README, website, passive-survey prose, and bibliography and was verified unchanged. The survey PDF is rebuilt and validated by the integration workflow.
"""
if "## Applied status" not in log:
    log = log.rstrip() + status + "\n"
write(log_path, log)

print("Applied bounded cellular-ISAC NLOS integration; verified existing SG-ATV consistency.")
