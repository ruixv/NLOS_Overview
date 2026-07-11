#!/usr/bin/env python3
"""Synchronize the citation-traced real-time dynamic NLOS milestone."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Real-time Non-line-of-Sight imaging of dynamic scenes"
DOI = "https://doi.org/10.1038/s41467-021-26721-x"
KEY = "namRealTimeDynamicScenes2021"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def sync_readme() -> None:
    text = read("README.md")
    row = (
        f"| 2021 | [{TITLE}]({DOI}) — Nam et al. | Nature Communications 2021 | "
        "Combines two gated $16\\times1$ SPAD arrays (28 active pixels), sparse relay-wall "
        "scanning, virtual-aperture remapping, and fast phasor-field propagation to acquire "
        "and reconstruct diffuse, non-retroreflective hidden scenes at 5 fps with about 1 s latency. |\n"
    )
    if TITLE not in text:
        anchor = "| 2021 | [Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging]"
        pos = text.find(anchor)
        if pos < 0:
            raise RuntimeError("README 2021 insertion anchor not found")
        text = text[:pos] + row + text[pos:]

    milestone = "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]"
    if milestone not in text:
        old = (
            "2018 ── O'Toole et al.: confocal NLOS + LCT — real-time O(N³logN) [Nature]\n"
            "   │     Liu et al.: phasor field — NLOS as virtual LOS wave propagation\n"
            "   │\n"
            "```"
        )
        new = (
            "2018 ── O'Toole et al.: confocal NLOS + LCT — real-time O(N³logN) [Nature]\n"
            "   │     Liu et al.: phasor field — NLOS as virtual LOS wave propagation\n"
            "   │\n"
            "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n"
            "   │\n"
            "```"
        )
        text = replace_once(text, old, new, "README milestone")
    write("README.md", text)


def sync_index() -> None:
    text = read("index.html")
    if TITLE not in text:
        anchor = '      {cat:"latest modality learning",title:"X-band Radar Non-Line-of-Sight Imaging"'
        obj = (
            '      {cat:"latest active",title:"Real-time Non-line-of-Sight imaging of dynamic scenes",'
            'authors:"Nam et al.",year:2021,venue:"Nature Communications 2021",'
            f'url:"{DOI}",key:"Two gated 16×1 SPAD arrays (28 active pixels), sparse scanning, '
            'virtual-aperture remapping, and fast phasor-field propagation acquire and reconstruct '
            'diffuse hidden scenes at 5 fps with about 1 s latency."},\n\n'
        )
        pos = text.find(anchor)
        if pos < 0:
            raise RuntimeError("Homepage paper-array insertion anchor not found")
        text = text[:pos] + obj + text[pos:]

    old_count = '<b>85</b><span>tracked latest entries</span>'
    new_count = '<b>86</b><span>tracked latest entries</span>'
    if old_count in text:
        text = text.replace(old_count, new_count, 1)
    elif new_count not in text:
        raise RuntimeError("Homepage latest-count anchor is neither 85 nor 86")

    old_timeline = (
        '<div class="tl"><div class="year">2021</div><div class="tl-body"><strong>'
        'Kilometer range, neural fields, virtual transport matrices, commercial LiDAR, picosecond timing, and self-calibration'
        '</strong><p>Long-range NLOS, NeTF, phasor-field virtual projector-camera systems for hidden light-transport analysis, '
        'PRL picosecond-resolution up-conversion detection, calibration-aware ToF reconstruction, and two-step LiDAR deep remapping '
        'expanded scale and acquisition regimes.</p></div></div>'
    )
    new_timeline = (
        '<div class="tl"><div class="year">2021</div><div class="tl-body"><strong>'
        'Real-time diffuse NLOS video, kilometer range, neural fields, virtual transport matrices, commercial LiDAR, picosecond timing, and self-calibration'
        '</strong><p>Nam et al. demonstrated a full 5 fps capture-and-reconstruction pipeline for diffuse, non-retroreflective hidden scenes; '
        'long-range NLOS, NeTF, phasor-field virtual projector-camera systems for hidden light-transport analysis, PRL picosecond-resolution '
        'up-conversion detection, calibration-aware ToF reconstruction, and two-step LiDAR deep remapping further expanded scale and acquisition regimes.'
        '</p></div></div>'
    )
    if "Real-time diffuse NLOS video, kilometer range" not in text:
        text = replace_once(text, old_timeline, new_timeline, "homepage 2021 timeline")
    write("index.html", text)


def sync_survey() -> None:
    text = read("article/2active.tex")
    marker = "providing an early full-pipeline real-time NLOS video milestone"
    if marker not in text:
        anchor = (
            "This landmark result marks a major step towards practical deployment. Further, Li~\\etal~developed TransiT, "
            "a transient transformer architecture for NLOS videography that reconstructs $64\\times64$ resolution videos at "
            "10\\,fps from $16\\times16$ sparse transient measurements via transfer learning to bridge the synthetic-to-real "
            "domain gap~\\cite{liTransiT2025}."
        )
        addition = (
            "\n\nBefore these later dynamic systems, Nam~\\etal~combined two gated $16\\times1$ SPAD arrays "
            "(28 active pixels), sparse relay-wall scanning, virtual-aperture remapping, and fast Rayleigh--Sommerfeld "
            "phasor-field propagation to acquire and reconstruct diffuse, non-retroreflective hidden scenes at "
            "$5\\,\\mathrm{fps}$ with approximately $1\\,\\mathrm{s}$ latency~\\cite{" + KEY + "}, providing an early "
            "full-pipeline real-time NLOS video milestone."
        )
        text = replace_once(text, anchor, anchor + addition, "survey dynamic-video paragraph")
    write("article/2active.tex", text)


def sync_bibliography() -> None:
    content = """% Citation-traced real-time dynamic NLOS milestone (12 July 2026).

@article{namRealTimeDynamicScenes2021,
  author = {Nam, Ji Hyun and Brandt, Eric and Bauer, Sebastian and Liu, Xiaochun and Sifakis, Eftychios and Velten, Andreas},
  title = {Real-time Non-line-of-Sight imaging of dynamic scenes},
  journal = {Nature Communications},
  volume = {12},
  pages = {6526},
  year = {2021},
  doi = {10.1038/s41467-021-26721-x},
  url = {https://doi.org/10.1038/s41467-021-26721-x}
}
"""
    (ROOT / "egbib_20260712_realtime_updates.bib").write_text(content, encoding="utf-8")


def sync_note() -> None:
    content = f"""# 12 July 2026 real-time dynamic NLOS citation-tracing update

## Citation-tracing result

A forward/reference-tracing pass through recent ToF NLOS comparative literature surfaced **{TITLE}** by Nam et al. The paper was already cited in legacy survey tables but was missing from the README and homepage and did not have an explicit literature-review sentence describing its system-level contribution.

The final publication is **Nature Communications 12, 6526 (2021)**, DOI `10.1038/s41467-021-26721-x`; it is therefore labeled by the journal rather than by its 2020 arXiv preprint.

## Why it belongs

The work combines two gated $16\\times1$ SPAD arrays (28 active pixels), sparse relay-wall scanning, virtual-aperture remapping, and accelerated phasor-field propagation. It reports end-to-end acquisition and reconstruction of diffuse, non-retroreflective dynamic hidden scenes at 5 fps with approximately 1 s latency, making it a milestone between fast reconstruction algorithms and later room-scale NLOS video systems.

## Synchronized artifacts

- `README.md`: final-venue paper row and a 2021 milestone-timeline node.
- `index.html`: searchable/latest paper object, updated 2021 trajectory, and latest-entry count 85 to 86.
- `article/2active.tex`: contribution inserted in the SPAD-array / dynamic-video discussion.
- `egbib_20260712_realtime_updates.bib`: publisher-verified metadata under `{KEY}`.
- `egbib_merged_20260711.bib`: regenerated by the duplicate-free bibliography merger.
- `bare_jrnl.pdf`: rebuilt only after strict LaTeX/BibTeX, PDF-text, and cross-artifact validation.
"""
    (ROOT / "updates/2026-07-12-realtime-dynamic-nlos-citation-tracing-update.md").write_text(content, encoding="utf-8")


def main() -> None:
    sync_readme()
    sync_index()
    sync_survey()
    sync_bibliography()
    sync_note()
    print("Synchronized real-time dynamic NLOS milestone across source artifacts")


if __name__ == "__main__":
    main()
