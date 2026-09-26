# Integration gap: Fast SPAD-array timing-error correction with time-referencing for NLOS imaging

## Verified paper

Alexander Spaett, Stéphane Schertzer, Thai-An Nguyen, and Martin Laurenzis, “Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging,” *Optics Express*, 34(12):22596–22613, 2026. DOI: 10.1364/OE.584776.

## Why it belongs

This is directly an NLOS/transient-imaging instrumentation paper, not a passing citation. It addresses pixel-dependent TDC timing errors in SPAD-array TCSPC measurements and establishes an absolute NLOS time reference from intrinsic LOS diffraction-wave and lens-flare peaks. The paper validates the correction in two non-confocal experimental setups and simulated confocal data, and reconstructs with the phasor-field algorithm. It therefore extends the active ToF/phasor-field development line toward practical SPAD-array calibration and deployable non-confocal acquisition.

## Contribution summary for README / Paper Explorer

**Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging** — Optics Express 2026. Introduces a two-stage calibration pipeline for SPAD-array NLOS: a pixel-wise lookup table corrects TDC bin-width/nonlinearity errors, while intrinsic LOS diffraction-wave and lens-flare signatures provide per-measurement absolute time referencing without external calibration, improving transient alignment and NLOS reconstruction sharpness.

Suggested tags: Active NLOS; transient imaging; SPAD array; TCSPC; calibration; non-confocal; phasor field; instrumentation.

## Suggested survey integration

- **README.md / 2026 timeline:** place under active/transient NLOS or practical sensing/instrumentation, near SPAD-array and non-confocal works.
- **index.html / Paper Explorer:** add the metadata and tags above; include in latest additions until displaced by newer papers.
- **bare_jrnl.tex:** integrate semantically in the active ToF hardware / single-photon acquisition discussion. Suggested literature-review sentence: “Recent work has also moved beyond reconstruction algorithms to correct hardware-level timing distortions: Spaett et al. calibrate pixel-dependent SPAD-array TDC bin widths and derive an intrinsic LOS-based time reference, enabling better-aligned non-confocal transients without external timing calibration.”
- **Bibliography:** merge `egbib_20260927_spad_timing_correction.bib` into the canonical bibliography, preserving repository citation-key conventions.
- **bare_jrnl.pdf:** rebuild only after the source and bibliography are integrated; verify citation resolution and consistency with README/index.

## Verification

Final venue verified as *Optics Express* 34(12), 22596–22613 (2026), DOI 10.1364/OE.584776. Exact-title and DOI searches of the repository default branch returned no match before staging. Do not label this as arXiv.

## Remaining work

Canonical README/index/LaTeX files were not overwritten from partial payloads in this run. Merge this staged entry into the complete current versions, compile `bare_jrnl.tex`, commit the regenerated PDF, then verify all public-facing artifacts contain the same paper/venue metadata.
