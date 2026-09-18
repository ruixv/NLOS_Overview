# 2026-09-18 verified NLOS literature gap: eye-safe compact SPAD-array localization

## Paper
Konstantin Albert, Jonathan Klein, Martin Laurenzis, and Andre Grosse, “Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays,” *Journal of the European Optical Society-Rapid Publications* (2026). DOI: 10.1051/jeos/2026019.

## Why it belongs
This is a genuine active optical NLOS system paper rather than a passing NLOS citation. It uses a 24×32 time-resolved SPAD array, compact 905-nm nanosecond laser diodes, non-confocal relay-wall measurements, ellipsoid/back-projection reconstruction, and dual off-axis illumination. The work targets practical eye-safe NLOS localization, studies pulse-width-induced uncertainty, and shows that temporal matched filtering can compensate long-pulse smearing. It also outlines a hybrid LiDAR–NLOS calibration route.

## Development-line placement
Place under active/transient NLOS hardware and practical deployment, near scan-free SPAD-array, consumer/compact LiDAR, eye-safe, and long-range NLOS work. Suggested trajectory: laboratory picosecond/femtosecond TCSPC systems → parallel SPAD-array acquisition → compact/consumer LiDAR-inspired hardware → eye-safe nanosecond-laser NLOS localization.

## Public-facing integration still required
- README.md: add a concise 2026 entry and place it in active optical / hardware / practical deployment categories.
- index.html / paper explorer / latest additions / timeline: add the same verified venue and DOI and emphasize compact eye-safe SPAD-array NLOS localization.
- bare_jrnl.tex: integrate semantically in the active optical hardware/practical-system discussion, not as a detached recent-paper list. Suggested sentence: “Recent work has further shifted active NLOS toward deployable hardware: Albert et al. combine a time-resolved SPAD array with compact eye-safe nanosecond laser diodes and dual off-axis illumination, showing that matched filtering can mitigate pulse-width-induced localization uncertainty while retaining photon-efficient non-confocal acquisition.”
- egbib.bib: merge the staged BibTeX entry from `egbib_20260918_eye_safe_spad_nlos.bib` after checking for key collisions.
- bare_jrnl.pdf: rebuild after source/bibliography integration and verify that the citation resolves.

## Verification
Publisher metadata: DOI 10.1051/jeos/2026019; received 26 Nov 2025; accepted 24 Feb 2026; published by Journal of the European Optical Society-Rapid Publications in 2026. Repository code search for the full title/eye-safe phrase returned no hit before staging.

## Safety note
The repository's README and canonical bibliography are large. This run did not overwrite them from truncated payloads. The staged BibTeX and this insertion note are intentionally small, auditable changes until full-file safe editing/build is available.
