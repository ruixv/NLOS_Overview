# NLOS survey consistency and citation-trace audit — 29 October 2026

## Scope and decision rule

This pass rechecked the repository's recent additions against `README.md`, `index.html`, `data/papers-source.html`, the dated update notes, the survey chapter sources, and the merged bibliography. Forward-citation searches were seeded from the field-defining active-NLOS works (Velten 2012, O'Toole/LCT 2018, Lindell/f-k migration 2019, and Liu/phasor-field papers), passive computational periscopy and PAC-Net/NLOS-Track, Neural Transient Fields and recent transient transformers, plus acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and Gaussian transient rendering. Candidates were retained only when their methods actually perform NLOS imaging/reconstruction or materially advance NLOS sensing, acquisition, or calibration.

No additional unlisted 2026 core successor survived the metadata-and-scope check. The audit did, however, find three papers already cataloged in README/Explorer but absent from the survey narrative and merged bibliography, as well as five earlier cataloged works missing from the narrative. All eight are now integrated into the appropriate active-NLOS sections.

## Papers integrated into the survey narrative

| Paper | Verified publication status | Survey placement and contribution |
|---|---|---|
| [Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging](https://doi.org/10.1364/OE.584776) | *Optics Express* 34(12), 22596–22613 (2026) | Active acquisition/calibration: lookup-table correction for pixel-dependent TCSPC bin widths and intrinsic diffraction/lens-flare features for absolute time referencing. |
| [Fast NLOS imaging at low sampling rates based on Poisson modeling](https://doi.org/10.1117/12.3091668) | *Proceedings of SPIE* 13992, 1399223 (2026; AOMATT 2025) | Active inverse reconstruction: Poisson-likelihood optimization with GPU-parallel Nesterov proximal-gradient updates at 1.56% sampling. |
| [Semantic-guided under sampling scanning for improving real-time performance of NLOS imaging](https://doi.org/10.1117/12.3094245) | *Proceedings of SPIE* 14000, 140004W (2026; CITA 2025) | Active acquisition planning: semantic relay-wall region selection followed by neighborhood sparse sampling. |
| [Non-line-of-sight reconstruction via structure sparsity regularization](https://doi.org/10.1364/OL.501622) | *Optics Letters* 48(18), 4881–4884 (2023) | Adds nuclear-norm structure-sparsity regularization to DLCT for low-SNR/short-exposure data. |
| [Automatic calibration of time of flight based non-line-of-sight reconstruction](https://arxiv.org/abs/2105.10603) | arXiv:2105.10603; no final venue verified in this pass | Jointly optimizes hidden-scene reconstruction and scan/relay calibration. |
| [Differentiable Transient Rendering](https://doi.org/10.1145/3478513.3480498) | *ACM Transactions on Graphics* 40(6), Article 286 (2021) | General differentiable transient path-integral renderer with non-planar-relay and two-corner NLOS demonstrations. |
| [Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier](https://arxiv.org/abs/2006.02600) | arXiv:2006.02600; no final venue verified in this pass | Quantifies partial-coherence error and practical validity limits for ideal phasor-field reconstruction. |
| [Cramer-Rao Lower Bound Optimization for Hidden Moving Target Sensing via Multi-IRS-Aided Radar](https://doi.org/10.1109/LSP.2022.3224681) | *IEEE Signal Processing Letters* 29, 2422–2426 (2022) | Multi-IRS hidden-target estimation bounds and Doppler-aware phase design; adjacent NLOS localization, not dense 3D imaging. |

## Final-venue and bibliography corrections

- Corrected the DLCT structure-sparsity record to its final *Optics Letters* venue rather than arXiv.
- Corrected *Differentiable Transient Rendering* to the 2021 ACM TOG issue and publisher DOI.
- Corrected the multi-IRS radar paper to *IEEE Signal Processing Letters* and its DOI.
- Replaced the earlier arXiv title/record for THz NLOS imaging with the final publication: [Seeing Around Obstacles Using Active Terahertz Imaging](https://doi.org/10.1109/TTHZ.2024.3401041), *IEEE Transactions on Terahertz Science and Technology* 14(4), 433–445 (2024). The arXiv preprint appeared under the title “Seeing Around Obstacles with Terahertz Waves.”
- Removed unused duplicate arXiv BibTeX keys where the same works are already cited through canonical final-venue or canonical survey keys. The two preprints above remain labeled arXiv because no final venue was verified.
- Updated the Paper Explorer proceedings metadata for the two SPIE papers and the Optics Express SPAD-calibration paper.

## Consistency and build checks

- All eight newly integrated citation keys are present in both `egbib_2026_updates.bib` and `egbib_merged_20260711.bib`.
- The merged bibliography has no duplicate BibTeX keys after the edit.
- The PDF build workflow now checks the eight new citation keys in the LaTeX auxiliary file.
- `README.md`, the website's Paper Explorer, survey chapter sources, and bibliography have been updated together.

**PDF status at note creation:** pending the post-merge GitHub Actions LaTeX build. The PDF will be reported as updated only after the build run and committed PDF blob are verified.
