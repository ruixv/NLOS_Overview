from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

NEW = [
    ("zhaiSecondOrderAcousticNLOS2025", "Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction"),
    ("jeonRayTracingMmWaveNLOS2025", "Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar"),
    ("yuBiScalarAA2025", "BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar"),
    ("yuTSANNLOS2025", "Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar"),
    ("yueCornerRadar2022", "CornerRadar: RF-Based Indoor Localization Around Corners"),
    ("woodfordMosaic2022", "Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar"),
    ("doddsRFlect2024", "Around the Corner mmWave Imaging in Practical Environments"),
    ("doddsMmNorm2025", "Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation"),
    ("doddsWaveFormer2026", "Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion"),
    ("zhouRISE2026", "RISE: Single Static Radar-based Indoor Scene Understanding"),
    ("sambasivanRendererBounds2026", "A Renderer-Enabled Framework for Computing Parameter Estimation Lower Bounds in Plenoptic Imaging Systems"),
]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {n}")
    return text.replace(old, new, 1)


def replace_html_record(text, title, new_line):
    pattern = re.compile(r'^\s*\{cat:.*?title:"' + re.escape(title) + r'".*?\},\s*$', re.M)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"website record {title!r}: expected one match, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + new_line + text[m.end():]


def replace_bib_key(text, key, entry):
    pattern = re.compile(r'^@\w+\s*\{\s*' + re.escape(key) + r'\s*,.*?^\}\s*$', re.M | re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"BibTeX key {key!r}: expected one entry, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + entry.rstrip() + text[m.end():]


def append_readme_year(text, year, lines):
    pattern = re.compile(rf'^{year} ──.*$', re.M)
    m = pattern.search(text)
    if not m:
        raise RuntimeError(f"README timeline year {year} not found")
    return text[:m.end()] + "\n" + lines.rstrip("\n") + text[m.end():]


def append_html_year(text, year, sentence):
    pattern = re.compile(r'(<div class="tl"><div class="year">' + str(year) + r'</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"website timeline year {year}: expected one block, found {len(matches)}")
    m = matches[0]
    return text[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + text[m.end():]


# ---------------------------------------------------------------------------
# README: new records, historical placement, and four final-venue corrections.
# ---------------------------------------------------------------------------
readme = read("README.md")
for _, title in NEW:
    if title in readme:
        raise RuntimeError(f"README already contains new title: {title}")
readme = replace_once(readme, "**Update run: 6 August 2026.**", "**Update run: 7 August 2026.**", "README update date")
header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
rows = """| 2026 | [Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion](https://openaccess.thecvf.com/content/CVPR2026/html/Dodds_Wave-Former_Through-Occlusion_3D_Reconstruction_via_Wireless_Shape_Completion_CVPR_2026_paper.html) — Dodds et al. | CVPR 2026, 21713–21724 | Physics-aware wireless shape completion converts sparse mmWave surface evidence into complete 3D geometry of fully occluded everyday objects, extending radar NLOS from localization and partial surfaces toward full-shape reconstruction. |
| 2026 | [RISE: Single Static Radar-based Indoor Scene Understanding](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_RISE_Single_Static_Radar-based_Indoor_Scene_Understanding_CVPR_2026_paper.html) — Zhou et al. | CVPR 2026, 32194–32205 | Exploits AoA/AoD multipath from one static radar and a sim-to-real hierarchical diffusion model to reconstruct room layout and detect objects, treating ghost reflections as geometric evidence. |
| 2026 | [A Renderer-Enabled Framework for Computing Parameter Estimation Lower Bounds in Plenoptic Imaging Systems](https://arxiv.org/abs/2602.00215) — Sambasivan et al. | arXiv 2026 | Adjacent theory: uses renderer-defined passive indirect/NLOS forward models to compute Hammersley–Chapman–Robbins estimation-error lower bounds, providing a principled way to assess when hidden-parameter recovery is information limited. |
| 2025 | [Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation](https://doi.org/10.1145/3711875.3729138) — Dodds et al. | ACM MobiSys 2025, 445–458 | mmNorm estimates a hidden object's mmWave surface-normal field and integrates it into 3D isosurfaces, moving RF NLOS beyond point localization toward measured object geometry. |
| 2025 | [Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar](https://doi.org/10.1109/IV64158.2025.11097630) — Jeon et al. | IEEE IV 2025, 1779–1786 | Infers T-junction layout from static radar returns and ray-traces dynamic multipath to localize multiple hidden pedestrians in measured outdoor data. |
| 2025 | [BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar](https://doi.org/10.1109/SWC65939.2025.00144) — Yu et al. | IEEE Smart World Congress 2025, 886–893 | Converts sparse mmWave point clouds to pseudo-images and applies attentive amplification for hidden-object detection and tracking in dynamic scenes. |
| 2025 | [Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar](https://doi.org/10.19678/j.issn.1000-3428.0252481) — Yu et al. | Computer Engineering, online first 2025 | A related two-stage attention architecture strengthens weak multipath features for mmWave NLOS object detection and tracking; kept cross-referenced with BiScalar-AA rather than treated as an unrelated lineage. |
| 2025 | [Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction](https://doi.org/10.1016/j.apacoust.2024.110369) — Zhai et al. | Applied Acoustics 228, 110369 (2025) | Builds a Biot–Tolstoy–Medwin second-order diffraction sensing matrix and solves a block-sparse Bayesian inverse problem, localizing hidden sources even when direct and first-order paths are unavailable. |
| 2024 | [Around the Corner mmWave Imaging in Practical Environments](https://doi.org/10.1145/3636534.3690671) — Dodds et al. | ACM MobiCom 2024, 953–967 | RFlect models poles, concave surfaces, and composite reflectors to reconstruct hidden object shape in practical environments, relaxing the flat-wall assumption of earlier around-corner radar systems. |
| 2022 | [CornerRadar: RF-Based Indoor Localization Around Corners](https://doi.org/10.1145/3517226) — Yue et al. | Proc. ACM IMWUT 6(1), Article 34 (2022) | A foundational RF around-corner localization system that learns propagation cues across varied indoor layouts and turns multipath into hidden-person position evidence. |
| 2022 | [Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar](https://doi.org/10.1145/3498361.3538944) — Woodford et al. | ACM MobiSys 2022, 155–167 | Exploits multiple curved and planar environmental reflectors to broaden automotive radar's NLOS coverage, establishing reflector geometry as a first-class design variable. |
"""
readme = replace_once(readme, header, header + rows, "README latest-additions header")

readme = replace_once(
    readme,
    "| 2025 | [Dual-branch Graph Feature Learning for NLOS Imaging](https://arxiv.org/abs/2502.19683) — Su et al. | arXiv 2025 | DG-NLOS uses graph feature learning with separate albedo and depth branches to reduce 3D-grid cost while jointly reconstructing hidden appearance and geometry. |",
    "| 2025 | [Dual-branch Graph Feature Learning for NLOS Imaging](https://doi.org/10.1609/aaai.v39i7.32757) — Su et al. | AAAI 2025, 39(7), 7051–7059 | DG-NLOS converts dense transient voxels into sparse graph features and separates albedo/depth reconstruction, reducing volumetric cost while jointly recovering hidden appearance and geometry. |",
    "README DG-NLOS final venue",
)
readme = replace_once(
    readme,
    "| 2024 | [Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR](https://arxiv.org/abs/2410.03555) — Young et al. | arXiv 2024 | Uses SPAD / single-photon LiDAR NLOS occupancy perception to guide robot navigation around occluded corners. |",
    "| 2025 | [Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR](https://doi.org/10.1109/ICRA55743.2025.11128292) — Young et al. | IEEE ICRA 2025, 4907–4914 | Integrates SPAD-based multi-bounce sensing, learned hidden-space occupancy estimation, and robot control; real L-shaped-corridor experiments demonstrate NLOS-assisted autonomous navigation. |",
    "README Young final venue",
)
readme = replace_once(
    readme,
    "| 2025 | [TransiT: Transient Transformer for Non-line-of-sight Videography](https://arxiv.org/abs/2503.11328) — Li et al. | ICCV 2025 |",
    "| 2025 | [TransiT: Transient Transformer for Non-line-of-sight Videography](https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html) — Li et al. | ICCV 2025, 27542–27551 |",
    "README TransiT final record",
)
readme = replace_once(
    readme,
    "| 2023 | [NLOS-NeuS: Non-line-of-sight Neural Implicit Surface](https://arxiv.org/abs/2303.12280) — Fujimura et al. | ICCV 2023 |",
    "| 2023 | [NLOS-NeuS: Non-line-of-sight Neural Implicit Surface](https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html) — Fujimura et al. | ICCV 2023, 10532–10541 |",
    "README NLOS-NeuS final record",
)
readme = append_readme_year(readme, 2022, "   │     CornerRadar learns indoor RF multipath cues for hidden-person localization around corners [IMWUT]\n   │     Mosaic exploits curved and multiple environmental reflectors for broader automotive around-corner radar coverage [MobiSys]")
readme = append_readme_year(readme, 2024, "   │     RFlect reconstructs hidden shape with poles, concave surfaces, and composite reflectors in practical mmWave environments [MobiCom]")
readme = append_readme_year(readme, 2025, "   │     Zhai et al.: second-order edge diffraction plus block-sparse Bayesian inversion localizes hidden acoustic sources when stronger paths vanish [Applied Acoustics]\n   │     mmNorm estimates mmWave surface normals for hidden-object 3D reconstruction; Jeon et al. add measured multi-target T-junction localization; BiScalar-AA/TSAN extend learned detection and tracking [MobiSys / IEEE IV / SWC / Computer Engineering]")
readme = append_readme_year(readme, 2026, "   │     Wave-Former completes full hidden 3D shapes from wireless evidence, while RISE turns single-static-radar multipath into room-layout reconstruction and object detection [CVPR]\n   │     Sambasivan et al. use renderer-defined indirect-imaging models to compute parameter-estimation lower bounds [arXiv; adjacent theory]")
write("README.md", readme)


# ---------------------------------------------------------------------------
# Website: searchable records, timeline, date, and self-consistent counter.
# ---------------------------------------------------------------------------
html = read("index.html")
for _, title in NEW:
    if title in html:
        raise RuntimeError(f"index.html already contains new title: {title}")
html = replace_once(html, "Updated 6 August 2026 · 210+ papers", "Updated 7 August 2026 · 210+ papers", "website update date")
records_anchor = "    const papers=[\n"
records = """      {cat:"latest modality radar rf mmwave learning reconstruction cvpr",title:"Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion",authors:"Laura Dodds et al.",year:2026,venue:"CVPR 2026, 21713–21724",url:"https://openaccess.thecvf.com/content/CVPR2026/html/Dodds_Wave-Former_Through-Occlusion_3D_Reconstruction_via_Wireless_Shape_Completion_CVPR_2026_paper.html",key:"Physics-aware wireless shape completion turns sparse mmWave surface proposals into complete 3D geometry of fully occluded objects."},
      {cat:"latest modality radar rf mmwave learning scene-understanding cvpr",title:"RISE: Single Static Radar-based Indoor Scene Understanding",authors:"Kaichen Zhou et al.",year:2026,venue:"CVPR 2026, 32194–32205",url:"https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_RISE_Single_Static_Radar-based_Indoor_Scene_Understanding_CVPR_2026_paper.html",key:"Uses AoA/AoD multipath enhancement and hierarchical diffusion to reconstruct indoor layout and detect objects from one static radar."},
      {cat:"latest theory passive bounds renderer adjacent",title:"A Renderer-Enabled Framework for Computing Parameter Estimation Lower Bounds in Plenoptic Imaging Systems",authors:"Sambasivan et al.",year:2026,venue:"arXiv 2026",url:"https://arxiv.org/abs/2602.00215",key:"Adjacent theory for passive indirect/NLOS imaging: renderer-defined forward models enable Hammersley–Chapman–Robbins parameter-estimation lower bounds."},
      {cat:"latest modality radar rf mmwave reconstruction mobisys",title:"Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation",authors:"Laura Dodds et al.",year:2025,venue:"ACM MobiSys 2025, 445–458",url:"https://doi.org/10.1145/3711875.3729138",key:"mmNorm estimates mmWave surface-normal fields and integrates them into hidden-object 3D isosurfaces."},
      {cat:"latest modality radar rf mmwave automotive localization measured",title:"Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar",authors:"Mingu Jeon et al.",year:2025,venue:"IEEE IV 2025, 1779–1786",url:"https://doi.org/10.1109/IV64158.2025.11097630",key:"Infers a T-junction layout from static radar returns and unfolds dynamic multipath by ray tracing for measured multi-pedestrian localization."},
      {cat:"latest modality radar rf mmwave learning detection tracking",title:"BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar",authors:"Yang Yu et al.",year:2025,venue:"IEEE Smart World Congress 2025, 886–893",url:"https://doi.org/10.1109/SWC65939.2025.00144",key:"Attention-amplified pseudo-images from sparse mmWave point clouds support NLOS object detection and tracking in dynamic scenes."},
      {cat:"latest modality radar rf mmwave learning detection tracking",title:"Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar",authors:"Yang Yu et al.",year:2025,venue:"Computer Engineering, online first 2025",url:"https://doi.org/10.19678/j.issn.1000-3428.0252481",key:"Two-stage attention strengthens weak multipath features for hidden-object detection and tracking; a related continuation of the BiScalar-AA branch."},
      {cat:"latest modality acoustic localization diffraction sparse-bayesian measured",title:"Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction",authors:"Qingbo Zhai et al.",year:2025,venue:"Applied Acoustics 228, 110369",url:"https://doi.org/10.1016/j.apacoust.2024.110369",key:"Second-order Biot–Tolstoy–Medwin edge diffraction becomes a block-sparse sensing operator when direct and first-order acoustic paths are unavailable."},
      {cat:"latest modality radar rf mmwave imaging reflectors mobicom",title:"Around the Corner mmWave Imaging in Practical Environments",authors:"Laura Dodds et al.",year:2024,venue:"ACM MobiCom 2024, 953–967",url:"https://doi.org/10.1145/3636534.3690671",key:"RFlect models complex practical reflectors such as poles and concave surfaces to reconstruct hidden object shape."},
      {cat:"latest modality radar rf localization historical",title:"CornerRadar: RF-Based Indoor Localization Around Corners",authors:"Shichao Yue et al.",year:2022,venue:"Proc. ACM IMWUT 6(1), Article 34",url:"https://doi.org/10.1145/3517226",key:"Foundational RF around-corner localization that learns multipath propagation cues across varied indoor layouts."},
      {cat:"latest modality radar rf automotive reflectors historical",title:"Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar",authors:"Timothy Woodford et al.",year:2022,venue:"ACM MobiSys 2022, 155–167",url:"https://doi.org/10.1145/3498361.3538944",key:"Uses curved and multiple environmental reflectors to broaden automotive around-corner radar coverage beyond planar-wall assumptions."},
"""
html = replace_once(html, records_anchor, records_anchor + records, "website papers array")

html = replace_html_record(html, "Dual-branch Graph Feature Learning for NLOS Imaging", '      {cat:"latest learning",title:"Dual-branch Graph Feature Learning for NLOS Imaging",authors:"Su et al.",year:2025,venue:"AAAI 2025, 39(7), 7051–7059",url:"https://doi.org/10.1609/aaai.v39i7.32757",key:"DG-NLOS converts dense transient voxels into sparse graph features with separate albedo and depth branches for efficient hidden appearance/geometry recovery."},')
html = replace_html_record(html, "Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR", '      {cat:"latest modality active robotics",title:"Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR",authors:"Young et al.",year:2025,venue:"IEEE ICRA 2025, 4907–4914",url:"https://doi.org/10.1109/ICRA55743.2025.11128292",key:"SPAD multi-bounce sensing and learned hidden occupancy are coupled directly to autonomous robot control in real L-shaped corridors."},')
html = replace_html_record(html, "TransiT: Transient Transformer for Non-line-of-sight Videography", '      {cat:"latest learning active",title:"TransiT: Transient Transformer for Non-line-of-sight Videography",authors:"Ruiqian Li et al.",year:2025,venue:"ICCV 2025, 27542–27551",url:"https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html",key:"High-speed NLOS videography from sparse 16×16 transient scans with transformer fusion and transfer learning."},')
html = replace_html_record(html, "NLOS-NeuS: Non-line-of-sight Neural Implicit Surface", '      {cat:"latest learning active",title:"NLOS-NeuS: Non-line-of-sight Neural Implicit Surface",authors:"Fujimura et al.",year:2023,venue:"ICCV 2023, 10532–10541",url:"https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html",key:"SDF-based neural implicit surfaces for smooth, high-detail hidden-surface reconstruction."},')

html = append_html_year(html, 2022, " CornerRadar established learned RF localization around indoor corners, while Mosaic showed that diverse curved and planar environmental reflectors can substantially expand automotive NLOS radar coverage.")
html = append_html_year(html, 2024, " RFlect then generalized practical around-corner mmWave imaging to poles, concave surfaces, and composite reflectors while reconstructing hidden shape.")
html = append_html_year(html, 2025, " The RF branch expanded from localization to mmNorm surface-normal 3D reconstruction, measured multi-target T-junction ray tracing, and learned BiScalar-AA/TSAN detection and tracking; acoustic work likewise exploited second-order edge diffraction when stronger paths were absent.")
html = append_html_year(html, 2026, " Wave-Former completed full hidden 3D shapes from wireless evidence and RISE used single-static-radar multipath for indoor layout reconstruction and object detection; renderer-enabled estimation bounds added an adjacent information-theoretic view of passive indirect imaging.")
actual = html.count('{cat:')
if actual != 268:
    raise RuntimeError(f"Expected 268 website paper records after integration, found {actual}")
html, n = re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>', f'<div class="stat"><b>{actual}</b><span>tracked latest entries</span></div>', html, count=1)
if n != 1:
    raise RuntimeError("website tracked-entry counter not found exactly once")
write("index.html", html)


# ---------------------------------------------------------------------------
# Survey prose: semantic insertion in acoustic, RF/mmWave, renderer/theory.
# ---------------------------------------------------------------------------
article5 = read("article/5newscenes.tex")
for key, _ in NEW:
    if key in article5:
        raise RuntimeError(f"article/5newscenes.tex already contains new citation key {key}")

acoustic_anchor = "At the task level, Wang~\\etal~combine bird's-eye-view scene geometry with time--frequency and spatiotemporal acoustic spectra"
acoustic_para = (
    "Zhai~\\etal~extend this diffraction-aware branch to the harder regime in which both the direct path and first-order diffraction are unavailable~\\cite{zhaiSecondOrderAcousticNLOS2025}. "
    "They construct the sensing matrix from the Biot--Tolstoy--Medwin second-order edge-diffraction response and solve for source position and strength with fast marginalized block sparse Bayesian learning. "
    "The simulation and 32-channel microphone-array results show that higher-order acoustic transport, normally treated as a weak residual, can itself become the principal NLOS localization cue.\n\n"
)
article5 = replace_once(article5, acoustic_anchor, acoustic_para + acoustic_anchor, "acoustic second-order insertion")

radar_anchor = r"\noindent \textbf{Multipath-exploitation inverse scattering for RF NLOS.}"
radar_para = (
    "\\vspace{0.8mm}\n\\noindent \\textbf{From around-corner RF localization to hidden-shape reconstruction.}\n"
    "A parallel systems lineage progressively broadens both reflector geometry and reconstruction targets. CornerRadar~\\cite{yueCornerRadar2022} learned propagation cues for indoor RF localization around corners, while Mosaic~\\cite{woodfordMosaic2022} showed in automotive settings that curved and multiple environmental reflectors can provide coverage that planar-wall models miss. "
    "RFlect~\\cite{doddsRFlect2024} subsequently modeled poles, concave surfaces, and composite reflectors and recovered hidden object shape in practical mmWave environments. mmNorm~\\cite{doddsMmNorm2025} moved further from location to geometry by estimating the hidden object's surface-normal field from mmWave reflections and integrating that field into a 3D surface. "
    "In outdoor T-junctions, Jeon~\\etal~\\cite{jeonRayTracingMmWaveNLOS2025} infer static layout from measured radar returns and ray-trace dynamic multipath to localize multiple hidden pedestrians. BiScalar-AA~\\cite{yuBiScalarAA2025} and the related two-stage attention network~\\cite{yuTSANNLOS2025} add a learned semantic branch for hidden-object detection and tracking from radar pseudo-images. "
    "At CVPR~2026, Wave-Former~\\cite{doddsWaveFormer2026} combines physics-aware wireless surface proposals with transformer shape completion to infer complete 3D geometry of fully occluded objects, while RISE~\\cite{zhouRISE2026} explicitly enhances AoA/AoD multipath from one static radar and uses hierarchical diffusion for indoor layout reconstruction and object detection. "
    "Together these works trace a clear RF trajectory from hidden position, through reflector-aware partial imaging and surface reconstruction, to learned complete shape and scene understanding.\n\n"
)
article5 = replace_once(article5, radar_anchor, radar_para + radar_anchor, "RF lineage insertion")

renderer_anchor = r"\bookmark[dest=\HyperLocalCurrentHref,level=2]{Scattering-Media NLOS Imaging}"
renderer_para = (
    "\\vspace{0.8mm}\n\\noindent \\textbf{Renderer-enabled performance bounds for indirect imaging.}\n"
    "Differentiable and physically based rendering also makes it possible to ask when a hidden parameter is recoverable before choosing a reconstruction network. Sambasivan~\\etal~\\cite{sambasivanRendererBounds2026} use renderer-defined plenoptic forward models, with particular emphasis on passive indirect/NLOS localization, to numerically evaluate Hammersley--Chapman--Robbins lower bounds under noise. "
    "This contribution is adjacent theory rather than a new reconstruction method, but it adds an information-theoretic perspective to the differentiable-rendering trajectory by quantifying estimator limits and the effect of forward-model mismatch.\n\n"
)
article5 = replace_once(article5, renderer_anchor, renderer_para + renderer_anchor, "renderer bounds insertion")

article5 = replace_once(
    article5,
    "Young~\\etal~studied single-photon-LiDAR NLOS sensing for autonomous navigation~\\cite{youngNavigationNLOS2024},",
    "At ICRA~2025, Young~\\etal~studied single-photon-LiDAR NLOS sensing for autonomous navigation~\\cite{youngNavigationNLOS2024},",
    "Young ICRA survey venue",
)
write("article/5newscenes.tex", article5)

article4 = read("article/4datadriven.tex")
article4 = replace_once(
    article4,
    "Su~\\etal~proposed DG-NLOS~\\cite{suDGNLOS2025},",
    "At AAAI~2025, Su~\\etal~proposed DG-NLOS~\\cite{suDGNLOS2025},",
    "DG-NLOS AAAI survey venue",
)
write("article/4datadriven.tex", article4)

bare = read("bare_jrnl.tex")
bare = replace_once(bare, "through 6 August 2026.", "through 7 August 2026.", "survey coverage date")
bare = "% 7 August 2026 citation trace: acoustic second-order diffraction, historical-to-CVPR RF/mmWave lineage, renderer-enabled indirect-imaging bounds, and final-venue corrections synchronized.\n" + bare
write("bare_jrnl.tex", bare)


# ---------------------------------------------------------------------------
# Bibliography used directly by bare_jrnl.tex.
# ---------------------------------------------------------------------------
bib = read("egbib_merged_20260711.bib")
for key, _ in NEW:
    if re.search(r'^@\w+\s*\{\s*' + re.escape(key) + r'\s*,', bib, re.M):
        raise RuntimeError(f"new BibTeX key already exists: {key}")

bib = replace_bib_key(bib, "suDGNLOS2025", r'''@inproceedings{suDGNLOS2025,
  author = {Su, Xiongfei and Zhu, Tianyi and Liu, Lina and Chen, Zheng and Zhang, Yulun and Li, Siyuan and Ye, Juntian and Xu, Feihu and Yuan, Xin},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  doi = {10.1609/aaai.v39i7.32757},
  number = {7},
  pages = {7051--7059},
  title = {Dual-branch Graph Feature Learning for NLOS Imaging},
  url = {https://doi.org/10.1609/aaai.v39i7.32757},
  volume = {39},
  year = {2025}
}''')
bib = replace_bib_key(bib, "youngNavigationNLOS2024", r'''@inproceedings{youngNavigationNLOS2024,
  archiveprefix = {arXiv},
  author = {Young, Aaron and Batagoda, Nevindu M. and Zhang, Harry and Dave, Akshat and Pediredla, Adithya and Negrut, Dan and Raskar, Ramesh},
  booktitle = {2025 IEEE International Conference on Robotics and Automation (ICRA)},
  doi = {10.1109/ICRA55743.2025.11128292},
  eprint = {2410.03555},
  pages = {4907--4914},
  publisher = {IEEE},
  title = {Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR},
  url = {https://doi.org/10.1109/ICRA55743.2025.11128292},
  year = {2025}
}''')
bib = replace_bib_key(bib, "liTransiT2025", r'''@inproceedings{liTransiT2025,
  archiveprefix = {arXiv},
  author = {Li, Ruiqian and Shen, Siyuan and Xia, Suan and Wang, Ziheng and Peng, Xingyue and Song, Chengxuan and Zhu, Yingsheng and Wu, Tao and Li, Shiying and Yu, Jingyi},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  eprint = {2503.11328},
  month = {October},
  pages = {27542--27551},
  title = {TransiT: Transient Transformer for Non-line-of-sight Videography},
  url = {https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html},
  year = {2025}
}''')
bib = replace_bib_key(bib, "fujimuraNLOSNeuS2023", r'''@inproceedings{fujimuraNLOSNeuS2023,
  archiveprefix = {arXiv},
  author = {Fujimura, Yuki and Kushida, Takahiro and Funatomi, Takuya and Mukaigawa, Yasuhiro},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  doi = {10.1109/ICCV51070.2023.00966},
  eprint = {2303.12280},
  month = {October},
  pages = {10532--10541},
  title = {NLOS-NeuS: Non-line-of-sight Neural Implicit Surface},
  url = {https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html},
  year = {2023}
}''')

new_entries = r'''

@article{zhaiSecondOrderAcousticNLOS2025,
  author = {Zhai, Qingbo and Ning, Fangli and Wei, Juan and Su, Zhaojing},
  doi = {10.1016/j.apacoust.2024.110369},
  journal = {Applied Acoustics},
  pages = {110369},
  title = {Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction},
  url = {https://doi.org/10.1016/j.apacoust.2024.110369},
  volume = {228},
  year = {2025}
}

@inproceedings{jeonRayTracingMmWaveNLOS2025,
  author = {Jeon, Mingu and Park, Byeonggyu and Kim, Hee Yeun and Kang, Yujeong and Choi, Byonghyok and Cho, Hansang and Kim, Byungkwan and Lee, Soomok and Seo, Seung Woo and Kim, Seong Woo},
  booktitle = {2025 IEEE Intelligent Vehicles Symposium (IV)},
  doi = {10.1109/IV64158.2025.11097630},
  pages = {1779--1786},
  publisher = {IEEE},
  title = {Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar},
  url = {https://doi.org/10.1109/IV64158.2025.11097630},
  year = {2025}
}

@inproceedings{yuBiScalarAA2025,
  author = {Yu, Yang and Hu, Shijie and Abdul Wahid, Junaid and Zhang, Han and Lv, Qiujie and Hu, Yazhou},
  booktitle = {2025 IEEE Smart World Congress (SWC)},
  doi = {10.1109/SWC65939.2025.00144},
  pages = {886--893},
  publisher = {IEEE},
  title = {BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar},
  url = {https://doi.org/10.1109/SWC65939.2025.00144},
  year = {2025}
}

@article{yuTSANNLOS2025,
  author = {Yu, Yang and Hu, Shijie and Fan, Kangkang and Guo, Wei and Hu, Yazhou and Zhang, Dawei},
  doi = {10.19678/j.issn.1000-3428.0252481},
  journal = {Computer Engineering},
  note = {Online first, published 9 September 2025},
  title = {Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar},
  url = {https://doi.org/10.19678/j.issn.1000-3428.0252481},
  year = {2025}
}

@article{yueCornerRadar2022,
  author = {Yue, Shichao and He, Hao and Cao, Peng and Zha, Kaiwen and Koizumi, Masayuki and Katabi, Dina},
  doi = {10.1145/3517226},
  journal = {Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies},
  number = {1},
  pages = {1--24},
  title = {CornerRadar: RF-Based Indoor Localization Around Corners},
  url = {https://doi.org/10.1145/3517226},
  volume = {6},
  year = {2022}
}

@inproceedings{woodfordMosaic2022,
  author = {Woodford, Timothy and Zhang, Xinyu and Chai, Eugene and Sundaresan, Karthikeyan},
  booktitle = {Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services (MobiSys)},
  doi = {10.1145/3498361.3538944},
  pages = {155--167},
  publisher = {ACM},
  title = {Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar},
  url = {https://doi.org/10.1145/3498361.3538944},
  year = {2022}
}

@inproceedings{doddsRFlect2024,
  author = {Dodds, Laura and Shanbhag, Hailan and Guan, Junfeng and Gupta, Saurabh and Hassanieh, Haitham},
  booktitle = {Proceedings of the 30th Annual International Conference on Mobile Computing and Networking (MobiCom)},
  doi = {10.1145/3636534.3690671},
  pages = {953--967},
  publisher = {ACM},
  title = {Around the Corner mmWave Imaging in Practical Environments},
  url = {https://doi.org/10.1145/3636534.3690671},
  year = {2024}
}

@inproceedings{doddsMmNorm2025,
  author = {Dodds, Laura and Boroushaki, Tara and Zhou, Kaichen and Adib, Fadel},
  booktitle = {Proceedings of the 23rd Annual International Conference on Mobile Systems, Applications and Services (MobiSys)},
  doi = {10.1145/3711875.3729138},
  pages = {445--458},
  publisher = {ACM},
  title = {Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation},
  url = {https://doi.org/10.1145/3711875.3729138},
  year = {2025}
}

@inproceedings{doddsWaveFormer2026,
  author = {Dodds, Laura and Lam, Maisy and Akbar, Waleed and Cheng, Yibo and Adib, Fadel},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  pages = {21713--21724},
  title = {Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion},
  url = {https://openaccess.thecvf.com/content/CVPR2026/html/Dodds_Wave-Former_Through-Occlusion_3D_Reconstruction_via_Wireless_Shape_Completion_CVPR_2026_paper.html},
  year = {2026}
}

@inproceedings{zhouRISE2026,
  author = {Zhou, Kaichen and Dodds, Laura and Afzal, Sayed Saad and Adib, Fadel},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  pages = {32194--32205},
  title = {RISE: Single Static Radar-based Indoor Scene Understanding},
  url = {https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_RISE_Single_Static_Radar-based_Indoor_Scene_Understanding_CVPR_2026_paper.html},
  year = {2026}
}

@misc{sambasivanRendererBounds2026,
  archiveprefix = {arXiv},
  author = {Sambasivan, Abhinav V. and Coulter, Liam J. and Paxman, Richard G. and Haupt, Jarvis D.},
  eprint = {2602.00215},
  primaryclass = {eess.IV},
  title = {A Renderer-Enabled Framework for Computing Parameter Estimation Lower Bounds in Plenoptic Imaging Systems},
  url = {https://arxiv.org/abs/2602.00215},
  year = {2026}
}
'''
bib = bib.rstrip() + new_entries + "\n"
write("egbib_merged_20260711.bib", bib)


# ---------------------------------------------------------------------------
# Traceable integration note.
# ---------------------------------------------------------------------------
note = ROOT / "updates/2026-08-07-citation-trace-integration.md"
if note.exists():
    raise RuntimeError(f"integration note already exists: {note}")
note.write_text("""# 7 August 2026 citation-trace integration

This synchronization converts the preceding citation-trace follow-up into public artifacts. It adds eleven verified missing records: second-order acoustic diffraction localization; CornerRadar and Mosaic; RFlect; mmNorm; measured T-junction multi-target mmWave localization; BiScalar-AA and its related two-stage-attention continuation; Wave-Former; RISE; and a renderer-enabled parameter-estimation-bounds paper explicitly labeled as adjacent theory. The RF lineage was prioritized because forward tracing from core/milestone NLOS work led to real, metadata-verifiable systems papers that were absent from the repository despite their direct hidden-space sensing or reconstruction focus.

The run also reconciles four final venues that were still stale in public artifacts: DG-NLOS to AAAI 2025 (39(7), 7051–7059), single-photon-LiDAR autonomous navigation to ICRA 2025 (4907–4914), TransiT to the final ICCV 2025 record (27542–27551), and NLOS-NeuS to the final ICCV 2023 record (10532–10541, DOI 10.1109/ICCV51070.2023.00966).

The website explorer increases from 257 to 268 records. The survey prose places the new acoustic paper beside diffraction-aware localization, the RF works in chronological systems/reconstruction context, and the renderer paper beside differentiable transient rendering as a performance-bounds contribution rather than a reconstruction algorithm. The bibliography used by `bare_jrnl.tex` is synchronized and `bare_jrnl.pdf` is rebuilt and validated by the guarded integration workflow before this update is committed.
""", encoding="utf-8")

print("Applied Aug 7 citation-traced NLOS integration and final-venue reconciliation.")
