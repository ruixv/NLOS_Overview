# 25 October 2026 — citation-tracing and cross-artifact consistency audit

## Outcome

No new high-confidence NLOS imaging paper was found that is absent from the current public corpus. The main finding is a consistency cleanup: all unique recent candidates identified through keyword searches and forward-citation checks were already represented in the README, Paper Explorer, survey, and active bibliography under canonical or legacy citation keys.

## Citation-tracing pass

The targeted forward-citation pass used the field-defining optical seeds (Velten 2012, O'Toole/LCT 2018, Lindell/f-k migration 2019, Liu/phasor fields), passive computational periscopy, and newer learned/modal papers. Scholarly indexes and publisher records were used to distinguish relevant NLOS reconstruction or tightly adjacent sensing from papers that merely cite NLOS in background. Representative verified works already covered include:

- TransiT — ICCV 2025, transient-transformer NLOS videography.
- Time-Resolved Transformer (TRT) — arXiv:2510.09205; no final venue was verifiable in this run.
- Noise-adapted Neural Operator — arXiv:2508.09655; no final venue was verifiable in this run.
- TransDiff — IEEE Transactions on Image Processing 34 (2025), 8018–8031.
- Adaptive artifact cancellation — Optics and Laser Technology 182 (2025), 112081; its reference list includes Velten, LCT-related, and phasor-field work.
- Adaptive mixture-distribution attention — IEEE Signal Processing Letters 32 (2025), 1690–1694.
- Adaptive spiral confocal scanning — IEEE Open Journal of Signal Processing 7 (2026), 482–491.
- Thermal NLOS through rough surfaces — ACM Transactions on Graphics 45(5), Article 173 (2026).
- GeRaF 2.0 / “Seeing through boxes” — CVPR 2026.
- Passive acoustic NLOS localization without a relay surface — Physical Review Applied 25, 024064 (2026), DOI 10.1103/p97k-sf71.
- Photonic sensing of hidden vital signs — Optica 13(9), 1742–1750 (2026), an adjacent physiological sensing task rather than dense 3D imaging.
- Open-pit 4D mmWave radar/LiDAR fusion — Sensors 26(14), 4615 (2026), an NLOS perception/risk-cue method rather than full object reconstruction.

The passive acoustic paper was checked against the publisher's final record and its cited references, which include Velten 2012, O'Toole 2018 LCT, Lindell 2019 f-k migration, and Liu et al.'s phasor-field work. The arXiv record is retained as provenance elsewhere, but the public venue is correctly Physical Review Applied.

## Bibliography cleanup

- Removed the unused arXiv-only alias `sommerPassiveAcousticNLOS2025` from the active merged bibliography; the survey cites the verified final-venue record `sommerPassiveAcousticNLOS2026`.
- Removed the unused duplicate-key alias `yangOpenPitNLOS2026`; the same DOI is already represented and cited as `yangMiningRadarLiDARNLOS2026`.
- No cited keys were removed. The canonical final-venue entries remain available in `egbib_merged_20260711.bib`.

## PDF status

After this consistency-only patch, the clean-build workflow [run #40202864838](https://github.com/ruixv/NLOS_Overview/actions/runs/40202864838) completed successfully on 25 October 2026. The regenerated PDF is **71 pages** (2,389,572 bytes), committed at [`04e71bd`](https://github.com/ruixv/NLOS_Overview/commit/04e71bdb7a42011f315c5d4dbe16b571fbb3aa03) with blob SHA `e32263bf052cba389436d95fd2834c2a7ee5df65`. The workflow passed clean LaTeX compilation, PDF validation, citation-key checks, and bibliography checks; no undefined citations or missing BibTeX entries were found. The README and Paper Explorer already covered the relevant papers, so no paper-list additions were necessary.
