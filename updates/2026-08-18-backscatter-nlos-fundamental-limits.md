# 18 August 2026 — Backscatter NLOS fundamental-limits gap

Status: pending guarded integration/build.

## Newly verified missing work

**Hüseyin Yiğitler, Musa Furkan Keskin, Ossi Kaltiokallio, and Riku Jäntti, “Ambient IoT Backscatter Devices as Passive Anchors for NLOS Cellular Positioning: Fundamental Limits,” arXiv:2607.03459, 2026.**

- Primary record: https://arxiv.org/abs/2607.03459
- arXiv DOI: https://doi.org/10.48550/arXiv.2607.03459
- Submitted 3 July 2026; the indexed v2 is dated 7 July 2026.
- No final accepted/published conference or journal venue could be verified in the current run, so the repository must retain **arXiv 2026** as the venue.

### Why it belongs

This paper is tightly adjacent to the repository’s RF/mmWave NLOS localization branch rather than a generic wireless-positioning paper. It models uplink NLOS positioning where the direct NLOS path and the backscatter-assisted paths share an unknown scatterer. Known-location Ambient-IoT backscatter devices act as passive anchors, but their reflection gains and residual phases are not assumed calibrated. The paper derives closed-form equivalent Fisher information matrices for calibrated, partially calibrated, and fully uncalibrated regimes, identifies which carrier-phase and bandwidth-dependent delay information survives the nuisance parameters, and maps the result to position-domain bounds. For joint single-snapshot identification of the UE and common scatterer it shows that at least two devices in 2D and three in 3D are necessary, with angular diversity required in addition to device count.

The contribution therefore complements the repository’s measured **Backscatter Assisted Indoor NLOS Positioning** entry: the earlier work demonstrates passive-anchor corridor tracking, whereas this paper supplies a calibration-aware fundamental-limit and deployment-geometry analysis.

## Citation-tracing / screening notes

This run rechecked the active optical core (Velten 2012, LCT, f-k, phasor fields), passive computational-periscopy line, NLOST/TransiT/ST-Mamba/DG-NLOS learned reconstruction branch, and modality-expansion work in acoustic, consumer-LiDAR, radar/RF/mmWave, and transient Gaussian rendering. The most recent high-confidence optical/transient candidates found in those searches were already present in the canonical corpus.

Two closely related backscatter items were screened separately:

1. **Backscatter Assisted Indoor NLOS Positioning**, arXiv:2606.17325. Secondary scholarly indexes reproduce an author/arXiv comment stating acceptance at IEEE PIMRC 2026, but this run did not find an official PIMRC program/proceedings or IEEE final record. Its current arXiv venue is therefore left unchanged rather than upgraded on secondary evidence alone.
2. **Self-Calibrated Indoor Tracking from Backscatter Fiducials under NLOS Transmitter Illumination**, arXiv:2606.17332. In its measured geometry the transmitter-to-fiducial links are NLOS but fiducial-to-receiver links are largely LOS. It is useful adjacent localization work, but weaker as a core hidden-space NLOS imaging/sensing entry than the shared-scatterer fundamental-limits paper, so it is not added in this run.

## Intended synchronized integration

The guarded integrator updates all public-facing artifacts together:

- `README.md`: paper row, RF/backscatter milestone line, and 18 August update date;
- `data/papers-source.html`: canonical Paper Explorer record, tracked-paper count, 2026 development timeline, and page date;
- `index.html`: visible update date;
- `article/5newscenes.tex`: semantic insertion in the radar/RF/mmWave section immediately after the measured passive-backscatter positioning discussion;
- `egbib_merged_20260711.bib`: unique `yigitlerAmbientIoTBackscatter2026` entry using arXiv metadata;
- `bare_jrnl.tex`: 18 August provenance marker;
- `bare_jrnl.pdf`: rebuild only after source/citation validation succeeds.

The associated GitHub Actions workflow performs a clean `pdflatex → bibtex → pdflatex → pdflatex` build, checks the citation in `.aux/.bbl`, verifies the title appears in extracted PDF text, render-checks the first and last pages, and only then commits the synchronized artifacts and rebuilt PDF.
