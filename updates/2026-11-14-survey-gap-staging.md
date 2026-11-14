# 2026-11-14 survey gap audit — staged integration (no PDF rebuild)

## Verified catalogued works missing from survey prose

1. **Zhou et al., Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation**, *Physical Review Letters* **136**, 083801 (2026), DOI: https://doi.org/10.1103/kd8v-fykm. Already present in README and consolidated bibliography as `zhouPolarizationSinglePixel2026`; no occurrence of this citation key in `article/2active.tex`, `article/3passive.tex`, or `article/5newscenes.tex` at audit time. Insert into `article/2active.tex` near optical active acquisition / single-pixel or structured illumination discussion, with a short paragraph on polarization-speckle modulation for indirect-light imaging. Confirm exact author list from publisher before correcting the existing malformed author field.
2. **Zeng et al., Compact non-line-of-sight imager at long range**, *Optics Express* **34**(9), 16911–16921 (2026), DOI: https://doi.org/10.1364/OE.597084. Already in README and consolidated bibliography as `zengCompactLongRangeNLOS2026`; no occurrence of this key in the three surveyed chapter files. Insert into `article/2active.tex` beside outdoor/long-range SPAD systems. The paper reports a compact daylight kilometer-range system at 2 fps.

## Checked and not duplicated

- Laser reflective tomography at 3.3 km (DOI 10.29026/oes.2026.260007) is already represented in README, active survey, and bibliography.
- GeRaF 2.0 (arXiv:2605.29098) is already represented in README, new-scenes chapter, and bibliography.
- The PRL polarization paper and Optics Express compact imager are already in README and bibliography, so do not add duplicate catalog entries.

## Safe follow-up

Read full current `article/2active.tex` and its blob SHA, insert the two citations in semantically appropriate paragraphs, verify both keys in the consolidated bibliography, then build `bare_jrnl.tex` and update `bare_jrnl.pdf` only after a successful compilation. This run deliberately did not replace the ~150 KB chapter without full structural editing/build verification. The existing PDF is **not** updated by this note.

This is a targeted search and cross-artifact check, not an exhaustive scholarly forward-citation export.
