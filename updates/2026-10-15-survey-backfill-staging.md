> **Resolved on 2026-10-16.** This is a historical staging audit. The final reconciliation found **seven distinct missing works**, not nine: the SSD and diffuse-aware attention entries were already cited under their verified canonical keys. See [2026-10-16 reconciliation](2026-10-16-survey-backfill-reconciliation.md). The PDF remains pending rebuild.

# 2026-10-15 NLOS survey backfill audit

## Verified gap
The README and paper explorer already include these 2026 works, and the merged BibTeX contains their keys, but none is cited in the included survey chapters. Add the following literature discussion in context rather than appending a detached list:

- `article/3passive.tex`, just before "Challenges and prospects": `rajiSoftShadowDiffusion2026` (3D computational periscopy, arXiv:2601.12257), `zhangSGATVPassiveNLOS2026` (structure-guided adaptive TV, Optics Express 34:5210-5224), and `wangDAAMPassiveNLOS2026` (diffuse-aware attention, Optics Express 34:26271-26289).
- `article/4datadriven.tex`, between "Learning the light-cone inverse" and "Physics-initialized triplane reconstruction": `zhangFMoENLOS2026` (frequency-domain regularization experts, Pattern Recognition 173:112914).
- `article/2active.tex`, in the wave-based methodology discussion before "It should be noted that not all...": `yuFrequencyDomainPhaseNLOS2026` (reference-function phase compensation for non-confocal reconstruction, Optics Express 34:3232-3243).
- `article/2active.tex`, immediately before "Neural implicit surface reconstruction": `liuGeometryConstrainedNLOS2026` (shape-operator normal regularization, IEEE TVCG 32:6524-6536).
- `article/2active.tex`, before "Limited resolution": `wangLRTNLOS2026` (scanning-free laser reflective tomography, Opto-Electronic Science 5:260007) and `qianHighSpeedNLOSFMCW2026` (predistorted FMCW LiDAR, SPIE Photonics Europe 14083:1408311).
- `article/2active.tex`, in "Limited resolution" following the existing feature-visibility discussion: `romanelliFiniteApertureNLOS2026` (yaw observability, finite relay aperture, Journal of Imaging 12:248).

## Bibliography repair
ACM's article page confirms DOI 10.1145/3811030, "Thermal Non-Line-of-Sight Imaging through Rough Surfaces", *ACM TOG* 45(5), **Article 173** (2026). Both existing keys `yeThermalRoughNLOS2026` and `yeThermalNLOSFormer2026` currently say `articleno = {41}`; change both to 173 without breaking existing citations.

## Recovery and PDF
The attempt to write full replacement text for large LaTeX chapters was blocked by connector safety checks. No chapter has been overwritten. README and website already list these works; do not duplicate entries. `bare_jrnl.pdf` is still stale. After obtaining a complete repository checkout including figure assets, run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`, inspect missing/duplicate citation diagnostics, and commit the rebuilt PDF.