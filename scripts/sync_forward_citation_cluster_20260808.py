from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "key": "zhaiSecondOrderAcousticNLOS2025",
        "title": "Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction",
        "year": 2025,
        "authors": "Zhai et al.",
        "venue": "Applied Acoustics 228, 110369 (2025)",
        "url": "https://doi.org/10.1016/j.apacoust.2024.110369",
        "summary": "Uses the Biot–Tolstoy–Medwin second-order edge-diffraction response as a sensing operator and block sparse Bayesian learning to localize hidden acoustic sources when direct and first-order paths are unavailable; validated with simulation and a 32-channel array.",
        "cat": "latest modality acoustic localization diffraction sparse-bayesian microphone-array measured",
    },
    {
        "key": "jeonTJunctionMmWaveNLOS2025",
        "title": "Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar",
        "year": 2025,
        "authors": "Jeon et al.",
        "venue": "IEEE Intelligent Vehicles Symposium (IV), 1779–1786 (2025)",
        "url": "https://doi.org/10.1109/IV64158.2025.11097630",
        "summary": "Infers T-junction layout from static 2D mmWave points, ray-traces dynamic multipath returns, and filters/clusters the unfolded points to localize multiple hidden pedestrians in measured outdoor experiments.",
        "cat": "latest modality radar rf mmwave automotive localization ray-tracing measured",
    },
    {
        "key": "yuBiScalarAA2025",
        "title": "BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar",
        "year": 2025,
        "authors": "Yu et al.",
        "venue": "IEEE Smart World Congress (SWC), 886–893 (2025)",
        "url": "https://doi.org/10.1109/SWC65939.2025.00144",
        "summary": "Maps sparse mmWave point clouds to pseudo-images and applies an attentive amplification network for hidden-object detection and tracking in dynamic outdoor scenes, extending radar NLOS toward learned semantic perception.",
        "cat": "latest modality radar rf mmwave detection tracking learning attention",
    },
    {
        "key": "yuTSANNLOS2025",
        "title": "Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar",
        "year": 2025,
        "authors": "Yu et al.",
        "venue": "Computer Engineering, online first 9 September 2025",
        "url": "https://doi.org/10.19678/j.issn.1000-3428.0252481",
        "summary": "Uses a two-stage attention architecture on radar pseudo-images for real-time hidden-target detection and tracking, reporting 75.62% mAP and a 5.99-point improvement over the compared baseline.",
        "cat": "latest modality radar rf mmwave detection tracking learning attention",
    },
    {
        "key": "yueCornerRadar2022",
        "title": "CornerRadar: RF-Based Indoor Localization Around Corners",
        "year": 2022,
        "authors": "Yue et al.",
        "venue": "PACM IMWUT 6(1), Article 34 (2022)",
        "url": "https://doi.org/10.1145/3517226",
        "summary": "Introduces a learned RF hint-map representation that captures practical indoor multipath and localizes people around corners across 56 environments, reducing median error by 3–12× versus prior RF baselines.",
        "cat": "latest modality radar rf localization indoor around-corner learning milestone",
    },
    {
        "key": "woodfordMosaic2022",
        "title": "Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar",
        "year": 2022,
        "authors": "Woodford et al.",
        "venue": "ACM MobiSys, 155–167 (2022)",
        "url": "https://doi.org/10.1145/3498361.3538944",
        "summary": "Uses multiple curved and planar environmental reflectors to enlarge around-corner automotive-radar coverage, more than doubling hidden-vehicle detection probability at three real urban sites.",
        "cat": "latest modality radar rf mmwave automotive reflectors around-corner milestone",
    },
    {
        "key": "doddsRFlect2024",
        "title": "Around the Corner mmWave Imaging in Practical Environments",
        "year": 2024,
        "authors": "Dodds et al.",
        "venue": "ACM MobiCom, 953–967 (2024)",
        "url": "https://doi.org/10.1145/3636534.3690671",
        "summary": "RFlect exploits practical environmental reflectors, including poles and curved/composite surfaces, to reconstruct hidden object shape beyond the planar-wall assumptions of earlier around-corner radar systems.",
        "cat": "latest modality radar rf mmwave imaging reconstruction reflectors practical milestone",
    },
    {
        "key": "doddsMmNorm2025",
        "title": "Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation",
        "year": 2025,
        "authors": "Dodds et al.",
        "venue": "ACM MobiSys, 445–458 (2025)",
        "url": "https://doi.org/10.1145/3711875.3729138",
        "summary": "mmNorm estimates surface-normal fields from mmWave observations and integrates them into hidden-object geometry, moving RF NLOS from localization and coarse reflectivity toward full 3D shape reconstruction.",
        "cat": "latest modality radar rf mmwave 3d reconstruction surface-normal geometry milestone",
    },
    {
        "key": "doddsWaveFormer2026",
        "title": "Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion",
        "year": 2026,
        "authors": "Dodds et al.",
        "venue": "CVPR, 21713–21724 (2026)",
        "url": "https://openaccess.thecvf.com/content/CVPR2026/html/Dodds_Wave-Former_Through-Occlusion_3D_Reconstruction_via_Wireless_Shape_Completion_CVPR_2026_paper.html",
        "summary": "A physics-aware transformer bridges raw mmWave sensing with wireless shape completion, using candidate surfaces, learned completion, and entropy-guided selection to recover complete 3D geometry of fully occluded everyday objects.",
        "cat": "latest modality radar rf mmwave 3d reconstruction transformer shape-completion learning cvpr",
    },
    {
        "key": "zhouRISE2026",
        "title": "RISE: Single Static Radar-based Indoor Scene Understanding",
        "year": 2026,
        "authors": "Zhou et al.",
        "venue": "CVPR, 32194–32205 (2026)",
        "url": "https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_RISE_Single_Static_Radar-based_Indoor_Scene_Understanding_CVPR_2026_paper.html",
        "summary": "Uses AoA/AoD multipath enhancement plus sim-to-real hierarchical diffusion for layout reconstruction and object detection from one static radar, establishing a large-scale benchmark for radar-only indoor scene understanding.",
        "cat": "latest modality radar rf mmwave scene-understanding layout object-detection diffusion cvpr",
    },
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {n}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, repl, label: str, flags=0) -> str:
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f"{label}: expected one regex match, found {n}")
    return out


# README --------------------------------------------------------------------
readme = read("README.md")
for p in PAPERS:
    if p["title"] in readme:
        raise RuntimeError(f"README already contains {p['title']}")
readme = replace_once(readme, "**Update run: 6 August 2026.**", "**Update run: 8 August 2026.**", "README update date")
header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
rows = "".join(
    f"| {p['year']} | [{p['title']}]({p['url']}) — {p['authors']} | {p['venue']} | {p['summary']} |\n"
    for p in PAPERS
)
readme = replace_once(readme, header, header + rows, "README latest table")

timeline_add = {
    2022: "    2022 ── CornerRadar: learned RF hint maps enable robust indoor around-corner localization across diverse layouts [PACM IMWUT]\n       │     Mosaic: diverse curved and planar urban reflectors broaden automotive around-corner radar coverage [MobiSys]\n",
    2024: "    2024 ── RFlect: practical poles and curved/composite reflectors support hidden-shape mmWave imaging beyond planar-wall assumptions [MobiCom]\n",
    2025: "    2025 ── mmNorm: mmWave surface-normal estimation advances hidden RF sensing from localization to 3D object geometry [MobiSys]\n       │     Jeon et al.: ray-traced 2D mmWave point clouds localize multiple hidden pedestrians at measured outdoor T-junctions [IEEE IV]\n       │     Zhai et al.: second-order edge diffraction plus block sparse Bayesian learning localizes hidden acoustic sources without direct/first-order paths [Applied Acoustics]\n       │     BiScalar-AA and TSAN: attention-based radar pseudo-image models extend NLOS toward learned object detection and tracking [IEEE SWC / Computer Engineering]\n",
    2026: "    2026 ── Wave-Former: physics-aware wireless shape completion reconstructs complete 3D geometry of fully occluded objects [CVPR]\n       │     RISE: AoA/AoD multipath enhancement and hierarchical diffusion enable layout reconstruction and object detection from one static radar [CVPR]\n",
}
for year, block in timeline_add.items():
    pattern = rf"(?m)^    {year} ── .+$"
    m = re.search(pattern, readme)
    if not m:
        raise RuntimeError(f"README timeline anchor missing for {year}")
    readme = readme[:m.start()] + block + readme[m.start():]

# Final-venue/link corrections that were already known but still stale on public master.
readme = regex_once(
    readme,
    r"\[Dual-branch Graph Feature Learning for NLOS Imaging\]\([^)]*\) — Su et al\. \| arXiv 2025 \|",
    "[Dual-branch Graph Feature Learning for NLOS Imaging](https://doi.org/10.1609/aaai.v39i7.32757) — Su et al. | AAAI 2025, 39(7), 7051–7059 |",
    "README DG-NLOS final venue",
)
readme = regex_once(
    readme,
    r"\[Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR\]\([^)]*\) — Young et al\. \| arXiv 2024 \|",
    "[Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR](https://doi.org/10.1109/ICRA55743.2025.11128292) — Young et al. | IEEE ICRA 2025, 4907–4914 |",
    "README autonomous navigation final venue",
)
readme = regex_once(
    readme,
    r"\[NLOS-NeuS: Non-line-of-sight Neural Implicit Surface\]\([^)]*\) — Fujimura et al\. \| ICCV 2023 \|",
    "[NLOS-NeuS: Non-line-of-sight Neural Implicit Surface](https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html) — Fujimura et al. | ICCV 2023, 10532–10541 |",
    "README NLOS-NeuS final page",
)
# TransiT can appear in a table with either arXiv or ICCV text; normalize when present.
readme, n_transit = re.subn(
    r"\[TransiT: Transient Transformer for Non-line-of-sight Videography\]\([^)]*\) — Li et al\. \| (?:arXiv 2025|ICCV 2025(?:, 27542–27551)?) \|",
    "[TransiT: Transient Transformer for Non-line-of-sight Videography](https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html) — Li et al. | ICCV 2025, 27542–27551 |",
    readme,
    count=1,
)
if n_transit != 1:
    raise RuntimeError(f"README TransiT normalization: expected one match, found {n_transit}")
write("README.md", readme)


# Website -------------------------------------------------------------------
html = read("index.html")
for p in PAPERS:
    if p["title"] in html:
        raise RuntimeError(f"index already contains {p['title']}")
html = replace_once(html, "Updated 6 August 2026 · 210+ papers", "Updated 8 August 2026 · 210+ papers", "website date")
records = "".join(
    '      {cat:"%s",title:"%s",authors:"%s",year:%d,venue:"%s",url:"%s",key:"%s"},\n'
    % (p["cat"], p["title"].replace('"','\\"'), p["authors"], p["year"], p["venue"].replace('"','\\"'), p["url"], p["summary"].replace('"','\\"'))
    for p in PAPERS
)
html = replace_once(html, "    const papers=[\n", "    const papers=[\n" + records, "website papers array")
actual = html.count("{cat:")
html = regex_once(
    html,
    r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
    f'<div class="stat"><b>{actual}</b><span>tracked latest entries</span></div>',
    "website paper counter",
)
web_timeline = {
    2022: " CornerRadar introduced learned RF hint maps for practical indoor around-corner localization, while Mosaic exploited diverse curved and planar reflectors to expand automotive radar coverage.",
    2024: " RFlect generalized practical mmWave hidden-shape imaging to poles and curved/composite environmental reflectors.",
    2025: " mmNorm recovered hidden 3D geometry from mmWave surface normals; Jeon et al. demonstrated ray-traced multi-pedestrian localization at outdoor T-junctions; second-order acoustic edge diffraction supported sparse-Bayesian hidden-source localization; and BiScalar-AA/TSAN expanded learned mmWave detection and tracking.",
    2026: " Wave-Former introduced physics-aware wireless shape completion for fully occluded 3D objects, while RISE used single-static-radar multipath and hierarchical diffusion for layout reconstruction and object detection.",
}
for year, sentence in web_timeline.items():
    pat = re.compile(rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
    m = pat.search(html)
    if not m:
        raise RuntimeError(f"website timeline anchor missing for {year}")
    html = html[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + html[m.end():]
# Normalize stale public explorer records when present.
def norm_record(title, url, venue):
    global html
    pat = re.compile(r'(\{cat:"[^"]*",title:"' + re.escape(title) + r'",authors:"[^"]*",year:\d+,venue:")[^"]*(",url:")[^"]*(",key:)')
    m = pat.search(html)
    if not m:
        raise RuntimeError(f"website record missing for final-venue normalization: {title}")
    html = html[:m.start()] + m.group(1) + venue + m.group(2) + url + m.group(3) + html[m.end():]

norm_record("Dual-branch Graph Feature Learning for NLOS Imaging", "https://doi.org/10.1609/aaai.v39i7.32757", "AAAI 2025, 39(7), 7051–7059")
norm_record("Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR", "https://doi.org/10.1109/ICRA55743.2025.11128292", "IEEE ICRA 2025, 4907–4914")
norm_record("NLOS-NeuS: Non-line-of-sight Neural Implicit Surface", "https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html", "ICCV 2023, 10532–10541")
norm_record("TransiT: Transient Transformer for Non-line-of-sight Videography", "https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html", "ICCV 2025, 27542–27551")
write("index.html", html)


# Survey --------------------------------------------------------------------
article = read("article/5newscenes.tex")
for p in PAPERS:
    if p["key"] in article:
        raise RuntimeError(f"survey already contains citation key {p['key']}")
radar_anchor = "The radar approach is complementary to optical NLOS: it operates through walls and in total darkness, but at lower spatial resolution than optical methods.\n\n"
radar_para = (
    "A parallel RF/mmWave lineage has progressively broadened the task from around-corner localization to practical hidden-shape and full-scene reconstruction. "
    "CornerRadar learned a propagation hint map for robust indoor localization across diverse layouts~\\cite{yueCornerRadar2022}, while Mosaic exploited curved and planar urban reflectors to widen automotive-radar blind-spot coverage~\\cite{woodfordMosaic2022}. "
    "RFlect then used practical environmental reflectors, including poles and curved/composite surfaces, for around-corner shape imaging~\\cite{doddsRFlect2024}. "
    "The geometry branch advanced with mmNorm, which estimates mmWave surface normals and integrates them into hidden 3D shape~\\cite{doddsMmNorm2025}, and with Jeon~\\etal, who infer T-junction layout from static radar points and ray-trace dynamic multipath to localize multiple hidden pedestrians in measured outdoor scenes~\\cite{jeonTJunctionMmWaveNLOS2025}. "
    "Attention-based BiScalar-AA and its related two-stage attention network convert sparse radar points to pseudo-images for learned NLOS object detection and tracking~\\cite{yuBiScalarAA2025,yuTSANNLOS2025}. "
    "Most recently, Wave-Former introduced physics-aware wireless shape completion for complete 3D geometry of fully occluded objects~\\cite{doddsWaveFormer2026}, whereas RISE combines AoA/AoD multipath enhancement with hierarchical diffusion for layout reconstruction and object detection from a single static radar~\\cite{zhouRISE2026}. "
    "Together, these works show a clear RF trajectory from point localization, through reflector-aware imaging and surface-normal recovery, to learned full-object and scene-level geometry.\n\n"
)
article = replace_once(article, radar_anchor, radar_anchor + radar_para, "survey radar insertion")
acoustic_anchor = "Together, these systems extend the acoustic trajectory beyond relay-wall tomography toward passive tracking and diffraction-aware source localization in practical occluded environments.\n\n"
acoustic_para = (
    "A complementary second-order regime arises when both the direct path and first-order diffraction are unavailable. Zhai~\\etal~construct a Biot--Tolstoy--Medwin second-order edge-diffraction transfer model and use it as the sensing matrix of a block-sparse inverse problem~\\cite{zhaiSecondOrderAcousticNLOS2025}. Fast marginalized block sparse Bayesian learning then estimates hidden-source position and strength; simulations and a 32-channel array experiment show that higher-order diffraction, usually treated as a weak residual, can become the primary sensing path under stronger occlusion.\n\n"
)
article = replace_once(article, acoustic_anchor, acoustic_anchor + acoustic_para, "survey acoustic insertion")
write("article/5newscenes.tex", article)

tex = read("bare_jrnl.tex")
tex = "% 8 August 2026 forward-citation trace: RF/mmWave milestone lineage, second-order acoustic diffraction, and four final-venue corrections synchronized.\n" + tex
write("bare_jrnl.tex", tex)


# Bibliography ---------------------------------------------------------------
bib = read("egbib_merged_20260711.bib")
for p in PAPERS:
    if re.search(r"@[A-Za-z]+\s*\{\s*" + re.escape(p["key"]) + r"\s*,", bib):
        raise RuntimeError(f"bibliography already contains {p['key']}")
entries = r'''

@article{zhaiSecondOrderAcousticNLOS2025,
  author = {Zhai, Qingbo and Ning, Fangli and Wei, Juan and Su, Zhaojing},
  title = {Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction},
  journal = {Applied Acoustics},
  volume = {228},
  pages = {110369},
  year = {2025},
  doi = {10.1016/j.apacoust.2024.110369},
  url = {https://doi.org/10.1016/j.apacoust.2024.110369}
}

@inproceedings{jeonTJunctionMmWaveNLOS2025,
  author = {Jeon, Mingu and Park, Byeonggyu and Kim, Hee Yeun and Kang, Yujeong and Choi, Byonghyok and Cho, Hansang and Kim, Byungkwan and Lee, Soomok and Seo, Seung Woo and Kim, Seong Woo},
  title = {Non-Line-of-Sight Multi-Target Localization in {T}-Junctions Using Ray Tracing of mmWave Radar},
  booktitle = {2025 IEEE Intelligent Vehicles Symposium (IV)},
  pages = {1779--1786},
  year = {2025},
  publisher = {IEEE},
  doi = {10.1109/IV64158.2025.11097630},
  url = {https://doi.org/10.1109/IV64158.2025.11097630}
}

@inproceedings{yuBiScalarAA2025,
  author = {Yu, Yang and Hu, Shijie and Abdul Wahid, Junaid and Zhang, Han and Lv, Qiujie and Hu, Yazhou},
  title = {BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar},
  booktitle = {2025 IEEE Smart World Congress (SWC)},
  pages = {886--893},
  year = {2025},
  publisher = {IEEE},
  doi = {10.1109/SWC65939.2025.00144},
  url = {https://doi.org/10.1109/SWC65939.2025.00144}
}

@article{yuTSANNLOS2025,
  author = {Yu, Yang and Hu, Shijie and Fan, Kangkang and Guo, Wei and Hu, Yazhou and Zhang, Dawei},
  title = {Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar},
  journal = {Computer Engineering},
  year = {2025},
  doi = {10.19678/j.issn.1000-3428.0252481},
  url = {https://doi.org/10.19678/j.issn.1000-3428.0252481},
  note = {Online first, published 9 September 2025}
}

@article{yueCornerRadar2022,
  author = {Yue, Shichao and He, Hao and Cao, Peng and Zha, Kaiwen and Koizumi, Masayuki and Katabi, Dina},
  title = {CornerRadar: RF-Based Indoor Localization Around Corners},
  journal = {Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies},
  volume = {6},
  number = {1},
  pages = {34:1--34:24},
  year = {2022},
  publisher = {ACM},
  doi = {10.1145/3517226},
  url = {https://doi.org/10.1145/3517226}
}

@inproceedings{woodfordMosaic2022,
  author = {Woodford, Timothy and Zhang, Xinyu and Chai, Eugene and Sundaresan, Karthikeyan},
  title = {Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar},
  booktitle = {Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services (MobiSys)},
  pages = {155--167},
  year = {2022},
  publisher = {ACM},
  doi = {10.1145/3498361.3538944},
  url = {https://doi.org/10.1145/3498361.3538944}
}

@inproceedings{doddsRFlect2024,
  author = {Dodds, Laura and Shanbhag, Hailan and Guan, Junfeng and Gupta, Saurabh and Hassanieh, Haitham},
  title = {Around the Corner mmWave Imaging in Practical Environments},
  booktitle = {Proceedings of the 30th Annual International Conference on Mobile Computing and Networking (MobiCom)},
  pages = {953--967},
  year = {2024},
  publisher = {ACM},
  doi = {10.1145/3636534.3690671},
  url = {https://doi.org/10.1145/3636534.3690671}
}

@inproceedings{doddsMmNorm2025,
  author = {Dodds, Laura and Boroushaki, Tara and Zhou, Kaichen and Adib, Fadel},
  title = {Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation},
  booktitle = {Proceedings of the 23rd Annual International Conference on Mobile Systems, Applications and Services (MobiSys)},
  pages = {445--458},
  year = {2025},
  publisher = {ACM},
  doi = {10.1145/3711875.3729138},
  url = {https://doi.org/10.1145/3711875.3729138}
}

@inproceedings{doddsWaveFormer2026,
  author = {Dodds, Laura and Lam, Maisy and Akbar, Waleed and Cheng, Yibo and Adib, Fadel},
  title = {Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {21713--21724},
  year = {2026},
  url = {https://openaccess.thecvf.com/content/CVPR2026/html/Dodds_Wave-Former_Through-Occlusion_3D_Reconstruction_via_Wireless_Shape_Completion_CVPR_2026_paper.html}
}

@inproceedings{zhouRISE2026,
  author = {Zhou, Kaichen and Dodds, Laura and Afzal, Sayed Saad and Adib, Fadel},
  title = {{RISE}: Single Static Radar-based Indoor Scene Understanding},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {32194--32205},
  year = {2026},
  url = {https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_RISE_Single_Static_Radar-based_Indoor_Scene_Understanding_CVPR_2026_paper.html}
}
'''
bib = bib.rstrip() + entries + "\n"

# Normalize already-integrated works to their final venues where stale arXiv-only metadata is still present.
def replace_bib_entry_by_title(text, title_pattern, replacement, label):
    pat = re.compile(r"@[A-Za-z]+\s*\{[^,]+,\n(?:(?!\n\}).)*?title\s*=\s*\{" + title_pattern + r"\}.*?\n\}", re.S | re.I)
    out, n = pat.subn(replacement.strip(), text, count=1)
    if n != 1:
        raise RuntimeError(f"{label}: expected one bibliography entry, found {n}")
    return out

# Preserve whatever citation keys are already used by extracting them first.
def normalized_entry(text, title_literal, body_builder, label):
    pat = re.compile(r"@([A-Za-z]+)\s*\{([^,]+),\n(?:(?!\n\}).)*?title\s*=\s*\{[^\n]*" + re.escape(title_literal) + r"[^\n]*\}.*?\n\}", re.S | re.I)
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"{label}: bibliography entry not found")
    replacement = body_builder(m.group(2))
    return text[:m.start()] + replacement.strip() + text[m.end():]

bib = normalized_entry(bib, "Dual-branch Graph Feature Learning for NLOS Imaging", lambda k: f'''@inproceedings{{{k},
  author = {{Su, Xiongfei and Zhu, Tianyi and Liu, Lina and Chen, Zheng and Zhang, Yulun and Li, Siyuan and Ye, Juntian and Xu, Feihu and Yuan, Xin}},
  title = {{Dual-branch Graph Feature Learning for NLOS Imaging}},
  booktitle = {{Proceedings of the AAAI Conference on Artificial Intelligence}},
  volume = {{39}},
  number = {{7}},
  pages = {{7051--7059}},
  year = {{2025}},
  doi = {{10.1609/aaai.v39i7.32757}},
  url = {{https://doi.org/10.1609/aaai.v39i7.32757}}
}}''', "DG-NLOS final bibliography")

bib = normalized_entry(bib, "Enhancing Autonomous Navigation by Imaging Hidden Objects", lambda k: f'''@inproceedings{{{k},
  author = {{Young, Aaron and Batagoda, Nevindu M. and Zhang, Harry and Dave, Akshat and Pediredla, Adithya and Negrut, Dan and Raskar, Ramesh}},
  title = {{Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR}},
  booktitle = {{2025 IEEE International Conference on Robotics and Automation (ICRA)}},
  pages = {{4907--4914}},
  year = {{2025}},
  publisher = {{IEEE}},
  doi = {{10.1109/ICRA55743.2025.11128292}},
  url = {{https://doi.org/10.1109/ICRA55743.2025.11128292}}
}}''', "ICRA navigation final bibliography")

bib = normalized_entry(bib, "NLOS-NeuS: Non-line-of-sight Neural Implicit Surface", lambda k: f'''@inproceedings{{{k},
  author = {{Fujimura, Yuki and Kushida, Takahiro and Funatomi, Takuya and Mukaigawa, Yasuhiro}},
  title = {{NLOS-NeuS: Non-line-of-sight Neural Implicit Surface}},
  booktitle = {{Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}},
  pages = {{10532--10541}},
  year = {{2023}},
  doi = {{10.1109/ICCV51070.2023.00966}},
  url = {{https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html}}
}}''', "NLOS-NeuS final bibliography")

bib = normalized_entry(bib, "TransiT: Transient Transformer for Non-line-of-sight Videography", lambda k: f'''@inproceedings{{{k},
  author = {{Li, Ruiqian and Shen, Siyuan and Xia, Suan and Wang, Ziheng and Peng, Xingyue and Song, Chengxuan and Zhu, Yingsheng and Wu, Tao and Li, Shiying and Yu, Jingyi}},
  title = {{TransiT: Transient Transformer for Non-line-of-sight Videography}},
  booktitle = {{Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}},
  pages = {{27542--27551}},
  year = {{2025}},
  url = {{https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html}}
}}''', "TransiT final bibliography")
write("egbib_merged_20260711.bib", bib)

note = ROOT / "updates/2026-08-08-forward-citation-rf-acoustic-integration.md"
if note.exists():
    raise RuntimeError("update note already exists")
note.write_text("""# Forward-citation and modality audit — 8 August 2026

This integration closes a verified gap in the RF/mmWave and diffraction-acoustic NLOS lineage. Ten genuinely NLOS or tightly adjacent sensing/reconstruction papers were checked against the public README, website explorer, survey source, and merged bibliography before insertion. The added sequence spans CornerRadar and Mosaic (2022), RFlect (2024), mmNorm and measured T-junction / attention-based radar perception plus second-order acoustic localization (2025), and Wave-Former / RISE (CVPR 2026).

The same run also normalizes four previously known final-venue records: DG-NLOS to AAAI 2025, single-photon-LiDAR autonomous navigation to ICRA 2025, TransiT to ICCV 2025, and NLOS-NeuS to ICCV 2023. The LaTeX build workflow validates that every new citation resolves and that the regenerated PDF contains the new literature-review text.

No direct NLOS-imaging publication newer than the 22 July 2026 Nature Communications TLTM-iteration paper was verified in this search pass.
""", encoding="utf-8")

print("Applied guarded 8 August forward-citation integration.")
