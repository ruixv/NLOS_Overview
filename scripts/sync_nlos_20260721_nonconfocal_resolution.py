#!/usr/bin/env python3
"""Synchronize three verified 2024 active-NLOS resolution papers.

The edits fail closed: every insertion uses a unique anchor, and the script
refuses to create duplicate DOI, title, or citation-key records.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

DOIS = (
    "10.1016/j.optlaseng.2024.108067",
    "10.1364/OE.518767",
    "10.1364/OL.528300",
)
KEYS = (
    "zhengSemiConfocalNLOS2024",
    "wangIRFDeconvolutionNLOS2024",
    "yuSphericalSliceNonconfocal2024",
)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def ensure_absent(text: str, tokens: tuple[str, ...], label: str) -> None:
    present = [token for token in tokens if token in text]
    if present:
        raise RuntimeError(f"{label}: already contains {present}")


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    ensure_absent(text, DOIS, path)
    rows = (
        "| 2024 | [Converting non-confocal measurements into semi-confocal ones with timing-accuracy improving for non-line-of-sight imaging](https://doi.org/10.1016/j.optlaseng.2024.108067) — Zheng et al. | Optics and Lasers in Engineering 2024 | Uses sectionalized-ellipsoid interpolation to redistribute point-illumination/SPAD-array measurements into timing-refined semi-confocal histograms, connecting efficient non-confocal capture to mature confocal reconstruction algorithms and resolving structures missed by FBP and normal-moveout correction. |\n"
        "| 2024 | [Enhancing the spatial resolution of time-of-flight based non-line-of-sight imaging via instrument response function deconvolution](https://doi.org/10.1364/OE.518767) — Wang et al. | Optics Express 2024 | Models measured transients as a Poisson convolution with the calibrated instrument response and iteratively deconvolves timing jitter before LCT or f-k migration; reconstruction remains effective at 1200 ps total jitter, approaching results previously requiring about 200 ps timing. |\n"
        "| 2024 | [High-resolution non-confocal non-line-of-sight imaging based on spherical-slice transform from spatial and temporal frequency to space and time](https://doi.org/10.1364/OL.528300) — Yu et al. | Optics Letters 2024 | Introduces a spherical-slice transform for non-confocal SPAD-array transients, avoiding artifacts, shape distortion, and position offsets while reaching several-hundred-millisecond GPU reconstruction on a 32×32 PF32 detector. |\n"
    )
    header = "|------|-------|----------------|----------------|\n"
    text = replace_once(text, header, header + rows, "README latest table")
    timeline_anchor = "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]"
    timeline_rows = (
        "   │     Zheng et al.: sectionalized-ellipsoid interpolation — non-confocal SPAD-array measurements become timing-refined semi-confocal histograms [Optics and Lasers in Engineering]\n"
        "   │     Wang et al.: instrument-response deconvolution — calibrated Poisson deblurring restores spatial resolution before LCT or f-k migration under severe timing jitter [Optics Express]\n"
        "   │     Yu et al.: spherical-slice transform — fast high-resolution non-confocal reconstruction without geometric artifacts or position offsets [Optics Letters]\n"
    )
    text = replace_once(text, timeline_anchor, timeline_rows + timeline_anchor, "README 2024 timeline")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    ensure_absent(text, DOIS, path)
    text = replace_once(
        text,
        '<div class="stat"><b>175</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>178</b><span>tracked latest entries</span></div>',
        "website tracked count",
    )
    objects = (
        '      {cat:"latest active nonconfocal acquisition",title:"Converting non-confocal measurements into semi-confocal ones with timing-accuracy improving for non-line-of-sight imaging",authors:"Zheng et al.",year:2024,venue:"Optics and Lasers in Engineering 2024",url:"https://doi.org/10.1016/j.optlaseng.2024.108067",key:"Sectionalized-ellipsoid interpolation redistributes point-illumination and SPAD-array measurements into timing-refined semi-confocal histograms, connecting practical non-confocal capture to mature confocal reconstruction algorithms."},\n'
        '      {cat:"latest active hardware resolution",title:"Enhancing the spatial resolution of time-of-flight based non-line-of-sight imaging via instrument response function deconvolution",authors:"Wang et al.",year:2024,venue:"Optics Express 2024",url:"https://doi.org/10.1364/OE.518767",key:"Calibrated Poisson deconvolution removes instrument-response timing blur before LCT or f-k migration, preserving high-resolution reconstruction under total temporal jitter as large as 1200 ps and at low SNR."},\n'
        '      {cat:"latest active nonconfocal wave realtime",title:"High-resolution non-confocal non-line-of-sight imaging based on spherical-slice transform from spatial and temporal frequency to space and time",authors:"Yu et al.",year:2024,venue:"Optics Letters 2024",url:"https://doi.org/10.1364/OL.528300",key:"A spherical-slice transform maps non-confocal spatial-temporal frequency data into hidden space and time, avoiding artifacts and positional distortion while running in several hundred milliseconds on 32×32 PF32 data."},\n'
    )
    text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")

    pattern = re.compile(
        r'(<div class="tl"><div class="year">2024</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
    )
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"website 2024 timeline: expected one block, found {len(matches)}")
    addition = (
        " Sectionalized-ellipsoid interpolation converted point-illumination/SPAD-array measurements into timing-refined semi-confocal histograms, while calibrated instrument-response deconvolution restored spatial detail before LCT and f-k migration under severe detector jitter. A spherical-slice transform then provided high-resolution non-confocal inversion without artifact interference, shape distortion, or position offset at several-hundred-millisecond GPU latency."
    )
    text = pattern.sub(lambda m: m.group(1) + m.group(2) + addition + m.group(3), text, count=1)
    write(path, text)


def update_active_survey() -> None:
    path = "article/2active.tex"
    text = read(path)
    ensure_absent(text, KEYS, path)
    table_anchor = "yuNonconfocalPhaseCompensation2026,tianSparseBayesianNLOS2026"
    table_new = "yuNonconfocalPhaseCompensation2026,zhengSemiConfocalNLOS2024,wangIRFDeconvolutionNLOS2024,yuSphericalSliceNonconfocal2024,tianSparseBayesianNLOS2026"
    text = replace_once(text, table_anchor, table_new, "active-method table citations")

    anchor = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Reference-function phase compensation for non-confocal capture.}"
    )
    prose = r"""\vspace{0.8mm}
\noindent \textbf{Non-confocal SPAD arrays: measurement conversion, timing restoration, and spherical-slice inversion.}
Parallel SPAD arrays improve photon efficiency and remove detector raster scanning, but separate illumination and detection positions replace confocal spheres with bistatic ellipsoids and make standard LCT or $f$--$k$ inversion less direct. Zheng~\etal~addressed this mismatch with sectionalized-ellipsoid interpolation, redistributing each non-confocal histogram into a timing-refined semi-confocal representation that can be processed by established confocal solvers~\cite{zhengSemiConfocalNLOS2024}. The spatial slicing can improve effective timing accuracy beyond the detector bin width and resolves structures missed by filtered backprojection and normal-moveout correction.

A complementary hardware-aware route treats temporal resolution itself as an inverse problem. Wang~\etal~modeled TCSPC measurements as a Poisson convolution with the calibrated instrument response and applied iterative deconvolution before LCT or $f$--$k$ migration~\cite{wangIRFDeconvolutionNLOS2024}. Their simulations and measurements show that useful high-resolution reconstruction can be retained with total timing jitter up to 1200~ps, close to results previously associated with approximately 200~ps timing, while remaining robust at low SNR.

Yu~\etal~then proposed a direct spherical-slice transform from spatial and temporal frequency to hidden space and time for non-confocal measurements~\cite{yuSphericalSliceNonconfocal2024}. The transform avoids artifact interference, shape distortion, and position offsets across varied scenes and reduces reconstruction to several hundred milliseconds on GPU for a $32\times32$ PF32 photon array. Together, these works establish a practical non-confocal resolution lineage: measurement conversion reuses mature confocal inverses, instrument-response deconvolution recovers lost temporal bandwidth, and spherical-slice inversion exploits the bistatic acquisition geometry directly.

"""
    text = replace_once(text, anchor, prose + anchor, "active nonconfocal narrative")
    write(path, text)


def update_master_tex() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    text = replace_once(text, "through 20 July 2026", "through 21 July 2026", "survey coverage date")
    anchor = "% 21 July 2026 citation trace integrates computational neuromorphic event-camera NLOS tracking.\n"
    addition = "% 21 July 2026 non-confocal resolution trace integrates semi-confocal conversion, instrument-response deconvolution, and spherical-slice inversion.\n"
    text = replace_once(text, anchor, anchor + addition, "survey integration marker")
    write(path, text)


def validate_sources() -> None:
    for path in ("README.md", "index.html"):
        text = read(path)
        for doi in DOIS:
            if text.count(doi) != 1:
                raise RuntimeError(f"{path}: expected one occurrence of {doi}")
    active = read("article/2active.tex")
    for key in KEYS:
        if active.count(key) < 2:
            raise RuntimeError(f"article/2active.tex: key not integrated in table and prose: {key}")


def main() -> None:
    update_readme()
    update_index()
    update_active_survey()
    update_master_tex()
    validate_sources()
    subprocess.run([sys.executable, str(ROOT / "scripts/merge_nlos_bibliography.py")], cwd=ROOT, check=True)
    merged = read("egbib_merged_20260711.bib")
    for key, doi in zip(KEYS, DOIS):
        if merged.count(key) != 1 or merged.count(doi) != 1:
            raise RuntimeError(f"merged bibliography inconsistency for {key} / {doi}")
    print("Integrated three verified non-confocal resolution papers.")


if __name__ == "__main__":
    main()
