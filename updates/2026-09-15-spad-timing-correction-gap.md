# 2026-09-15 integration note: SPAD-array timing correction

## Verified missing paper

Alexander Spaett, Stéphane Schertzer, Thai-An Nguyen, and Martin Laurenzis, “Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging,” *Optics Express*, vol. 34, no. 12, pp. 22596–22613, 2026. DOI: 10.1364/OE.584776.

## Why it belongs

This paper addresses a hardware/measurement bottleneck that becomes increasingly important as NLOS systems move from single-pixel detectors toward SPAD arrays. Pixel-dependent TDC gain, offset, and differential-nonlinearity errors broaden aggregated transients. The authors use a precomputed per-pixel lookup table to equalize time-bin widths, then derive an NLOS-specific absolute time reference from intrinsic LOS diffraction-wave and lens-flare peaks. They demonstrate sharper phasor-field reconstructions in two non-confocal experimental systems and simulated confocal data. The paper explicitly builds on Velten-style transient NLOS and uses Liu et al.’s phasor-field reconstruction, making it a strong Core-paper forward-citation descendant.

## Recommended integration

- README Latest Additions: add under 2026 active NLOS / hardware and calibration. Suggested summary: “Corrects SPAD-array pixel-wise TDC gain/offset/bin-width errors with a fast LUT and derives an intrinsic LOS-based time reference for NLOS measurements, improving temporal alignment and phasor-field reconstruction without external timing calibration.”
- README taxonomy: Active NLOS Imaging → Hardware Devices / calibration and practical systems.
- Website Paper Explorer: tags `active`, `SPAD`, `TCSPC`, `calibration`, `phasor-field`, `non-confocal`, `hardware`.
- Timeline: place in 2026 practical-system maturation alongside compact eye-safe SPAD arrays, consumer LiDAR, long-range systems, and GPU reconstruction.
- Survey source: integrate semantically in the active-NLOS hardware/acquisition discussion, after SPAD-array/high-throughput acquisition and before reconstruction algorithms. Emphasize that higher spatial parallelism introduces pixel-dependent timing nonuniformity, so detector calibration becomes part of the NLOS inverse pipeline rather than a separable hardware detail.
- Canonical bibliography: merge `egbib_20260915_spad_timing_correction.bib` into the bibliography used by the survey.
- PDF: rebuild `bare_jrnl.pdf` only after README/website/survey/bibliography synchronization.

## Consistency status

At this run, repository code search returned no title or DOI hit for this paper. The staging BibTeX and this precise integration note were committed. Large public-facing files were not overwritten from truncated responses; therefore README/index/survey/PDF synchronization remains pending and must not be claimed as complete.
