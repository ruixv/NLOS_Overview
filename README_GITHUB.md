<div align="center">

# Awesome Non-Line-of-Sight (NLOS) Imaging

**A comprehensive, curated survey of Non-Line-of-Sight Imaging research**

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Paper](https://img.shields.io/badge/Survey_Paper-IEEE_TGRS-blue)](https://doi.org/)
[![Papers](https://img.shields.io/badge/Papers-200+-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026-red)]()

*Based on the survey: "Non-Line-of-Sight Imaging: A Comprehensive Survey" (2021, Updated 2022–2026)*  
*Authors: Ruixu Geng · Yang Hu · Yan Chen*

</div>

---

## What is NLOS Imaging?

**Non-Line-of-Sight (NLOS) imaging** is the problem of reconstructing hidden scenes that cannot be directly observed — for example, around corners, behind walls, or through scattering media. The key idea is that light (or other waves) undergoes diffuse reflections off visible relay surfaces, encoding information about the hidden scene that can be computationally recovered.

```
                 ┌─────────────────────────────────────────────────┐
                 │                                                 │
   [Laser/       │    ②   Hidden Object                            │
    Detector] ───┼──► ①  (3rd bounce ←→ 2nd bounce)   Wall (relay)│
                 │                                                 │
                 │    Measurement at Wall  →  Reconstruction       │
                 └─────────────────────────────────────────────────┘
                    NLOS:  "Seeing Around Corners"
```

**Why it matters:** Autonomous driving (detecting pedestrians behind corners), search-and-rescue (finding people in collapsed buildings), medical imaging, and robot navigation all benefit from the ability to sense beyond the direct line of sight.

---

## Table of Contents

- [Milestone Timeline](#milestone-timeline)
- [Taxonomy](#taxonomy)
- [Active NLOS Imaging](#active-nlos-imaging)
  - [Hardware Devices](#hardware-devices)
  - [Forward Models](#forward-models)
  - [Reconstruction Algorithms](#reconstruction-algorithms)
  - [Detection, Tracking and Recognition](#detection-tracking-and-recognition)
- [Passive NLOS Imaging](#passive-nlos-imaging)
  - [Intensity-Based Methods](#intensity-based-methods)
  - [Coherence-Based Methods](#coherence-based-methods)
  - [Real-Time Passive Tracking](#real-time-passive-tracking)
- [Deep Learning for NLOS](#deep-learning-for-nlos)
  - [End-to-End Networks](#end-to-end-networks)
  - [Physics-Guided Networks](#physics-guided-networks)
  - [Transformers](#transformers)
  - [State-Space Models (Mamba)](#state-space-models-mamba)
  - [Graph Neural Networks](#graph-neural-networks)
  - [Diffusion Models](#diffusion-models)
  - [Neural Implicit Representations](#neural-implicit-representations)
  - [Dynamic NLOS Imaging](#dynamic-nlos-imaging)
- [New NLOS Scenes](#new-nlos-scenes)
  - [Two-Bounce NLOS](#two-bounce-nlos)
  - [Keyhole Imaging](#keyhole-imaging)
  - [Radar-Based NLOS](#radar-based-nlos)
  - [Acoustic NLOS](#acoustic-nlos)
  - [Human Pose Estimation](#human-pose-estimation)
  - [Polarization-Based NLOS](#polarization-based-nlos)
  - [Super-Field-of-View NLOS](#super-field-of-view-nlos)
- [Datasets](#datasets)
- [Open-Source Code](#open-source-code)
- [Related Surveys and Resources](#related-surveys-and-resources)
- [Citation](#citation)
- [Contributing](#contributing)

---

## Milestone Timeline

Key breakthroughs that shaped the NLOS Imaging field:

```
2008 ── Raskar & Davis: "5D Time-Light Transport" — theoretical foundation
   │
2012 ── Velten et al.: First experimental NLOS imaging (streak camera) [Nature Comm.]
   │
2014 ── Heide et al.: "Diffuse Mirrors" — ToF camera + optimization [SIGGRAPH]
   │
2015 ── Buttafava et al.: SPAD-based NLOS — democratizing hardware
   │
2018 ── O'Toole et al.: Confocal NLOS + LCT — real-time O(N³logN) [Nature]
   │     Liu et al.: Phasor Field — NLOS as LOS diffraction problem
   │
2019 ── Lindell et al.: f-k migration — wave-based NLOS [SIGGRAPH]
   │     Katz et al.: Passive NLOS via speckle correlation
   │
2020 ── Saunders et al.: Computational periscopy (ordinary camera)
   │     Liu et al.: Phasor Field Diffraction — non-confocal generalization
   │
2021 ── Wu et al.: 1.43 km long-range NLOS [Nature Comm.]
   │     Shen et al.: Neural Transient Field (NeTF) — unsupervised
   │
2022 ── Cao et al.: UNCOVER — sub-mm resolution via wavefront shaping [Nature Photonics]
   │     Mu et al.: Physics-rescue deep NLOS [TPAMI]
   │
2023 ── Li et al.: NLOST — first transformer for NLOS [CVPR]
   │     Wang et al.: PAC-Net + NLOS-Track dataset — passive tracking [CVPR]
   │     Fujimura et al.: NLOS-NeuS — neural implicit surface [ICCV]
   │
2024 ── Ye et al.: Real-time 4 fps NLOS video of room-sized scenes [Nat. Comp. Sci.]
   │     Li et al.: ST-Mamba — spatial-temporal Mamba for NLOS video [NeurIPS]
   │     Cui et al.: Virtual Scanning — unsupervised NLOS [NeurIPS]
   │     Czajkowski et al.: 3D passive NLOS with ordinary camera [Nature Comm.]
   │
2025 ── Li et al.: TransiT — 10 fps NLOS video with transient transformer [CVPR]
   │     Sun et al.: Learnable physical priors for generalization [CVPR]
   │     Su et al.: DG-NLOS — graph neural network [AAAI]
   │     Lai et al.: HoloRadar — full 3D NLOS radar reconstruction [NeurIPS]
   │
2026 ── Xiao et al.: NLOS human pose estimation [OLE]
        Zhou et al.: Polarization single-pixel scanning-free NLOS [PRL]
        Li et al.: Super-field-of-view NLOS imaging [Photonics Research]
```

---

## Taxonomy

```
NLOS Imaging
├── Active NLOS
│   ├── Hardware
│   │   ├── Streak Camera (ultra-high temporal resolution)
│   │   ├── SPAD (single-photon, affordable)
│   │   ├── SPAD Array (scannerless)
│   │   ├── ToF Camera (real-time, low cost)
│   │   ├── Interferometer (sub-micron resolution)
│   │   └── LiDAR (integrated, commercial)
│   ├── Forward Models
│   │   ├── ToF-based (ellipsoid / confocal)
│   │   └── Wave-based (f-k migration / phasor field)
│   └── Reconstruction
│       ├── Volumetric (FBP, LCT, deconvolution)
│       ├── Surface (Fermat paths, first-return photons)
│       └── Neural (transformers, implicit surfaces, diffusion)
│
├── Passive NLOS
│   ├── Conventional Camera (intensity, partial occluder)
│   ├── Polarized Camera (polarization cues)
│   ├── Interferometer (spatial/temporal coherence)
│   ├── Hyperspectral Camera (spectral fusion)
│   └── Infrared Camera
│
├── Deep Learning
│   ├── End-to-End (U-Net, ResNet variants)
│   ├── Physics-Guided (forward model + network)
│   ├── New Architectures (Transformer, Mamba, GNN)
│   ├── Generative (Diffusion, VAE)
│   ├── Neural Implicit (NeTF, NLOS-NeuS)
│   └── Dynamic / Video NLOS
│
└── New NLOS Scenes
    ├── Two-Bounce Imaging
    ├── Keyhole Imaging
    ├── Radar NLOS (mmWave)
    ├── Acoustic / Ultrasound NLOS
    ├── Human Pose Estimation
    ├── Polarization Single-Pixel
    └── Super-Field-of-View
```

---

## Active NLOS Imaging

### Hardware Devices

#### Streak Camera

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Recovering Three-Dimensional Shape Around a Corner using Ultrafast Time-of-Flight Imaging](https://www.nature.com/articles/ncomms1747) — Velten et al. | Nature Comm. 2012 | First experimental 3D NLOS reconstruction |
| [Reconstruction of Hidden 3D Scenes from Multi-return Transient Imaging](https://link.springer.com/article/10.1007/s11263-012-0520-4) — Gupta et al. | IJCV 2012 | Multi-return transient NLOS model |

#### SPAD (Single-Photon Avalanche Diode)

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Non-line-of-sight imaging using a time-gated single photon avalanche diode](https://opg.optica.org/oe/fulltext.cfm?uri=oe-23-16-20997) — Buttafava et al. | Opt. Express 2015 | First SPAD-based NLOS imaging | — |
| [Confocal Non-Line-of-Sight Imaging Based on the Light-Cone Transform](https://www.nature.com/articles/s41586-018-0862-6) — O'Toole et al. | **Nature 2018** | LCT: O(N³logN) real-time reconstruction | [Code](https://github.com/m-toole/lct-nlos) |
| [Non-line-of-sight imaging over 1.43 km](https://www.nature.com/articles/s41467-021-25279-2) — Wu et al. | Nature Comm. 2021 | Record 1.43 km long-range NLOS | — |
| [Non-line-of-sight imaging with signal-to-noise ratio: A survey](https://doi.org/) — Li et al. | JSTQE 2021 | SNR analysis for long-range NLOS | — |
| Fast-Gated 16×16 SPAD Array for NLOS — Riccardo et al. | Opt. Lett. 2022 | Gate-out direct bounce; 16 TDCs on-chip | — |
| Gradient-Gated SPAD Array — Zhao et al. | Opt. Express 2023 | Spatially varying gate for saturation suppression | — |
| [SNSPD-Based Infrared NLOS Imaging at 1550 nm](https://doi.org/) — Feng et al. | Photon. Res. 2023 | NLOS at telecom wavelengths; superior timing jitter | — |

#### SPAD Array (Scannerless)

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Efficient Non-Line-of-Sight Imaging from Transient Sinograms](https://link.springer.com/chapter/10.1007/978-3-030-58604-1_33) — Isogawa et al. | ECCV 2020 | Circular scanning C²NLOS | — |
| [Scannerless Real-Time Non-Line-of-Sight Imaging with a Solid-State Camera](https://doi.org/) — Jin et al. | Optica 2020 | 32×32 SPAD array scannerless NLOS | — |
| [Real-Time Non-Line-of-Sight Imaging of Dynamic Scenes](https://link.springer.com/article/10.1007/s43588-024-00711-5) — Ye et al. | **Nature Comput. Sci. 2024** | **4 fps real-time NLOS video of room-sized dynamic scenes** | — |
| Real-Time Scan-Free NLOS at 19 fps — Zhang et al. | Optica 2024 | Single-pixel + structured illumination; outdoor daylight | — |

#### ToF Camera

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Diffuse Mirrors: 3D Reconstruction from Diffuse Indirect Illumination Using Inexpensive Time-of-Flight Sensors](https://dl.acm.org/doi/10.1145/2601097.2601205) — Heide et al. | SIGGRAPH 2014 | Optimization-based ToF NLOS |
| [Occluded Imaging with Time-of-Flight Sensors](https://dl.acm.org/doi/10.1145/2858965) — Kadambi et al. | TOG 2016 | ToF camera NLOS with surface normals |

#### Interferometer

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Theory of Fermat Paths for Non-Line-of-Sight Shape Reconstruction](https://openaccess.thecvf.com/content_CVPR_2019/html/Xin_Theory_of_Fermat_Paths_for_Non-Line-of-Sight_Shape_Reconstruction_CVPR_2019_paper.html) — Xin et al. | CVPR 2019 | Fermat paths encode surface normals |
| [Non-line-of-sight 3D Imaging with a Superheterodyne Interferometer](https://doi.org/) — Willomitzer et al. | 2018 | 50 µm resolution via SHI |

#### LiDAR

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Fast Non-Line-of-Sight Imaging with Two-Step Deep Learning](https://doi.org/) — Zhu et al. | AAAI 2021 | Commercial LiDAR + deep learning for NLOS |

#### Active Focusing — High Resolution

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [High-Resolution Non-Line-of-Sight Imaging with Wavefront Shaping (UNCOVER)](https://www.nature.com/articles/s41566-022-01009-8) — Cao et al. | **Nature Photonics 2022** | **0.6 mm resolution at 0.55 m; 900× distance-to-resolution ratio** |

---

### Forward Models

#### ToF-Based Models

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Confocal Non-Line-of-Sight Imaging Based on the Light-Cone Transform](https://www.nature.com/articles/s41586-018-0862-6) — O'Toole et al. | Nature 2018 | Confocal LCT model | [Code](https://github.com/m-toole/lct-nlos) |
| [Non-line-of-sight Imaging with Partial Occluders and Surface Normals](https://dl.acm.org/doi/10.1145/3072959.3073599) — Heide et al. | TOG 2017 | Occluder-constrained optimization |
| [Exploiting Occlusion in Non-Line-of-Sight Active Imaging](https://ieeexplore.ieee.org/document/8421181) — Thrampoulidis et al. | IEEE SPL 2018 | Occlusion reduces ill-posedness |
| Non-Line-of-Sight Reconstruction for Arbitrary Illumination — Liu et al. | 2023 | CC-SOCR Bayesian framework; non-regular relay grids |
| Non-Planar Relay Surface Reconstruction — Gu et al. | 2023 | FFT-based confocal NLOS for curved relay surfaces |

#### Wave-Based Models

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Acoustic Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3306346.3322996) — Lindell et al. | SIGGRAPH 2019 | f-k migration — wave-based NLOS from seismology | [Code](https://github.com/computational-imaging/acoustic-nlos) |
| [Virtual Wave Optics for Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3386569.3392470) — Liu et al. | SIGGRAPH 2020 | Phasor field: NLOS as LOS diffraction | [Code](https://github.com/gliu7/phasor) |
| [Phasor Field Waves](https://dl.acm.org/doi/10.1145/3306346.3322995) — Reza et al. | SIGGRAPH 2019 | Phasor field derivation and analysis | — |
| Higher-Order Bounce Imaging (Virtual Mirrors) — Royo et al. | 2023 | 4th-bounce reflections expand hidden scene coverage |
| Phasor Fields under Scattering Conditions — Luesia et al. | 2022 | Robustness analysis for contaminated relay surfaces |
| Coherent NLOS with Frequency-Comb Calibration — Huang et al. | 2024 | NLOS under strong ambient light; NLOS vibrometry |

---

### Reconstruction Algorithms

#### Inverse Methods

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Recovering Three-Dimensional Shape Around a Corner](https://www.nature.com/articles/ncomms1747) — Velten et al. | Nature Comm. 2012 | Filter Back Projection (FBP) for NLOS | — |
| [Diffuse Mirrors](https://dl.acm.org/doi/10.1145/2601097.2601205) — Heide et al. | SIGGRAPH 2014 | Matrix inverse + TV optimization | — |
| [Confocal Non-Line-of-Sight Imaging (LCT)](https://www.nature.com/articles/s41586-018-0862-6) — O'Toole et al. | Nature 2018 | 3D deconvolution; O(N³logN) | [Code](https://github.com/m-toole/lct-nlos) |
| [DLCT: Deep Learning LCT](https://openaccess.thecvf.com/content_CVPR_2020/html/Young_Non-Line-of-Sight_Surface_Reconstruction_Using_the_Directional_Light-Cone_Transform_CVPR_2020_paper.html) — Young et al. | CVPR 2020 | Surface + volumetric via directional LCT | — |
| [Volumetric Albedo from Angle-Resolved NLOS Scans](https://openaccess.thecvf.com/content_CVPR_2019/html/Tsai_Volumetric_Albedo_From_Angle-Resolved_NLOS_Scans_CVPR_2019_paper.html) — Tsai et al. | CVPR 2019 | First-return photons → surface normals | — |

#### Wave-Based Methods

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Wave-Based Non-Line-of-Sight Imaging Using Fast f-k Migration](https://dl.acm.org/doi/10.1145/3306346.3322996) — Lindell et al. | SIGGRAPH 2019 | f-k migration; FFT + Stolt interpolation | [Code](https://github.com/computational-imaging/nlos-fk) |
| [Virtual Wave Optics for Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3386569.3392470) — Liu et al. | SIGGRAPH 2020 | Phasor field diffraction; non-confocal O(N³logN) | [Code](https://github.com/gliu7/phasor) |
| [Phasor Field Waves](https://dl.acm.org/doi/10.1145/3306346.3322995) — Reza et al. | SIGGRAPH 2019 | Phasor field framework | — |

#### Reducing Scanning / Sparse Acquisition

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Compressed Sensing for Active NLOS](https://doi.org/) — Ye et al. | Opt. Express 2021 | 5×5 scan points → 64×64 resolution |
| First Photon Event Stamping (FPES) — Li et al. | Opt. Lett. 2022 | 10× fewer photons via Poisson statistics |
| Photon-Efficient NLOS — Liu et al. | 2022 | Sub-photon-per-pixel reconstruction |
| Signal Superresolution for NLOS — Wang et al. | 2023 | 16× acquisition speedup |
| Deep Under-Scanning Measurements (TRN+VRN) — Li et al. | 2023 | 50× faster than iterative; sparse-to-dense transients |
| [Virtual Scanning](https://proceedings.neurips.cc/paper_files/paper/2024/) — Cui et al. | NeurIPS 2024 | Unsupervised NLOS from irregular undersampled transients |
| Two-Step Deep Remapping — Zhu et al. | 2022 | Non-confocal→confocal remapping; 4× speedup |

---

### Detection, Tracking and Recognition

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Non-Line-of-Sight Tracking of People at Long Range](https://opg.optica.org/optica/fulltext.cfm?uri=optica-4-2-164) — Chan et al. | Optica 2017 | Long-range NLOS person tracking |
| [Detection and Tracking of Moving Objects Hidden from View](https://www.nature.com/articles/nphoton.2015.234) — Gariepy et al. | Nature Photonics 2016 | SPAD array tracking |
| [Neural Network Identification of People Hidden from View](https://www.nature.com/articles/lsa201752) — Caramazza et al. | Light: Science 2017 | Single SPAD point for recognition |
| [Direct Object Recognition without Line-of-Sight](https://doi.org/) — Lei et al. | Opt. Express 2019 | Steady-state NLOS recognition (ResNet) |
| [Optical Non-Line-of-Sight Physics-Based 3D Human Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2020/html/Isogawa_Optical_Non-Line-of-Sight_Physics-Based_3D_Human_Pose_Estimation_CVPR_2020_paper.html) — Isogawa et al. | CVPR 2020 | LSTM + physics model for NLOS pose estimation |

---

## Passive NLOS Imaging

### Intensity-Based Methods

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Turning Corners into Cameras: Principles and Methods](https://openaccess.thecvf.com/content_iccv_2017/html/Bouman_Turning_Corners_Into_ICCV_2017_paper.html) — Bouman et al. | ICCV 2017 | Motion-based passive NLOS | — |
| [Computational Periscopy with an Ordinary Digital Camera](https://www.nature.com/articles/s41586-019-0928-6) — Saunders et al. | **Nature 2019** | Partial occluder + ordinary camera | — |
| [Computational Mirrors: Blind Inverse Light Transport](https://dl.acm.org/doi/10.1145/3355089.3356530) — Aittala et al. | SIGGRAPH Asia 2019 | Unsupervised deep matrix factorization | — |
| [Two-Dimensional Non-Line-of-Sight Scene Estimation](https://openaccess.thecvf.com/content_CVPR_2020/html/Seidel_Two-Dimensional_Non-Line-of-Sight_Scene_Estimation_From_Thermal_Infrared_CVPR_2020_paper.html) — Seidel et al. | CVPR 2020 | Penumbra (shadow) based 2D NLOS | — |
| [Snapshot Corner Camera](https://doi.org/) — Seidel et al. | 2023 | Single-frame NLOS without scanning |
| [Full-Color 3D Passive NLOS with an Ordinary Camera](https://www.nature.com/articles/s41467-024-48956-2) — Czajkowski, Murray-Bruce | **Nature Comm. 2024** | **3D reconstruction from ordinary camera; two orthogonal edges** | — |

#### Hyperspectral / Multispectral Passive NLOS

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| Hyper-NLOS — Chen et al. | 2024 | Hyperspectral camera + HFN-Net fusion; band selection |
| Rough Surfaces as Relay Surfaces — Li et al. | 2025 | Mixed diffuse-specular relay model; expands usable surfaces |

### Coherence-Based Methods

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Non-invasive Single-Shot Imaging Through Scattering Layers and Around Corners via Speckle Correlations](https://www.nature.com/articles/nphoton.2014.234) — Katz et al. | Nature Photonics 2014 | Optical memory effect + speckle autocorrelation |
| [Passive Sensing Around the Corner Using Spatial Coherence](https://www.nature.com/articles/s41467-018-07567-2) — Batarseh et al. | Nature Comm. 2018 | Spatial coherence; point source detection |
| [Multi-Modal Non-Line-of-Sight Passive Imaging](https://doi.org/) — Beckus et al. | Opt. Express 2019 | Coherence + intensity fusion |
| [Passive Non-Line-of-Sight Imaging Using Optimal Transport](https://doi.org/) — Boger-Lombard et al. | Optica 2019 | Temporal coherence for passive ToF |
| [Polarized Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content_CVPR_2020/html/Tanaka_Polarized_Non-Line-of-Sight_Imaging_CVPR_2020_paper.html) — Tanaka et al. | CVPR 2020 | Polarizer reduces condition number |

### Real-Time Passive Tracking

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Propagate-and-Calibrate: Real-Time Passive Non-Planar NLOS Tracking (PAC-Net)](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_Propagate-and-Calibrate_Real-Time_Passive_Non-Planar_NLOS_Tracking_CVPR_2023_paper.html) — Wang et al. | CVPR 2023 | PAC-Net; **NLOS-Track dataset** (first large-scale passive tracking dataset) | [Code+Data](https://github.com/JerrickLiu/AnytimeNLOS) |
| [Full-Color 3D NLOS with Ordinary Camera](https://www.nature.com/articles/s41467-024-48956-2) — Czajkowski, Murray-Bruce | Nature Comm. 2024 | 3D passive NLOS; no calibration images | — |

---

## Deep Learning for NLOS

### End-to-End Networks

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Steady-State Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content_CVPR_2019/html/Chen_Steady-State_Non-Line-of-Sight_Imaging_CVPR_2019_paper.html) — Chen et al. | CVPR 2019 | CW laser + U-Net for 3D NLOS from steady-state | — |
| [Deep Non-Line-of-Sight Reconstruction](https://openaccess.thecvf.com/content_CVPR_2020/html/Chopite_Deep_Non-Line-of-Sight_Reconstruction_CVPR_2020_paper.html) — Chopite et al. | CVPR 2020 | 3D U-Net for transient → depth map | — |
| [Learned Feature Embeddings for Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3414685.3417825) — Chen et al. | SIGGRAPH Asia 2020 | Physics-constrained feature embedding | [Code](https://github.com/computational-imaging/nlos-fk) |
| [Non-Line-of-Sight Imaging Using Deep Learning](https://doi.org/) — Yu et al. | Opt. Express 2019 | U-Net for passive speckle NLOS | — |
| [Non-line-of-sight imaging via variational autoencoder](https://doi.org/) — Tancik et al. | 2018 | VAE + CNN for passive NLOS; classification | — |
| Physics Rescue: Deep Network for High-Speed NLOS — Mu et al. | **TPAMI 2022** | Physics model + DL; 5 fps, 10× speedup | — |
| Two-Step Deep Remapping — Zhu et al. | 2022 | Non-confocal to confocal remapping; 4× FK speedup | — |
| Untrained Deep Decoder for NLOS — Wu et al. | 2022 | Deep image prior without training data | — |

### Physics-Guided Networks

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Non-Line-of-Sight Imaging via Neural Transient Fields (NeTF)](https://ieeexplore.ieee.org/document/9645260) — Shen et al. | TPAMI 2021 | Unsupervised neural transient field; MLP maps measurement to scene | [Code](https://github.com/zeromakerplus/NeTF_public) |
| [Deep-Inverse Correlography: Towards Real-Time High-Resolution Non-Line-of-Sight Imaging](https://opg.optica.org/optica/fulltext.cfm?uri=optica-7-1-63) — Metzler et al. | Optica 2020 | U-Net phase recovery for speckle NLOS | — |
| Deep Under-Scanning Measurements (TRN+VRN) — Li et al. | 2023 | 50× speed; physics-based volume reconstruction | — |
| [Learnable Physical Priors for Generalizable NLOS Reconstruction](https://openaccess.thecvf.com/content/CVPR2025/) — Sun et al. | CVPR 2025 | Adaptive learned priors; improves generalization across SNR and scenes | — |
| [Virtual Scanning (Unsupervised from Irregular Undersampled Transients)](https://proceedings.neurips.cc/) — Cui et al. | NeurIPS 2024 | SURE-based denoiser; no paired training data needed | — |
| Enhancing Learnable Reconstruction with Fourier Attention — Yu et al. | 2023 | Learnable inverse kernel + attention for high-frequency recovery | — |
| Aperture Phasor Field Enhancement — Cho et al. | 2024 | Learned aperture phasor field representation | — |
| Domain Reduction Strategy — Shim et al. | 2024 | Focus search on likely hidden object regions; 10× compute reduction | — |

### Transformers

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [NLOST: Non-Line-of-Sight Imaging with Transformer](https://openaccess.thecvf.com/content/CVPR2023/) — Li et al. | **CVPR 2023** | **First transformer for NLOS; spatial-temporal self-attention at multi-scale** | [Code](https://github.com/lhlawrence/NLOST) |
| [TransiT: Transient Imaging Transformer for Videographic NLOS Reconstruction](https://openaccess.thecvf.com/content/CVPR2025/) — Li et al. | **CVPR 2025** | **10 fps NLOS video; 64×64 from 16×16 sparse transients via transfer learning** | — |

### State-Space Models (Mamba)

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [ST-Mamba: Spatial-Temporal Mamba for NLOS Videography with Temporal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/) — Li et al. | **NeurIPS 2024** | **First Mamba model for NLOS; phasor field wave-based loss; temporal consistency** | — |

### Graph Neural Networks

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [DG-NLOS: Dual-Branch Graph Neural Network for NLOS Reconstruction](https://ojs.aaai.org/index.php/AAAI/article/view/) — Su et al. | **AAAI 2025** | **First GNN for NLOS; dual-branch albedo + depth; sparse structural features** | — |

### Diffusion Models

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Model-Guided Iterative Diffusion Sampling for NLOS Reconstruction](https://doi.org/) — Su et al. | JSPS 2024 | Diffusion model guided by NLOS physical forward model | — |

### Neural Implicit Representations

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Non-Line-of-Sight Imaging via Neural Transient Fields (NeTF)](https://ieeexplore.ieee.org/document/9645260) — Shen et al. | TPAMI 2021 | MLP neural transient field; unsupervised | [Code](https://github.com/zeromakerplus/NeTF_public) |
| [NLOS-NeuS: Non-Line-of-Sight Neural Implicit Surface](https://openaccess.thecvf.com/content/ICCV2023/) — Fujimura et al. | **ICCV 2023** | **SDF neural implicit surface for NLOS; smooth 3D surface reconstruction** | — |

### Dynamic NLOS Imaging

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Real-Time Non-Line-of-Sight Imaging of Dynamic Scenes](https://www.nature.com/articles/s43588-024-00711-5) — Ye et al. | **Nature Comput. Sci. 2024** | **4 fps NLOS video; spectrum filtering + interleaved scanning** |
| [ST-Mamba for NLOS Videography](https://proceedings.neurips.cc/paper_files/paper/2024/) — Li et al. | NeurIPS 2024 | Mamba-based temporal consistency for video NLOS |
| [TransiT: Transient Imaging Transformer](https://openaccess.thecvf.com/content/CVPR2025/) — Li et al. | CVPR 2025 | 10 fps at 64×64; 16×16 sparse transient input |
| Plug-and-Play Dynamic NLOS — Ye et al. | 2024 | PnP + deep denoiser; frequency-domain physics filtering |
| Dynamic NLOS via Single-Pixel Detection — Pei et al. | Opt. Express 2021 | Dynamic NLOS from single-pixel detector |

---

## New NLOS Scenes

### Two-Bounce NLOS

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Imaging Around Corners Using Transient Knowledge](https://doi.org/) — Vedaldi (Henley) et al. | ECCV 2020 | First two-bounce NLOS; hidden object blocks light between two relay surfaces |
| Role of Transients in Two-Bounce NLOS — Somasundaram et al. | 2023 | First systematic analysis of ToF in 2B-NLOS; tradeoffs for resolution and measurement count |

### Keyhole Imaging

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path](https://www.science.org/doi/10.1126/sciadv.abg2187) — Metzler et al. | Science Advances 2021 | Beamsplitter confocal NLOS without scanning; expectation-maximization reconstruction | — |

### Radar-Based NLOS

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Seeing Around Street Corners: Non-Line-of-Sight Detection and Tracking in-the-Wild Using Doppler Radar](https://openaccess.thecvf.com/content_CVPR_2020/html/Scheiner_Seeing_Around_Street_Corners_Non-Line-of-Sight_Detection_and_Tracking_in-the-Wild_CVPR_2020_paper.html) — Scheiner et al. | CVPR 2020 | Doppler radar NLOS for automotive vehicle detection |
| [HoloRadar: Full 3D NLOS Reconstruction via mmWave Radar on a Mobile Robot](https://proceedings.neurips.cc/paper_files/paper/2025/) — Lai et al. | **NeurIPS 2025** | **Full 3D scene reconstruction with single mmWave radar; physics-guided mirror-image ray modeling** |

### Acoustic NLOS

| Paper | Venue | Key Contribution | Code |
|-------|-------|-----------------|------|
| [Acoustic Non-Line-of-Sight Imaging](https://dl.acm.org/doi/10.1145/3306346.3322996) — Lindell et al. | SIGGRAPH 2019 | Microphone array acoustic NLOS; same algorithms as optical | [Code](https://github.com/computational-imaging/acoustic-nlos) |
| [Ultrasound NLOS Imaging via Synthetic Aperture](https://doi.org/) | Commun. Physics 2025 | Bat-echolocation frequency; cm-scale depth resolution; 3D multi-target reconstruction |

### Human Pose Estimation

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Optical Non-Line-of-Sight Physics-Based 3D Human Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2020/html/Isogawa_Optical_Non-Line-of-Sight_Physics-Based_3D_Human_Pose_Estimation_CVPR_2020_paper.html) — Isogawa et al. | CVPR 2020 | LSTM+physics for NLOS pose estimation |
| NLOS Human Pose Estimation — Xiao et al. | **OLE 2026** | Joint transient + volume feature extraction; multi-resolution pipeline for scale variation |

### Polarization-Based NLOS

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| [Polarized Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content_CVPR_2020/html/Tanaka_Polarized_Non-Line-of-Sight_Imaging_CVPR_2020_paper.html) — Tanaka et al. | CVPR 2020 | Polarizer as passive NLOS constraint |
| Polarization-Based Scanning-Free Single-Pixel NLOS — Zhou et al. | **PRL 2026** | Polarization-encoded speckle patterns; no scanning, no temporal resolution needed |

### Super-Field-of-View NLOS

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| Super-Field-of-View NLOS via Spatial Encoding — Li et al. | **Photonics Research 2026** | Translated PSF spatial encoding; FoV significantly beyond relay surface limits |

---

## Datasets

| Dataset | Paper | Year | Type | Size | Link |
|---------|-------|------|------|------|------|
| **LCT Confocal Dataset** | O'Toole et al. (Nature 2018) | 2018 | Active, confocal SPAD | Multiple scenes | [Link](https://github.com/m-toole/lct-nlos) |
| **f-k Dataset** | Lindell et al. (SIGGRAPH 2019) | 2019 | Active, confocal SPAD | Multiple objects | [Link](https://github.com/computational-imaging/nlos-fk) |
| **Galindo Benchmark** | Galindo et al. | 2019 | Active SPAD, benchmarking | Time-resolved measurements | [Link](https://doi.org/10.1364/OE.380140) |
| **NeTF Dataset** | Shen et al. (TPAMI 2021) | 2021 | Simulated + real transients | Multiple objects | [Link](https://github.com/zeromakerplus/NeTF_public) |
| **NLOS-Track** | Wang et al. (CVPR 2023) | 2023 | **Passive NLOS tracking** | First large-scale dynamic passive dataset; thousands of clips | [Link](https://github.com/JerrickLiu/AnytimeNLOS) |
| **NLOS Transient Renderer** | Royo et al. | 2022 | Synthetic renderer | Highly configurable NLOS scene renderer | — |
| **Fast Differentiable Transient Renderer** | Plack et al. | 2023 | Differentiable synthetic | Auto-differentiation support | — |

---

## Open-Source Code

| Repository | Paper | Description |
|------------|-------|-------------|
| [lct-nlos](https://github.com/m-toole/lct-nlos) | O'Toole et al. (Nature 2018) | LCT confocal NLOS reconstruction (MATLAB) |
| [nlos-fk](https://github.com/computational-imaging/nlos-fk) | Lindell et al. (SIGGRAPH 2019) | f-k migration wave-based NLOS (Python) |
| [acoustic-nlos](https://github.com/computational-imaging/acoustic-nlos) | Lindell et al. (SIGGRAPH 2019) | Acoustic NLOS imaging |
| [phasor-field](https://github.com/gliu7/phasor) | Liu et al. (SIGGRAPH 2020) | Phasor field virtual wave optics |
| [NeTF](https://github.com/zeromakerplus/NeTF_public) | Shen et al. (TPAMI 2021) | Neural transient field (unsupervised) |
| [NLOST](https://github.com/lhlawrence/NLOST) | Li et al. (CVPR 2023) | Transformer-based 3D NLOS reconstruction |
| [AnytimeNLOS / NLOS-Track](https://github.com/JerrickLiu/AnytimeNLOS) | Wang et al. (CVPR 2023) | PAC-Net passive tracking + NLOS-Track dataset |

---

## Related Surveys and Resources

| Title | Authors | Venue | Link |
|-------|---------|-------|------|
| **Non-line-of-sight Imaging** (comprehensive review) | Faccio et al. | **Nature Physics 2020** | [Link](https://www.nature.com/articles/s41567-020-0858-7) |
| **Non-Line-of-Sight Imaging: A Comprehensive Survey** | Geng, Hu, Chen et al. | IEEE TGRS 2022 (updated 2026) | [Paper] |
| Unlocking the Potential of NLOS Sensing | Scheiner et al. | 2022 | — |
| NLOS Imaging: A Review of Recent Advances | Chen et al. | 2023 | — |

**Related GitHub Repositories:**
- [Awesome Computational Photography](https://github.com/vinthony/awesome-deep-hdr)
- [Awesome Time-of-Flight Imaging](https://github.com/)
- [Awesome Inverse Problems in Imaging](https://github.com/)

---

## Summary Statistics

| Category | # Papers (pre-2022) | # Papers (2022–2026) | Total |
|----------|--------------------|-----------------------|-------|
| Active NLOS | ~45 | ~25 | ~70 |
| Passive NLOS | ~20 | ~8 | ~28 |
| Deep Learning | ~15 | ~20 | ~35 |
| New NLOS Scenes | ~5 | ~10 | ~15 |
| Datasets & Tools | ~5 | ~5 | ~10 |
| **Total** | **~90** | **~68** | **~158** |

---

## Citation

If this repository is useful for your research, please cite our survey paper:

```bibtex
@article{geng2022nlos,
  title   = {Non-Line-of-Sight Imaging: A Comprehensive Survey},
  author  = {Geng, Ruixu and Hu, Yang and Chen, Yan},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  year    = {2022},
  note    = {Updated 2022--2026}
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
  author    = {Lindell, David B and Tseng, Joh K and O'Toole, Matthew},
  booktitle = {ACM SIGGRAPH},
  year      = {2019}
}

@inproceedings{liu2020phasor,
  title     = {Virtual wave optics for non-line-of-sight imaging},
  author    = {Liu, Xiaochun and Guillen, Ibón and La Manna, Marco and Nam, Ji Hyun and Reza, Syed Azer and Le Mung, Toan and Jarabo, Adrian and Gutierrez, Diego and Velten, Andreas},
  booktitle = {ACM SIGGRAPH},
  year      = {2020}
}

@inproceedings{li2023nlost,
  title     = {{NLOST}: Non-Line-of-Sight Imaging with Transformer},
  author    = {Li, Yue and Cardona, Antoni and Wetzstein, Gordon},
  booktitle = {CVPR},
  year      = {2023}
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

1. **Add a paper:** Open a Pull Request with the paper details in the appropriate section. Format:  
   `[Title](link) — Authors | Venue Year | One-sentence contribution`

2. **Fix a broken link:** Open an Issue or PR.

3. **Add a code repository:** If a paper has released code that is not listed, please add it to the Open-Source Code section.

**Guidelines:**
- Papers should be peer-reviewed (conference or journal) or have significant community impact.
- Include a concise description of the key contribution.
- Link to the official paper page or arXiv preprint when possible.
- For code repositories, prefer official author repositories.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

<div align="center">

**Star this repository if you find it helpful!**

Maintained by [Ruixu Geng](mailto:gengruixu@std.uestc.edu.cn) · University of Electronic Science and Technology of China

*Last updated: May 2026*

</div>
