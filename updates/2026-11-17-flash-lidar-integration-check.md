# 2026-11-17 Flash-LiDAR NLOS integration audit (pending)

## Verified candidate

Peizhao Qiu, Emmanuel A. Olowe, Zhenya Zang, Istvan Gyongy, and Danial Chitnis, **Simulation-Driven Approach for Occlusion-Based Non-Line-Of-Sight Detection Using a Low-Cost Flash LiDAR**, arXiv:2611.04068 (submitted 2 November 2026), https://arxiv.org/abs/2611.04068 . No final peer-reviewed venue was verified in this pass; do not label as a journal or conference paper without evidence.

This is **occlusion-based hidden-target detection**, not hidden-scene 3D reconstruction. Photon Monte Carlo simulations train a classifier to detect multi-bounce target signatures from a low-cost TMF8829 SPAD flash LiDAR. Reported synthetic AP: 0.91; 180 real measurements: 86.67% accuracy and 0.95 AP. Categorize under active ToF / consumer SPAD LiDAR / NLOS detection, and distinguish from around-the-corner imaging.

## Repository audit and safe insertion plan

On 17 November 2026 the complete current master versions of README.md (234597 characters), data/papers-source.html (262736 characters), article/2active.tex (151589 characters), and egbib_merged_20260711.bib (465666 characters) were fetched via the GitHub contents connector. None contained the arXiv identifier 2611.04068. These are substantial files: do not replace them using truncated excerpts.

1. README.md: insert a 2026 active-optical / low-cost consumer LiDAR NLOS detection entry in the chronological paper list and timeline, with arXiv status and the detection-vs-reconstruction distinction.
2. data/papers-source.html: add the matching Paper Explorer record in the source data and update latest additions / 2026 timeline; check whether index.html consumes this file before editing the site wrapper.
3. article/2active.tex: place a brief discussion in the active ToF / SPAD / consumer LiDAR section, noting that simulation-to-real occlusion detection extends low-cost NLOS sensing but does not recover 3D shape. Add a citation in the relevant table only if its task column explicitly says detection.
4. egbib_merged_20260711.bib: add the verified entry below, retaining the same key across chapters. Ensure bare_jrnl.tex includes article/2active.tex through its existing input mechanism; compile and inspect bare_jrnl.pdf after source integration.
5. Validate README, website, survey text, bibliography, and compiled PDF before merging. Current PDF is **not** verified updated.

```bibtex
@misc{qiuSimulationDrivenOcclusionNLOS2026,
  author = {Qiu, Peizhao and Olowe, Emmanuel A. and Zang, Zhenya and Gyongy, Istvan and Chitnis, Danial},
  title = {Simulation-Driven Approach for Occlusion-Based Non-Line-Of-Sight Detection Using a Low-Cost Flash {LiDAR}},
  year = {2026},
  eprint = {2611.04068},
  archivePrefix = {arXiv},
  primaryClass = {eess.IV},
  url = {https://arxiv.org/abs/2611.04068},
  note = {Preprint, submitted 2 November 2026; final venue not verified}
}
```

## Other checks

The repository already contains the 2026 finite-aperture yaw estimation and learned light-cone transform papers in README, Paper Explorer, and bibliography; do not duplicate them. MALCT final Optics Express venue was previously synchronized. This pass used targeted literature discovery and repository comparisons; it did **not** exhaustively export all forward citations for every foundational seed.

**Status:** staging/audit only; README, website, LaTeX, BibTeX and PDF remain unchanged by this note. Keep the recurring literature check running.
