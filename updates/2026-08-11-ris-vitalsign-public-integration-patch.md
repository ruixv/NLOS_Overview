# 11 August 2026 — NLOS citation-trace and RF/RIS synchronization

A fresh keyword and forward-citation-oriented pass was run around the repository's core active, passive, learned, and modality-expansion seeds. The newest direct optical papers surfaced by the search (including geometry-constrained TVCG reconstruction, rough-wall thermal NLOS, diffuse-aware passive encoding, long-range/all-day SPAD systems, cost-effective FMCW interferometry, Neural Illumination Fields, physics-informed cascade learning, and recent sparse/irregular acquisition methods) were already present in the current repository corpus. No additional post-July-2026 direct NLOS-imaging record passed the relevance and metadata checks in this run.

The audit identified a cross-artifact gap in the RF/RIS branch and one venue correction:

1. **Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces** — Acta Electronica Sinica 53(1), 1–13 (2025), DOI `10.12263/DZXB.20240674`.
2. **Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring** — IEEE MTT-S IMBioC 2025, DOI `10.1109/IMBioC63524.2025.10989670`.
3. **mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera** — corrected from arXiv-only labeling to IEEE/RSJ IROS 2025, pp. 19661–19668, DOI `10.1109/IROS60139.2025.11246461`.

The two vital-sign papers are classified as **NLOS physiological/semantic sensing**, not hidden-shape imaging. The survey prose is also synchronized with previously catalogued records that lacked equivalent narrative integration: adaptive artifact cancellation, curvature regularization, TransDiff, adaptive spiral scanning, optimization-derived zero-shot attention, frequency-domain multi-regularization experts, and sparse-aperture ISAR NLOS imaging.

The bibliography merge consumes `egbib_20260811_ris_vitalsign_updates.bib` and the other dated supplements, so the final merged database uses verified conference/journal records rather than stale arXiv metadata. CI rebuilds `bare_jrnl.pdf` and validates source/bibliography/README/website/PDF consistency before the public merge.
