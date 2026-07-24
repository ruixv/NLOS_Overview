# Radar/mmWave/sub-THz NLOS reconstruction lineage — 24 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found. The newest date-verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

Citation tracing through the active optical NLOS core and the radar reconstruction literature exposed a major modality-level consistency gap. Eight direct hidden-scene reconstruction papers are absent from `README.md` and `index.html`; seven are also absent from the survey prose and consolidated bibliography, while HoloRadar is discussed in `article/5newscenes.tex` but lacks a public explorer record and canonical BibTeX entry.

## Verified missing lineage

1. **Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar** — Shunjun Wei et al.; *IEEE Transactions on Geoscience and Remote Sensing* 60, 1–18 / Article 5106518 (2022); DOI `10.1109/TGRS.2021.3112579`.
2. **Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging** — Xiang Cai et al.; *Journal of Radars* 13(4), 791–806 (2024); DOI `10.12000/JR24060`.
3. **RM-CSTV: An Effective High-Resolution Method of Non-Line-of-Sight Millimeter-Wave Radar 3-D Imaging** — Xinyuan Liu et al.; *National Science Open* 3(5), Article 20230085 (2024); DOI `10.1360/nso/20230085`.
4. **Non-Line-of-Sight 3D Reconstruction with Radar (HoloRadar)** — Haowen Lai, Zitong Lan, Mingmin Zhao; *NeurIPS 2025*.
5. **Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement** — Xiang Cai et al.; *IEEE Transactions on Antennas and Propagation* 73(10), 8088–8103 (2025); DOI `10.1109/TAP.2025.3583778`.
6. **Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning** — Xiang Cai et al.; *IEEE Transactions on Computational Imaging* 11, 1190–1205 (2025); DOI `10.1109/TCI.2025.3597462`.
7. **RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar** — Kun Chen et al.; *Journal of Radars* 15(1), 42–63 (2026); DOI `10.12000/JR25132`.
8. **Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging** — Kun Chen et al.; *Photonics* 13(5), Article 440 (2026); DOI `10.3390/photonics13050440`.

## Intended cross-artifact integration

The guarded synchronizer `scripts/sync_nlos_20260724_radar_lineage.py` contains precise, fail-closed edits to:

1. Add all eight papers to `README.md` Latest Additions and the 2022/2024/2025/2026 development timeline.
2. Add searchable `index.html` paper-explorer records, expand the website timeline, and change the tracked-entry count from 193 to 201.
3. Insert two semantically placed literature-review paragraphs into `article/5newscenes.tex`:
   - **Measured mmWave reconstruction from physical models to fast regularized migration**, connecting the 2022 measured model to NSIR and RM-CSTV.
   - **Self-supervised and model-unfolded radar NLOS reconstruction**, connecting ACTE-Net, equivariant adaptive-threshold learning, RM-operator unfolding, 121 GHz holographic unfolding, and HoloRadar.
4. Add canonical BibTeX entries to `egbib_merged_20260711.bib`, including the missing `laiHoloRadar2025` record required by the existing survey citation.
5. Add a trace marker to `bare_jrnl.tex`, compile the survey, validate all eight generated bibliography items, inspect extracted PDF text and rendered pages, and commit the regenerated `bare_jrnl.pdf`.

## Current status

The guarded source synchronizer and GitHub Actions build workflow have been committed. At the time this note was written, no workflow-generated source-integration/PDF-rebuild commit was present on `master`. Therefore the public README, website, survey source, consolidated bibliography, and PDF are **not yet claimed as synchronized for these eight records**. No large file was overwritten blindly, and no PDF update is being claimed without a verified binary commit.
