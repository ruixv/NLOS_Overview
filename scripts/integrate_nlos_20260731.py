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


readme = read("README.md")
readme = readme.replace("**Update run: 30 July 2026.**", "**Update run: 31 July 2026.**")
rows = [
    "| 2025 | [Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation](https://doi.org/10.1109/EICARS68214.2025.11320161) — Lin et al. | IEEE EICARS 2025, 140–143 | Uses CLAHE/Sobel-guided contrast modulation and physically guided slot regularization to stabilize object-centric attention on temporally truncated, photon-sparse NLOS signals. It extends the learned-transient branch from reconstruction toward robust semantic classification under incomplete time-series measurements. |\n",
    "| 2025 | [Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model](https://doi.org/10.1007/s00371-025-04069-3) — Jin et al. | The Visual Computer 41(13), 10789–10804 (2025) | MSPDiff progressively reconstructs polarized long-wave-infrared relay observations from coarse to fine resolution, using polarization as a physical cue inside diffusion sampling; the reported passive dataset results reach 25.78 dB PSNR and 0.92 SSIM. |\n",
    "| 2025 | [Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging](https://doi.org/10.1007/s00371-025-03837-5) — Chen et al. | The Visual Computer 41(10), 7767–7780 (2025) | LMS-NLOS combines multi-scale encoding, detail-enhanced Transformer blocks, asymmetric shallow/deep fusion, contour-aware loss, and spatial-shift feed-forward units; its lightweight variant nearly halves model size while retaining strong passive reconstruction quality. |\n",
]
missing_rows = [row for row in rows if row.split("](")[0].split("[")[-1] not in readme]
if missing_rows:
    readme = insert_after_once(readme, "|------|-------|----------------|----------------|\n", "".join(missing_rows), "README latest table")

timeline_add = (
    "2025 ── Chen et al.: LMS-NLOS couples lightweight multi-scale fusion and attention-guided detail recovery for deployable passive reconstruction [The Visual Computer]\n"
    "   │     Jin et al.: MSPDiff introduces polarization-guided coarse-to-fine diffusion for passive LWIR NLOS reconstruction [The Visual Computer]\n"
    "   │     Lin et al.: CA-SlotNet uses contrast-guided slot routing and physics-aware regularization for classification from temporally truncated photon sequences [IEEE EICARS]\n"
)
if "MSPDiff introduces polarization-guided" not in readme:
    readme = insert_before_once(readme, "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics", timeline_add, "README 2025 timeline")
write("README.md", readme)

index = read("index.html")
index = index.replace("Updated 30 July 2026", "Updated 31 July 2026")
index = index.replace("Last updated: 30 July 2026", "Last updated: 31 July 2026")
objects = [
    '      {cat:"latest learning recognition transient photon-sparse truncated slot-attention",title:"Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation",authors:"Lin et al.",year:2025,venue:"IEEE EICARS 2025",url:"https://doi.org/10.1109/EICARS68214.2025.11320161",key:"CA-SlotNet injects CLAHE/Sobel-guided local-contrast modulation into slot attention and adds physically guided slot regularization, stabilizing semantic inference from incomplete photon-sparse transient sequences."},\n',
    '      {cat:"latest passive learning diffusion polarization thermal lwir",title:"Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model",authors:"Jin et al.",year:2025,venue:"The Visual Computer 2025",url:"https://doi.org/10.1007/s00371-025-04069-3",key:"MSPDiff uses polarized LWIR relay observations and progressive coarse-to-fine diffusion training, injecting polarization-derived physical cues into passive reconstruction and reporting 25.78 dB PSNR and 0.92 SSIM."},\n',
    '      {cat:"latest passive learning lightweight transformer attention multi-scale",title:"Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging",authors:"Chen et al.",year:2025,venue:"The Visual Computer 2025",url:"https://doi.org/10.1007/s00371-025-03837-5",key:"LMS-NLOS combines multi-scale encoder-decoder features, detail-enhanced Transformer processing, asymmetric fusion, contour-aware loss, and spatial-shift feed-forward units; the compact variant nearly halves model size."},\n',
]
missing_objects = [obj for obj in objects if re.search(r'title:"([^"]+)"', obj).group(1) not in index]
if missing_objects:
    index = insert_after_once(index, "    const papers=[\n", "".join(missing_objects), "index papers")
if "MSPDiff moved polarization cues" not in index:
    index = index.replace(
        "<p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction,",
        "<p>LMS-NLOS established a lightweight attention-guided passive reconstruction route, MSPDiff moved polarization cues into coarse-to-fine LWIR diffusion, and CA-SlotNet extended photon-transient learning toward classification under temporal truncation. TransDiff, DO-NLOS, physics-guided high-speed reconstruction,",
        1,
    )
paper_count = index.count("{cat:")
index, n = re.subn(r'<b>\d+</b><span>tracked latest entries</span>', f'<b>{paper_count}</b><span>tracked latest entries</span>', index, count=1)
if n != 1:
    raise RuntimeError("website tracked-entry count anchor not found")
write("index.html", index)

passive = read("article/3passive.tex")
passive_block = r"""
\vspace{0.8mm}
\noindent \textbf{Lightweight fusion and polarization-guided diffusion.}
Chen~\etal~introduced LMS-NLOS~\cite{chenLightweightMultiScalePassiveNLOS2025}, combining multi-scale encoder--decoder features with a detail-enhanced Transformer, asymmetric shallow/deep fusion, contour-aware supervision, and spatial-shift feed-forward units. Its compact variant reduces model size by nearly one half while retaining competitive passive reconstruction, making efficiency an explicit design objective rather than a post-hoc compression step. Jin~\etal~subsequently proposed MSPDiff~\cite{jinMSPDiffPassiveNLOS2025}, which uses polarized long-wave-infrared relay observations and a coarse-to-fine diffusion schedule. Polarization supplies a physically meaningful guide to source and surface structure, while progressive diffusion restores increasingly fine hidden detail. Together, these works trace a transition from generic attention to deployable multi-scale networks and then to physics-guided generative priors for passive NLOS.
"""
if "jinMSPDiffPassiveNLOS2025" not in passive:
    anchor = "Recent ordinary-camera methods increasingly encode the relay-wall transport structure inside the network rather than relying on a generic image-to-image backbone. Wang~\\etal~introduced diffuse-aware attention-enhanced encoding for passive NLOS reconstruction~\\cite{wangDiffuseAwarePassive2026}. By explicitly emphasizing features that survive diffuse relay transport, the method represents a further step from early U-Net mappings toward attention mechanisms designed around the conditioning of the passive forward process.\n"
    passive = insert_after_once(passive, anchor, passive_block, "passive learned methods")
write("article/3passive.tex", passive)

data = read("article/4datadriven.tex")
old_para = (
    "Recent work increasingly treats reconstructed NLOS observations as inputs to semantic inference rather than as final outputs. "
    "Sun~\\etal~introduced AME-Net for passive hidden-action recognition from subtle relay-wall video and released the NLOS-Action synthetic/real benchmark~\\cite{sunAdaptiveMotionNLOS2025}. "
    "Lin~\\etal~then considered multiple photon-corrupted NLOS reconstructions as complementary views: NCR-MVC repairs inconsistent neighborhood graphs with shared-neighbor reweighting, Huber-smoothed dual consistency gates, and adaptive inverse-loss view weights, while retaining closed-form alternating updates and a convergence guarantee~\\cite{linNCRMultiViewNLOS2026}. "
    "QSS-Net further makes efficient NLOS classification itself the target, representing the field's shift from complete geometric recovery toward time-sensitive semantic decisions~\\cite{linQSSNetNLOS2026}. "
    "Together with learned feature embeddings and NLOS-R$^2$, these studies establish recognition, action understanding, and clustering as a parallel trajectory to hidden-scene reconstruction."
)
new_para = (
    "Recent work increasingly treats reconstructed NLOS observations as inputs to semantic inference rather than as final outputs. "
    "Sun~\\etal~introduced AME-Net for passive hidden-action recognition from subtle relay-wall video and released the NLOS-Action synthetic/real benchmark~\\cite{sunAdaptiveMotionNLOS2025}. "
    "Lin~\\etal~then considered multiple photon-corrupted NLOS reconstructions as complementary views: NCR-MVC repairs inconsistent neighborhood graphs with shared-neighbor reweighting, Huber-smoothed dual consistency gates, and adaptive inverse-loss view weights, while retaining closed-form alternating updates and a convergence guarantee~\\cite{linNCRMultiViewNLOS2026}. "
    "The same group addressed temporally truncated photon sequences with CA-SlotNet~\\cite{linCASlotNetNLOS2025}: CLAHE- and Sobel-guided local-contrast modulation adjusts slot-attention logits, while a physically guided slot regularizer stabilizes object routing when only part of the transient is observed. "
    "QSS-Net further makes efficient NLOS classification itself the target, representing the field's shift from complete geometric recovery toward time-sensitive semantic decisions~\\cite{linQSSNetNLOS2026}. "
    "Together with learned feature embeddings and NLOS-R$^2$, these studies establish truncation-robust classification, recognition, action understanding, and clustering as a parallel trajectory to hidden-scene reconstruction."
)
if "linCASlotNetNLOS2025" not in data:
    if old_para not in data:
        raise RuntimeError("CA-SlotNet paragraph anchor not found")
    data = data.replace(old_para, new_para, 1)
write("article/4datadriven.tex", data)

main = read("bare_jrnl.tex")
marker = "% 31 July 2026 forward-citation trace: CA-SlotNet, LMS-NLOS, and polarization-guided MSPDiff synchronized.\n"
if marker not in main:
    main = insert_after_once(main, "%% bare_jrnl.tex\n", marker, "bare_jrnl marker")
write("bare_jrnl.tex", main)

note = ROOT / "updates/20260731_passive_learning_citation_trace.md"
note.write_text(
    """# NLOS citation-tracing update — 31 July 2026

This pass followed forward citations from core active/learned NLOS papers and the passive computational-periscopy lineage, then verified candidates against publisher DOI metadata, scholarly indexes, the current README, website explorer, survey source, and merged bibliography.

Integrated:

- **Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation** — IEEE EICARS 2025, DOI `10.1109/EICARS68214.2025.11320161`. Forward-citation candidate from LEAP; semantic transient classification under incomplete photon sequences.
- **Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging** — *The Visual Computer* 41(10), 7767–7780 (2025), DOI `10.1007/s00371-025-03837-5`. Lightweight multi-scale/Transformer passive reconstruction.
- **Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model** — *The Visual Computer* 41(13), 10789–10804 (2025), DOI `10.1007/s00371-025-04069-3`. Polarization-guided LWIR diffusion reconstruction; identified in the forward-citation chain of LMS-NLOS.

Screened but not integrated in this run:

- **Passive NLOS Imaging Based on Multi-Dimension Collaborative Attention Module** (SSRN 2025, DOI `10.2139/ssrn.5169297`). It is directly relevant, but only preprint metadata was verified and no final peer-reviewed venue was found; the published LMS-NLOS/MSPDiff lineage provides stronger, independently indexed records for the same passive-learning trajectory.

The synchronized update includes README, website timeline/explorer, semantically placed survey prose, canonical BibTeX, and a rebuilt survey PDF with citation and render checks.
""",
    encoding="utf-8",
)
print(f"Integrated 3 records; website now contains {paper_count} paper objects.")
