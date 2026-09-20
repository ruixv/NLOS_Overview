# Integration note — Passive NLOS with diffuse-aware attention (Optics Express 2026)

Verified missing paper (repository-wide title and DOI searches returned no matches before staging):

- Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, and Li Zhao, “Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,” *Optics Express*, 34(14), 26271–26289, 2026. DOI: 10.1364/OE.601398.

## Why it belongs

This is a genuine passive NLOS reconstruction paper rather than a generic attention model. It targets the weak, spatially mixed indirect-light signal measured by an ordinary passive imaging setup. Its diffuse-aware attention module (DAAM) encodes two NLOS-specific priors: anisotropic angular structure of diffuse reflections through deformable spatial attention, and channel-dependent SNR through mean/std-based channel attention. A learnable gate combines them inside a residual-attention encoder. The paper is useful in the trajectory from generic learned passive reconstruction toward architectures whose attention mechanisms explicitly reflect diffuse transport and weak-signal statistics.

## Canonical integration locations

1. **README.md** — add under Passive NLOS / learned passive reconstruction, with venue `Optics Express 2026`, DOI link, and a concise summary emphasizing diffuse-transport-aware spatial attention plus SNR-aware channel attention.
2. **Development timeline** — add a 2026 entry after the earlier passive learned-reconstruction / PAC-Net lineage, but do not mark it as a field-defining Core milestone.
3. **index.html / Paper Explorer / Latest Additions** — add as `Passive`, `Learned reconstruction`, `Physics-aware attention`, `2026`.
4. **bare_jrnl.tex** — integrate semantically into the passive-NLOS learned-reconstruction discussion. Suggested literature-review sentence: “Recent passive methods have begun to embed diffuse-transport priors directly into learned architectures; Wang et al. introduce diffuse-aware attention that combines deformable spatial attention for anisotropic indirect-light structure with channel attention conditioned on SNR statistics.” Preserve the survey’s existing citation/style conventions.
5. **Canonical bibliography** — merge the verified entry staged in `egbib_20260920_daam_passive_nlos.bib`, adapting only the BibTeX key if needed to match repository convention.
6. **bare_jrnl.pdf** — rebuild only after the canonical TeX/BibTeX integration succeeds; do not treat this note as evidence that the PDF was regenerated.

## Verification status

Final venue was verified as *Optics Express* 34(14), 26271–26289 (2026), DOI 10.1364/OE.601398. Do not label this as arXiv. Public-facing canonical artifacts were not overwritten in this staging step because a safe complete-file edit/build path was not established in this run.
