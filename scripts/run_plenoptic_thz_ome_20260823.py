from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_KEY = "weiPolarizationEncodedOMEMultiplexing2026"
CANONICAL_KEY = "weiPolarizationSpatialMultiplexing2026"

# The 2026 polarization-multiplexing paper was already present in the merged
# bibliography under CANONICAL_KEY.  Keep that established key rather than
# creating a duplicate entry, while letting the guarded integration add any
# missing README/V2/survey context and merge the genuinely missing records.
staging = ROOT / "egbib_20260823_plenoptic_thz_ome_gap.bib"
if staging.exists():
    text = staging.read_text(encoding="utf-8")
    if OLD_KEY in text and CANONICAL_KEY not in text:
        staging.write_text(text.replace(OLD_KEY, CANONICAL_KEY), encoding="utf-8")

impl = ROOT / "scripts" / "integrate_plenoptic_thz_ome_20260823.py"
source = impl.read_text(encoding="utf-8").replace(OLD_KEY, CANONICAL_KEY)
namespace = {"__name__": "__main__", "__file__": str(impl)}
exec(compile(source, str(impl), "exec"), namespace)
