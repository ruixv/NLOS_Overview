#!/usr/bin/env python3
"""Anchor-checked synchronization of the virtual NLOS light-transport paper.

The script is intentionally idempotent and refuses to write when a known anchor
has changed, avoiding blind replacement of the hand-maintained README, homepage,
and LaTeX survey source.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging"
CITE_KEY = "marcoVirtualLightTransport2021"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, description: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {description} anchor, found {count}")
    return text.replace(old, new, 1)


def patch_readme() -> None:
    path = "README.md"
    text = read(path)
    if TITLE in text:
        return
    anchor = (
        "| 2021 | [Automatic calibration of time of flight based non-line-of-sight reconstruction]"
        "(https://arxiv.org/abs/2105.10603) — Sadhu et al. | arXiv 2021 | Makes ToF NLOS "
        "reconstruction robust to relay-wall illumination/detection miscalibration by jointly "
        "optimizing hidden albedo and virtual scan positions in a differentiable forward model. |"
    )
    row = (
        "| 2021 | [Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging]"
        "(https://arxiv.org/abs/2103.12622) — Marco et al. | arXiv 2021 | Extends phasor-field "
        "virtual wave optics from hidden-geometry reconstruction to hidden-scene light-transport "
        "analysis, creating virtual projector-camera pairs for relighting and separation of direct, "
        "first-order indirect, and higher-order indirect components. |"
    )
    text = replace_once(text, anchor, row + "\n" + anchor, "README 2021 insertion")
    write(path, text)


def patch_index() -> None:
    path = "index.html"
    text = read(path)
    if TITLE in text:
        return

    count_anchor = '<div class="stat"><b>83</b><span>tracked latest entries</span></div>'
    count_new = '<div class="stat"><b>84</b><span>tracked latest entries</span></div>'
    text = replace_once(text, count_anchor, count_new, "homepage latest-count")

    timeline_old = (
        '<div class="tl"><div class="year">2021</div><div class="tl-body"><strong>Kilometer range, '
        'neural fields, commercial LiDAR, picosecond timing, and self-calibration</strong><p>Long-range '
        'NLOS, NeTF, PRL picosecond-resolution up-conversion detection, calibration-aware ToF '
        'reconstruction, and two-step LiDAR deep remapping expanded scale and acquisition regimes.'
        '</p></div></div>'
    )
    timeline_new = (
        '<div class="tl"><div class="year">2021</div><div class="tl-body"><strong>Kilometer range, '
        'neural fields, virtual transport matrices, commercial LiDAR, picosecond timing, and '
        'self-calibration</strong><p>Long-range NLOS, NeTF, phasor-field virtual projector-camera '
        'systems for hidden light-transport analysis, PRL picosecond-resolution up-conversion '
        'detection, calibration-aware ToF reconstruction, and two-step LiDAR deep remapping expanded '
        'scale and acquisition regimes.</p></div></div>'
    )
    text = replace_once(text, timeline_old, timeline_new, "2021 timeline")

    object_anchor = (
        '      {cat:"latest active",title:"Automatic calibration of time of flight based '
        'non-line-of-sight reconstruction",authors:"Sadhu et al.",year:2021,venue:"arXiv 2021",'
        'url:"https://arxiv.org/abs/2105.10603",key:"Differentiable forward model jointly optimizes '
        'hidden albedo and virtual scan positions under relay-wall calibration error."},'
    )
    new_object = (
        '      {cat:"latest active",title:"Virtual Light Transport Matrices for Non-Line-Of-Sight '
        'Imaging",authors:"Marco et al.",year:2021,venue:"arXiv 2021",url:"https://arxiv.org/abs/'
        '2103.12622",key:"Phasor-field virtual projector-camera pairs estimate hidden-scene light '
        'transport for relighting and separation of direct and higher-order indirect components."},'
    )
    text = replace_once(text, object_anchor, new_object + "\n" + object_anchor, "homepage paper object")
    write(path, text)


def patch_survey() -> None:
    path = "article/2active.tex"
    text = read(path)
    if CITE_KEY in text:
        return
    anchor = (
        "Different from other methods, phasor field methods~\\cite{liuPhasorFieldDiffraction2020,"
        "liuVirtualWaveOptics2018} transform the relay wall into a virtual aperture (or lens of any "
        "LOS system). The reconstruction is the diffraction integral of the wavefront of the virtual "
        "aperture, which is equivalent to the forward propagation process of the measurement data. "
        "Therefore, phasor field methods~\\cite{liuPhasorFieldDiffraction2020,liuVirtualWaveOptics2018} "
        "do not need to reverse the forward process like inverse methods~\\cite{otooleConfocalNonlineofsightImaging2018,"
        "veltenRecoveringThreedimensionalShape2012} -- they can directly complete the reconstruction "
        "through wavefront propagation.\n\n"
    )
    paragraph = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Virtual light-transport analysis.}\n"
        "Marco~\\etal~extended phasor-field virtual wave optics beyond hidden-geometry reconstruction "
        "by constructing computational projector--camera pairs and estimating a virtual light "
        "transport matrix of the hidden scene~\\cite{marcoVirtualLightTransport2021}. Probing this "
        "matrix enables virtual relighting and separates direct, first-order indirect, and higher-order "
        "indirect illumination in cluttered NLOS scenes, showing that transient NLOS measurements can "
        "support light-transport analysis as well as geometric imaging.\n\n"
    )
    text = replace_once(text, anchor, anchor + paragraph, "phasor-field survey insertion")
    write(path, text)


def verify() -> None:
    checks = {
        "README.md": TITLE,
        "index.html": TITLE,
        "article/2active.tex": CITE_KEY,
        "egbib_20260711_vltm_updates.bib": CITE_KEY,
    }
    for path, token in checks.items():
        text = read(path)
        if token not in text:
            raise RuntimeError(f"Verification failed: {token!r} absent from {path}")
    index = read("index.html")
    if '<div class="stat"><b>84</b><span>tracked latest entries</span></div>' not in index:
        raise RuntimeError("Homepage latest count was not updated to 84")


if __name__ == "__main__":
    patch_readme()
    patch_index()
    patch_survey()
    verify()
    print("Virtual light transport matrix synchronization applied and verified.")
