# 27 August 2026 — NIR raster-scan NLOS final-venue gap

## Verified missing paper

Mohammad Roueinfar and Mahdi Salmanian, “Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength,” *2025 33rd International Conference on Electrical Engineering (ICEE)*, pp. 1175–1179, 2025. DOI: `10.1109/ICEE67339.2025.11213924`.

The paper reappeared on arXiv in July 2026 as `arXiv:2607.04183`, but bibliographic indexes resolve the same work to the earlier final IEEE conference publication. The repository should therefore label it by the final venue **IEEE ICEE 2025**, not arXiv 2026. A canonical staging BibTeX entry is provided in `egbib_20260827_nir_raster_scan_gap.bib` with key `roueinfarNIRRasterNLOS2025`.

## Why it belongs

This is a genuine active optical NLOS imaging experiment rather than a generic NLOS-propagation paper. An 808-nm, 500-mW NIR laser is raster-scanned over a visible relay wall using a pan-tilt mechanism; light follows the standard three-bounce wall → hidden target → wall path and is recorded by an NIR camera. The paper reports reconstructions for three hidden targets and compares them with ground truth using MSE/RMSE. Its contribution is modest relative to ultrafast transient methods, but it documents a low-complexity steady-state NIR raster-scanning branch that is currently absent from the overview.

## Repository audit

Searches for the exact title, DOI `10.1109/ICEE67339.2025.11213924`, and canonical key found no current repository entry. This should therefore be treated as a new paper record rather than a venue correction of an existing entry.

## Safe integration plan

1. **README.md / Latest Additions** — add the IEEE ICEE 2025 record, preferably with a concise summary: `Demonstrates a low-complexity active NIR NLOS system using an 808-nm laser raster-scanned across a relay wall by a pan-tilt unit; an NIR camera records three-bounce returns and reconstructs simple hidden targets, with MSE/RMSE evaluation against ground truth.`
2. **Development timeline** — place under 2025 active/hardware directions as a practical steady-state/raster-scanning NIR branch, not as a replacement for transient ToF reconstruction.
3. **data/papers-source.html** — add exactly one canonical paper object, family `active`, year `2025`, venue `IEEE ICEE 2025`, DOI URL above, key `roueinfarNIRRasterNLOS2025`; recompute any tracked-entry count.
4. **article/2active.tex** — integrate one short sentence in the acquisition/hardware or alternative active-imaging discussion, distinguishing steady-state NIR raster scanning from ultrafast ToF/SPAD pipelines. Do not overstate methodological novelty.
5. **egbib_merged_20260711.bib** — merge `roueinfarNIRRasterNLOS2025` exactly once and verify DOI/key uniqueness; remove the staging BibTeX only after successful public integration.
6. **bare_jrnl.tex / bare_jrnl.pdf** — after the source edits, clean-build with the repository’s normal `pdflatex → bibtex → pdflatex → pdflatex` sequence. Verify the citation in `.aux/.bbl`, PDF text extraction, and representative page rendering before committing the rebuilt binary.

## Fresh-search context

The same run rechecked recent 2026 optical/transient/passive/RF results and forward citations of the LCT, f-k migration, phasor-field, and computational-periscopy milestones. High-confidence recent papers such as PICL, all-day Si-SPAD, Stereo NLOS, DCEEM, arbitrary-relay 3D Gaussian Transient Rendering, and the open-pit mmWave–LiDAR NLOS work are already present in the repository or already have explicit pending integration notes; they should not be duplicated.

Because several previously verified consistency gaps are still staged against the same large public files, this run uses the patch-style fallback rather than whole-file replacement. No claim is made that README, V2, the survey body, or `bare_jrnl.pdf` already contains this ICEE paper.
