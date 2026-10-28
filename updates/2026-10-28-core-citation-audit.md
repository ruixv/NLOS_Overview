# NLOS core-citation and venue-consistency audit — 28 October 2026

## Scope and method

Performed a forward-citation pass seeded by the field-defining active ToF papers (Velten et al. 2012, O'Toole et al. 2018/LCT, Lindell et al. 2019/f-k migration, and Liu et al.'s phasor-field work), passive computational periscopy (Saunders et al.), PAC-Net/NLOS-Track, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, and modality-expansion milestones including acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Candidate checks used publisher pages, arXiv, DBLP, PubMed, OpenAlex-indexed records, and official conference/project pages. Each candidate was checked for an actual hidden-scene reconstruction or a clearly scoped adjacent NLOS sensing contribution, rather than mere citation in passing.

## Citation-traced candidates verified as already covered

- **Cascaded Non-Line-of-Sight Imaging** — ACM Transactions on Graphics 45(6), Article 205 / SIGGRAPH Asia 2026, DOI [10.1145/3842503](https://doi.org/10.1145/3842503). Uses higher-order fourth-/fifth-bounce information to extend ToF NLOS to more complex multi-corner scenes. Already represented in the README, paper explorer, active-NLOS survey prose, and final-venue bibliography.
- **A comprehensive study of time-of-flight non-line-of-sight imaging** — arXiv:2603.09548; no final venue verified. Compares ToF NLOS inverse methods under a common forward model and controlled hardware/photon-count conditions. Already cited in the active-NLOS survey section.
- **Geometry-Constrained Non-Line-of-Sight Imaging** — IEEE Transactions on Visualization and Computer Graphics 32(7), 6524–6536 (2026), DOI [10.1109/TVCG.2026.3684832](https://doi.org/10.1109/TVCG.2026.3684832). Adds shape-operator regularization for joint hidden-surface normal, albedo, and geometry recovery. Already integrated.
- **A model decomposition method for the real-time non-line-of-sight imaging (MD-NLOS)** — iScience 29(6), 115828 (2026), DOI [10.1016/j.isci.2026.115828](https://doi.org/10.1016/j.isci.2026.115828). Reformulates sparse transient inversion as non-negative LASSO with spectral filtering for efficient reconstruction. Already integrated.
- **Non-line-of-sight imaging via physics-informed cascade learning (PICL)** — Journal of the Optical Society of America A 43(9), E9–E18 (2026), DOI [10.1364/JOSAA.593401](https://doi.org/10.1364/JOSAA.593401). Separates SPAD-specific noise before physics-informed transient reconstruction. Already integrated.
- **Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering** — SIGGRAPH Conference Papers 2026, DOI [10.1145/3799902.3811137](https://doi.org/10.1145/3799902.3811137). Uses 3D Gaussian primitives and differentiable transient rendering for sparse, non-planar relay surfaces. Already integrated.
- **Transient video interpolation for dynamic non-line-of-sight imaging (TransVID)** — Optics Express 34(3), 4882–4894 (2026), DOI [10.1364/OE.580550](https://doi.org/10.1364/OE.580550). Diffusion-based interpolation densifies low-resolution, low-frame-rate transient videos. Already integrated.
- **Compact non-line-of-sight imager at long range** — Optics Express 34(9), 16911–16921 (2026), DOI [10.1364/OE.597084](https://doi.org/10.1364/OE.597084). Demonstrates kilometer-range daytime imaging with adaptive gating and a compact SPAD-based prototype. Already integrated.
- **Edge-aware dual-spectral NLOS imaging architecture** — Proceedings of SPIE 14177, 141777B (NDTA 2025; published 2026), DOI [10.1117/12.3109634](https://doi.org/10.1117/12.3109634). Fuses visible and LWIR observations for low-power edge reconstruction. Already integrated in the passive survey section and bibliography.
- **Ultrasound synthetic aperture non-line-of-sight imaging** — Communications Physics 8, 432 (2025), DOI [10.1038/s42005-025-02335-3](https://doi.org/10.1038/s42005-025-02335-3), and **Non-Line-of-Sight 3D Reconstruction with Radar (HoloRadar)** — NeurIPS 2025. Both modality expansions are already represented.

The repository also already covers the 2025 IEEE ICEE near-infrared raster-scanning system, passive MARMOT pretraining, and adjacent distributed-channel/HDC sensing. No newly verified citation-traced paper was found to warrant an additional catalog entry in this run.

## Consistency corrections applied

1. Repointed MARMOT citations in article/4datadriven.tex and article/5newscenes.tex from the arXiv-era key shenMARMOT2025 to shen2026marmot, the final *Visual Intelligence* 4, article 22 (2026) record, DOI [10.1007/s44267-026-00125-1](https://doi.org/10.1007/s44267-026-00125-1).
2. Removed the duplicate arXiv-only bibliography records for MARMOT (arXiv:2506.08470) and Soft Shadow Diffusion (arXiv:2601.12257). The canonical final records remain: MARMOT in *Visual Intelligence* (2026), and Soft Shadow Diffusion in ECCV 2024, DOI [10.1007/978-3-031-72989-8_22](https://doi.org/10.1007/978-3-031-72989-8_22). The later arXiv upload of SSD is not a distinct new paper.
3. Updated the survey source log, README audit pointer, and website timeline to document the scope and decisions.

## Build status

The LaTeX/PDF build is intentionally not claimed as complete by this note. The repository's CI build must pass and the regenerated bare_jrnl.pdf must be verified on the resulting commit before the update is reported as complete.
