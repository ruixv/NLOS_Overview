# 18 July 2026 passive-NLOS and geometry citation-tracing update

This update follows forward citations and direct methodological descendants of computational periscopy, passive light-transport inversion, transient surface optimization, and geometry-aware active NLOS reconstruction. Candidate papers were retained only when the primary task is hidden-scene imaging or reconstruction rather than generic NLOS propagation or localization.

## Newly integrated papers

### Passive non-line-of-sight imaging at 10 meters

- Authors: Yijun Zhou, Wenwen Li, Wei Li, Chen Dai, Jian-Wei Zeng, Feihu Xu
- Venue: *Optics Letters* 50(20), 6333–6336 (2025)
- DOI: `10.1364/OL.573268`
- Contribution: combines pattern-based calibration and low-rank matrix decomposition to enhance weak wall-encoded signals and separate ambient background. It demonstrates ordinary-camera passive NLOS at a 10 m wall-to-camera distance and a 4.5 m wall-to-object distance, with centimeter-scale resolution at an SBR down to −13 dB.

### Neural Networks Meet Light Transport Physics for Passive Non-Line-of-Sight Imaging Enhancement

- Authors: Rui Liang, Zhenjun Xu, Xi Tong, Jiangxin Yang, Xin Li, Yanpeng Cao
- Venue: *IEEE Transactions on Computational Imaging* 12, 282–296 (2026)
- DOI: `10.1109/TCI.2026.3653304`
- Contribution: introduces the HPDI hybrid physics–data framework. A physics-informed coarse-to-fine pathway and a data-driven implicit reconstruction pathway are adaptively fused, improving passive reconstruction fidelity, generalization, interpretability, and data efficiency across settings with and without occluders.

## Final-venue correction and survey completion

### Geometry-Constrained Non-Line-of-Sight Imaging

- Authors: Xueying Liu, Lianfang Wang, Jun Liu, Yong Wang, Yuping Duan
- Final venue: *IEEE Transactions on Visualization and Computer Graphics* 32(7), 6524–6536 (2026)
- DOI: `10.1109/TVCG.2026.3684832`
- Previous repository status: arXiv 2025 under the preliminary title “Geometric Constrained Non-Line-of-Sight Imaging”.
- Contribution: jointly reconstructs hidden albedo and surface normals, using a shape operator to regularize normal-field variation. The final paper reports improved geometric detail and robustness and approximately 30× faster optimization than an earlier surface-reconstruction baseline.

## Repository integration plan

The guarded synchronizer `scripts/sync_nlos_20260718_passive_geometry.py` performs idempotent, unique-anchor edits to:

- `README.md`: two new paper rows, the final TVCG venue correction, update date, and timeline entries;
- `index.html`: two new searchable entries, the corrected geometry record, tracked-entry count, and 2025/2026 timeline context;
- `article/3passive.tex`: a long-range passive-NLOS literature-review paragraph and table row, plus an HPDI deep-learning table row;
- `article/4datadriven.tex`: a hybrid physics–data passive reconstruction paragraph;
- `article/2active.tex`: a geometry-constrained joint normal/albedo paragraph.

`egbib_20260718_passive_geometry_updates.bib` provides the canonical metadata. Because dated supplements are merged in filename order, its `liuGeometricConstrainedNLOS2025` record supersedes the earlier arXiv metadata while preserving the citation key already used by the survey.

The associated GitHub Actions workflow runs the guarded edit, regenerates the duplicate-free bibliography, performs a clean LaTeX/BibTeX build, checks citation and bibliography integrity, renders both the previous and updated PDFs, verifies the new review phrases in the generated PDF, and commits the synchronized source artifacts and `bare_jrnl.pdf` only after validation succeeds.
