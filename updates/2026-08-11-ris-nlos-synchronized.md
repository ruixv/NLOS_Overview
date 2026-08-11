# 11 August 2026 — RF/RIS NLOS public synchronization

This bounded synchronization follows a fresh keyword, venue, arXiv, project-page, and forward-citation-oriented pass around the repository's core NLOS papers. No additional recent direct NLOS-imaging paper survived the relevance and metadata checks beyond the already curated 2026 frontier. The actionable gap was a small RF/RIS branch plus two final-venue/cross-artifact corrections.

## Integrated / corrected

1. **Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces** — *Acta Electronica Sinica* 53(1), 1–13 (2025), DOI `10.12263/DZXB.20240674`. Added as physiological RF/RIS NLOS sensing, not geometric imaging.
2. **Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring** — IEEE IMBioC 2025, DOI `10.1109/IMBioC63524.2025.10989670`. Added as experimentally validated NLOS vital-sign sensing.
3. **Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface** — final IEEE RadarConf25 2025 record, DOI `10.1109/RadarConf2559087.2025.11205052`; the later arXiv copy remains auxiliary metadata only.
4. **mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera** — corrected from arXiv-only labeling to final IEEE/RSJ IROS 2025, DOI `10.1109/IROS60139.2025.11246461`.
5. **Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength** — the final IEEE ICEE 2025 record was already present in the website, survey source, and bibliography; this run adds an explicit README Latest Additions entry so the public artifacts no longer disagree.

The existing supplemental bibliography `egbib_20260811_ris_vitalsign_updates.bib` is the canonical source for the four RF/RIS records. The merge step regenerates `egbib_merged_20260711.bib` and normalizes the survey citations to those final records.

## Search decisions

The fresh pass also screened adjacent shadow/gesture semantic work and other 2026 NLOS-adjacent submissions. Items without a verified final venue or without a sufficiently direct NLOS sensing/reconstruction contribution were not promoted merely because they cite NLOS core papers.

## Synchronization target

The CI integration updates `README.md`, `index.html`, `article/5newscenes.tex`, `bare_jrnl.tex`, the merged BibTeX database, and the compiled `bare_jrnl.pdf`, then validates source/PDF consistency before committing the public artifacts.
