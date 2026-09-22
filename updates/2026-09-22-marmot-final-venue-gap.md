# MARMOT final-venue / integration gap — 2026-09-22

## Verified missing paper
Siyuan Shen, Ziheng Wang, Xingyue Peng, Suan Xia, Ruiqian Li, Shiying Li, Jingyi Yu, **“MARMOT: Masked Autoencoder for Modeling Transient Imaging,” Visual Intelligence, vol. 4, article 22, 2026.** DOI: 10.1007/s44267-026-00125-1. Originally arXiv:2506.08470.

Springer/SciOpen metadata verifies the final journal venue. Repository-wide searches for the full title and arXiv ID returned no matches before staging.

## Why it matters
MARMOT moves learned transient NLOS from task-specific supervised reconstruction toward large-scale self-supervised transient pretraining. A Transformer masked autoencoder predicts missing relay-wall transients from sparse/irregular measurements; the pretrained representation transfers to transient completion, 3D NLOS reconstruction, classification, albedo estimation, and depth estimation. TransVerse provides one million synthetic confocal NLOS transients rendered from 500,000 Objaverse objects. The work is directly connected to the LCT/f-k/phasor-field and learned-NLOS lineage through its reconstruction baselines and downstream evaluations.

## Canonical integration locations
- **README.md:** add under latest additions and learned/transient NLOS; venue must be `Visual Intelligence 2026`, not arXiv.
- **Development timeline:** add a 2026 milestone for `masked transient pretraining / self-supervised transient foundation priors`, linking the trajectory from task-specific NLOST/TransiT/ST-Mamba-style learned inversion to reusable transient representations.
- **index.html / Paper Explorer:** add metadata, DOI/arXiv link, tags such as `active`, `transient`, `learned`, `self-supervised`, `masked pretraining`, `sparse scanning`.
- **bare_jrnl.tex:** integrate semantically in the learned reconstruction / transient-transformer discussion. Suggested literature-review point: masked transient pretraining decouples representation learning from a single reconstruction objective by recovering heavily subsampled transient fields and transferring the learned encoder to multiple hidden-scene inference tasks.
- **canonical bibliography:** merge the verified entry staged in `egbib_20260922_marmot_visual_intelligence.bib`; deduplicate any older arXiv-only entry if later discovered.
- **bare_jrnl.pdf:** rebuild only after the canonical TeX/Bib changes are safely integrated; verify README, website, TeX, bibliography, and PDF consistency.

## Build status
This staging update does **not** claim that the canonical README/index/TeX/Bib or PDF have been rebuilt. Large canonical files should only be replaced from complete contents with current blob SHAs; do not overwrite them from truncated payloads.
