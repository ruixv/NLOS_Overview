#!/usr/bin/env python3
"""Synchronize citation-traced Optica/APS NLOS follow-up papers, 17 July 2026."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

DIFFUSE = "Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding"
L2CT = "Learned light-cone transform for fast and accurate non-line-of-sight imaging"
TRANSVID = "Transient video interpolation for dynamic non-line-of-sight imaging"
MULTISURFACE = "Multi-surface sub-resolution non-line-of-sight imaging via transient waveform deposition"
SIMULATION = "Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def replace_line_containing(text: str, needle: str, replacement: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {label} line containing {needle!r}, found {len(matches)}")
    ending = "\n" if lines[matches[0]].endswith("\n") else ""
    lines[matches[0]] = replacement.rstrip("\n") + ending
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = [
        (DIFFUSE, f"| 2026 | [{DIFFUSE}](https://opg.optica.org/oe/abstract.cfm?uri=oe-34-14-26271) — Wang et al. | Optics Express 2026 | Introduces diffuse-aware, attention-enhanced feature encoding for ordinary-camera passive NLOS reconstruction, explicitly targeting information loss caused by diffuse relay-wall transport rather than treating the wall projection as an unconstrained image-to-image mapping. |"),
        (L2CT, f"| 2026 | [{L2CT}](https://doi.org/10.1103/jsbg-c7l5) — Gao et al. | Physical Review Applied 2026 | Citation-traced directly from the original LCT: replaces its fixed low-pass Wiener stage with high-frequency-enhanced learnable filtering, spatiotemporal feature extraction, and volume projection; reports a 5 dB PSNR gain over LCT and cross-system measured-data generalization. |"),
        (TRANSVID, f"| 2026 | [{TRANSVID}](https://doi.org/10.1364/OE.580550) — Sun et al. | Optics Express 2026 | Introduces TransVID, the first diffusion-based transient-video interpolation framework for dynamic NLOS; jointly performs spatial and temporal upsampling, recovering 128×128 transient video at 16 fps from 16×16 measurements at 4 fps before hidden-scene reconstruction. |"),
        (MULTISURFACE, f"| 2025 | [{MULTISURFACE}](https://doi.org/10.1364/OE.579004) — Wei et al. | Optics Express 2025 | Decomposes overlapping multi-surface transient returns as Gaussian mixtures using L1–L2 deconvolution and constrained modified Levenberg–Marquardt fitting, then reconstructs each deposited waveform with LCT; improves reported axial/lateral discrimination from 5.25/9.74 cm to 1 cm. |"),
    ]
    header = "|------|-------|----------------|----------------|\n"
    insertion = "".join(row + "\n" for title, row in rows if f"[{title}]" not in text)
    if insertion:
        text = replace_once(text, header, header + insertion, "README latest-table")

    sim_row = (
        f"| 2025 | [{SIMULATION}](https://doi.org/10.1364/OE.575753) — Shi et al. | Optics Express 2025 | "
        "Provides a configurable intensity-transport transient simulator from depth and optional albedo maps, models detector jitter and Poisson noise, releases seven ShapeNet-category datasets, and benchmarks LCT, phasor-field, f-k, and backprojection baselines. |"
    )
    text = replace_line_containing(text, f"[{SIMULATION}]", sim_row, "simulation final-venue correction")

    if "Gao et al.: learned LCT" not in text:
        anchor = "   │     Lu et al. and Behari et al.: RF geometry reconstruction and low-cost-LiDAR spatial-reasoning benchmarks [CVPR]\n"
        addition = (
            "   │     Gao et al.: learned LCT — high-frequency-preserving trainable inversion grounded in the original light-cone transform [Physical Review Applied]\n"
            "   │     Sun et al.: TransVID — diffusion-based spatial-temporal interpolation for dynamic transient video [Optics Express]\n"
            "   │     Wang et al.: diffuse-aware attention encoding for passive NLOS through relay-wall diffusion [Optics Express]\n"
            "   │\n"
            "2025 ── Wei et al.: multi-surface waveform deposition — sub-resolution separation of overlapping transient surfaces before LCT reconstruction [Optics Express]\n"
        )
        text = replace_once(text, anchor, anchor + addition, "README 2026 frontier timeline")
    path.write_text(text, encoding="utf-8")


def paper_object(title: str, authors: str, year: int, venue: str, url: str, cat: str, key: str) -> str:
    return f'      {{cat:"{cat}",title:"{title}",authors:"{authors}",year:{year},venue:"{venue}",url:"{url}",key:"{key}"}},'


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    objects = [
        (DIFFUSE, paper_object(DIFFUSE, "Wang et al.", 2026, "Optics Express 2026", "https://opg.optica.org/oe/abstract.cfm?uri=oe-34-14-26271", "latest passive learning", "Diffuse-aware attention-enhanced encoding explicitly preserves hidden-scene evidence mixed by diffuse relay-wall transport for ordinary-camera passive NLOS reconstruction.")),
        (L2CT, paper_object(L2CT, "Gao et al.", 2026, "Physical Review Applied 2026", "https://doi.org/10.1103/jsbg-c7l5", "latest active learning", "A citation-traced extension of LCT that learns high-frequency-enhanced Wiener filtering and combines it with spatiotemporal extraction and volume projection, improving measured-data reconstruction across systems.")),
        (TRANSVID, paper_object(TRANSVID, "Sun et al.", 2026, "Optics Express 2026", "https://doi.org/10.1364/OE.580550", "latest active learning dynamic", "TransVID uses spatial-temporal attention and latent conditional diffusion to interpolate low-resolution, low-frame-rate transient measurements into dense high-speed transient video for dynamic NLOS.")),
        (MULTISURFACE, paper_object(MULTISURFACE, "Wei et al.", 2025, "Optics Express 2025", "https://doi.org/10.1364/OE.579004", "latest active", "Gaussian-mixture waveform deposition separates overlapping returns from multiple hidden surfaces before LCT reconstruction, enabling centimeter-scale sub-resolution discrimination.")),
    ]
    new_lines = ""
    inserted = 0
    for title, obj in objects:
        if f'title:"{title}"' not in text:
            new_lines += obj + "\n"
            inserted += 1
    if new_lines:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + new_lines, "homepage paper array")
    if inserted:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
        match = pattern.search(text)
        if not match:
            raise RuntimeError("Homepage tracked-count anchor is missing")
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + inserted}{m.group(3)}", text, count=1)

    sim_obj = paper_object(SIMULATION, "Shi et al.", 2025, "Optics Express 2025", "https://doi.org/10.1364/OE.575753", "latest dataset active", "A configurable, detector-aware fast transient simulator and open seven-category benchmark with LCT, phasor-field, f-k, and backprojection baselines.")
    text = replace_line_containing(text, f'title:"{SIMULATION}"', sim_obj, "homepage simulation final venue")

    pattern_2026 = re.compile(r'^\s*<div class="tl"><div class="year">2026</div>.*$', re.MULTILINE)
    new_2026 = '      <div class="tl"><div class="year">2026</div><div class="tl-body"><strong>Deployable sensing, learned physical operators, dynamic transient completion, thermal/passive reconstruction, consumer LiDAR, and RF geometry</strong><p>PICL couples SPAD-specific noise separation with a differentiable forward model; all-day Si-SPAD sensing reaches 200 m under intense illumination; NLOSFormer handles rough-wall thermal transport; MDUNet and diffuse-aware attention advance ordinary-camera passive reconstruction; learned LCT turns the field-defining analytic inverse into a high-frequency-preserving trainable operator; TransVID uses conditional diffusion for joint spatial-temporal transient interpolation; consumer LiDAR and CVPR radar/LiDAR work broaden deployable hardware; and Gaussian transient rendering supports arbitrary relay geometry.</p></div></div>'
    if len(pattern_2026.findall(text)) != 1:
        raise RuntimeError("Expected exactly one 2026 homepage timeline row")
    text = pattern_2026.sub(new_2026, text, count=1)
    path.write_text(text, encoding="utf-8")


def append_active_table_keys(text: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if "Pulsed laser & SPAD & Time of fight &  3D reconstruction" in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one active SPAD reconstruction row, found {len(matches)}")
    line = lines[matches[0]]
    match = re.search(r"\\cite\{([^}]*)\}", line)
    if not match:
        raise RuntimeError("Active SPAD row has no citation list")
    keys = [k.strip() for k in match.group(1).split(",") if k.strip()]
    for key in ("gaoLearnedLCT2026", "sunTransVID2026", "weiMultiSurfaceNLOS2025"):
        if key not in keys:
            keys.append(key)
    lines[matches[0]] = line[:match.start(1)] + ",".join(keys) + line[match.end(1):]
    return "".join(lines)


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = append_active_table_keys(path.read_text(encoding="utf-8"))
    if "weiMultiSurfaceNLOS2025" not in text[text.index(r"\end{table*}") + len(r"\end{table*}"):]:
        anchor = "\n\vspace{0.8mm}\n\noindent \\textbf{Active Focusing for High Resolution.}"
        paragraph = (
            "\n\vspace{0.8mm}\n"
            "\\noindent \\textbf{Multi-surface sub-resolution transient decomposition.}\n"
            "Dense hidden geometry can produce temporally overlapping returns whose separation is below the native impulse-response width. Wei~\\etal~modeled multi-surface transient reflections as Gaussian mixtures, combined $L_1$--$L_2$ waveform deconvolution with constrained modified Levenberg--Marquardt fitting, and deposited the separated components into individual transient volumes before LCT reconstruction~\\cite{weiMultiSurfaceNLOS2025}. The reported centimeter-scale discrimination substantially improves both axial and lateral separation of nearby surfaces, showing that resolution can be increased in the transient-signal domain before applying a conventional volumetric inverse.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "active focusing heading")
    path.write_text(text, encoding="utf-8")


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")
    if "wangDiffuseAwarePassive2026" not in text:
        anchor = "\n\vspace{0.8mm}\n\\noindent \\textbf{Thermal NLOS through rough relay surfaces.}"
        paragraph = (
            "\n\vspace{0.8mm}\n"
            "\\noindent \\textbf{Diffuse-aware attention encoding for passive NLOS.}\n"
            "Recent ordinary-camera methods increasingly encode the relay-wall transport structure inside the network rather than relying on a generic image-to-image backbone. Wang~\\etal~introduced diffuse-aware attention-enhanced encoding for passive NLOS reconstruction~\\cite{wangDiffuseAwarePassive2026}. By explicitly emphasizing features that survive diffuse relay transport, the method represents a further step from early U-Net mappings toward attention mechanisms designed around the conditioning of the passive forward process.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "thermal passive paragraph")
    table_end = text.index(r"\end{table*}")
    if "wangDiffuseAwarePassive2026" not in text[:table_end]:
        anchor = "    \\cite{yeThermalNLOSFormer2026} & Thermal radiation & Thermal camera & Rough-wall convolution kernel with physics-embedded learning & 2D reconstruction and relative depth\\\\%%%% Table body\n"
        row = "    \\cite{wangDiffuseAwarePassive2026} & Ambient light & Conventional camera & Diffuse-aware attention-enhanced feature encoding & 2D reconstruction\\\\%%%% Table body\n"
        text = replace_once(text, anchor, anchor + row, "passive frontier table row")
    path.write_text(text, encoding="utf-8")


def update_learning() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if "gaoLearnedLCT2026" not in text:
        anchor = "\n\\vspace{0.8mm}\n\\noindent \\textbf{SPAD-aware physics-informed cascade learning.}"
        paragraphs = (
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Learning the light-cone inverse.}\n"
            "The original LCT obtains computational efficiency from a closed-form resampling and Wiener-deconvolution pipeline, but fixed low-pass filtering can suppress fine geometry. Gao~\\etal~proposed a learned light-cone transform (L2CT) that retains the analytic LCT structure while replacing its frequency response with high-frequency-enhanced learnable Wiener filtering and adding spatiotemporal feature-extraction and volume-projection modules~\\cite{gaoLearnedLCT2026}. Its improvement on measurements from different acquisition systems illustrates a useful middle ground between fixed analytic inverses and unconstrained end-to-end networks: the milestone operator remains recognizable, while the poorly conditioned spectral components are learned from data.\n"
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Diffusion-based transient video interpolation.}\n"
            "Dynamic NLOS systems face coupled spatial and temporal undersampling before reconstruction begins. Sun~\\etal~introduced TransVID, which uses a spatial--temporal attention encoder and latent conditional diffusion to interpolate transient videos jointly across scan position and time~\\cite{sunTransVID2026}. The method maps $16\\times16$ measurements at 4~fps to $128\\times128$ transient videos at 16~fps, providing a measurement-domain complement to ST-Mamba and TransiT: instead of reconstructing hidden video directly from sparse captures, it first synthesizes a dense, high-frame-rate transient sequence that can feed existing physical or learned inverses.\n"
        )
        text = replace_once(text, anchor, paragraphs + anchor, "PICL learning paragraph")
    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-17-optics-citation-followup.md"
    note = """# Optica and LCT citation-tracing follow-up — 17 July 2026

This follow-up adds four direct NLOS papers absent from the public repository snapshot and corrects the final venue of the transient-simulation benchmark.

- Wang et al., *Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding*, Optics Express 34(14), 26271–26289 (2026).
- Gao et al., *Learned light-cone transform for fast and accurate non-line-of-sight imaging*, Physical Review Applied 25, 044024 (2026), DOI `10.1103/jsbg-c7l5`.
- Sun et al., *Transient video interpolation for dynamic non-line-of-sight imaging*, Optics Express 34(3), 4882–4894 (2026), DOI `10.1364/OE.580550`.
- Wei et al., *Multi-surface sub-resolution non-line-of-sight imaging via transient waveform deposition*, Optics Express 33(24), 51362–51382 (2025), DOI `10.1364/OE.579004`.
- Shi et al., *Fast non-line-of-sight transient data simulation and an open benchmark dataset*: corrected from arXiv to Optics Express 33(24), 51335–51350 (2025), DOI `10.1364/OE.575753`.

The guarded synchronizers place these works in README, the homepage explorer/timeline, and the active, passive, and learned-reconstruction survey narratives. The workflow merges the canonical BibTeX records, clean-builds the survey, rejects undefined or duplicate citations, validates generated PDF text, and commits `bare_jrnl.pdf` only after all checks pass.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(note, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_passive()
    update_learning()
    update_note()
    print("Synchronized the 17 July 2026 Optica/LCT NLOS follow-up.")


if __name__ == "__main__":
    main()
