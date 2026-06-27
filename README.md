<div align="center">

# Awesome Non-Line-of-Sight (NLOS) Imaging

**A comprehensive, curated survey of Non-Line-of-Sight Imaging research**

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Papers](https://img.shields.io/badge/Papers-180+-green)]()
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

**Update run: 27 June 2026.** This section tracks newly found or newly completed entries that were not explicitly covered in the previous README / homepage snapshot.

| Year | Paper | Venue / Status | Why it matters |
|------|-------|----------------|----------------|
| 2026 | [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | SIGGRAPH 2026 | Uses 3D Gaussian primitives and differentiable transient rendering; targets spatially limited, non-planar, arbitrary relay surfaces. |
| 2026 | [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865) — Somasundaram et al. | Nature 2026 | Demonstrates plug-and-play NLOS using smartphone-grade / consumer LiDAR with motion-induced aperture sampling. |
| 2026 | [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals](https://arxiv.org/abs/2605.29098) — Lu et al. | CVPR 2026 | GeRaF 2.0: neural RF geometry reconstruction that combines LoS visual priors with NLoS radar propagation. |
| 2026 | [A comprehensive study of time-of-flight non-line-of-sight imaging](https://arxiv.org/abs/2603.09548) — Marco et al. | arXiv 2026 | Benchmark-style comparative study unifying ToF NLOS forward/inverse models under common hardware constraints. |
| 2026 | [Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface](https://arxiv.org/abs/2602.11471) — Yasmeen et al. | arXiv 2026 | RIS-assisted around-corner radar sensing; steers energy into NLOS regions and recovers human micro-Doppler signatures. |
| 2025 | [3D Reconstruction from Transient Measurements with Time-Resolved Transformer](https://arxiv.org/abs/2510.09205) — Li et al. | arXiv 2025 | TRT/TRT-NLOS spatio-temporal transformer for photon-efficient LOS/NLOS transient 3D reconstruction with code and datasets. |
| 2025 | [Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging](https://arxiv.org/abs/2508.09655) — Wang et al. | arXiv 2025 | Introduces NANO: a noise-conditioned neural-operator inverse solver for robust NLOS reconstruction under sparse scanning and photon-starved noise. |
| 2025 | [Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform](https://arxiv.org/abs/2508.02003) — Wei et al. | arXiv 2025 | Recasts hidden scenes as 2D functions and reduces runtime/memory by orders of magnitude for lightweight NLOS. |
| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Brings self-supervised masked pretraining to NLOS transients and introduces TransVerse-scale transient data for downstream NLOS tasks. |
| 2025 | [Passive acoustic non-line-of-sight localization without a relay surface](https://arxiv.org/abs/2506.08471) — Sommer, Katz | arXiv 2025 | Uses knife-edge diffraction and doorway/corner geometry for passive 3D acoustic localization without conventional relay surfaces. |
| 2025 | [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://arxiv.org/abs/2505.08240) — Shi et al. | arXiv 2025 | Tag-assisted mmWave NLOS localization using multipath, HFD modulation, and FS-MUSIC; relevant to RF NLOS sensing/localization rather than full imaging. |
| 2025 | [Geometric Constrained Non-Line-of-Sight Imaging](https://arxiv.org/abs/2503.17992) — Liu et al. | arXiv 2025 | Joint albedo/surface reconstruction with normal-field regularization for higher-detail hidden geometry. |
| 2025 | [Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms](https://arxiv.org/abs/2501.05244) — Sultan et al. | arXiv 2025 | Uses NUFFT/SFFT to support irregular relay sampling and flexible hidden-volume sampling while retaining FFT-like scalability. |
| 2024 | [Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy](https://arxiv.org/abs/2601.12257) — Raji, Murray-Bruce | ECCV 2024 | Extends passive shadow-based computational periscopy to 3D from a single ordinary NLOS photograph via an SNLLS model and a physics-inspired neural solver. |
| 2024 | [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | Uses an event camera for dynamic diffusion-spot features and a physics-embedded model for passive NLOS imaging of moving objects. |
| 2022 | [Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera](https://arxiv.org/abs/2209.13300) — Wang et al. | arXiv 2022 | Introduces event-based passive NLOS for moving targets and the NLOS-ES event-camera dataset. |

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
   │
2026 ── Somasundaram et al.: consumer LiDAR NLOS via motion-induced sampling [Nature]
        Lu et al.: GeRaF 2.0 — RF/radar NLOS 3D reconstruction [CVPR]
        Wang et al.: 3D Gaussian Transient Rendering for arbitrary relay geometry [SIGGRAPH]
        Yasmeen et al.: RIS-assisted around-corner radar sensing
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

#### Wave-Based / Frequency-Domain Models

| Paper | Venue | Key Contribution | Code |
|-------|-------|------------------|------|
| [Wave-Based Non-Line-of-Sight Imaging Using Fast f-k Migration](https://dl.acm.org/doi/10.1145/3306346.3322996) — Lindell et al. | SIGGRAPH 2019 | f-k migration; FFT + Stolt interpolation. | [Code](https://github.com/computational-imaging/nlos-fk) |
| [Virtual Wave Optics for Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3386569.3392470) — Liu et al. | SIGGRAPH 2020 | Phasor field: NLOS as LOS diffraction. | — |
| Phasor Field Waves — Reza et al. | SIGGRAPH 2019 | Phasor field derivation and analysis. | — |
| [Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms](https://arxiv.org/abs/2501.05244) — Sultan et al. | arXiv 2025 | NUFFT/SFFT for irregular relay sampling and scalable reconstruction. | — |
| [Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform](https://arxiv.org/abs/2508.02003) — Wei et al. | arXiv 2025 | 2D hidden-scene representation and Quasi-Fresnel direct inversion. | — |

---

### Reconstruction Algorithms

#### Inverse / Optimization Methods

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Recovering Three-Dimensional Shape Around a Corner](https://www.nature.com/articles/ncomms1747) — Velten et al. | Nature Comm. 2012 | Filter Back Projection (FBP) for NLOS. |
| [Diffuse Mirrors](https://dl.acm.org/doi/10.1145/2601097.2601205) — Heide et al. | SIGGRAPH 2014 | Matrix inverse + TV optimization. |
| [Confocal NLOS Imaging (LCT)](https://www.nature.com/articles/s41586-018-0862-6) — O'Toole et al. | Nature 2018 | 3D deconvolution; O(N³logN). |
| [DLCT: Directional Light-Cone Transform](https://openaccess.thecvf.com/content_CVPR_2020/html/Young_Non-Line-of-Sight_Surface_Reconstruction_Using_the_Directional_Light-Cone_Transform_CVPR_2020_paper.html) — Young et al. | CVPR 2020 | Surface + volumetric reconstruction via directional LCT. |
| [Volumetric Albedo from Angle-Resolved NLOS Scans](https://openaccess.thecvf.com/content_CVPR_2019/html/Tsai_Volumetric_Albedo_From_Angle-Resolved_NLOS_Scans_CVPR_2019_paper.html) — Tsai et al. | CVPR 2019 | First-return photons → surface normals. |
| [Geometric Constrained Non-Line-of-Sight Imaging](https://arxiv.org/abs/2503.17992) — Liu et al. | arXiv 2025 | Normal-field regularization for joint albedo/surface reconstruction. |

#### Reducing Scanning / Sparse Acquisition

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| Compressed Sensing for Active NLOS — Ye et al. | Opt. Express 2021 | 5×5 scan points → 64×64 resolution. |
| [Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization](https://arxiv.org/abs/2211.15367) — Liu et al. | arXiv 2022 | Sparse-measurement SSCR framework; mixed-dimensional regularization. |
| First Photon Event Stamping (FPES) — Li et al. | Opt. Lett. 2022 | 10× fewer photons via Poisson statistics. |
| Photon-Efficient NLOS — Liu et al. | 2022 | Sub-photon-per-pixel reconstruction. |
| Signal Superresolution for NLOS — Wang et al. | 2023 | Sparse-to-dense transients; acquisition speedup. |
| Deep Under-Scanning Measurements (TRN+VRN) — Li et al. | 2023 | 50× faster than iterative; sparse-to-dense transients. |
| Virtual Scanning — Cui et al. | NeurIPS 2024 | Unsupervised NLOS from irregular undersampled transients. |
| Two-Step Deep Remapping — Zhu et al. | 2022 | Non-confocal→confocal remapping; 4× speedup. |
| [Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging](https://arxiv.org/abs/2508.09655) — Wang et al. | arXiv 2025 | Noise-conditioned operator-learning reconstruction for sparse illumination and low-SNR transient data. |

---

### Detection, Tracking and Recognition

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Non-Line-of-Sight Tracking of People at Long Range](https://opg.optica.org/optica/fulltext.cfm?uri=optica-4-2-164) — Chan et al. | Optica 2017 | Long-range NLOS person tracking. |
| Detection and Tracking of Moving Objects Hidden from View — Gariepy et al. | Nature Photonics 2016 | SPAD array tracking. |
| Neural Network Identification of People Hidden from View — Caramazza et al. | Light: Sci. Appl. 2017 | Single SPAD point for recognition. |
| Direct Object Recognition without Line-of-Sight — Lei et al. | Opt. Express 2019 | Steady-state NLOS recognition. |
| [Optical Non-Line-of-Sight Physics-Based 3D Human Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2020/html/Isogawa_Optical_Non-Line-of-Sight_Physics-Based_3D_Human_Pose_Estimation_CVPR_2020_paper.html) — Isogawa et al. | CVPR 2020 | LSTM + physics model for NLOS pose estimation. |

---

## Passive NLOS Imaging

### Intensity-Based Methods

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Turning Corners into Cameras: Principles and Methods](https://openaccess.thecvf.com/content_iccv_2017/html/Bouman_Turning_Corners_Into_ICCV_2017_paper.html) — Bouman et al. | ICCV 2017 | Motion-based passive NLOS. |
| [Computational Periscopy with an Ordinary Digital Camera](https://www.nature.com/articles/s41586-019-0928-6) — Saunders et al. | **Nature 2019** | Partial occluder + ordinary camera. |
| Computational Mirrors: Blind Inverse Light Transport — Aittala et al. | NeurIPS 2019 | Unsupervised deep matrix factorization. |
| Two-Dimensional Non-Line-of-Sight Scene Estimation — Seidel et al. | CVPR 2020 | Penumbra/shadow-based 2D NLOS. |
| Snapshot Corner Camera — Seidel et al. | 2023 | Single-frame NLOS without scanning. |
| [Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy](https://arxiv.org/abs/2601.12257) — Raji, Murray-Bruce | **ECCV 2024** | Single ordinary NLOS photograph → 3D hidden scene; SNLLS model + physics-inspired neural solver. |
| Full-Color 3D Passive NLOS with an Ordinary Camera — Czajkowski, Murray-Bruce | **Nature Comm. 2024** | 3D reconstruction from ordinary camera; two orthogonal edges. |

### Event-Camera / Neuromorphic Passive NLOS

| Paper | Venue | Key Contribution | Dataset |
|-------|-------|------------------|---------|
| [Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera](https://arxiv.org/abs/2209.13300) — Wang et al. | arXiv 2022 | First event-based passive NLOS imaging for moving targets; asynchronous event data preserves dynamic information and reduces speckle degradation. | NLOS-ES |
| [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | EPNP prototype: event-camera dynamic diffusion-spot features + simulation pretraining and limited real-data fine-tuning with physical embedding. | — |

### Hyperspectral / Multispectral Passive NLOS

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| Hyper-NLOS — Chen et al. | 2024 | Hyperspectral camera + HFN-Net fusion; band selection. |
| Rough Surfaces as Relay Surfaces — Li et al. | 2025 | Mixed diffuse-specular relay model; expands usable surfaces. |

### Coherence / Polarization / Optimization

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Non-invasive Single-Shot Imaging Through Scattering Layers and Around Corners via Speckle Correlations](https://www.nature.com/articles/nphoton.2014.234) — Katz et al. | Nature Photonics 2014 | Optical memory effect + speckle autocorrelation. |
| [Passive Sensing Around the Corner Using Spatial Coherence](https://www.nature.com/articles/s41467-018-05985-w) — Batarseh et al. | Nature Comm. 2018 | Spatial coherence; point source detection. |
| Multi-Modal Non-Line-of-Sight Passive Imaging — Beckus et al. | IEEE TIP 2019 | Coherence + intensity fusion. |
| Passive Optical Time-of-Flight Non-Line-of-Sight Imaging — Boger-Lombard et al. | Optica 2019 | Temporal coherence for passive depth. |
| [Polarized Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content_CVPR_2020/html/Tanaka_Polarized_Non-Line_of-Sight_Imaging_CVPR_2020_paper.html) — Tanaka et al. | CVPR 2020 | Polarizer reduces condition number. |
| Passive Non-Line-of-Sight Imaging Using Optimal Transport — Geng et al. | **IEEE TIP 2022** | OT/Wasserstein objective for robust passive NLOS. |
| Passive Non-Line-of-Sight Imaging with Light Transport Modulation — Zhang et al. | **IEEE TIP 2025** | Adaptive transport modulation improves reconstruction stability. |
| Passive Non-Line-of-Sight Imaging with Parallel Encoder — Du et al. | ICASSP 2025 | Parallel multi-scale encoder; improved passive NLOS fidelity and inference efficiency. |

### Real-Time Passive Tracking

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Propagate-and-Calibrate: Real-Time Passive Non-Planar NLOS Tracking (PAC-Net)](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_Propagate-and-Calibrate_Real-Time_Passive_Non-Planar_NLOS_Tracking_CVPR_2023_paper.html) — Wang et al. | CVPR 2023 | PAC-Net; NLOS-Track dataset. |
| Full-Color 3D NLOS with Ordinary Camera — Czajkowski, Murray-Bruce | Nature Comm. 2024 | 3D passive NLOS; no calibration images. |

---

## Deep Learning for NLOS

### End-to-End and Physics-Guided Networks

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Steady-State Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content_CVPR_2019/html/Chen_Steady-State_Non-Line-of-Sight_Imaging_CVPR_2019_paper.html) — Chen et al. | CVPR 2019 | CW laser + U-Net for 3D NLOS from steady-state. |
| [Deep Non-Line-of-Sight Reconstruction](https://openaccess.thecvf.com/content_CVPR_2020/html/Chopite_Deep_Non-Line-of-Sight_Reconstruction_CVPR_2020_paper.html) — Chopite et al. | CVPR 2020 | 3D U-Net for transient → depth map. |
| [Learned Feature Embeddings for Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3414685.3417825) — Chen et al. | SIGGRAPH Asia 2020 | Physics-constrained feature embedding. |
| Physics Rescue: Deep Network for High-Speed NLOS — Mu et al. | **TPAMI 2022** | Physics model + DL; 5 fps, 10× speedup. |
| Untrained Deep Decoder for NLOS — Wu et al. | 2022 | Deep image prior without training data. |
| [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | Physics-embedded learning with event-camera features for moving passive NLOS targets. |
| [Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy](https://arxiv.org/abs/2601.12257) — Raji, Murray-Bruce | ECCV 2024 | Physics-inspired learning for passive 3D computational periscopy from ordinary shadow measurements. |
| [Learnable Physical Priors for Generalizable NLOS Reconstruction](https://arxiv.org/abs/2409.14011) — Sun et al. | CVPR 2025 | Adaptive learned priors for cross-system and low-SNR generalization. |
| [Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging](https://arxiv.org/abs/2508.09655) — Wang et al. | arXiv 2025 | NANO: noise level estimation + neural-operator inverse mapping for sparse/noisy transient reconstruction. |
| Virtual Scanning — Cui et al. | NeurIPS 2024 | SURE-based denoiser; no paired training data. |
| Enhancing Learnable Reconstruction with Fourier Attention — Yu et al. | 2023 | Learnable inverse kernel + attention for high-frequency recovery. |
| Domain Reduction Strategy — Shim et al. | 2024 | Focus search on likely hidden object regions; compute reduction. |

### New Architectures

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| NLOST: Non-Line-of-Sight Imaging with Transformer — Li et al. | **CVPR 2023** | First transformer for NLOS; spatial-temporal self-attention. |
| TransiT: Transient Imaging Transformer for Videographic NLOS Reconstruction — Li et al. | **CVPR 2025** | 10 fps NLOS video; sparse transients via transfer learning. |
| ST-Mamba: Spatial-Temporal Mamba for NLOS Videography — Li et al. | **NeurIPS 2024** | First Mamba model for NLOS; temporal consistency. |
| DG-NLOS: Dual-Branch Graph Neural Network for NLOS Reconstruction — Su et al. | **AAAI 2025** | First GNN-style NLOS reconstruction framework. |
| [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Self-supervised masked autoencoder pretraining for transient/NLOS data; supports arbitrary sampling and downstream NLOS tasks. |
| [3D Reconstruction from Transient Measurements with Time-Resolved Transformer](https://arxiv.org/abs/2510.09205) — Li et al. | arXiv 2025 | TRT/TRT-NLOS spatio-temporal transformer for photon-efficient LOS/NLOS transient 3D reconstruction. |
| Model-Guided Iterative Diffusion Sampling for NLOS Reconstruction — Su et al. | 2024 | Diffusion model guided by NLOS forward model. |

### Neural Implicit / Differentiable Representations

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Non-Line-of-Sight Imaging via Neural Transient Fields (NeTF)](https://ieeexplore.ieee.org/document/9645260) — Shen et al. | TPAMI 2021 | MLP neural transient field; unsupervised. |
| NLOS-NeuS: Non-Line-of-Sight Neural Implicit Surface — Fujimura et al. | **ICCV 2023** | SDF neural implicit surface for smooth 3D NLOS geometry. |
| [Omni-Line-of-Sight Imaging for Holistic Shape Reconstruction](https://arxiv.org/abs/2304.10780) — Huang et al. | arXiv 2023 | Combines LOS and NLOS transient measurements for holistic 3D shape reconstruction. |
| [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | **SIGGRAPH 2026** | 3D Gaussian primitives + differentiable transient rendering for arbitrary relay surfaces. |

### Dynamic NLOS Imaging

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Real-Time Non-Line-of-Sight Imaging of Dynamic Scenes](https://www.nature.com/articles/s43588-024-00711-5) — Ye et al. | **Nature Comput. Sci. 2024** | 4 fps NLOS video; spectrum filtering + interleaved scanning. |
| ST-Mamba for NLOS Videography — Li et al. | NeurIPS 2024 | Mamba-based temporal consistency for video NLOS. |
| TransiT: Transient Imaging Transformer — Li et al. | CVPR 2025 | 10 fps at 64×64; sparse transient input. |
| Plug-and-Play Dynamic NLOS — Ye et al. | 2024 | PnP + deep denoiser; frequency-domain physics filtering. |
| Dynamic NLOS via Single-Pixel Detection — Pei et al. | Opt. Express 2021 | Dynamic NLOS from single-pixel detector. |
| [Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera](https://arxiv.org/abs/2209.13300) — Wang et al. | arXiv 2022 | Asynchronous event data for moving passive NLOS targets. |
| [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | Event-camera + physical embedding for dynamic passive NLOS. |

---

## New NLOS Scenes and Modalities

### Two-Bounce / Keyhole / Arbitrary Relay Geometry

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| Imaging Around Corners Using Transient Knowledge — Vedaldi/Henley et al. | ECCV 2020 | First two-bounce NLOS; hidden object blocks light between two relay surfaces. |
| Role of Transients in Two-Bounce NLOS — Somasundaram et al. | 2023 | Systematic analysis of ToF in 2B-NLOS. |
| [Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path](https://www.science.org/doi/10.1126/sciadv.abg2187) — Metzler et al. | Science Advances 2021 | Beamsplitter confocal NLOS without scanning. |
| [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | SIGGRAPH 2026 | Handles spatially limited and non-planar relay surfaces. |

### Radar / RF / mmWave NLOS

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Seeing Around Street Corners: Non-Line-of-Sight Detection and Tracking in-the-Wild Using Doppler Radar](https://openaccess.thecvf.com/content_CVPR_2020/html/Scheiner_Seeing_Around_Street_Corners_Non-Line-of-Sight_Detection_and_Tracking_in-the-Wild_CVPR_2020_paper.html) — Scheiner et al. | CVPR 2020 | Doppler radar NLOS for automotive vehicle detection. |
| HoloRadar: Full 3D NLOS Reconstruction via mmWave Radar on a Mobile Robot — Lai et al. | **NeurIPS 2025** | Full 3D scene reconstruction with a single mobile mmWave radar. |
| [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://arxiv.org/abs/2505.08240) — Shi et al. | arXiv 2025 | Single-tag mmWave backscatter localization in NLOS; HFD modulation separates tag/environment reflections and FS-MUSIC resolves multipath. |
| [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals](https://arxiv.org/abs/2605.29098) — Lu et al. | **CVPR 2026** | GeRaF 2.0: combines LoS visual priors and NLoS RF propagation for neural geometry reconstruction. |
| [Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface](https://arxiv.org/abs/2602.11471) — Yasmeen et al. | arXiv 2026 | RIS-assisted NLOS radar sensing at 5.5 GHz; improves access to non-specular around-corner regions and human micro-Doppler signatures. |

### Acoustic / Ultrasound NLOS

| Paper | Venue | Key Contribution | Code |
|-------|-------|------------------|------|
| Acoustic Non-Line-of-Sight Imaging — Lindell et al. | SIGGRAPH 2019 | Microphone-array acoustic NLOS; same algorithms as optical. | [Code](https://github.com/computational-imaging/acoustic-nlos) |
| Ultrasound NLOS Imaging via Synthetic Aperture | Commun. Physics 2025 | Bat-echolocation frequency; cm-scale depth resolution; 3D multi-target reconstruction. | — |
| [Passive acoustic non-line-of-sight localization without a relay surface](https://arxiv.org/abs/2506.08471) — Sommer, Katz | arXiv 2025 | Relay-free passive acoustic NLOS: knife-edge diffraction and doorway/corner geometry for 3D source localization. | — |

### Event-Camera / Neuromorphic NLOS

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera](https://arxiv.org/abs/2209.13300) — Wang et al. | arXiv 2022 | Uses asynchronous event streams to image moving NLOS targets and introduces NLOS-ES. |
| [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | Event-enhanced passive NLOS prototype with physical embedding and simulation-to-real fine-tuning. |

### Human Pose / Polarization / Super-FoV

| Paper | Venue | Key Contribution |
|-------|-------|------------------|
| [Optical Non-Line-of-Sight Physics-Based 3D Human Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2020/html/Isogawa_Optical_Non-Line-of-Sight_Physics-Based_3D_Human_Pose_Estimation_CVPR_2020_paper.html) — Isogawa et al. | CVPR 2020 | LSTM+physics for NLOS pose estimation. |
| NLOS Human Pose Estimation — Xiao et al. | OLE 2026 | Joint transient + volume feature extraction; multi-resolution pipeline. |
| [Polarized Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content_CVPR_2020/html/Tanaka_Polarized_Non-Line_of-Sight_Imaging_CVPR_2020_paper.html) — Tanaka et al. | CVPR 2020 | Polarizer as passive NLOS constraint. |
| Polarization-Based Scanning-Free Single-Pixel NLOS — Zhou et al. | PRL 2026 | Polarization-encoded speckle patterns; no scanning, no temporal resolution needed. |
| Super-Field-of-View NLOS via Spatial Encoding — Li et al. | Photonics Research 2026 | Spatial encoding pushes FoV beyond relay-surface limits. |

---

## Datasets and Open-Source Code

| Resource | Paper | Year | Type | Link |
|----------|-------|------|------|------|
| **LCT / f-k Confocal Dataset** | O'Toole et al.; Lindell et al. | 2018–2019 | Active, confocal SPAD | [Link](https://github.com/computational-imaging/nlos-fk) |
| **Galindo Benchmark** | Galindo et al. | 2019 | Active SPAD benchmark | [Link](https://doi.org/10.1364/OE.380140) |
| **NLOS-ES** | Wang et al. | 2022 | Passive event-camera NLOS dataset | [arXiv](https://arxiv.org/abs/2209.13300) |
| **NLOS-Track** | Wang et al. | 2023 | Passive NLOS tracking dataset | — |
| **NLOS-Passive** | Geng et al. | 2022 | Passive NLOS imaging dataset | [Link](https://github.com/ruixv/NLOS-OT) |
| **NLOS Transient Renderer** | Royo et al. | 2022 | Synthetic renderer | — |
| **Fast Differentiable Transient Renderer** | Plack et al. | 2023 | Differentiable transient renderer | — |
| **nlos-fk** | Lindell et al. | 2019 | f-k migration code | [Link](https://github.com/computational-imaging/nlos-fk) |
| **acoustic-nlos** | Lindell et al. | 2019 | Acoustic NLOS code | [Link](https://github.com/computational-imaging/acoustic-nlos) |
| **NLOS_imaging_over_1.43km** | Wu et al. | 2021 | Long-range NLOS code/data | [Link](https://github.com/quantum-inspired-lidar/NLOS_imaging_over_1.43km) |
| **NLOS-OT** | Geng et al. | 2022 | Passive NLOS OT code/data | [Link](https://github.com/ruixv/NLOS-OT) |
| **TRT Code / Datasets** | Li et al. | 2025 | Transient transformer code/datasets | [Link](https://github.com/Depth2World/TRT) |

---

## Related Surveys and Benchmarks

| Title | Authors | Venue / Status | Link | Why useful |
|-------|---------|----------------|------|------------|
| Non-line-of-sight Imaging | Faccio, Velten, Wetzstein | **Nature Reviews Physics 2020** | [Link](https://www.nature.com/articles/s42254-020-0174-8) | Comprehensive review of core physical principles and early progress. |
| Recent Advances on Non-Line-of-Sight Imaging | Geng, Hu, Chen | APSIPA TSIP 2022 | [Link](https://doi.org/10.1561/116.00000019) | Survey organized by conventional physical models, deep learning, and new scenes. |
| [A comprehensive study of time-of-flight non-line-of-sight imaging](https://arxiv.org/abs/2603.09548) | Marco et al. | arXiv 2026 | [arXiv](https://arxiv.org/abs/2603.09548) | Common formulation and benchmark-style comparison of representative ToF NLOS methods. |

---

## Citation

If this repository is useful for your research, please cite our survey paper:

```bibtex
@article{geng2022nlos,
  title   = {Recent Advances on Non-Line-of-Sight Imaging: Conventional Physical Models, Deep Learning, and New Scenes},
  author  = {Geng, Ruixu and Hu, Yang and Chen, Yan},
  year    = {2022}
}
```

Key papers in the field:

```bibtex
@article{otoole2018confocal,
  title   = {Confocal non-line-of-sight imaging based on the light-cone transform},
  author  = {O'Toole, Matthew and Lindell, David B and Wetzstein, Gordon},
  journal = {Nature},
  volume  = {555},
  pages   = {338--341},
  year    = {2018}
}

@inproceedings{lindell2019wave,
  title     = {Wave-based non-line-of-sight imaging using fast fk-migration},
  author    = {Lindell, David B and Tseng, John K and O'Toole, Matthew},
  booktitle = {ACM SIGGRAPH},
  year      = {2019}
}

@inproceedings{liu2020phasor,
  title     = {Virtual wave optics for non-line-of-sight imaging},
  author    = {Liu, Xiaochun and others},
  booktitle = {ACM SIGGRAPH},
  year      = {2020}
}

@article{ye2024realtime,
  title   = {Real-time non-line-of-sight imaging of dynamic scenes},
  author  = {Ye, Yue and others},
  journal = {Nature Computational Science},
  year    = {2024}
}
```

---

## Contributing

We welcome contributions! Please:

1. **Add a paper:** Open a Pull Request with the paper details in the appropriate section.
2. **Fix a broken link:** Open an Issue or PR.
3. **Add a code repository:** If a paper has released code not yet listed, add it to the Open-Source Code section.
4. **Flag uncertain metadata:** If a paper title, venue, author list, or code link needs verification, open an Issue.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

<div align="center">

**Star this repository if you find it helpful!**

*Last updated: 27 June 2026*

</div>
