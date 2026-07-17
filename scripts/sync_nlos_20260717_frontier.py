#!/usr/bin/env python3
"""Synchronize the 17 July 2026 NLOS frontier update across public artifacts."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATE_OLD = "16 July 2026"
DATE_NEW = "17 July 2026"

MDUNET = "MDUNet: Multimodal Decoding UNet for Passive Occluder-Aided Non-line-of-sight 3D Imaging"
THERMAL = "Thermal Non-Line-of-Sight Imaging through Rough Surfaces"
PICL = "Non-line-of-sight imaging via physics-informed cascade learning"
ALLDAY = "All-day non-line-of-sight imaging based on Si-SPAD and phase-congruency-based structured ε-regularization"
CONSUMER = "Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling"
GERAF = "Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals"
DENALI = "DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs"


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
    text = text.replace(f"Update run: {DATE_OLD}", f"Update run: {DATE_NEW}")

    rows = [
        (MDUNET, f"| 2026 | [{MDUNET}](https://doi.org/10.1109/WACV61042.2026.00053) — Raji, Murray-Bruce | WACV 2026 | Jointly reconstructs a 3D hidden-occluder SDF/mesh and a 2D radiosity image of non-occluding content from one ordinary soft-shadow photograph. Shared latent features couple the two decoder paths, delivering over 100× faster inference than Soft Shadow Diffusion and over 1000× faster inference than iterative optimization while transferring from simulation to real measurements. |"),
        (THERMAL, f"| 2026 | [{THERMAL}](https://doi.org/10.1145/3811030) — Ye et al. | ACM TOG 2026 | Introduces NLOSFormer for passive thermal imaging through rough relay surfaces. An explicitly estimated convolution kernel constrains an end-to-end reconstruction network; ThermalNLOS supplies training and evaluation data, and experiments demonstrate rough-wall generalization, relative depth estimation, and dynamic reconstruction at 4 fps. |"),
        (PICL, f"| 2026 | [{PICL}](https://doi.org/10.1364/JOSAA.593401) — Zhao et al. | JOSA A 2026 | Cascades a lightweight SPAD-specific noise-separation network with a reconstruction network containing a differentiable NLOS forward model. The self-supervised physics-informed design removes the need for large paired datasets and improves robustness under mixed detector noise and low-SNR measurements. |"),
        (ALLDAY, f"| 2026 | [{ALLDAY}](https://doi.org/10.1016/j.optlaseng.2026.109919) — Yin et al. | Optics and Lasers in Engineering 2026 | Co-designs a detector-aware Si-SPAD system and phase-congruency structured regularization for extreme ambient light. The system reports an 18× SBR gain over InGaAs-SPAD capture and demonstrates 200 m NLOS imaging under 94,314 lx illumination with 4 cm lateral and 1 cm axial resolution. |"),
    ]
    anchor = "|------|-------|----------------|----------------|\n"
    insertion = ""
    for title, row in rows:
        if f"[{title}]" not in text:
            insertion += row + "\n"
    if insertion:
        text = replace_once(text, anchor, anchor + insertion, "README latest-table")

    text = replace_line_containing(
        text,
        f"[{CONSUMER}]",
        f"| 2026 | [{CONSUMER}](https://doi.org/10.1038/s41586-026-10502-x) — Somasundaram et al. | Nature 2026 | Demonstrates plug-and-play NLOS on smartphone-grade consumer LiDAR through motion-induced aperture sampling and multi-frame fusion, supporting hidden 3D reconstruction, single/multi-object tracking, and camera localization with off-the-shelf hardware. |",
        "consumer-LiDAR README correction",
    )
    text = replace_line_containing(
        text,
        f"[{GERAF}]",
        f"| 2026 | [{GERAF}](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_Radar_Signals_CVPR_2026_paper.html) — Lu et al. | CVPR 2026 | GeRaF 2.0 combines visible exterior geometry with NLOS RF propagation in a unified neural field, stabilizing signed-distance optimization and producing physically consistent visible and hidden surfaces. |",
        "GeRaF README correction",
    )
    text = replace_line_containing(
        text,
        f"[{DENALI}]",
        f"| 2026 | [{DENALI}](https://openaccess.thecvf.com/CVPR2026?day=2026-06-05) — Behari et al. | CVPR 2026 | Provides a large-scale low-cost LiDAR space-time-histogram dataset and benchmark for data-driven NLOS spatial reasoning, lowering the barrier to learning with commodity depth sensors. |",
        "DENALI README correction",
    )

    if "2026 ── Zhao et al.: PICL" not in text:
        marker = "\n```\n\n---\n\n## Taxonomy"
        block = (
            "2026 ── Zhao et al.: PICL — SPAD-aware denoising cascaded with self-supervised differentiable-physics reconstruction [JOSA A]\n"
            "   │     Ye et al.: NLOSFormer — real-time thermal NLOS through rough surfaces with explicit kernel estimation [ACM TOG]\n"
            "   │     Yin et al.: all-day Si-SPAD NLOS — 200 m reconstruction under 94,314 lx ambient illumination [Optics and Lasers in Engineering]\n"
            "   │     Raji & Murray-Bruce: MDUNet — fast joint 2D/3D passive computational periscopy [WACV]\n"
            "   │     Somasundaram et al.: consumer-LiDAR NLOS via motion-induced aperture sampling [Nature]\n"
            "   │     Lu et al. and Behari et al.: RF geometry reconstruction and low-cost-LiDAR spatial-reasoning benchmarks [CVPR]\n"
        )
        text = replace_once(text, marker, "\n" + block + "```\n\n---\n\n## Taxonomy", "README timeline ending")

    path.write_text(text, encoding="utf-8")


def paper_object(title: str, authors: str, venue: str, url: str, cat: str, key: str) -> str:
    return f'      {{cat:"{cat}",title:"{title}",authors:"{authors}",year:2026,venue:"{venue}",url:"{url}",key:"{key}"}},'


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(DATE_OLD, DATE_NEW)

    objects = [
        (MDUNET, paper_object(MDUNET, "Raji and Murray-Bruce", "WACV 2026", "https://doi.org/10.1109/WACV61042.2026.00053", "latest passive learning", "A shared encoder and specialized 3D-SDF and 2D-radiosity decoder paths jointly recover hidden occluding geometry and non-occluding content from one soft-shadow image, transferring from simulation to real measurements while greatly reducing inference time.")),
        (THERMAL, paper_object(THERMAL, "Ye et al.", "ACM TOG 2026", "https://doi.org/10.1145/3811030", "latest passive learning modality dataset", "NLOSFormer explicitly estimates a rough-wall thermal transport kernel and uses it to guide reconstruction; ThermalNLOS supports training, while experiments demonstrate cross-wall generalization, relative depth estimation, and dynamic reconstruction at 4 fps.")),
        (PICL, paper_object(PICL, "Zhao et al.", "JOSA A 2026", "https://doi.org/10.1364/JOSAA.593401", "latest active learning", "PICL cascades SPAD-specific mixed-noise separation with self-supervised reconstruction embedding a differentiable forward model, improving low-SNR robustness without requiring a large paired NLOS dataset.")),
        (ALLDAY, paper_object(ALLDAY, "Yin et al.", "Optics and Lasers in Engineering 2026", "https://doi.org/10.1016/j.optlaseng.2026.109919", "latest active", "A detector-aware Si-SPAD design and phase-congruency structured regularizer enable 200 m active NLOS imaging under 94,314 lx ambient light, with an 18× SBR improvement over InGaAs-SPAD capture.")),
    ]
    inserted = 0
    new_lines = ""
    for title, obj in objects:
        if f'title:"{title}"' not in text:
            new_lines += obj + "\n"
            inserted += 1
    if new_lines:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + new_lines, "homepage paper array")

    corrected = {
        CONSUMER: paper_object(CONSUMER, "Somasundaram et al.", "Nature 2026", "https://doi.org/10.1038/s41586-026-10502-x", "latest active modality", "Motion-induced aperture sampling and multi-frame fusion bring hidden 3D reconstruction, tracking, and camera localization to smartphone-grade consumer LiDAR."),
        GERAF: paper_object(GERAF, "Lu, Shanbhag, Al Hassanieh", "CVPR 2026", "https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_Radar_Signals_CVPR_2026_paper.html", "latest modality learning", "GeRaF 2.0 uses visible exterior geometry as a physical prior for RF propagation and stable neural-SDF reconstruction of geometry inside enclosed spaces."),
        DENALI: paper_object(DENALI, "Behari et al.", "CVPR 2026", "https://openaccess.thecvf.com/CVPR2026?day=2026-06-05", "latest dataset modality learning", "A large-scale low-cost-LiDAR space-time-histogram dataset and benchmark for learned NLOS spatial reasoning."),
    }
    for title, obj in corrected.items():
        text = replace_line_containing(text, f'title:"{title}"', obj, f"homepage correction for {title}")

    if inserted:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
        match = pattern.search(text)
        if not match:
            raise RuntimeError("Homepage tracked-count anchor is missing")
        count = int(match.group(2)) + inserted
        text = pattern.sub(lambda m: f"{m.group(1)}{count}{m.group(3)}", text, count=1)

    pattern_2026 = re.compile(r'^\s*<div class="tl"><div class="year">2026</div>.*$', re.MULTILINE)
    new_2026 = '      <div class="tl"><div class="year">2026</div><div class="tl-body"><strong>Physics-informed cascades, all-day SPAD operation, rough-wall thermal NLOS, learned computational periscopy, consumer LiDAR, arbitrary relays, and RF geometry</strong><p>The frontier moved decisively toward deployable hidden-scene sensing: PICL couples SPAD-specific noise separation with a differentiable forward model; Si-SPAD and phase-congruency regularization sustain 200 m active imaging under intense daylight; NLOSFormer reconstructs dynamic thermal scenes through rough walls; MDUNet jointly decodes hidden 3D occluders and 2D radiosity from ordinary soft-shadow photographs; motion-induced aperture sampling enables smartphone-grade LiDAR NLOS; Gaussian transient rendering and CUDA methods handle arbitrary relay geometry; and CVPR work advances RF reconstruction and low-cost-LiDAR spatial reasoning.</p></div></div>'
    if len(pattern_2026.findall(text)) != 1:
        raise RuntimeError("Expected exactly one 2026 homepage timeline row")
    text = pattern_2026.sub(new_2026, text, count=1)
    path.write_text(text, encoding="utf-8")


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")
    if "yeThermalNLOSFormer2026" not in text:
        anchor = "\n\n\n\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Interferometer}"
        paragraph = (
            "\n\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Thermal NLOS through rough relay surfaces.}\n"
            "Thermal cameras remove the need for external illumination by sensing radiation emitted by hidden targets, but rough relay walls strongly mix the measured spatial signal. Ye~\\etal~formulated this transport as a convolution and proposed NLOSFormer, which explicitly estimates the corresponding kernel and uses it to guide an end-to-end reconstruction network~\\cite{yeThermalNLOSFormer2026}. The accompanying ThermalNLOS dataset and geometry-aware augmentation improve generalization across wall materials. Experiments further demonstrate relative depth estimation and dynamic thermal NLOS reconstruction at 4~fps, extending passive thermal imaging beyond the reflective-surface assumptions of earlier systems.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "passive interferometer heading")
    if "rajiMDUNet2026" not in text:
        anchor = "\n\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Polarizer}"
        paragraph = (
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Fully learned multimodal computational periscopy.}\n"
            "Recent occluder-aided passive methods recover both the hidden occluding geometry and the radiance distribution of non-occluding content. Raji and Murray-Bruce proposed MDUNet, whose shared encoder and specialized 3D-SDF and 2D-radiosity decoder paths jointly infer these representations from a single soft-shadow photograph~\\cite{rajiMDUNet2026}. Compared with the preceding hybrid diffusion and physics pipeline, the fully trained model substantially reduces inference time while transferring from simulation to real measurements under changing ambient illumination, marking a shift toward direct multimodal passive reconstruction.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "passive polarizer heading")
    table_anchor = "    \\cite{zhang2025passive} & Ambient light & Conventional camera & Modulated light transport intensity &  2D/3D reconstruction\\\\%%%% Table body\n"
    additions = ""
    if "\\cite{rajiMDUNet2026}" not in text[:text.index(r"\end{table*}")]:
        additions += "    \\cite{rajiMDUNet2026} & Ambient light & Conventional camera & Soft-shadow occlusion with coupled learned 2D/3D decoding & Joint 2D radiosity and 3D occluder reconstruction\\\\%%%% Table body\n"
    if "\\cite{yeThermalNLOSFormer2026}" not in text[:text.index(r"\end{table*}")]:
        additions += "    \\cite{yeThermalNLOSFormer2026} & Thermal radiation & Thermal camera & Rough-wall convolution kernel with physics-embedded learning & 2D reconstruction and relative depth\\\\%%%% Table body\n"
    if additions:
        text = replace_once(text, table_anchor, table_anchor + additions, "passive table final row")
    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    table = text[:text.index(r"\end{table*}")]
    if "yinAllDayNLOS2026" not in table:
        text = replace_once(text, "liDeepNLOSUnderscanning2023}", "liDeepNLOSUnderscanning2023,yinAllDayNLOS2026}", "active SPAD citation list")
    if "\\noindent \\textbf{All-day SPAD NLOS imaging.}" not in text:
        anchor = "\n\\vspace{0.8mm}\n\\noindent \\textbf{Active Focusing for High Resolution.}"
        paragraph = (
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{All-day SPAD NLOS imaging.}\n"
            "Yin~\\etal~co-designed detector selection and reconstruction for active NLOS under extreme daylight~\\cite{yinAllDayNLOS2026}. A SPAD model incorporating photon-detection efficiency and timing jitter motivates the use of a Si-SPAD, while phase-congruency-based structured $\\epsilon$-regularization separates coherent object structure from Poisson and background noise in the virtual phasor field. The resulting system reports an 18-fold SBR increase over InGaAs-SPAD capture and reconstructs targets at 200~m under 94,314~lx ambient illumination, connecting phasor-field robustness with hardware-level detector optimization for continuous outdoor operation.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "active focusing heading")
    path.write_text(text, encoding="utf-8")


def update_learning() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if "zhaoPICL2026" not in text:
        anchor = "\nAnother example of exploiting deep learning to promote the development of NLOS imaging is LiDAR-based imaging"
        paragraph = (
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{SPAD-aware physics-informed cascade learning.}\n"
            "Zhao~\\etal~addressed the coupling between detector noise and ill-posed transient inversion with physics-informed cascade learning (PICL)~\\cite{zhaoPICL2026}. A lightweight first network separates SPAD-specific dark-count, timing-jitter, and mixed interference components, after which a second network reconstructs the hidden scene while embedding a differentiable forward model. Because physical measurement consistency supplies self-supervision, PICL avoids dependence on a large paired NLOS dataset and provides a direct bridge from trainable inverse kernels toward hardware-aware, noise-adaptive reconstruction.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "LiDAR learning paragraph")
    path.write_text(text, encoding="utf-8")


def update_new_scenes() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")
    if "somasundaramConsumerLiDAR2026" not in text:
        anchor = "\n\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Radar-Based NLOS Imaging}"
        subsection = (
            "\n\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Consumer LiDAR and Low-Cost Spatial Reasoning}\n"
            "\\subsection{Consumer LiDAR and Low-Cost Spatial Reasoning}\n"
            "Research-grade transient systems have traditionally required high-power lasers, dense calibrated scanning, and expensive timing electronics. Somasundaram~\\etal~introduced a motion-induced aperture-sampling model that unifies object shape, object motion, and camera motion, enabling multi-frame NLOS reconstruction, tracking, and camera localization with smartphone-grade consumer LiDAR~\\cite{somasundaramConsumerLiDAR2026}. This Nature result turns previously harmful motion and low spatial resolution into a synthetic aperture and marks a shift from laboratory NLOS hardware toward plug-and-play sensing.\n\n"
            "Low-cost sensing also changes the role of datasets and cross-modal priors. DENALI provides space--time histograms and spatial-reasoning annotations for commodity LiDAR, establishing a CVPR benchmark for learned NLOS reasoning~\\cite{behariDENALI2026}. In RF imaging, GeRaF~2.0 combines visible line-of-sight geometry outside an enclosure with radar propagation inside it, using the exterior geometry to regularize neural signed-distance reconstruction of hidden surfaces~\\cite{luSeeingThroughBoxes2026}. Together these works show that deployable NLOS increasingly couples inexpensive measurements with motion, visible-scene geometry, and learned priors rather than relying only on denser transient acquisition.\n"
        )
        text = replace_once(text, anchor, subsection + anchor, "radar section heading")
    path.write_text(text, encoding="utf-8")


def update_main_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = path.read_text(encoding="utf-8")
    text = text.replace("150+ NLOS papers", "190+ NLOS papers")
    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-17-mdunet-cvpr-venue-patch.md"
    text = path.read_text(encoding="utf-8")
    if "## Integration status" not in text:
        status = (
            "\n## Integration status\n\n"
            "Applied on 17 July 2026 together with three additional verified frontier papers: PICL (JOSA A), NLOSFormer thermal imaging through rough surfaces (ACM TOG), and all-day Si-SPAD NLOS imaging (Optics and Lasers in Engineering). README, homepage, survey sections, consolidated bibliography, and the regenerated PDF are validated by the accompanying GitHub Actions workflow.\n"
        )
        text = replace_once(text, "# NLOS literature update patch — 17 July 2026\n", "# NLOS literature update patch — 17 July 2026\n" + status, "patch-note title")
    text = text.replace("No claim is made here that `bare_jrnl.pdf` has already been regenerated; the binary remains unchanged until this patch is applied and compiled.", "The synchronization workflow applies this patch, performs a clean LaTeX/BibTeX build, validates the generated bibliography and PDF text, and commits the regenerated `bare_jrnl.pdf`.")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_passive()
    update_active()
    update_learning()
    update_new_scenes()
    update_main_tex()
    update_note()
    print("Synchronized the 17 July 2026 NLOS frontier update across public and survey artifacts.")


if __name__ == "__main__":
    main()
