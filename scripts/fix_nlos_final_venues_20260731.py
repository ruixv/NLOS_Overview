#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

readme_path = root / "README.md"
readme = readme_path.read_text(encoding="utf-8")

leap_pattern = re.compile(r'^\| 2024 \| \[Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging\]\([^\n]+$', re.M)
leap_row = "| 2024 | [Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging](https://doi.org/10.1007/978-3-031-72775-7_5) — Cho et al. | ECCV 2024, LNCS 15101, 72–89 | LEAP predicts clean full-aperture phasor fields from noisy partial measurements, enabling high-quality NLOS reconstruction with 16×–64× fewer samples and scan areas up to 4× smaller. |"
readme, n = leap_pattern.subn(leap_row, readme, count=1)
if n != 1:
    raise RuntimeError(f"Expected one README LEAP row, replaced {n}")

tltm_pattern = re.compile(r'^\| 2024 \| \[Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging\]\([^\n]+$', re.M)
tltm_row = "| 2026 | [Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging](https://doi.org/10.1038/s41467-026-75177-4) — Sultan et al. | Nature Communications 2026 | Measures the full relay-wall TLTM-1 with dense illumination and a gated 16×16 SPAD array, then computationally focuses virtual illumination and detection in the hidden scene to recover TLTM-2 for indirect shadows, interreflection analysis, relighting, transport separation, and dual photography. |"
readme, n = tltm_pattern.subn(tltm_row, readme, count=1)
if n != 1:
    raise RuntimeError(f"Expected one README TLTM row, replaced {n}")
readme_path.write_text(readme, encoding="utf-8")

index_path = root / "index.html"
index = index_path.read_text(encoding="utf-8")
old_leap = '{cat:"latest active learning",title:"Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging",authors:"Cho et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2407.18574",key:"LEAP predicts clean full-aperture phasor fields from noisy partial measurements."}'
new_leap = '{cat:"latest active learning",title:"Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging",authors:"Cho et al.",year:2024,venue:"ECCV 2024",url:"https://doi.org/10.1007/978-3-031-72775-7_5",key:"LEAP predicts clean full-aperture phasor fields from noisy partial measurements, supporting 16×–64× fewer samples and up to 4× smaller apertures."}'
if index.count(old_leap) != 1:
    raise RuntimeError(f"Expected one stale LEAP website object, found {index.count(old_leap)}")
index = index.replace(old_leap, new_leap, 1)

expected_tltm = '{cat:"latest active transient spad array light transport matrix phasor relighting",title:"Iterating the transient light transport matrix for non-line-of-sight imaging",authors:"Sultan et al.",year:2026,venue:"Nature Communications 2026",url:"https://doi.org/10.1038/s41467-026-75177-4"'
if expected_tltm not in index:
    raise RuntimeError("Final Nature Communications TLTM website record is missing")
index_path.write_text(index, encoding="utf-8")

note = root / "updates/20260731_public_final_venue_consistency.md"
note.write_text("""# 31 July 2026 public final-venue consistency pass

Two public-facing records still retained their original arXiv labels even though final venues were already verified in the bibliography and survey build.

- **Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging (LEAP)** is now labeled **ECCV 2024**, LNCS 15101, pages 72–89, DOI `10.1007/978-3-031-72775-7_5` in README and the website explorer.
- **Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging** is now labeled **Nature Communications 2026**, DOI `10.1038/s41467-026-75177-4` in README; the website record was already correct and was checked rather than duplicated.

The LaTeX survey and consolidated bibliography already carried the final venue metadata, so no survey-prose or PDF rebuild was required for this public-label correction. The existing PDF was validated to contain both titles.
""", encoding="utf-8")

print("Corrected LEAP and TLTM final venues in public-facing records.")
