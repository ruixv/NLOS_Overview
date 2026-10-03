# Integration note: finite-aperture yaw limits in confocal NLOS

## Verified missing paper

Riccardo Romanelli, Lorenzo Francesco Livi, Francesco V. Pepe, Giacomo Sorelli, Enea Mauri, Milena D'Angelo, and Massimiliano Proietti, **“Finite-Aperture Limits for Yaw Estimation in Confocal Non-Line-of-Sight Imaging,”** *Journal of Imaging*, 12(6), 248, 2026. DOI: 10.3390/jimaging12060248.

Publisher metadata: https://doi.org/10.3390/jimaging12060248

## Why it belongs in NLOS_Overview

This is directly about confocal time-of-flight NLOS imaging rather than generic occlusion sensing. It characterizes how a finite sampled relay-wall aperture limits hidden planar-target yaw estimation. The paper derives a geometric switch-line visibility criterion and complements it with Fisher-information analysis of the transient, showing that loss of unique planar reconstruction and loss of useful angular information occur at different yaw angles. It validates the analysis experimentally and illustrates how the same finite-aperture limitation manifests differently in f-k migration and backprojection.

The paper explicitly situates the analysis relative to standard confocal transient reconstruction, the missing-cone/visibility problem, f-k reconstruction, backprojection, and related directional/polarization/transient-discontinuity approaches. It therefore fits the core active-ToF development line and is useful for a survey discussion of measurement geometry and fundamental observability limits.

## Recommended integration

- **README Latest Additions / 2026 timeline:** add under active ToF / theory and practical measurement limits.
- **Active NLOS → Forward Models or Reconstruction Algorithms:** summarize as a finite-relay-aperture observability analysis rather than a new reconstruction algorithm.
- **Website Paper Explorer:** tags: `Active`, `ToF`, `Confocal`, `Forward model`, `Visibility`, `Finite aperture`, `Fisher information`.
- **Milestone/development narrative:** place near work on NLOS visibility/missing-cone limits and after LCT/f-k/phasor-field formulations; emphasize the shift from reconstruction formulas toward quantifying which scene parameters remain observable under finite relay-wall support.
- **bare_jrnl.tex:** integrate into the active-NLOS theory/limitations discussion. Suggested literature-review sentence: “Recent work has further quantified the measurement-side limits imposed by finite relay apertures: Romanelli et al. derive a geometric switch-line criterion for planar-target yaw observability in confocal NLOS and show through Fisher information that angular sensitivity degrades continuously as informative transient regions are clipped, rather than vanishing exactly at the geometric reconstruction boundary.”
- **Bibliography:** merge `egbib_20261003_finite_aperture_yaw_gap.bib` into the canonical bibliography used by `bare_jrnl.tex` and cite it from the inserted survey sentence.
- **PDF:** rebuild `bare_jrnl.pdf` after canonical source/bibliography integration.

## Consistency / safety status

Repository-wide title search on the default branch returned no match before staging, so this was a verified gap at this run. Publisher metadata was checked against the Journal of Imaging article page; the final journal venue is used rather than an arXiv label. The canonical README/index/LaTeX files were not overwritten from a truncated large-file payload. This note and the verified BibTeX staging file preserve a safe integration path for the next complete read-edit-build cycle. Do not consider README/index/bare_jrnl.tex/bare_jrnl.pdf synchronized until those edits and the PDF rebuild are explicitly verified.
