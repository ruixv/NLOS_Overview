# Verified NLOS frontier source update — 17 July 2026

This update records three newly verified direct NLOS-imaging papers and preserves the MDUNet / final-venue corrections identified earlier on 17 July 2026. The large public artifacts have **not** been replaced blindly through the GitHub Contents API. Instead, accurate canonical metadata and a guarded, anchor-checked synchronizer have been committed so the changes can be applied without truncating `README.md`, `index.html`, or the LaTeX survey.

## Newly verified papers

1. **Non-line-of-sight imaging via physics-informed cascade learning** — Rui Zhao, Yifan He, Yi-Ming Lin, Rui Chen; *Journal of the Optical Society of America A* 43(9), E9–E18, 2026; DOI: `10.1364/JOSAA.593401`; published 15 July 2026. PICL cascades SPAD-specific mixed-noise separation with a self-supervised reconstruction network containing a differentiable NLOS forward model.
2. **Thermal Non-Line-of-Sight Imaging through Rough Surfaces** — Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, Feihu Xu; *ACM Transactions on Graphics* 45(5), Article 41, pp. 1–21, 2026; DOI: `10.1145/3811030`; published 29 June 2026. NLOSFormer explicitly estimates a rough-wall thermal transport kernel, introduces ThermalNLOS, supports relative-depth estimation, and reconstructs dynamic scenes at 4 fps.
3. **All-day non-line-of-sight imaging based on Si-SPAD and phase-congruency-based structured ε-regularization** — Yuyang Yin, Yingjie Shi, Chenyang Wu, Taotao Qin, Lianfa Bai, Yi Zhang, Enlai Guo, Jing Han; *Optics and Lasers in Engineering* 205, 109919, 2026; DOI: `10.1016/j.optlaseng.2026.109919`. The detector-aware Si-SPAD design and structured virtual-phasor-field regularization demonstrate 200 m NLOS reconstruction under 94,314 lx illumination.

The final metadata corrections retained in the same synchronization set are:

- **MDUNet** — WACV 2026, pp. 461–471, DOI `10.1109/WACV61042.2026.00053`.
- **Imaging hidden objects with consumer LiDAR via motion-induced sampling** — *Nature* 653, 693–699, 2026, DOI `10.1038/s41586-026-10502-x`.
- **Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals** — CVPR 2026, pp. 1221–1230.
- **DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs** — CVPR 2026, pp. 3046–3055.

## Committed implementation

- `egbib_20260717_frontier_updates.bib` contains canonical BibTeX records for all seven papers above.
- `scripts/sync_nlos_20260717_frontier.py` performs guarded, idempotent updates to:
  - `README.md` latest additions and development timeline;
  - `index.html` paper explorer, tracked-entry count, update date, and 2026 timeline;
  - `article/2active.tex`, `article/3passive.tex`, `article/4datadriven.tex`, and `article/5newscenes.tex` at semantically appropriate locations;
  - `bare_jrnl.tex` paper-count statement;
  - the consolidated bibliography through the existing merge script.
- `.github/workflows/sync_nlos_frontier_20260717.yml` is prepared to apply the guarded update, merge and audit BibTeX, clean-build `bare_jrnl.pdf`, render both old and new PDFs, validate citations and generated text, and commit the regenerated binary.

## Current completion state

At the time this note was committed, the workflow had not produced the expected source-integration or PDF-rebuild commit. Therefore:

- the canonical metadata, synchronizer, workflow, and this explicit update record are committed;
- `README.md`, `index.html`, survey section files, merged bibliography, and `bare_jrnl.pdf` must **not** yet be described as mutually synchronized;
- `bare_jrnl.pdf` has **not** been claimed as regenerated in this update.

The next safe execution step is to run `python scripts/sync_nlos_20260717_frontier.py`, then `python scripts/merge_nlos_bibliography.py`, clean-compile `bare_jrnl.tex`, and run the validation checks encoded in the workflow before committing the generated PDF.
