#!/usr/bin/env python3
"""Synchronize verified reconstruction, pose, renderer, RF, and robotics NLOS records."""
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

NEW_PUBLIC = [
    {
        "title": "Non-line-of-sight human pose estimation",
        "authors": "Xiao et al.", "year": 2026, "venue": "Optics and Lasers in Engineering 2026",
        "url": "https://doi.org/10.1016/j.optlaseng.2026.109658", "cat": "latest active semantics",
        "key": "xiaoNLOSHumanPose2026",
        "summary": "Directly estimates semantic body joints from transient-derived intensity and depth features, using a physics-based smartphone-video synthesis pipeline for training and demonstrating robust measured-data pose recovery at 1.75 m and SNR 0.13.",
    },
    {
        "title": "Frequency-domain multi-regularization-experts fusion for robust non-line-of-sight imaging",
        "authors": "Zhang et al.", "year": 2026, "venue": "Pattern Recognition 2026",
        "url": "https://doi.org/10.1016/j.patcog.2025.112914", "cat": "latest active reconstruction",
        "key": "zhangFrequencyMoENLOS2026",
        "summary": "Introduces a frequency-domain mixture of regularization experts whose gating weights are derived from optimization dual variables, combining direct-method efficiency with improved robustness and real-data albedo reconstruction.",
    },
    {
        "title": "Canny operator-based artifact identification and suppression for non-line-of-sight imaging",
        "authors": "Chen et al.", "year": 2026, "venue": "Optics and Laser Technology 2026",
        "url": "https://doi.org/10.1016/j.optlastec.2025.114542", "cat": "latest active reconstruction",
        "key": "chenCannyArtifactNLOS2026",
        "summary": "Combines Canny/morphological artifact segmentation, reference-free sharpness and residual metrics, and genetic optimization of a transient blur kernel to suppress backprojection artifacts in simulated and measured confocal and non-confocal data.",
    },
    {
        "title": "Nonconfocal non-line-of-sight imaging with specular-flight-path regularization for complex multi-orientation objects",
        "authors": "Shi et al.", "year": 2026, "venue": "Photonics Research 2026",
        "url": "https://doi.org/10.1364/PRJ.579183", "cat": "latest active reconstruction",
        "key": "shiSpecularFlightPathNLOS2026",
        "summary": "Uses local matrix analysis to identify low-redundancy specular-flight-path regions and regularizes non-confocal inversion around those paths, improving reconstruction of tilted, multi-orientation hidden objects.",
    },
    {
        "title": "Super-resolution non-line-of-sight imaging with laser pulses multiplexing",
        "authors": "Miao et al.", "year": 2026, "venue": "Optics and Lasers in Engineering 2026",
        "url": "https://doi.org/10.1016/j.optlaseng.2025.109558", "cat": "latest active hardware",
        "key": "miaoLaserPulseMultiplexingNLOS2026",
        "summary": "Uses deterministic cross-pulse sub-bin modulation and non-negative least squares to recover 64 ps transients from 704 ps photon-timing hardware, retaining benefits under severe under-scanning and extending to non-confocal arrays.",
    },
]

PUBLIC_ONLY = [
    ("Beyond lambda/2: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?", "chenBeyondLambdaEMVS2026"),
    ("Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform", "weiQuasiFresnelNLOS2025"),
    ("N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization", "shiN2LoS2025"),
    ("SuperEx: Enhancing Indoor Mapping and Exploration using Non-Line-of-Sight Perception", "gargSuperEx2025"),
    ("mitransient: Transient light transport in Mitsuba 3", "royoMitransient2025"),
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"Expected one {label}, found {n}")
    return text.replace(old, new, 1)


def insert_after_heading(text: str, heading: str, block: str) -> str:
    marker = f"\\noindent \\textbf{{{heading}}}"
    starts = [m.start() for m in re.finditer(re.escape(marker), text)]
    if len(starts) != 1:
        raise RuntimeError(f"Expected one heading {heading!r}, found {len(starts)}")
    end = text.find("\n\n", starts[0])
    if end < 0:
        raise RuntimeError(f"Paragraph end missing after {heading}")
    return text[:end+2] + block.strip("\n") + "\n\n" + text[end+2:]


def add_key_to_row(text: str, needle: str, key: str) -> str:
    lines = text.splitlines(keepends=True)
    ids = [i for i, line in enumerate(lines) if needle in line]
    if len(ids) != 1:
        raise RuntimeError(f"Expected one row matching {needle!r}, found {len(ids)}")
    i = ids[0]
    line = lines[i]
    match = re.search(r"\\cite\{([^}]*)\}", line)
    if not match:
        raise RuntimeError(f"No citation list in row {needle}")
    keys = [item.strip() for item in match.group(1).split(",") if item.strip()]
    if key not in keys:
        keys.append(key)
        lines[i] = line[:match.start(1)] + ",".join(keys) + line[match.end(1):]
    return "".join(lines)


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = ""
    for paper in NEW_PUBLIC:
        if f"[{paper['title']}]" not in text:
            rows += (
                f"| {paper['year']} | [{paper['title']}]({paper['url']}) - {paper['authors']} | "
                f"{paper['venue']} | {paper['summary']} |\n"
            )
    if rows:
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + rows, "README table header")
    text = text.replace(
        "https://opg.optica.org/oe/abstract.cfm?uri=oe-34-14-26271",
        "https://doi.org/10.1364/OE.601398",
    )
    if "18 July 2026 reconstruction/pose consistency audit" not in text:
        anchor = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
        lines = (
            "   |     Xiao et al.: semantic human-pose recovery extends active transients beyond shape reconstruction [Optics and Lasers in Engineering]\n"
            "   |     Zhang et al.: dual-variable frequency experts improve robust active inversion [Pattern Recognition]\n"
            "   |     Chen et al.: reference-free Canny-guided correction suppresses backprojection artifacts [Optics and Laser Technology]\n"
            "   |     Shi et al.: specular-flight-path priors improve non-confocal multi-orientation recovery [Photonics Research]\n"
            "   |     Miao et al.: pulse multiplexing computationally exceeds detector timing resolution [Optics and Lasers in Engineering]\n"
            "   |     18 July 2026 reconstruction/pose consistency audit: public-only RF, robotics, renderer, and Quasi-Fresnel records integrated into the survey\n"
        )
        text = replace_once(text, anchor, lines + anchor, "README audit marker")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    new_lines = "\n".join(
        paper_object(paper) for paper in NEW_PUBLIC
        if f'title:"{paper["title"]}"' not in text
    )
    if new_lines:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + new_lines + "\n", "paper array")
    text = text.replace(
        "https://opg.optica.org/oe/abstract.cfm?uri=oe-34-14-26271",
        "https://doi.org/10.1364/OE.601398",
    )
    if "Pulse multiplexing computationally exceeds detector timing resolution" not in text:
        lines = text.splitlines(keepends=True)
        ids = [i for i, line in enumerate(lines) if '<div class="year">2026</div>' in line]
        if len(ids) != 1:
            raise RuntimeError("2026 timeline row mismatch")
        closing = "</p></div></div>"
        sentence = (
            " Pulse multiplexing computationally exceeds detector timing resolution; frequency-expert and Canny-guided solvers improve robust inversion; specular-flight-path priors strengthen non-confocal recovery; and active transients advance from geometry to semantic human-pose estimation."
        )
        lines[ids[0]] = lines[ids[0]].replace(closing, sentence + closing, 1)
        text = "".join(lines)
    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    for key in [
        "miaoLaserPulseMultiplexingNLOS2026",
        "weiQuasiFresnelNLOS2025",
        "zhangFrequencyMoENLOS2026",
        "chenCannyArtifactNLOS2026",
        "shiSpecularFlightPathNLOS2026",
    ]:
        text = add_key_to_row(text, "& Pulsed laser & SPAD & Time of fight &  3D reconstruction", key)
    text = add_key_to_row(text, "& Pulsed laser & SPAD & Time of fight &  Pose estimation", "xiaoNLOSHumanPose2026")
    additions = [
        ("Miniaturized TCSPC electronics.", "Timing super-resolution by laser-pulse multiplexing.", r'''
\vspace{0.8mm}
\noindent \textbf{Timing super-resolution by laser-pulse multiplexing.}
Detector jitter and histogram bin width ordinarily impose a hard axial-resolution floor. Miao~\etal~instead exploit deterministic offsets between repeated laser pulses to build a sub-bin modulation matrix and recover fine transient histograms with non-negative least squares~\cite{miaoLaserPulseMultiplexingNLOS2026}. Their laser-pulse-multiplexing system reconstructs 64~ps transients from hardware with a native 704~ps single-photon timing resolution, remains useful when only about 5\% of relay positions are sampled, and extends to non-confocal arrays. This shifts part of the temporal-resolution burden from specialized detectors to calibrated computational modulation.
'''),
        ("Nonuniform and scaled Fourier sampling.", "Two-dimensional Quasi-Fresnel inversion.", r'''
\vspace{0.8mm}
\noindent \textbf{Two-dimensional Quasi-Fresnel inversion.}
Most fast transient inverses still allocate a three-dimensional hidden volume even when the target is effectively a surface. Wei~\etal~represent both aggregated measurements and the hidden scene as two-dimensional functions and derive a direct Quasi-Fresnel transform between them~\cite{weiQuasiFresnelNLOS2025}. The reduction in representation dimension lowers runtime and memory by orders of magnitude while preserving reconstruction quality, creating a route toward high-resolution active NLOS on mobile or embedded hardware.
'''),
        ("Sparse Bayesian transient restoration.", "Frequency-domain regularization experts.", r'''
\vspace{0.8mm}
\noindent \textbf{Frequency-domain regularization experts.}
A single spectral prior is rarely optimal across low-frequency shape, high-frequency boundaries, and scene-dependent noise. Zhang~\etal~formulate active NLOS reconstruction as a frequency-domain mixture of regularization experts and derive expert weights from optimization dual variables rather than heuristic or learned gating~\cite{zhangFrequencyMoENLOS2026}. The resulting solver retains direct-method computational efficiency while improving real-data albedo fidelity and robustness over analytic, iterative, and representative learned baselines.

\vspace{0.8mm}
\noindent \textbf{Reference-free artifact identification and correction.}
Chen~\etal~address backprojection artifacts without ground-truth images or a perfectly matched forward model~\cite{chenCannyArtifactNLOS2026}. Canny edges and morphological closing separate likely object and artifact regions; Tenengrad sharpness and residual energy define a reference-free genetic-algorithm objective; and an optimized blur kernel corrects the measured transient before backprojection. Tests on confocal and non-confocal simulated and measured data show a complementary robustness route based on measurement correction rather than a stronger scene prior.
'''),
        ("Reference-function phase compensation for non-confocal capture.", "Specular-flight-path regularization.", r'''
\vspace{0.8mm}
\noindent \textbf{Specular-flight-path regularization.}
Non-confocal measurements provide flexible capture but can become highly redundant for complex tilted objects. Shi~\etal~use local matrix analysis to identify specular-flight-path regions with lower column similarity and information redundancy, then regularize inversion around those paths~\cite{shiSpecularFlightPathNLOS2026}. The method improves simulated and measured reconstruction for multi-orientation hidden scenes, showing that path selection can condition the inverse problem before generic spatial regularization is applied.
'''),
    ]
    for anchor, heading, block in additions:
        if heading not in text:
            text = insert_after_heading(text, anchor, block)
    path.write_text(text, encoding="utf-8")


def update_learning() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if "Differentiable transient simulation infrastructure." not in text:
        marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Network Architecture}"
        block = r'''
\vspace{0.8mm}
\noindent \textbf{Differentiable transient simulation infrastructure.}
Royo~\etal~released \textit{mitransient}, an extension of Mitsuba~3 for CPU/GPU time-resolved light transport~\cite{royoMitransient2025}. The toolkit supports realistic materials and participating media, transient polarization tracking, differentiable rendering, NLOS scene construction, and capture-noise simulation. It complements task-specific synthetic datasets by providing a reusable forward-model layer for testing acquisition designs, generating training data, and optimizing transient inverse problems under a consistent physically based renderer.

'''
        text = replace_once(text, marker, block + marker, "network architecture marker")
    path.write_text(text, encoding="utf-8")


def update_newscenes() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")
    text = text.replace(r'\href{https://arxiv.org/abs/2505.08240}{N$^2$LoS}', r'N$^2$LoS~\cite{shiN2LoS2025}')
    text = text.replace(r'\href{https://arxiv.org/abs/2510.10506}{SuperEx}', r'SuperEx~\cite{gargSuperEx2025}')
    if "Tag-assisted multipath disambiguation." not in text:
        block = r'''
\vspace{0.8mm}
\noindent \textbf{Tag-assisted multipath disambiguation.}
Shi~\etal~introduced N$^2$LoS, which combines a single 24~GHz radar with an active backscatter tag~\cite{shiN2LoS2025}. Hybrid frequency-hopping/direct-sequence signaling separates tag returns from environmental reflectors, while frequency--spatial MUSIC resolves additional multipath components. Experiments report roughly 10--12~cm median coordinate error at 5~m, illustrating how a lightweight tag can convert uncontrolled around-corner multipath into identifiable localization paths.
'''
        marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Acoustic NLOS Imaging}"
        text = replace_once(text, marker, block + "\n" + marker, "acoustic section marker")
    if "Semantic human-pose recovery from transients." not in text:
        marker = "Estimating 3D human poses of persons hidden around a corner is an example of semantic NLOS understanding beyond shape reconstruction."
        addition = r'''

\vspace{0.8mm}
\noindent \textbf{Semantic human-pose recovery from transients.}
Xiao~\etal~move beyond applying a conventional pose estimator to a reconstructed hidden image by directly fusing transient-derived intensity and depth features and regressing semantic body joints end to end~\cite{xiaoNLOSHumanPose2026}. A physics-based pipeline synthesizes training measurements from ordinary smartphone videos, while real experiments demonstrate pose estimation at a 1.75~m relay distance and under an SNR of 0.13. This development advances the earlier physics-based HiddenPose concept toward detailed, low-SNR measured-scene semantics.
'''
        text = replace_once(text, marker, marker + addition, "human pose introduction")
    path.write_text(text, encoding="utf-8")


def validate() -> None:
    files = {
        name: (ROOT / path).read_text(encoding="utf-8")
        for name, path in {
            "readme": "README.md",
            "index": "index.html",
            "active": "article/2active.tex",
            "learning": "article/4datadriven.tex",
            "new": "article/5newscenes.tex",
            "bib": "egbib_20260718_reconstruction_pose_consistency.bib",
        }.items()
    }
    source = files["active"] + files["learning"] + files["new"]
    for paper in NEW_PUBLIC:
        title = str(paper["title"])
        key = str(paper["key"])
        if files["readme"].lower().count("[" + title.lower() + "]") != 1:
            raise RuntimeError(f"README entry missing or duplicated: {title}")
        if files["index"].lower().count('title:"' + title.lower() + '"') != 1:
            raise RuntimeError(f"Homepage entry missing or duplicated: {title}")
        if key not in source:
            raise RuntimeError(f"Survey citation missing: {key}")
        if files["bib"].lower().count("{" + key.lower() + ",") != 1:
            raise RuntimeError(f"Canonical BibTeX entry missing or duplicated: {key}")
    for _, key in PUBLIC_ONLY:
        if key not in source:
            raise RuntimeError(f"Public-only survey integration missing: {key}")
        if files["bib"].lower().count("{" + key.lower() + ",") != 1:
            raise RuntimeError(f"Public-only BibTeX entry missing or duplicated: {key}")
    if "10.1364/OE.601398" not in files["readme"] or "10.1364/OE.601398" not in files["index"]:
        raise RuntimeError("Diffuse-aware final DOI is not synchronized")
    if files["bib"].lower().count("{wangdiffuseawarepassive2026,") != 1:
        raise RuntimeError("Diffuse-aware correction entry missing")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_learning()
    update_newscenes()
    validate()
    print("Synchronized five final-venue papers, five public-only consistency records, and the diffuse-aware DOI correction.")


if __name__ == "__main__":
    main()
