# 26 August 2026 — polarization-speckle NLOS consistency gap

## Verified paper

Yijun Zhou, Wenwen Li, Wei Li, Xin Huang, Chen Dai, Zhong-Pei Xiao, Zheng-Ping Li, Feihu Xu, and Jian-Wei Pan, “Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation,” *Physical Review Letters*, 136(14), 143801, 2026. DOI: `10.1103/kd8v-fykm`.

APS lists the article as published on 6 April 2026. The work demonstrates polarization-based scanning-free NLOS single-pixel imaging: polarization changes generate diverse speckle illuminations at a rough relay wall, a single-pixel detector records the hidden-scene responses, and angular-memory-effect calibration enables noninvasive calibration. The reported system achieves millimeter-scale keyhole reconstruction.

## Current repository state

This is **not** a newly discovered paper entry for every artifact. The current repository already contains the paper in `README.md` (including the 2026 development timeline) and `article/2active.tex`, where the existing survey prose and active-method table cite the canonical key `zhouPolarizationSpeckleNLOS2026`.

The consistency gap is narrower and should be fixed without duplication:

1. `data/papers-source.html` does not currently contain the title/key, so the V2 Paper Explorer / graph corpus cannot surface the paper.
2. `egbib_merged_20260711.bib` does not currently contain `zhouPolarizationSpeckleNLOS2026`, even though `article/2active.tex` cites that key.
3. `egbib.bib` also does not contain the key.

A verified staging entry is provided in `egbib_20260826_polarization_speckle_gap.bib`.

## Safe integration plan

### README.md

Do **not** add a second paper row or a second 2026 timeline entry. The paper is already present. Only preserve the existing PRL metadata and contribution summary.

### V2 website / canonical corpus

Insert one paper record into `data/papers-source.html` with:

- Title: `Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation`
- Authors: Yijun Zhou; Wenwen Li; Wei Li; Xin Huang; Chen Dai; Zhong-Pei Xiao; Zheng-Ping Li; Feihu Xu; Jian-Wei Pan
- Year: 2026
- Venue: `Physical Review Letters 136(14), 143801 (2026)`
- DOI URL: `https://doi.org/10.1103/kd8v-fykm`
- Citation key: `zhouPolarizationSpeckleNLOS2026`
- Family/category: active optical / single-pixel / polarization-coded steady-state NLOS
- Contribution: polarization diversity at a rough relay wall generates scanning-free speckle illumination codes; single-pixel measurements recover hidden scenes with millimeter-scale keyhole resolution and noninvasive angular-memory-effect calibration.

Recompute any tracked-entry count from the resulting corpus rather than manually guessing the number. Do not duplicate the already existing 2026 development-timeline wording unless the V2 timeline itself lacks it.

### LaTeX survey

`article/2active.tex` already contains the appropriate literature-review prose and method-table citation. Do **not** append a second paragraph. Preserve the existing key `zhouPolarizationSpeckleNLOS2026`.

### Bibliography

Merge the entry from `egbib_20260826_polarization_speckle_gap.bib` into the canonical bibliography used by `bare_jrnl.tex` exactly once. Prefer the existing citation key `zhouPolarizationSpeckleNLOS2026`; do not create an alias key. Verify DOI uniqueness for `10.1103/kd8v-fykm`.

### bare_jrnl.tex / PDF

No new survey prose is required. If the repository convention records update provenance/date in `bare_jrnl.tex`, update that marker only after the bibliography and V2 corpus are synchronized.

Rebuild the survey using the repository’s normal clean LaTeX/BibTeX sequence (equivalent to `pdflatex -> bibtex -> pdflatex -> pdflatex`). Before committing a regenerated `bare_jrnl.pdf`, verify:

- `zhouPolarizationSpeckleNLOS2026` is resolved in `.aux/.bbl` with no undefined citation;
- DOI `10.1103/kd8v-fykm` occurs once in the canonical bibliography;
- README contains one paper entry, V2 contains one paper entry, and the survey contains the existing prose only once;
- extracted PDF text contains the polarization-speckle discussion and the PRL bibliography record;
- representative PDF pages render correctly.

Until those checks pass and the rebuilt binary is actually committed, do not claim that `bare_jrnl.pdf` has been updated in response to this gap.
