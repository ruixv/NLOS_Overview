# NLOS literature integration backlog — 2026-10-08

This note records four verified NLOS papers missing from the repository default branch as of 2026-10-08. It is intentionally a staging/integration note: canonical README/index/survey files were not overwritten from partial buffers.

## 1. Stereo Non-Line-of-Sight Imaging
Pablo Luesia-Lahoz, Sergio Cartiel, Adolfo Muñoz. *The Visual Computer* 42, 148 (2026). DOI: 10.1007/s00371-025-04340-7.
Contribution: two distinct relay walls combined through phasor fields reduce missing-cone visibility limitations and provide orientation cues.
Suggested placement: active ToF / phasor-field / visibility and missing-cone timeline.

## 2. Forward and inverse diffraction in phasor fields
Jorge Garcia-Pueyo, Adolfo Muñoz. *Optics Express* 33(5), 11420–11441 (2025). DOI: 10.1364/OE.553755.
Contribution: interprets phasor-field reconstruction as inverse diffraction using unitary propagation/dual-space arguments; analyzes well-posedness and proposes a matrix-rank quality metric related to Rayleigh resolution.
Suggested placement: phasor-field theory, immediately after foundational phasor-field/RSD discussion.

## 3. Adaptive Spiral Scanning for Confocal Non-Line-of-Sight Imaging
IEEE Open Journal of Signal Processing 7, 482–491 (2026). DOI: 10.1109/OJSP.2026.3688052.
Contribution: Dynamic Archimedean Spiral Confocal NLOS adaptively shifts the scan toward high-return regions; Voronoi density compensation corrects nonuniform sampling.
Suggested placement: acquisition efficiency / adaptive and sparse relay-wall sampling.

## 4. A model decomposition method for the real-time non-line-of-sight imaging
*iScience* (2026). DOI: 10.1016/j.isci.2026.115828.
Contribution: MD-NLOS reformulates sparse-transient reconstruction as non-negative LASSO with spectral filtering and GPU-parallelizable optimization; reported 128×128 recovery from 64 samples in 4.6 s.
Suggested placement: sparse/real-time model-based reconstruction.

## Canonical integration checklist
- Add concise entries to README.md with final venues above.
- Add records to index.html / Paper Explorer / latest additions / timeline.
- Integrate Stereo NLOS and inverse-phasor-fields into the phasor-field/visibility survey discussion; adaptive spiral scanning into efficient acquisition; MD-NLOS into sparse/real-time reconstruction.
- Add canonical BibTeX entries using publisher/DOI metadata.
- Rebuild bare_jrnl.pdf after source/bibliography integration.
- Verify README, website, bare_jrnl.tex, bibliography and PDF are mutually consistent.
