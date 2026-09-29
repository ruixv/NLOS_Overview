# Integration gap: diffuse-aware passive NLOS imaging

## Verified missing paper

Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, Li Zhao, “Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,” *Optics Express*, 34(14), 26271–26289, 2026. DOI: 10.1364/OE.601398.

This title and DOI were searched against the repository default branch before staging and returned no match.

## Contribution and placement

The paper targets passive NLOS reconstruction under ambient illumination, where weak indirect signals and diffuse transport make deep feature extraction difficult. It introduces a diffuse-aware attention module (DAAM) that embeds two physical priors: anisotropic angular structure of diffuse reflections and channel-wise SNR disparity. Deformable convolution provides spatial attention, mean/std pooling provides channel attention, and a learnable gate fuses them in a residual-attention encoder.

Recommended trajectory placement: passive computational periscopy / learned passive NLOS -> physics-aware passive encoders -> diffuse-aware attention for weak-signal reconstruction.

## Required canonical integration

- README.md: add under 2026 passive/learned NLOS timeline and Paper Explorer with the final Optics Express venue and DOI.
- index.html: add to latest additions and passive/learned reconstruction filters/timeline.
- bare_jrnl.tex: integrate semantically in the passive NLOS / learned reconstruction discussion, contrasting generic learned attention with explicit diffuse-transport and SNR priors rather than appending an isolated list item.
- Canonical bibliography: merge the verified BibTeX staged in `egbib_20260929_diffuse_aware_passive_nlos.bib` into the bibliography actually used by bare_jrnl.tex.
- bare_jrnl.pdf: rebuild after source/bibliography integration and verify the citation resolves.

The large canonical files were not overwritten from partial/truncated content in this run. This note records the exact remaining integration work rather than claiming those artifacts were updated.
