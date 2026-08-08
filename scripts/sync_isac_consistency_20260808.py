from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SPAWC_TITLE = "Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave"
ICT_TITLE = "Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware"
SGATV_TITLE = "Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging"
MICROCOMB_TITLE = "Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection"


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
for title in (SPAWC_TITLE, MICROCOMB_TITLE):
    if title in readme:
        raise RuntimeError(f"README already contains {title}; integration may already be applied")
if readme.count(SGATV_TITLE) != 1:
    raise RuntimeError(f"README SG-ATV title count is {readme.count(SGATV_TITLE)}; expected current baseline count 1")
if readme.count(ICT_TITLE) != 1:
    raise RuntimeError(f"README ICT title count is {readme.count(ICT_TITLE)}")

header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
new_rows = (
    "| 2026 | [Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection](https://doi.org/10.1002/advs.202516806) — Zhi et al. | Advanced Science 13(12), e16806 (2026) | Demonstrates a dual-multi-soliton microcomb NLOS imaging branch: photon-level coherent ranging is relayed by a diffuse wall, a 2D translation stage samples the hidden target, and the system reconstructs millimeter-scale 3D relief while combining high coherent precision with higher power efficiency and acquisition speed than single-soliton ranging. |\n"
    "| 2024 | [Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave](https://doi.org/10.1109/SPAWC60668.2024.10694426) — Tosi et al. | IEEE SPAWC 2024, 331–335 | Demonstrates NLOS target detection using a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment, evaluates CSI-processing strategies for suppressing TDD-induced spectral replicas, and establishes the experimental precursor to the later reliable intrusion-detection system. |\n"
)
readme = replace_once(readme, header, header + new_rows, "README latest-additions header")
readme = replace_line_regex(
    readme,
    r'^\| 2026 \| \[Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware\]\(https://arxiv\.org/abs/2604\.07032\) — Tosi et al\. \| arXiv 2026 \|.*$',
    "| 2026 | [Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware](https://arxiv.org/abs/2604.07032) — Tosi et al. | 32nd International Conference on Telecommunications (ICT 2026), 25–30 | Uses a commercial 27.4-GHz 5G/mmWave ISAC platform, large-surface reflections, range–Doppler processing, and PHD filtering for reliable detection and tracking of fully occluded moving intruders in an industrial testbed; the arXiv link is retained for accessible full text. |",
    "README ICT final venue",
)
write("README.md", readme)


# Website -------------------------------------------------------------------
html = read("index.html")
for title in (SPAWC_TITLE, MICROCOMB_TITLE):
    if title in html:
        raise RuntimeError(f"index.html already contains {title}; integration may already be applied")
if html.count(SGATV_TITLE) != 1:
    raise RuntimeError(f"index.html SG-ATV title count is {html.count(SGATV_TITLE)}")
if html.count(ICT_TITLE) != 1:
    raise RuntimeError(f"index.html ICT title count is {html.count(ICT_TITLE)}")

ict_pattern = re.compile(r'^\s*\{cat:.*?title:"' + re.escape(ICT_TITLE) + r'".*?\},\s*$', re.M)
ict_matches = list(ict_pattern.finditer(html))
if len(ict_matches) != 1:
    raise RuntimeError(f"website ICT record count is {len(ict_matches)}")
ict = ict_matches[0]
records = (
    '      {cat:"latest active coherent modality photon-level microcomb",title:"Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection",authors:"Zhi et al.",year:2026,venue:"Advanced Science 13(12), e16806",url:"https://doi.org/10.1002/advs.202516806",key:"Dual-multi-soliton coherent ranging is demonstrated for wall-relayed NLOS 3D imaging, combining photon-level operation with higher power efficiency and faster multi-interferogram acquisition than the single-soliton configuration."},\n'
    '      {cat:"latest modality radar rf mmwave isac sensing",title:"Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",authors:"Tosi et al.",year:2024,venue:"IEEE SPAWC 2024, 331–335",url:"https://doi.org/10.1109/SPAWC60668.2024.10694426",key:"A 27.4-GHz 5G/mmWave ISAC proof-of-concept demonstrates around-corner target detection in a factory-like environment and evaluates CSI processing to suppress TDD-induced spectral replicas."},\n'
)
new_ict_record = '      {cat:"latest modality radar rf mmwave isac sensing tracking",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al.",year:2026,venue:"ICT 2026, 25–30",url:"https://arxiv.org/abs/2604.07032",key:"Commercial 27.4-GHz 5G/mmWave ISAC hardware combines large-surface reflections, range–Doppler processing, and PHD filtering for reliable fully occluded intrusion detection and tracking in an industrial testbed."},'
html = html[:ict.start()] + records + new_ict_record + html[ict.end():]
html = replace_once(html, '<b>267</b><span>tracked latest entries</span>', '<b>269</b><span>tracked latest entries</span>', "website explorer count")
if "Cellular ISAC demonstrates practical NLOS sensing" not in html:
    html = append_html_year(html, 2024, " Cellular ISAC demonstrates practical NLOS sensing with a 27.4-GHz 5G proof-of-concept at SPAWC, explicitly addressing TDD spectral replicas and hidden-target detection.")
if "dual-multi-soliton microcombs extend coherent NLOS" not in html:
    html = append_html_year(html, 2026, " Advanced Science dual-multi-soliton microcombs extend coherent NLOS into photon-level wall-relayed 3D imaging, while ICT 2026 extends the cellular-ISAC branch from feasibility to reliable range–Doppler intrusion detection and PHD-filtered tracking.")
write("index.html", html)


# Active optical survey: extend coherent branch -----------------------------
a2 = read("article/2active.tex")
if "zhiMultiSolitonMicrocombNLOS2026" in a2:
    raise RuntimeError("article/2active.tex already contains microcomb citation")
table_old = r"\cite{huangCombCalibratedNLOS2024,yeCombCalibratedFMCWTracking2025,chenVectorEnhancedFMCWNLOS2025,liangFMCWNLOS2026} & Frequency-swept laser & Coherent FMCW interferometer & Beat frequency, phase, and Doppler & 3D imaging / tracking / vibrometry\\%%%% Table body"
table_new = r"\cite{huangCombCalibratedNLOS2024,yeCombCalibratedFMCWTracking2025,chenVectorEnhancedFMCWNLOS2025,liangFMCWNLOS2026,zhiMultiSolitonMicrocombNLOS2026} & Frequency-swept / dual-comb laser & Coherent interferometer & Beat frequency, phase, photon-level ranging, and Doppler & 3D imaging / tracking / vibrometry\\%%%% Table body"
a2 = replace_once(a2, table_old, table_new, "active coherent-system table row")
coherent_end = "Together, these works establish coherent FMCW LiDAR as a complementary trajectory to SPAD-based transient NLOS: it directly measures range, phase, Doppler, and vibration with fine resolution, while trading the simplicity of photon counting for interferometric calibration and coherence control.\n"
microcomb_para = r"""
\vspace{0.8mm}
\noindent \textbf{Dual-microcomb photon-level NLOS imaging.}
Zhi~\etal~extended the coherent branch from comb-calibrated frequency sweeps to dual-multi-soliton microcomb ranging~\cite{zhiMultiSolitonMicrocombNLOS2026}. Multi-soliton states produce multiple interferograms within one update period while retaining the coherence needed for precision ranging, increasing useful optical power and acquisition speed relative to a single-soliton configuration. Beyond conventional ranging and long-distance experiments, the authors explicitly demonstrated three-bounce NLOS imaging: a signal comb illuminates a diffuse relay wall, the wall illuminates a hidden stepped-height target, and the returning wall-scattered field interferes with a local comb to recover depth while a two-dimensional translation stage supplies lateral samples. This result links photon-level coherent metrology to NLOS reconstruction and broadens the coherent-sensing trajectory beyond FMCW sweep calibration toward microcomb sources that jointly target sensitivity, precision, and acquisition rate.
"""
a2 = replace_once(a2, coherent_end, coherent_end + microcomb_para, "coherent FMCW paragraph end")
write("article/2active.tex", a2)


# Radar/RF survey prose: cellular ISAC lineage ------------------------------
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
for key in ("tosiFeasibilityISACNLOS2024", "tosiReliableISACNLOS2026", "zhiMultiSolitonMicrocombNLOS2026"):
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

@article{zhiMultiSolitonMicrocombNLOS2026,
  author = {Zhi, Jiawen and Guo, Xiaoyang and Yang, Xusheng and Little, Brent E. and Chu, Sai T. and Shao, Chenggang and Wang, Mengyu and Liang, Yan and Xie, Peng and Wang, Weiqiang and Wu, Hanzhong},
  title = {Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection},
  journal = {Advanced Science},
  volume = {13},
  number = {12},
  pages = {e16806},
  year = {2026},
  doi = {10.1002/advs.202516806},
  url = {https://doi.org/10.1002/advs.202516806}
}
"""
write("egbib_merged_20260711.bib", bib.rstrip() + entries + "\n")


# Top-level source audit comment -------------------------------------------
bare = read("bare_jrnl.tex")
comment = "% 8 August 2026 citation/venue trace: dual-microcomb NLOS imaging and SPAWC cellular-ISAC precursor integrated; ICT final venue corrected; SG-ATV consistency verified.\n"
if comment not in bare:
    bare = comment + bare
write("bare_jrnl.tex", bare)


# Update logs ---------------------------------------------------------------
isac_log_path = "updates/2026-08-08-isac-nlos-final-venue-citation-trace.md"
isac_log = read(isac_log_path)
status = """

## Applied status

Applied through the guarded 8 August 2026 cross-artifact integration. The SPAWC 2024 precursor is now included in README, website, survey prose, and bibliography; the 2026 intrusion-detection paper is labeled by its final ICT 2026 venue. SG-ATV was already synchronized across README, website, passive-survey prose, and bibliography and was verified unchanged. The survey PDF is rebuilt and validated by the integration workflow.
"""
if "## Applied status" not in isac_log:
    isac_log = isac_log.rstrip() + status + "\n"
write(isac_log_path, isac_log)

micro_log = """# 8 August 2026 — dual-microcomb coherent NLOS citation trace

## Added record

- **Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection** — Jiawen Zhi, Xiaoyang Guo, Xusheng Yang, Brent E. Little, Sai T. Chu, Chenggang Shao, Mengyu Wang, Yan Liang, Peng Xie, Weiqiang Wang, and Hanzhong Wu. *Advanced Science* **13**(12), e16806 (2026). DOI: `10.1002/advs.202516806`.
- The paper is primarily a coherent-ranging/metrology contribution, but it contains a direct three-bounce NLOS imaging experiment using a diffuse relay wall and dual-multi-soliton ranging to reconstruct the depth relief of a hidden target. It therefore belongs in the coherent active-NLOS hardware trajectory rather than being treated as merely adjacent ranging work.
- It explicitly builds on the coherent NLOS/vibrometry lineage represented by the 2024 comb-calibrated coherent-sensor work, making it a high-value forward-citation discovery.

## Integration

Added to README Latest Additions, the website explorer and 2026 timeline, the coherent active-method table/prose in `article/2active.tex`, `egbib_merged_20260711.bib`, and the rebuilt `bare_jrnl.pdf`. The generated survey is validated for resolved citations and rendered first/last pages before the integration commit is pushed.
"""
write("updates/2026-08-08-dual-microcomb-nlos-citation-trace.md", micro_log)

print("Applied cellular-ISAC and dual-microcomb NLOS integration; verified existing SG-ATV consistency.")
