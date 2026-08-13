# 13 August 2026 — acoustic ANLOS-R gap

> **Resolved:** integrated into public artifacts and rebuilt survey PDF on 13 August 2026.


A fresh recent-literature and forward-citation pass found one high-confidence missing paper:

**Dilan Onat Alakuş and İbrahim Türkoğlu, “Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net and Multimodal Fusion With the ANLOS-R Dataset,” IEEE Access, vol. 14, pp. 26983–27004, 2026. DOI: 10.1109/ACCESS.2026.3664294.**

The final venue, volume, pages, DOI, and authors were verified against Crossref-backed ORCID metadata and the first author's institutional publication record. The paper introduces ANLOS-R: 1,440 wall-mediated acoustic NLOS echo samples from an 8-speaker/8-microphone setup at three sensor positions, plus an attention-U-Net reflection-isolation stage and multimodal spectral-temporal material-classification pipeline.

This is distinct from the already-covered Sensors 2026 follow-up, “Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion” (DOI 10.3390/s26051577). The current survey describes ANLOS-R while citing only the later Sensors work, so the IEEE Access paper should be added as the dataset/multimodal-method precursor and the Sensors paper retained as the wavelet-feature/SHAP extension.

The broader pass did not identify another stronger missing 2026 paper: learned LCT, PICL, TransVID, diffuse-aware passive NLOS, stereo NLOS, arbitrary-relay CUDA reconstruction, Super-FoV, consumer-LiDAR NLOS, DENALI, HoloRadar, passive relay-free acoustic localization, and rough-wall thermal NLOS are already present in the current repository.

## Safe-update limitation

The available GitHub write action replaces existing UTF-8 files wholesale, while large live files are returned through the connector in truncated form. To avoid overwriting README, index, survey source, or the merged bibliography from partial content, this run stages the verified BibTeX entry in `egbib_20260813_acoustic_anlos_r_gap.bib` and records the exact public-artifact edits below.

## README.md

In `## Latest Additions`, add:

```markdown
| 2026 | [Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net and Multimodal Fusion With the ANLOS-R Dataset](https://doi.org/10.1109/ACCESS.2026.3664294) — Alakuş and Türkoğlu | IEEE Access 14, 26983–27004 (2026) | Introduces ANLOS-R, a 1,440-sample wall-mediated acoustic NLOS dataset collected with an 8-speaker/8-microphone multi-position setup, together with attention-U-Net reflection isolation and multimodal spectral-temporal fusion for hidden-material recognition. It is the dataset/multimodal precursor to the later Sensors 2026 wavelet-feature follow-up. |
```

Also place it adjacent to the existing Sensors 2026 Alakuş–Türkoğlu entry in the acoustic/new-modality list.

## index.html

Add this object beside the existing acoustic material-recognition record:

```javascript
{cat:"latest modality acoustic dataset learning recognition semantic",title:"Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net and Multimodal Fusion With the ANLOS-R Dataset",authors:"Alakuş and Türkoğlu",year:2026,venue:"IEEE Access 14, 26983–27004 (2026)",url:"https://doi.org/10.1109/ACCESS.2026.3664294",key:"Introduces the 1,440-sample ANLOS-R wall-mediated acoustic dataset and an attention-U-Net reflection-isolation plus multimodal spectral-temporal fusion pipeline for hidden-material recognition; it precedes the later Sensors 2026 wavelet-feature study."},
```

Revise the 2026 timeline acoustic-semantic sentence so it says that ANLOS-R established the measured multi-position dataset and reflection-isolation/fusion pipeline, while the Sensors follow-up reused the dataset with wavelet-acoustic features, recurrent models, and SHAP interpretation.

## article/5newscenes.tex

In `Acoustic NLOS Imaging`, revise the current `Material recognition from wall-mediated acoustic echoes` paragraph into a two-paper progression:

1. Cite `alakusANLOSR2026` for the ANLOS-R dataset, 8×8 speaker/microphone acquisition, three sensor positions, 1,440 samples, attention-U-Net reflection isolation, and multimodal spectral-temporal fusion.
2. Keep `alakusAcousticMaterialNLOS2026` for the subsequent Sensors study's 70-dimensional wavelet-acoustic feature representation, recurrent classifiers, and SHAP analysis.

Suggested literature-review wording:

```latex
Alaku{\c{s}} and T{\"u}rko{\u{g}}lu first introduced ANLOS-R as a dedicated multi-channel acoustic NLOS dataset and semantic-sensing benchmark~\cite{alakusANLOSR2026}. The acquisition uses eight loudspeakers and eight microphones facing a relay wall while the direct path to the target is blocked, records three sensor positions and single-channel, combined/MIMO, and background measurements, and contains 1,440 echo samples. Their accompanying pipeline isolates target-related reflection regions with an attention-enhanced U-Net and fuses spectral and temporal representations for material classification. Building on the same acquisition, the subsequent Sensors study~\cite{alakusAcousticMaterialNLOS2026} combines classical acoustic descriptors with multi-scale wavelet energy and entropy, uses recurrent models for hidden-material recognition, and adds SHAP-based interpretation. Together, the two works extend acoustic NLOS from localization and geometry toward dataset-driven material-aware perception.
```

## bare_jrnl.tex and bibliography

Add a top synchronization comment noting the 13 August 2026 ANLOS-R integration. Merge `egbib_20260813_acoustic_anlos_r_gap.bib` into `egbib_merged_20260711.bib` with key `alakusANLOSR2026`, after checking DOI/key uniqueness.

## PDF status

`bare_jrnl.pdf` was not regenerated in this run because the public source patch could not be safely applied without risking large-file truncation. After merging the source edits, rebuild the survey with the repository's normal LaTeX/BibTeX workflow and verify that README, index, survey text, bibliography, and PDF all contain the IEEE Access paper exactly once and retain the Sensors follow-up separately.
