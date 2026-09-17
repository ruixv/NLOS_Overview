# 2026-09-17 update: MD-NLOS / iScience gap

## Verified missing paper

Peng Yang, Zewei Wang, Yinghui Guo, Xiaoying Li, Mingbo Pu, Hengshuo Guo, Mingfeng Xu, Fei Zhang, Yuanmao Wang, and Xiangang Luo, **“A model decomposition method for the real-time non-line-of-sight imaging,”** *iScience*, 29(6), 115828, 2026. DOI: 10.1016/j.isci.2026.115828.

Repository title/DOI searches before staging returned no match.

### Contribution
MD-NLOS reformulates the confocal transient inverse problem as a non-negative LASSO problem after decomposing the measurement operator into the known system/PSF and unknown hidden-scene albedo. A frequency-domain point-wise form makes gradient computation GPU-friendly; spectral filtering improves noise robustness. The paper reports 128x128 experimental reconstruction from 64 relay samples in 4.6 s, and sub-second reconstruction for 64x64 data, targeting the acquisition-quality-computation trade-off in real-time NLOS.

### Citation-tracing relevance
This is a high-confidence forward-lineage work rather than a paper that cites NLOS only in passing. Its method is explicitly LCT-based and its references include O'Toole et al. (Nature 2018 LCT), Liu et al. (Nature 2019 phasor-field virtual wave optics), Reza et al. (phasor-field waves), Lindell et al. acoustic NLOS, and subsequent sparse/undersampled NLOS methods.

## Integration locations

- **README.md / Latest Additions:** add as *iScience* 2026. Suggested summary: “MD-NLOS decomposes the LCT forward model and solves a GPU-friendly non-negative LASSO problem with spectral filtering, enabling sparse transient acquisition and fast optimization (128x128 experimental reconstruction from 64 samples in 4.6 s).”
- **README.md / Active NLOS / Reconstruction Algorithms:** place with LCT-derived optimization, undersampling, compressed/few-shot, and real-time reconstruction methods.
- **README.md / Milestone Timeline:** optional 2026 entry under practical real-time / sparse transient reconstruction; do not present as a field-defining milestone unless timeline granularity supports method-level entries.
- **index.html / Paper Explorer + Latest Additions:** category `Active / Transient / Optimization / Real-time`; keywords `LCT`, `model decomposition`, `LASSO`, `sparse sampling`, `GPU`, `spectral filtering`.
- **Survey LaTeX:** insert semantically after discussion of LCT/frequency-domain analytic inversion and sparse/under-scanned optimization, near DO-NLOS / compressed sensing / few-shot acquisition. Suggested literature-review sentence: “Recent work further restructures LCT-based inversion for sparse, real-time reconstruction: MD-NLOS decomposes the transient operator into system and scene terms and solves the resulting non-negative LASSO problem through GPU-friendly frequency-domain updates, narrowing the gap between iterative reconstruction quality and direct-method speed.”
- **Canonical bibliography:** merge `egbib_20260917_md_nlos_iscience.bib` after checking for duplicate DOI/title/citation key.
- **bare_jrnl.pdf:** rebuild only after source and bibliography integration; verify the new citation resolves and PDF is regenerated before claiming consistency.

## Consistency status
This file and the verified staging BibTeX are safe additions. README.md, index.html, the canonical survey source/bibliography, and bare_jrnl.pdf still require integration/rebuild; do not claim those artifacts contain this paper until those edits are verified.
