#!/usr/bin/env bash
set -euo pipefail

BRANCH=automation/picl-public-sync-20260806
OUTPUT_BRANCH="automation/generated-picl-public-sync-${GITHUB_RUN_ID:-manual}"

git show "origin/${BRANCH}:scripts/sync_picl_public_artifacts_20260806.py" > /tmp/sync_picl.py
git show "origin/${BRANCH}:scripts/run_picl_public_integration_20260806.sh" > /tmp/original_runner.sh
python3 -m py_compile /tmp/sync_picl.py

# The master README already contains PICL in its main catalog and timeline.
# Let the bounded updater apply all other edits, then remove only the duplicate
# Latest Additions row that causes its legacy one-occurrence assertion to fail.
set +e
python3 /tmp/sync_picl.py
sync_status=$?
set -e
if [[ $sync_status -ne 0 && $sync_status -ne 1 ]]; then
  exit "$sync_status"
fi

python3 - <<'PY'
from pathlib import Path

title = "Non-line-of-sight imaging via physics-informed cascade learning"
latest_row = (
    "| 2026 | [Non-line-of-sight imaging via physics-informed cascade learning]"
    "(https://doi.org/10.1364/JOSAA.593401) — Zhao et al. | "
    "Journal of the Optical Society of America A 43(9), E9–E18 (2026) | "
    "PICL cascades a lightweight SPAD-specific noise-separation network with a reconstruction network that embeds a differentiable NLOS forward model. The self-supervised physical-consistency objective avoids dependence on large paired datasets and improves robustness under mixed dark-count, timing-jitter, and low-SNR interference. |\n"
)
readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")
if readme.count(title) == 2 and latest_row in readme:
    readme = readme.replace(latest_row, "", 1)
old_main = (
    "| 2026 | [Non-line-of-sight imaging via physics-informed cascade learning]"
    "(https://doi.org/10.1364/JOSAA.593401) — Zhao et al. | JOSA A 2026 |"
)
new_main = (
    "| 2026 | [Non-line-of-sight imaging via physics-informed cascade learning]"
    "(https://doi.org/10.1364/JOSAA.593401) — Zhao et al. | "
    "Journal of the Optical Society of America A 43(9), E9–E18 (2026) |"
)
if old_main in readme:
    readme = readme.replace(old_main, new_main, 1)
if readme.count(title) != 1:
    raise SystemExit(f"README PICL title count is {readme.count(title)}, expected 1")
readme_path.write_text(readme, encoding="utf-8")

note_path = Path("updates/2026-08-06-picl-public-artifact-sync.md")
note = note_path.read_text(encoding="utf-8")
note = note.replace(
    "Added **Non-line-of-sight imaging via physics-informed cascade learning** (Zhao et al., *Journal of the Optical Society of America A* 43(9), E9–E18, 2026; DOI `10.1364/JOSAA.593401`) to the README Latest Additions table and website paper explorer.",
    "Verified the existing README catalog/timeline coverage of **Non-line-of-sight imaging via physics-informed cascade learning** (Zhao et al., *Journal of the Optical Society of America A* 43(9), E9–E18, 2026; DOI `10.1364/JOSAA.593401`), expanded its README venue metadata, and added the missing website paper-explorer record.",
)
note_path.write_text(note, encoding="utf-8")

html = Path("index.html").read_text(encoding="utf-8")
assert html.count(title) == 1
assert readme.count("Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors") == 1
assert "ICCV 2025, 25040–25049" in readme
print("Existing README PICL record reconciled with website and survey")
PY

# Execute the reviewed build, validation, rendering, and generated-branch
# persistence stages from the original runner, skipping its updater invocation.
awk '/^sudo sed -i/{emit=1} emit' /tmp/original_runner.sh > /tmp/build_validate_persist.sh
# PDF text extraction may insert a line-break hyphen inside the title; the DOI,
# journal, and a distinctive title fragment together remain a strict check.
sed -i 's/nonlineofsightimagingviaphysicsinformedcascadelearning/physicsinformedcascadelearning/' /tmp/build_validate_persist.sh
source /tmp/build_validate_persist.sh
