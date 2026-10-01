# NLOS literature gap — NIR raster scanning

## Verified missing paper

Mohammad Roueinfar and Mahdi Salmanian, **“Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength,”** *2025 33rd International Conference on Electrical Engineering (ICEE)*, pp. 1175–1179, 2025. DOI: 10.1109/ICEE67339.2025.11213924. A later author manuscript is available as arXiv:2607.04183 (posted July 2026), but the final venue is ICEE 2025 and should be used in the survey.

### Why it belongs

This is a genuine active optical NLOS imaging experiment rather than an incidental NLOS citation. It uses an 808-nm, 500-mW NIR laser, a pan–tilt mechanism for relay-wall raster scanning, and an NIR camera to recover hidden targets through a three-bounce path. Experiments on several target shapes study the scan-density/image-quality trade-off using MSE/RMSE. The contribution is modest relative to transient/SPAD milestones, but it is useful as a practical low-cost NIR raster-scanning branch of active NLOS hardware.

## Integration plan

- **README.md:** add under active optical / practical systems, chronologically at 2025. Use the final ICEE 2025 venue, with arXiv:2607.04183 only as an optional accessible manuscript link.
- **index.html / Paper Explorer:** classify as `Active`, `Optical/NIR`, `Raster scanning`, `Practical system`; add to the 2025 timeline rather than 2026 despite the 2026 arXiv upload.
- **bare_jrnl.tex:** integrate in the active-NLOS acquisition/system discussion near raster-scanning and practical hardware variants. Suggested concise literature sentence: “Beyond ultrafast transient systems, Roueinfar and Salmanian demonstrated a lower-cost NIR implementation based on relay-wall raster scanning with a pan–tilt illuminator and an NIR camera, highlighting the acquisition-density versus reconstruction-quality trade-off.”
- **Bibliography:** merge `egbib_20261002_nir_raster_scanning_gap.bib` into the canonical bibliography and cite it from `bare_jrnl.tex`.
- **bare_jrnl.pdf:** rebuild only after the canonical source/bibliography integration is complete; verify README, website, LaTeX, bibliography, and PDF consistency afterward.

## Verification / deduplication

Repository-wide GitHub code search for the full title returned no result before staging. Web metadata verifies DOI `10.1109/ICEE67339.2025.11213924`, ICEE 2025, pages 1175–1179. The July 2026 arXiv upload carries the same DOI, so it must not be mislabeled as a 2026 arXiv-only work.

## Safety note

The canonical large public-facing files were not overwritten in this run because a complete safe read/edit/build cycle was not available. This staging note records exact semantic insertion points rather than risking truncation or inconsistent partial updates.
