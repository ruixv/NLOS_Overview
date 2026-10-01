# Directional confocal NLOS range-characterization gap (2026-10-01)

## Verified missing paper

Lingyun Qiu, Zuoqiang Shi, Jianyu Wang, and Shiwei Wu, **“Reconstruction and Range Characterization for a Directional Confocal Non-Line-of-Sight Imaging Model,”** arXiv:2609.26846 (2026). https://arxiv.org/abs/2609.26846

No final conference/journal venue was verified as of 2026-10-01, so the venue should remain arXiv rather than guessing a publication venue.

## Why it belongs

This is a mathematical/theoretical NLOS reconstruction paper rather than a generic inverse-problems citation. It studies directional albedo recovery from confocal NLOS measurements. Radial preprocessing reduces the directional model to spherical means of the divergence; the paper establishes uniqueness up to divergence-free fields, gives an explicit Fourier–sine reconstruction of the irrotational Helmholtz component, and characterizes the exact range of the forward operator in a weighted Hilbert space. It therefore extends the classical confocal/spherical-Radon theoretical line toward directional reflectance fields and explicit identifiability/range characterization.

## Safe integration plan

- **README.md:** add to the 2026 theory/modeling timeline and active ToF/confocal reconstruction section. Suggested summary: “Directional confocal NLOS theory: characterizes identifiability and the exact forward-model range for directional albedo fields, with an explicit Fourier–sine reconstruction of the recoverable irrotational component.”
- **index.html / Paper Explorer:** category `Active / ToF`, secondary tag `Theory / inverse problems`; add to Latest Additions and 2026 timeline.
- **bare_jrnl.tex:** integrate near the discussion of confocal forward models, spherical/Radon-transform formulations, and frequency-domain inversion—not as an isolated recent-work list. Suggested literature-review point: recent theory generalizes scalar-albedo confocal models to directional fields and makes the null space (divergence-free component) and recoverable component explicit.
- **Bibliography:** merge `egbib_20261001_directional_confocal_range.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- **PDF:** rebuild `bare_jrnl.pdf` only after the source and canonical bibliography are integrated and compile cleanly.

## Consistency status

The paper was absent from default-branch repository code search for both `2609.26846` and `Directional Confocal` before staging. This run intentionally did not overwrite large canonical artifacts without a complete safe read/edit/build cycle. The staging BibTeX and this note are therefore the authoritative pending integration record; README/index/survey/PDF must not be reported as updated until that integration and build are verified.
