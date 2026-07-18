#!/usr/bin/env python3
"""Synchronize verified 18 July 2026 NLOS citation-tracing additions."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATE = "18 July 2026"

PAPERS = [
    {
        "title": "Adaptive Spiral Scanning for Confocal Non-Line-of-Sight Imaging",
        "authors": "Oyama et al.",
        "year": 2026,
        "venue": "IEEE OJSP 2026",
        "url": "https://doi.org/10.1109/OJSP.2026.3688052",
        "cat": "latest active acquisition",
        "key": "oyamaAdaptiveSpiralNLOS2026",
        "summary": "Dynamically shifts an Archimedean spiral toward relay-wall regions with strong measured return intensity and applies Voronoi density compensation to correct the resulting nonuniform sampling, extending transient-sinogram acquisition from fixed circular trajectories to adaptive measurement allocation.",
    },
    {
        "title": "Submillimeter non-line-of-sight ranging and imaging via cost-effective FMCW interferometry",
        "authors": "Liang et al.",
        "year": 2026,
        "venue": "Photonics Research 2026",
        "url": "https://doi.org/10.1364/PRJ.595776",
        "cat": "latest active coherent",
        "key": "liangFMCWNLOS2026",
        "summary": "Uses a dual-path FMCW interferometer with fixed-delay fiber calibration and dynamic temporal phase subdivision to compensate sweep nonlinearity, demonstrating 450-um ranging resolution, millimeter-scale 3D NLOS imaging, and operation under more than 8 klux ambient illumination.",
    },
    {
        "title": "Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography",
        "authors": "Wang et al.",
        "year": 2026,
        "venue": "Opto-Electronic Science 2026",
        "url": "https://doi.org/10.29026/oes.2026.260007",
        "cat": "latest active long-range",
        "key": "wangLaserReflectiveTomography2026",
        "summary": "Treats the diffuse relay wall as a natural beam expander and combines single-point third-bounce detection with multi-angle laser reflective tomography. The scanning-free system reports roughly 91x faster acquisition, 3.3-km operation, and better-than-3-cm resolution in about three minutes.",
    },
    {
        "title": "Non-confocal non-line-of-sight imaging using frequency-domain phase compensation with the reference function",
        "authors": "Yu et al.",
        "year": 2026,
        "venue": "Optics Express 2026",
        "url": "https://doi.org/10.1364/OE.580027",
        "cat": "latest active reconstruction",
        "key": "yuNonconfocalPhaseCompensation2026",
        "summary": "Transfers a single-input/multiple-output millimeter-wave frequency-domain imaging formulation to optical non-confocal NLOS and uses reference-function phase compensation plus FFT reconstruction to reduce artifacts, shape distortion, and computation.",
    },
    {
        "title": "Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging",
        "authors": "Zhang et al.",
        "year": 2026,
        "venue": "Optics Express 2026",
        "url": "https://doi.org/10.1364/OE.587111",
        "cat": "latest passive reconstruction",
        "key": "zhangStructureGuidedATV2026",
        "summary": "Derives spatially varying total-variation weights from a preliminary hidden-scene estimate, automatically balancing edge preservation and noise suppression for conventional-camera passive NLOS without manual regularization tuning.",
    },
    {
        "title": "Non-Line-of-Sight Imaging via Sparse Bayesian Learning Deconvolution",
        "authors": "Tian et al.",
        "year": 2026,
        "venue": "Photonics 2026",
        "url": "https://doi.org/10.3390/photonics13010053",
        "cat": "latest active reconstruction",
        "key": "tianSparseBayesianNLOS2026",
        "summary": "Introduces a geometry-agnostic sparse Bayesian transient-restoration front end before LCT or f-k migration, suppressing photon background and instrument-response blur while preserving physically meaningful multipath returns.",
    },
    {
        "title": "Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation",
        "authors": "Zhou et al.",
        "year": 2026,
        "venue": "Physical Review Letters 2026",
        "url": "https://doi.org/10.1103/kd8v-fykm",
        "cat": "latest active single-pixel",
        "key": "zhouPolarizationSpeckleNLOS2026",
        "summary": "Modulates polarization to generate diverse rough-wall speckle illuminations and recovers hidden scenes with a single-pixel detector, enabling scanning-free millimeter-resolution keyhole imaging with noninvasive memory-effect calibration.",
    },
    {
        "title": "High-resolution Fourier single-pixel non-line-of-sight imaging employing diffusion model",
        "authors": "Fu et al.",
        "year": 2026,
        "venue": "Optics and Lasers in Engineering 2026",
        "url": "https://doi.org/10.1016/j.optlaseng.2026.109724",
        "cat": "latest learned single-pixel",
        "key": "fuFourierSinglePixelDiffusion2026",
        "summary": "Uses measured low-frequency Fourier coefficients as a consistency constraint inside diffusion sampling, restoring high-frequency hidden-scene detail at sampling rates as low as 3 percent under strong multilayer scattering.",
    },
    {
        "title": "Multiple-object passive non-line-of-sight imaging",
        "authors": "Chen et al.",
        "year": 2026,
        "venue": "Frontiers of Computer Science 2026",
        "url": "https://doi.org/10.1007/s11704-025-40887-3",
        "cat": "latest passive learning",
        "key": "chenMultipleObjectPassiveNLOS2026",
        "summary": "Introduces a nested U-Net multi-attention model with channel, spatial, and self-attention plus multi-branch supervision to reconstruct passive infrared scenes containing one to three simultaneously hidden objects.",
    },
]


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


def insert_line_before(text: str, needle: str, new_line: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {label} line containing {needle!r}, found {len(matches)}")
    lines.insert(matches[0], new_line.rstrip("\n") + "\n")
    return "".join(lines)


def insert_after_heading_block(text: str, heading: str, block: str, label: str) -> str:
    marker = f"\\noindent \\textbf{{{heading}}}"
    starts = [m.start() for m in re.finditer(re.escape(marker), text)]
    if len(starts) != 1:
        raise RuntimeError(f"Expected one {label} heading, found {len(starts)}")
    end = text.find("\n\n", starts[0])
    if end < 0:
        raise RuntimeError(f"Could not locate paragraph end after {label}")
    return text[: end + 2] + block.strip("\n") + "\n\n" + text[end + 2 :]


def append_timeline_sentence(text: str, year: int, marker: str, sentence: str) -> str:
    if marker in text:
        return text
    lines = text.splitlines(keepends=True)
    needle = f'<div class="year">{year}</div>'
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    line = lines[matches[0]]
    closing = "</p></div></div>"
    if closing not in line:
        raise RuntimeError(f"Homepage timeline row for {year} has an unexpected structure")
    ending = "\n" if line.endswith("\n") else ""
    core = line[:-1] if ending else line
    core = core.replace(closing, " " + sentence + closing, 1)
    lines[matches[0]] = core + ending
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("17 July 2026", DATE)

    insertion = ""
    for paper in PAPERS:
        if f"[{paper['title']}]" in text:
            continue
        insertion += (
            f"| {paper['year']} | [{paper['title']}]({paper['url']}) - {paper['authors']} | "
            f"{paper['venue']} | {paper['summary']} |\n"
        )
    if insertion:
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + insertion, "README latest-additions table")

    timeline_marker = "18 July 2026 core-citation tracing"
    if timeline_marker not in text:
        marker = "\n```\n\n---\n\n## Taxonomy"
        timeline = (
            "2026 -- Oyama et al.: adaptive spiral relay-wall sampling allocates limited confocal measurements from observed return intensity [IEEE OJSP]\n"
            "   |     Liang et al.: cost-effective FMCW interferometry reaches submillimeter ranging and millimeter-scale NLOS imaging [Photonics Research]\n"
            "   |     Wang et al.: scanning-free laser reflective tomography demonstrates 3.3-km hidden imaging with centimeter resolution [Opto-Electronic Science]\n"
            "   |     Yu et al.: reference-function frequency-domain phase compensation accelerates non-confocal reconstruction [Optics Express]\n"
            "   |     Tian et al.: sparse Bayesian transient restoration improves LCT and f-k inputs under photon and hardware limits [Photonics]\n"
            "   |     Zhou et al.: polarization-speckle single-pixel modulation opens a scanning-free keyhole NLOS branch [Physical Review Letters]\n"
            "   |     Zhang et al.: structure-guided adaptive total variation removes manual passive-NLOS regularization tuning [Optics Express]\n"
            "   |     Fu et al.: a diffusion prior restores high-frequency Fourier single-pixel measurements at extreme undersampling [Optics and Lasers in Engineering]\n"
            "   |     Chen et al.: multi-attention passive reconstruction handles several simultaneously hidden objects [Frontiers of Computer Science]\n"
            "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
        )
        text = replace_once(text, marker, "\n" + timeline + "```\n\n---\n\n## Taxonomy", "README timeline ending")

    path.write_text(text, encoding="utf-8")


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("17 July 2026", DATE)

    new_lines = ""
    inserted = 0
    for paper in PAPERS:
        if f'title:"{paper["title"]}"' in text:
            continue
        new_lines += paper_object(paper) + "\n"
        inserted += 1
    if new_lines:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + new_lines, "homepage paper array")
    if inserted:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
        match = pattern.search(text)
        if not match:
            raise RuntimeError("Homepage tracked-count anchor is missing")
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + inserted}{m.group(3)}", text, count=1)

    text = append_timeline_sentence(
        text,
        2026,
        "Adaptive spiral sampling",
        "Adaptive spiral sampling redirects confocal measurements toward measured return intensity; calibrated FMCW interferometry introduces submillimeter coherent ranging; laser reflective tomography removes relay-wall scanning at 3.3 km; reference-function phase compensation accelerates non-confocal inversion; sparse Bayesian deconvolution improves transient inputs; polarization speckles enable scanning-free single-pixel keyhole imaging; adaptive-TV and multi-attention models broaden passive recovery; and diffusion priors extend Fourier single-pixel NLOS under extreme undersampling.",
    )
    path.write_text(text, encoding="utf-8")


def add_active_table_keys(text: str) -> str:
    keys = [
        "oyamaAdaptiveSpiralNLOS2026",
        "liangFMCWNLOS2026",
        "wangLaserReflectiveTomography2026",
        "yuNonconfocalPhaseCompensation2026",
        "tianSparseBayesianNLOS2026",
        "zhouPolarizationSpeckleNLOS2026",
    ]
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if "& Pulsed laser & SPAD & Time of fight &  3D reconstruction" in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one active-SPAD table row, found {len(matches)}")
    line = lines[matches[0]]
    match = re.search(r"\\cite\{([^}]*)\}", line)
    if not match:
        raise RuntimeError("Could not find citation list in active-SPAD table row")
    current = [k.strip() for k in match.group(1).split(",") if k.strip()]
    changed = False
    for key in keys:
        if key not in current:
            current.append(key)
            changed = True
    if changed:
        line = line[: match.start(1)] + ",".join(current) + line[match.end(1) :]
        lines[matches[0]] = line
    return "".join(lines)


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    text = add_active_table_keys(text)

    additions = [
        (
            "Adaptive spiral relay-wall sampling.",
            "Super-field-of-view reconstruction by translated PSFs.",
            r"""
\vspace{0.8mm}
\noindent \textbf{Adaptive spiral relay-wall sampling.}
Fixed circular and spiral trajectories reduce acquisition relative to dense raster scanning, but they spend the same sampling budget regardless of where a localized hidden target returns useful photons. Oyama~\etal~proposed Dynamic Archimedean Spiral Confocal NLOS, which updates the spiral center from sequential estimates of relay-wall return intensity and concentrates later measurements on informative regions~\cite{oyamaAdaptiveSpiralNLOS2026}. Voronoi density compensation corrects the nonuniform sampling induced by this adaptive path before transient-sinogram reconstruction. The method directly continues C$^2$NLOS from predefined structured paths toward closed-loop measurement allocation.
""",
        ),
        (
            "Sparse Bayesian transient restoration.",
            "Model-decomposition reconstruction from sparse transients.",
            r"""
\vspace{0.8mm}
\noindent \textbf{Sparse Bayesian transient restoration.}
Analytic inverses cannot recover temporal detail that has already been buried by photon noise or broadened by the instrument response. Tian~\etal~introduced sparse Bayesian learning as a geometry-independent deconvolution stage before LCT or $f$--$k$ migration~\cite{tianSparseBayesianNLOS2026}. Adaptive sparsity inference suppresses background fluctuations while retaining physically plausible multipath peaks, improving boundary sharpness and robustness without changing the acquisition geometry or downstream reconstruction. This signal-domain route complements spatial undersampling methods by treating transient fidelity itself as a deployment bottleneck.
""",
        ),
        (
            "Reference-function phase compensation for non-confocal capture.",
            "Stereo relay-wall acquisition.",
            r"""
\vspace{0.8mm}
\noindent \textbf{Reference-function phase compensation for non-confocal capture.}
Non-confocal acquisition improves photon use and capture speed but produces bistatic path geometry that is less convenient for confocal Fourier inverses. Yu~\etal~transferred a single-input/multiple-output frequency-domain imaging formulation from millimeter-wave sensing and derived a reference-function phase compensation method for optical NLOS~\cite{yuNonconfocalPhaseCompensation2026}. FFT implementation reduces computation while measured and simulated results show fewer artifacts and less geometric distortion. The work provides an explicit RF-to-optical algorithmic bridge rather than using radar only as an application analogy.
""",
        ),
        (
            "Scanning-free laser reflective tomography.",
            "Compact kilometer-range NLOS imaging.",
            r"""
\vspace{0.8mm}
\noindent \textbf{Scanning-free laser reflective tomography.}
Long-range transient systems usually trade spatial resolution against the number of relay-wall scan positions. Wang~\etal~instead use the diffuse wall as a natural beam expander, record third-bounce light with a single detector, and recover the hidden target from angular measurements generated by laser reflective tomography~\cite{wangLaserReflectiveTomography2026}. Indoor experiments report roughly twice the resolution and $91\times$ the acquisition speed of point scanning; an outdoor experiment reconstructs targets at 3.3~km with better than 3~cm resolution in about three minutes. This result removes relay-wall raster scanning from the kilometer-scale branch rather than merely accelerating its inverse.
""",
        ),
        (
            "Polarization-speckle single-pixel imaging.",
            "Active Focusing for High Resolution.",
            r"""
\vspace{0.8mm}
\noindent \textbf{Polarization-speckle single-pixel imaging.}
Zhou~\etal~introduced polarization as an illumination-coding degree of freedom for scanning-free NLOS imaging~\cite{zhouPolarizationSpeckleNLOS2026}. Different incident polarization states produce diverse speckle patterns after interaction with the rough relay surface, and a single-pixel detector measures the corresponding hidden-scene responses. The system achieves millimeter-scale keyhole reconstruction and uses the angular memory effect for noninvasive calibration, expanding single-pixel NLOS beyond spatial-mask and temporal-coding designs.
""",
        ),
    ]
    for heading, anchor, paragraph in additions:
        if heading not in text:
            text = insert_after_heading_block(text, anchor, paragraph, anchor)

    if "Cost-effective FMCW interferometry." not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Cost-effective FMCW interferometry.}
Liang~\etal~developed a coherent NLOS ranging and imaging system based on frequency-modulated continuous-wave interferometry rather than pulsed photon timing~\cite{liangFMCWNLOS2026}. A polarization-maintaining optical-delay fiber supplies a fixed Mach--Zehnder calibration path, and dynamic temporal phase subdivision estimates and compensates laser-sweep nonlinearity without an optical frequency comb. The reported 1.8~ps effective temporal resolution supports 450~$\mu$m ranging resolution, 1~mm axial and 2.4~mm lateral imaging resolution at a 110~cm hidden distance, including measurements above 8~klux ambient illumination. This adds a cost-conscious coherent branch between superheterodyne interferometry and SPAD ToF systems.

"""
        marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Laser and conventional camera}"
        text = replace_once(text, marker, paragraph + marker, "laser-and-camera subsection")

    path.write_text(text, encoding="utf-8")


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")

    if "Structure-guided adaptive total variation." not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Structure-guided adaptive total variation.}
A fixed TV weight cannot simultaneously preserve weak boundaries and suppress spatially varying passive-NLOS noise across different scenes. Zhang~\etal~derive a guidance map from a preliminary reconstruction and use it to assign spatially varying regularization strengths~\cite{zhangStructureGuidedATV2026}. The resulting parameter-free SG-ATV solver removes manual tuning while retaining the conventional-camera light-transport model, showing how classical computational periscopy can remain competitive through scene-adaptive optimization rather than learned priors alone.
"""
        text = insert_after_heading_block(text, "Long-range passive NLOS under severe background.", paragraph, "long-range passive paragraph")

    if "Multi-object passive reconstruction." not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Multi-object passive reconstruction.}
Most learned passive systems are trained and evaluated with one dominant hidden target. Chen~\etal~introduced a nested U-Net multi-attention architecture for infrared scenes containing one to three hidden objects~\cite{chenMultipleObjectPassiveNLOS2026}. Channel, spatial, and self-attention emphasize complementary transport features, while multiple decoder branches and joint supervision stabilize reconstruction at different semantic scales. The work broadens passive deep reconstruction from isolated silhouettes toward scenes with variable object count and mutual signal mixing.
"""
        text = insert_after_heading_block(text, "Fully learned multimodal computational periscopy.", paragraph, "MDUNet paragraph")

    rows = [
        ("zhangStructureGuidedATV2026", r"    \cite{zhangStructureGuidedATV2026} & Ambient light & Conventional color camera & Intensity with structure-guided adaptive TV & Parameter-free 2D reconstruction\\%%%% Table body"),
        ("chenMultipleObjectPassiveNLOS2026", r"    \cite{chenMultipleObjectPassiveNLOS2026} & Infrared radiation & Infrared camera & Learned multi-attention transport features & Multiple-object 2D reconstruction\\%%%% Table body"),
    ]
    for key, row in rows:
        if f"\\cite{{{key}}} &" not in text:
            text = insert_line_before(text, "\\cite{rajiMDUNet2026} &", row, "passive technology table")

    if "chenMultipleObjectPassiveNLOS2026" not in text.split("\\caption{NLOS imaging based on deep learning", 1)[-1]:
        row = r"    \cite{chenMultipleObjectPassiveNLOS2026} & End-to-End: nested U-Net with multi-attention & Infrared scattering image & Multiple hidden-object image & Passive infrared NLOS with variable object count & Experimental and synthetic data\\ %%%%"
        text = insert_line_before(text, "\\cite{du2025passive} &", row, "deep-learning table")

    path.write_text(text, encoding="utf-8")


def update_learning() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if "Diffusion-prior Fourier single-pixel imaging." not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Diffusion-prior Fourier single-pixel imaging.}
Fu~\etal~combined Fourier single-pixel acquisition with a generative diffusion prior for hidden imaging under severe scattering and extreme undersampling~\cite{fuFourierSinglePixelDiffusion2026}. Measured low-frequency Fourier coefficients remain enforced as a data-consistency constraint during iterative denoising, while the learned prior supplies the missing high-frequency structure. Experiments through multiple paper layers at sampling rates down to 3\% illustrate a distinct diffusion trajectory from transient-volume reconstruction: the generative prior operates directly on compressed single-pixel spectral measurements.
"""
        text = insert_after_heading_block(text, "Diffusion model priors.", paragraph, "diffusion-prior paragraph")
    path.write_text(text, encoding="utf-8")


def update_main() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = path.read_text(encoding="utf-8")
    old = "This update extends coverage to include significant advances from 2022 to 2026."
    new = "This update extends coverage to include significant advances from 2022 through 18 July 2026."
    if old in text:
        text = replace_once(text, old, new, "survey update horizon")
    elif new not in text:
        raise RuntimeError("Survey update-horizon sentence is missing")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_passive()
    update_learning()
    update_main()
    print("Synchronized nine verified core-citation and modality-expansion NLOS papers.")


if __name__ == "__main__":
    main()
