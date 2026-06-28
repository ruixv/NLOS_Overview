# 2026-06-28 Low-Cost LiDAR / mmWave NLOS Update

This update pass used keyword search plus citation-tracing style checks around core NLOS imaging papers and recent modality-expansion papers. Three additional relevant papers were found that were not explicitly covered in the README / homepage snapshot.

## Newly identified entries

1. **DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs** — Behari et al., arXiv 2026  
   Link: https://arxiv.org/abs/2604.16201  
   Category: Consumer / low-cost LiDAR NLOS; datasets; spatial reasoning.  
   Contribution: introduces 72,000 real-world hidden-object scenes captured as space-time histograms from low-cost LiDARs, shifting consumer-LiDAR NLOS from pure reconstruction toward data-driven spatial reasoning.

2. **MITO: Enabling Non-Line-of-Sight Perception using Millimeter-waves through Real-World Datasets and Simulation Tools** — Dodds, Boroushaki, Adib, arXiv 2025  
   Link: https://arxiv.org/abs/2502.10259  
   Category: Radar / RF / mmWave NLOS; datasets; simulation tools.  
   Contribution: provides multi-spectral mmWave images, LOS/NLOS captures, segmentation masks, and a simulation tool for learning-based NLOS perception through common occluders.

3. **mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera** — Park et al., arXiv 2025  
   Link: https://arxiv.org/abs/2508.02348  
   Category: Radar / RF / mmWave NLOS; localization; autonomous driving.  
   Contribution: uses camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization at T-junctions, complementing the repository's radar NLOS detection/localization entries.

No final accepted/published venue was verified for these three papers during this run, so they should be labeled as **arXiv** until a final venue is confirmed.

## Files safely updated

- `article/5newscenes.tex`  
  Added MITO and mmWave pedestrian localization to the Radar/RF/mmWave subsection, and added a new `Low-Cost LiDAR NLOS Spatial Reasoning` subsection integrating DENALI with the consumer-LiDAR NLOS thread.

- `egbib_2026_updates.bib`  
  Added BibTeX entries for DENALI, MITO, and mmWave pedestrian localization; also corrected the GeRaF 2.0 BibTeX author metadata to match the arXiv record.

## README / website patch still to apply

The GitHub contents API wrapper available in this environment only supports complete text replacement for large files. To avoid truncating or corrupting `README.md` or `index.html`, this run did **not** overwrite those large files. Apply the following safe patch when direct repository editing or a normal git checkout is available.

### README.md

In `Latest Additions`, insert near the 2026 consumer-LiDAR entries:

```markdown
| 2026 | [DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs](https://arxiv.org/abs/2604.16201) — Behari et al. | arXiv 2026 | Releases 72,000 real low-cost-LiDAR space-time-histogram hidden-object scenes, enabling data-driven NLOS spatial reasoning beyond smartphone-LiDAR reconstruction. |
```

Insert near the 2025 RF/mmWave entries:

```markdown
| 2025 | [MITO: Enabling Non-Line-of-Sight Perception using Millimeter-waves through Real-World Datasets and Simulation Tools](https://arxiv.org/abs/2502.10259) — Dodds et al. | arXiv 2025 | Provides real multi-spectral mmWave LOS/NLOS images and simulation tools for learning-based through-occlusion / NLOS perception. |
| 2025 | [mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera](https://arxiv.org/abs/2508.02348) — Park et al. | arXiv 2025 | Uses camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization in urban driving. |
```

In `Milestone Timeline`, extend the 2025 line with MITO and NLOS pedestrian localization, and the 2026 line with DENALI.

In `New NLOS Scenes and Modalities`:

- Add DENALI to `ToF Camera / LiDAR` or a new low-cost-LiDAR subsection.
- Add MITO and Park et al. to `Radar / RF / mmWave NLOS`.
- Add DENALI to `Datasets and Open-Source Code`.

### index.html

Recommended updates:

- Change latest-entry count from `23` to `26`.
- Add DENALI, MITO, and Park et al. to the `papers` array with categories `latest dataset active modality`, `latest dataset modality`, and `latest modality`, respectively.
- Extend the 2025 and 2026 timeline text to mention mmWave datasets/localization and low-cost-LiDAR NLOS spatial reasoning.
- Add `DENALI`, `MITO`, and `mmWave pedestrian` to the search placeholder.

## Survey/PDF build status

The survey source has been updated through `article/5newscenes.tex` and `egbib_2026_updates.bib`, but the PDF was not regenerated in this environment. The build still requires the bibliography line in `bare_jrnl.tex` to be changed from:

```tex
\bibliography{egbib}
```

to:

```tex
\bibliography{egbib,egbib_2026_updates}
```

Then run the normal LaTeX/BibTeX build and commit the refreshed `bare_jrnl.pdf`.
