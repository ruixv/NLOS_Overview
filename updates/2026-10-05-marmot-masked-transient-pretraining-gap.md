# Integration note — MARMOT masked transient pretraining gap (2026-10-05)

## Verified missing paper

Siyuan Shen, Ziheng Wang, Xingyue Peng, Ruiqian Li, Qilin Sun, Shiying Li, and Jingyi Yu, **“MARMOT: masked autoencoder for modeling transient imaging,” Visual Intelligence, vol. 4, article 22, 2026.** DOI: 10.1007/s44267-026-00125-1. Published 18 August 2026.

Publisher: https://link.springer.com/article/10.1007/s44267-026-00125-1
Preprint: https://arxiv.org/abs/2506.08470

The publisher version is authoritative. Note that the final author list differs from the original 2025 arXiv version: the version of record lists Qilin Sun and does not list Suan Xia as an author; the publisher acknowledgements thank Suan Xia for data-acquisition support.

## Why it belongs in NLOS_Overview

MARMOT is directly about confocal transient NLOS imaging rather than a generic masked-autoencoder paper. It introduces self-supervised pretraining over transient measurements: a Transformer encoder receives sparse/irregular relay-wall histograms and a lightweight decoder predicts the missing dense transient volume. The pretrained representation is reused for transient completion, NLOS 3D reconstruction, classification, albedo estimation, and depth estimation. It also introduces TransVerse, reported in the final paper as one million confocal NLOS transients rendered from 500,000 Objaverse objects.

This marks a useful trajectory shift from task-specific supervised NLOS networks toward reusable transient foundation/pretraining priors. The paper explicitly situates itself relative to LCT, f-k, phasor-field methods, NLOST, AGK, LPP, neural fields, sparse scanning, and Virtual Scanning, making it tightly connected to the survey's Core/milestone literature.

## Repository check

A default-branch GitHub code search for `MARMOT` returned no matches before this staging commit, so the paper is missing from the current public repository artifacts rather than merely missing from one section.

## Recommended canonical integration

### README / development timeline

Place under 2026 learning-based active/transient NLOS, near sparse/undersampled transient reconstruction and Transformer-based reconstruction entries.

Suggested concise entry:

> **MARMOT: masked autoencoder for modeling transient imaging** — Shen et al., *Visual Intelligence* 2026. Introduces large-scale self-supervised masked pretraining for NLOS transients; reconstructs dense measurements from sparse or irregular scans and transfers the learned transient representation to 3D reconstruction, depth, albedo, and classification. TransVerse contains one million confocal transients rendered from 500,000 Objaverse objects.

### Website / Paper Explorer

Category: `Active / Transient` + `Learning-based` + `Sparse sampling / pretraining`.

Trajectory wording: `task-specific reconstruction → transient Transformers → sparse/irregular acquisition → masked transient pretraining and reusable representations`.

### Survey source

Insert semantically in the learning-based active-NLOS section, after discussion of transient Transformers / sparse-scan learning and before or alongside emerging generalizable priors.

Suggested literature-review sentence:

> Moving beyond task-specific supervised reconstruction, MARMOT introduces self-supervised masked pretraining directly in transient space, learning a reusable representation from large-scale synthetic measurements that supports sparse and irregular acquisition as well as downstream reconstruction, depth, albedo, and recognition tasks.

This is also a natural place to discuss the field's move from individual reconstruction architectures toward pretrained transient representations and large synthetic transient corpora.

### Bibliography

Merge `egbib_20261005_marmot_gap.bib` into the canonical bibliography. Preserve the final publisher author list rather than copying the older arXiv author list.

## Build / consistency status

This run intentionally stages the verified citation and precise integration instructions instead of replacing large canonical files from partial connector buffers. README.md, index.html, bare_jrnl.tex (or modular article source), canonical bibliography, and bare_jrnl.pdf still require a full safe read-edit-build-validation cycle. Do not claim the PDF has been regenerated until compilation and the resulting binary commit are verified.
