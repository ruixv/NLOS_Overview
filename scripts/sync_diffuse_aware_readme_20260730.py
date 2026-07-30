from pathlib import Path

TITLE = "Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding"
ROW = (
    "| 2026 | [Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding]"
    "(https://doi.org/10.1364/OE.601398) — Wang et al. | Optics Express 34(14), "
    "26271–26289 (2026) | Introduces a diffuse-aware attention module that encodes two "
    "passive-NLOS priors: anisotropic angular structure in relay-wall diffusion and unequal "
    "signal-to-noise ratios across feature channels. Deformable spatial attention, mean–standard-"
    "deviation channel pooling, and gated fusion preserve weak hidden-scene evidence in an "
    "ordinary-camera reconstruction network. |\n"
)

readme_path = Path("README.md")
text = readme_path.read_text(encoding="utf-8")
count = text.count(TITLE)
if count > 1:
    raise SystemExit(f"Refusing to edit README.md: {TITLE!r} already appears {count} times")
if count == 0:
    anchor = "|------|-------|----------------|----------------|\n"
    if text.count(anchor) != 1:
        raise SystemExit("Latest-additions table anchor is missing or ambiguous")
    text = text.replace(anchor, anchor + ROW, 1)
    readme_path.write_text(text, encoding="utf-8")

if readme_path.read_text(encoding="utf-8").count(TITLE) != 1:
    raise SystemExit("README synchronization failed")
