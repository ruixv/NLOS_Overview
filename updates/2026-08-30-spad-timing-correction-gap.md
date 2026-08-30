# 2026-08-30 update: SPAD timing-correction NLOS gap

## Verified missing paper

Alexander Spaett, Stéphane Schertzer, Thai-An Nguyen, and Martin Laurenzis, **“Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging,”** *Optics Express*, 34(12):22596–22613, 2026. DOI: `10.1364/OE.584776`.

Publisher/PubMed metadata verify the final journal venue and pagination. The work is genuinely NLOS-specific: it corrects SPAD-array TCSPC timing nonuniformity and establishes a geometry-aware absolute time reference for NLOS measurements, then demonstrates improved reconstructions in two non-confocal experiments and simulated confocal data. The paper reconstructs with the Phasor-Field method, so it belongs directly in the hardware/calibration trajectory supporting modern transient NLOS rather than in generic SPAD instrumentation.

## Why it matters

The paper addresses a practical deployment bottleneck that is easy to miss in algorithm-centered surveys: pixel-dependent TDC gain/bin-width errors and scan-point-dependent temporal referencing can blur or depth-shift reconstructions even when the inverse solver is correct. Its LUT-based correction is fast and parallelizable, and the LOS-feature-based time reference removes the need for a separate external timing calibration. This extends the development trajectory from high-resolution SPAD arrays and phasor-field reconstruction toward calibration-aware, scalable transient NLOS systems.

Suggested concise summary:

> **Fast SPAD-array timing-error correction with time-referencing for NLOS imaging** — Corrects pixel-wise TDC/bin-width nonuniformity with a precomputed LUT and derives an intrinsic LOS-based reference time for each illumination/sensing pair, yielding sharper and more accurate SPAD-array transient NLOS reconstructions without external timing calibration.

## Guarded integration locations

### README.md

Add to **Latest Additions** and to the active-NLOS hardware/acquisition/calibration portion of the timeline, near SPAD-array / compact / eye-safe / consumer-LiDAR hardware entries.

Recommended row metadata:
- Year: 2026
- Venue: *Optics Express* 34(12), 22596–22613 (2026)
- DOI: `10.1364/OE.584776`
- Category: Active NLOS / SPAD hardware / calibration / transient preprocessing

### Website / Paper Explorer

Add the same paper object to the canonical paper data source used by `index.html` / Paper Explorer, tagged with terms such as:
`active`, `transient`, `SPAD`, `TCSPC`, `calibration`, `timing`, `phasor-field`, `hardware`.

Also expose it in Latest Additions and the 2026 timeline.

### Survey LaTeX

Integrate semantically into the active-NLOS hardware / acquisition / SPAD discussion rather than appending a detached list item. A suitable literature-review sentence is:

> As SPAD arrays move NLOS acquisition toward parallel and higher-throughput capture, pixel-dependent TDC nonuniformity and scan-dependent timing offsets become reconstruction-limiting calibration errors; Spaett *et al.* introduced a lookup-table bin-width correction together with an intrinsic LOS-feature-based time reference, improving phasor-field reconstructions without requiring external timing calibration~\cite{spaettSPADTimingNLOS2026}.

If the survey already discusses consumer LiDAR, compact SPAD arrays, scan-free NLOS, or eye-safe nanosecond-diode systems, place this sentence nearby to emphasize the complementary role of calibration in practical deployment.

### Bibliography

Merge `egbib_20260830_spad_timing_correction_gap.bib` into the canonical bibliography without duplicating the DOI or citation key.

## Build and consistency check

After guarded source integration:
1. Rebuild `bare_jrnl.pdf` from the canonical LaTeX source.
2. Confirm `spaettSPADTimingNLOS2026` resolves in `.aux/.bbl` with no undefined citation.
3. Confirm the DOI/title appear once in README, website corpus, survey bibliography, and PDF.
4. Confirm venue is *Optics Express* rather than arXiv.
5. Confirm the paper is categorized as active transient NLOS calibration/hardware support, not as a new inverse reconstruction algorithm.

## Safety note

This run did not overwrite large README / website / LaTeX files because the available connector returns large files in truncated chunks and update writes require whole-file replacement. Doing so from partial content risks data loss. The verified BibTeX entry and precise insertion plan are therefore staged safely for guarded integration.
