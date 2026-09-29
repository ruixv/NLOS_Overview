# Verified NLOS gaps — 2026-09-29

Two peer-reviewed 2026 papers were verified as relevant and absent from the default branch by exact-title and DOI searches.

## 1. Non-confocal frequency-domain phase compensation

Jing Ping Yu, Xiao Rui Tian, Jie Yang, Zhou Yang, Ming Ze Yang, Si Qi Zhang, Meng Tang, Chen Fei Jin, “Non-confocal non-line-of-sight imaging using frequency-domain phase compensation with the reference function,” *Optics Express*, 34(2):3232–3243, 2026. DOI: 10.1364/OE.580027.

**Contribution.** Transfers a single-input/multiple-output frequency-domain imaging formulation from millimeter-wave imaging to optical non-confocal NLOS. Reference-function phase compensation and FFT reconstruction target high-resolution recovery with fewer artifacts and lower computational cost. This is directly relevant to the survey's non-confocal, frequency-domain, and cross-modal RF/optical-method-transfer threads.

**Integration locations.**
- README: 2026 active/transient timeline; category active ToF / non-confocal / frequency-domain reconstruction.
- Website: Paper Explorer and 2026 latest additions/timeline.
- bare_jrnl.tex: frequency-domain analytic reconstruction discussion after LCT/f-k and alongside non-confocal acquisition; note the explicit transfer of a mmWave SISO/SIMO-style phase-compensation idea into optical NLOS.
- Canonical bibliography: merge the verified BibTeX entry from `egbib_20260929_frequency_sgatv_gap.bib`.

## 2. Structure-guided adaptive total variation for passive NLOS

Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, Guorong Sui, “Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging,” *Optics Express*, 34(3):5210–5224, 2026. DOI: 10.1364/OE.587111.

**Contribution.** Introduces a structure-guided adaptive total-variation framework for passive NLOS with a conventional color camera, addressing the dependence of conventional regularized inversion on fixed or manually tuned priors. It belongs to the passive computational-imaging trajectory between classical inverse reconstruction and recent learned/physics-aware passive methods.

**Integration locations.**
- README: 2026 passive NLOS timeline; category passive / optimization / conventional-camera imaging.
- Website: Paper Explorer and 2026 latest additions/timeline.
- bare_jrnl.tex: passive inverse-problem/regularization discussion, before or alongside learned passive reconstruction and diffuse-aware attention methods.
- Canonical bibliography: merge the verified BibTeX entry from `egbib_20260929_frequency_sgatv_gap.bib`.

## Build/consistency status

The two records above are staged and metadata-verified. Large canonical files were not overwritten from partial content. README.md, index.html, bare_jrnl.tex, the canonical bibliography, and bare_jrnl.pdf still require guarded integration and PDF rebuild before they can be claimed mutually consistent.
