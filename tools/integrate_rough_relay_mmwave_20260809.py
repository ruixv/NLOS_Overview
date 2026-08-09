from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing",
        "row": "| 2024 | [Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing](https://doi.org/10.1109/JIOT.2023.3328018) — Xu, Liu, Jiang | IEEE Internet of Things Journal 11(6), 10964–10978 (2024) | Models rough relay walls with stochastic microfacets and turns the resulting scattering diversity into useful NLOS measurements. Its stochastic-geometry-aided three-stage recovery uses virtual ghost targets rather than suppressing them, extending commodity-mmWave sensing beyond ideal smooth-wall specular assumptions. |",
        "obj": "      {cat:\"latest modality radar rf mmwave rough-relay scattering imaging sensing measured\",title:\"Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing\",authors:\"Xu, Liu, Jiang\",year:2024,venue:\"IEEE IoT Journal 11(6), 10964–10978 (2024)\",url:\"https://doi.org/10.1109/JIOT.2023.3328018\",key:\"Models rough relay walls as stochastic microfacets and exploits their scattering diversity with SGTR, converting multipath ghost targets into useful around-corner recovery cues instead of assuming a smooth specular wall.\"},",
    },
    {
        "title": "Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface",
        "row": "| 2024 | [Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface](https://doi.org/10.1109/TSP.2024.3505938) — Xu et al. | IEEE Transactions on Signal Processing 72, 5628–5643 (2024) | Formulates multi-angle-relay mmWave NLOS imaging with an automotive-squint SAR model and a double-sparse hidden-image structure. Time-domain double-sparse thresholding and an approximate frequency-domain operator improve reconstruction under heterogeneous relay orientations in simulation and measured experiments. |",
        "obj": "      {cat:\"latest modality radar rf mmwave multiangle relay sparse reconstruction measured\",title:\"Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface\",authors:\"Xu et al.\",year:2024,venue:\"IEEE TSP 72, 5628–5643 (2024)\",url:\"https://doi.org/10.1109/TSP.2024.3505938\",key:\"Uses an automotive-squint SAR model plus double-sparse image structure, TD-DSTA optimization, and an approximate frequency-domain operator for measured NLOS imaging with heterogeneous multi-angle relay surfaces.\"},",
    },
    {
        "title": "Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces",
        "row": "| 2025 | [Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces](https://doi.org/10.1109/LSP.2025.3567216) — Xu et al. | IEEE Signal Processing Letters 32, 2075–2079 (2025) | Treats relay-surface angles as uncertain dictionary parameters instead of perfectly known geometry. A double-sparse spike-and-slab prior, expectation-propagation inference, and EM-based parameter updates reduce NLOS reconstruction error when multi-angle relay layouts are imprecisely calibrated. |",
        "obj": "      {cat:\"latest modality radar rf mmwave bayesian sparse multiangle relay calibration reconstruction\",title:\"Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces\",authors:\"Xu et al.\",year:2025,venue:\"IEEE SPL 32, 2075–2079 (2025)\",url:\"https://doi.org/10.1109/LSP.2025.3567216\",key:\"Treats multi-angle relay orientations as uncertain dictionary parameters and combines a double-sparse spike-and-slab prior, expectation propagation, and EM updates for calibration-robust mmWave NLOS reconstruction.\"},",
    },
    {
        "title": "mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing",
        "row": "| 2025 | [mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing](https://doi.org/10.1109/INFOCOM55648.2025.11044715) — Lv et al. | IEEE INFOCOM 2025, 1–10 | Reconstructs the relay reflector from mmWave measurements themselves before around-corner human sensing, removing the common dependence on LiDAR or manually supplied wall geometry. This makes reflector geometry part of the sensing problem rather than a fixed calibration input. |",
        "obj": "      {cat:\"latest modality radar rf mmwave reflector reconstruction lidar-free human sensing around-corner\",title:\"mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing\",authors:\"Lv et al.\",year:2025,venue:\"IEEE INFOCOM 2025, 1–10\",url:\"https://doi.org/10.1109/INFOCOM55648.2025.11044715\",key:\"Reconstructs relay-reflector geometry directly from mmWave data and then performs around-corner human sensing, removing the LiDAR or known-wall-geometry prerequisite used by many earlier systems.\"},",
    },
    {
        "title": "Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar",
        "row": "| 2024 | [Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar](https://doi.org/10.1145/3636534.3690710) — Mehrotra et al. | ACM MobiCom 2024, 1545–1559 | Explicitly models and exploits multi-bounce scattering so a standalone commodity mmWave radar can localize objects outside its transmit beam, behind occlusions, or even behind the radar without prior environment knowledge. Across five real environments it reports 2×–10× lower median beyond-FOV localization error than baselines. |",
        "obj": "      {cat:\"latest modality radar rf mmwave multibounce beyond-fov localization measured\",title:\"Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar\",authors:\"Mehrotra et al.\",year:2024,venue:\"ACM MobiCom 2024, 1545–1559\",url:\"https://doi.org/10.1145/3636534.3690710\",key:\"Explicitly exploits multi-bounce scattering to localize objects outside the transmit beam, behind occlusions, or behind the radar without environment priors; five real environments show 2×–10× lower median beyond-FOV error.\"},",
    },
    {
        "title": "MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions",
        "row": "| 2026 | [MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions](https://doi.org/10.1109/MAES.2026.3701667) — Liu et al. | IEEE Aerospace and Electronic Systems Magazine, 2026 | Synthesizes the emerging rough-relay mmWave NLOS problem: real building materials and non-flat surfaces break smooth-specular assumptions but also create exploitable scattering diversity. The article organizes the modeling, multipath-management, and recovery challenges that connect rough-wall sensing to the 2024–2025 reconstruction methods. |",
        "obj": "      {cat:\"latest survey modality radar rf mmwave rough-relay overview\",title:\"MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions\",authors:\"Liu et al.\",year:2026,venue:\"IEEE Aerospace and Electronic Systems Magazine 2026\",url:\"https://doi.org/10.1109/MAES.2026.3701667\",key:\"Overview of realistic rough-relay mmWave NLOS: explains why non-flat building materials violate ideal specular assumptions and organizes scattering models, multipath-management strategies, and reconstruction solutions.\"},",
    },
]

SURVEY_ANCHOR = "Together, these works show a clear RF trajectory from point localization, through reflector-aware imaging and surface-normal recovery, to learned full-object and scene-level geometry."
SURVEY_TEXT = r'''\vspace{0.8mm}
\noindent \textbf{Rough, uncertain, and unknown relay geometry in mmWave NLOS.}
A complementary radar trajectory removes the ideal planar/specular relay assumption itself. Xu~\etal~model rough relay surfaces as stochastic microfacet scatterers and deliberately exploit the resulting multipath diversity with a stochastic-geometry-aided recovery procedure~\cite{xuRoughRelayMmWave2024}. Their later multi-angle formulation uses an automotive-squint SAR model and a double-sparse image prior to separate structure shared across heterogeneous relay orientations~\cite{xuDoubleSparseMmWave2024}; when those orientations are only approximately known, a Bayesian extension treats the relay angles as latent dictionary parameters and alternates expectation-propagation inference with parameter updates~\cite{xuBayesianMmWave2025}. Lv~\etal~push calibration further by reconstructing the relay reflector directly from mmWave measurements before around-corner human sensing, removing the dependence on LiDAR-provided reflector geometry~\cite{lvRelayReflector2025}. In parallel, Hydra explicitly models multi-bounce scattering from uncontrolled intermediate objects and localizes targets beyond the transmit field of view without prior environment knowledge~\cite{mehrotraHydra2024}. A 2026 Aerospace and Electronic Systems Magazine overview consolidates these rough-relay challenges and solutions~\cite{liuRoughRelaySurvey2026}. Taken together, this branch changes relay geometry from a fixed prerequisite into an estimated, uncertain, or even beneficial part of the inverse problem, complementing HoloRadar/RFlect-style reflector-aware reconstruction and the newer learned full-scene systems.'''

BIB_ENTRIES = r'''

@article{xuRoughRelayMmWave2024,
  author = {Xu, You and Liu, Guanghua and Jiang, Tao},
  title = {Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing},
  journal = {IEEE Internet of Things Journal},
  volume = {11},
  number = {6},
  pages = {10964--10978},
  year = {2024},
  doi = {10.1109/JIOT.2023.3328018},
  url = {https://doi.org/10.1109/JIOT.2023.3328018}
}

@article{xuDoubleSparseMmWave2024,
  author = {Xu, You and Liu, Guanghua and Lu, Xiaotong and Xie, Chao and Xiao, Lixia and Jiang, Tao},
  title = {Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface},
  journal = {IEEE Transactions on Signal Processing},
  volume = {72},
  pages = {5628--5643},
  year = {2024},
  doi = {10.1109/TSP.2024.3505938},
  url = {https://doi.org/10.1109/TSP.2024.3505938}
}

@article{xuBayesianMmWave2025,
  author = {Xu, You and Liu, Guanghua and Lu, Xiaotong and Xiao, Lixia and Jiang, Tao},
  title = {Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces},
  journal = {IEEE Signal Processing Letters},
  volume = {32},
  pages = {2075--2079},
  year = {2025},
  doi = {10.1109/LSP.2025.3567216},
  url = {https://doi.org/10.1109/LSP.2025.3567216}
}

@inproceedings{lvRelayReflector2025,
  author = {Lv, Jiaxi and Fan, Guiyun and Fu, Xinyue and Sun, Jiahui and Ding, Rong and Jin, Haiming},
  title = {mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing},
  booktitle = {IEEE INFOCOM 2025 - IEEE Conference on Computer Communications},
  pages = {1--10},
  year = {2025},
  doi = {10.1109/INFOCOM55648.2025.11044715},
  url = {https://doi.org/10.1109/INFOCOM55648.2025.11044715}
}

@inproceedings{mehrotraHydra2024,
  author = {Mehrotra, Nishant and Pandey, Divyanshu and Prabhakara, Akarsh and Liu, Yawen and Kumar, Swarun and Sabharwal, Ashutosh},
  title = {Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar},
  booktitle = {Proceedings of the 30th Annual International Conference on Mobile Computing and Networking},
  pages = {1545--1559},
  year = {2024},
  publisher = {ACM},
  doi = {10.1145/3636534.3690710},
  url = {https://doi.org/10.1145/3636534.3690710}
}

@article{liuRoughRelaySurvey2026,
  author = {Liu, Guanghua and Lu, Xiaotong and Xu, You and Yuan, Haoran},
  title = {MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions},
  journal = {IEEE Aerospace and Electronic Systems Magazine},
  year = {2026},
  doi = {10.1109/MAES.2026.3701667},
  url = {https://doi.org/10.1109/MAES.2026.3701667},
  note = {Early access}
}
'''

UPDATE_NOTE = '''# 9 August 2026 rough-relay mmWave citation-trace update

A forward/backward citation-tracing pass around HoloRadar, RFlect, classical around-corner radar, and recent rough-relay mmWave work exposed a coherent missing branch that was not represented in the public README, website explorer, or survey text.

Integrated records:

- Xu, Liu, Jiang, **Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing**, IEEE Internet of Things Journal 11(6), 10964–10978 (2024), DOI 10.1109/JIOT.2023.3328018.
- Xu et al., **Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface**, IEEE Transactions on Signal Processing 72, 5628–5643 (2024), DOI 10.1109/TSP.2024.3505938.
- Xu et al., **Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces**, IEEE Signal Processing Letters 32, 2075–2079 (2025), DOI 10.1109/LSP.2025.3567216.
- Lv et al., **mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing**, IEEE INFOCOM 2025, 1–10, DOI 10.1109/INFOCOM55648.2025.11044715.
- Mehrotra et al., **Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar**, ACM MobiCom 2024, 1545–1559, DOI 10.1145/3636534.3690710.
- Liu et al., **MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions**, IEEE Aerospace and Electronic Systems Magazine (2026), DOI 10.1109/MAES.2026.3701667.

The survey integration treats these as one trajectory: rough and multi-angle relay surfaces first become useful stochastic/scattering structure, then uncertain relay geometry becomes a latent inference variable, and finally the reflector/environment itself is reconstructed or bypassed through multi-bounce modeling. This complements the already-covered HoloRadar, RFlect, CornerRadar, Mosaic, mmNorm, RISE, and Wave-Former lineage instead of duplicating it.

The searchable website count increases from 268 to 274. The rebuilt PDF must contain the new radar paragraph and all six bibliography entries before this update is considered complete.
'''


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def patch_readme():
    path = "README.md"
    text = read(path)
    start = text.index("## Latest Additions")
    end = text.index("\n---", start)
    header = "|------|-------|----------------|----------------|"
    pos = text.index(header, start, end) + len(header)
    insertion = []
    latest = text[start:end]
    for p in PAPERS:
        if p["title"] not in latest:
            insertion.append(p["row"])
    if insertion:
        text = text[:pos] + "\n" + "\n".join(insertion) + text[pos:]

    # Add concise trajectory notes to the existing milestone rows, without creating duplicate year rows.
    milestone = text.index("## Milestone Timeline")
    for year, sentence in {
        "2024": " Rough-relay scattering, multi-angle sparse inversion, and Hydra's environment-free multi-bounce sensing expanded RF NLOS beyond smooth planar reflectors.",
        "2025": " Relay-angle uncertainty became part of Bayesian inversion, while LiDAR-free reflector reconstruction made the relay geometry itself an estimated quantity.",
        "2026": " A dedicated rough-relay mmWave overview consolidated realistic scattering-surface challenges and solutions.",
    }.items():
        if sentence.strip() not in text[milestone:]:
            pat = re.compile(rf"^(\| {year} \| )(.*?)( \|)$", re.M)
            m = pat.search(text, milestone)
            if not m:
                raise RuntimeError(f"README milestone row {year} not found")
            text = text[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + text[m.end():]
    write(path, text)


def append_index_timeline(text, year, sentence):
    if sentence in text:
        return text
    pat = re.compile(rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"index timeline year {year} not found")
    return text[:m.start()] + m.group(1) + m.group(2) + " " + sentence + m.group(3) + text[m.end():]


def patch_index():
    path = "index.html"
    text = read(path)
    anchor = "    const papers=[\n"
    if text.count(anchor) != 1:
        raise RuntimeError("index paper-array anchor is not unique")
    new_objects = [p["obj"] for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if new_objects:
        text = text.replace(anchor, anchor + "\n".join(new_objects) + "\n", 1)

    # The preceding MARMOT/N2LoS/ISAC pass leaves the explorer at 268; six verified records raise it to 274.
    text = text.replace('<div class="stat"><b>268</b><span>tracked latest entries</span></div>', '<div class="stat"><b>274</b><span>tracked latest entries</span></div>')
    text = append_index_timeline(text, "2024", "Rough-relay stochastic scattering, multi-angle sparse inversion, and Hydra's environment-free multi-bounce sensing expanded mmWave NLOS beyond ideal planar reflectors.")
    text = append_index_timeline(text, "2025", "Bayesian relay-angle inference and LiDAR-free reflector reconstruction made relay geometry an estimated part of the inverse problem.")
    text = append_index_timeline(text, "2026", "A dedicated IEEE AES Magazine overview consolidated rough-relay mmWave challenges and solutions.")
    write(path, text)


def patch_survey():
    path = "article/5newscenes.tex"
    text = read(path)
    if "xuRoughRelayMmWave2024" not in text:
        if text.count(SURVEY_ANCHOR) != 1:
            raise RuntimeError(f"radar survey anchor count is {text.count(SURVEY_ANCHOR)}, expected 1")
        text = text.replace(SURVEY_ANCHOR, SURVEY_ANCHOR + "\n\n" + SURVEY_TEXT, 1)
    write(path, text)


def patch_bib():
    path = "egbib_merged_20260711.bib"
    text = read(path)
    keys = ["xuRoughRelayMmWave2024", "xuDoubleSparseMmWave2024", "xuBayesianMmWave2025", "lvRelayReflector2025", "mehrotraHydra2024", "liuRoughRelaySurvey2026"]
    if any(key in text for key in keys):
        present = [key for key in keys if key in text]
        if len(present) != len(keys):
            raise RuntimeError(f"partial rough-relay bibliography integration detected: {present}")
    else:
        text = text.rstrip() + BIB_ENTRIES + "\n"
    write(path, text)


def patch_master_tex_and_note():
    path = "bare_jrnl.tex"
    text = read(path)
    marker = "% 9 August 2026 citation trace: rough-relay, uncertain-relay, reflector-reconstruction, and multi-bounce mmWave NLOS lineage integrated.\n"
    if not text.startswith(marker):
        text = marker + text
    write(path, text)
    write("updates/2026-08-09-rough-relay-mmwave-citation-trace.md", UPDATE_NOTE)


def validate():
    readme = read("README.md")
    index = read("index.html")
    survey = read("article/5newscenes.tex")
    bib = read("egbib_merged_20260711.bib")
    tex = read("bare_jrnl.tex")
    for p in PAPERS:
        assert p["title"] in readme
        assert p["title"] in index
    for key in ["xuRoughRelayMmWave2024", "xuDoubleSparseMmWave2024", "xuBayesianMmWave2025", "lvRelayReflector2025", "mehrotraHydra2024", "liuRoughRelaySurvey2026"]:
        assert survey.count(key) == 1
        assert bib.count("{" + key + ",") == 1
    for doi in ["10.1109/JIOT.2023.3328018", "10.1109/TSP.2024.3505938", "10.1109/LSP.2025.3567216", "10.1109/INFOCOM55648.2025.11044715", "10.1145/3636534.3690710", "10.1109/MAES.2026.3701667"]:
        assert doi in readme and doi in bib
    assert '<div class="stat"><b>274</b><span>tracked latest entries</span></div>' in index
    assert "Rough, uncertain, and unknown relay geometry in mmWave NLOS" in survey
    assert "rough-relay, uncertain-relay" in tex


if __name__ == "__main__":
    patch_readme()
    patch_index()
    patch_survey()
    patch_bib()
    patch_master_tex_and_note()
    validate()
    print("Rough-relay / multi-angle / unknown-reflector / multi-bounce mmWave citation-trace integration passed.")
