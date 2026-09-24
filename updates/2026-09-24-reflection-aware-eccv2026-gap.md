# Integration note — Reflection-Aware Reasoning for NLOS Pedestrian Localization

Verified missing paper found on 2026-09-24:

- Byeonggyu Park, Mingu Jeon, Seong-Woo Kim, “Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization,” ECCV 2026, DOI: 10.1007/978-3-032-37356-4_7, arXiv:2609.27346.
- Final venue is verified as ECCV 2026 (Springer proceedings, Part LI), so do not label the venue as arXiv.
- Project page: https://bingurrr.github.io/reflection-aware-nlos/

## Why it belongs

This is a genuine RF/mmWave NLOS sensing paper rather than a generic occlusion paper. It uses 77-GHz automotive radar multipath as hidden-target evidence, fuses radar point clouds with front-view camera features to infer reflection order and reflective-surface structure in BEV, and applies physics-guided ray tracing/geometric mirroring to undo multipath distortion and localize pedestrians hidden around corners. It extends prior static automotive radar NLOS localization to a moving ego-vehicle and reports real outdoor evaluation (120 scenarios, 12,539 frames; 1.23-m localization accuracy on the project page).

## Canonical integration locations

1. README.md: add under RF/mmWave / multimodal NLOS sensing and the 2026 development timeline. Concise summary: “Extends automotive mmWave NLOS localization to moving ego-vehicles by fusing camera/radar features to infer reflection type and reflective surfaces, then unfolding multipath with physics-guided ray tracing; validated in real outdoor driving scenes.”
2. index.html / Paper Explorer: add as ECCV 2026, tags `RF/mmWave`, `automotive`, `multimodal`, `localization`, `physics-guided`, and include it in Latest Additions and the 2026 timeline.
3. bare_jrnl.tex: integrate semantically in the RF/mmWave / emerging modalities discussion, after earlier around-the-corner mmWave and automotive NLOS localization works. Emphasize the trajectory from static geometry-assisted multipath localization to reflection-aware, ego-dynamic radar-camera reasoning.
4. Canonical bibliography: merge the verified BibTeX staged in `egbib_20260924_reflection_aware_eccv2026.bib` and deduplicate any arXiv-only entry.
5. Rebuild bare_jrnl.pdf after source integration and verify README/index/TeX/bibliography/PDF consistency.

Large canonical files were not overwritten from partial payloads in this run; this note is intentionally a safe patch-style staging record.
