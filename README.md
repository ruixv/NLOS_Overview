<div align="center">

# Awesome Non-Line-of-Sight (NLOS) Imaging

**A comprehensive, curated survey of Non-Line-of-Sight Imaging research**

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Papers](https://img.shields.io/badge/Papers-190+-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last_Updated-June_2026-red)]()

*Authors: Ruixu Geng · Yang Hu · Yan Chen*

---

### 📄 Papers

| | Link |
|---|---|
| **Original Survey** (peer-reviewed, APSIPA TSIP 2022) | [![APSIPA](https://img.shields.io/badge/APSIPA_TSIP_2022-10.1561%2F116.00000019-blue)](https://doi.org/10.1561/116.00000019) [![arXiv](https://img.shields.io/badge/arXiv-2104.13807-b31b1b)](https://arxiv.org/pdf/2104.13807) |
| **Updated Survey** (2022–2026 extension, *not peer-reviewed*) | [![PDF](https://img.shields.io/badge/PDF-Updated_2026-orange)](https://ruixv.github.io/NLOS_Overview/bare_jrnl.pdf) |
| **Interactive Project Homepage** | [![Homepage](https://img.shields.io/badge/Homepage-ruixv.github.io%2FNLOS__Overview-teal)](https://ruixv.github.io/NLOS_Overview/) |

</div>

---

## What is NLOS Imaging?

**Non-Line-of-Sight (NLOS) imaging** reconstructs or senses hidden scenes that cannot be directly observed — for example, around corners, behind walls, inside occluded spaces, or through scattering/opaque media. The key idea is that light, sound, radio-frequency waves, or other signals interact with visible relay surfaces, hidden objects, tags, or environmental reflectors; the indirect measurements encode recoverable information about hidden geometry, albedo, motion, identity, or position.

```
Emitter / sensor ──► relay wall / reflector / aperture ──► hidden target
        ▲                                                        │
        └──────────── indirect return / transient / RF / sound ◄─┘

measurement → physical forward model → inverse solver / neural prior → hidden scene
```

**Why it matters:** autonomous driving, robotics, search-and-rescue, medical imaging, surveillance, and scene understanding all benefit from sensing beyond direct line of sight.

---

## Table of Contents

- [Latest Additions](#latest-additions)
- [Milestone Timeline](#milestone-timeline)
- [Taxonomy](#taxonomy)
- [Active NLOS Imaging](#active-nlos-imaging)
  - [Hardware Devices](#hardware-devices)
  - [Forward Models](#forward-models)
  - [Reconstruction Algorithms](#reconstruction-algorithms)
  - [Detection, Tracking and Recognition](#detection-tracking-and-recognition)
- [Passive NLOS Imaging](#passive-nlos-imaging)
- [Deep Learning for NLOS](#deep-learning-for-nlos)
- [New NLOS Scenes and Modalities](#new-nlos-scenes-and-modalities)
- [Datasets and Open-Source Code](#datasets-and-open-source-code)
- [Related Surveys and Benchmarks](#related-surveys-and-benchmarks)
- [Citation](#citation)
- [Contributing](#contributing)

---

## Latest Additions

**Update run: 29 June 2026.** This section tracks newly found or newly completed entries that were not explicitly covered in the previous README / homepage snapshot.

| Year | Paper | Venue / Status | Why it matters |
|------|-------|----------------|----------------|
| 2026 | [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | SIGGRAPH 2026 | Uses 3D Gaussian primitives and differentiable transient rendering; targets spatially limited, non-planar, arbitrary relay surfaces. |
| 2026 | [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865) — Somasundaram et al. | Nature 2026 | Demonstrates plug-and-play NLOS using smartphone-grade / consumer LiDAR with motion-induced aperture sampling. |
| 2026 | [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals](https://arxiv.org/abs/2605.29098) — Lu et al. | CVPR 2026 | GeRaF 2.0: neural RF geometry reconstruction that combines LoS visual priors with NLoS radar propagation. |
| 2026 | [DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs](https://arxiv.org/abs/2604.16201) — Behari et al. | arXiv 2026 | Large-scale low-cost LiDAR space-time histogram dataset for data-driven NLOS spatial reasoning. |
| 2026 | [NLOS-Aided Joint OTA Synchronization and Off-Grid Imaging for Distributed MIMO Systems](https://arxiv.org/abs/2603.13981) — Tong et al. | arXiv 2026 | Jointly refines over-the-air synchronization and sparse off-grid environment imaging in distributed MIMO/ISAC by exploiting reconstructed NLOS components. |
| 2026 | [A comprehensive study of time-of-flight non-line-of-sight imaging](https://arxiv.org/abs/2603.09548) — Marco et al. | arXiv 2026 | Benchmark-style comparative study unifying ToF NLOS forward/inverse models under common hardware constraints. |
| 2026 | [Exploiting Double-Bounce Paths in Snapshot Radio SLAM: Bounds, Algorithms and Experiments](https://arxiv.org/abs/2603.02832) — Zhang et al. | arXiv 2026 | Shows that higher-order NLoS radio paths can improve snapshot mmWave SLAM and reveal landmarks hidden to single-bounce models. |
| 2026 | [Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface](https://arxiv.org/abs/2602.11471) — Yasmeen et al. | arXiv 2026 | RIS-assisted around-corner radar sensing; steers energy into NLOS regions and recovers human micro-Doppler signatures. |
| 2026 | [Beyond λ/2: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?](https://arxiv.org/abs/2602.07515) — Chen et al. | arXiv 2026 | RIS-aided NLOS bistatic MIMO radar localization with EMVS polarization cues and phase-disambiguating array geometry. |
| 2026 | [Backscatter Assisted Indoor NLOS Positioning](https://arxiv.org/abs/2606.17325) — Ruttik et al. | arXiv 2026 | Uses passive backscatter devices as virtual anchors for RF NLOS indoor positioning in corridors. |
| 2025 | [MITO: Enabling Non-Line-of-Sight Perception using Millimeter-waves through Real-World Datasets and Simulation Tools](https://arxiv.org/abs/2502.10259) — Dodds et al. | arXiv 2025 | Dataset and simulation tooling for mmWave NLOS perception with paired LOS/NLOS captures and RGB-D/mask supervision. |
| 2025 | [See and Beam: Leveraging LiDAR Sensing and Specular Surfaces for Indoor mmWave Connectivity](https://arxiv.org/abs/2511.09840) — Bandari et al. | arXiv 2025 | Uses LiDAR-visible specular surfaces to infer NLOS mmWave reflection paths and localize users for beam steering. |
| 2025 | [3D Reconstruction from Transient Measurements with Time-Resolved Transformer](https://arxiv.org/abs/2510.09205) — Li et al. | arXiv 2025 | TRT/TRT-NLOS spatio-temporal transformer for photon-efficient LOS/NLOS transient 3D reconstruction with code and datasets. |
| 2025 | [Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging](https://arxiv.org/abs/2508.09655) — Wang et al. | arXiv 2025 | Introduces NANO: a noise-conditioned neural-operator inverse solver for robust NLOS reconstruction under sparse scanning and photon-starved noise. |
| 2025 | [Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform](https://arxiv.org/abs/2508.02003) — Wei et al. | arXiv 2025 | Recasts hidden scenes as 2D functions and reduces runtime/memory by orders of magnitude for lightweight NLOS. |
| 2025 | [mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera](https://arxiv.org/abs/2508.02348) — Park et al. | arXiv 2025 | Uses camera-extracted road layout to interpret mmWave radar point clouds for around-corner pedestrian localization. |
| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Brings self-supervised masked pretraining to NLOS transients and introduces TransVerse-scale transient data for downstream NLOS tasks. |
| 2025 | [Passive acoustic non-line-of-sight localization without a relay surface](https://arxiv.org/abs/2506.08471) — Sommer, Katz | arXiv 2025 | Uses knife-edge diffraction and doorway/corner geometry for passive 3D acoustic localization without conventional relay surfaces. |
| 2025 | [mmMirror: Device Free mmWave Indoor NLoS Localization Using Van-Atta-Array IRS](https://arxiv.org/abs/2505.10816) — Yan et al. | arXiv 2025 | Uses a Van-Atta-array IRS with commodity FMCW radar for device-free around-corner / NLOS localization. |
| 2025 | [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://arxiv.org/abs/2505.08240) — Shi et al. | arXiv 2025 | Tag-assisted mmWave NLOS localization using multipath, HFD modulation, and FS-MUSIC; relevant to RF NLOS sensing/localization rather than full imaging. |
| 2025 | [Geometric Constrained Non-Line-of-Sight Imaging](https://arxiv.org/abs/2503.17992) — Liu et al. | arXiv 2025 | Joint albedo/surface reconstruction with normal-field regularization for higher-detail hidden geometry. |
| 2025 | [Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms](https://arxiv.org/abs/2501.05244) — Sultan et al. | arXiv 2025 | Uses NUFFT/SFFT to support irregular relay sampling and flexible hidden-volume sampling while retaining FFT-like scalability. |
| 2025 | [SuperEx: Enhancing Indoor Mapping and Exploration using Non-Line-of-Sight Perception](https://arxiv.org/abs/2510.10506) — Garg, Dave | arXiv 2025 | Integrates single-photon LiDAR NLOS perception into indoor mapping and exploration through hidden-space carving. |
| 2025 | [mitransient: Transient light transport in Mitsuba 3](https://arxiv.org/abs/2510.25660) — Royo et al. | arXiv 2025 | Differentiable transient-rendering toolkit for time-resolved simulation, NLOS scenes, polarization, and capture noise. |
| 2024 | [Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy](https://arxiv.org/abs/2601.12257) — Raji, Murray-Bruce | ECCV 2024 | Extends passive shadow-based computational periscopy to 3D from a single ordinary NLOS photograph via an SNLLS model and a physics-inspired neural solver. |
| 2024 | [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | Uses an event camera for dynamic diffusion-spot features and a physics-embedded model for passive NLOS imaging of moving objects. |
| 2023 | [Non-line-of-sight reconstruction via structure sparsity regularization](https://arxiv.org/abs/2308.02782) — Huang et al. | arXiv 2023 | DLCT-based reconstruction with nuclear-norm structure sparsity regularization for low-SNR transient data. |
| 2023 | [Non-line-of-sight snapshots and background mapping with an active corner camera](https://www.nature.com/articles/s41467-023-39327-2) — Seidel et al. | Nature Communications 2023 | Active corner camera reconstructs moving foreground objects and maps stationary hidden background. |
| 2022 | [Seeing Around Obstacles with Terahertz Waves](https://arxiv.org/abs/2205.05066) — Cui, Trichopoulos | arXiv 2022 | THz / sub-THz around-obstacle imaging using lossy-mirror environmental surfaces. |
| 2022 | [Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera](https://arxiv.org/abs/2209.13300) — Wang et al. | arXiv 2022 | Introduces event-based passive NLOS for moving targets and the NLOS-ES event-camera dataset. |
| 2021 | [Non-line-of-sight imaging with picosecond temporal resolution](https://arxiv.org/abs/2106.15798) — Wang et al. | Physical Review Letters 2021 | Up-conversion single-photon detector enables picosecond-scale timing and much finer axial NLOS resolution. |

---

## Milestone Timeline

Key breakthroughs that shaped the NLOS Imaging field:

```
2008 ── Raskar & Davis: 5D Time-Light Transport — theoretical foundation
   │
2012 ── Velten et al.: first experimental 3D NLOS reconstruction [Nature Comm.]
   │
2014 ── Heide et al.: Diffuse Mirrors — ToF camera + optimization [SIGGRAPH]
   │
2015 ── Buttafava et al.: SPAD-based NLOS — more accessible hardware
   │
2018 ── O'Toole et al.: confocal NLOS + LCT — real-time O(N³logN) [Nature]
   │     Liu et al.: phasor field — NLOS as virtual LOS wave propagation
   │
2019 ── Lindell et al.: f-k migration — wave-based NLOS [SIGGRAPH]
   │     Katz et al.: passive NLOS via speckle correlation
   │
2020 ── Saunders et al.: computational periscopy with ordinary camera [Nature]
   │     Liu et al.: phasor field diffraction — non-confocal generalization [SIGGRAPH]
   │
2021 ── Wu et al.: 1.43 km long-range NLOS [Nature Comm.]
   │     Shen et al.: Neural Transient Field (NeTF) — unsupervised neural field [TPAMI]
   │
2022 ── Cao et al.: UNCOVER — sub-mm resolution via wavefront shaping [Nature Photonics]
   │     Mu et al.: Physics-rescue deep NLOS [TPAMI]
   │     Wang et al.: first event-camera passive NLOS for moving targets
   │
2023 ── Li et al.: NLOST — first transformer for NLOS [CVPR]
   │     Wang et al.: PAC-Net + NLOS-Track dataset — passive tracking [CVPR]
   │     Fujimura et al.: NLOS-NeuS — neural implicit surface [ICCV]
   │
2024 ── Ye et al.: real-time 4 fps NLOS video of room-sized scenes [Nat. Comp. Sci.]
   │     Li et al.: ST-Mamba — spatial-temporal Mamba for NLOS video [NeurIPS]
   │     Cui et al.: Virtual Scanning — unsupervised irregular undersampling [NeurIPS]
   │     Czajkowski et al.: 3D passive NLOS with ordinary camera [Nature Comm.]
   │     Raji & Murray-Bruce: SSD for 3D computational periscopy [ECCV]
   │     Wang et al.: event-enhanced passive NLOS with physical embedding
   │
2025 ── Li et al.: TransiT — transient transformer for video NLOS [CVPR]
   │     Sun et al.: learnable physical priors for generalization [CVPR]
   │     Su et al.: DG-NLOS — graph neural network [AAAI]
   │     Lai et al.: HoloRadar — full 3D NLOS radar reconstruction [NeurIPS]
   │     Shen et al.: MARMOT — masked autoencoder pretraining for transient/NLOS data
   │     Li et al.: Time-Resolved Transformer for LOS/NLOS transient reconstruction
   │     Wang et al.: NANO — noise-adapted neural operator for robust sparse/noisy NLOS
   │     Sommer & Katz: passive acoustic NLOS without relay surfaces
   │     Shi et al.: N2LoS — single-tag mmWave backscatter NLOS localization
   │     Wei et al.: Quasi-Fresnel Transform — lightweight 2D NLOS inversion
   │     Dodds et al.: MITO — real-world/simulated mmWave NLOS perception dataset
   │
2026 ── Somasundaram et al.: consumer LiDAR NLOS via motion-induced sampling [Nature]
        Lu et al.: GeRaF 2.0 — RF/radar NLOS 3D reconstruction [CVPR]
        Wang et al.: 3D Gaussian Transient Rendering for arbitrary relay geometry [SIGGRAPH]
        Behari et al.: DENALI — low-cost LiDAR NLOS spatial reasoning dataset
        Tong et al.: NLOS-aided OTA synchronization and off-grid imaging for distributed MIMO/ISAC
        Zhang et al.: double-bounce radio SLAM reveals landmarks hidden to single-bounce paths
        Yasmeen et al.: RIS-assisted around-corner radar sensing
        Chen et al.: EMVS-array NLOS localization beyond λ/2 spacing
```

---

## Taxonomy

```
NLOS Imaging
├── Active optical NLOS
│   ├── Hardware: streak camera, SPAD, SPAD array, ToF camera, interferometer, LiDAR
│   ├── Forward models: ellipsoidal ToF, light-cone transform, phasor field, f-k migration
│   └── Reconstruction: FBP, deconvolution, wave optics, optimization, differentiable rendering
│
├── Passive optical NLOS
│   ├── Intensity / shadow / penumbra
│   ├── Coherence / speckle correlation
│   ├── Polarization / hyperspectral cues
│   ├── Event-camera / neuromorphic motion cues
│   └── Real-time passive tracking
│
├── Learning-based NLOS
│   ├── CNN / U-Net / encoder-decoder
│   ├── Physics-guided networks and learned priors
│   ├── Transformer, Mamba, GNN, diffusion
│   ├── Neural operators and algorithm unfolding
│   ├── Self-supervised transient pretraining
│   └── Neural implicit fields and Gaussian primitives
│
└── New scenes and modalities
    ├── Two-bounce and keyhole imaging
    ├── Consumer LiDAR / mobile NLOS
    ├── Radar / RF / mmWave NLOS
    ├── Distributed MIMO / ISAC NLOS off-grid imaging
    ├── Higher-order radio-SLAM multipath exploitation
    ├── RIS-assisted around-corner radar
    ├── Tag-assisted mmWave NLOS localization
    ├── Acoustic / ultrasound NLOS
    ├── Relay-free acoustic diffraction localization
    ├── Event-camera passive NLOS
    ├── Human pose estimation
    └── Arbitrary / non-planar / spatially limited relay surfaces
```

---

## Active NLOS Imaging

### Hardware Devices

#### Streak Camera

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Recovering Three-Dimensional Shape Around a Corner using Ultrafast Time-of-Flight Imaging](https://www.nature.com/articles/ncomms1747) — Velten et al. | Nature Comm. 2012 | First experimental 3D NLOS reconstruction. |
| Reconstruction of Hidden 3D Scenes from Multi-return Transient Imaging — Gupta et al. | IJCV 2012 | Multi-return transient NLOS model. |

#### SPAD / Single-Photon Sensors

| Paper | Venue | Key Contribution | Code |
|-------|-------|------------------|------|
| [Non-line-of-sight imaging using a time-gated single photon avalanche diode](https://opg.optica.org/oe/fulltext.cfm?uri=oe-23-16-20997) — Buttafava et al. | Opt. Express 2015 | First SPAD-based NLOS imaging. | — |
| [Confocal Non-Line-of-Sight Imaging Based on the Light-Cone Transform](https://www.nature.com/articles/s41586-018-0862-6) — O'Toole et al. | **Nature 2018** | LCT: O(N³logN) real-time reconstruction. | [Code](https://github.com/computational-imaging/nlos-fk) |
| [Non-line-of-sight imaging over 1.43 km](https://www.nature.com/articles/s41467-021-25279-2) — Wu et al. | Nature Comm. 2021 | Record 1.43 km long-range NLOS. | [Code](https://github.com/quantum-inspired-lidar/NLOS_imaging_over_1.43km) |
| Fast-Gated 16×16 SPAD Array for NLOS — Riccardo et al. | Opt. Lett. 2022 | Gate-out direct bounce; 16 TDCs on-chip. | — |
| Gradient-Gated SPAD Array — Zhao et al. | Opt. Express 2023 | Spatially varying gate for saturation suppression. | — |
| SNSPD-Based Infrared NLOS Imaging at 1550 nm — Feng et al. | Photon. Res. 2023 | NLOS at telecom wavelengths; superior timing jitter. | — |

#### SPAD Array / Scannerless / Real-Time Systems

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Efficient Non-Line-of-Sight Imaging from Transient Sinograms](https://link.springer.com/chapter/10.1007/978-3-030-58604-1_33) — Isogawa et al. | ECCV 2020 | Circular scanning C²NLOS. |
| Scannerless Real-Time Non-Line-of-Sight Imaging with a Solid-State Camera — Jin et al. | Optica 2020 | 32×32 SPAD array scannerless NLOS. |
| [Real-Time Non-Line-of-Sight Imaging of Dynamic Scenes](https://www.nature.com/articles/s43588-024-00711-5) — Ye et al. | **Nature Comput. Sci. 2024** | 4 fps real-time NLOS video of room-sized dynamic scenes. |
| Real-Time Scan-Free NLOS at 19 fps — Zhang et al. | Optica 2024 | Single-pixel + structured illumination; outdoor daylight. |

#### ToF Camera / LiDAR

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Diffuse Mirrors: 3D Reconstruction from Diffuse Indirect Illumination Using Inexpensive Time-of-Flight Sensors](https://dl.acm.org/doi/10.1145/2601097.2601205) — Heide et al. | SIGGRAPH 2014 | Optimization-based ToF NLOS. |
| [Occluded Imaging with Time-of-Flight Sensors](https://dl.acm.org/doi/10.1145/2858965) — Kadambi et al. | TOG 2016 | ToF camera NLOS with surface normals. |
| Fast Non-Line-of-Sight Imaging with Two-Step Deep Learning — Zhu et al. | AAAI 2021 | Commercial LiDAR + deep learning for NLOS. |
| [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865) — Somasundaram et al. | **Nature 2026** | Smartphone-grade / consumer LiDAR NLOS using multi-frame motion-induced aperture sampling. |

#### Interferometer / Active Focusing

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Theory of Fermat Paths for Non-Line-of-Sight Shape Reconstruction](https://openaccess.thecvf.com/content_CVPR_2019/html/Xin_Theory_of_Fermat_Paths_for_Non-Line-of-Sight_Shape_Reconstruction_CVPR_2019_paper.html) — Xin et al. | CVPR 2019 | Fermat paths encode surface normals. |
| Non-line-of-sight 3D Imaging with a Superheterodyne Interferometer — Willomitzer et al. | 2018 | ~50 µm resolution via superheterodyne interferometry. |
| [High-Resolution Non-Line-of-Sight Imaging with Wavefront Shaping (UNCOVER)](https://www.nature.com/articles/s41566-022-01009-8) — Cao et al. | **Nature Photonics 2022** | ~0.6 mm resolution at 0.55 m; ~900× distance-to-resolution ratio. |

---

### Forward Models

#### ToF-Based Models

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Confocal Non-Line-of-Sight Imaging Based on the Light-Cone Transform](https://www.nature.com/articles/s41586-018-0862-6) — O'Toole et al. | Nature 2018 | Confocal LCT model. |
| [Non-line-of-sight Imaging with Partial Occluders and Surface Normals](https://dl.acm.org/doi/10.1145/3072959.3073599) — Heide et al. | TOG 2017 | Occluder-constrained optimization. |
| [Exploiting Occlusion in Non-Line-of-Sight Active Imaging](https://ieeexplore.ieee.org/document/8421181) — Thrampoulidis et al. | IEEE SPL 2018 | Occlusion reduces ill-posedness. |
| [Non-Line-of-Sight Imaging with Arbitrary Illumination and Detection Pattern](https://arxiv.org/abs/2211.00648) — Liu et al. | arXiv 2022 | CC-SOCR Bayesian framework; arbitrary relay sampling. |
| Non-Planar Relay Surface Reconstruction — Gu et al. | 2023 | FFT-based confocal NLOS for curved relay surfaces. |
