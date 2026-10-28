# 28 October 2026 — NLOS literature and citation-tracing update

## Newly integrated items

- **Doppler-aided Position-Velocity Tracking of Hidden Objects using mmWave Radar** — Yerin Cheon, Kush Garg, and Akshat Dave; arXiv:2610.34085, submitted 25 October 2026. The preprint retains sequential range–azimuth–Doppler measurements, predicts position and velocity separately with recurrent temporal branches, and introduces 576 sequences / 720,856 frames with synchronized ground truth. No final conference or journal venue was verifiable on 28 October 2026. It is categorized as adjacent mmWave NLOS sensing/tracking, not dense 3D reconstruction.
- **Hybrid active-passive non-line-of-sight 3D color imaging via amplitude-color decomposition** — Xiaojie Shi et al.; *Photonics Research*, DOI [10.1364/PRJ.608001](https://doi.org/10.1364/PRJ.608001). Publisher metadata report acceptance on 14 October and online posting on 15 October 2026; volume/issue/pages remain pending. The record was already present in README and the merged bibliography but lacked a substantive discussion in the survey. Added that discussion to the New NLOS Scenes chapter.

## Citation-tracing pass

The new mmWave preprint's related-work section explicitly discusses the active optical milestones: Velten et al. (2012) experimental 3D reconstruction, O'Toole et al. (2018) confocal LCT, Lindell et al. (2019) fast f-k migration, and Liu et al. (2019) phasor-field virtual-wave optics. Its RF/NLOS lineage also includes CornerRadar (2022), scattered-mmWave indoor tracking (2024), Doppler radar tracking in the wild (2020), and 2026 radar reconstruction work. This makes it a verified forward-citation candidate rather than a superficial keyword match.

Keyword and publisher-index checks also revisited:
- *Cascaded Non-Line-of-Sight Imaging* — ACM TOG 45(6), Article 205 / SIGGRAPH Asia 2026; already covered in the survey and bibliography.
- *Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering* — SIGGRAPH 2026; already covered in the survey and bibliography.
- *Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction* — arXiv:2608.28183; already discussed in the active reconstruction section and bibliography.
- *Measurement-Adaptive Light-Cone Transform for Robust Non-Line-of-Sight Imaging* — arXiv:2610.22847; already covered.
- *High-resolution Fourier single-pixel non-line-of-sight imaging employing diffusion model* — *Optics and Lasers in Engineering* 201 (2026), Article 109724; already covered.
- *Transient Non-Line-of-Sight Temporal Super-Resolution Based on Temporal Decoupling* — DOI 10.1016/j.optlaseng.2026.110054; the publisher page was available, with the issue dated November 2026. Already covered; retained as the final journal record, not arXiv.

## Cross-artifact changes

- README latest additions: added the Doppler-aware tracking preprint and advanced the update date to 28 October.
- Website homepage and Paper Explorer: added the preprint with an explicit arXiv-only status; added a timeline milestone.
- Survey: integrated the Photonics Research hybrid color paper in the passive/appearance discussion and the new radar tracking preprint in the mmWave section.
- Bibliography: added `cheonDopplerPositionVelocityNLOS2026`; retained the existing DOI-backed `shiHybridActivePassiveColor2026`.
- PDF: rebuild/validation is tracked by [GitHub Actions run 40616025858](https://github.com/ruixv/NLOS_Overview/actions/runs/40616025858). The clean build and validation succeeded. The regenerated `bare_jrnl.pdf` is committed on `master` with blob SHA `12be7a3e5b9817bd9020a4671d6f5b0a6ffa6e58`.

## Scope decisions

General LoS/NLoS propagation classification and UAV TDOA localization were not added as imaging papers. The mmWave tracking preprint is included only as a clearly labelled adjacent NLOS sensing benchmark. Final venues were preferred wherever publisher records could be verified; arXiv is retained as venue only for the two preprints without a verified final venue.
