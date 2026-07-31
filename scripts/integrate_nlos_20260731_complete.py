#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def insert_after_once(text: str, anchor: str, addition: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(anchor, anchor + addition, 1)


def insert_before_once(text: str, anchor: str, addition: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(anchor, addition + anchor, 1)


# README ---------------------------------------------------------------------
readme = read("README.md")
readme, n = re.subn(
    r"\*\*Update run: [^*]+\.\*\*",
    "**Update run: 31 July 2026.**",
    readme,
    count=1,
)
if n != 1:
    raise RuntimeError("README update date not found")

rows = [
    "| 2025 | [Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation](https://doi.org/10.1109/EICARS68214.2025.11320161) — Lin et al. | IEEE EICARS 2025, 140–143 | Uses CLAHE/Sobel-guided contrast modulation and physically guided slot regularization to stabilize object-centric attention on temporally truncated, photon-sparse NLOS signals. It extends the learned-transient branch from reconstruction toward robust semantic classification under incomplete time-series measurements. |\n",
    "| 2025 | [Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model](https://doi.org/10.1007/s00371-025-04069-3) — Jin et al. | The Visual Computer 41(13), 10789–10804 (2025) | MSPDiff progressively reconstructs polarized long-wave-infrared relay observations from coarse to fine resolution, using polarization as a physical cue inside diffusion sampling; the reported passive dataset results reach 25.78 dB PSNR and 0.92 SSIM. |\n",
    "| 2025 | [Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging](https://doi.org/10.1007/s00371-025-03837-5) — Chen et al. | The Visual Computer 41(10), 7767–7780 (2025) | LMS-NLOS combines multi-scale encoding, detail-enhanced Transformer blocks, asymmetric shallow/deep fusion, contour-aware loss, and spatial-shift feed-forward units; its lightweight variant nearly halves model size while retaining strong passive reconstruction quality. |\n",
    "| 2025 | [Multipath Exploitation-Based Linearized Inverse Scattering Method for Non-Line-of-Sight Indoor Imaging of PEC Objects](https://doi.org/10.1109/JSTARS.2025.3537181) — Suenobu et al. | IEEE JSTARS 18, 6694–6709 (2025) | Treats wall-mediated multipath as a geometry-specific numerical Green tensor inside a physical-optics linearized inverse-scattering model. Full-wave simulation and measured 2 GHz T-junction experiments recover the location and planar extent of hidden PEC objects. |\n",
    "| 2024 | [Non-Line-of-Sight Imaging by Linearized Inverse Scattering Method Based on Physical Optics](https://doi.org/10.1109/ICEAA61917.2024.10701790) — Suenobu et al. | IEEE ICEAA 2024 | Establishes the simulation-only precursor: known T-junction geometry and a numerically computed multipath Green tensor make physical-optics linearized inverse scattering applicable to hidden PEC targets. |\n",
]
missing_rows = []
for row in rows:
    title = row.split("](", 1)[0].split("[", 1)[1]
    if title not in readme:
        missing_rows.append(row)
if missing_rows:
    readme = insert_after_once(
        readme,
        "|------|-------|----------------|----------------|\n",
        "".join(missing_rows),
        "README latest table",
    )

passive_timeline = (
    "2025 ── Chen et al.: LMS-NLOS couples lightweight multi-scale fusion and attention-guided detail recovery for deployable passive reconstruction [The Visual Computer]\n"
    "   │     Jin et al.: MSPDiff introduces polarization-guided coarse-to-fine diffusion for passive LWIR NLOS reconstruction [The Visual Computer]\n"
    "   │     Lin et al.: CA-SlotNet uses contrast-guided slot routing and physics-aware regularization for classification from temporally truncated photon sequences [IEEE EICARS]\n"
)
if "MSPDiff introduces polarization-guided" not in readme:
    readme = insert_before_once(
        readme,
        "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics",
        passive_timeline,
        "README passive timeline",
    )

rf_timeline = (
    "2024 ── Suenobu et al.: physical-optics linearized inverse scattering embeds a known T-junction's multipath Green tensor for simulated hidden-PEC imaging [IEEE ICEAA]\n"
    "2025 ── Suenobu et al.: the multipath-exploitation formulation is extended to full-wave simulation and measured 2 GHz indoor T-junction imaging [IEEE JSTARS]\n"
)
if "multipath-exploitation formulation is extended" not in readme:
    readme = insert_before_once(
        readme,
        "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics",
        rf_timeline,
        "README RF timeline",
    )

# Correct public-facing final venue if the older arXiv-only record remains.
readme = readme.replace("Geometric Constrained Non-Line-of-Sight Imaging", "Geometry-Constrained Non-Line-of-Sight Imaging")
readme = readme.replace("https://arxiv.org/abs/2503.17992", "https://doi.org/10.1109/TVCG.2026.3684832")
readme = readme.replace("https://arxiv.org/pdf/2503.17992", "https://doi.org/10.1109/TVCG.2026.3684832")
write("README.md", readme)


# Website --------------------------------------------------------------------
index = read("index.html")
index = re.sub(r"Updated \d{1,2} [A-Za-z]+ 2026", "Updated 31 July 2026", index)
index = re.sub(r"Last updated: \d{1,2} [A-Za-z]+ 2026", "Last updated: 31 July 2026", index)

objects = [
    '      {cat:"latest learning recognition transient photon-sparse truncated slot-attention",title:"Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation",authors:"Lin et al.",year:2025,venue:"IEEE EICARS 2025",url:"https://doi.org/10.1109/EICARS68214.2025.11320161",key:"CA-SlotNet injects CLAHE/Sobel-guided local-contrast modulation into slot attention and adds physically guided slot regularization, stabilizing semantic inference from incomplete photon-sparse transient sequences."},\n',
    '      {cat:"latest passive learning diffusion polarization thermal lwir",title:"Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model",authors:"Jin et al.",year:2025,venue:"The Visual Computer 2025",url:"https://doi.org/10.1007/s00371-025-04069-3",key:"MSPDiff uses polarized LWIR relay observations and progressive coarse-to-fine diffusion training, injecting polarization-derived physical cues into passive reconstruction and reporting 25.78 dB PSNR and 0.92 SSIM."},\n',
    '      {cat:"latest passive learning lightweight transformer attention multi-scale",title:"Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging",authors:"Chen et al.",year:2025,venue:"The Visual Computer 2025",url:"https://doi.org/10.1007/s00371-025-03837-5",key:"LMS-NLOS combines multi-scale encoder-decoder features, detail-enhanced Transformer processing, asymmetric fusion, contour-aware loss, and spatial-shift feed-forward units; the compact variant nearly halves model size."},\n',
    '      {cat:"latest radar rf inverse-scattering multipath physical-optics measured",title:"Multipath Exploitation-Based Linearized Inverse Scattering Method for Non-Line-of-Sight Indoor Imaging of PEC Objects",authors:"Suenobu et al.",year:2025,venue:"IEEE JSTARS 2025",url:"https://doi.org/10.1109/JSTARS.2025.3537181",key:"A geometry-specific numerical Green tensor incorporates wall-mediated multipath into a physical-optics linearized inverse-scattering operator; full-wave and measured 2 GHz T-junction experiments recover hidden PEC targets."},\n',
    '      {cat:"radar rf inverse-scattering multipath physical-optics simulation",title:"Non-Line-of-Sight Imaging by Linearized Inverse Scattering Method Based on Physical Optics",authors:"Suenobu et al.",year:2024,venue:"IEEE ICEAA 2024",url:"https://doi.org/10.1109/ICEAA61917.2024.10701790",key:"Simulation precursor that uses known T-junction geometry and a numerical multipath Green tensor to linearize physical-optics inversion for hidden PEC imaging."},\n',
]
missing_objects = []
for obj in objects:
    title = re.search(r'title:"([^"]+)"', obj).group(1)
    if title not in index:
        missing_objects.append(obj)
if missing_objects:
    index = insert_after_once(index, "    const papers=[\n", "".join(missing_objects), "index papers")

summary_sentence = (
    "LMS-NLOS established a lightweight attention-guided passive reconstruction route, "
    "MSPDiff moved polarization cues into coarse-to-fine LWIR diffusion, CA-SlotNet extended "
    "photon-transient learning toward classification under temporal truncation, and Suenobu et al. "
    "advanced physical-optics multipath inversion from simulation to measured RF NLOS. "
)
if "CA-SlotNet extended photon-transient learning" not in index:
    pattern = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)', re.S)
    index, n = pattern.subn(lambda m: m.group(1) + summary_sentence, index, count=1)
    if n != 1:
        raise RuntimeError("index 2025 timeline anchor not found")

index = index.replace("Geometric Constrained Non-Line-of-Sight Imaging", "Geometry-Constrained Non-Line-of-Sight Imaging")
index = index.replace("https://arxiv.org/abs/2503.17992", "https://doi.org/10.1109/TVCG.2026.3684832")
index = index.replace("https://arxiv.org/pdf/2503.17992", "https://doi.org/10.1109/TVCG.2026.3684832")
paper_count = index.count("{cat:")
index, n = re.subn(
    r'<b>\d+</b><span>tracked latest entries</span>',
    f'<b>{paper_count}</b><span>tracked latest entries</span>',
    index,
    count=1,
)
if n != 1:
    raise RuntimeError("website tracked-entry count anchor not found")
write("index.html", index)


# Passive survey prose --------------------------------------------------------
passive = read("article/3passive.tex")
passive_block = r"""
\vspace{0.8mm}
\noindent \textbf{Lightweight fusion and polarization-guided diffusion.}
Chen~\etal~introduced LMS-NLOS~\cite{chenLightweightMultiScalePassiveNLOS2025}, combining multi-scale encoder--decoder features with a detail-enhanced Transformer, asymmetric shallow/deep fusion, contour-aware supervision, and spatial-shift feed-forward units. Its compact variant reduces model size by nearly one half while retaining competitive passive reconstruction, making efficiency an explicit design objective rather than a post-hoc compression step. Jin~\etal~subsequently proposed MSPDiff~\cite{jinMSPDiffPassiveNLOS2025}, which uses polarized long-wave-infrared relay observations and a coarse-to-fine diffusion schedule. Polarization supplies a physically meaningful guide to source and surface structure, while progressive diffusion restores increasingly fine hidden detail. Together, these works trace a transition from generic attention to deployable multi-scale networks and then to physics-guided generative priors for passive NLOS.
"""
if "jinMSPDiffPassiveNLOS2025" not in passive:
    anchor = (
        "Recent ordinary-camera methods increasingly encode the relay-wall transport structure inside the network rather than relying on a generic image-to-image backbone. "
        "Wang~\\etal~introduced diffuse-aware attention-enhanced encoding for passive NLOS reconstruction~\\cite{wangDiffuseAwarePassive2026}. "
        "By explicitly emphasizing features that survive diffuse relay transport, the method represents a further step from early U-Net mappings toward attention mechanisms designed around the conditioning of the passive forward process.\n"
    )
    passive = insert_after_once(passive, anchor, passive_block, "passive learned methods")
write("article/3passive.tex", passive)


# Data-driven survey prose ----------------------------------------------------
data = read("article/4datadriven.tex")
if "linCASlotNetNLOS2025" not in data:
    anchor = (
        "Lin~\\etal~then considered multiple photon-corrupted NLOS reconstructions as complementary views: NCR-MVC repairs inconsistent neighborhood graphs with shared-neighbor reweighting, Huber-smoothed dual consistency gates, and adaptive inverse-loss view weights, while retaining closed-form alternating updates and a convergence guarantee~\\cite{linNCRMultiViewNLOS2026}. "
    )
    addition = (
        "The same group addressed temporally truncated photon sequences with CA-SlotNet~\\cite{linCASlotNetNLOS2025}: CLAHE- and Sobel-guided local-contrast modulation adjusts slot-attention logits, while a physically guided slot regularizer stabilizes object routing when only part of the transient is observed. "
    )
    data = insert_after_once(data, anchor, addition, "CA-SlotNet recognition paragraph")
    old = "establish recognition, action understanding, and clustering as a parallel trajectory"
    new = "establish truncation-robust classification, recognition, action understanding, and clustering as a parallel trajectory"
    if old not in data:
        raise RuntimeError("recognition trajectory sentence not found")
    data = data.replace(old, new, 1)
write("article/4datadriven.tex", data)


# RF/new-scenes survey prose --------------------------------------------------
newscenes = read("article/5newscenes.tex")
rf_block = r"""
\vspace{0.8mm}
\noindent \textbf{Multipath-exploitation inverse scattering for RF NLOS.}
Suenobu~\etal~first applied a physical-optics linearization to a known indoor T-junction, using a numerically evaluated Green tensor to encode the wall-mediated paths between the radar aperture and hidden imaging region~\cite{suenobuPhysicalOpticsNLOS2024}. Their subsequent journal study extended this formulation to multipath-exploitation imaging of PEC objects~\cite{suenobuMultipathInverseScatteringNLOS2025}. Rather than suppressing indirect returns as ghosts, the method incorporates them into the forward operator and recovers hidden target position and planar extent. Three-dimensional full-wave simulations and measured 2~GHz anechoic-chamber experiments establish a complementary RF trajectory to mirror-symmetry backprojection and learned mmWave reconstruction: environment geometry is assumed known, while target scattering is inferred through a linearized inverse problem.

"""
if "suenobuMultipathInverseScatteringNLOS2025" not in newscenes:
    newscenes = insert_before_once(
        newscenes,
        "Du~\\etal~extended radar NLOS from room-scale mmWave perception toward long-range X-band imaging",
        rf_block,
        "RF inverse-scattering paragraph",
    )
write("article/5newscenes.tex", newscenes)


# Main source marker ----------------------------------------------------------
main = read("bare_jrnl.tex")
marker = "% 31 July 2026 citation trace: RF inverse-scattering lineage, CA-SlotNet, LMS-NLOS, MSPDiff, and the final TVCG geometry-constrained record synchronized.\n"
if marker not in main:
    main = insert_after_once(main, "%% bare_jrnl.tex\n", marker, "bare_jrnl marker")
write("bare_jrnl.tex", main)


# Append a completion record to the existing audit notes without discarding
# their verified metadata and exact insertion history.
completion = (
    "\n## Integration completed\n\n"
    "The pending records in this note were synchronized across README, website, semantically appropriate survey sections, the consolidated bibliography, and the rebuilt survey PDF on 31 July 2026. The final integration also includes the RF inverse-scattering lineage and the final IEEE TVCG venue for Geometry-Constrained Non-Line-of-Sight Imaging.\n"
)
for note_path in (
    "updates/20260731_passive_learning_citation_trace.md",
    "updates/20260731_rf_inverse_scattering_and_consistency.md",
):
    text = read(note_path)
    if "## Integration completed" not in text:
        write(note_path, text.rstrip() + "\n" + completion)

print(f"Integrated five pending records; website now contains {paper_count} paper objects.")
