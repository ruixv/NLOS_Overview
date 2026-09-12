# 2026-09-12 — SPAD-array timing correction / time referencing

## Newly verified missing paper

Alexander Spaett, Stéphane Schertzer, Thai-An Nguyen, and Martin Laurenzis, **“Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging,”** *Optics Express*, 34(12), 22596–22613, 2026. DOI: 10.1364/OE.584776.

This paper is directly relevant to transient NLOS acquisition rather than merely a generic SPAD-calibration work. It measures and corrects pixel-dependent TCSPC/TDC timing errors in a SPAD array (about 6% mean-bin-width variation and about 0.6% bin-to-bin fluctuation), uses a precomputed per-pixel lookup table to resample histograms onto a uniform temporal grid, and introduces an NLOS-specific absolute time-reference scheme based on intrinsic LOS features (the diffraction-wave and lens-flare peaks). The authors demonstrate sharper and better aligned NLOS reconstructions in two non-confocal experimental configurations and simulated confocal data.

## Why it belongs in the survey

The work fills a hardware/calibration gap between increasingly large SPAD arrays and reconstruction algorithms such as back-projection, f-k migration, LCT, and phasor-field methods. Its field-development role is best summarized as:

`single-pixel / small-array TCSPC -> scalable SPAD arrays -> pixel-wise timing calibration -> self-referenced NLOS transient alignment`

The paper should be categorized primarily under **Active NLOS Imaging / Hardware Devices and calibration**, with a cross-reference from reconstruction preprocessing / photon-efficient transient acquisition.

## Verified metadata

- Venue: *Optics Express*
- Volume: 34
- Issue: 12
- Pages: 22596–22613
- Publication date: June 2026
- DOI: 10.1364/OE.584776
- Authors: Alexander Spaett; Stéphane Schertzer; Thai-An Nguyen; Martin Laurenzis

A verified staging entry is in `egbib_20260912_spad_timing_correction.bib` with key `spaettSPADTiming2026`.

## Required integration locations

### README.md

Add a 2026 entry to **Latest Additions** and to the active-NLOS hardware / transient-acquisition portion of the development timeline. Suggested concise summary:

> **Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging — Spaett et al. — Optics Express 34(12), 22596–22613 (2026).** Corrects pixel-dependent SPAD/TCSPC time-bin nonuniformity with a precomputed LUT and derives an NLOS-specific absolute timing reference from intrinsic LOS peaks, improving temporal alignment and reconstruction sharpness without external path-length calibration.

### article/2active.tex

Insert into the hardware / SPAD-array / transient acquisition subsection near discussion of SPAD detector architecture, calibration, photon-efficient acquisition, or array-based NLOS systems. Suggested survey prose:

> As SPAD arrays grow in pixel count, detector-side timing nonuniformity becomes a reconstruction-limiting error source rather than a negligible calibration detail. Spaett et al.~\cite{spaettSPADTiming2026} measured pixel-dependent TCSPC time-bin variations and introduced a lookup-table correction that resamples each pixel onto a uniform temporal grid. For NLOS acquisition they further derived an absolute time reference from intrinsic line-of-sight diffraction-wave and lens-flare features, avoiding an external path-length calibration and yielding sharper, better aligned non-confocal reconstructions. This work highlights a shift from reconstruction-only optimization toward detector-aware transient calibration as a prerequisite for scalable array-based NLOS imaging.

### Canonical bibliography

Merge `spaettSPADTiming2026` from `egbib_20260912_spad_timing_correction.bib` into the bibliography actually loaded by `bare_jrnl.tex` (currently `egbib_merged_20260711.bib`, unless that wiring has changed in a later commit). Check for title/DOI duplicates before insertion.

### Website / Paper Explorer

Add under Active NLOS / Hardware & Acquisition and include the DOI link, final venue metadata, and the concise summary above. If the homepage has a latest-additions or 2026 timeline panel, include it there as well.

### PDF consistency

After source and canonical bibliography integration, compile `bare_jrnl.tex` and verify that `spaettSPADTiming2026` resolves, the bibliography shows *Optics Express* 34(12), 22596–22613 (2026), and `bare_jrnl.pdf` is regenerated before reporting full cross-artifact completion.

## Citation-tracing/search note

This run also rechecked the forward-citation neighborhoods and recent successors of the canonical LCT, f-k migration, phasor-field, computational-periscopy, Neural Transient Fields, learned-transformer, acoustic, RF/mmWave, consumer-LiDAR, and 3D transient-rendering lines. The prominent 2026 reconstruction papers returned by those searches were already represented in the repository corpus; the SPAD timing paper was retained because it is a genuinely NLOS-specific acquisition/calibration contribution and no repository occurrence of its title, DOI, or authors was found during the direct repository checks.

## Safe-update status

The main public files are large and connector responses may truncate their contents. Do not overwrite README, `article/2active.tex`, `index.html`, or the canonical merged bibliography from a partial fetch. Integrate the staged entry only after obtaining complete source content or an edit mechanism that can safely preserve the entire file, then rebuild the PDF.
