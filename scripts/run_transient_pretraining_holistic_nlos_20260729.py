#!/usr/bin/env python3
from pathlib import Path

script = Path(__file__).with_name("integrate_transient_pretraining_holistic_nlos_20260729.py")
source = script.read_text(encoding="utf-8")

old_guard = 'require_count(readme0, M_TITLE, 0, "missing MARMOT README record")\n'
new_guard = 'require_count(readme0, M_TITLE, 1, "existing MARMOT README record")\n'
if source.count(old_guard) != 1:
    raise RuntimeError(f"Expected one obsolete MARMOT README guard; found {source.count(old_guard)}")
source = source.replace(old_guard, new_guard, 1)

old_row = '    "| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Uses a scanning-pattern mask for self-supervised pretraining on the 500,000-model TransVerse dataset, learning to complete arbitrarily sampled transients and transfer reusable features to downstream NLOS imaging tasks. |\\n"\n'
if source.count(old_row) != 1:
    raise RuntimeError(f"Expected one duplicate MARMOT insertion row; found {source.count(old_row)}")
source = source.replace(old_row, "", 1)

old_write = 'write(README, readme)\n\n# Website: retain the existing MARMOT object, add the two absent records, update dates and count dynamically.\n'
new_write = '''old_marmot_row = "| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Brings self-supervised masked pretraining to NLOS transients and introduces TransVerse-scale transient data for downstream NLOS tasks. |\\n"
new_marmot_row = "| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Uses a scanning-pattern mask for self-supervised pretraining on the 500,000-model TransVerse dataset, learning to complete arbitrarily sampled transients and transfer reusable features to downstream NLOS imaging tasks. |\\n"
require_count(readme, old_marmot_row, 1, "existing MARMOT README row")
readme = readme.replace(old_marmot_row, new_marmot_row, 1)
write(README, readme)

# Website: retain the existing MARMOT object, add the two absent records, update dates and count dynamically.
'''
if source.count(old_write) != 1:
    raise RuntimeError(f"Expected one README write anchor; found {source.count(old_write)}")
source = source.replace(old_write, new_write, 1)

namespace = {"__file__": str(script), "__name__": "__main__"}
exec(compile(source, str(script), "exec"), namespace)
