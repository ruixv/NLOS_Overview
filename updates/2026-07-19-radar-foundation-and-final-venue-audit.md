# 19 July 2026 radar-foundation citation trace and final-venue audit

STATUS: STAGED — verified metadata has been committed in dated BibTeX supplements, but the large public/source files and `bare_jrnl.pdf` have not been overwritten or rebuilt in this pass.

## Search and verification scope

This pass combined fresh keyword searches with a forward/backward citation trace around the optical core papers and the repository's modality-expansion milestones. In particular, the radar branch was followed backward from the staged 2026 range-migration operator-learning paper through its directly cited measured-mmWave reconstruction lineage. Candidates were retained only when the publisher record and abstract established genuine hidden-target NLOS 3D reconstruction rather than detection-only, communications-only, or a passing citation.

The most recent journal paper with an explicit verified online-publication date remains *Non-line-of-sight imaging via physics-informed cascade learning* (JOSA A, published 15 July 2026, DOI `10.1364/JOSAA.593401`). The final 3D-GTR record belongs to SIGGRAPH Conference Papers '26, whose conference dates are 19–23 July 2026, but the public metadata checked in this pass did not expose a separate online-publication date for ordering it against PICL.

## Newly verified missing radar/mmWave reconstruction papers

### Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar

- Authors: Shunjun Wei, Jinshan Wei, Xinyuan Liu, Mou Wang, Shan Liu, Fan Fan, Xiaoling Zhang, Jun Shi, Guolong Cui
- Final venue: *IEEE Transactions on Geoscience and Remote Sensing*, vol. 60, article 5106518, pp. 1–18, 2022
- DOI: `10.1109/TGRS.2021.3112579`
- Contribution: establishes a measured 77-GHz MIMO mmWave around-corner 3D imaging model, derives resolution, and introduces mirror-symmetry backprojection with minimum-entropy phase-error compensation. This is a foundational radar-modality milestone rather than a localization-only paper.

### Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging

- Authors: Xiang Cai, Shunjun Wei, Yanbo Wen, Jiangbo Hu, Mou Wang, Jun Shi, Guolong Cui
- Final venue: *Journal of Radars*, 13(4), 791–806, 2024
- DOI: `10.12000/JR24060`
- Contribution: separates LOS/NLOS multipath echoes with a model-driven procedure and jointly reconstructs hidden geometry under total-variation, sparsity, relay-phase-error, and minimum-MSE constraints. Measured corner experiments reconstruct knives and metal racks.
- Citation-trace relevance: directly builds on the 2022 TGRS mmWave 3D system and cites Velten's 2012 optical NLOS milestone as part of the cross-modality lineage.

### RM-CSTV: An Effective High-Resolution Method of Non-Line-of-Sight Millimeter-Wave Radar 3-D Imaging

- Authors: Xinyuan Liu, Shunjun Wei, Wei Pu, Xiang Cai, Yanbo Wen, Shisheng Guo, Lingjiang Kong, Xiaoling Zhang
- Final venue: *National Science Open*, 3(5), article 20230085, 2024
- DOI: `10.1360/nso/20230085`
- Contribution: embeds a fast range-migration kernel in a complex sparse/total-variation reconstruction, uses NLOS geometric constraints for relay extraction and target-position correction, preserves target contours under sparse sampling, and reports approximately two orders of magnitude lower computation than matrix-based CSTV.
- Development role: forms the direct algorithmic bridge from the 2022 measured mmWave model to the staged 2026 learned range-migration/FISTA operator.

Canonical metadata is stored in `egbib_20260719_radar_foundation_trace.bib`.

## Final-venue corrections found during the audit

### Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering

- The README already labels the work as SIGGRAPH 2026 but still links to the arXiv record.
- Verified final record: SIGGRAPH Conference Papers '26, 11 pages, DOI `10.1145/3799902.3811137`.
- The public link and bibliography should use the ACM DOI; the arXiv identifier `2606.21270` may remain as a secondary source.

### TransiT: Transient Transformer for Non-line-of-sight Videography

- The README already labels the work as ICCV 2025 but still links to arXiv.
- Verified final record: Ruiqian Li, Siyuan Shen, Suan Xia, Ziheng Wang, Xingyue Peng, Chengxuan Song, Yingsheng Zhu, Tao Wu, Shiying Li, Jingyi Yu; ICCV 2025, pp. 27542–27551.
- Replace the preliminary link/metadata with the official CVF record while retaining the arXiv link only as secondary material.

### Dual-branch Graph Feature Learning for NLOS Imaging (DG-NLOS)

- The README currently exposes this paper as arXiv 2025.
- Verified final record: Xiongfei Su, Tianyi Zhu, Lina Liu, Zheng Chen, Yulun Zhang, Siyuan Li, Juntian Ye, Feihu Xu, Xin Yuan; AAAI 2025, vol. 39(7), pp. 7051–7059; DOI `10.1609/aaai.v39i7.32757`.
- The README, homepage, survey prose, and bibliography should use AAAI 2025 as the venue.

Canonical final-venue metadata is stored in `egbib_20260719_final_venue_audit.bib`.

The previously staged correction of *Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors* to ICCV 2025 remains valid and should be applied in the same source-normalization pass. Its details are recorded in `updates/2026-07-19-ptycho-and-venue-followup.md`.

## Precise cross-artifact integration plan

### `README.md`

1. Add one row for each of the three radar papers above to **Latest Additions**.
2. In the development timeline, represent the radar reconstruction trajectory as:
   - 2022: measured 77-GHz MIMO NLOS 3D model and mirror-symmetry backprojection;
   - 2024: model-driven multipath separation/phase-error-aware sparse reconstruction and RM-CSTV acceleration;
   - 2026: range-migration operator learning and deep-unfolded sub-THz reconstruction.
3. Replace the 3D-GTR URL with `https://doi.org/10.1145/3799902.3811137` and normalize the venue to `ACM SIGGRAPH 2026`.
4. Replace the TransiT URL with the official ICCV page and retain `ICCV 2025`.
5. Replace DG-NLOS's arXiv venue/link with `AAAI 2025` and `https://doi.org/10.1609/aaai.v39i7.32757`.
6. Apply the already staged ICCV 2025 correction for Learnable Physical Priors.

### `index.html`

1. Add searchable objects for the three radar papers with categories covering `radar`, `rf`, `mmwave`, `3d reconstruction`, `range migration`, `sparse reconstruction`, and `phase error`.
2. Correct the `url` and `venue` fields of 3D-GTR, TransiT, DG-NLOS, and Learnable Physical Priors.
3. Extend the 2022/2024/2026 timeline entries with the radar reconstruction lineage above.
4. Recompute the tracked-entry statistic from the actual paper-object count rather than incrementing it manually.

### Survey source

- In `article/5newscenes.tex`, insert a compact radar-development paragraph before the staged 2026 operator-learning paragraph. It should explain the progression from mirror-symmetry backprojection, through phase-error-aware sparse/TV inversion and RM-CSTV, to learned range-migration operators. This is semantically preferable to appending a disconnected list.
- In `article/4datadriven.tex`, identify TransiT as the final ICCV 2025 paper and DG-NLOS as the final AAAI 2025 paper wherever they are discussed.
- In the transient-rendering discussion, cite 3D-GTR with its final SIGGRAPH metadata and describe arbitrary, spatially limited, non-planar relay geometry as its field-level contribution.
- Apply the pending ptychographic-correlography, learned radar/THz, and Learnable Physical Priors updates recorded in `updates/2026-07-19-ptycho-and-venue-followup.md` during the same merge, avoiding duplicated paragraphs.
- In `bare_jrnl.tex`, retain the existing section structure, update the source-audit marker only after the included section files and bibliography are synchronized, and do not claim coverage that is absent from the compiled PDF.

### Bibliography and PDF

1. Merge `egbib_20260719_radar_foundation_trace.bib` and `egbib_20260719_final_venue_audit.bib` into the bibliography used by `bare_jrnl.tex`.
2. Preserve existing citation keys if they are already referenced in LaTeX; use the dated supplements as metadata overrides and reject duplicate title/DOI records.
3. Clean-build with LaTeX/BibTeX or `latexmk`.
4. Verify that every added or corrected citation appears in the generated `.bbl`, that the log has no undefined citations, and that the PDF contains the phrases `mirror-symmetry backprojection`, `RM-CSTV`, `AAAI 2025`, `ICCV 2025`, and `3D Gaussian Transient Rendering`.
5. Render-check every PDF page before committing the regenerated binary.

## Current repository state

The dated BibTeX supplements are committed. The exact-title and DOI checks did not find the three radar papers in the current public snapshot, while README currently retains preliminary links or venues for 3D-GTR, TransiT, DG-NLOS, and Learnable Physical Priors.

Because the available GitHub write interface replaces existing large files as whole blobs and this environment cannot clone the repository or run its LaTeX toolchain, `README.md`, `index.html`, survey sections, merged bibliography, and `bare_jrnl.pdf` were not overwritten blindly. The PDF is **not** claimed as regenerated in this pass.
