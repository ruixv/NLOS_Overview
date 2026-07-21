#!/usr/bin/env python3
"""Robust README-only synchronization for the coherent FMCW citation trace."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "README.md"

ROWS = (
    "| 2024 | [Non-Line-of-Sight Imaging and Vibrometry Using a Comb-Calibrated Coherent Sensor](https://doi.org/10.1103/PhysRevLett.132.233802) — Huang et al. | Physical Review Letters 2024 | Establishes coherent optical NLOS sensing with an optical-frequency-comb-calibrated FMCW LiDAR, providing sub-picosecond effective temporal resolution, submillimeter hidden-scene localization and 3D imaging, and frequency-resolved NLOS vibrometry under strong ambient light. |\n"
    "| 2025 | [High-Resolution Non-Line-of-Sight Tracking by Comb-Calibrated FMCW LiDAR](https://doi.org/10.1002/lpor.202401250) — Ye et al. | Laser & Photonics Reviews 2025 | Extends comb-calibrated coherent NLOS from static imaging to snapshot multi-object tracking, reporting 2 mm 3D position accuracy and 2 mm/s velocity accuracy without temporal accumulation. |\n"
    "| 2025 | [Non-Line-of-Sight Ranging and 3D Imaging Using Vector Enhanced Sensitive FMCW LiDAR](https://doi.org/10.1109/JLT.2024.3523206) — Chen et al. | Journal of Lightwave Technology 2025 | Uses laser-feedback interferometry, polarization-vector enhancement, and K-domain resampling for a simpler sensitive FMCW architecture, demonstrating better-than-32-µm NLOS absolute ranging and millimeter-level hidden 3D imaging at about 2.8 m. |\n"
)


def insert_after_unique_line(text: str, needle: str, addition: str, label: str) -> str:
    matches = list(re.finditer(rf"(?m)^.*{re.escape(needle)}.*(?:\n|$)", text))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one matching line, found {len(matches)}")
    match = matches[0]
    return text[: match.end()] + addition + text[match.end() :]


def update_readme() -> None:
    text = PATH.read_text(encoding="utf-8")
    if "10.1103/PhysRevLett.132.233802" not in text:
        anchor = "|------|-------|----------------|----------------|\n"
        if text.count(anchor) != 1:
            raise RuntimeError(f"latest-additions table: expected one header, found {text.count(anchor)}")
        text = text.replace(anchor, anchor + ROWS, 1)

    if "comb-calibrated coherent FMCW NLOS" not in text:
        text = insert_after_unique_line(
            text,
            "event-enhanced passive NLOS",
            "    │     Huang et al.: comb-calibrated coherent FMCW NLOS — sub-picosecond equivalent timing enables submillimeter 3D imaging and hidden-object vibrometry [Physical Review Letters]\n",
            "2024 milestone",
        )

    if "comb-calibrated FMCW tracking" not in text:
        text = insert_after_unique_line(
            text,
            "spatial-correlation scan-free NLOS",
            "    │     Ye et al.: comb-calibrated FMCW tracking — snapshot multi-object position and velocity recovery at 2-mm and 2-mm/s accuracy [Laser & Photonics Reviews]\n"
            "    │     Chen et al.: vector-enhanced sensitive FMCW LiDAR — laser-feedback interferometry and K-domain resampling provide micrometer ranging and millimeter hidden 3D imaging [Journal of Lightwave Technology]\n",
            "2025 milestone",
        )
    PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
