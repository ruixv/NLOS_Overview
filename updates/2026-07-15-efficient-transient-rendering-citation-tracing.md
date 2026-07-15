# 15 July 2026 citation-tracing update: efficient transient NLOS rendering

## Search result

Fresh searches of arXiv, conference and journal indexes, project pages, and recent NLOS modality terms did not identify a directly relevant NLOS-imaging paper newer than the repository's 5 July 2026 NIR raster-scanning entry that could be independently metadata-verified in this run.

The citation/reference-tracing pass did identify a meaningful public-artifact gap:

- **Julian Iseringhausen and Matthias B. Hullin, “Non-Line-of-Sight Reconstruction Using Efficient Transient Rendering,” ACM Transactions on Graphics 39(1), 2020.** DOI: `10.1145/3368314`.

The paper is genuinely active transient NLOS reconstruction. It uses a custom GPU renderer for time-resolved three-bounce transport inside a nonlinear analysis-by-synthesis optimization, represents the hidden object as an implicit level-set surface, and models BRDF-dependent scattering, orientation, visibility, and self-occlusion. Its experiments include synthetic and measured transient data, noise, and non-diffuse materials.

This work directly continues the Velten-style transient reconstruction and LCT-era forward-model trajectory. Later transient inverse-rendering papers, including fast differentiable transient rendering and 3D Gaussian Transient Rendering, cite it as an early physically based surface-optimization approach. It is therefore a field-development milestone rather than a paper that merely cites NLOS in passing.

## Repository gap before this update

The paper already had an accurate DOI-bearing bibliography record and appeared only in the broad active-method table through citation key `iseringhausen:2018`. It was absent from:

- the README latest/missing-paper list;
- the README milestone timeline;
- the homepage paper explorer;
- the homepage development timeline; and
- the survey's inverse-rendering narrative.

## Applied synchronization

The synchronization script performs idempotent, marker-checked edits:

1. Adds the final ACM TOG 2020 paper and concise contribution summary to `README.md`.
2. Adds a 2020 development milestone connecting physically based analysis-by-synthesis to later differentiable and neural transient rendering.
3. Adds one searchable homepage paper object and increments the tracked-entry count from 99 to 100.
4. Extends the homepage 2020 timeline.
5. Inserts a semantically placed literature-review paragraph in `article/2active.tex`, between the inverse-rendering introduction and the later fast differentiable transient-rendering work.
6. Adds a canonical dated BibTeX correction source using the existing survey key `iseringhausen:2018`, final ACM TOG venue, DOI, journal volume/issue, publisher, ISSN, and DOI URL.
7. Rebuilds the merged bibliography and `bare_jrnl.pdf`, then validates source, citation, bibliography, and PDF consistency.

No large source file is overwritten blindly: all edits are guarded by exact anchors and uniqueness checks.
