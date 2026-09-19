# 2026-09-19 update — Noise-adapted Neural Operator gap

## Verified missing paper

Lianfang Wang, Kuilin Qin, Xueying Liu, Huibin Chang, Yong Wang, and Yuping Duan, **“Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging,”** arXiv:2508.09655 (2025).

Current scholarly-index checks (arXiv and DBLP/CoRR) do not verify a final peer-reviewed venue, so this entry must remain labeled **arXiv 2025** until a final venue is independently verified.

### Why it belongs
The paper is directly about transient optical NLOS reconstruction. It introduces a noise-estimation module and a parameterized neural operator, built through deep algorithm unfolding, to adapt the inverse mapping to varying transient-noise levels. It also fuses global and local spatiotemporal features and evaluates simulated/real, fast-scanning, and sparse-illumination NLOS data. This is a useful milestone in the trajectory from task-specific CNN/Transformer reconstruction toward physics-structured operator learning and noise-conditioned inverse operators.

## Required canonical integration

- **README.md — Latest Additions:** add a concise entry under 2025 learned reconstruction / neural operators.
- **README.md — Deep Learning for NLOS:** place near physics-guided/unrolled reconstruction rather than generic image-to-image networks.
- **index.html / Paper Explorer:** add tags such as `active`, `transient`, `learned reconstruction`, `neural operator`, `noise-adaptive`, `algorithm unfolding`; include in the 2025 timeline only as a supporting development, not a field-defining milestone.
- **bare_jrnl.tex:** integrate semantically in the learned/physics-guided reconstruction discussion. Suggested literature-review sentence: “Recent work further recasts transient inversion as operator learning: Wang et al. condition a deeply unfolded neural operator on an estimated noise level, allowing a shared inverse model to adapt across noisy, fast-scanning, and sparsely sampled NLOS measurements.”
- **Canonical bibliography:** merge the verified entry staged in `egbib_20260919_noise_adapted_neural_operator.bib`, deduplicating by title and arXiv ID.
- **bare_jrnl.pdf:** rebuild only after the canonical LaTeX and bibliography are integrated successfully.

## Consistency / safety note
Repository-wide title and arXiv-ID searches returned no match before staging. Large canonical files were not overwritten from partial/truncated payloads in this run. The staging BibTeX and this note should be merged into the canonical artifacts in a later safe full-file update; until then, do not claim README/site/survey/PDF consistency.
