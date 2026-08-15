from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

SPOTLIGHT_TITLE = "Learning-Based Spotlight Position Optimization for Non-Line-of-Sight Human Localization and Posture Classification"
PASSIVE_TITLE = "Deep-Learning-Based Real-Time Passive Non-Line-of-Sight Imaging for Room-Scale Scenes"
HOU_KEY = "houMultiPersonPose2025"
SPOT_KEY = "chandranSpotlightWACV2024"
PASS_KEY = "liUSEENPassiveNLOS2024"


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:120]}")


# README: public latest-addition rows + historical placement.
readme = read("README.md")
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README latest table")
rows = []
if SPOTLIGHT_TITLE not in readme:
    rows.append(
        "| 2024 | [Learning-Based Spotlight Position Optimization for Non-Line-of-Sight Human Localization and Posture Classification](https://doi.org/10.1109/WACV57701.2024.00417) — Chandran et al. | IEEE/CVF WACV 2024 | Uses an off-the-shelf projector-camera pair and a message-passing network to infer scene structure and choose the spotlight position that maximizes useful indirect signal, enabling hidden-person localization and posture classification under more arbitrary scene geometry than planar-relay assumptions. |\n"
    )
if PASSIVE_TITLE not in readme:
    rows.append(
        "| 2024 | [Deep-Learning-Based Real-Time Passive Non-Line-of-Sight Imaging for Room-Scale Scenes](https://doi.org/10.3390/s24196480) — Li and Zhang | Sensors 24(19), 6480 (2024) | Introduces USEEN for conventional-camera passive NLOS in room-scale scenes, targeting diffuse relay surfaces and ambient-light interference while reporting 12.2 ms inference for real-time hidden-person reconstruction. |\n"
    )
if rows:
    readme = readme.replace(header, header + "".join(rows), 1)

timeline_anchor = "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
if "Chandran et al.: learned spotlight selection" not in readme:
    require(readme, timeline_anchor, "README 2024 timeline")
    readme = readme.replace(
        timeline_anchor,
        timeline_anchor
        + "   │     Chandran et al.: learned spotlight selection with an off-the-shelf projector-camera pair turns illumination placement into an end-to-end NLOS sensing variable [WACV]\n"
        + "   │     Li and Zhang: USEEN brings passive diffuse-wall NLOS reconstruction to room-scale scenes with 12.2 ms inference [Sensors]\n",
        1,
    )
write("README.md", readme)


# Canonical website corpus: explorer/latest cards and historical timeline are driven by data/papers-source.html.
data = read("data/papers-source.html")
objects = []
if SPOTLIGHT_TITLE not in data:
    objects.append(
        '      {cat:"latest learning active steady-state projector camera localization posture semantic arbitrary-relay",title:"Learning-Based Spotlight Position Optimization for Non-Line-of-Sight Human Localization and Posture Classification",authors:"Chandran et al.",year:2024,venue:"IEEE/CVF WACV 2024",url:"https://doi.org/10.1109/WACV57701.2024.00417",key:"Uses an off-the-shelf projector-camera system and a message-passing network to learn scene geometry and select spotlight positions that maximize useful indirect signal for hidden-person localization and posture classification, extending learned NLOS sensing beyond fixed planar relay assumptions."},\n'
    )
if PASSIVE_TITLE not in data:
    objects.append(
        '      {cat:"latest passive learning realtime room-scale diffuse ambient conventional-camera",title:"Deep-Learning-Based Real-Time Passive Non-Line-of-Sight Imaging for Room-Scale Scenes",authors:"Li and Zhang",year:2024,venue:"Sensors 24(19), 6480 (2024)",url:"https://doi.org/10.3390/s24196480",key:"Introduces USEEN for room-scale passive NLOS reconstruction from diffuse relay observations, emphasizing robustness to ambient-light interference and reporting 12.2 ms inference for real-time hidden-person imaging."},\n'
    )
if objects:
    anchor = "    const papers=[\n"
    require(data, anchor, "paper corpus")
    data = data.replace(anchor, anchor + "".join(objects), 1)
    count = len(objects)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    old = int(m.group(1))
    data = pat.sub(f'<b>{old + count}</b><span>tracked latest entries</span>', data, count=1)

if "learned spotlight placement" not in data:
    pat = re.compile(r'(<div class="tl"><div class="year">2024</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate 2024 website timeline block")
    sentence = (
        " Chandran et al. made spotlight placement itself learnable with an off-the-shelf projector-camera system for hidden-person localization and posture classification under flexible scene geometry."
        " Li and Zhang introduced USEEN for room-scale passive diffuse-wall NLOS, reporting 12.2 ms inference and robustness to ambient-light interference."
    )
    data = data[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + data[m.end():]
write("data/papers-source.html", data)


# Active-method table: synchronize an already-public 2025 multi-person pose paper and the 2024 learned-lighting paper.
active = read("article/2active.tex")
pose_old = r"\cite{isogawaOpticalNonLineofSightPhysicsBased2020,romanelliFiniteApertureYawNLOS2026,xiaoNLOSHumanPose2026} & Pulsed laser & SPAD & Time of fight &  Pose estimation"
pose_new = r"\cite{isogawaOpticalNonLineofSightPhysicsBased2020,houMultiPersonPose2025,romanelliFiniteApertureYawNLOS2026,xiaoNLOSHumanPose2026} & Pulsed laser & SPAD & Time of fight &  Pose estimation"
if HOU_KEY not in active.split("\\bookmark", 1)[0]:
    require(active, pose_old, "active pose table")
    active = active.replace(pose_old, pose_new, 1)

ch_old = r"\cite{chandranAdaptiveLightingDataDriven2019} & Incoherent light source (imaging side) & Conventional camera & Intensity &  Detection/ Tracking/ Identification"
ch_new = r"\cite{chandranAdaptiveLightingDataDriven2019,chandranSpotlightWACV2024} & Projector / incoherent illumination & Conventional camera & Intensity &  Localization / posture classification"
if SPOT_KEY not in active.split("\\bookmark", 1)[0]:
    require(active, ch_old, "active spotlight table")
    active = active.replace(ch_old, ch_new, 1)
write("article/2active.tex", active)


# Deep-learning narrative: bridge learned acquisition control and the already-listed multi-person transient pose paper.
dd = read("article/4datadriven.tex")
if SPOT_KEY not in dd or HOU_KEY not in dd:
    anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{From reconstruction to recognition and clustering.}"
    require(dd, anchor, "data-driven semantic section")
    para = r"""\vspace{0.8mm}
\noindent \textbf{Learned illumination control and multi-person pose sensing.}
Semantic NLOS systems increasingly optimize not only the decoder but also how indirect evidence is acquired. Chandran~\etal~use an off-the-shelf projector and camera and train a message-passing network to infer scene structure and select the spotlight position that maximizes downstream NLOS localization and posture-classification performance~\cite{chandranSpotlightWACV2024}. The illumination position is therefore learned end-to-end rather than supplied as a separately supervised target, and synthetic plus real experiments extend learned steady-state sensing beyond a fixed planar-relay configuration. Hou~\etal~address a complementary limitation of transient semantic sensing: previous pose methods largely assume one hidden person. Their AMPE-NLOS pipeline first uses LCT to form coarse three-dimensional features, refines them with a 3D U-Net, and then predicts body-center heatmaps and SMPL parameter maps so a variable number of people can be separated by body-center-guided sampling~\cite{houMultiPersonPose2025}. Experiments on simulated multi-person transients and a self-built confocal laser/SPAD system move active NLOS from single-person pose inference toward multi-person three-dimensional mesh sensing.

"""
    dd = dd.replace(anchor, para + anchor, 1)
write("article/4datadriven.tex", dd)


# Passive narrative: add room-scale real-time conventional-camera branch.
passive = read("article/3passive.tex")
if PASS_KEY not in passive:
    anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Diffuse-aware attention encoding for passive NLOS.}"
    require(passive, anchor, "passive diffuse-aware section")
    para = r"""\vspace{0.8mm}
\noindent \textbf{Room-scale real-time passive reconstruction.}
Li and Zhang targeted a deployment regime that is only weakly represented by small laboratory passive-NLOS datasets: moving people in room-scale hidden scenes observed through diffuse relay surfaces under ambient illumination~\cite{liUSEENPassiveNLOS2024}. Their unseen-scene encoding enhancement network (USEEN) is a compact convolutional reconstruction model designed to preserve hidden-scene structure while suppressing relay-wall and illumination interference. The reported 12.2~ms inference time makes reconstruction latency an explicit systems objective, complementing computational-periscopy methods that emphasize inverse conditioning and later attention, diffusion, spectral, and thermal models that emphasize reconstruction fidelity or robustness. This work therefore supplies an intermediate step from ordinary-camera passive inversion toward practical real-time indoor sensing.

"""
    passive = passive.replace(anchor, para + anchor, 1)
write("article/3passive.tex", passive)


# Top-level survey synchronization marker.
tex = read("bare_jrnl.tex")
marker = "% 15 August 2026 citation/gap trace: WACV learned spotlight control, room-scale passive USEEN, and multi-person pose survey consistency synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Update note records what was integrated and why.
note = ROOT / "updates/2026-08-15-semantic-passive-gap.md"
note.write_text(
    """# 15 August 2026 semantic/passive NLOS gap synchronization

This citation-tracing and public-artifact consistency pass integrates two verified 2024 papers that were absent from the repository and closes one survey-only consistency gap for a 2025 paper already present in README/website/BibTeX.

## Newly integrated papers

1. Sreenithy Chandran, Tatsuya Yatagawa, Hiroyuki Kubo, and Suren Jayasuriya, **Learning-Based Spotlight Position Optimization for Non-Line-of-Sight Human Localization and Posture Classification**, IEEE/CVF WACV 2024, DOI `10.1109/WACV57701.2024.00417`.
   - Off-the-shelf projector + camera.
   - Message-passing network learns scene structure and selects the spotlight position that maximizes downstream NLOS localization/posture performance.
   - Important because acquisition/illumination placement becomes a learned variable and the system is not restricted to a fixed planar relay geometry.

2. Yuzhe Li and Yuning Zhang, **Deep-Learning-Based Real-Time Passive Non-Line-of-Sight Imaging for Room-Scale Scenes**, Sensors 24(19), 6480 (2024), DOI `10.3390/s24196480`.
   - USEEN targets room-scale passive hidden-person reconstruction through diffuse relay surfaces.
   - Reports 12.2 ms inference and explicitly evaluates ambient-light robustness.
   - Adds a practical real-time indoor branch between computational periscopy and later attention/diffusion/thermal passive models.

## Consistency repair

The already-public **Non-line-of-sight multi-person pose sensing** (Hou et al., Optics Express 2025, DOI `10.1364/OE.570120`) already existed in README/website/BibTeX but was not cited in the survey body. The active-method pose table and deep-learning narrative now include it, describing the LCT + 3D U-Net + body-center-guided SMPL pipeline for adaptive multi-person 3D pose sensing.

## Public artifacts

The synchronized integration updates README, the canonical website corpus in `data/papers-source.html`, the active/passive/deep-learning survey sections, top-level `bare_jrnl.tex`, merged bibliography, and rebuilt `bare_jrnl.pdf`. The canonical `index.html` consumes the paper corpus from `data/papers-source.html`, so Paper Explorer/latest/timeline changes are reflected without duplicating the historical paper array in `index.html`.
""",
    encoding="utf-8",
)

print("semantic/passive NLOS gap integration applied")
