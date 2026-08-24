# Eye-safe optical localization and NLOS pose-estimation gaps — 24 August 2026

A fresh recent-paper search plus Core-paper/citation-lineage pass identified two final-venue 2026 NLOS papers that are not present in the current README, canonical V2 paper corpus, survey source, or merged bibliography.

## 1. Eye-safe compact active NLOS localization

- Konstantin Albert, Julian Klein, Manuel Ligges, Anton Grabmaier, “Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays,” *Journal of the European Optical Society-Rapid Publications*, 22(1), article 40, 2026. DOI `10.1051/jeos/2026019`.
- Final venue verified from the journal page: published online 19 May 2026.
- Technical role: replaces the usual bulky femto/picosecond scanned source with inexpensive nanosecond laser diodes and a parallel 24×32 SPAD array with per-pixel timing. Two off-axis illumination positions reduce pulse-width-induced localization uncertainty; matched filtering compensates the long laser pulse, and the paper proposes a practical hybrid LiDAR–NLOS calibration path.
- This is directly relevant to the LCT/f-k/phasor-field hardware lineage because it targets the same transient inverse problem while moving the acquisition stack toward eye-safe, scan-free, compact deployment.
- Canonical BibTeX key: `albertEyeSafeNLOS2026`.

## 2. Low-SNR semantic NLOS human pose estimation

- Zhongpei Xiao, Chen Dai, Ruilin Ye, Jianwei Zeng, Wenwen Li, Feihu Xu, “Non-line-of-sight human pose estimation,” *Optics and Lasers in Engineering*, 201, 109658, 2026. DOI `10.1016/j.optlaseng.2026.109658`.
- Final venue verified from Elsevier/Crossref metadata; June 2026 issue.
- Technical role: task-specific semantic NLOS sensing. The method reconstructs a hidden volume, jointly extracts depth/intensity features, and predicts 3D human keypoints with a multi-stage deep network. A physics-based data-generation pipeline synthesizes large-scale training data from smartphone videos. The paper reports robust pose estimation down to SNR 0.13 and target depths up to 1.75 m from the relay surface.
- The paper explicitly cites the field-defining active NLOS lineage, including Velten et al. and Lindell et al. f-k migration, and should be placed after earlier optical NLOS pose works such as Isogawa et al. CVPR 2020 / HiddenPose rather than treated as generic computer-vision pose estimation.
- Canonical BibTeX key: `xiaoNLOSHumanPose2026`.

## Recommended public integration

1. **README.md / Latest Additions** — add both final journal records with DOI links and concise contribution summaries.
2. **README.md / timeline** — add the eye-safe paper to the 2026 active-hardware/practical-deployment branch (`picosecond scanned systems → SPAD arrays / scan-free capture → compact eye-safe nanosecond localization`) and the pose paper to the semantic branch (`transient reconstruction → NLOS human pose inference → low-SNR task-specific semantic sensing`).
3. **data/papers-source.html** — add one canonical paper object for each paper and update the 2026 timeline; recompute the tracked-entry count from the paper array.
4. **article/2active.tex** — integrate Albert et al. into the practical active-system / SPAD-array acquisition discussion, emphasizing eye safety, nanosecond sources, parallel non-confocal detection, matched filtering, and localization rather than full dense shape recovery.
5. **article/4datadriven.tex** — integrate Xiao et al. after earlier human-pose / semantic transient NLOS work, highlighting depth–intensity feature fusion, physics-based synthetic training data, and low-SNR pose inference.
6. **egbib_merged_20260711.bib** — merge `albertEyeSafeNLOS2026` and `xiaoNLOSHumanPose2026` exactly once. Staging entries are in `egbib_20260824_eye_safe_pose_gap.bib`. Verify DOI/key uniqueness.
7. **bare_jrnl.tex / bare_jrnl.pdf** — update the survey provenance date only after the source edits above are complete; clean-build with `pdflatex → bibtex → pdflatex → pdflatex` (or equivalent), verify both citation keys in `.aux/.bbl`, confirm both contributions survive PDF text extraction, render-check at least the affected pages plus first/last pages, then commit the rebuilt PDF.

## Scope decisions

- `NLOS-MT`, MARMOT, Learned LCT, PICL, Stereo NLOS, 3D Gaussian Transient Rendering, all-day Si-SPAD, and the recent passive/thermal/RF additions were rechecked and are already represented in the repository; do not duplicate them.
- The already-staged `Joint Localization of LOS and NLOS Targets With Clutter Mitigation via Multipath Exploitation Radar` is a separate RF gap and should remain in its own integration lineage.
- Because multiple guarded integrations are currently touching the same large public artifacts, this run intentionally uses the repository's patch-style fallback instead of whole-file replacement. No claim is made that README/V2/survey/PDF already contain these two papers.
