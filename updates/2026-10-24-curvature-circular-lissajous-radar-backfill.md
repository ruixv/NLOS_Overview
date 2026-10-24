# 2026-10-24: Core-paper citation trace and optical/radar NLOS backfill

This update closes six verified historical gaps discovered through selective forward-citation/reference tracing of core transient-imaging and NLOS-reconstruction papers (including LCT, phasor field, circular transient sinograms and recent optical inverse-reconstruction papers), plus a targeted radar/ISAR bibliography search. All six directly concern hidden-scene reconstruction or hidden moving-target imaging, not generic multipath communications.

| Venue/year | DOI | Contribution | Survey location |
| --- | --- | --- | --- |
| IEEE TPAMI 46(12), 8474–8485 (2024) | 10.1109/TPAMI.2024.3409414 | Ding et al., object/joint-domain curvature regularization and GPU ADMM under sparse active-NLOS sampling. Existing BibTeX reused. | `article/2active.tex`: *Curvature priors for under-sampled inverse imaging* |
| IEEE ICIP, 2751–2757 (2024) | 10.1109/ICIP51287.2024.10648011 | Yang and Isogawa, E-C2NLOS transient-sinogram super-resolution for circular scanning. | `article/2active.tex`: *Adaptive spiral relay-wall sampling* |
| SPIE 13104, 1310457 (2024) | 10.1117/12.3023661 | Wang et al., extended imaging distance with resolution considerations. | `article/2active.tex`: *Extended-range relay acquisition* |
| IEEE TGRS 62, 1–18 (2024) | 10.1109/TGRS.2024.3447900 | Wen et al., detail-aware sparse-aperture moving-target ISAR NLOS imaging. Existing BibTeX reused. | `article/5newscenes.tex`: *Sparse-aperture and moving-target radar imaging* |
| SPIE 13542, 1354210 (2025) | 10.1117/12.3055473 | Wang et al., Lissajous structured confocal scanning. | `article/2active.tex`: *Adaptive spiral relay-wall sampling* |
| IEEE TVT 74(1), 179–190 (2025) | 10.1109/TVT.2024.3398218 | Wen et al., CMTI polar-format/autofocus hidden moving-target radar imaging. | `article/5newscenes.tex`: *Sparse-aperture and moving-target radar imaging* |

The README latest-additions table and development timeline, the website Core Reading Path, and the searchable Paper Explorer/timeline were updated with all six entries. `bare_jrnl.tex` includes both modified chapters and the merged bibliography (`egbib_merged_20260711.bib`). Four new verified BibTeX entries were added; the TPAMI and TGRS papers had reliable existing entries but were previously absent from the survey text and public-facing listings. Final published venues are used, not arXiv.

**PDF publication checkpoint — VERIFIED:** GitHub Actions [run 40077778125](https://github.com/ruixv/NLOS_Overview/actions/runs/40077778125) completed successfully on 24 October 2026 at 08:24 UTC. The clean LaTeX build generated a validated **70-page** survey, ran bibliography/citation checks, and successfully committed the binary to `master` at [`bcafd39`](https://github.com/ruixv/NLOS_Overview/commit/bcafd39b8fd95c2522d36d2f222363cd5c880680). The PDF Git blob SHA changed from `1669471a8dcb82179467d87ef104b5c1cc5d45a1` to **`864a8e65d3ad263b1c9a1f1419baa9c5bc4b6760`**. The six added survey citations and their four newly added bibliography entries are now included in the newly rebuilt PDF. The survey remains a project-maintained companion rather than a newly peer-reviewed journal revision.

This is a selective citation/reference trace, not an exhaustive sweep of every forward citation to all core papers.
