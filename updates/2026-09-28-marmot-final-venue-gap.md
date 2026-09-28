# MARMOT final-venue integration gap — 2026-09-28

## Verified missing paper

Siyuan Shen, Ziheng Wang, Xingyue Peng, Ruiqian Li, Qilin Sun, Shiying Li, and Jingyi Yu, **“MARMOT: masked autoencoder for modeling transient imaging,” Visual Intelligence, vol. 4, article 22, 2026.** DOI: 10.1007/s44267-026-00125-1. Originally released as arXiv:2506.08470.

Publisher metadata verifies the final journal version. The final author list differs from the 2025 arXiv version: Suan Xia is not in the final author list and Qilin Sun is included. Use the final journal metadata in all public-facing artifacts.

## Why it belongs in the survey

MARMOT introduces self-supervised masked pretraining for transient/NLOS measurements rather than training a dedicated inverse model for each task. A Transformer encoder-decoder reconstructs masked transient histograms under sparse, irregular, and non-uniform relay-wall sampling. Its TransVerse pretraining corpus contains one million confocal NLOS transients rendered from 500,000 Objaverse objects. The learned transient representation transfers to transient completion/NLOS reconstruction and downstream classification, albedo estimation, and depth estimation. This marks a trajectory from task-specific supervised NLOS networks toward reusable transient foundation/pretraining priors.

## Verified source

- Final publisher DOI: https://doi.org/10.1007/s44267-026-00125-1
- Final venue: Visual Intelligence 4, article 22 (2026)
- arXiv source: https://arxiv.org/abs/2506.08470

## Repository checks

Exact-title, DOI, `MARMOT`, `masked autoencoder`, and `TransVerse` searches on the repository default branch returned no match before this staging update.

## Required canonical integration

1. **README.md** — add MARMOT to Latest Additions and the 2026 learned/transient-imaging timeline. Categorize under Deep Learning for NLOS / learned transient representations. Suggested summary: “Self-supervised masked pretraining learns a reusable prior over transient measurements, supports sparse/irregular scan completion, and transfers to NLOS reconstruction, classification, albedo and depth tasks.”
2. **index.html / Paper Explorer** — add the same final journal metadata, DOI, arXiv link, tags `active`, `transient`, `deep-learning`, `self-supervised`, `masked-pretraining`, `sparse-sampling`, and place it in the 2026 latest/timeline view.
3. **bare_jrnl.tex** — integrate semantically in the learned-reconstruction section after transformer/transient-network discussion, not as an isolated appendix list. Recommended literature-review point: MARMOT shifts learned NLOS reconstruction from task-specific supervised inversion toward reusable self-supervised transient representations, using masked measurement modeling to accommodate arbitrary sparse scans and transfer across reconstruction and inference tasks.
4. **Bibliography** — merge the verified entry staged in `egbib_20260928_marmot_final_venue.bib` into the canonical bibliography used by `bare_jrnl.tex`; use the final journal author list and venue rather than the 2025 arXiv metadata.
5. **bare_jrnl.pdf** — rebuild only after the canonical LaTeX and bibliography have been safely integrated; verify the citation resolves and the final journal venue is rendered correctly.

## Consistency status

This run intentionally did not overwrite large canonical files from truncated connector payloads. The verified BibTeX and this insertion plan are committed safely. README/index/survey/PDF remain to be integrated and rebuilt from complete file contents in a future safe-edit pass; do not claim those artifacts are synchronized until verified.
