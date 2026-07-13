#!/usr/bin/env python3
"""Synchronize two missing 2024 NLOS papers across public artifacts.

The edits are marker-based and idempotent. The script aborts instead of
blindly rewriting a large hand-maintained file if an expected marker is absent
or ambiguous.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NIGHT_TITLE = "NIGHT -- Non-Line-of-Sight Imaging from Indirect Time of Flight Data"
TCSPC_TITLE = "Miniaturized time-correlated single-photon counting module for time-of-flight non-line-of-sight imaging applications"
NIGHT_KEY = "caligiuriNIGHT2024"
TCSPC_KEY = "wuMiniaturizedTCSPC2024"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} marker, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    text = read("README.md")
    text = text.replace("**Update run: 12 July 2026.**", "**Update run: 13 July 2026.**", 1)

    marker = (
        "| 2024 | [Virtual Scanning: Unsupervised Non-line-of-sight Imaging from Irregularly "
        "Undersampled Transients](https://proceedings.neurips.cc/paper_files/paper/2024/file/"
        "c58437945392cec01e0c75ff6cef901a-Paper-Conference.pdf) — Cui et al. | NeurIPS 2024 | "
        "Learns from irregularly undersampled transients without paired supervision, combining virtual "
        "scanning, measurement consistency, and a physics-guided SURE denoiser. |\n"
    )
    rows = ""
    if TCSPC_TITLE not in text:
        rows += (
            f"| 2024 | [{TCSPC_TITLE}](https://doi.org/10.1063/5.0193824) — Wu et al. | "
            "Review of Scientific Instruments 2024 | Miniaturizes the timing backend of single-photon "
            "ToF NLOS: a four-channel TCSPC module provides a 10 ps bin and 27.4 ps minimum RMS timing "
            "resolution, supporting 6.3 cm lateral and 2.3 cm depth resolution at a 5 m sensor distance. |\n"
        )
    if NIGHT_TITLE not in text:
        rows += (
            f"| 2024 | [{NIGHT_TITLE}](https://arxiv.org/abs/2403.19376) — Caligiuri et al. | "
            "ECCV 2024 Workshop (MELEX) | Introduces NLOS depth reconstruction from an off-the-shelf "
            "indirect-ToF sensor without extra transient hardware, using a learned virtual-mirror model "
            "and a purpose-built synthetic dataset. |\n"
        )
    if rows:
        text = replace_once(text, marker, rows + marker, "README Virtual Scanning row")

    for title in (TCSPC_TITLE, NIGHT_TITLE):
        if text.count(title) != 1:
            raise RuntimeError(f"README should contain one {title!r} entry, found {text.count(title)}")
    if "**Update run: 13 July 2026.**" not in text:
        raise RuntimeError("README update date did not advance to 13 July 2026")
    write("README.md", text)


def update_homepage() -> None:
    text = read("index.html")
    text = text.replace("Updated 12 July 2026", "Updated 13 July 2026", 1)
    text = text.replace("Last updated: 12 July 2026", "Last updated: 13 July 2026", 1)

    marker = (
        '      {cat:"latest learning active",title:"Virtual Scanning: Unsupervised Non-line-of-sight '
        'Imaging from Irregularly Undersampled Transients",authors:"Cui et al.",year:2024,'
    )
    objects = ""
    if TCSPC_TITLE not in text:
        objects += (
            '      {cat:"latest hardware active",title:"Miniaturized time-correlated single-photon counting '
            'module for time-of-flight non-line-of-sight imaging applications",authors:"Wu et al.",year:2024,'
            'venue:"Review of Scientific Instruments 2024",url:"https://doi.org/10.1063/5.0193824",'
            'key:"Four-channel compact TCSPC electronics provide 10 ps bins and 27.4 ps minimum RMS timing '
            'resolution for a 1550 nm single-photon ToF NLOS system at a 5 m sensor distance."},\n'
        )
    if NIGHT_TITLE not in text:
        objects += (
            '      {cat:"latest hardware learning active dataset",title:"NIGHT -- Non-Line-of-Sight Imaging '
            'from Indirect Time of Flight Data",authors:"Caligiuri et al.",year:2024,'
            'venue:"ECCV 2024 Workshop (MELEX)",url:"https://arxiv.org/abs/2403.19376",'
            'key:"Off-the-shelf indirect-ToF NLOS depth reconstruction without extra transient hardware, '
            'using a learned virtual-mirror representation and a synthetic training dataset."},\n'
        )
    if objects:
        text = replace_once(text, marker, objects + marker, "homepage Virtual Scanning object")

    count_re = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    matches = count_re.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage tracked-entry count, found {len(matches)}")
    current = int(matches[0])
    if current not in (89, 90, 91):
        raise RuntimeError(f"Unexpected homepage count {current}; initial-access synchronization may be missing")
    text = count_re.sub('<b>91</b><span>tracked latest entries</span>', text, count=1)

    old_timeline = (
        '      <div class="tl"><div class="year">2024</div><div class="tl-body"><strong>Real-time video, '
        'LEAP, HDPS, TLTM iteration, ptychography, autonomous navigation, robot tracking, and EM skins</strong>'
        '<p>Dynamic room-sized NLOS video, spectrum filtering with motion compensation, plug-and-play '
        'reconstruction, Virtual Scanning, domain reduction, Mamba-style temporal modeling, phasor-field '
        'enhancement, ptychographic depth-resolved NLOS, single-photon-LiDAR navigation, mobile-robot tracking, '
        'and passive metasurface-assisted radar NLOS became central.</p></div></div>'
    )
    new_timeline = (
        '      <div class="tl"><div class="year">2024</div><div class="tl-body"><strong>Real-time video, '
        'commodity iToF, compact TCSPC, LEAP, HDPS, TLTM iteration, ptychography, robotics, and EM skins</strong>'
        '<p>Dynamic room-sized NLOS video, off-the-shelf indirect-ToF depth inference, miniaturized single-photon '
        'timing electronics, spectrum filtering with motion compensation, plug-and-play reconstruction, Virtual '
        'Scanning, domain reduction, Mamba-style temporal modeling, phasor-field enhancement, ptychographic '
        'depth-resolved NLOS, single-photon-LiDAR navigation, mobile-robot tracking, and passive metasurface-assisted '
        'radar NLOS became central.</p></div></div>'
    )
    if "commodity iToF, compact TCSPC" not in text:
        text = replace_once(text, old_timeline, new_timeline, "homepage 2024 timeline")

    for title in (TCSPC_TITLE, NIGHT_TITLE):
        if text.count(title) != 1:
            raise RuntimeError(f"Homepage should contain one {title!r} object, found {text.count(title)}")
    if '<b>91</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage tracked-entry count did not update to 91")
    if "Updated 13 July 2026" not in text or "Last updated: 13 July 2026" not in text:
        raise RuntimeError("Homepage dates did not update to 13 July 2026")
    write("index.html", text)


def update_survey() -> None:
    text = read("article/2active.tex")

    old_spad_table = "yeCompressedSensingActive2021} & Pulsed laser & SPAD & Time of fight &  3D reconstruction"
    new_spad_table = "yeCompressedSensingActive2021,wuMiniaturizedTCSPC2024} & Pulsed laser & SPAD & Time of fight &  3D reconstruction"
    if TCSPC_KEY not in text:
        text = replace_once(text, old_spad_table, new_spad_table, "active-table SPAD citations")

    old_tof_table = r"\cite{heideDiffuseMirrors3D2014,kadambiOccludedImagingTimeofflight2016} & Modulated laser & ToF camera"
    new_tof_table = r"\cite{heideDiffuseMirrors3D2014,kadambiOccludedImagingTimeofflight2016,caligiuriNIGHT2024} & Modulated laser & ToF camera"
    if NIGHT_KEY not in text:
        text = replace_once(text, old_tof_table, new_tof_table, "active-table ToF citations")

    tcspc_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Miniaturized TCSPC electronics.}
Compact timing electronics are becoming a deployment bottleneck rather than only detector sensitivity. Wu~\etal~integrated a four-channel TCSPC module around a commercial TDC ASIC, providing a 10\,ps bin size and 27.4\,ps minimum RMS timing resolution~\cite{wuMiniaturizedTCSPC2024}. In a 1550\,nm confocal single-photon NLOS experiment at a 5\,m sensor distance and 1\,ms pixel dwell time, the module supported 6.3\,cm lateral and 2.3\,cm depth resolution. This work moves the Velten--phasor-field sensing chain toward compact handheld or vehicle-mounted implementations by miniaturizing the timing backend rather than changing the inverse model.

'''
    if "Miniaturized TCSPC electronics." not in text:
        marker = r'''\vspace{0.8mm}
\noindent \textbf{Active Focusing for High Resolution.}
'''
        text = replace_once(text, marker, tcspc_paragraph + marker, "active-focusing section marker")

    night_paragraph = r'''Caligiuri~\etal~demonstrated that the lower-cost modulated-light branch can be pushed to commodity indirect-ToF hardware: NIGHT uses an off-the-shelf iToF sensor without additional time-resolved instrumentation and learns a virtual-mirror representation that maps multipath measurements to hidden-scene depth~\cite{caligiuriNIGHT2024}. Together with a purpose-built synthetic dataset, the method shifts consumer-ToF NLOS from analytic phase-based models toward learned reconstruction, although its reported validation remains primarily synthetic.

'''
    if "commodity indirect-ToF hardware" not in text:
        marker = r'''\bookmark[dest=\HyperLocalCurrentHref,level=3]{Active light source and interferometry}
'''
        text = replace_once(text, marker, night_paragraph + marker, "interferometry-section marker")

    if text.count(f"\\cite{{{TCSPC_KEY}}}") < 1:
        raise RuntimeError(f"Survey did not cite {TCSPC_KEY}")
    if text.count(f"\\cite{{{NIGHT_KEY}}}") < 1:
        raise RuntimeError(f"Survey did not cite {NIGHT_KEY}")
    write("article/2active.tex", text)


def main() -> None:
    source_bib = ROOT / "egbib_20260713_consumer_tof_updates.bib"
    source = source_bib.read_text(encoding="utf-8") if source_bib.exists() else ""
    for key in (NIGHT_KEY, TCSPC_KEY):
        if key not in source:
            raise RuntimeError(f"Source BibTeX record {key} is missing")
    update_readme()
    update_homepage()
    update_survey()
    print("Synchronized commodity iToF and compact TCSPC NLOS papers across README, homepage, timeline, and survey source.")


if __name__ == "__main__":
    main()
