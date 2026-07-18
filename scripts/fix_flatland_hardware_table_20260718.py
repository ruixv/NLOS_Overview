#!/usr/bin/env python3
"""Keep the Flatland simulation framework out of the hardware-specific SPAD table."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

active_path = ROOT / "article/2active.tex"
text = active_path.read_text(encoding="utf-8")
wrong = ",shiSpecularFlightPathNLOS2026,sunCUDAIrregularRelayNLOS2026,penaFlatlandNLOS2025}"
right = ",shiSpecularFlightPathNLOS2026,sunCUDAIrregularRelayNLOS2026}"

if wrong in text:
    if text.count(wrong) != 1:
        raise RuntimeError(f"Expected one inaccurate hardware-table citation sequence, found {text.count(wrong)}")
    text = text.replace(wrong, right, 1)
elif right not in text:
    raise RuntimeError("Expected corrected active-SPAD citation tail was not found")

if text.count("penaFlatlandNLOS2025") != 1:
    raise RuntimeError("Flatland should remain cited exactly once in its simulation-framework review paragraph")

active_path.write_text(text, encoding="utf-8")

note_path = ROOT / "updates/2026-07-18-irregular-relay-flatland-citation-trace.md"
if note_path.exists():
    note = note_path.read_text(encoding="utf-8")
    clarification = (
        "\n## Hardware-table clarification\n\n"
        "Flatland is an enabling 2D transient simulation and analysis framework, not a pulsed-laser/SPAD hardware experiment. "
        "It is integrated in the active-method literature review and bibliography, but intentionally excluded from the hardware-specific active-SPAD summary row.\n"
    )
    if "## Hardware-table clarification" not in note:
        note = note.rstrip() + "\n" + clarification
    note_path.write_text(note, encoding="utf-8")

print("Corrected Flatland hardware-table categorization.")
