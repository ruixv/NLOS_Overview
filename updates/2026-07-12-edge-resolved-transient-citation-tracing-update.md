# 12 July 2026 edge-resolved transient imaging citation-tracing update

## Search result

A fresh search of recent arXiv, conference, journal, project-page, and lab-page updates did not reveal a newer high-confidence direct NLOS-imaging paper than the 5 July 2026 NIR raster-scanning preprint already covered by the repository. The newest verified frontier items returned by the search, including arbitrary-relay 3D Gaussian Transient Rendering and the comparative ToF NLOS study, were already present.

The high-priority citation-tracing pass did reveal one directly relevant missing milestone paper:

- **Seeing Around Corners with Edge-Resolved Transient Imaging** — Joshua Rapp, Charles Saunders, Julián Tachella, John Murray-Bruce, Yoann Altmann, Jean-Yves Tourneret, Stephen McLaughlin, Robin M. A. Dawson, Franco N. C. Wong, and Vivek K. Goyal.
- **Final venue:** *Nature Communications*, 2020.
- **DOI:** `10.1038/s41467-020-19727-4`.
- **arXiv:** `2002.07118`.

The paper is genuinely NLOS imaging rather than a passing citation. It explicitly develops an active optical corner-imaging system that combines pulsed illumination, a gated SPAD/TCSPC detector, and a vertical edge occluder. Adjacent transient histograms isolate successive angular wedges; the method reconstructs a 2.5D plan view with surface heights over a 180-degree field of view. Experiments use 45 illumination locations on a 1.5 cm semicircular arc and recover hidden rooms up to 3 m in each dimension, with approximately 10 cm height accuracy for the reported staircase target.

The paper also directly connects the active and passive branches of the field and cites the repository's core seeds, including Velten et al. 2012, O'Toole et al. 2018 LCT, Lindell et al. 2019 f-k migration, Liu et al. phasor-field imaging, computational periscopy, and acoustic NLOS.

## Repository integration

The update synchronizes the paper across:

1. `README.md` Latest Additions and milestone timeline.
2. `index.html` paper explorer, tracked-entry count, and 2020 development timeline.
3. `article/2active.tex`, immediately before the recent-SPAD-advances discussion, where its combination of time-of-flight ranging and occlusion-coded angular resolution is most relevant.
4. `egbib_20260712_erti_updates.bib`, using the verified final Nature Communications venue and DOI.
5. `egbib_merged_20260711.bib`, regenerated through the repository's duplicate-free bibliography merger.
6. `bare_jrnl.pdf`, rebuilt from a clean LaTeX/BibTeX state and checked for undefined citations and visible paper metadata.

The synchronization script is marker-based and idempotent; it aborts rather than overwriting a large public-facing file when an expected insertion marker is missing or ambiguous.

**Build result:** pending the automated clean LaTeX/BibTeX synchronization and PDF validation triggered by this update.
