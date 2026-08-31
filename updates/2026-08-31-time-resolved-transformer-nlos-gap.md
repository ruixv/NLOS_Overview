# Time-Resolved Transformer NLOS integration note — 2026-08-31

## Verified missing paper

Yue Li, Shida Sun, Yu Hong, Feihu Xu, and Zhiwei Xiong, **“3D Reconstruction from Transient Measurements with Time-Resolved Transformer,”** arXiv:2510.09205 (2025), DOI: 10.48550/arXiv.2510.09205.

As of 2026-08-31, DBLP still indexes this work only as CoRR/arXiv and no final conference or journal venue could be verified. Keep `arXiv` as the venue until a final publication is confirmed.

## Why it belongs in NLOS_Overview

This is not a generic transient-imaging citation. The paper contains a dedicated **TRT-NLOS** reconstruction pipeline for confocal transient NLOS data. It combines a lightweight transient denoiser, physics-derived shallow features, local/global spatio-temporal self-attention encoders, spatio-temporal cross-attention decoders, and feature fusion to recover hidden-scene intensity and depth. It is evaluated against FBP, LCT, f-k, RSD and learned baselines on synthetic and measured NLOS data, and releases code plus real NLOS measurements.

The useful field trajectory is:

`physics-based transient inversion -> learned transient reconstruction -> Transformer-based spatio-temporal modeling -> generic transient foundation/pretraining models (e.g. MARMOT)`

## Repository duplicate check

Repository-wide searches for the exact title and `TRT-NLOS` returned no matches in the current corpus. No commit message matching “Time-Resolved Transformer” was found either.

## Required guarded integration

Because README.md (~179 KB) and egbib.bib (~276 KB) are large and the available write action replaces whole files, do **not** rebuild them from truncated connector output. Apply the following insertions from a full local checkout or another non-truncating path.

### README.md

Add to **Latest Additions** and to the 2025 learned/transient timeline:

> **3D Reconstruction from Transient Measurements with Time-Resolved Transformer** — Li et al., arXiv 2025. TRT introduces local/global spatio-temporal self-attention and cross-attention tailored to transient measurements; its TRT-NLOS branch combines denoising, physics-derived shallow features, and Transformer fusion for hidden-scene intensity/depth reconstruction on simulated and real captures.

Suggested category: **Deep Learning for NLOS / Learned Reconstruction / Transient Transformers**.

### Website / Paper Explorer

Add the same record to the canonical paper data source used by `index.html` (currently under the repository `data/` pipeline) and expose it in Latest Additions, 2025 timeline, learned methods, and transient/Transformer filters. Link the arXiv page and project/code repository when available.

### Survey source

Integrate semantically into the learned-reconstruction section (rather than appending a standalone list item), near NLOST / TransiT / ST-Mamba / NLOS-MT / MARMOT. Suggested literature-review sentence:

> Beyond task-specific transient Transformers, Li *et al.* introduce TRT-NLOS, which factorizes local and global spatio-temporal attention and then recombines them through cross-attention, illustrating a broader shift from purely reconstruction-specific networks toward reusable architectures tailored to the structure of transient measurements.

Use citation key `liTimeResolvedTransformer2025`.

### Bibliography

Merge `egbib_20260831_trt_nlos_gap.bib` into the canonical bibliography used by `bare_jrnl.tex`, preserving the current arXiv-only venue until a final venue is verified.

### Consistency / PDF rebuild

After integration, verify the title/citation appears in README, website source, survey TeX, and canonical bibliography, then rebuild `bare_jrnl.pdf` from a clean LaTeX build. Confirm the PDF contains the new literature-review sentence and citation before publishing the binary.

## Citation-tracing notes from this run

Forward-citation/seed searches around LCT, f-k migration, phasor fields, computational periscopy, and Neural Transient Fields mostly returned works already present in the repository (e.g. Learned LCT, TLTM iteration, 3D Gaussian Transient Rendering, recent phasor-field and sparse-acquisition papers). The TRT paper was the strongest verified corpus gap found in this pass.
