# 2026-09-11 — Diffuse-aware passive NLOS consistency update

## Verified paper

Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, and Li Zhao, “Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,” *Optics Express*, vol. 34, no. 14, pp. 26271–26289, 2026. DOI: 10.1364/OE.601398.

Publisher-indexed metadata confirms the final journal venue and pagination. The method introduces a diffuse-aware attention module (DAAM) for passive NLOS reconstruction. DAAM encodes two physically motivated priors: anisotropic spatial structure of diffuse reflection through deformable convolution, and channel-wise signal reliability through mean/std pooling, with learnable gated fusion. It is embedded in a residual-attention encoder and evaluated on the NLOS-OT dataset.

## Why this update is needed

The paper is already discussed in `article/3passive.tex` under “Diffuse-aware attention encoding for passive NLOS” and cited there as `wangDiffuseAwarePassive2026`, so it is not a newly discovered paper for the survey narrative. However, direct inspection found a cross-artifact consistency gap: the paper was not surfaced by the current README / GitHub code-search snapshot, and its verified BibTeX was not visible in the beginning of the canonical merged bibliography. A verified standalone BibTeX staging file has therefore been added as `egbib_20260911_diffuse_aware_passive.bib`.

## Required integration locations

1. **README.md — Latest Additions / Passive NLOS**
   Add a concise entry near other 2026 passive learned-reconstruction papers:
   - Venue: *Optics Express* 34(14), 26271–26289 (2026)
   - DOI: https://doi.org/10.1364/OE.601398
   - Summary: physics-aware DAAM uses deformable spatial attention plus mean/std channel statistics to preserve weak diffuse-wall signals in passive NLOS reconstruction.

2. **index.html — Paper Explorer / latest additions / passive-learning timeline**
   Add the same paper with family `passive` or `learning`, year 2026, final Optics Express venue, DOI link, and a short summary emphasizing physically informed attention for diffuse transport.

3. **article/3passive.tex**
   The survey prose is already present and should be retained. No duplicate paragraph should be added. Verify the citation key remains `wangDiffuseAwarePassive2026`.

4. **egbib_merged_20260711.bib**
   Merge the verified entry from `egbib_20260911_diffuse_aware_passive.bib` if the key is not already present. If an older/preprint duplicate exists, keep only the final Optics Express record.

5. **bare_jrnl.tex / bare_jrnl.pdf**
   `bare_jrnl.tex` includes the modular survey sections, so no duplicate prose is required. After canonical bibliography integration, compile and verify that `wangDiffuseAwarePassive2026` resolves and regenerate `bare_jrnl.pdf`.

## Citation-tracing note

This paper also appeared in a forward-citation neighborhood of the 2025 passive NLOS work “Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging,” making it a useful citation-tracing confirmation rather than a keyword-only hit. This reinforces the passive-learning trajectory from generic encoder–decoder models to attention mechanisms explicitly shaped by diffuse light-transport statistics.

## Status

- Verified standalone BibTeX staging: added.
- Survey narrative in `article/3passive.tex`: already present.
- README / website / canonical merged bibliography / rebuilt PDF: still require coordinated integration from complete file contents; do not overwrite those large files from truncated reads.
