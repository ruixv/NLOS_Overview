from pathlib import Path
import re

PAPERS = [
    {
        "key": "chenJointNLOSLayoutTargets2022",
        "doi": "10.1109/TGRS.2022.3182429",
        "year": 2022,
        "title": "Joint Estimation of NLOS Building Layout and Targets via Sparsity-Driven Approach",
        "authors_short": "Chen et al.",
        "venue": "IEEE TGRS 60, 1–13 (2022), Art. 5114513",
        "summary": "Removes the known-layout prerequisite by jointly estimating hidden targets and building geometry from MIMO multipath, combining a parameterized propagation model with shape-remodeling group sparsity and particle-swarm search.",
        "cat": "latest rf radar nlos multipath unknown-layout joint-estimation sparse",
    },
    {
        "key": "wuAssociationHypothesisNLOS2023",
        "doi": "10.1109/TGRS.2023.3250831",
        "year": 2023,
        "title": "NLOS Positioning for Building Layout and Target Based on Association and Hypothesis Method",
        "authors_short": "Wu et al.",
        "venue": "IEEE TGRS 61, 1–13 (2023), Art. 5101913",
        "summary": "Jointly estimates an unknown L-shaped building layout and hidden target without prior map information by combining diffraction/multiple-reflection modeling, MTI/backprojection preprocessing, geometric association, and multipath-ghost hypotheses.",
        "cat": "latest rf radar nlos multipath unknown-layout association diffraction",
    },
    {
        "key": "zhuDoDDoANLOS2023",
        "doi": "10.1109/TIM.2023.3323003",
        "year": 2023,
        "title": "Non-Line-of-Sight Targets Localization Algorithm via Joint Estimation of DoD and DoA",
        "authors_short": "Zhu et al.",
        "venue": "IEEE Transactions on Instrumentation and Measurement 72, 1–11 (2023)",
        "summary": "Extends L-corner multi-target radar localization beyond ToA by modeling range, Doppler, DoD and DoA, estimating the reflector from static points, recognizing multipath from joint departure/arrival angles, and recovering targets by mirror symmetry.",
        "cat": "latest rf radar mmwave nlos multipath dod doa multitarget",
    },
    {
        "key": "xuMultiDomainFeaturesNLOS2023",
        "doi": "10.1109/JSEN.2023.3325976",
        "year": 2023,
        "title": "Multi-Domain Features-Based NLOS Target Localization Method for MIMO UWB Radar",
        "authors_short": "Xu et al.",
        "venue": "IEEE Sensors Journal 23(23), 29314–29322 (2023)",
        "summary": "Uses range–Doppler topology to associate measured ToAs with target-specific multipath classes, then combines angle and range information for multi-target UWB MIMO localization in L-shaped NLOS scenes.",
        "cat": "latest rf radar uwb nlos multipath range-doppler multidomain",
    },
    {
        "key": "chenDriverAssistanceNLOS2023",
        "doi": "10.1109/TVT.2022.3227971",
        "year": 2023,
        "title": "Non-Line-of-Sight Multi-Target Localization Algorithm for Driver-Assistance Radar System",
        "authors_short": "Chen et al.",
        "venue": "IEEE Transactions on Vehicular Technology 72(4), 5332–5337 (2023)",
        "summary": "Targets blind street-corner driver assistance: matrix-pencil ToA estimation and joint range/angle path recognition pair L-shaped multipath returns with multiple hidden vehicles or pedestrians, with simulation and experimental validation.",
        "cat": "latest rf radar automotive nlos multipath multitarget driver-assistance",
    },
    {
        "key": "xuMultiDomainAssociationNLOS2025",
        "doi": "10.1007/978-981-96-3576-4_29",
        "year": 2025,
        "title": "Joint Estimation of NLOS Building Layout and Target Position Based on Multi-domain Association",
        "authors_short": "Xu et al.",
        "venue": "Springer LNEE 1379 (4th ICAUS 2024 proceedings), 313–322 (2025)",
        "summary": "Combines spatial- and time-domain associations with DoD/DoA-aware multipath recognition, then uses angle and range information to jointly estimate building layout and hidden-target position.",
        "cat": "latest rf radar nlos multipath unknown-layout multidomain association",
    },
    {
        "key": "zhouNLOSBuildingLayoutInSAR2025",
        "doi": "10.1109/IGARSS55030.2025.11244088",
        "year": 2025,
        "title": "On the NLOS Building Layout Relocation in Array InSAR 3D Imaging",
        "authors_short": "Zhou et al.",
        "venue": "IEEE IGARSS 2025, 9526–9530",
        "summary": "Extends unknown-environment NLOS inference into array-InSAR/TomoSAR 3D scene formation by addressing relocation of building layout under NLOS propagation in UAV-borne array imaging.",
        "cat": "latest rf radar sar insar nlos unknown-layout 3d-imaging",
    },
]

BIB_ENTRIES = r'''

@article{chenJointNLOSLayoutTargets2022,
  author = {Chen, Jiahui and Zhang, Yang and Guo, Shisheng and Cui, Guolong and Wu, Peilun and Jia, Chao and Kong, Lingjiang},
  title = {Joint Estimation of NLOS Building Layout and Targets via Sparsity-Driven Approach},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {60},
  pages = {1--13},
  year = {2022},
  doi = {10.1109/TGRS.2022.3182429},
  url = {https://doi.org/10.1109/TGRS.2022.3182429}
}

@article{wuAssociationHypothesisNLOS2023,
  author = {Wu, Peilun and Chen, Jiahui and Guo, Shisheng and Cui, Guolong and Kong, Lingjiang and Yang, Xiaobo},
  title = {NLOS Positioning for Building Layout and Target Based on Association and Hypothesis Method},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {61},
  pages = {1--13},
  year = {2023},
  doi = {10.1109/TGRS.2023.3250831},
  url = {https://doi.org/10.1109/TGRS.2023.3250831}
}

@article{zhuDoDDoANLOS2023,
  author = {Zhu, Zhihao and Guo, Shisheng and Chen, Jiahui and Xue, Shucheng and Xu, Zihan and Wu, Peilun and Cui, Guolong and Kong, Lingjiang},
  title = {Non-Line-of-Sight Targets Localization Algorithm via Joint Estimation of DoD and DoA},
  journal = {IEEE Transactions on Instrumentation and Measurement},
  volume = {72},
  pages = {1--11},
  year = {2023},
  doi = {10.1109/TIM.2023.3323003},
  url = {https://doi.org/10.1109/TIM.2023.3323003}
}

@article{xuMultiDomainFeaturesNLOS2023,
  author = {Xu, Zihan and Guo, Shisheng and Chen, Jiahui and Zhu, Zhihao and Xue, Shucheng and Wu, Peilun and Cui, Guolong and Kong, Lingjiang},
  title = {Multi-Domain Features-Based NLOS Target Localization Method for MIMO UWB Radar},
  journal = {IEEE Sensors Journal},
  volume = {23},
  number = {23},
  pages = {29314--29322},
  year = {2023},
  doi = {10.1109/JSEN.2023.3325976},
  url = {https://doi.org/10.1109/JSEN.2023.3325976}
}

@article{chenDriverAssistanceNLOS2023,
  author = {Chen, Jiahui and Guo, Shisheng and Luo, Haolan and Li, Nian and Cui, Guolong},
  title = {Non-Line-of-Sight Multi-Target Localization Algorithm for Driver-Assistance Radar System},
  journal = {IEEE Transactions on Vehicular Technology},
  volume = {72},
  number = {4},
  pages = {5332--5337},
  year = {2023},
  doi = {10.1109/TVT.2022.3227971},
  url = {https://doi.org/10.1109/TVT.2022.3227971}
}

@incollection{xuMultiDomainAssociationNLOS2025,
  author = {Xu, Zihan and Qiu, Chen and Guo, Shisheng and Xue, Shucheng and Zhu, Zhihao and Wu, Peilun and Wu, Nan and Chen, Jiahui and Cui, Guolong},
  title = {Joint Estimation of NLOS Building Layout and Target Position Based on Multi-domain Association},
  booktitle = {Proceedings of 4th 2024 International Conference on Autonomous Unmanned Systems (4th ICAUS 2024): Volume VI},
  series = {Lecture Notes in Electrical Engineering},
  volume = {1379},
  pages = {313--322},
  publisher = {Springer Nature Singapore},
  year = {2025},
  doi = {10.1007/978-981-96-3576-4_29},
  url = {https://doi.org/10.1007/978-981-96-3576-4_29}
}

@inproceedings{zhouNLOSBuildingLayoutInSAR2025,
  author = {Zhou, Yisen and Guo, Shisheng and Zhu, Zhihao and Zeng, Xujing and Yu, Yupeng and Wang, Yubo and Cui, Guolong},
  title = {On the NLOS Building Layout Relocation in Array InSAR 3D Imaging},
  booktitle = {2025 IEEE International Geoscience and Remote Sensing Symposium (IGARSS)},
  pages = {9526--9530},
  year = {2025},
  doi = {10.1109/IGARSS55030.2025.11244088},
  url = {https://doi.org/10.1109/IGARSS55030.2025.11244088}
}
'''


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {n}")
    return text.replace(old, new, 1)


def regex_once(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one regex match, found {n}")
    return out


# README: newly found historical gaps belong in Latest Additions and in their development years.
readme = read("README.md")
readme = readme.replace("**Update run: 23 August 2026.**", "**Update run: 24 August 2026.**")
missing_rows = []
for p in PAPERS:
    if p["doi"].lower() not in readme.lower():
        missing_rows.append(
            f'| {p["year"]} | [{p["title"]}](https://doi.org/{p["doi"]}) — {p["authors_short"]} | '
            f'{p["venue"]} | {p["summary"]} |\n'
        )
if missing_rows:
    anchor = "|------|-------|----------------|----------------|\n"
    readme = replace_once(readme, anchor, anchor + "".join(missing_rows), "README Latest Additions table")

readme_timeline = {
    2022: "   │     Chen et al.: joint sparsity-driven estimation made unknown building layout part of the MIMO-radar NLOS inverse problem instead of a fixed calibration input [IEEE TGRS]\n",
    2023: "   │     Wu/Xu/Zhu/Chen et al.: association-and-hypothesis, range–Doppler topology, DoD/DoA, and driver-assistance multipath pairing expanded unknown-layout NLOS radar to robust multi-target localization [IEEE TGRS/TIM/Sensors Journal/TVT]\n",
    2025: "   │     Xu et al. combined spatial/time-domain associations for joint target–layout inference, while Zhou et al. extended NLOS building-layout relocation to array-InSAR/TomoSAR 3D imaging [Springer ICAUS / IEEE IGARSS]\n",
}
for year, line in readme_timeline.items():
    marker = line.strip()
    if marker not in readme:
        pattern = rf"(^\s*{year} ──[^\n]*\n)"
        readme = regex_once(readme, pattern, lambda m, line=line: m.group(1) + line, f"README {year} timeline", flags=re.M)
write("README.md", readme)


# V2 wrapper date.
index = read("index.html")
if "Updated 24 Aug 2026" not in index:
    if "Updated 23 Aug 2026" not in index:
        raise RuntimeError("index.html public-date anchor not found")
    index = index.replace("Updated 23 Aug 2026", "Updated 24 Aug 2026")
write("index.html", index)


# Canonical V2 paper corpus / explorer / timeline.
corpus = read("data/papers-source.html")
objs = []
for p in PAPERS:
    if p["doi"].lower() not in corpus.lower():
        title = p["title"].replace('"', '&quot;')
        summary = p["summary"].replace('"', '&quot;')
        objs.append(
            f'      {{cat:"{p["cat"]}",title:"{title}",authors:"{p["authors_short"]}",year:{p["year"]},'
            f'venue:"{p["venue"]}",url:"https://doi.org/{p["doi"]}",key:"{summary}"}},\n'
        )
if objs:
    corpus = replace_once(corpus, "    const papers=[\n", "    const papers=[\n" + "".join(objs), "V2 canonical paper array")

def append_timeline_year(html, year, sentence, marker):
    if marker in html:
        return html
    pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
    def repl(m):
        body = m.group(2).rstrip()
        if body and not body.endswith(" "):
            body += " "
        return m.group(1) + body + sentence + m.group(3)
    return regex_once(html, pattern, repl, f"V2 {year} timeline", flags=re.S)

corpus = append_timeline_year(
    corpus, 2022,
    "Chen et al. also made the relay map itself unknown, jointly estimating NLOS building layout and targets from MIMO multipath with sparsity-driven inference.",
    "made the relay map itself unknown",
)
corpus = append_timeline_year(
    corpus, 2023,
    "A radar lineage then combined association-and-hypothesis reasoning, range–Doppler topology, joint DoD/DoA, and driver-assistance path pairing to make unknown-layout and multi-target NLOS localization increasingly structured and robust.",
    "association-and-hypothesis reasoning",
)
corpus = append_timeline_year(
    corpus, 2025,
    "Multi-domain spatial/time association further coupled hidden-target and layout estimation, while array-InSAR work extended NLOS building-layout relocation into UAV-borne 3D scene formation.",
    "array-InSAR work extended NLOS building-layout relocation",
)

# Recompute canonical paper count.
arr_start = corpus.find("    const papers=[")
arr_end = corpus.find("\n    ];", arr_start)
if arr_start < 0 or arr_end < 0:
    raise RuntimeError("could not locate canonical paper array")
tracked = corpus[arr_start:arr_end].count("{cat:")
corpus, n = re.subn(
    r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)',
    rf'\g<1>{tracked}\g<2>', corpus, count=1,
)
if n != 1:
    raise RuntimeError("could not update V2 tracked-entry count")
corpus = corpus.replace("Updated 23 August 2026", "Updated 24 August 2026")
corpus = corpus.replace("Last updated: 23 August 2026", "Last updated: 24 August 2026")
write("data/papers-source.html", corpus)


# Radar survey: repair the historical precursor chain immediately before the existing 2025 unknown-geometry paragraph.
radar = read("article/5newscenes.tex")
keys = [p["key"] for p in PAPERS]
if not all(k in radar for k in keys):
    heading = "\\noindent \\textbf{From assumed relay geometry to joint environment and target inference.}\n"
    paragraph = r'''The removal of known relay geometry began earlier than the recent 2025 reflector-estimation work. Chen \etal~\cite{chenJointNLOSLayoutTargets2022} parameterized the L-shaped multipath geometry and coupled shape-remodeling group sparsity with particle-swarm search so that MIMO radar can jointly reconstruct multiple hidden targets and the unknown building layout. Wu \etal~\cite{wuAssociationHypothesisNLOS2023} replaced a fixed map with diffraction- and reflection-aware geometric association and multipath-ghost hypotheses, jointly estimating the L-shaped layout and hidden target from MTI/backprojection observations. For multi-target cases, Zhu \etal~\cite{zhuDoDDoANLOS2023} expanded path recognition from time of arrival alone to range, Doppler, DoD, and DoA, estimating the reflector from static radar points before mirror-symmetry localization; Chen \etal~\cite{chenDriverAssistanceNLOS2023} adapted multipath pairing to driver-assistance radar using matrix-pencil delay estimates and joint range/angle constraints. Xu \etal~\cite{xuMultiDomainFeaturesNLOS2023} then formalized a range--Doppler topology that matches ToAs to path classes and targets, and a later multi-domain association study combined spatial and temporal cues to jointly recover building layout and target position~\cite{xuMultiDomainAssociationNLOS2025}. Zhou \etal~\cite{zhouNLOSBuildingLayoutInSAR2025} further extended the unknown-layout problem into array-InSAR/TomoSAR 3-D imaging by explicitly addressing NLOS building-layout relocation. These works establish the precursor trajectory for the reflective-surface and joint environment/target methods below.\n\n'''
    radar = replace_once(radar, heading, heading + paragraph, "radar unknown-layout heading")
write("article/5newscenes.tex", radar)


# Canonical merged bibliography: append only fully missing records; fail closed on partial/duplicate states.
bib = read("egbib_merged_20260711.bib")
new_entries = []
for p in PAPERS:
    key_n = len(re.findall(r"@[A-Za-z]+\{" + re.escape(p["key"]) + r",", bib, flags=re.I))
    doi_n = bib.lower().count(p["doi"].lower())
    if key_n == 0 and doi_n == 0:
        # Pull the exact entry from the verified block below.
        pattern = r"@[A-Za-z]+\{" + re.escape(p["key"]) + r",.*?\n\}"
        m = re.search(pattern, BIB_ENTRIES, flags=re.S | re.I)
        if not m:
            raise RuntimeError(f"missing prepared BibTeX entry for {p['key']}")
        new_entries.append(m.group(0))
    elif key_n != 1 or doi_n != 1:
        raise RuntimeError(f"partial/duplicate bibliography state for {p['key']}: key={key_n}, doi={doi_n}")
if new_entries:
    bib = bib.rstrip() + "\n\n" + "\n\n".join(new_entries) + "\n"
write("egbib_merged_20260711.bib", bib)


# Survey provenance.
tex = read("bare_jrnl.tex")
note = "% 24 August 2026 radar citation trace: unknown-layout, multi-domain path association, driver-assistance multi-target localization, and array-InSAR layout-relocation precursors synchronized.\n"
if note not in tex:
    tex = note + tex
write("bare_jrnl.tex", tex)


# Final source-level assertions.
for p in PAPERS:
    for path in ["README.md", "data/papers-source.html", "egbib_merged_20260711.bib"]:
        if p["doi"].lower() not in read(path).lower():
            raise RuntimeError(f"missing DOI {p['doi']} from {path}")
    if p["key"] not in read("article/5newscenes.tex"):
        raise RuntimeError(f"missing survey citation key {p['key']}")

print(f"Prepared {len(PAPERS)} verified radar NLOS lineage records; V2 tracked entries={tracked}")
