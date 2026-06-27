# Citation-tracing update notes — 27 June 2026

This note records high-confidence NLOS imaging papers found by forward-citation and adjacent-topic tracing from core NLOS papers. These entries should be mirrored into the main README sections and are already reflected in the interactive homepage paper explorer.

## Newly added / missing papers

| Year | Paper | Venue / Status | Suggested category | Why it matters |
|------|-------|----------------|--------------------|----------------|
| 2025 | [SuperEx: Enhancing Indoor Mapping and Exploration using Non-Line-of-Sight Perception](https://arxiv.org/abs/2510.10506) — Garg, Dave | arXiv 2025 | New scenes / robotic NLOS / single-photon LiDAR | Integrates NLOS sensing into the robotic mapping-exploration loop using SP-LiDAR timing histograms, NLOS empty-space carving, and structure recovery. |
| 2025 | [mitransient: Transient light transport in Mitsuba 3](https://arxiv.org/abs/2510.25660) — Royo et al. | arXiv 2025 | Datasets / open-source code / simulation | Mitsuba 3 extension for time-resolved, polarized, differentiable transient simulation, including tools for realistic NLOS scene setups and capture noise. |
| 2023 | [Non-line-of-sight reconstruction via structure sparsity regularization](https://arxiv.org/abs/2308.02782) — Huang et al. | arXiv 2023 | Reconstruction algorithms / regularization | Adds nuclear-norm structure-sparsity regularization to DLCT-style NLOS reconstruction for low-SNR transient measurements. |
| 2023 | [Non-line-of-sight snapshots and background mapping with an active corner camera](https://www.nature.com/articles/s41467-023-39327-2) — Seidel et al. | Nature Communications 2023 | Active NLOS / scannerless / active corner camera | Uses complete optical response modeling without multiple illumination positions to reconstruct moving foreground objects and map stationary hidden background. |
| 2022 | [Seeing Around Obstacles with Terahertz Waves](https://arxiv.org/abs/2205.05066) — Cui, Trichopoulos | arXiv 2022 | New modalities / THz NLOS | Demonstrates sub-THz around-obstacle imaging with lossy-mirror building surfaces and mirror-folding reconstruction. |
| 2021 | [Non-line-of-sight imaging with picosecond temporal resolution](https://arxiv.org/abs/2106.15798) — Wang et al. | Physical Review Letters 2021 | SPAD / single-photon sensors / high-resolution active NLOS | Uses an up-conversion single-photon detector with ~1.4 ps timing, giving 180 µm axial and 2 mm lateral NLOS resolution. |

## Metadata correction

| Paper | Previous label | Correct label | Evidence |
|------|----------------|---------------|----------|
| [Non-line-of-sight imaging with arbitrary illumination and detection pattern](https://www.nature.com/articles/s41467-023-38898-4) — Liu et al. | arXiv 2022 | Nature Communications 2023 | Final Nature Communications article, volume 14, article 3230, published 03 June 2023. |

## README insertion suggestions

- Add the PRL picosecond paper under `SPAD / Single-Photon Sensors` and the 2021 milestone line.
- Add the active corner camera paper under `SPAD Array / Scannerless / Real-Time Systems` and the 2023 milestone line.
- Correct `Non-Line-of-Sight Imaging with Arbitrary Illumination and Detection Pattern` from `arXiv 2022` to `Nature Comm. 2023` in `Forward Models`.
- Add the structure-sparsity paper under `Reconstruction Algorithms`.
- Add the THz paper under `New NLOS Scenes and Modalities`.
- Add SuperEx under robotic / mobile NLOS applications.
- Add mitransient under `Datasets and Open-Source Code`.
