# Radar/acoustic NLOS citation-trace update — 22 August 2026

This run combined recent publisher/project/lab-page searches with forward-citation and lineage tracing from the repository's established optical, radar, and acoustic NLOS milestones. Three high-confidence missing works were verified:

1. Xiaonan Wang, Zhe Chen, and Fuliang Yin, **A dual-branch fusion network for footstep sound source localization in non-line-of-sight corridors**, *The Journal of the Acoustical Society of America* 160(2), 1400–1412 (2026), DOI `10.1121/10.0044386`. CorridorLocNet fuses Mel-spectrogram and GCC-PHAT features with residual-CNN and lightweight-Conformer branches plus cross-attention, using a real around-corner footstep dataset.
2. Hee-Yeun Kim et al., **Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation**, *IEEE/RSJ IROS 2025*, 21352–21359, DOI `10.1109/IROS60139.2025.11246930`. The final conference record supersedes the arXiv-only version.
3. Byeonggyu Park, Mingu Jeon, and Seong-Woo Kim, **Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization**, accepted to *ECCV 2026*. The project page and independent lab publication lists verify acceptance; proceedings DOI/pages were not yet public, so the repository uses the accepted final venue plus project page without fabricating missing metadata.

The audit also found a cross-artifact consistency gap for Jeon et al., **Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar**, *IEEE IV 2025*, DOI `10.1109/IV64158.2025.11097630`: it was already present in the canonical website corpus and merged bibliography, but not in the radar survey prose. This integration closes that gap.

The automotive radar narrative is now: measured multi-target T-junction ray tracing → camera-conditioned road-layout interpretation → temporary parked-vehicle/darting-out geometry → reflection-aware ego-dynamic multimodal reasoning. The acoustic narrative is extended from physics-explicit edge diffraction and passive vehicle tracking to learned corridor-multipath spatial fingerprints.

The guarded workflow rebuilds `bare_jrnl.pdf`, checks the new citations in `.aux/.bbl`, validates README / `data/papers-source.html` / survey / bibliography consistency, and renders relevant PDF pages before the public changes are committed.
