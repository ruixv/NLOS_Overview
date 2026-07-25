# 26 July 2026 citation-tracing update

## Scope

This batch follows the forward-citation and related-work chains around Velten 2012, LCT, f-k migration, phasor fields, computational periscopy, NLOST, and recent passive spectral/speckle methods. Candidates were retained only when the publisher abstract and method description established direct hidden-scene reconstruction or tightly coupled passive-NLOS signal separation.

## Verified missing records

1. **Speckle-correlation-based non-line-of-sight imaging under white-light illumination** — Meiling Zhou, Yang Zhang, Ping Wang, Runze Li, Tong Peng, Junwei Min, Shaohui Yan, Baoli Yao. *Optics & Laser Technology* 170, 110231 (2024). DOI: `10.1016/j.optlastec.2023.110231`.
   - Zernike-polynomial envelope correction and low-pass filtering improve white-light speckle autocorrelation under ambient illumination and detector misalignment.
   - The reference list explicitly contains Velten 2012, LCT, and phasor-field virtual wave optics.

2. **Non-line-of-sight imaging under white-light illumination using physics-enhanced deep learning** — Zhenfeng Fu, Fei Wang, Shanshan Zheng, Guohai Situ. *Applied Optics* 64(16), 4607–4614 (2025). DOI: `10.1364/AO.561658`.
   - Embeds the speckle-correlation model and a denoising prior in a trainable ordinary-camera reconstruction pipeline.
   - Final Optica venue and publication date (23 May 2025) replace any preprint-only status.

3. **Single-shot non-line-of-sight imaging based on the statistical average characteristics of a speckle pattern under ambient light** — Junjie Zhou, Liang Yin, Minglong Hu, Shilin Ren, Yingchun Ding. *Optics Communications* 586, 131847 (2025). DOI: `10.1016/j.optcom.2025.131847`.
   - Uses covariance of one random speckle pattern to recover object-spectrum amplitude beyond the conventional memory-effect field of view and at −2.06 dB SNR.
   - Its references include Velten, LCT, and phasor-field milestones, confirming direct NLOS relevance.

4. **Isolating Signals in Passive Non-Line-of-Sight Imaging Using Spectral Content** — Connor Hashemi, Rafael Avelar, James Leger. *IEEE TPAMI* 47(9), 7328–7339 (2025). DOI: `10.1109/TPAMI.2023.3301336`.
   - Multispectral unmixing and a convex known-spectrum solver separate desired wall-mediated radiance from clutter up to 50 times stronger.
   - The final 2025 volume/issue/pages are used rather than the 2023 early-access year.

5. **Hyperspectral passive non-line-of-sight imaging with band selection** — Mingyang Chen, Shaohui Jin, Mengge Liu, Ziqin Xu, Hao Liu, Mingliang Xu. *Expert Systems with Applications* 290, 128394 (2025). DOI: `10.1016/j.eswa.2025.128394`.
   - HSBS-Net combines differentiable band selection, a spectral-energy-guided KA-Transformer, robust sparse loss, and the HP-NLOS physical hyperspectral dataset.

6. **CMFormer: Non-line-of-sight imaging with a memory-efficient MetaFormer network** — Shihao Zhang, Shaohui Jin, Hao Liu, Yue Li, Xiaoheng Jiang, Mingliang Xu. *Optics and Lasers in Engineering* 187, 108875 (2025). DOI: `10.1016/j.optlaseng.2025.108875`.
   - Directly extends the NLOST learned-transient lineage with a convolutional MetaFormer, aggregate feature transmission, cross-layer attention, checkpointing, and 8-fps consumer-GPU reconstruction.

## Integration map

- `README.md`: add six DOI-linked rows and 2024/2025 development milestones.
- `index.html`: add six searchable records, update the tracked-entry total by the actual number of newly inserted records, extend the timeline, and repair missing commas between adjacent paper objects if encountered.
- `article/3passive.tex`: add the white-light/single-shot speckle trajectory; replace the stale hyperspectral paragraph, including its incorrect HoloRadar citation, with clutter-aware multispectral and band-selection coverage; extend the passive-method table.
- `article/4datadriven.tex`: add CMFormer in the learned transient trajectory and the physics-enhanced white-light method in the physics–data hybrid discussion.
- `egbib_merged_20260711.bib`: append six DOI-verified records under stable new citation keys, failing closed if a DOI already exists under a different key.
- `bare_jrnl.tex`: add a trace marker without changing the survey structure.
- `bare_jrnl.pdf`: rebuild only after all source and bibliography checks pass.

## Validation requirements

The guarded synchronizer requires exactly one title in README and the website explorer, exactly one DOI and the expected key in the bibliography, and citations in the appropriate survey section. The build workflow additionally checks HTML/JavaScript syntax, unresolved LaTeX citations, duplicate bibliography warnings, PDF metadata/text extraction, and rendered first/last pages before committing the regenerated PDF.

The newest independently date-verified direct NLOS publication remains **Iterating the transient light transport matrix for non-line-of-sight imaging**, published online by *Nature Communications* on 22 July 2026. This batch fills older coverage gaps rather than claiming a later publication.
