# Open-pit mmWave–LiDAR NLOS perception gap — 26 August 2026

A fresh recent-paper search plus RF/NLOS citation-lineage pass identified one final-venue 2026 paper that is not present in the current README, canonical V2 paper corpus, survey source, or merged bibliography.

## Verified missing paper

- Jianjian Yang, Yuyu Zhang, Zhiyao Zheng, and Yuyuan Zhang, “Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion,” *Sensors*, 26(14), 4615, 2026. DOI `10.3390/s26144615`.
- Final venue verified from the publisher record and PubMed/PMC; published 21 July 2026.
- Canonical BibTeX key: `yangOpenPitNLOS2026`.
- Staging BibTeX: `egbib_20260826_openpit_mmwave_lidar_gap.bib`.

## Why it belongs in the NLOS overview

This is not a generic multimodal-perception paper that merely uses the word “occlusion.” It explicitly treats severe non-line-of-sight blind spots in autonomous open-pit haulage, uses 4D mmWave radar to recover hidden-target evidence where LiDAR has no direct observations, and models multipath contamination as a primary obstacle. The proposed Blind-Spot Complementary Fusion (BSCF) framework suppresses multipath artifacts using geometric constraints, aligns radar and LiDAR, and selectively injects high-confidence radar evidence into LiDAR blind regions. The paper also introduces a Volume Recovery Rate (VRR) proxy to quantify hidden-region spatial evidence and validates the method in real mine scenes with large metallic occluders.

Its technical role is best described as **existence-level NLOS sensing / blind-region completion**, not dense hidden-scene imaging. It therefore fits the repository's RF/mmWave “new scenes / practical sensing” branch alongside automotive around-corner radar, HoloRadar, unknown-layout multipath localization, and other modality-expansion work.

## Recommended public integration

1. **README.md / Latest Additions** — add the final Sensors 2026 record with DOI link and a concise contribution summary emphasizing 4D mmWave–LiDAR fusion, multipath suppression, and hidden-target risk cues under complete LiDAR occlusion.
2. **README.md / development timeline** — add a 2026 RF/mmWave deployment node such as: `automotive / corridor NLOS radar → multimodal blind-region completion in unstructured open-pit scenes`.
3. **data/papers-source.html** — add one canonical paper object; family should be `rf`. Recompute the tracked-entry count from the corpus rather than manually guessing it.
4. **article/5newscenes.tex** — integrate into the radar/RF NLOS section after the automotive radar / multimodal reflection-reasoning lineage. Suggested literature-review role: extend NLOS radar from structured road/corner geometry to unstructured mining scenes where large metallic machines generate both true blind spots and severe multipath ghosts. Clarify that the goal is existence-level hidden-target evidence and blind-region completion rather than full dense image reconstruction.
5. **egbib_merged_20260711.bib** — merge `yangOpenPitNLOS2026` exactly once; verify DOI/key uniqueness and remove the staging `.bib` after successful integration.
6. **bare_jrnl.tex / bare_jrnl.pdf** — update the provenance date only after the source edits are complete. Clean-build with `pdflatex → bibtex → pdflatex → pdflatex` (or equivalent), verify `yangOpenPitNLOS2026` in `.aux/.bbl`, confirm the new RF/mmWave paragraph survives PDF text extraction, render-check the affected radar-survey page plus first/last pages, then commit the rebuilt PDF.

## Suggested concise contribution text

> Introduces a geometry-constrained Blind-Spot Complementary Fusion framework that combines 4D mmWave radar and LiDAR for NLOS perception in open-pit mines. The method suppresses strong multipath ghosts, aligns the heterogeneous point clouds, and injects high-confidence radar observations into LiDAR blind regions to provide hidden-target existence cues under extreme occlusion; a Volume Recovery Rate proxy quantifies recovered spatial evidence.

## Scope decision

The paper is included because it performs explicit NLOS hidden-target sensing using mmWave returns in regions with no LiDAR line of sight and treats multipath suppression as part of the inference pipeline. It should be categorized as **tightly adjacent NLOS sensing / RF modality expansion**, not as an optical NLOS reconstruction method.

Recent optical/transient candidates rechecked in the same pass—including Stereo NLOS, 3D Gaussian Transient Rendering, PICL, MD-NLOS, all-day Si-SPAD, Geometry-Constrained NLOS, DCEEM, and Neural Illumination Fields—are already represented in the repository or existing update lineage and should not be duplicated.

Because the public README, V2 corpus, survey source, merged bibliography, and PDF are large and have several pending guarded integrations, this run intentionally uses the repository's patch-style fallback instead of whole-file replacement. No claim is made that the public README/V2/survey/PDF already contains this paper.
