# Survey integration update — 28 June 2026

This update mirrors the recent citation-tracing additions into the LaTeX survey source while avoiding unsafe overwrites of large repository files.

## Source files updated

- `article/5newscenes.tex`
  - Added an **Active Corner Cameras** subsection for Seidel et al., *Nature Communications* 2023.
  - Added a **Robotic Exploration with NLOS Perception** subsection for SuperEx.
  - Added a **Terahertz NLOS Imaging** subsection for Cui and Trichopoulos.
  - Expanded **Radar-Based NLOS Imaging** to include N2LoS, distributed MIMO/ISAC NLOS imaging, and RIS-assisted around-corner radar.
  - Expanded **Acoustic NLOS Imaging** to include relay-free passive acoustic NLOS localization.

- `article/6conclusion.tex`
  - Added survey-level synthesis covering picosecond temporal resolution, TRT, MARMOT, NANO, mitransient, structure-sparsity regularization, Quasi-Fresnel Transform, event-camera NLOS, RF/mmWave/ISAC, relay-free acoustic NLOS, SuperEx, arbitrary relay geometries, active corner cameras, and 3D Gaussian Transient Rendering.

- `egbib_2026_updates.bib`
  - Added BibTeX entries for the newly integrated and recently added 2021--2026 papers.

## Papers covered by this survey integration

| Year | Paper | Venue / Status | Survey placement |
|------|-------|----------------|------------------|
| 2021 | Non-line-of-sight imaging with picosecond temporal resolution | Physical Review Letters 2021 | Conclusion / fundamental-resolution progress |
| 2022 | Seeing Around Obstacles with Terahertz Waves | arXiv 2022 | New scenes / THz NLOS |
| 2022 | Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera | arXiv 2022 | Conclusion / event-camera passive NLOS |
| 2023 | Non-line-of-sight snapshots and background mapping with an active corner camera | Nature Communications 2023 | New scenes / active corner cameras |
| 2023 | Non-line-of-sight reconstruction via structure sparsity regularization | arXiv 2023 | Conclusion / reconstruction infrastructure |
| 2024 | Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding | arXiv 2024 | Conclusion / event-camera passive NLOS |
| 2024 | Soft Shadow Diffusion | ECCV 2024 | Bibliography supplement |
| 2025 | MARMOT: Masked Autoencoder for Modeling Transient Imaging | arXiv 2025 | Conclusion / deep learning advances |
| 2025 | 3D Reconstruction from Transient Measurements with Time-Resolved Transformer | arXiv 2025 | Conclusion / deep learning advances |
| 2025 | Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging | arXiv 2025 | Conclusion / deep learning advances |
| 2025 | Passive acoustic non-line-of-sight localization without a relay surface | arXiv 2025 | New scenes / acoustic NLOS |
| 2025 | SuperEx: Enhancing Indoor Mapping and Exploration using Non-Line-of-Sight Perception | arXiv 2025 | New scenes / robotic exploration |
| 2025 | mitransient: Transient light transport in Mitsuba 3 | arXiv 2025 | Conclusion / rendering infrastructure |
| 2025 | N2LoS: Single-Tag mmWave Backscatter for Robust NLOS Localization | arXiv 2025 | New scenes / radar-RF-mmWave |
| 2026 | RIS-assisted around-corner radar sensing | arXiv 2026 | New scenes / radar-RF-mmWave |
| 2026 | NLOS-aided distributed MIMO/ISAC off-grid imaging | arXiv 2026 | New scenes / radar-RF-mmWave |
| 2026 | Consumer LiDAR NLOS via motion-induced sampling | Nature 2026 | Bibliography supplement / conclusion context |
| 2026 | GeRaF 2.0 radar NLOS 3D reconstruction | CVPR 2026 | Conclusion / radar-RF-mmWave |
| 2026 | 3D Gaussian Transient Rendering for arbitrary relay geometries | SIGGRAPH 2026 | Conclusion / arbitrary relay geometry |

## Remaining safe patch steps

The main `bare_jrnl.tex` currently uses:

```tex
\bibliography{egbib}
```

To compile with the new bibliography supplement, change it to:

```tex
\bibliography{egbib,egbib_2026_updates}
```

This run did not directly replace `bare_jrnl.tex` because large-file replacement through the connector requires supplying the complete file and risks accidental truncation if any fetched content is clipped. The article source files have nevertheless been updated, and the new bibliography supplement is present.

## README consistency patch

The interactive homepage already includes the citation-tracing additions. The README should still mirror the citation-tracing update note by adding the six rows from `updates/2026-06-27-citation-tracing.md` to `Latest Additions`, inserting them into the timeline/category sections, and correcting the venue of "Non-line-of-sight imaging with arbitrary illumination and detection pattern" to **Nature Communications 2023**.

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The available execution environment did not provide a usable local shell/LaTeX compilation path, and the GitHub connector path used here safely updates text files but does not compile LaTeX or upload a regenerated binary PDF. The source-level survey integration has been committed; the remaining manual/CI step is to compile the PDF after applying the bibliography-line change above.
