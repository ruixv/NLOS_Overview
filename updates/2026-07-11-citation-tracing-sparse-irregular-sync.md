# 11 July 2026 citation-tracing and sparse/irregular NLOS sync

This update was driven by forward-citation tracing from the field-defining LCT, f-k migration, phasor-field, neural-transient-field, transformer, and 3D Gaussian transient-rendering lineages. Each added item is directly about NLOS imaging/reconstruction rather than a paper that merely cites NLOS work in passing.

## Public artifacts

- `README.md`: nine missing published papers added; final venue corrections applied where independently verifiable.
- `index.html`: the same papers plus the previously README-only NIR raster-scanning paper added; latest count changed from 71 to 81 and timeline summaries updated.
- `article/4datadriven.tex`: added TransDiff and physics-guided high-speed reconstruction in the physics/learning section.
- `article/2active.tex`: added a sparse/irregular-relay paragraph covering DO-NLOS, sub-pixel modulation, and CUDA acceleration.
- `egbib_20260711_updates.bib`: five new final-venue BibTeX records with DOI metadata.
- `bare_jrnl.tex`: bibliography command expanded to all `egbib*.bib` sources.

## Venue corrections

The public surfaces were corrected from arXiv-only labels to verified final venues for 3D Gaussian Transient Rendering (SIGGRAPH 2026), TransiT (ICCV 2025), NLOS-NeuS (ICCV 2023), Self-Calibrating Fully Differentiable NLOS Inverse Rendering (SIGGRAPH Asia 2023), Differentiable Transient Rendering (ACM TOG 2021), Keyhole Imaging (IEEE TCI 2021), and Partial Occluders and Surface Normals (ACM TOG 2019).

## PDF status

The accompanying GitHub Actions run attempts a clean LaTeX/BibTeX rebuild. The workflow appends the final success/failure status below before committing. If compilation fails, source changes are still committed and the old PDF is deliberately left untouched.

**Build result:** successful clean LaTeX/BibTeX rebuild; `bare_jrnl.pdf` was regenerated and validated with `pdfinfo` and `pdftotext` in CI (latexmk exit code 0).
