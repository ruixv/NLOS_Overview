# 2026-09-24 update: directional confocal NLOS range characterization

## Verified missing paper

Lingyun Qiu, Zuoqiang Shi, Jianyu Wang, and Shiwei Wu, **“Reconstruction and Range Characterization for a Directional Confocal Non-Line-of-Sight Imaging Model,”** arXiv:2609.26846 (2026). Submitted 22 September 2026; updated 24 September 2026. No final conference/journal venue was verified in this run, so the venue should remain arXiv.

## Why it belongs

This is a theoretical active/confocal NLOS paper rather than a generic inverse-problems citation. It studies recovery of a directional albedo vector field from confocal NLOS measurements. Radial preprocessing maps the measurements to spherical means of the divergence; the work characterizes the divergence-free ambiguity, gives an explicit Fourier--sine reconstruction of the irrotational Helmholtz component, and derives an exact weighted Hilbert-space range characterization. It also treats partial relay-wall measurements and therefore complements the repository's LCT/f-k/phasor-field line with a mathematical identifiability/range-analysis direction.

## Safe integration plan

- **README.md:** add under 2026 active/transient NLOS, preferably a theory / inverse-problem / observability subcategory. Suggested one-line summary: “Directional confocal NLOS: characterizes recoverable directional-albedo components, the divergence-free ambiguity, and the exact data range via spherical-mean/Fourier--sine analysis.”
- **index.html / Paper Explorer:** add tags `Active`, `Transient`, `Confocal`, `Theory`, `Inverse Problems`, `Directional Albedo`; add to the 2026 timeline near other visibility/aperture/forward-model analyses.
- **bare_jrnl.tex:** integrate semantically in the active ToF forward/inverse-model discussion, after LCT/f-k/phasor-field mathematical formulations or near visibility/identifiability limitations. Emphasize that recent theory is moving beyond scalar isotropic reflectance toward directional fields and explicit null-space/range characterization.
- **Bibliography:** merge the verified entry staged in `egbib_20260924_directional_confocal_range.bib` into the canonical bibliography, preserving the repository's citation-key convention.
- **PDF:** rebuild `bare_jrnl.pdf` only after the canonical TeX and bibliography are safely updated.

## Consistency / safety note

Repository-wide exact-title search returned no match before staging. Large canonical files were not overwritten from partial content in this run. The staging BibTeX and this note are the verified changes; README/index/TeX/PDF still require canonical integration and rebuild.
