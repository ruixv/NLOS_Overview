# 2026-09-16 — Diffuse-aware passive NLOS integration gap

## Verified missing paper

Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, and Li Zhao, “Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,” *Optics Express*, vol. 34, no. 14, pp. 26271–26289, 2026. DOI: 10.1364/OE.601398.

Published 13 July 2026 (publisher record; accepted 26 June 2026). This is a final journal publication, not an arXiv-only entry.

## Why it belongs

The paper addresses passive RGB NLOS reconstruction under weak diffuse signals. Its diffuse-aware attention module (DAAM) encodes two physics-motivated priors: anisotropic spatial scattering through deformable convolution and channel-wise SNR disparity through mean/std pooling, with gated fusion inside a residual encoder. It therefore extends the passive learned-reconstruction trajectory from generic encoder/attention architectures toward physically informed feature attention.

## Recommended integration

- **README.md / Latest Additions:** add as a 2026 Optics Express entry; summarize as physics-informed diffuse-aware attention for passive RGB NLOS.
- **README.md / Passive NLOS + Deep Learning:** place near recent passive learned reconstruction / hyperspectral / event-camera methods.
- **Website / Paper Explorer / timeline:** category `Passive NLOS` + `Deep Learning`; development cue: generic learned passive reconstruction → physically informed attention for weak diffuse signals.
- **Survey LaTeX:** integrate semantically in the passive learned-reconstruction discussion (rather than appending only to a list). Suggested sentence: “Recent passive reconstruction work further embeds scattering priors into learned feature extraction: Wang et al. introduce diffuse-aware spatial and channel attention that adapts to anisotropic relay-wall scattering and channel-wise SNR variation, improving preservation of weak indirect signals.”
- **Bibliography:** merge `egbib_20260916_daam_passive_nlos.bib` into the canonical bibliography used by the survey.
- **PDF:** rebuild `bare_jrnl.pdf` after the canonical bibliography and survey source are updated.

## Consistency status

At this run, direct GitHub code search found no title or DOI occurrence in the repository. Large public-facing files were not overwritten from partial/truncated payloads. The verified BibTeX staging file and this exact integration note are committed so a later full-file/patch-capable run can safely synchronize README, website, survey source, canonical bibliography, and PDF.
