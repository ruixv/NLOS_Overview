# 22 July 2026 NIR raster-scanning final-venue correction

## Verified correction

`Non-Line-of-Sight imaging using raster scanning at NIR wavelength` was uploaded to arXiv as `2607.04183` in July 2026, but it had already been formally published in the **2025 33rd International Conference on Electrical Engineering (ICEE)**.

- Authors: Mohammad Roueinfar and Mahdi Salmanian
- Final venue: 2025 33rd International Conference on Electrical Engineering (ICEE)
- Pages: 1–5
- DOI: `10.1109/ICEE67339.2025.11213924`
- IEEE publication date indexed by scholarly services: 13 May 2025

The repository must therefore use the final IEEE conference venue and DOI rather than treating the later arXiv upload as a 2026 publication.

## Cross-artifact changes

The guarded synchronizer `scripts/sync_nlos_20260722_nir_final_venue.py` performs the following updates:

1. Replaces the arXiv 2026 README row with an IEEE ICEE 2025 row and DOI link.
2. Corrects the website paper-explorer record without changing the tracked-paper count.
3. Adds the work to the 2025 development timeline as a low-cost 808 nm steady-state raster-scanning baseline.
4. Integrates a short literature-review paragraph into the conventional-camera portion of `article/2active.tex` and cites it in the active-method table.
5. Adds a DOI-verified canonical BibTeX record with key `roueinfarNIRRaster2025`.
6. Adds a dated integration marker to `bare_jrnl.tex`.
7. Updates the README and website dates to 22 July 2026.

## Build and validation requirements

The associated workflow must:

- run the guarded synchronizer;
- regenerate the consolidated bibliography with `scripts/merge_nlos_bibliography.py`;
- perform a clean `pdflatex → bibtex → pdflatex ×2` build;
- reject undefined citations or multiply defined bibliography entries;
- verify the DOI and final venue in README, website, survey source, merged bibliography, and extracted PDF text;
- confirm that the old arXiv URL is no longer used for this public entry;
- commit `README.md`, `index.html`, `article/2active.tex`, `bare_jrnl.tex`, the new bibliography supplement, the merged bibliography, and `bare_jrnl.pdf` only after all checks pass.

No paper-count increment is required because the work was already represented in README and the website; this run corrects venue metadata and fills the survey/BibTeX consistency gap.
