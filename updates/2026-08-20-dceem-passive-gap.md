# 20 August 2026 — DCEEM passive-NLOS gap

## Verified missing paper

Xuefeng Wang, Xingsu Chen, Miao Xu, Lan Wang, Gulnaz Alimjan, and Li Zhao, **“Enhancing passive non-line-of-sight imaging via dynamic channel optimization,”** *Optics Communications*, vol. 620, article 133626, 2026. DOI: `10.1016/j.optcom.2026.133626`.

Publisher source: https://doi.org/10.1016/j.optcom.2026.133626

Elsevier currently assigns the article to *Optics Communications* volume 620 (December 2026), article 133626. Because a final DOI, journal, volume, and article number are already publisher-verified, use the journal venue rather than an arXiv label.

### Why it belongs

This is directly a passive NLOS reconstruction paper, not a generic low-light or inverse-imaging paper. It proposes a **Dynamic Channel Enhancement Encoding Mechanism (DCEEM)** for conventional-camera PNLOS. DCEEM combines feature statistics with light-transport physical descriptors through Bayesian multiplicative fusion to generate adaptive channel weights, suppresses noise-dominated channels under low SNR, and uses a hierarchical low-dimensional denoising → high-dimensional refinement → vector-quantization optimization pipeline. The paper evaluates the method on real-world passive-NLOS datasets and positions it after NLOS-OT, ParaEncodeNet, NLOS-LTM, Transformer-based passive reconstruction, and Hyper-NLOS.

The useful development-line interpretation is:

> passive learned inversion → latent/light-transport-aware encoding → hyperspectral/contextual conditioning → **physics-aware dynamic channel gating under low SNR**.

## Current repository audit

As checked on 20 August 2026, the exact title / DOI / article number is absent from:

- `README.md`
- the V2 canonical corpus `data/papers-source.html`
- `article/3passive.tex`
- `egbib_merged_20260711.bib`

Do not maintain a duplicate paper array in `index.html`; the V2 Paper Explorer and timeline use `data/papers-source.html` as the canonical corpus.

## Safe integration locations

### 1. `README.md`

In **Latest Additions**, insert immediately after the table header (before the current NLOS-MT row):

```markdown
| 2026 | [Enhancing passive non-line-of-sight imaging via dynamic channel optimization](https://doi.org/10.1016/j.optcom.2026.133626) — Wang et al. | Optics Communications 620, 133626 (2026) | Introduces DCEEM for low-SNR passive NLOS: Bayesian multiplicative fusion combines feature statistics with light-transport descriptors to adaptively suppress noise-dominated channels, while hierarchical denoising/refinement and vector-quantization optimization strengthen hidden-scene reconstruction. |
```

Also add a short 2026 milestone sentence placing DCEEM after NLOS-LTM / ParaEncodeNet / Hyper-NLOS as a physics-aware channel-selection step for low-SNR passive reconstruction.

### 2. `data/papers-source.html`

Add this object near the top of `const papers=[` with the other latest learned/passive entries:

```javascript
{cat:"latest passive learning physics-guided low-snr light-transport vector-quantization channel-attention reconstruction",title:"Enhancing passive non-line-of-sight imaging via dynamic channel optimization",authors:"Wang et al.",year:2026,venue:"Optics Communications 620, 133626 (2026)",url:"https://doi.org/10.1016/j.optcom.2026.133626",key:"Introduces DCEEM for low-SNR passive NLOS: Bayesian multiplicative fusion combines feature statistics with light-transport physical descriptors to adaptively suppress noise-dominated channels, followed by hierarchical denoising/refinement and vector-quantization optimization."},
```

In the 2026 timeline paragraph, add a concise sentence such as:

> Wang et al. made passive feature selection explicitly light-transport-aware with DCEEM, using Bayesian dynamic channel weighting and hierarchical denoising/refinement to suppress low-SNR channel aliasing before vector quantization.

Increment the displayed tracked-paper count exactly once.

### 3. `article/3passive.tex`

Insert in the learned passive-reconstruction discussion after the NLOS-OT / parallel-encoder / light-transport-aware / hyperspectral learned-reconstruction lineage rather than appending a disconnected final list. Suggested prose:

```latex
More recently, Wang et al.~\cite{wangDynamicChannelPNLOS2026} targeted the channel-aliasing failure mode of low-SNR passive NLOS reconstruction with a dynamic channel enhancement encoding mechanism (DCEEM). Rather than deriving channel attention only from latent feature statistics, DCEEM combines those statistics with light-transport descriptors through Bayesian multiplicative fusion, then follows the signal-to-noise evolution of the encoder with low-dimensional denoising, high-dimensional refinement, and vector-quantization optimization. This direction moves learned passive inversion from increasingly expressive backbones toward explicit physics-aware selection of which latent channels should be trusted under weak indirect illumination.
```

### 4. Bibliography

Merge the single canonical entry from `egbib_20260820_dceem_passive_gap.bib` into `egbib_merged_20260711.bib`, preserving key `wangDynamicChannelPNLOS2026`. Before merging, assert uniqueness of both the key and DOI `10.1016/j.optcom.2026.133626`.

### 5. `bare_jrnl.tex` and PDF

Update the survey provenance/date only when the public artifacts are integrated. Then perform a clean build using the repository's normal LaTeX/BibTeX sequence (typically `pdflatex → bibtex → pdflatex → pdflatex`). Verify:

- `wangDynamicChannelPNLOS2026` occurs in the `.aux` and resolves in the `.bbl`;
- README and V2 corpus each contain the paper exactly once;
- the survey text contains the DCEEM literature-review sentence in the passive section;
- the DOI appears exactly once as a canonical bibliography record;
- regenerated `bare_jrnl.pdf` contains searchable semantic tokens such as `dynamic channel`, `Bayesian`, and `light-transport` after normalizing hyphenation/whitespace;
- first and last PDF pages render successfully.

Do **not** claim `bare_jrnl.pdf` is updated until this clean build and cross-artifact validation pass.

## Interaction with pending passive-lineage integration

PR #135 is still open for the separately verified Hyper-NLOS 2024 and *Turning rough surfaces into non-line-of-sight cameras* 2025 gaps. Avoid independently overwriting the same large passive-survey / corpus files while that guarded integration is unresolved. This note and the staging BibTeX intentionally keep the newly verified DCEEM record losslessly ready for the next safe synchronized public-content build.

## Integration status

Integrated by the guarded 21 August 2026 workflow after the Hyper-NLOS / rough-surface passive milestone update had landed on `master`. The workflow synchronizes README, the canonical V2 corpus/timeline, passive-survey prose, merged bibliography, and the rebuilt survey PDF, and validates citation resolution and rendered PDF endpoints before committing.
