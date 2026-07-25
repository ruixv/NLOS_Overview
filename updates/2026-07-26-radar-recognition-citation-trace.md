# 26 July 2026 measured multipath radar recognition update

## Scope

This pass followed the forward-citation and related-work chains around street-corner radar, HoloRadar, multipath exploitation, RF/mmWave NLOS localization, and semantic hidden-scene understanding. Candidates were retained only when measured NLOS propagation was central to the sensing task rather than a incidental test condition.

## Verified missing records

1. **Non-Line-of-Sight Target Recognition Method Based on Multi-Scale Feature Fusion** — Xiaolu Zeng, Yifei Yang, Han Zhao, Shichao Zhong, Xiaopeng Yang. *Journal of Signal Processing* 42(3), 357–370 (2026). DOI: `10.12466/xhcl.2026.03.006`.
   - A measured 15 GHz stepped-frequency radar captures multipath and local-scattering signatures through concrete and wooden walls.
   - Adaptive multi-scale residual convolutions and attention fuse high-amplitude single-path cues with broader multipath structure, classifying four hidden target types with 99.6% accuracy.
   - The work is semantic NLOS target recognition, not hidden-shape or 3D reconstruction.

2. **Multipath Contrastive Learning for Non-line-of-sight Human Activity Recognition Using an Ultrawideband Radar** — Xiaoling Zhong, Junlin Zhou, Yong Jia, Qingxi Zhu, Guangle Yao, Shi Yi. *Journal of Radars*, Online First (2026). DOI: `10.12000/JR25241`.
   - MuPhyCoNet uses separated multipath time-frequency observations as physically meaningful positive views for self-supervised contrastive learning.
   - Observation- and prediction-level physics constraints improve sample efficiency; the measured 19,500-spectrogram dataset reports 94.32% six-action accuracy with only 10% labels.
   - This extends RF NLOS toward human-activity understanding while remaining a semantic sensing task rather than full scene imaging.

## Integration map

- `README.md`: add both DOI-linked records and two 2026 semantic-radar timeline milestones.
- `index.html`: add two searchable records, increase the tracked-entry total by two, extend the 2026 timeline, and synchronize the footer date.
- `article/5newscenes.tex`: add a radar-semantic-sensing paragraph after the existing detection/localization discussion.
- `article/4datadriven.tex`: connect multipath-aware target/activity recognition to the survey's recognition and physics-informed representation-learning trajectory.
- `egbib_merged_20260711.bib`: add DOI-verified records with stable citation keys.
- `bare_jrnl.tex`: add a trace marker while preserving the survey structure.
- `bare_jrnl.pdf`: clean-build only after source, citation, JavaScript, and bibliography checks pass.

The newest independently date-verified direct NLOS imaging publication remains **Iterating the transient light transport matrix for non-line-of-sight imaging**, published online by *Nature Communications* on 22 July 2026. The two records in this batch expand the semantic RF branch rather than superseding that publication date.
