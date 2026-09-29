# NLOS literature integration gap — 2026-09-29

This note records two verified papers that are absent from the repository's default-branch code-search index and should be integrated into the canonical README, website, survey source, bibliography, and regenerated PDF. The large canonical files were not overwritten from partial/truncated connector payloads.

## 1. 3D Gaussian Transient Rendering — final venue verified

**Yi Wang, Ziyu Zhan, Yuran Wang, Hao Wang, Qiang Liu, Zuoqiang Shi, Lingyun Qiu, Xing Fu, “Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering,” ACM SIGGRAPH 2026 Conference Papers, 85:1–85:11, DOI 10.1145/3799902.3811137.** Earlier version: arXiv:2606.21270.

Why it matters: this work removes the usual planar/dense relay-wall assumption by representing the hidden scene with 3D Gaussians and optimizing them through an efficient differentiable transient renderer. It supports spatially limited, sparse, arbitrarily shaped relay surfaces and both confocal and non-confocal measurements. This is an important bridge from neural/differentiable transient rendering to practical arbitrary-relay geometry.

Suggested integration:
- README Latest Additions / 2026 timeline: Active NLOS → learned/differentiable reconstruction; emphasize arbitrary relay geometry and sparse measurements.
- Website Paper Explorer / timeline: tags `active`, `transient`, `3DGS`, `differentiable-rendering`, `arbitrary-relay`, `SIGGRAPH-2026`.
- `bare_jrnl.tex`: place in the learned reconstruction / differentiable transient rendering discussion, after neural transient fields / learned transient representations and alongside emerging neural scene representations. Add a short trajectory sentence explaining the move from planar-wall transient inversion to explicit differentiable scene representations that tolerate arbitrary relay surfaces.
- Canonical bibliography: use the SIGGRAPH 2026 entry and DOI, not arXiv as the venue.

## 2. MD-NLOS — sparse, near-real-time model decomposition

**Peng Yang, Zewei Wang, Yinghui Guo, Xiaoying Li, Mingbo Pu, Hengshuo Guo, Mingfeng Xu, Fei Zhang, Yuanmao Wang, Xiangang Luo, “A model decomposition method for the real-time non-line-of-sight imaging,” iScience 29(6), 115828 (2026), DOI 10.1016/j.isci.2026.115828.**

Why it matters: MD-NLOS derives an LCT-based model decomposition, formulates sparse transient reconstruction as a non-negative LASSO problem, uses spectral filtering and GPU-friendly frequency-domain operations, and targets the acquisition/reconstruction bottleneck jointly. The paper reports 128×128 experimental reconstructions from 64 relay-wall samples in 4.6 s and 256×256 synthetic reconstruction from 36 samples in 3.1 s.

Suggested integration:
- README Latest Additions / 2026 timeline: Active NLOS → sparse acquisition / efficient reconstruction.
- Website Paper Explorer: tags `active`, `LCT`, `sparse-sampling`, `optimization`, `real-time`, `iScience-2026`.
- `bare_jrnl.tex`: place after LCT-derived inversion and sparse/regularized reconstruction methods, with a sentence on model decomposition making sparse optimization computationally practical via point-wise frequency-domain operators.
- Canonical bibliography: use the final iScience metadata and DOI.

## Verification and consistency status

Repository-wide exact-title / distinctive-term searches returned no default-branch matches for either paper at the start of this run. Final venue for 3D Gaussian Transient Rendering was verified through DBLP (SIGGRAPH 2026, DOI 10.1145/3799902.3811137); MD-NLOS final metadata was verified through iScience/PubMed (vol. 29, issue 6, article 115828, DOI 10.1016/j.isci.2026.115828). Verified BibTeX is staged in `egbib_20260929_missing_nlos_batch.bib`.

Remaining work: safely integrate both entries into `README.md`, `index.html`, `bare_jrnl.tex`, and the canonical bibliography, then compile and commit `bare_jrnl.pdf` and verify all public-facing artifacts are mutually consistent. Do not claim those canonical artifacts are updated until that build/integration is actually verified.
