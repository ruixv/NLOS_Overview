#!/usr/bin/env python3
"""Synchronize optimized Fourier sampling across the NLOS public artifacts."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms"
KEY = "sultanOptimizedSamplingNLOS2025"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("**Update run: 15 July 2026.**", "**Update run: 16 July 2026.**")

    if TITLE not in text:
        row = (
            "| 2025 | [Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms]"
            "(https://arxiv.org/abs/2501.05244) — Sultan et al. | arXiv 2025 | "
            "Uses phasor-field sampling analysis, NUFFT, and SFFT to reconstruct from sparse irregular relay samples, "
            "query arbitrary hidden-volume locations, and enlarge reconstruction volumes without increasing stored samples, "
            "while retaining FFT-like computational complexity. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    addition = (
        "   │     Sultan et al.: optimized NUFFT/SFFT sampling — irregular relay scans and flexible hidden-volume grids at FFT-like cost [arXiv]\n"
    )
    if addition not in text:
        anchor = (
            "   │     Liu et al.: geometric constraints on hidden surface normals for fast sparse-transient reconstruction [arXiv]\n"
        )
        text = replace_once(text, anchor, anchor + addition, "README 2025 milestone")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("Updated 15 July 2026 · 190+ papers", "Updated 16 July 2026 · 190+ papers")
    text = text.replace("Last updated: 15 July 2026", "Last updated: 16 July 2026")

    old_paper = (
        '      {cat:"latest active",title:"Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms",'
        'authors:"Sultan et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2501.05244",'
        'key:"NUFFT/SFFT sampling strategy for sparse irregular relay grids and scalable hidden-volume reconstruction."},'
    )
    new_paper = (
        '      {cat:"latest active",title:"Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms",'
        'authors:"Sultan et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2501.05244",'
        'key:"Phasor-field sampling analysis exposes spatial oversampling; NUFFT supports sparse irregular relay samples and arbitrary hidden-volume queries, while SFFT enlarges reconstruction volumes without increasing stored samples, all at FFT-like complexity."},'
    )
    if old_paper in text:
        text = replace_once(text, old_paper, new_paper, "homepage paper entry")
    elif TITLE not in text:
        paper = new_paper + "\n"
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>101</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>102</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_timeline = (
        '<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, geometric surface priors, graph models, pretraining, open transient benchmarks, radar, acoustic, 6G initial-access imaging, and robotic NLOS</strong><p>'
        'TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, fast configurable transient simulation with an open ShapeNet benchmark, shape-operator regularization for hidden surface normals, MITO, N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and relay-free acoustic NLOS broadened the toolbox.</p></div></div>'
    )
    new_timeline = (
        '<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, optimized Fourier sampling, geometric surface priors, graph models, pretraining, open transient benchmarks, radar, acoustic, 6G initial-access imaging, and robotic NLOS</strong><p>'
        'TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, fast configurable transient simulation with an open ShapeNet benchmark, shape-operator regularization for hidden surface normals, MITO, N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and relay-free acoustic NLOS broadened the toolbox. Sultan et al. further moved FFT-based phasor-field inversion beyond fixed Cartesian grids by combining NUFFT reconstruction for sparse irregular relay samples and arbitrary hidden-volume queries with SFFT scaling for larger volumes at unchanged sample storage.</p></div></div>'
    )
    if old_timeline in text:
        text = replace_once(text, old_timeline, new_timeline, "homepage 2025 timeline")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")

    table_old = ",guFastNLOSNonPlanar2023} & Pulsed laser & SPAD & Time of fight &  3D reconstruction"
    table_new = ",guFastNLOSNonPlanar2023,sultanOptimizedSamplingNLOS2025} & Pulsed laser & SPAD & Time of fight &  3D reconstruction"
    if table_old in text:
        text = replace_once(text, table_old, table_new, "active-SPAD table citation")

    heading = "\\noindent \\textbf{Nonuniform and scaled Fourier sampling.}"
    if heading not in text:
        anchor = (
            "The phasor field methods\\cite{rezaPhasorFieldWaves2019,liuPhasorFieldDiffraction2020,liuVirtualWaveOptics2018}, which have attracted widespread attention recently, regard the NLOS imaging as a diffraction-based LOS (line-of-sight) optical imaging problem. The projector function and diffraction function are determined by selecting a suitable LOS template, thereby directly reconstructing the hidden scene. Although based on wave propagation, these methods are all suitable for ToF measurement, making it easy to collect data and apply the model to public NLOS imaging datasets.\n"
        )
        paragraph = (
            "\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Nonuniform and scaled Fourier sampling.}\n"
            "FFT-accelerated LCT, $f$--$k$ migration, and phasor-field methods conventionally couple acquisition and reconstruction to uniform Cartesian grids. Sultan~\\etal~showed that practical relay measurements are often spatially oversampled and introduced modified Fourier operators that preserve fast wave-based inversion while relaxing this coupling~\\cite{sultanOptimizedSamplingNLOS2025}. Their NUFFT formulation reconstructs from sparse, irregularly sampled relay regions of arbitrary shape and evaluates the hidden volume at arbitrary locations, while a scaled FFT enlarges the reconstructed volume without increasing the number of stored samples. This development shifts Fourier-domain NLOS from fixed-grid acceleration toward acquisition-aware and memory-aware sampling without sacrificing FFT-like asymptotic complexity.\n"
        )
        text = replace_once(text, anchor, anchor + paragraph, "survey phasor-field paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, and survey source.")


if __name__ == "__main__":
    main()
