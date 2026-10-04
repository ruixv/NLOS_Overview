# Integration note: SG-ATV passive NLOS gap (2026-10-04)

## Verified missing paper

Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, and Guorong Sui, “Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging,” *Optics Express*, 34(3), 5210–5224 (2026). DOI: 10.1364/OE.587111.

Repository-wide searches by full title and DOI returned no match on the default branch before staging this note/BibTeX entry.

## Why it belongs

This is a genuine passive NLOS reconstruction paper using a conventional color camera and the Saunders-style linear light-transport formulation, not a generic inverse-imaging paper that merely cites NLOS work. SG-ATV derives a guidance map from a preliminary reconstruction and converts local structural cues into spatially varying TV weights. The method is designed to reduce scene-dependent manual regularization tuning while preserving edges and suppressing homogeneous-region noise. The paper reports roughly 30× reconstruction-efficiency improvement over its fixed-TV baseline and substantially improved stability across parameter settings/scenes.

## Citation-tracing relevance

The paper explicitly states that its passive forward model follows the computational-periscopy/Saunders framework. It is therefore a direct forward-citation descendant of a Core passive-NLOS milestone rather than a keyword-only match.

## Recommended canonical integration

- **README timeline / latest additions:** add under 2026 passive/computational NLOS, after model-based light-transport/regularized reconstruction work and alongside recent physics-informed passive reconstruction.
- **Paper explorer / index.html:** category `Passive NLOS` / `Optimization & physical priors`; contribution summary: “Introduces structure-guided adaptive total variation for ordinary-camera passive NLOS, deriving spatially varying regularization from a preliminary reconstruction to reduce manual parameter tuning while preserving edges and suppressing noise.”
- **Survey source:** place in the passive-NLOS reconstruction section after the Saunders/computational-periscopy linear transport model and subsequent regularized inverse methods, before or alongside learned passive reconstruction. Suggested transition: “Recent work also revisits model-based passive reconstruction rather than replacing the transport model with a neural network. Zhang et al. derive spatially adaptive total-variation weights from an initial hidden-scene estimate, reducing sensitivity to globally tuned regularization while retaining the interpretability of the linear light-transport formulation.”
- **Bibliography:** merge `egbib_20261004_sg_atv_passive_gap.bib` into the canonical bibliography, preserving the repository’s BibTeX key/style conventions.

## Build/consistency status

The canonical README/index/survey/bibliography/PDF were not overwritten in this run because a complete safe read-edit-build-validation buffer for all large public-facing files was not available. This staging note and verified BibTeX entry are intentionally small recovery artifacts. A later integration pass should update README.md, index.html, the appropriate passive-NLOS LaTeX section (and bare_jrnl.tex if it is the canonical aggregate), the canonical bibliography, then rebuild bare_jrnl.pdf and verify that all public-facing artifacts contain the same venue/year/DOI and contribution summary.
