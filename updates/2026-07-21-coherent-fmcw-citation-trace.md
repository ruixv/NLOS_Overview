# 21 July 2026 coherent-FMCW optical NLOS citation trace

## Verified missing lineage

This pass identified three direct optical NLOS papers absent from the README, homepage, survey narrative, and consolidated bibliography:

1. **Non-Line-of-Sight Imaging and Vibrometry Using a Comb-Calibrated Coherent Sensor** — Huang et al., *Physical Review Letters* 132(23), 233802 (2024), DOI `10.1103/PhysRevLett.132.233802`.
   - Optical-frequency-comb-calibrated FMCW coherent sensing.
   - Sub-picosecond effective temporal resolution, submillimeter NLOS localization and 3D imaging, strong-ambient-light operation, and hidden-object vibrometry.

2. **High-Resolution Non-Line-of-Sight Tracking by Comb-Calibrated FMCW LiDAR** — Ye et al., *Laser & Photonics Reviews* 19(6), 2401250 (2025), DOI `10.1002/lpor.202401250`.
   - Directly cites Velten 2012, LCT, phasor-field and f-k milestones.
   - Snapshot multi-object NLOS tracking with reported 2 mm position and 2 mm/s velocity accuracy.

3. **Non-Line-of-Sight Ranging and 3D Imaging Using Vector Enhanced Sensitive FMCW LiDAR** — Chen et al., *Journal of Lightwave Technology* 43(9), 4119–4126 (2025), DOI `10.1109/JLT.2024.3523206`.
   - Laser-feedback interferometry, polarization-vector enhancement and K-domain resampling.
   - Better-than-32-micrometer absolute ranging and millimeter-level hidden 3D imaging at approximately 2.8 m.

The repository already covered the 2026 endpoint, **Submillimeter non-line-of-sight ranging and imaging via cost-effective FMCW interferometry**, DOI `10.1364/PRJ.595776`. This update therefore integrates the missing 2024–2025 precursors and rewrites the survey treatment as a coherent technical trajectory rather than duplicating the 2026 record.

## Cross-artifact integration

The guarded synchronizer updates:

- `README.md`: three verified rows and 2024/2025 milestones;
- `index.html`: searchable paper objects, timeline context and tracked-entry count 175 → 178;
- `article/2active.tex`: a dedicated coherent-FMCW hardware/reconstruction paragraph and a corrected active-system table row;
- `bare_jrnl.tex`: coverage date and integration marker;
- `egbib_merged_20260711.bib`: generated from the new canonical supplement without duplicate DOI or citation keys;
- `bare_jrnl.pdf`: clean LaTeX/BibTeX rebuild and text/citation validation.

The build workflow rejects partial DOI coverage, missing citation keys, duplicate records, undefined citations, empty PDFs, or a stale website count before committing generated sources and the binary PDF.

## Latest-publication check

The search did not verify a direct NLOS imaging publication later than **15 July 2026**, so *Non-line-of-sight imaging via physics-informed cascade learning* remains the newest directly date-verifiable NLOS paper in this run.
