#!/usr/bin/env python3
"""Final guarded source synchronization for the 20 July 2026 NLOS pass.

Integrates two scan-free active-NLOS papers, upgrades the event-camera paper to
its final IEEE Sensors Journal record, and completes public/survey coverage of
the PRL polarization-speckle single-pixel milestone. The repository's PR
validation workflow is responsible for rebuilding and validating the PDF.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def insert_after(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, anchor + payload, label)


def insert_before(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, payload + anchor, label)


def split_bib(text: str) -> tuple[str, list[str]]:
    first = text.find("@")
    if first < 0:
        return text, []
    prefix = text[:first]
    entries: list[str] = []
    i = first
    while i < len(text):
        at = text.find("@", i)
        if at < 0:
            break
        brace = text.find("{", at)
        if brace < 0:
            raise RuntimeError("Malformed BibTeX entry")
        depth = 0
        j = brace
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    entries.append(text[at:j].strip())
                    i = j
                    break
            j += 1
        else:
            raise RuntimeError("Unbalanced BibTeX entry")
    return prefix, entries


def bib_key(entry: str) -> str:
    match = re.match(r"@\w+\s*\{\s*([^,]+),", entry, flags=re.I)
    return match.group(1).strip() if match else ""


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = text.replace("**Update run: 19 July 2026.**", "**Update run: 20 July 2026.**")

    header = "|------|-------|----------------|----------------|\n"
    rows = []
    if "10.1103/kd8v-fykm" not in text:
        rows.append(
            "| 2026 | [Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation](https://doi.org/10.1103/kd8v-fykm) — Zhou et al. | Physical Review Letters 2026 | Uses polarization-controlled relay-wall speckles as diverse scanning-free illumination patterns and a single-pixel detector to recover keyhole-hidden scenes with millimeter-scale detail; angular-memory-effect calibration avoids invasive access to the hidden region. |\n"
        )
    if "10.1016/j.optlaseng.2025.109100" not in text:
        rows.append(
            "| 2025 | [High-resolution and real-time non-line-of-sight imaging based on spatial correlation](https://doi.org/10.1016/j.optlaseng.2025.109100) — Zhang et al. | Optics and Lasers in Engineering 2025 | Develops SCBSF-NLOS, a scan-free non-confocal system with a 3D blur-kernel forward model and spatial-correlation resampling; reports about 2 cm lateral resolution and 5 fps dynamic reconstruction from a 16×16 detector. |\n"
        )
    if "10.1063/5.0235687" not in text:
        rows.append(
            "| 2024 | [Real-time scan-free non-line-of-sight imaging](https://doi.org/10.1063/5.0235687) — Zhang et al. | APL Photonics 2024 | Replaces relay-wall raster scanning with parallel SPAD-array acquisition and boundary migration, reaching 151 fps transient capture and 19 fps end-to-end imaging; plug-and-play super-resolution reduces the array requirement from 32×32 to 8×8. |\n"
        )
    if rows:
        text = insert_after(text, header, "".join(rows), "README latest-additions header")

    final_event = (
        "| 2024 | [Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding](https://doi.org/10.1109/JSEN.2024.3468909) — Wang et al. | IEEE Sensors Journal 2024 | Uses an event camera to extract asynchronous motion cues from relay-wall diffusion patterns and combines physics-based simulation pretraining with limited measured-data fine-tuning for moving hidden-object reconstruction. |"
    )
    if "2404.05977" in text:
        text, n = re.subn(
            r"^\| 2024 \| \[Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding\]\(https://arxiv\.org/abs/2404\.05977\).*?\|$",
            final_event,
            text,
            count=1,
            flags=re.M,
        )
        if n != 1:
            raise RuntimeError("README event-camera preprint row not found")
    elif "10.1109/JSEN.2024.3468909" not in text:
        raise RuntimeError("README event-camera record missing")

    anchor_2024 = "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n"
    extra_2024 = (
        "   │     Zhang et al.: real-time scan-free NLOS — parallel SPAD-array boundary migration reaches 151-fps acquisition and 19-fps end-to-end reconstruction [APL Photonics]\n"
        "   │     Wang et al.: event-enhanced passive NLOS — asynchronous diffusion-pattern changes and physics-embedded learning reconstruct moving hidden objects [IEEE Sensors Journal]\n"
    )
    text = insert_after(text, anchor_2024, extra_2024, "README 2024 timeline")

    anchor_2025 = "   │     Garcia-Pueyo and Muñoz: inverse phasor fields — diffraction-operator conditioning and a rank-based recoverability metric [Optics Express]\n"
    extra_2025 = "   │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D blur-kernel model and correlation resampling recover 2-cm detail at 5 fps from a 16×16 detector [Optics and Lasers in Engineering]\n"
    text = insert_after(text, anchor_2025, extra_2025, "README 2025 timeline")

    if "20 July 2026 scan-free/event-camera consistency pass" not in text:
        marker = "   |     19 July 2026 phasor/polarization citation trace: inverse-diffraction conditioning and time-gated polarimetric recovery integrated across public, survey, bibliography, and build artifacts\n"
        audit = "   |     20 July 2026 scan-free/event-camera consistency pass: parallel transient acquisition, spatial-correlation reconstruction, the final EPNP venue, and PRL polarization-speckle coverage synchronized across public and survey sources\n"
        text = insert_before(text, marker, audit, "README update audit")

    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    text = text.replace("Updated 19 July 2026 · 190+ papers", "Updated 20 July 2026 · 190+ papers")

    old_event = '{cat:"latest passive learning modality",title:"Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding",authors:"Wang et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2404.05977",key:"Event-camera dynamic diffusion-spot features plus physical embedding for moving passive NLOS targets."},'
    new_event = '{cat:"latest passive event camera dynamic moving object physics embedded neuromorphic",title:"Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding",authors:"Wang et al.",year:2024,venue:"IEEE Sensors Journal 2024",url:"https://doi.org/10.1109/JSEN.2024.3468909",key:"EPNP uses asynchronous event-camera cues from relay-wall diffusion patterns and physics-based simulation pretraining with limited real-data fine-tuning for moving hidden-object reconstruction."},'
    if old_event in text:
        text = replace_once(text, old_event, new_event, "website event-camera object")
    elif "10.1109/JSEN.2024.3468909" not in text:
        raise RuntimeError("Website event-camera object missing")

    additions: list[str] = []
    if "10.1063/5.0235687" not in text:
        additions.append('      {cat:"latest active transient hardware scan-free SPAD array real-time",title:"Real-time scan-free non-line-of-sight imaging",authors:"Zhang et al.",year:2024,venue:"APL Photonics 2024",url:"https://doi.org/10.1063/5.0235687",key:"Parallel SPAD-array boundary migration reaches 151-fps transient acquisition and 19-fps end-to-end reconstruction; super-resolution reduces the array requirement from 32×32 to 8×8."},\n')
    if "10.1016/j.optlaseng.2025.109100" not in text:
        additions.append('      {cat:"latest active transient scan-free non-confocal spatial correlation real-time",title:"High-resolution and real-time non-line-of-sight imaging based on spatial correlation",authors:"Zhang et al.",year:2025,venue:"Optics and Lasers in Engineering 2025",url:"https://doi.org/10.1016/j.optlaseng.2025.109100",key:"SCBSF-NLOS combines a 3D blur-kernel model with spatial-correlation resampling, reporting 2-cm lateral resolution and 5-fps dynamic reconstruction from a 16×16 detector."},\n')
    if "10.1103/kd8v-fykm" not in text:
        additions.append('      {cat:"latest active polarization speckle single pixel scan-free keyhole",title:"Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation",authors:"Zhou et al.",year:2026,venue:"Physical Review Letters 2026",url:"https://doi.org/10.1103/kd8v-fykm",key:"Polarization-controlled relay-wall speckles encode hidden scenes for scanning-free single-pixel keyhole NLOS imaging with millimeter-scale detail and noninvasive angular-memory-effect calibration."},\n')
    if additions:
        pos = text.rfind("    ];")
        if pos < 0:
            raise RuntimeError("Website paper-array closing anchor missing")
        text = text[:pos] + "".join(additions) + text[pos:]

    def append_timeline(year: int, sentence: str, token: str) -> None:
        nonlocal text
        if token in text:
            return
        pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
        match = re.search(pattern, text, flags=re.S)
        if not match:
            raise RuntimeError(f"Website {year} timeline block missing")
        body = match.group(2).rstrip() + " " + sentence
        text = text[:match.start()] + match.group(1) + body + match.group(3) + text[match.end():]

    append_timeline(2024, "Parallel SPAD-array acquisition then removed relay-wall raster scanning at 19 fps, while event-enhanced passive sensing exploited neuromorphic motion cues.", "removed relay-wall raster scanning at 19 fps")
    append_timeline(2025, "SCBSF-NLOS coupled scan-free capture to a 3D blur-kernel model and spatial-correlation super-resolution, reaching 2-cm detail at 5 fps.", "spatial-correlation super-resolution")
    append_timeline(2026, "Polarization-speckle modulation added a scanning-free single-pixel keyhole branch with millimeter-scale recovery.", "single-pixel keyhole branch")

    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.S)
    if not array:
        raise RuntimeError("Website papers array missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    text, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError("Website tracked-entry statistic missing")
    write(path, text)


def update_active() -> None:
    path = "article/2active.tex"
    text = read(path)
    old = r"\cite{nam_real-time_2020,jinScannerlessNonlineofsightThree2020} & Pulsed laser & SPAD array & Time of fight &  3D reconstruction\\%%%% Table body"
    new = r"\cite{nam_real-time_2020,jinScannerlessNonlineofsightThree2020,zhangRealTimeScanFreeNLOS2024,zhangSpatialCorrelationNLOS2025} & Pulsed laser & SPAD array & Time of fight &  3D reconstruction\\%%%% Table body"
    if "zhangRealTimeScanFreeNLOS2024" not in text:
        text = replace_once(text, old, new, "active SPAD-array table row")

    scan_anchor = "Although the combination of pulsed lasers and time-resolved detectors suffer from long scanning time when collecting data, it is still the most popular active NLOS imaging camera method. It can obtain accurate time information and the potential applications of scanning-free technologies, such as SPAD array\\cite{jinScannerlessNonlineofsightThree2020,nam_real-time_2020,pei_dynamic_2021}.\n"
    scan_prose = """

\\vspace{0.8mm}
\\noindent \\textbf{Scan-free transient acquisition and spatial-correlation reconstruction.}
Zhang~\\etal~eliminated relay-wall raster scanning by combining parallel SPAD-array capture with boundary-migration reconstruction~\\cite{zhangRealTimeScanFreeNLOS2024}. The system reports 151-fps transient acquisition and 19-fps end-to-end hidden-scene imaging, while plug-and-play super-resolution reduces the required detector array from $32\\times32$ to $8\\times8$. Their subsequent SCBSF-NLOS formulation models scan-free non-confocal measurements using a three-dimensional blur kernel and forward-evolution operator, then applies spatial-correlation resampling to restore high-frequency structure~\\cite{zhangSpatialCorrelationNLOS2025}. Experiments report approximately 2\\,cm lateral resolution and 5-fps dynamic reconstruction with a $16\\times16$ detector. Together these papers shift real-time NLOS from sparse sequential scanning toward co-designed parallel acquisition and model-based spatial super-resolution.
"""
    if "Scan-free transient acquisition and spatial-correlation reconstruction" not in text:
        text = insert_after(text, scan_anchor, scan_prose, "active scan-free prose")

    wave_anchor = "\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Wave-based model}\n"
    pol_prose = """
\\vspace{0.8mm}
\\noindent \\textbf{Polarization-speckle single-pixel NLOS.}
Zhou~\\etal~introduced a complementary scanning-free polarization route in which changing the incident polarization produces diverse speckle illuminations after reflection from a rough relay wall~\\cite{zhouPolarizationSpeckleNLOS2026}. A single-pixel detector records the corresponding hidden-scene responses, and the angular memory effect supports noninvasive calibration without direct access to the hidden region. The demonstrated keyhole system recovers millimeter-scale detail. Unlike time-gated polarimetry, which augments transient transport with directional observability, polarization-speckle modulation uses polarization diversity as the illumination code itself and therefore opens a single-pixel active-NLOS branch without spatial relay scanning.

"""
    if "Polarization-speckle single-pixel NLOS" not in text:
        text = insert_before(text, wave_anchor, pol_prose, "active polarization prose")
    write(path, text)


def update_passive() -> None:
    path = "article/3passive.tex"
    text = read(path)
    key = "wangEventEnhancedPassiveNLOS2024"
    if key not in text:
        row_anchor = "   \\cite{sunAdaptiveMotionNLOS2025} & Ambient light & Conventional RGB camera & Temporal relay-wall motion & Action recognition\\\\%%%% Table body\n"
        event_row = "   \\cite{wangEventEnhancedPassiveNLOS2024} & Ambient/incoherent illumination & Event camera + conventional camera & Asynchronous diffusion-pattern motion with physics-embedded learning & Dynamic 2D reconstruction\\\\%%%% Table body\n"
        text = insert_after(text, row_anchor, event_row, "passive event-camera table row")

    heading = "\\vspace{0.8mm}\n\\noindent \\textbf{Structure-guided adaptive total variation.}"
    prose = """\\vspace{0.8mm}
\\noindent \\textbf{Event-camera passive NLOS for moving objects.}
Wang~\\etal~used an event camera to isolate asynchronous motion-induced changes in relay-wall diffusion patterns and combined these measurements with a physics-embedded reconstruction network~\\cite{wangEventEnhancedPassiveNLOS2024}. Simulation-based pretraining models dynamic light transport and sensor behavior, followed by fine-tuning on limited measured data. This extends frame-based passive NLOS toward neuromorphic acquisition, emphasizing weak temporal changes that would otherwise be attenuated or aliased in conventional video.

"""
    if "Event-camera passive NLOS for moving objects" not in text:
        text = insert_before(text, heading, prose, "passive event-camera prose")
    write(path, text)


def update_master_bib_notes() -> None:
    master_path = "bare_jrnl.tex"
    master = read(master_path)
    master = master.replace("through 18 July 2026", "through 20 July 2026")
    master = master.replace("through 19 July 2026", "through 20 July 2026")
    write(master_path, master)

    canonical_sources = [
        "egbib_20260719_scanfree_spatial_correlation.bib",
        "egbib_20260720_event_camera_final_venue.bib",
        "egbib_20260720_polarization_single_pixel.bib",
    ]
    canonical: list[str] = []
    for source in canonical_sources:
        _, entries = split_bib(read(source))
        canonical.extend(entries)

    bib_path = "egbib_merged_20260711.bib"
    prefix, entries = split_bib(read(bib_path))
    keys = {bib_key(e) for e in canonical}
    tokens = (
        "10.1063/5.0235687",
        "10.1016/j.optlaseng.2025.109100",
        "10.1109/jsen.2024.3468909",
        "2404.05977",
        "10.1103/kd8v-fykm",
        "event-enhanced passive non-line-of-sight imaging for moving objects with physical embedding",
    )
    kept = []
    for entry in entries:
        low = entry.lower()
        if bib_key(entry) in keys or any(token in low for token in tokens):
            continue
        kept.append(entry)
    merged = prefix.rstrip() + "\n\n" + "\n\n".join(kept + canonical) + "\n"
    write(bib_path, merged)

    for note_path in (
        "updates/2026-07-19-scanfree-spatial-correlation-citation-trace.md",
        "updates/2026-07-20-event-camera-final-venue-correction.md",
    ):
        note = read(note_path)
        note = re.sub(r"\*\*STATUS: STAGED[^\n]*\*\*", "**STATUS: SOURCE-INTEGRATED — public pages, survey sections, and canonical bibliography synchronized on 20 July 2026; PDF status is determined by the repository validation workflow.**", note, count=1)
        write(note_path, note)


def validate() -> None:
    artifacts = {
        "README": read("README.md"),
        "website": read("index.html"),
        "active": read("article/2active.tex"),
        "passive": read("article/3passive.tex"),
        "master": read("bare_jrnl.tex"),
        "bib": read("egbib_merged_20260711.bib"),
    }
    for doi in ("10.1063/5.0235687", "10.1016/j.optlaseng.2025.109100", "10.1103/kd8v-fykm"):
        if artifacts["README"].count(doi) != 1 or artifacts["website"].count(doi) != 1 or doi not in artifacts["bib"]:
            raise RuntimeError(f"Cross-artifact DOI validation failed: {doi}")
    event = "10.1109/jsen.2024.3468909"
    if artifacts["README"].lower().count(event) != 1 or artifacts["website"].lower().count(event) != 1 or event not in artifacts["bib"].lower():
        raise RuntimeError("Event-camera final DOI validation failed")
    if any("2404.05977" in artifacts[name] for name in ("README", "website", "bib")):
        raise RuntimeError("Obsolete event-camera preprint metadata remains")
    for key, section in (
        ("zhangRealTimeScanFreeNLOS2024", "active"),
        ("zhangSpatialCorrelationNLOS2025", "active"),
        ("zhouPolarizationSpeckleNLOS2026", "active"),
        ("wangEventEnhancedPassiveNLOS2024", "passive"),
    ):
        if key not in artifacts[section] or artifacts["bib"].count("{" + key + ",") != 1:
            raise RuntimeError(f"Citation/BibTeX validation failed: {key}")
    if "through 20 July 2026" not in artifacts["master"]:
        raise RuntimeError("Survey coverage date not updated")
    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", artifacts["website"], flags=re.S)
    stat = re.search(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', artifacts["website"])
    if not array or not stat:
        raise RuntimeError("Website paper-array/statistic missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    if int(stat.group(1)) != count:
        raise RuntimeError(f"Website count mismatch: {stat.group(1)} != {count}")


if __name__ == "__main__":
    update_readme()
    update_index()
    update_active()
    update_passive()
    update_master_bib_notes()
    validate()
    print("Final 20 July 2026 NLOS source synchronization completed.")
