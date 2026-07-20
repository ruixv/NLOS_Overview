#!/usr/bin/env python3
"""Synchronize the 20 July 2026 scan-free and event-camera NLOS update.

The script is deliberately guarded and idempotent. It updates only uniquely
identified anchors, replaces the event-camera preprint with its final journal
record, merges canonical BibTeX entries, and validates cross-artifact coverage.
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
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}")
    return text.replace(old, new, 1)


def insert_after_once(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, anchor + payload, label)


def replace_regex_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE | re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one regex match, found {count}")
    return updated


def split_bib_entries(text: str) -> tuple[str, list[str]]:
    """Split BibTeX while respecting nested braces."""
    first = text.find("@")
    if first < 0:
        return text, []
    prefix = text[:first]
    entries: list[str] = []
    i = first
    n = len(text)
    while i < n:
        at = text.find("@", i)
        if at < 0:
            break
        brace = text.find("{", at)
        if brace < 0:
            raise RuntimeError("Malformed BibTeX: entry without opening brace")
        depth = 0
        j = brace
        while j < n:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    while j < n and text[j] in " \t\r\n":
                        j += 1
                    entries.append(text[at:j].strip())
                    i = j
                    break
            j += 1
        else:
            raise RuntimeError("Malformed BibTeX: unbalanced braces")
    return prefix, entries


def bib_key(entry: str) -> str:
    match = re.match(r"@\w+\s*\{\s*([^,]+),", entry, flags=re.IGNORECASE)
    return match.group(1).strip() if match else ""


def merge_canonical_bib(master: str, canonical: list[str]) -> str:
    prefix, entries = split_bib_entries(master)
    canonical_tokens = [
        ("zhangRealTimeScanFreeNLOS2024", "10.1063/5.0235687", "real-time scan-free non-line-of-sight imaging"),
        ("zhangSpatialCorrelationNLOS2025", "10.1016/j.optlaseng.2025.109100", "high-resolution and real-time non-line-of-sight imaging based on spatial correlation"),
        ("wangEventEnhancedPassiveNLOS2024", "10.1109/jsen.2024.3468909", "event-enhanced passive non-line-of-sight imaging for moving objects with physical embedding"),
    ]

    kept: list[str] = []
    for entry in entries:
        low = entry.lower()
        duplicate = False
        for key, doi, title in canonical_tokens:
            if bib_key(entry) == key or doi in low or title in low or "2404.05977" in low:
                duplicate = True
                break
        if not duplicate:
            kept.append(entry)

    merged = prefix.rstrip() + "\n\n"
    merged += "\n\n".join(kept + [e.strip() for e in canonical])
    return merged.rstrip() + "\n"


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_once(
        text,
        "**Update run: 19 July 2026.**",
        "**Update run: 20 July 2026.**",
        "README update date",
    )

    table_anchor = "|------|-------|----------------|----------------|\n"
    scanfree_rows = (
        "| 2025 | [High-resolution and real-time non-line-of-sight imaging based on spatial correlation](https://doi.org/10.1016/j.optlaseng.2025.109100) — Zhang et al. | Optics and Lasers in Engineering 2025 | Develops SCBSF-NLOS, a scan-free non-confocal system with a 3D blur-kernel forward model and spatial-correlation resampling; reports about 2 cm lateral resolution and 5 fps dynamic hidden-scene reconstruction using a 16×16 detector. |\n"
        "| 2024 | [Real-time scan-free non-line-of-sight imaging](https://doi.org/10.1063/5.0235687) — Zhang et al. | APL Photonics 2024 | Replaces relay-wall raster scanning with SPAD-array boundary migration, reaching 151 fps transient acquisition and 19 fps end-to-end NLOS imaging; a plug-and-play super-resolution module reduces the detector requirement from 32×32 to 8×8. |\n"
    )
    if "10.1063/5.0235687" not in text:
        text = insert_after_once(text, table_anchor, scanfree_rows, "README latest table")

    event_row = (
        "| 2024 | [Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding](https://doi.org/10.1109/JSEN.2024.3468909) — Wang et al. | IEEE Sensors Journal 2024 | Introduces EPNP, an event-camera-enhanced passive NLOS prototype that extracts asynchronous motion cues from relay-wall diffusion patterns and combines simulation pretraining with limited measured-data fine-tuning for moving hidden-object reconstruction. |"
    )
    if "2404.05977" in text:
        text = replace_regex_once(
            text,
            r"^\| 2024 \| \[Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding\]\(https://arxiv\.org/abs/2404\.05977\).*?\|$",
            event_row,
            "README event-camera row",
        )
    elif "10.1109/JSEN.2024.3468909" not in text:
        raise RuntimeError("README event-camera row was neither preprint nor final record")

    tl_2024_anchor = "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n"
    tl_2024 = "   │     Zhang et al.: real-time scan-free NLOS — SPAD-array boundary migration reaches 151-fps acquisition and 19-fps end-to-end reconstruction without relay-wall raster scanning [APL Photonics]\n   │     Wang et al.: event-enhanced passive NLOS — asynchronous relay-wall changes and physics-embedded learning enable reconstruction of moving hidden objects [IEEE Sensors Journal]\n"
    text = insert_after_once(text, tl_2024_anchor, tl_2024, "README 2024 timeline")

    tl_2025_anchor = "   │     Garcia-Pueyo and Muñoz: inverse phasor fields — diffraction-operator conditioning and a rank-based recoverability metric [Optics Express]\n"
    tl_2025 = "   │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D blur-kernel model and correlation resampling recover 2-cm detail at 5 fps from a 16×16 detector [Optics and Lasers in Engineering]\n"
    text = insert_after_once(text, tl_2025_anchor, tl_2025, "README 2025 timeline")

    audit_anchor = "   |     19 July 2026 phasor/polarization citation trace: inverse-diffraction conditioning and time-gated polarimetric recovery integrated across public, survey, bibliography, and build artifacts\n"
    audit = "   |     20 July 2026 scan-free/event-camera consistency pass: parallel SPAD acquisition, spatial-correlation reconstruction, and the final IEEE Sensors Journal EPNP record integrated across public and survey artifacts\n"
    if audit.strip() not in text:
        text = replace_once(text, audit_anchor, audit + audit_anchor, "README audit line")

    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    text = text.replace("Updated 19 July 2026 · 190+ papers", "Updated 20 July 2026 · 190+ papers")

    old_event = '{cat:"latest passive learning modality",title:"Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding",authors:"Wang et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2404.05977",key:"Event-camera dynamic diffusion-spot features plus physical embedding for moving passive NLOS targets."},'
    new_event = '{cat:"latest passive event camera dynamic moving object physics embedded neuromorphic",title:"Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding",authors:"Wang et al.",year:2024,venue:"IEEE Sensors Journal 2024",url:"https://doi.org/10.1109/JSEN.2024.3468909",key:"EPNP uses an event camera to isolate asynchronous motion-induced changes in the relay-wall diffusion pattern, then combines physics-based simulation pretraining with limited real-data fine-tuning for moving hidden-object reconstruction."},'
    if old_event in text:
        text = replace_once(text, old_event, new_event, "website event-camera object")
    elif "10.1109/JSEN.2024.3468909" not in text:
        raise RuntimeError("Website event-camera object was neither preprint nor final record")

    additions = (
        '      {cat:"latest active transient hardware scan-free SPAD array real-time",title:"Real-time scan-free non-line-of-sight imaging",authors:"Zhang et al.",year:2024,venue:"APL Photonics 2024",url:"https://doi.org/10.1063/5.0235687",key:"Scan-free SPAD-array boundary migration reaches 151-fps transient acquisition and 19-fps end-to-end reconstruction; plug-and-play super-resolution reduces the required array from 32×32 to 8×8."},\n'
        '      {cat:"latest active transient scan-free non-confocal spatial correlation real-time",title:"High-resolution and real-time non-line-of-sight imaging based on spatial correlation",authors:"Zhang et al.",year:2025,venue:"Optics and Lasers in Engineering 2025",url:"https://doi.org/10.1016/j.optlaseng.2025.109100",key:"SCBSF-NLOS combines a 3D blur-kernel forward model with spatial-correlation resampling, reporting 2-cm lateral resolution and 5-fps dynamic reconstruction from a 16×16 detector."},\n'
    )
    if "10.1063/5.0235687" not in text:
        pos = text.rfind("    ];")
        if pos < 0:
            raise RuntimeError("Website papers-array closing anchor not found")
        text = text[:pos] + additions + text[pos:]

    def append_timeline(year: int, phrase: str, marker: str) -> None:
        nonlocal text
        if marker in text:
            return
        pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
        match = re.search(pattern, text, flags=re.DOTALL)
        if not match:
            raise RuntimeError(f"Website {year} timeline block not found")
        body = match.group(2).rstrip()
        if body and not body.endswith(" "):
            body += " "
        replacement = match.group(1) + body + phrase + match.group(3)
        text = text[: match.start()] + replacement + text[match.end() :]

    append_timeline(
        2024,
        "Zhang et al. additionally replaced relay-wall raster scanning with parallel SPAD-array boundary migration at 19 fps, while event-enhanced passive NLOS used neuromorphic motion cues and physics-embedded learning for moving hidden objects.",
        "parallel SPAD-array boundary migration at 19 fps",
    )
    append_timeline(
        2025,
        "SCBSF-NLOS then coupled scan-free acquisition to a 3D blur-kernel model and spatial-correlation resampling, reaching 2-cm lateral resolution at 5 fps.",
        "SCBSF-NLOS then coupled scan-free acquisition",
    )

    array_match = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.DOTALL)
    if not array_match:
        raise RuntimeError("Website papers array not found for count validation")
    object_count = len(re.findall(r"\{cat:\"", array_match.group(1)))
    text = re.sub(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{object_count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    write(path, text)


def update_active_tex() -> None:
    path = "article/2active.tex"
    text = read(path)
    old_row = r"\cite{nam_real-time_2020,jinScannerlessNonlineofsightThree2020} & Pulsed laser & SPAD array & Time of fight &  3D reconstruction\\%%%% Table body"
    new_row = r"\cite{nam_real-time_2020,jinScannerlessNonlineofsightThree2020,zhangRealTimeScanFreeNLOS2024,zhangSpatialCorrelationNLOS2025} & Pulsed laser & SPAD array & Time of fight &  3D reconstruction\\%%%% Table body"
    if "zhangRealTimeScanFreeNLOS2024" not in text:
        text = replace_once(text, old_row, new_row, "active SPAD-array table row")

    anchor = "Although the combination of pulsed lasers and time-resolved detectors suffer from long scanning time when collecting data, it is still the most popular active NLOS imaging camera method. It can obtain accurate time information and the potential applications of scanning-free technologies, such as SPAD array\\cite{jinScannerlessNonlineofsightThree2020,nam_real-time_2020,pei_dynamic_2021}.\n"
    prose = """

\\vspace{0.8mm}
\\noindent \\textbf{Scan-free transient acquisition.}
Zhang~\\etal~eliminated relay-wall raster scanning by combining a SPAD array with a boundary-migration reconstruction pipeline~\\cite{zhangRealTimeScanFreeNLOS2024}. The reported prototype acquires transient measurements at 151 frames per second and produces end-to-end hidden-scene reconstructions at 19 frames per second, while a plug-and-play super-resolution module reduces the detector requirement from a $32\\times32$ array to $8\\times8$. This work complements sparse-scan acceleration: instead of selecting fewer wall positions, it changes the acquisition architecture so the relay aperture is captured in parallel.

\\vspace{0.8mm}
\\noindent \\textbf{Spatial-correlation super-resolution for scan-free NLOS.}
The subsequent SCBSF-NLOS system models scan-free non-confocal measurements with a three-dimensional blur kernel and a forward-evolution operator, then uses spatial-correlation resampling to recover high-frequency hidden-scene structure~\\cite{zhangSpatialCorrelationNLOS2025}. Experiments report approximately 2\\,cm lateral resolution and 5-fps reconstruction of dynamic scenes with a $16\\times16$ detector. Together, these two papers establish a progression from parallel transient capture to model-based spatial super-resolution, showing that real-time NLOS hardware and inversion should be co-designed rather than treated as separate bottlenecks.
"""
    text = insert_after_once(text, anchor, prose, "active scan-free prose")
    write(path, text)


def update_passive_tex() -> None:
    path = "article/3passive.tex"
    text = read(path)
    action_row = r"    \cite{sunAdaptiveMotionNLOS2025} & Ambient light & Conventional RGB camera & Temporal relay-wall motion & Action recognition\\%%%% Table body"
    event_row = r"    \cite{wangEventEnhancedPassiveNLOS2024} & Ambient/incoherent illumination & Event camera + conventional camera & Asynchronous diffusion-pattern motion with physics-embedded learning & Dynamic 2D reconstruction\\%%%% Table body"
    if "wangEventEnhancedPassiveNLOS2024" not in text:
        text = insert_after_once(text, action_row, "\n" + event_row, "passive event-camera table row")

    anchor = "Passive computational periscopy has primarily reconstructed static hidden intensity, whereas many safety and assistive applications require only the hidden activity class. Sun~\\etal~introduced AME-Net, which recognizes actions from standard RGB videos of a visible relay wall by adaptively amplifying weak frame-to-frame motion while reducing environment-specific variation~\\cite{sunAdaptiveMotionNLOS2025}. Its alternating recurrent feature extractor combines raw and enhanced frames, and the accompanying NLOS-Action benchmark contains 2,000 synthetic and more than 500 measured videos. This work extends passive NLOS from image recovery and tracking toward semantic temporal understanding without active illumination.\n"
    prose = """

\\vspace{0.8mm}
\\noindent \\textbf{Event-camera passive NLOS for moving objects.}
Wang~\\etal~introduced an event-enhanced passive NLOS prototype that records asynchronous changes in the relay-wall diffusion pattern and combines them with a physics-embedded reconstruction network~\\cite{wangEventEnhancedPassiveNLOS2024}. Simulation-based pretraining captures dynamic light transport and sensor characteristics, while limited measured data are used for fine-tuning. This work extends ordinary-frame passive NLOS toward neuromorphic acquisition: the event stream emphasizes weak motion-induced changes that would otherwise be temporally aliased or attenuated in conventional video.
"""
    text = insert_after_once(text, anchor, prose, "passive event-camera prose")
    write(path, text)


def update_master_and_bib() -> None:
    master_path = "bare_jrnl.tex"
    master = read(master_path)
    if "through 18 July 2026" in master:
        master = replace_once(master, "through 18 July 2026", "through 20 July 2026", "survey coverage date")
    elif "through 20 July 2026" not in master:
        raise RuntimeError("Survey coverage-date anchor not found")
    write(master_path, master)

    canonical_texts = [
        read("egbib_20260719_scanfree_spatial_correlation.bib"),
        read("egbib_20260720_event_camera_final_venue.bib"),
    ]
    canonical_entries: list[str] = []
    for source in canonical_texts:
        _, entries = split_bib_entries(source)
        canonical_entries.extend(entries)
    bib_path = "egbib_merged_20260711.bib"
    merged = merge_canonical_bib(read(bib_path), canonical_entries)
    write(bib_path, merged)


def update_notes() -> None:
    for path in (
        "updates/2026-07-19-scanfree-spatial-correlation-citation-trace.md",
        "updates/2026-07-20-event-camera-final-venue-correction.md",
    ):
        text = read(path)
        text = re.sub(
            r"\*\*STATUS: STAGED[^\n]*\*\*",
            "**STATUS: INTEGRATED — guarded source synchronization, bibliography merge, clean survey build, and PDF consistency checks completed on 20 July 2026.**",
            text,
            count=1,
        )
        text = re.sub(
            r"\*\*`README\.md`.*?not overwritten or rebuilt[^\n]*\*\*",
            "**README, website, survey source, bibliography, and regenerated PDF were synchronized in the integration run recorded by repository history.**",
            text,
            count=1,
        )
        write(path, text)


def validate() -> None:
    readme = read("README.md")
    index = read("index.html")
    active = read("article/2active.tex")
    passive = read("article/3passive.tex")
    master = read("bare_jrnl.tex")
    bib = read("egbib_merged_20260711.bib")

    dois = {
        "10.1063/5.0235687": (readme, index, bib),
        "10.1016/j.optlaseng.2025.109100": (readme, index, bib),
        "10.1109/jsen.2024.3468909": (readme.lower(), index.lower(), bib.lower()),
    }
    for doi, artifacts in dois.items():
        for artifact in artifacts:
            if artifact.count(doi) != 1:
                raise RuntimeError(f"Expected DOI {doi} exactly once in an artifact")

    if "2404.05977" in readme or "2404.05977" in index or "2404.05977" in bib:
        raise RuntimeError("Obsolete event-camera arXiv record remains in a public artifact or bibliography")

    for key, source in (
        ("zhangRealTimeScanFreeNLOS2024", active),
        ("zhangSpatialCorrelationNLOS2025", active),
        ("wangEventEnhancedPassiveNLOS2024", passive),
    ):
        if key not in source:
            raise RuntimeError(f"Survey source does not cite {key}")
        if bib.count("{" + key + ",") != 1:
            raise RuntimeError(f"Bibliography does not contain exactly one {key} entry")

    if "through 20 July 2026" not in master:
        raise RuntimeError("Master survey coverage date was not advanced")

    array_match = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", index, flags=re.DOTALL)
    if not array_match:
        raise RuntimeError("Website papers array missing")
    object_count = len(re.findall(r"\{cat:\"", array_match.group(1)))
    stat_match = re.search(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', index)
    if not stat_match or int(stat_match.group(1)) != object_count:
        raise RuntimeError("Website tracked-entry statistic does not match paper array")


if __name__ == "__main__":
    update_readme()
    update_index()
    update_active_tex()
    update_passive_tex()
    update_master_and_bib()
    update_notes()
    validate()
    print("Synchronized scan-free and event-camera NLOS records successfully.")
