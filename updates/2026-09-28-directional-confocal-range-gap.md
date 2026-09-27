# Missing NLOS paper integration note — 2026-09-28

## Verified missing paper

Lingyun Qiu, Zuoqiang Shi, Jianyu Wang, and Shiwei Wu, **“Reconstruction and Range Characterization for a Directional Confocal Non-Line-of-Sight Imaging Model,”** arXiv:2609.26846, 2026. Submitted 22 September 2026. arXiv DOI: 10.48550/arXiv.2609.26846.

Verified source: https://arxiv.org/abs/2609.26846

No final journal/conference venue was verified in this run, so the venue must remain **arXiv (2026)** until a final publication is confirmed.

## Why it belongs in the survey

This is directly about confocal transient NLOS reconstruction, not a paper that merely cites NLOS work. It extends the mathematical understanding of directional/albedo-aware confocal NLOS. Radial preprocessing reduces the directional model to spherical means of the divergence; the paper identifies divergence-free fields as the complete ambiguity, gives an explicit Fourier–sine reconstruction of the irrotational Helmholtz component, characterizes the weighted Hilbert-space range of valid data, proves a local-data uniqueness result, and implements an FFT/Stolt reconstruction with O(N^3 log N) complexity. Imaging examples include model-generated, rendered, and measured transients.

## Repository check

An exact-title search of the repository default branch returned no match before this staging note was created.

## Required canonical integration

1. **README.md** — add to the 2026 active/transient NLOS timeline, preferably near analytic/frequency-domain reconstruction and directional/reflectance-aware methods. Suggested summary: “Provides a rigorous directional confocal NLOS model: radial preprocessing maps measurements to spherical means of the directional-albedo divergence; characterizes the divergence-free ambiguity and data range, proves local uniqueness, and gives an FFT/Stolt reconstruction for the recoverable irrotational component.”
2. **index.html / Paper Explorer** — add under Active / Transient / Confocal / Analytic Reconstruction / Theory, with tags such as directional albedo, inverse problem, spherical means, range characterization, Helmholtz decomposition, Stolt interpolation.
3. **bare_jrnl.tex** — integrate semantically into the analytic/model-based active-NLOS discussion rather than appending a paper list. It is useful after LCT/f-k/Radon-transform material to show that recent work is moving beyond scalar Lambertian hidden-scene models toward directional fields while explicitly identifying identifiability limits and valid-data ranges.
4. **Bibliography** — merge the verified entry staged in `egbib_20260928_directional_confocal_range.bib` into the canonical bibliography used by `bare_jrnl.tex`, avoiding duplicate keys.
5. **bare_jrnl.pdf** — rebuild only after source/bibliography integration and commit the regenerated PDF if binary update is available.
6. **Consistency check** — verify the paper appears consistently in README, website, survey text, canonical bibliography, and rebuilt PDF.

## Safety/status

This run did not overwrite large canonical files from partial/truncated connector payloads. The BibTeX staging file and this note are the verified safe updates. Canonical integration and PDF rebuild remain pending and must not be reported as completed until validated.
