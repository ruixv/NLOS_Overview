# 2026-10-16 NLOS survey source reconciliation

## Scope and literature status
Reviewed the existing README, website paper explorer, bibliography, and included LaTeX chapters against the 2026-10-15 staging audit. Checked recent active, passive, transient, acoustic, and RF/mmWave NLOS results and representative forward-citation lineages (LCT, f-k migration, phasor fields, computational periscopy). No additional publication was confirmed as missing from the public paper catalog during this pass.

## Corrected staging diagnosis
The prior staging note called for nine missing citation keys, but two were aliases of already-cited works, **not new survey gaps**:
- `rajiSoftShadowDiffusion2026` is the 2026 arXiv posting of the **ECCV 2024** Soft Shadow Diffusion paper already cited under `rajiSoftShadowDiffusion2024`. arXiv explicitly identifies ECCV 2024 as its journal reference.
- `wangDAAMPassiveNLOS2026` and the already-cited `wangDiffuseAwarePassive2026` share DOI **10.1364/OE.601398**. The latter already appears in the passive survey.

Accordingly, **seven distinct works** required missing-prose backfill. The integrated chapter changes are:
- `article/3passive.tex`: structure-guided adaptive total variation, `zhangSGATVPassiveNLOS2026`.
- `article/4datadriven.tex`: frequency-domain multi-regularization experts, `zhangFMoENLOS2026`.
- `article/2active.tex`: reference-function non-confocal phase compensation `yuFrequencyDomainPhaseNLOS2026`; geometry-constrained reconstruction `liuGeometryConstrainedNLOS2026`; scanning-free laser reflective tomography `wangLRTNLOS2026`; predistorted FMCW LiDAR `qianHighSpeedNLOSFMCW2026`; and finite-aperture yaw observability `romanelliFiniteApertureNLOS2026`.

## Bibliography reconciliation
- `yeThermalRoughNLOS2026` and `yeThermalNLOSFormer2026`: ACM TOG 45(5), Article **173** (not 41), DOI 10.1145/3811030.
- Legacy alias `rajiSoftShadowDiffusion2026` now carries the verified **ECCV 2024** publication record, DOI 10.1007/978-3-031-72989-8_22, instead of treating the later arXiv upload as a new 2026 paper. The established 2024 citation key remains unchanged.
- Both aliases for diffuse-aware attention remain available for backward compatibility, but only the already-cited `wangDiffuseAwarePassive2026` is used in the survey.

## Public-artifact and PDF status
All seven works were already present in README and the paper explorer, so no duplicate paper records were added. `bare_jrnl.tex` includes the changed chapter files through existing `\\input` directives. The survey PDF **must be rebuilt** after merging the source updates: the existing PDF is stale and is not claimed to contain the newly integrated prose. A complete checkout with figures and bibliography is required. Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`; verify no undefined citations or duplicate BibTeX keys, then commit the resulting `bare_jrnl.pdf`. This run could not obtain the complete repository in the local container because external GitHub DNS resolution failed.

## Verified metadata
- ACM publisher: https://doi.org/10.1145/3811030
- arXiv version and explicit ECCV 2024 journal reference: https://arxiv.org/abs/2601.12257
- ECCV proceedings: https://doi.org/10.1007/978-3-031-72989-8_22
- Optics Express diffuse-aware attention: https://doi.org/10.1364/OE.601398
- Journal of Imaging finite-aperture analysis: https://doi.org/10.3390/jimaging12060248
