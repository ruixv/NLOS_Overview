# 2026-09-21 gap: structure-guided adaptive TV for passive NLOS

Verified missing paper:

- Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, and Guorong Sui, "Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging," *Optics Express*, 34(3):5210–5224, 2026. DOI: 10.1364/OE.587111.

## Why it belongs

This is a genuine passive NLOS reconstruction paper using a conventional color camera and an experimentally measured optical transport matrix. SG-ATV derives spatially varying TV weights from a fast preliminary reconstruction and updates them during optimization, reducing manual regularization tuning while balancing structural preservation, noise suppression, and cross-channel color consistency. It is best categorized under passive optical NLOS / optimization-driven reconstruction / adaptive priors rather than learned reconstruction.

The paper directly cites milestone NLOS works including Saunders et al. computational periscopy, O'Toole et al. LCT, Liu et al. phasor-field NLOS, and Velten et al. 2012, so it is also a verified forward-lineage result from multiple Core seeds.

## Integration plan

- README.md: add to passive optical NLOS / optimization-based reconstruction, with a concise note emphasizing parameter-free structure-guided adaptive TV.
- index.html / Paper Explorer: add Optics Express 2026 metadata and tags `passive`, `optimization`, `adaptive-prior`, `color-camera`; place in the 2026 timeline without marking it as a field-defining milestone.
- bare_jrnl.tex: integrate into the passive computational-periscopy / inverse-problem discussion, contrasting fixed/manual regularization with scene-adaptive variational priors. A suitable literature-review transition is: "Recent work has also revisited interpretable variational reconstruction: SG-ATV derives spatially varying regularization weights from a preliminary hidden-scene estimate, reducing manual parameter tuning while preserving structure and color consistency in passive NLOS."
- Bibliography: merge the verified entry staged in `egbib_20260921_sg_atv_passive_nlos.bib` into the canonical bibliography used by bare_jrnl.tex.
- PDF: rebuild bare_jrnl.pdf only after the canonical LaTeX and bibliography edits are safely applied and validated.

## Verification

Repository-wide searches for the complete title and DOI `10.1364/OE.587111` returned no matches before this staging update. Metadata was verified against the final Optics Express/PubMed record. Do not label this paper as arXiv.

Canonical README/index/LaTeX files were not overwritten in this run because safe full-file mutation/build validation was not available; this note records exact semantic insertion points rather than risking truncation.
