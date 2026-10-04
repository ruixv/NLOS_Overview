# Integration note — NIR raster-scanning NLOS gap (2026-10-04)

## Verified missing paper

Mohammad Roueinfar and Mahdi Salmanian, **“Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength,”** *2025 33rd International Conference on Electrical Engineering (ICEE)*, pp. 1175–1179, 2025. DOI: `10.1109/ICEE67339.2025.11213924`. A later arXiv posting is `arXiv:2607.04183` (5 July 2026), but the final venue is ICEE 2025 and should be used in public-facing metadata.

## Scope / contribution

This is a direct optical NLOS-imaging paper rather than generic NLOS detection. It uses an 808-nm, 500-mW NIR laser, a pan–tilt raster scan of the relay wall, and an NIR camera to recover hidden 2D targets through three-bounce indirect transport. Experiments on three target shapes compare 4×4, 8×8, and 16×16 scan grids and quantify reconstruction error with MSE/RMSE. Its main survey value is as a compact, comparatively low-cost NIR implementation and as an explicit illustration of the acquisition-quality trade-off of relay-wall raster scanning; it is not a replacement for time-resolved 3D NLOS methods.

## Repository check

Repository-wide default-branch searches for the exact title and for `Roueinfar` returned no matches before staging, so this is a genuine coverage gap at this run.

## Recommended integration

- **README / Paper Explorer:** add under active optical / practical NLOS systems, year 2025. Suggested one-line summary: “Demonstrates a compact 808-nm NIR three-bounce NLOS system using pan–tilt relay-wall raster scanning and an NIR camera; increasing the scan grid from 4×4 to 16×16 improves hidden-target fidelity at the cost of acquisition time.”
- **Development timeline:** place with practical/low-cost active optical implementations rather than SPAD/transient reconstruction milestones.
- **Survey source:** in the active-NLOS hardware/acquisition discussion, use it as a recent example of intensity-based NIR raster scanning, contrasting its simple hardware with time-resolved SPAD/ToF systems and with newer scan-free approaches.
- **Bibliography:** merge the verified entry from `egbib_20261004_nir_raster_gap.bib` into the canonical bibliography, avoiding duplicate arXiv-only metadata.
- **Website:** mirror the README metadata and category; link DOI and optionally arXiv as an accessible preprint.

## Verification / remaining work

Metadata cross-checked against the DOI-bearing conference record and the later arXiv record. The arXiv posting itself exposes DOI `10.1109/ICEE67339.2025.11213924`, so venue should be **ICEE 2025**, not arXiv 2026.

Large canonical README/index/survey files were not overwritten from partial connector buffers in this run. They still require a complete safe read-edit-validation cycle, followed by LaTeX compilation and consistency checking of README, website, survey source, canonical bibliography, and `bare_jrnl.pdf`.
