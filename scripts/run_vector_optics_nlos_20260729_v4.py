#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
script = Path(__file__).with_name("integrate_vector_optics_nlos_20260729.py")
source = script.read_text(encoding="utf-8")

# The README currently contains several 2025 timeline lines. Replace the broad
# regex in the original guarded script with the unique first 2025 milestone.
old = '    r"^2025 ──[^\\n]*\\n",\n'
new = '    r"^2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning \\[IEEE ICEE\\]\\n",\n'
if source.count(old) != 1:
    raise RuntimeError(f"Expected one broad 2025 timeline anchor, found {source.count(old)}")
source = source.replace(old, new, 1)
namespace = {"__file__": str(script), "__name__": "__main__"}
exec(compile(source, str(script), "exec"), namespace)

# Keep the public counter derived from the actual explorer objects rather than
# depending on a stale manually recorded count.
index = ROOT / "index.html"
html = index.read_text(encoding="utf-8")
actual = html.count("{cat:")
pattern = r"<b>\d+</b><span>tracked latest entries</span>"
if len(re.findall(pattern, html)) != 1:
    raise RuntimeError("Could not uniquely identify website tracked-entry counter")
html = re.sub(pattern, f"<b>{actual}</b><span>tracked latest entries</span>", html, count=1)
index.write_text(html, encoding="utf-8")
print(f"Website explorer synchronized at {actual} entries")

# Repair a pre-existing survey/public-artifact inconsistency exposed by the
# clean BibTeX build: the neuromorphic tracking paper was cited in the survey
# but absent from the consolidated bibliography.
bib_path = ROOT / "egbib_merged_20260711.bib"
bib = bib_path.read_text(encoding="utf-8")
neuromorphic_key = "zhuEfficientNeuromorphicNLOSTracking2024"
neuromorphic_doi = "10.1364/OL.530066"
if neuromorphic_key not in bib:
    if neuromorphic_doi in bib:
        raise RuntimeError(
            f"DOI {neuromorphic_doi} exists under another key; refusing to create a duplicate entry"
        )
    bib = bib.rstrip() + r'''

@article{zhuEfficientNeuromorphicNLOSTracking2024,
  author    = {Zhu, Shuo and Ge, Zhou and Wang, Chutian and Han, Jing and Lam, Edmund Y.},
  title     = {Efficient Non-Line-of-Sight Tracking with Computational Neuromorphic Imaging},
  journal   = {Optics Letters},
  year      = {2024},
  volume    = {49},
  number    = {13},
  pages     = {3584--3587},
  publisher = {Optica Publishing Group},
  doi       = {10.1364/OL.530066},
  url       = {https://doi.org/10.1364/OL.530066},
  note      = {Published online 18 June 2024}
}
'''
    bib_path.write_text(bib, encoding="utf-8")
    print("Repaired missing neuromorphic-tracking bibliography entry")
else:
    print("Neuromorphic-tracking bibliography entry already present")

note = ROOT / "updates/2026-07-29-vector-optics-nlos-integration.md"
with note.open("a", encoding="utf-8") as f:
    f.write(
        "\nThe clean build also repaired the previously unresolved citation "
        "`zhuEfficientNeuromorphicNLOSTracking2024` by adding the verified "
        "Optics Letters 2024 record (DOI `10.1364/OL.530066`) to the consolidated bibliography.\n"
    )
