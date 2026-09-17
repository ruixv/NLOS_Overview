# MARMOT final-venue / missing-paper integration — 2026-09-17

Verified missing work: Siyuan Shen, Ziheng Wang, Xingyue Peng, Ruiqian Li, Qilin Sun, Shiying Li, and Jingyi Yu, “MARMOT: masked autoencoder for modeling transient imaging,” Visual Intelligence, vol. 4, article 22, 2026. DOI: 10.1007/s44267-026-00125-1. Final journal metadata supersedes the earlier arXiv:2506.08470 record. Publisher metadata lists the final seven-author set above.

Contribution: MARMOT introduces self-supervised masked transient pretraining for NLOS/transient imaging. A Transformer encoder-decoder learns from sparse, irregular, and non-uniform relay-wall samples by masking transient measurements and predicting missing transients. The resulting representation supports transient completion and NLOS reconstruction, while encoder features transfer to classification, albedo estimation, and depth estimation. The associated TransVerse corpus contains one million confocal NLOS transients rendered from 500,000 Objaverse objects. This is a useful milestone from task-specific supervised NLOS networks toward reusable pretrained transient representations / foundation-style priors.

Integration locations when large-file edits are safe:
- README.md: add to Latest Additions and learned/data-driven NLOS; venue must be Visual Intelligence 2026, not arXiv 2025.
- index.html / paper explorer: add under learned reconstruction / transient representation learning and the 2026 timeline; emphasize masked transient pretraining and sparse/irregular sampling.
- Survey LaTeX: integrate semantically in the data-driven / learned reconstruction discussion after transient-transformer methods and alongside sparse/irregular acquisition. Suggested trajectory sentence: “Recent work has begun to move beyond task-specific transient reconstruction toward reusable representation learning: MARMOT pretrains a masked Transformer on large-scale transient data, enabling completion of sparsely and irregularly sampled measurements and transfer to reconstruction and other downstream NLOS inference tasks.”
- Canonical bibliography: merge the verified BibTeX staged in `egbib_20260917_marmot_visual_intelligence.bib`; avoid retaining a duplicate arXiv-only entry if one exists elsewhere.
- Rebuild bare_jrnl.pdf after the canonical survey source and bibliography are updated, then verify README, website, survey source, bibliography, and PDF agree on the final venue.

This staging note is used instead of blindly overwriting large public-facing files from partial connector payloads.
