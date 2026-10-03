# NLOS literature gap: eye-safe compact SPAD-array localization (2026-10-03)

## Verified missing paper

**Konstantin Albert, Johannes Klein, Martin Laurenzis, and Andreas Gries, “Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays,” Journal of the European Optical Society-Rapid Publications (2026).** DOI: 10.1051/jeos/2026019.

Publisher metadata verifies acceptance on 24 February 2026 and final publication by EDP Sciences in 2026. Repository-wide searches for the exact title, DOI, and `eye-safe` returned no match before this staging update.

## Why it belongs in NLOS_Overview

This is a direct active optical NLOS localization paper, not a generic NLOS sensing citation. It targets a practical hardware limitation of time-resolved optical NLOS: laboratory systems often rely on expensive ultrashort lasers and can require optical powers that complicate eye-safe deployment.

The system combines compact 905-nm nanosecond pulsed laser diodes with a 24 x 32 SPAD array containing per-pixel timing. Rather than scanning confocally, the detector observes a relay-wall region in parallel. Two illumination positions outside the detector field of view avoid first-photon saturation and provide complementary ellipsoidal constraints. Superposing their back-projection reconstructions geometrically confines the feasible target region. The paper also shows that temporal matched filtering can compensate for the long laser pulse more effectively than spatial edge filtering, so localization can become limited mainly by detector timing and measurement geometry rather than laser pulse width.

The authors explicitly position the design toward a hybrid LiDAR-NLOS system for direct relay-wall calibration. This makes the paper especially relevant to the survey's trajectory from laboratory picosecond/femtosecond ToF NLOS toward compact, scan-free, eye-safe, LiDAR-like hardware.

## Recommended canonical integration

### README.md

Add under the 2026 active optical / practical systems timeline rather than learned reconstruction. Suggested concise entry:

- **Eye-safe compact SPAD-array NLOS localization** — Albert *et al.*, *Journal of the European Optical Society-Rapid Publications*, 2026. Uses compact 905-nm nanosecond laser diodes and a time-resolved 24 x 32 SPAD array for photon-efficient non-confocal localization; dual off-axis illumination and matched filtering mitigate detector saturation and long-pulse uncertainty, pointing toward practical hybrid LiDAR-NLOS systems. DOI: 10.1051/jeos/2026019.

### Website / Paper Explorer

Categories/tags: `Active NLOS`, `ToF`, `SPAD array`, `non-confocal`, `scan-free`, `eye-safe`, `compact hardware`, `LiDAR`, `localization`, `2026`.

Development-line placement: laboratory ultrafast ToF hardware -> parallel SPAD-array acquisition -> compact/eye-safe NLOS -> consumer/practical LiDAR-like NLOS.

### Survey source

Integrate semantically into the active-NLOS acquisition/hardware discussion (the repository currently also has modular `article/2active.tex`; keep `bare_jrnl.tex` and modular sources consistent if both are maintained). A suitable literature-review sentence is:

> Recent hardware work further shifts active NLOS sensing toward deployable LiDAR-like architectures: Albert *et al.* combine eye-safe nanosecond laser diodes with a time-resolved SPAD array and parallel non-confocal wall observation, using spatially separated illumination and temporal matched filtering to compensate for first-photon saturation and long-pulse localization uncertainty \cite{albert2026eyesafe}.

This should be discussed near scan-free SPAD-array systems, compact/long-range prototypes, and consumer-LiDAR NLOS rather than appended as an isolated paper list.

### Bibliography

Merge `egbib_20261003_eyesafe_spad_gap.bib` into canonical `egbib.bib` after checking for key collision. The staging key is `albert2026eyesafe`.

### PDF/build consistency

After canonical source integration, rebuild `bare_jrnl.pdf` and verify that README.md, website/index.html, survey source, canonical bibliography, and PDF all contain the same final venue/year. Do not label this work as arXiv; the final publisher venue is verified.

## Current-run safety note

The repository's README is about 181 kB and `article/2active.tex` about 136 kB. This run did not overwrite those large canonical files without a complete read/edit/validation cycle. The verified bibliography staging entry and this precise insertion note were committed instead, preserving all existing content while making the missing paper actionable for the next safe canonical integration/build pass.
