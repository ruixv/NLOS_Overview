# 2026-09-13 — Missing mmWave NLOS radar imaging papers

This update records two verified IEEE journal papers that are directly relevant to the RF/mmWave NLOS-imaging branch but were not found in the current repository by title or DOI search.

## 1. CMTI: Non-Line-of-Sight Radar Imaging for Non-Cooperative Corner Motion Target

- **Authors:** Yanbo Wen, Shunjun Wei, Xiang Cai, Rong Shen, Mou Wang, Jun Shi, Guolong Cui
- **Venue:** IEEE Transactions on Vehicular Technology, 74(1), 179–190 (2025)
- **DOI:** 10.1109/TVT.2024.3398218
- **Final venue verification:** IEEE Xplore / DBLP metadata
- **Contribution:** Introduces an mmWave NLOS imaging pipeline for moving hidden targets. CMTI first suppresses background clutter and extracts NLOS target echoes, then combines PFA-based ISAR imaging with envelope alignment, phase correction, autofocus, target-rotation estimation, and a mirror-symmetry reconstruction step. Near-field measurements demonstrate high-resolution images of non-cooperative moving targets around a corner.
- **Trajectory placement:** static mmWave NLOS reconstruction -> moving-target NLOS ISAR -> learned/unsupervised mmWave NLOS reconstruction.

## 2. Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning

- **Authors:** Xiang Cai, Shunjun Wei, Mou Wang, Hao Zhang, Kun Chen, Xinyuan Liu, Jun Shi, Guolong Cui
- **Venue:** IEEE Transactions on Computational Imaging, 11, 1190–1205 (2025)
- **DOI:** 10.1109/TCI.2025.3597462
- **Final venue verification:** IEEE Xplore / DBLP metadata
- **Contribution:** Proposes a fully self-supervised equivariant-imaging framework for 2D/3D NLOS mmWave SAR reconstruction. The reconstruction network is a TV-constrained deep-unfolding model, while APConv learns adaptive thresholds; group-invariance/equivariance supplies supervision from partial, noisy, multipath-contaminated NLOS measurements without requiring clean LOS ground truth. Experiments use measured NLOS mmWave echoes.
- **Trajectory placement:** model-based sparse mmWave NLOS -> deep unfolding -> self-supervised/equivariant NLOS SAR reconstruction.

## Repository integration locations

### README.md

Add both papers to the RF/mmWave/radar subsection and the development timeline. Suggested concise entries:

- **2025 — CMTI: Non-Line-of-Sight Radar Imaging for Non-Cooperative Corner Motion Target — IEEE TVT.** Around-corner mmWave ISAR for non-cooperative moving targets; combines NLOS echo extraction, autofocus/PFA reconstruction, and mirror-symmetry correction to form high-resolution hidden-target images.
- **2025 — Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning — IEEE TCI.** Fully self-supervised NLOS mmWave SAR reconstruction using equivariant imaging, a TV-constrained deep-unfolding backbone, and adaptive learned thresholds, validated on measured multipath-contaminated echoes.

### Survey source

Integrate semantically in the RF/mmWave subsection of `article/5newscenes.tex` rather than appending an isolated list. Suggested literature-review prose:

> Beyond static hidden-scene recovery, Wen et al. extended mmWave NLOS imaging to non-cooperative moving targets through CMTI, coupling corner-echo extraction with ISAR autofocus and mirror-symmetry reconstruction \cite{wenCMTINLOS2025}. More recently, Cai et al. moved the mmWave branch toward data-driven inverse solvers without clean LOS supervision: their equivariant-imaging framework unfolds a TV-regularized reconstruction algorithm and learns adaptive thresholds directly from measured NLOS echoes under group-consistency constraints \cite{caiEquivariantNLOSmmWSAR2025}. Together with recent artifact-cancellation networks and HoloRadar-style scene reconstruction, these works mark a transition from hand-designed multipath inversion toward motion-aware and self-supervised learned radar NLOS imaging.

### Bibliography

Merge the two entries from `egbib_20260913_missing_mmwave_nlos_radar.bib` into the canonical bibliography used by `bare_jrnl.tex` (currently `egbib_merged_20260711.bib`, unless the survey source has since changed its bibliography target). Preserve citation keys:

- `wenCMTINLOS2025`
- `caiEquivariantNLOSmmWSAR2025`

### Website / paper explorer

Add both under **RF / mmWave / Radar NLOS**. Suggested tags:

- CMTI: `RF`, `mmWave`, `Radar`, `ISAR`, `Dynamic`, `Moving target`, `Model-based`
- Equivariant mmW SAR: `RF`, `mmWave`, `Radar`, `SAR`, `Deep unfolding`, `Self-supervised`, `Equivariant learning`

Place CMTI before the 2025 TAP artifact-cancellation paper in the historical progression, and place the equivariant TCI paper alongside the 2025 learned mmWave reconstruction works.

## Consistency checklist

Before claiming the update complete:

1. Add both records to README.md.
2. Add both records to `index.html` / paper explorer / timeline data.
3. Insert the survey prose into the RF/mmWave section of `article/5newscenes.tex` (or the current equivalent source included by `bare_jrnl.tex`).
4. Merge both BibTeX entries into the canonical bibliography.
5. Recompile `bare_jrnl.pdf` and confirm both references resolve.
6. Verify README, website, LaTeX source, bibliography, and PDF all expose the same final venue metadata.

## Search notes

The broader September 2026 keyword and forward-citation pass also resurfaced 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, TLTM iteration, transient-video interpolation, learned LCT, passive diffuse-aware attention, thermal NLOSFormer, and compact long-range optical NLOS; these are already represented in the repository or recent update logs and should not be duplicated. A 2026 SPAD/TCSPC human-presence detection paper was also found, but the two entries above were prioritized because they are direct image-reconstruction papers and fill a clearer missing mmWave-imaging lineage.
