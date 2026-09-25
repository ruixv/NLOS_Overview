# NLOS literature gap update — 2026-09-25 (batch 4)

This patch note records three metadata-verified 2026 papers that were absent from repository-wide title searches at discovery time. They were found during forward-citation / related-work tracing from the active transient NLOS lineage and should be integrated into the canonical README, homepage/Paper Explorer, survey source, bibliography, and rebuilt PDF when those large files can be edited from complete payloads.

## 1. Super-field-of-view non-line-of-sight imaging via spatial encoding of a translated point spread function

- **Authors:** Tongyao Li, Yingjie Shi, Jinye Miao, Yi Wei, Lingfeng Liu, Lianfa Bai, Enlai Guo, Jing Han
- **Venue:** *Photonics Research* 14(5), 1959–1972 (2026)
- **DOI:** 10.1364/PRJ.583728
- **Published:** 24 Apr 2026 (publisher-formatted article); DOI metadata verified.
- **Contribution:** Introduces a translated-PSF forward model plus spatial encoding to reconstruct hidden targets beyond the conventional detection region. Simulations cover an area equivalent to 9× the detection region; experiments recover targets beyond 2× the detection range along one direction and demonstrate stitched large-FoV reconstruction from a single scan.
- **Recommended taxonomy:** Active / transient NLOS → forward models & reconstruction → field-of-view extension / spatial encoding.
- **Timeline role:** Extends the LCT/convolutional-operator lineage from efficient inversion inside a nominal relay-wall support to computationally expanded hidden-scene field of view.

## 2. CUDA-accelerated non-line-of-sight imaging with irregular relay surfaces

- **Authors:** Yi Sun, Yu Hong, Ziheng Qiu, Wei Li, Wenwen Li, Qilin Sun, Feihu Xu
- **Venue:** *Optics and Lasers in Engineering* 200, 109591 (2026)
- **DOI:** 10.1016/j.optlaseng.2025.109591
- **Contribution:** Backprojection directly supports irregular relay geometry and arbitrary non-uniform scan patterns without planarization/resampling; frequency-domain bandpass filtering suppresses noise/multipath, while a CUDA implementation provides at least two orders of magnitude speedup over CPU baselines.
- **Recommended taxonomy:** Active / transient NLOS → arbitrary relay surfaces / practical reconstruction / GPU acceleration.
- **Timeline role:** A useful bridge between classical backprojection, practical non-planar relay surfaces, and the newer arbitrary-relay differentiable-rendering / 3D-Gaussian direction.

## 3. A model decomposition method for the real-time non-line-of-sight imaging

- **Authors:** Peng Yang, Zewei Wang, Yinghui Guo, Xiaoying Li, Mingbo Pu, Hengshuo Guo, Mingfeng Xu, Fei Zhang, Yuanmao Wang, Xiangang Luo
- **Venue:** *iScience* 29(6), 115828 (2026)
- **DOI:** 10.1016/j.isci.2026.115828
- **Contribution:** MD-NLOS reformulates an LCT-based confocal model as a non-negative LASSO problem, uses residual-domain spectral filtering and GPU-parallelizable frequency-domain operations, and targets sparse/undersampled acquisition. Reported experimental 128×128 reconstruction uses 64 samples in 4.6 s; 64×64 cases approach sub-second reconstruction.
- **Recommended taxonomy:** Active / transient NLOS → sparse/under-scanned reconstruction → real-time physics-based optimization.
- **Timeline role:** Continues the LCT → under-scanning/regularized inversion → GPU-friendly near-real-time model-based reconstruction trajectory without requiring learned training data.

## Integration locations

1. **README.md:** add concise entries to Latest Additions; place Super-FoV and MD-NLOS under Active NLOS / Reconstruction Algorithms, and CUDA irregular-relay under practical/arbitrary-relay reconstruction. Add 2026 timeline nodes only if they improve the historical narrative rather than duplicating the catalogue.
2. **index.html / Paper Explorer:** add searchable records with tags such as `active`, `transient`, `super-fov`, `spatial-encoding`; `irregular-relay`, `backprojection`, `cuda`; and `undersampling`, `lasso`, `real-time`, respectively. Add to Latest Additions and timeline consistently with README.
3. **bare_jrnl.tex:** integrate semantically rather than as a tail list. Suggested discussion: (a) after convolution/LCT and sparse-scanning discussion, note translated-PSF spatial encoding as an FoV-extension of convolutional NLOS models; (b) in practical/general relay geometry discussion, contrast CUDA backprojection on irregular surfaces with differentiable arbitrary-relay approaches; (c) in efficient/undersampled reconstruction, describe MD-NLOS as a non-negative LASSO/spectral-filtering route toward near-real-time model-based reconstruction.
4. **Bibliography:** merge the verified entries staged in `egbib_20260925_missing_nlos_batch4.bib` into the bibliography actually referenced by `bare_jrnl.tex`, preserving repository citation-key conventions.
5. **PDF:** rebuild `bare_jrnl.pdf` only after canonical TeX and bibliography integration succeeds; do not treat this note or staging bibliography as evidence that the PDF has been rebuilt.

## Consistency status

Canonical README/index/TeX/PDF were intentionally not overwritten from a truncated large-file payload. This note and the staging BibTeX are the safe recovery artifacts for the next full-file integration pass. The three papers should not be considered fully integrated until README, website, `bare_jrnl.tex`, canonical bibliography, and regenerated `bare_jrnl.pdf` are mutually consistent.
