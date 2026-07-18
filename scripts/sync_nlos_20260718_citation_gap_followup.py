#!/usr/bin/env python3
"""Synchronize verified citation-traced NLOS gaps across public and survey artifacts."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Learning-based NLOS imaging with Kolmogorov-Arnold network-enhanced transformer",
        "authors": "Liu et al.", "year": 2025, "venue": "Optics & Laser Technology 2025",
        "url": "https://doi.org/10.1016/j.optlastec.2025.113463",
        "cat": "latest active learning transformer transient", "key": "liuKANTransformerNLOS2025",
        "summary": "Combines a KAN-enhanced Transformer for nonlinear global transient features, convolutional attention for local detail, and EfficientSAM contour guidance, improving simulated and measured active-NLOS reconstructions.",
    },
    {
        "title": "Feature enhanced non-line-of-sight imaging using graph model in latent space",
        "authors": "Xu et al.", "year": 2025, "venue": "Optics & Laser Technology 2025",
        "url": "https://doi.org/10.1016/j.optlastec.2024.111538",
        "cat": "latest active optimization graph regularization", "key": "xuGraphLatentNLOS2025",
        "summary": "Uses a group graph-Laplacian model in a compressed latent representation as a RED-style structural regularizer, balancing detail preservation, noise suppression, and efficiency for confocal and non-confocal transients.",
    },
    {
        "title": "Non-line-of-sight imaging with adaptive artifact cancellation",
        "authors": "Zhou et al.", "year": 2025, "venue": "Optics & Laser Technology 2025",
        "url": "https://doi.org/10.1016/j.optlastec.2024.112081",
        "cat": "latest active reconstruction artifact backprojection", "key": "zhouAdaptiveArtifactCancellation2025",
        "summary": "Introduces ground-truth-independent TOF-SSIM for parameter selection and adaptively cancels backprojection artifacts by modifying and reprojecting transient histograms in confocal and non-confocal settings.",
    },
    {
        "title": "Adaptive Attention Based on Mixture Distribution for Zero-Shot Non-Line-of-Sight Imaging",
        "authors": "Zhang, Liu, Duan", "year": 2025, "venue": "IEEE Signal Processing Letters 2025",
        "url": "https://doi.org/10.1109/LSP.2025.3558458",
        "cat": "latest active optimization zero-shot attention", "key": "zhangAdaptiveMixtureZeroShot2025",
        "summary": "Models target and background residuals with a mixture distribution; dual-space adaptive weights act as zero-shot attention inside an alternating-minimization solver without paired training data.",
    },
    {
        "title": "Passive non-line-of-sight pedestrian imaging based on light transport matrix decomposition",
        "authors": "Chen et al.", "year": 2025, "venue": "Optics and Lasers in Engineering 2025",
        "url": "https://doi.org/10.1016/j.optlaseng.2025.109032",
        "cat": "latest passive infrared pedestrian transformer", "key": "chenLTMDPassiveNLOS2025",
        "summary": "Decomposes passive long-wave-infrared transport into illumination and reflection components and uses an illumination-oriented Transformer; IF-NLOS provides 33,000 images and experiments extend hidden-pedestrian imaging to 20 m.",
    },
    {
        "title": "Non-line-of-sight imaging via scalable scattering mapping using TOF cameras",
        "authors": "Fang et al.", "year": 2025, "venue": "Photonics Research 2025",
        "url": "https://doi.org/10.1364/PRJ.558736",
        "cat": "latest modality commodity tof learning", "key": "fangScalableScatteringTOF2025",
        "summary": "Uses a low-cost continuous-wave ToF camera and a learned scalable-scattering mapping to decouple object and relay-surface signatures, trained on 210,000 depth images and tested on laboratory and real walls.",
    },
    {
        "title": "Edge-aware dual-spectral NLOS imaging architecture",
        "authors": "Shi et al.", "year": 2026, "venue": "Proc. SPIE / NDTA 2025 (published 2026)",
        "url": "https://doi.org/10.1117/12.3109634",
        "cat": "latest passive dual spectral edge deployment", "key": "shiDualSpectralEdgeNLOS2026",
        "summary": "Fuses synchronized visible and long-wave-infrared measurements in an INT8 CPU pipeline, reporting 78.4 ms latency and sub-10 W operation on Jetson AGX Orin for deployable passive NLOS reconstruction.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def insert_before_once(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    return replace_once(text, marker, addition.rstrip() + "\n\n" + marker, label)


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def append_to_timeline_year(text: str, year: int, sentence: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if f'<div class="year">{year}</div>' in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    line = lines[matches[0]]
    if sentence.strip() not in line:
        closing = "</p></div></div>"
        if closing not in line:
            raise RuntimeError(f"Timeline closing marker missing for {year}")
        lines[matches[0]] = line.replace(closing, " " + sentence.strip() + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = ""
    for p in PAPERS:
        if f"[{p['title']}]" not in text:
            rows += f"| {p['year']} | [{p['title']}]({p['url']}) - {p['authors']} | {p['venue']} | {p['summary']} |\n"
    if rows:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + rows, "README latest-additions header")

    anchor = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
    lines = (
        "   |     KAN-Transformer, latent graph regularization, mixture-distribution zero-shot attention, and adaptive artifact cancellation broaden learned and optimization-based active inversion [Optics & Laser Technology / IEEE SPL]\n"
        "   |     Long-wave-infrared transport decomposition and commodity CW-ToF scattering mapping extend practical passive and low-cost depth-camera NLOS [Optics and Lasers in Engineering / Photonics Research]\n"
        "   |     Visible/LWIR dual-spectral fusion moves passive NLOS toward low-power edge deployment [SPIE NDTA]\n"
        "   |     18 July 2026 citation-gap follow-up: seven final-venue records integrated across public, survey, bibliography, and build artifacts\n"
    )
    if "18 July 2026 citation-gap follow-up" not in text:
        text = replace_once(text, anchor, lines + anchor, "README core-citation marker")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    additions = [paper_object(p) for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if additions:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + "\n".join(additions) + "\n", "homepage paper array")

    stat = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    match = stat.search(text)
    if not match:
        raise RuntimeError("Homepage tracked-entry statistic not found")
    count = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    if int(match.group(2)) != count:
        text = stat.sub(lambda m: m.group(1) + str(count) + m.group(3), text, count=1)

    text = append_to_timeline_year(
        text, 2025,
        "A citation-tracing follow-up added KAN-enhanced transient Transformers, latent graph/RED regularization, mixture-distribution zero-shot attention, adaptive artifact cancellation, long-range infrared transport decomposition, and commodity CW-ToF scalable-scattering mapping.",
    )
    text = append_to_timeline_year(
        text, 2026,
        "Dual-spectral visible/LWIR fusion with quantized CPU inference demonstrated a low-power edge-deployment path for passive NLOS.",
    )
    path.write_text(text, encoding="utf-8")


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")
    block = r"""\vspace{0.8mm}
\noindent \textbf{Long-range infrared transport decomposition.}
Chen~\etal~extended passive NLOS pedestrian imaging to long-wave infrared sensing and explicitly decomposed the light-transport matrix into illumination and reflection components~\cite{chenLTMDPassiveNLOS2025}. The illumination component restores gross brightness, while the reflection component sharpens contours; an illumination-oriented Transformer restricts contextual modeling to informative regions instead of propagating low-SNR background. The accompanying IF-NLOS dataset contains 33,000 images across distances, relay angles, and illumination conditions, and experiments reach hidden-pedestrian ranges of 20~m. This work connects computational-periscopy-style transport estimation with self-emitted thermal cues and task-specific long-range perception.

\vspace{0.8mm}
\noindent \textbf{Dual-spectral passive NLOS at the edge.}
Shi~\etal~combined synchronized visible and long-wave-infrared relay observations with attention-based dual-branch fusion and INT8 inference~\cite{shiDualSpectralEdgeNLOS2026}. The CPU-oriented implementation reports 78.4~ms latency and sub-10~W power on an embedded Jetson platform. Although the conference study emphasizes deployment rather than a new light-transport inverse, it marks a useful systems trajectory: complementary spectral cues can be fused under strict latency and energy constraints instead of assuming a laboratory GPU and a single sensing band.
"""
    marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Interferometer}"
    text = insert_before_once(text, marker, block, "passive interferometer marker")
    path.write_text(text, encoding="utf-8")


def update_data_driven() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    block = r"""\vspace{0.8mm}
\noindent \textbf{KAN-enhanced transient Transformers with semantic guidance.}
Liu~\etal~combined a Kolmogorov--Arnold Network-enhanced Transformer with convolutional attention for active transient NLOS reconstruction~\cite{liuKANTransformerNLOS2025}. Learnable KAN activations model nonlinear global transport features, the convolutional branch preserves local structure, and EfficientSAM-derived contours enter through a semantic loss. The measured-data evaluation places this method in the trajectory from NLOST and TransiT toward hybrid architectures that jointly exploit global transient dependencies, local spatial evidence, and pretrained semantic priors.

\vspace{0.8mm}
\noindent \textbf{Latent graph and zero-shot mixture regularization.}
Xu~\etal~compressed the hidden volume along its relatively redundant depth profile and built a group graph-Laplacian feature extractor in the latent space~\cite{xuGraphLatentNLOS2025}. Used as a regularization-by-denoising structural term, it combines learned feature statistics with iterative measurement inversion while lowering the cost of full three-dimensional nonlocal graphs. Zhang~\etal~take a complementary training-free route: a mixture distribution separates target and background residual behavior, and dual-space adaptive weights become a zero-shot attention mechanism inside alternating minimization~\cite{zhangAdaptiveMixtureZeroShot2025}. Together these methods show that attention-like adaptivity need not be confined to supervised neural networks; it can also emerge from probabilistic residual models and optimization dual variables.

\vspace{0.8mm}
\noindent \textbf{Ground-truth-independent artifact cancellation.}
Zhou~\etal~introduced time-of-flight structural similarity (TOF-SSIM), which forward-projects a candidate hidden reconstruction and evaluates its consistency with the measured transient without requiring hidden-scene ground truth~\cite{zhouAdaptiveArtifactCancellation2025}. The resulting adaptive artifact-cancellation procedure modifies and backprojects the transient contribution associated with streaking artifacts and applies to both confocal and non-confocal data. This closes a practical gap between fast backprojection and heavier iterative solvers by making reconstruction-parameter selection and artifact suppression measurement-driven.
"""
    marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Challenges and Prospects}"
    text = insert_before_once(text, marker, block, "deep-learning challenges marker")
    path.write_text(text, encoding="utf-8")


def update_new_scenes() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")
    block = r"""\vspace{0.8mm}
\noindent \textbf{Commodity continuous-wave ToF scattering maps.}
Fang~\etal~used a low-cost continuous-wave ToF camera to acquire relay-surface intensity and depth images and proposed scalable scattering mapping (SSM) for learned decoupling of object and relay-surface scattering signatures~\cite{fangScalableScatteringTOF2025}. The study collected 210,000 depth images across polypropylene, acrylic, Lambertian, painted-door, and plaster-wall relays, and demonstrated reconstruction on laboratory objects and clothing in a corridor. Unlike picosecond transient inversion, SSM calibrates a scene-dependent degradation-to-clear mapping from commodity correlation-depth measurements, broadening deployable NLOS toward inexpensive depth cameras while making the need for coverage of new object--relay combinations explicit.
"""
    marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Radar-Based NLOS Imaging}"
    text = insert_before_once(text, marker, block, "radar section marker")
    path.write_text(text, encoding="utf-8")


def update_master_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = path.read_text(encoding="utf-8")
    marker = "\\input{article/2active.tex}"
    comment = "% 18 July 2026 citation-gap follow-up integrates seven verified active, passive, and commodity-ToF papers in the section sources.\n"
    if comment.strip() not in text:
        text = replace_once(text, marker, comment + marker, "master survey section anchor")
    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-18-citation-gap-followup.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "STATUS: STAGED — public sources and PDF have not yet been rebuilt.",
        "STATUS: SYNCHRONIZED — source artifacts were updated by the guarded workflow; PDF validity is checked before its separate commit.",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_passive()
    update_data_driven()
    update_new_scenes()
    update_master_tex()
    update_note()
    print("Synchronized seven verified citation-gap NLOS papers.")


if __name__ == "__main__":
    main()
