# 2026-09-30 integration gap: SPAD-array timing correction for NLOS

## Verified missing paper

Alexander Spaett, Stéphane Schertzer, Thai-An Nguyen, and Martin Laurenzis, **“Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging,”** *Optics Express*, 34(12):22596–22613, 2026. DOI: 10.1364/OE.584776.

Verified final venue: Optics Express (published June 2026). Repository-wide exact-title and DOI searches returned no matches before staging.

## Why it belongs

This is directly NLOS-specific instrumentation/calibration work rather than generic SPAD characterization. It corrects pixel-dependent TCSPC/TDC bin-width and offset errors with a precomputed lookup table, then derives an absolute NLOS time reference from intrinsic LOS diffraction-wave and lens-flare features. The paper validates the correction in two non-confocal experimental NLOS setups and simulated confocal data, and shows sharper phasor-field reconstructions after correction. It fills a practical systems gap between SPAD-array acquisition and downstream transient reconstruction.

## Recommended integration

- **README / 2026 timeline:** place under active ToF / SPAD hardware and calibration, near scan-free SPAD-array and practical-system papers. Suggested summary: “Corrects per-pixel TCSPC timing-bin nonuniformity and establishes scan-position-specific absolute time references from intrinsic LOS features, improving temporal alignment and NLOS reconstruction fidelity without external timing calibration.”
- **Website / Paper Explorer:** tags: Active NLOS; ToF; SPAD array; TCSPC; calibration; non-confocal; phasor field; practical systems.
- **bare_jrnl.tex:** integrate in the active-ToF hardware/calibration discussion, emphasizing that modern parallel SPAD arrays introduce pixel-dependent TDC/bin-width errors that can directly blur reconstructed geometry; cite this work as an explicit sensor-to-reconstruction calibration solution. This is especially appropriate near practical SPAD-array / low-latency / scan-free system discussion, not only in a generic learned-method list.
- **Bibliography:** merge the verified entry staged in `egbib_20260930_spad_timing_correction.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- **PDF:** rebuild `bare_jrnl.pdf` only after canonical TeX and bibliography integration.

## Consistency status

Canonical README/index/TeX/PDF were not overwritten in this run because safe complete-file editing/build validation was not established. This note is intentionally a non-destructive staging record; do not claim the PDF is updated until it is rebuilt and committed.
