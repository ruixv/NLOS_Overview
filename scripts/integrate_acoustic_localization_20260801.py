#!/usr/bin/env python3
"""Synchronize two verified acoustic NLOS localization papers.

Edits are bounded and idempotent. The companion workflow consolidates the
bibliography, rebuilds the PDF, and validates every public artifact.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VEHICLE_TITLE = "Non-Line-of-Sight Vehicle Localization Based on Sound"
VEHICLE_KEY = "jeonSoundVehicleNLOS2025"
EDGE_TITLE = (
    "Localizing acoustic sources in non-line-of-sight scenarios using "
    "irregular-grid beamforming and first-order edge diffraction"
)
EDGE_KEY = "zhaiIrregularGridAcousticNLOS2025"


def require_once(text: str, needle: str, label: str) -> None:
    count = text.count(needle)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {count}")


def insert_latest_row(text: str, title: str, row: str) -> str:
    if title in text:
        return text
    anchor = "|------|-------|----------------|----------------|\n"
    require_once(text, anchor, "Latest Additions table separator")
    return text.replace(anchor, anchor + row, 1)


def insert_after_unique_line(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if marker in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {len(matches)}")
    lines.insert(matches[0] + 1, addition)
    return "".join(lines)


def insert_paper_record(text: str, title: str, record: str) -> str:
    if f'title:"{title}"' in text:
        return text
    anchor = "    const papers=[\n"
    require_once(text, anchor, "paper explorer array")
    return text.replace(anchor, anchor + record, 1)


def append_timeline_sentence(text: str, year: int, sentence: str, marker: str) -> str:
    if marker in text:
        return text
    pattern = re.compile(
        rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">'
        r'<strong>.*?</strong><p>)(.*?)(</p>)',
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f"Could not locate the {year} website timeline entry")
    return text[:match.start(2)] + match.group(2) + sentence + text[match.end(2):]


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    vehicle_row = (
        "| 2025 | [Non-Line-of-Sight Vehicle Localization Based on Sound]"
        "(https://doi.org/10.1109/TITS.2024.3510582) — Jeon et al. | "
        "IEEE Transactions on Intelligent Transportation Systems 26(2), 2321–2338 (2025) | "
        "Introduces an Acoustic-Spatial Pseudo-Likelihood particle filter for tracking "
        "vehicles approaching from fully occluded road regions. ARIL supplies BEV "
        "ground-truth positions and, together with OVAD, validates a practical passive "
        "acoustic NLOS localization branch for collision avoidance. |\n"
    )
    edge_row = (
        "| 2025 | [Localizing acoustic sources in non-line-of-sight scenarios using "
        "irregular-grid beamforming and first-order edge diffraction]"
        "(https://doi.org/10.1016/j.measurement.2025.117944) — Zhai et al. | "
        "Measurement 256, 117944 (2025) | Builds a non-free-field steering vector from "
        "the Biot–Tolstoy–Medwin first-order edge-diffraction response and combines it "
        "with irregular-grid frequency-domain beamforming. Simulations and a 32-channel "
        "array experiment localize hidden acoustic sources while limiting main-lobe "
        "deformation behind finite obstacle edges. |\n"
    )
    text = insert_latest_row(text, VEHICLE_TITLE, vehicle_row)
    text = insert_latest_row(text, EDGE_TITLE, edge_row)
    timeline_lines = (
        "   │     Jeon et al.: ASPLE particle filtering and the ARIL/OVAD datasets "
        "bring passive acoustic NLOS vehicle localization into road-safety tracking "
        "[IEEE T-ITS]\n"
        "   │     Zhai et al.: Biot–Tolstoy–Medwin edge diffraction supplies a "
        "physics-aware steering vector for irregular-grid hidden-source beamforming "
        "[Measurement]\n"
    )
    text = insert_after_unique_line(
        text,
        "Doğan: laser–acoustic early fusion and LAO-Net",
        timeline_lines,
        "Scientific Reports acoustic timeline milestone",
    )
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    vehicle_record = (
        '      {cat:"latest modality acoustic passive localization tracking vehicle '
        'autonomous-driving dataset",title:"Non-Line-of-Sight Vehicle Localization '
        'Based on Sound",authors:"Jeon et al.",year:2025,venue:"IEEE T-ITS 26(2), '
        '2321–2338",url:"https://doi.org/10.1109/TITS.2024.3510582",key:"An '
        'Acoustic-Spatial Pseudo-Likelihood particle filter tracks vehicles approaching '
        'from fully occluded road regions; ARIL provides BEV ground truth and validation '
        'is reported on ARIL and OVAD."},\n'
    )
    edge_record = (
        '      {cat:"latest modality acoustic passive localization beamforming '
        'diffraction obstacle-edge",title:"Localizing acoustic sources in '
        'non-line-of-sight scenarios using irregular-grid beamforming and first-order '
        'edge diffraction",authors:"Zhai et al.",year:2025,venue:"Measurement 256, '
        '117944",url:"https://doi.org/10.1016/j.measurement.2025.117944",key:"The '
        'Biot–Tolstoy–Medwin first-order edge-diffraction response defines a non-free-field '
        'steering vector for irregular-grid frequency-domain beamforming, validated with '
        'simulation and a 32-channel array experiment."},\n'
    )
    text = insert_paper_record(text, VEHICLE_TITLE, vehicle_record)
    text = insert_paper_record(text, EDGE_TITLE, edge_record)
    text = append_timeline_sentence(
        text,
        2025,
        " Passive acoustic NLOS also broadened from volumetric echo reconstruction to "
        "application-oriented localization: ASPLE particle filtering tracks hidden "
        "vehicles with ARIL/OVAD, while diffraction-aware irregular-grid beamforming "
        "localizes sources behind finite obstacle edges.",
        "ASPLE particle filtering tracks hidden vehicles",
    )
    actual = text.count("{cat:")
    text, count = re.subn(
        r'<b>\d+</b><span>tracked latest entries</span>',
        f'<b>{actual}</b><span>tracked latest entries</span>',
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("website tracked-entry count anchor not found")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")
    if VEHICLE_KEY not in text or EDGE_KEY not in text:
        section_start = text.find(r"\subsection{Acoustic NLOS Imaging}")
        if section_start < 0:
            raise RuntimeError("Acoustic NLOS Imaging subsection was not found")
        next_section = text.find(r"\bookmark[", section_start + 1)
        if next_section < 0:
            raise RuntimeError("Could not locate the subsection following Acoustic NLOS Imaging")
        paragraph = (
            "\n\nRecent acoustic work has also separated hidden-source localization from "
            "volumetric echo reconstruction. Jeon~\\etal~track vehicles approaching from "
            "fully occluded road regions using an Acoustic--Spatial Pseudo-Likelihood "
            "inside a particle filter~\\cite{jeonSoundVehicleNLOS2025}. Their ARIL dataset "
            "adds bird's-eye-view position ground truth and, together with OVAD, turns "
            "passive acoustic NLOS sensing into an application-oriented trajectory estimate "
            "for collision avoidance. Zhai~\\etal~instead model the finite obstacle edge "
            "itself: the Biot--Tolstoy--Medwin first-order diffraction response forms a "
            "non-free-field steering vector for irregular-grid frequency-domain "
            "beamforming~\\cite{zhaiIrregularGridAcousticNLOS2025}. The resulting method "
            "limits main-lobe deformation as the hidden source moves and is validated with "
            "both simulations and a 32-channel microphone-array experiment. Together, "
            "these systems extend the acoustic trajectory beyond relay-wall tomography "
            "toward passive tracking and diffraction-aware source localization in practical "
            "occluded environments.\n"
        )
        text = text[:next_section].rstrip() + paragraph + "\n" + text[next_section:]
        path.write_text(text, encoding="utf-8")
    main = ROOT / "bare_jrnl.tex"
    main_text = main.read_text(encoding="utf-8")
    marker = (
        "% 1 August 2026 citation trace: passive acoustic vehicle tracking and "
        "edge-diffraction localization synchronized across public artifacts.\n"
    )
    if marker not in main_text:
        anchor = "%% bare_jrnl.tex\n"
        require_once(main_text, anchor, "bare_jrnl header")
        main.write_text(main_text.replace(anchor, anchor + marker, 1), encoding="utf-8")


def update_note() -> None:
    note = ROOT / "updates/2026-08-01-acoustic-nlos-localization.md"
    note.write_text(
        """# Acoustic NLOS localization citation-trace update — 1 August 2026

A modality-focused search and citation audit of the acoustic NLOS branch identified two peer-reviewed works absent from the README, website explorer, survey prose, and merged bibliography:

- Mingu Jeon, Jae Kyung Cho, Hee Yeun Kim, Byeonggyu Park, Seung Woo Seo, and Seong Woo Kim, **Non-Line-of-Sight Vehicle Localization Based on Sound**, *IEEE Transactions on Intelligent Transportation Systems* 26(2), 2321–2338 (2025), DOI `10.1109/TITS.2024.3510582`.
- Qingbo Zhai, Libin Du, and Zhaojing Su, **Localizing acoustic sources in non-line-of-sight scenarios using irregular-grid beamforming and first-order edge diffraction**, *Measurement* 256, 117944 (2025), DOI `10.1016/j.measurement.2025.117944`.

Both are genuine NLOS sensing works rather than papers that mention NLOS propagation incidentally. Jeon et al. estimate the positions and trajectories of fully occluded vehicles from reflected/diffracted sound using an Acoustic-Spatial Pseudo-Likelihood particle filter and release the ARIL dataset with BEV ground truth. Zhai et al. explicitly model finite-edge diffraction with the Biot–Tolstoy–Medwin response and use it to construct a non-free-field steering vector for experimentally validated hidden-source beamforming.

The synchronized integration adds final-venue metadata and concise summaries to README and the interactive explorer, expands the 2025 acoustic timeline, inserts a literature-review paragraph into the Acoustic NLOS Imaging subsection, adds canonical BibTeX records, regenerates the merged bibliography and survey PDF, and verifies source/PDF consistency and first/last-page rendering.
""",
        encoding="utf-8",
    )


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    update_note()
    print("Integrated two acoustic NLOS localization papers.")


if __name__ == "__main__":
    main()
