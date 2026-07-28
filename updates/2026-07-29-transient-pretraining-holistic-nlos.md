# Transient pretraining, unified reconstruction, and holistic 3D NLOS update — 29 July 2026

## Status

A recent-paper, lab-page, and forward-lineage audit identified two missing works and one cross-artifact inconsistency:

1. **Real-Time and High-Fidelity Non-Line-of-Sight Imaging** is absent from the README, website explorer/timeline, survey prose, and consolidated bibliography.
2. **MARMOT: Masked Autoencoder for Modeling Transient Imaging** is already present in the website explorer/timeline and consolidated bibliography, but is missing from README and the LaTeX survey. Its current BibTeX author field is incomplete and misspells Siyuan Shen.
3. **HOLI-1-to-3: Transient-Enhanced Holistic Image-to-3D Generation** is absent from the README, website, survey, and consolidated bibliography even though a final TPAMI publication is verifiable.

Canonical metadata is provided in `egbib_20260729_transient_pretraining_holistic_nlos.bib`.

## Verified papers

### Real-Time and High-Fidelity Non-Line-of-Sight Imaging

- Authors: Xiangyang Ji, Jianyu Wang, Leping Xiao, Shiwei Wu, Yuran Wang, Zuoqiang Shi, Lingyun Qiu, Xing Fu
- Status: Research Square preprint, version posted 6 March 2026
- DOI: `10.21203/rs.3.rs-8336286/v1`
- Contribution: proposes a unified inverse framework for both see-through-scattering-media and see-around-corner NLOS. Scale modulation and joint regularization recover hidden albedo and depth across diverse measurement settings, and the accompanying dataset spans both scenario classes.
- Categorization: direct active/computational NLOS reconstruction; preprint because no final journal or conference venue was verified.

### MARMOT: Masked Autoencoder for Modeling Transient Imaging

- Authors: Siyuan Shen, Ziheng Wang, Xingyue Peng, Suan Xia, Ruiqian Li, Shiying Li, Jingyi Yu
- Status: arXiv:2506.08470, 2025; no final venue verified
- DOI: `10.48550/arXiv.2506.08470`
- Contribution: self-supervised masked pretraining on the 500,000-model TransVerse transient dataset. Its scanning-pattern mask treats the retained subset as arbitrary sampling and learns to predict complete transients, enabling feature transfer or decoder fine-tuning for downstream NLOS tasks.
- Categorization: learned transient representation / masked pretraining / arbitrary-sampling completion.

### HOLI-1-to-3: Transient-Enhanced Holistic Image-to-3D Generation

- Authors: Siyuan Shen, Suan Xia, Xingyue Peng, Ziyu Wang, Yingsheng Zhu, Shiying Li, Jingyi Yu
- Venue: IEEE Transactions on Pattern Analysis and Machine Intelligence 47(9), 7206–7217, 2025
- DOI: `10.1109/TPAMI.2024.3463875`
- Contribution: unifies an LOS radiance field and an NLOS transient field in a neural plenoptic representation. Diffusion and transient priors recover both visible and invisible object geometry from one viewpoint.
- Categorization: tightly adjacent NLOS-enabled holistic 3D generation, not a conventional relay-wall-only reconstruction method.

## Citation-tracing rationale

The two Shen et al. works are direct descendants of the Neural Transient Fields trajectory. MARMOT changes the learned transient branch from scene-specific optimization or supervised task training to reusable self-supervised pretraining, while HOLI-1-to-3 uses transient-field evidence to constrain geometry invisible to a conventional LOS image. The Research Square work explicitly unifies two NLOS scenario families and belongs beside LCT, f-k, phasor-field, Quasi-Fresnel, and regularized inverse methods rather than being an incidental NLOS citation.

## Exact integration plan

### `README.md`

Add all three records at the top of **Latest Additions**. Add MARMOT and HOLI-1-to-3 to the 2025 timeline as the shift toward reusable transient pretraining and NLOS-conditioned holistic 3D completion. Add the unified reconstruction preprint to the 2026 timeline, clearly labeled as a preprint.

### `index.html`

- Preserve the existing MARMOT explorer object and timeline mention; do not duplicate it.
- Add searchable objects for the unified reconstruction preprint and HOLI-1-to-3.
- Recommended tags:
  - `latest active reconstruction unified inverse regularization scattering corner preprint`
  - `latest learning transient-fields holistic-3d los-nlos diffusion`
- Recalculate the displayed paper count from the JavaScript object count rather than hard-coding it.

### `article/2active.tex`

After the Quasi-Fresnel discussion, add **Unified reconstruction across NLOS scenario classes**, explaining that Ji et al. use scale modulation and joint regularization to span through-medium and around-corner measurements while recovering albedo and depth. Keep the Research Square status explicit.

### `article/4datadriven.tex`

1. After the shared learned-representation discussion, add **Masked transient pretraining**, explaining MARMOT, the scanning-pattern mask, TransVerse, and the shift from task-specific inversion to reusable transient features.
2. After the Neural Transient Fields discussion, add **From hidden reconstruction to holistic 3D completion**, explaining how HOLI-1-to-3 unifies radiance and transient fields and uses NLOS evidence to constrain invisible geometry.

### `bare_jrnl.tex`

Add a trace marker noting integration of unified cross-scenario reconstruction, masked transient pretraining, and NLOS-enhanced holistic 3D generation.

### Bibliography

- Replace the incomplete `shenMARMOT2025` record in `egbib_merged_20260711.bib` with the complete seven-author arXiv metadata from the canonical file.
- Add `jiUnifiedRealTimeNLOS2026` and `shenHOLI1to3TPAMI2025` exactly once.

## Build and validation

After source integration, run a clean `pdflatex → bibtex → pdflatex ×2` build. Verify that:

1. each DOI occurs once in the appropriate public artifacts and consolidated bibliography;
2. MARMOT has one website object, one complete BibTeX record, a README row, and a resolved survey citation;
3. the two new website objects increment the actual explorer count by exactly two and the displayed count matches it;
4. the LaTeX log contains no undefined citations or repeated bibliography entries;
5. extracted PDF text contains all three titles or unambiguous title fragments;
6. the first and last PDF pages render successfully;
7. the PDF binary changes before any claim that `bare_jrnl.pdf` was regenerated.

## Latest-publication check

No direct NLOS-imaging publication later than 22 July 2026 was verified in this pass. The latest date-verified direct paper remains *Iterating the transient light transport matrix for non-line-of-sight imaging* in *Nature Communications*.
