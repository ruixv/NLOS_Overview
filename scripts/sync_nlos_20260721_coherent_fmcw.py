#!/usr/bin/env python3
"""Integrate the verified coherent-FMCW optical NLOS lineage.

The update is fail-closed: every mutation uses a unique semantic anchor and
validation rejects partial cross-artifact coverage or duplicate bibliography
records.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

DOIS = (
    "10.1103/PhysRevLett.132.233802",
    "10.1002/lpor.202401250",
    "10.1109/JLT.2024.3523206",
)
KEYS = (
    "huangCombCalibratedNLOS2024",
    "yeCombCalibratedFMCWTracking2025",
    "chenVectorEnhancedFMCWNLOS2025",
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


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    rows = (
        "| 2024 | [Non-Line-of-Sight Imaging and Vibrometry Using a Comb-Calibrated Coherent Sensor](https://doi.org/10.1103/PhysRevLett.132.233802) — Huang et al. | Physical Review Letters 2024 | Establishes coherent optical NLOS sensing with an optical-frequency-comb-calibrated FMCW LiDAR, providing sub-picosecond effective temporal resolution, submillimeter hidden-scene localization and 3D imaging, and frequency-resolved NLOS vibrometry under strong ambient light. |\n"
        "| 2025 | [High-Resolution Non-Line-of-Sight Tracking by Comb-Calibrated FMCW LiDAR](https://doi.org/10.1002/lpor.202401250) — Ye et al. | Laser & Photonics Reviews 2025 | Extends comb-calibrated coherent NLOS from static imaging to snapshot multi-object tracking, reporting 2 mm 3D position accuracy and 2 mm/s velocity accuracy without temporal accumulation. |\n"
        "| 2025 | [Non-Line-of-Sight Ranging and 3D Imaging Using Vector Enhanced Sensitive FMCW LiDAR](https://doi.org/10.1109/JLT.2024.3523206) — Chen et al. | Journal of Lightwave Technology 2025 | Uses laser-feedback interferometry, polarization-vector enhancement, and K-domain resampling for a simpler sensitive FMCW architecture, demonstrating better-than-32-µm NLOS absolute ranging and millimeter-level hidden 3D imaging at about 2.8 m. |\n"
    )
    if DOIS[0] not in text:
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + rows, "README latest-additions table")

    prl_line = "    │     Wang et al.: event-enhanced passive NLOS — asynchronous diffusion-pattern changes and physics-embedded learning reconstruct moving hidden objects [IEEE Sensors Journal]\n"
    prl_insert = "    │     Huang et al.: comb-calibrated coherent FMCW NLOS — sub-picosecond equivalent timing enables submillimeter 3D imaging and hidden-object vibrometry [Physical Review Letters]\n"
    if "comb-calibrated coherent FMCW NLOS" not in text:
        text = replace_once(text, prl_line, prl_line + prl_insert, "README 2024 timeline")

    sc_line = "    │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D blur-kernel model and correlation resampling recover 2-cm detail at 5 fps from a 16×16 detector [Optics and Lasers in Engineering]\n"
    fmcw_lines = (
        "    │     Ye et al.: comb-calibrated FMCW tracking — snapshot multi-object position and velocity recovery at 2-mm and 2-mm/s accuracy [Laser & Photonics Reviews]\n"
        "    │     Chen et al.: vector-enhanced sensitive FMCW LiDAR — laser-feedback interferometry and K-domain resampling provide micrometer ranging and millimeter hidden 3D imaging [Journal of Lightwave Technology]\n"
    )
    if "comb-calibrated FMCW tracking" not in text:
        text = replace_once(text, sc_line, sc_line + fmcw_lines, "README 2025 timeline")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    objects = (
        '      {cat:"latest active coherent fmcw lidar imaging vibrometry",title:"Non-Line-of-Sight Imaging and Vibrometry Using a Comb-Calibrated Coherent Sensor",authors:"Huang et al.",year:2024,venue:"Physical Review Letters 2024",url:"https://doi.org/10.1103/PhysRevLett.132.233802",key:"Introduces optical-frequency-comb-calibrated FMCW coherent NLOS sensing with sub-picosecond effective timing, submillimeter localization and 3D imaging, strong-ambient-light operation, and hidden-object vibrometry."},\n'
        '      {cat:"latest active coherent fmcw lidar tracking",title:"High-Resolution Non-Line-of-Sight Tracking by Comb-Calibrated FMCW LiDAR",authors:"Ye et al.",year:2025,venue:"Laser & Photonics Reviews 2025",url:"https://doi.org/10.1002/lpor.202401250",key:"Extends comb-calibrated coherent NLOS to real-time snapshot multi-object tracking, reporting 2-mm 3D position accuracy and 2-mm/s velocity accuracy without accumulation."},\n'
        '      {cat:"latest active coherent fmcw lidar ranging",title:"Non-Line-of-Sight Ranging and 3D Imaging Using Vector Enhanced Sensitive FMCW LiDAR",authors:"Chen et al.",year:2025,venue:"Journal of Lightwave Technology 2025",url:"https://doi.org/10.1109/JLT.2024.3523206",key:"Combines laser-feedback interferometry, polarization-vector enhancement, and K-domain resampling in a compact FMCW architecture, demonstrating better-than-32-micrometer NLOS ranging and millimeter-level hidden 3D imaging."},\n'
    )
    if DOIS[0] not in text:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")
        text = replace_once(
            text,
            '<div class="stat"><b>175</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>178</b><span>tracked latest entries</span></div>',
            "website tracked count",
        )

    def extend_timeline(year: int, sentence: str, token: str) -> None:
        nonlocal text
        if token in text:
            return
        pattern = re.compile(
            rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        matches = list(pattern.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"website {year} timeline: expected one block, found {len(matches)}")
        match = matches[0]
        body = match.group(2).rstrip()
        if body and not body.endswith((".", "!", "?")):
            body += "."
        replacement = match.group(1) + body + " " + sentence + match.group(3)
        text = text[:match.start()] + replacement + text[match.end():]

    extend_timeline(
        2024,
        "Comb-calibrated coherent FMCW sensing added a parallel optical route to pulsed-SPAD transients, reaching sub-picosecond equivalent timing, submillimeter hidden 3D imaging, and NLOS vibrometry.",
        "sub-picosecond equivalent timing",
    )
    extend_timeline(
        2025,
        "The coherent branch then expanded to snapshot multi-object position/velocity tracking and to a vector-enhanced laser-feedback-interferometry architecture for micrometer ranging and millimeter hidden 3D imaging.",
        "vector-enhanced laser-feedback-interferometry architecture",
    )
    write(path, text)


def update_active() -> None:
    path = "article/2active.tex"
    text = read(path)

    # The 2026 FMCW paper was previously grouped with pulsed-laser/SPAD methods.
    text = text.replace(",oyamaAdaptiveSpiralNLOS2026,liangFMCWNLOS2026,wangLaserReflectiveTomography2026", ",oyamaAdaptiveSpiralNLOS2026,wangLaserReflectiveTomography2026")

    table_anchor = r"    \cite{Willomitzer:18,xinTheoryFermatPaths2019,rezaPhasorFieldWaves2019} & Pulsed laser & Interferometer & Coherence &  3D reconstruction\\%%%% Table body" + "\n"
    coherent_row = r"    \cite{huangCombCalibratedNLOS2024,yeCombCalibratedFMCWTracking2025,chenVectorEnhancedFMCWNLOS2025,liangFMCWNLOS2026} & Frequency-swept laser & Coherent FMCW interferometer & Beat frequency, phase, and Doppler & 3D imaging / tracking / vibrometry\\%%%% Table body" + "\n"
    if KEYS[0] not in text:
        text = replace_once(text, table_anchor, table_anchor + coherent_row, "active-method table")

    prose_anchor = r"\vspace{0.8mm}" + "\n" + r"\noindent \textbf{Scan-free transient acquisition and spatial-correlation reconstruction.}"
    prose = r"""\vspace{0.8mm}
\noindent \textbf{Coherent FMCW NLOS ranging, imaging, tracking, and vibrometry.}
A coherent branch of optical NLOS replaces pulsed photon-arrival histograms with frequency-swept interferometric beat signals. Huang~\etal~calibrated FMCW LiDAR sweeps with an optical frequency comb, obtaining sub-picosecond effective temporal resolution and sufficient coherent gain for submillimeter hidden-scene localization and three-dimensional imaging under strong ambient illumination~\cite{huangCombCalibratedNLOS2024}. Because the coherent measurement also preserves frequency and phase, the same platform recovers hidden-object vibration with dozen-hertz accuracy, extending NLOS sensing beyond static geometry. Ye~\etal~subsequently used comb calibration for snapshot multi-object tracking, reporting 2\,mm three-dimensional position accuracy and 2\,mm\,s$^{-1}$ velocity accuracy without the accumulation required by many ToF or radar trackers~\cite{yeCombCalibratedFMCWTracking2025}. Chen~\etal~pursued a lower-complexity vector-enhanced sensitive FMCW design based on laser-feedback interferometry, polarization-vector enhancement, and K-domain resampling, demonstrating better-than-32-$\mu$m absolute ranging and millimeter-level hidden three-dimensional imaging at an approximately 2.8\,m NLOS distance~\cite{chenVectorEnhancedFMCWNLOS2025}. The later dual-path, fixed-delay-fiber calibration and dynamic temporal phase subdivision system~\cite{liangFMCWNLOS2026} further improved cost and sweep-linearity compensation while retaining 450-$\mu$m ranging resolution, millimeter-scale imaging, and operation beyond 8\,klux. Together, these works establish coherent FMCW LiDAR as a complementary trajectory to SPAD-based transient NLOS: it directly measures range, phase, Doppler, and vibration with fine resolution, while trading the simplicity of photon counting for interferometric calibration and coherence control.

""" + prose_anchor
    if "Coherent FMCW NLOS ranging, imaging, tracking, and vibrometry" not in text:
        text = replace_once(text, prose_anchor, prose, "coherent FMCW survey paragraph")
    write(path, text)


def update_master() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    text = text.replace("through 20 July 2026", "through 21 July 2026")
    marker = "% 21 July 2026 coherent-FMCW citation trace integrates comb-calibrated imaging/vibrometry, snapshot tracking, and vector-enhanced sensitive ranging.\n"
    if marker not in text:
        anchor = "% 21 July 2026 citation trace integrates computational neuromorphic event-camera NLOS tracking.\n"
        text = replace_once(text, anchor, anchor + marker, "master survey integration marker")
    write(path, text)


def merge_bibliography() -> None:
    subprocess.run(["python", "scripts/merge_nlos_bibliography.py"], cwd=ROOT, check=True)


def validate() -> None:
    readme = read("README.md")
    index = read("index.html")
    active = read("article/2active.tex")
    bib = read("egbib_merged_20260711.bib")
    master = read("bare_jrnl.tex")
    for doi in DOIS:
        if readme.count(doi) != 1:
            raise RuntimeError(f"README DOI coverage error: {doi}")
        if index.count(doi) != 1:
            raise RuntimeError(f"website DOI coverage error: {doi}")
        if bib.lower().count(("doi = {" + doi + "}").lower()) != 1:
            raise RuntimeError(f"bibliography DOI coverage error: {doi}")
    for key in KEYS:
        if active.count(key) != 2:  # active table plus literature-review paragraph
            raise RuntimeError(f"active survey citation coverage error: {key}")
        if bib.count("{" + key + ",") != 1:
            raise RuntimeError(f"bibliography key coverage error: {key}")
    if active.count("liangFMCWNLOS2026") != 2:
        raise RuntimeError("2026 FMCW endpoint must occur in the coherent table and prose only")
    if "through 21 July 2026" not in master:
        raise RuntimeError("master survey coverage date was not updated")
    if '<div class="stat"><b>178</b><span>tracked latest entries</span></div>' not in index:
        raise RuntimeError("website tracked-entry count is inconsistent")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_master()
    merge_bibliography()
    validate()
    print("Integrated and validated the coherent FMCW optical NLOS lineage.")


if __name__ == "__main__":
    main()
