# NLOS literature gap update — 2026-09-25

Two metadata-verified NLOS papers were found missing by repository-wide title/DOI searches. Canonical large files were not overwritten from partial payloads.

## 1. MARMOT: masked autoencoder for modeling transient imaging

**Final venue:** Visual Intelligence, 4, Article 22 (2026). DOI: 10.1007/s44267-026-00125-1.

**Contribution:** Self-supervised masked-autoencoder pretraining for confocal transient imaging. A Transformer encoder/decoder learns reusable transient priors from sparse, irregular, and non-uniform relay-wall samples. TransVerse provides one million synthetic confocal NLOS transients rendered from 500,000 Objaverse objects. Recovered measurements support transient completion and 3D reconstruction, while pretrained features transfer to classification, albedo estimation, and depth estimation. The paper explicitly builds on LCT, f-k, phasor-field and recent learned NLOS methods, making it a direct Core-paper descendant rather than an incidental NLOS citation.

**Recommended placement:** README 2026 learned/transient section; website Latest Additions + Paper Explorer + 2026 timeline; bare_jrnl.tex learned-reconstruction/sparse-acquisition discussion. Suggested trajectory sentence: "Recent work is beginning to shift learned NLOS reconstruction from task-specific supervision toward reusable transient representations: MARMOT uses masked self-supervised pretraining on large-scale synthetic transients to support sparse/irregular acquisition and multiple downstream NLOS tasks."

## 2. Non-line-of-sight imaging via physics-informed cascade learning

**Final venue:** Journal of the Optical Society of America A, 43(9), E9–E18 (2026). DOI: 10.1364/JOSAA.593401. Published 15 July 2026.

**Contribution:** Physics-informed cascade learning (PICL) couples a SPAD-specific noise-separation network with a reconstruction network containing a differentiable NLOS forward model. The design targets mixed SPAD dark-count/time-jitter noise and low-SNR inversion while avoiding reliance on large paired NLOS training datasets.

**Recommended placement:** README 2026 active/learned reconstruction section; website Latest Additions + Paper Explorer + timeline; bare_jrnl.tex physics-guided learned reconstruction / photon-starved-SPAD robustness discussion. Suggested trajectory sentence: "Physics-informed learning is also moving closer to the acquisition hardware: PICL explicitly separates SPAD noise before enforcing a differentiable transient forward model during reconstruction, improving low-SNR robustness without large paired datasets."

## Consistency work still required

Integrate both entries from `egbib_20260925_missing_nlos_batch3.bib` into the canonical bibliography; update README.md, index.html, and bare_jrnl.tex at the semantic locations above; then rebuild bare_jrnl.pdf and verify all public-facing artifacts contain the same final-venue metadata. Do not claim the PDF is updated until a successful LaTeX build and binary commit are verified.
