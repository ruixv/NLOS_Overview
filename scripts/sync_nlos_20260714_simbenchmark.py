#!/usr/bin/env python3
"""Idempotently integrate the 2025 fast NLOS transient simulator and benchmark."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset"
URL = "https://arxiv.org/abs/2506.03747"
KEY = "shiFastNLOSTransientSimulation2025"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")

    row = (
        f"| 2025 | [{TITLE}]({URL}) — Shi et al. | arXiv 2025 | "
        "Provides a configurable FFT/LCT-based transient simulator from depth and optional albedo maps, models detector jitter and Poisson noise, releases seven ShapeNet-category datasets, and benchmarks LCT, phasor-field, f-k, and backprojection reconstruction baselines. |\n"
    )
    if TITLE not in text:
        anchor = (
            "| 2025 | [TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces](https://doi.org/10.1109/TIP.2025.3637694) — Cui et al. | IEEE TIP 2025 | Uses latent diffusion and unsupervised measurement consistency to synthesize/recover dense transient information from aperture-limited relay measurements. |"
        )
        text = replace_once(text, anchor, row + anchor, "README 2025 paper row")

    timeline_anchor = (
        "   │     Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]\n"
        "   │\n"
        "```"
    )
    timeline_new = (
        "   │     Royo et al.: virtual mirrors — higher-order phasor transport and two-corner NLOS [SIGGRAPH / TOG]\n"
        "   │\n"
        "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
        "   │\n"
        "```"
    )
    text = replace_once(text, timeline_anchor, timeline_new, "README 2025 timeline")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    paper = (
        '      {cat:"latest dataset active",title:"Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset",authors:"Shi et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2506.03747",key:"A configurable FFT/LCT simulator generates noisy transient volumes from depth and albedo maps, releases seven ShapeNet-category datasets, and benchmarks LCT, phasor-field, f-k, and backprojection baselines."},\n'
    )
    if TITLE not in text:
        anchor = (
            '      {cat:"latest learning active",title:"TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces",authors:"Cui et al.",year:2025,venue:"IEEE TIP 2025",url:"https://doi.org/10.1109/TIP.2025.3637694",key:"Latent diffusion and unsupervised consistency recover dense transient information from aperture-limited measurements."},'
        )
        text = replace_once(text, anchor, paper + anchor, "homepage paper object")

    text = replace_once(
        text,
        '<b>95</b><span>tracked latest entries</span>',
        '<b>96</b><span>tracked latest entries</span>',
        "homepage tracked-entry count",
    )

    old_timeline = (
        '<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, graph models, pretraining, radar, acoustic, 6G initial-access imaging, and robotic NLOS</strong><p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, MITO, N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and relay-free acoustic NLOS broadened the toolbox.</p></div></div>'
    )
    new_timeline = (
        '<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>Operator learning, graph models, pretraining, open transient benchmarks, radar, acoustic, 6G initial-access imaging, and robotic NLOS</strong><p>TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, fast configurable transient simulation with an open ShapeNet benchmark, MITO, N2LoS, mmMirror, reflector-assisted base-station initial-access imaging, and relay-free acoustic NLOS broadened the toolbox.</p></div></div>'
    )
    text = replace_once(text, old_timeline, new_timeline, "homepage 2025 timeline")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if KEY in text:
        return

    anchor = (
        "Since 2022, dedicated NLOS rendering tools have emerged to generate higher-fidelity synthetic training data. Royo~\\etal~presented the first NLOS transient renderer designed to accurately simulate light transport in NLOS scenarios, enabling generation of realistic training data and testing of reconstruction algorithms~\\cite{royoNLOSTransientRendering2022}. Plack~\\etal~subsequently developed a fast differentiable transient renderer for NLOS scenes that supports automatic differentiation, enabling gradient-based optimization of scene parameters and end-to-end training of NLOS reconstruction networks~\\cite{plackFastDifferentiable2023}. For passive NLOS tracking, Wang~\\etal~released the NLOS-Track dataset, the first large-scale dynamic passive NLOS tracking dataset with thousands of real and synthetic video clips paired with trajectory labels~\\cite{wangPropagateCalibrate2023}, addressing the severe data scarcity problem in passive NLOS research."
    )
    paragraph = (
        "\n\nComplementing physically complete transient renderers with a benchmark-oriented alternative, Shi~\\etal~introduced a configurable simulator grounded in the light-cone transform and accelerated by three-dimensional FFT convolution~\\cite{shiFastNLOSTransientSimulation2025}. The framework accepts depth and optional albedo maps, exposes relay-wall extent, stand-off distance, temporal binning, detector jitter, and Poisson noise as explicit parameters, and releases transient data for seven ShapeNet object categories together with common LCT, phasor-field, $f$--$k$, and backprojection baselines. This development lowers the cost of standardized algorithm comparison and large-scale learning, while remaining complementary to Monte Carlo transient rendering when higher-order transport, complex materials, or full sensor realism are required."
    )
    text = replace_once(text, anchor, anchor + paragraph, "survey dataset paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE}")


if __name__ == "__main__":
    main()
