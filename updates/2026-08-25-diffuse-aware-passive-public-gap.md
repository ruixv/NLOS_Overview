# 25 August 2026 — diffuse-aware passive-NLOS public-artifact gap

## Verified paper

Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, and Li Zhao, **“Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,”** *Optics Express*, vol. 34, no. 14, pp. 26271–26289, 2026. DOI: **10.1364/OE.601398**.

Publisher metadata is final (Optics Express 34(14), 26271–26289; published 8 July 2026 / issue dated 13 July 2026). The method introduces a diffuse-aware attention module (DAAM) for ordinary-camera passive NLOS. DAAM uses two physically motivated priors: anisotropic spatial structure of diffuse relay transport and channel-wise SNR disparity. The implementation uses deformable convolution for anisotropic spatial attention, mean/std pooling for channel attention, a learnable gate for fusion, and a residual-attention encoder. Experiments are reported on NLOS-OT.

## Repository audit

This is **not** a missing survey/bibliography paper. It is already integrated in:

- `article/3passive.tex` under **“Diffuse-aware attention encoding for passive NLOS”**, cited as `wangDiffuseAwarePassive2026`.
- `egbib_merged_20260711.bib` as `wangDiffuseAwarePassive2026`, with DOI `10.1364/OE.601398`.
- the deployed `bare_jrnl.pdf`, where the passive-method narrative and bibliography entry are present.

The current public-discovery gap is:

- `README.md`: title/DOI absent from Latest Additions and development timeline.
- `data/papers-source.html`: title/DOI absent from the canonical V2 Paper Explorer / graph corpus and 2026 timeline.

Therefore the safe update is to add the paper to README + V2 corpus/timeline **without** creating a second BibTeX entry or duplicating survey prose.

## Precise README insertion

Under `## Latest Additions`, add:

```markdown
| 2026 | [Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding](https://doi.org/10.1364/OE.601398) — Wang et al. | Optics Express 34(14), 26271–26289 (2026) | Introduces DAAM, a physics-motivated residual-attention encoder for ordinary-camera passive NLOS that combines deformable-convolution spatial attention with mean/std channel-SNR attention to preserve weak diffuse-transport features under low SNR. |
```

In the 2026 milestone/development timeline, add a concise phrase such as:

> Diffuse-aware attention brought explicit relay-transport anisotropy and channel-wise SNR priors into passive RGB reconstruction, complementing light-transport-aware channel selection, hyperspectral conditioning, diffusion models, and rough-relay physical encoding.

After public integration, update the README run date to **25 August 2026**.

## Precise V2 corpus insertion

In `data/papers-source.html`, add one canonical paper object in the passive / learning family with:

- title: `Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding`
- authors: `Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, Li Zhao`
- year: `2026`
- venue: `Optics Express 34(14), 26271–26289`
- url: `https://doi.org/10.1364/OE.601398`
- key / citation id: `wangDiffuseAwarePassive2026`
- contribution summary: `Physics-motivated DAAM combines anisotropic spatial attention and channel-wise SNR attention to preserve weak diffuse-transport features in passive NLOS reconstruction.`

Add a 2026 timeline sentence matching the README wording, recompute the tracked-entry count from the canonical corpus rather than hard-coding it, and update the public-page update date to **25 August 2026**.

## Survey / bibliography / PDF handling

Do **not** add a duplicate bibliography record. Reuse the existing `wangDiffuseAwarePassive2026` entry.

Do **not** append a second literature-review paragraph: `article/3passive.tex` already contains the appropriate narrative.

The currently deployed PDF already contains the DAAM paragraph and the bibliography entry. A PDF rebuild is therefore not semantically required for this specific gap; if `bare_jrnl.tex` or any survey source date is changed during the public synchronization, rebuild with:

```bash
pdflatex -interaction=nonstopmode bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode bare_jrnl.tex
pdflatex -interaction=nonstopmode bare_jrnl.tex
```

Then verify:

1. `wangDiffuseAwarePassive2026` resolves in `.aux/.bbl` exactly once.
2. DOI `10.1364/OE.601398` occurs exactly once in the merged bibliography.
3. README and V2 corpus each contain exactly one paper entry.
4. PDF text contains the diffuse-aware-attention narrative and final Optics Express citation.
5. No duplicate `wangDiffuseAwarePassive2026` BibTeX key is introduced.

## Why this was not written directly into the large public files in this run

The available repository write action replaces an entire UTF-8 file. `README.md` and especially `data/papers-source.html` are large and the fetch response is truncated in this environment, so whole-file replacement would risk silent truncation/data loss. Following the repository-update safety rule, this note records exact insertion locations and content instead of blindly overwriting those files.
