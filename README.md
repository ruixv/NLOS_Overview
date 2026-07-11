<div align="center">

# Awesome Non-Line-of-Sight (NLOS) Imaging

**A comprehensive, curated survey of Non-Line-of-Sight Imaging research**

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Papers](https://img.shields.io/badge/Papers-190+-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last_Updated-July_2026-red)]()

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

**Update run: 12 July 2026.** This section tracks newly found or newly completed entries that were not explicitly covered in the previous README / homepage snapshot.

| Year | Paper | Venue / Status | Why it matters |
|------|-------|----------------|----------------|
| 2026 | [X-band Radar Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html) — Du et al. | CVPR 2026 | Introduces a learned, geometry-aware X-band radar NLOS reconstruction system; converts normally diffuse optical transport into predominantly specular long-wavelength transport and experimentally reconstructs hidden objects at ranges up to 40 m. |
| 2026 | [Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging](https://doi.org/10.1016/j.optlaseng.2025.109514) — Zhang et al. | Optics and Lasers in Engineering 2026 | Uses a self-supervised continuous neural illumination field and differentiable intensity rendering for two-bounce NLOS reconstruction without binary shadow segmentation, reaching centimeter-scale detail in large hidden spaces under low-contrast and ambient-light interference. |
| 2026 | [CUDA-accelerated non-line-of-sight imaging with irregular relay surfaces](https://doi.org/10.1016/j.optlaseng.2025.109591) — Sun et al. | Optics and Lasers in Engineering 2026 | GPU-accelerated filtered backprojection for measurements acquired on irregular, non-planar relay surfaces, reducing the practical cost of geometry-aware active NLOS reconstruction. |
| 2025 | [TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces](https://doi.org/10.1109/TIP.2025.3637694) — Cui et al. | IEEE TIP 2025 | Uses latent diffusion and unsupervised measurement consistency to synthesize/recover dense transient information from aperture-limited relay measurements. |
| 2025 | [Under-scanning non-line-of-sight imaging based on convolution approximation and optimization](https://doi.org/10.1063/5.0266391) — Miao et al. | APL Photonics 2025 | DO-NLOS combines a convolution approximation with optimization to reconstruct hidden scenes from strongly under-scanned transient measurements. |
| 2025 | [Physics to the Rescue: Deep Non-line-of-sight Reconstruction for High-speed Imaging](https://doi.org/10.1109/TPAMI.2022.3203383) — Mu et al. | IEEE TPAMI 2025 | Embeds wave-propagation and volume-rendering priors in a neural model for robust high-speed NLOS reconstruction from approximate real-time capture models. |
| 2025 | [Sub-pixel resolving modulation for non-line-of-sight imaging](https://doi.org/10.1364/OE.569102) — Zhang et al. | Optics Express 2025 | Introduces sub-pixel modulation to improve spatial resolving power beyond the native relay-wall sampling grid. |
| 2024 | [Virtual Scanning: Unsupervised Non-line-of-sight Imaging from Irregularly Undersampled Transients](https://proceedings.neurips.cc/paper_files/paper/2024/file/c58437945392cec01e0c75ff6cef901a-Paper-Conference.pdf) — Cui et al. | NeurIPS 2024 | Learns from irregularly undersampled transients without paired supervision, combining virtual scanning, measurement consistency, and a physics-guided SURE denoiser. |
| 2024 | [Real-time non-line-of-sight computational imaging using spectrum filtering and motion compensation](https://doi.org/10.1038/s43588-024-00722-4) — Ye et al. | Nature Computational Science 2024 | Couples spectrum-domain filtering with motion compensation/interleaved scanning to deliver room-scale real-time NLOS video. |
| 2024 | [Plug-and-play algorithms for dynamic non-line-of-sight imaging](https://doi.org/10.1145/3665139) — Ye et al. | ACM TOG 2024 | A flexible dynamic-NLOS inverse framework that combines wave-physics filtering with learned denoiser priors for temporally consistent hidden-scene video. |
| 2024 | [Domain Reduction Strategy for Non Line of Sight Imaging](https://arxiv.org/abs/2308.10269) — Shim et al. | ECCV 2024 | Periodically prunes empty hidden-space regions during inverse rendering, accelerating geometry/albedo recovery under sparse and general acquisition setups. |
| 2026 | [Non-Line-of-Sight imaging using raster scanning at NIR wavelength](https://arxiv.org/abs/2607.04183) — Roueinfar, Salmanian | arXiv 2026 | Demonstrates a low-cost 808 nm NIR raster-scanning active NLOS setup with pan-tilt illumination and NIR-camera capture over three hidden targets; useful as a simple hardware/acquisition baseline rather than a new inverse-model frontier. |
| 2026 | [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | SIGGRAPH 2026 | Uses 3D Gaussian primitives and differentiable transient rendering; targets spatially limited, non-planar, arbitrary relay surfaces. |
| 2026 | [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865) — Somasundaram et al. | arXiv 2026 | Demonstrates plug-and-play NLOS using smartphone-grade / consumer LiDAR with motion-induced aperture sampling. |
| 2026 | [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals](https://arxiv.org/abs/2605.29098) — Lu et al. | arXiv 2026 | GeRaF 2.0: neural RF geometry reconstruction that combines LoS visual priors with NLoS radar propagation. |
| 2026 | [Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware](https://arxiv.org/abs/2604.07032) — Tosi et al. | arXiv 2026 | 5G/mmWave ISAC proof-of-concept for fully NLOS intrusion detection and tracking with large-surface reflections, range-Doppler processing, and PHD filtering. |
| 2026 | [Radar Cross Section Characterization of Quantized Reconfigurable Intelligent Surfaces](https://arxiv.org/abs/2603.27961) — Yasmeen et al. | arXiv 2026 | Complements RIS around-corner radar sensing by characterizing one-bit/quantized RIS RCS and experimentally recovering micro-Doppler signatures in non-specular or shadowed regions. |
| 2026 | [DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs](https://arxiv.org/abs/2604.16201) — Behari et al. | arXiv 2026 | Large-scale low-cost LiDAR space-time histogram dataset for data-driven NLOS spatial reasoning. |
| 2026 | [NLOS-Aided Joint OTA Synchronization and Off-Grid Imaging for Distributed MIMO Systems](https://arxiv.org/abs/2603.13981) — Tong et al. | arXiv 2026 | Jointly refines over-the-air synchronization and sparse off-grid environment imaging in distributed MIMO/ISAC by exploiting reconstructed NLOS components. |
| 2026 | [A comprehensive study of time-of-flight non-line-of-sight imaging](https://arxiv.org/abs/2603.09548) — Marco et al. | arXiv 2026 | Benchmark-style comparative study unifying ToF NLOS forward/inverse models under common hardware constraints. |
| 2026 | [Exploiting Double-Bounce Paths in Snapshot Radio SLAM: Bounds, Algorithms and Experiments](https://arxiv.org/abs/2603.02832) — Zhang et al. | arXiv 2026 | Shows that higher-order NLoS radio paths can improve snapshot mmWave SLAM and reveal landmarks hidden to single-bounce models. |
| 2026 | [Cramer-Rao Bounds for Target Parameter Estimation in a Bi-Static IRS-Assisted Radar Configuration](https://arxiv.org/abs/2603.01660) — Sanjeeva Reddy S, Vinod Veera Reddy | arXiv 2026 | Characterizes angle-estimation limits for a passive-IRS bistatic NLOS radar geometry, clarifying what reconfigurable RF relay surfaces can theoretically recover. |
| 2026 | [Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface](https://arxiv.org/abs/2602.11471) — Yasmeen et al. | arXiv 2026 | RIS-assisted around-corner radar sensing; steers energy into NLOS regions and recovers human micro-Doppler signatures. |
| 2026 | [Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface](https://arxiv.org/abs/2602.11473) — Yasmeen et al. | arXiv 2026 | Extends RIS-assisted around-corner radar toward practical one-bit dual-beam RIS configurations, benchmarking beam steering and radar cross-section against metal and ideal single-beam RIS baselines. |
| 2026 | [Beyond λ/2: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?](https://arxiv.org/abs/2602.07515) — Chen et al. | arXiv 2026 | RIS-aided NLOS bistatic MIMO radar localization with EMVS polarization cues and phase-disambiguating array geometry. |
| 2026 | [RIS-aided Radar Detection Architectures with Application to Low-RCS Targets](https://arxiv.org/abs/2601.10846) — Colone et al. | arXiv 2026 | Designs RIS-aided monostatic/bistatic radar detection architectures that redirect low-RCS target energy back toward the radar. |
| 2026 | [Backscatter Assisted Indoor NLOS Positioning](https://arxiv.org/abs/2606.17325) — Ruttik et al. | arXiv 2026 | Uses passive backscatter devices as virtual anchors for RF NLOS indoor positioning in corridors. |
| 2026 | [Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy](https://arxiv.org/abs/2601.12257) — Raji, Murray-Bruce | arXiv 2026 | Extends passive shadow-based computational periscopy to 3D from a single ordinary NLOS photograph via an SNLLS model and a physics-inspired neural solver. |
| 2025 | [MITO: Enabling Non-Line-of-Sight Perception using Millimeter-waves through Real-World Datasets and Simulation Tools](https://arxiv.org/abs/2502.10259) — Dodds et al. | arXiv 2025 | Dataset and simulation tooling for mmWave NLOS perception with paired LOS/NLOS captures and RGB-D/mask supervision. |
| 2025 | [See and Beam: Leveraging LiDAR Sensing and Specular Surfaces for Indoor mmWave Connectivity](https://arxiv.org/abs/2511.09840) — Bandari et al. | arXiv 2025 | Uses LiDAR-visible specular surfaces to infer NLOS mmWave reflection paths and localize users for beam steering. |
| 2025 | [3D Reconstruction from Transient Measurements with Time-Resolved Transformer](https://arxiv.org/abs/2510.09205) — Li et al. | arXiv 2025 | TRT/TRT-NLOS spatio-temporal transformer for photon-efficient LOS/NLOS transient 3D reconstruction with code and datasets. |
| 2025 | [TransiT: Transient Transformer for Non-line-of-sight Videography](https://arxiv.org/abs/2503.11328) — Li et al. | ICCV 2025 | Transient transformer for high-speed NLOS videography; reconstructs 10 fps videos from sparse $16\times16$ transient scans with transfer learning for synthetic-to-real adaptation. |
| 2025 | [Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging](https://arxiv.org/abs/2508.09655) — Wang et al. | arXiv 2025 | Introduces NANO: a noise-conditioned neural-operator inverse solver for robust NLOS reconstruction under sparse scanning and photon-starved noise. |
| 2025 | [Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform](https://arxiv.org/abs/2508.02003) — Wei et al. | arXiv 2025 | Recasts hidden scenes as 2D functions and reduces runtime/memory by orders of magnitude for lightweight NLOS. |
| 2025 | [mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera](https://arxiv.org/abs/2508.02348) — Park et al. | arXiv 2025 | Uses camera-extracted road layout to interpret mmWave radar point clouds for around-corner pedestrian localization. |
| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Brings self-supervised masked pretraining to NLOS transients and introduces TransVerse-scale transient data for downstream NLOS tasks. |
| 2025 | [Passive acoustic non-line-of-sight localization without a relay surface](https://arxiv.org/abs/2506.08471) — Sommer, Katz | arXiv 2025 | Uses knife-edge diffraction and doorway/corner geometry for passive 3D acoustic localization without conventional relay surfaces. |
| 2025 | [mmMirror: Device Free mmWave Indoor NLoS Localization Using Van-Atta-Array IRS](https://arxiv.org/abs/2505.10816) — Yan et al. | arXiv 2025 | Uses a Van-Atta-array IRS with commodity FMCW radar for device-free around-corner / NLOS localization. |
| 2025 | [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://arxiv.org/abs/2505.08240) — Shi et al. | arXiv 2025 | Tag-assisted mmWave NLOS localization using multipath, HFD modulation, and FS-MUSIC; relevant to RF NLOS sensing/localization rather than full imaging. |
| 2025 | [Geometric Constrained Non-Line-of-Sight Imaging](https://arxiv.org/abs/2503.17992) — Liu et al. | arXiv 2025 | Joint albedo/surface reconstruction with normal-field regularization for higher-detail hidden geometry. |
| 2025 | [Dual-branch Graph Feature Learning for NLOS Imaging](https://arxiv.org/abs/2502.19683) — Su et al. | arXiv 2025 | DG-NLOS uses graph feature learning with separate albedo and depth branches to reduce 3D-grid cost while jointly reconstructing hidden appearance and geometry. |
| 2025 | [Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms](https://arxiv.org/abs/2501.05244) — Sultan et al. | arXiv 2025 | Uses NUFFT/SFFT to support irregular relay sampling and flexible hidden-volume sampling while retaining FFT-like scalability. |
| 2025 | [SuperEx: Enhancing Indoor Mapping and Exploration using Non-Line-of-Sight Perception](https://arxiv.org/abs/2510.10506) — Garg, Dave | arXiv 2025 | Integrates single-photon LiDAR NLOS perception into indoor mapping and exploration through hidden-space carving. |
| 2025 | [mitransient: Transient light transport in Mitsuba 3](https://arxiv.org/abs/2510.25660) — Royo et al. | arXiv 2025 | Differentiable transient-rendering toolkit for time-resolved simulation, NLOS scenes, polarization, and capture noise. |
| 2024 | [Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging](https://arxiv.org/abs/2412.10300) — Sultan et al. | arXiv 2024 | Treats a measured relay-surface TLTM as a first-order system that can be computationally focused into the hidden scene to obtain second-order transport, relighting, and dual photography. |
| 2024 | [Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR](https://arxiv.org/abs/2410.03555) — Young et al. | arXiv 2024 | Uses SPAD / single-photon LiDAR NLOS occupancy perception to guide robot navigation around occluded corners. |
| 2024 | [Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors](https://arxiv.org/abs/2409.14011) — Sun et al. | arXiv 2024 | Learns path-compensation and adaptive phasor-field priors for cross-system and low-SNR NLOS generalization. |
| 2024 | [Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging](https://arxiv.org/abs/2407.18574) — Cho et al. | arXiv 2024 | LEAP predicts clean full-aperture phasor fields from noisy partial measurements, enabling high-quality NLOS reconstruction with $16\times$--$64\times$ fewer samples and smaller scan areas. |
| 2024 | [Ptychographic non-line-of-sight imaging for depth-resolved visualization of hidden objects](https://arxiv.org/abs/2405.11115) — Song et al. | arXiv 2024 | Uses coded ptychography and relay-wall modulation to recover depth-resolved hidden objects and the wall modulation profile. |
| 2024 | [PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot](https://arxiv.org/abs/2404.05024) — Kannapiran et al. | arXiv 2024 | Uses a moving RGB camera on a small robot/drone and an attention-based temporal model to choose relay planes and estimate hidden-person 2D trajectories in real time. |
| 2024 | [Passive None-line-of-sight imaging with arbitrary scene condition and detection pattern in small amount of prior data](https://arxiv.org/abs/2404.06015) — Gui et al. | arXiv 2024 | HDPS estimates passive NLOS transport/target structure from limited prior data, targeting arbitrary scene conditions and detection patterns without retraining a separate model per setup. |
| 2024 | [Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins](https://arxiv.org/abs/2401.06891) — Tornielli Bellini et al. | arXiv 2024 | Uses static passive electromagnetic-skin modules to focus radar energy into NLOS regions and synthesize multi-view near-field radar images. |
| 2024 | [Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding](https://arxiv.org/abs/2404.05977) — Wang et al. | arXiv 2024 | Uses an event camera for dynamic diffusion-spot features and a physics-embedded model for passive NLOS imaging of moving objects. |
| 2023 | [Self-Calibrating, Fully Differentiable NLOS Inverse Rendering](https://arxiv.org/abs/2309.12047) — Choi et al. | SIGGRAPH Asia 2023 | Couples diffraction-based volumetric NLOS reconstruction with differentiable transient rendering and self-calibrates imaging parameters directly from measured transients. |
| 2023 | [Non-line-of-sight imaging in the presence of scattering media using phasor fields](https://arxiv.org/abs/2311.09223) — Luesia et al. | arXiv 2023 | Extends phasor-field NLOS analysis to hidden scenes submerged in scattering media, empirically testing robustness under fog/smoke-like volumetric scattering. |
| 2023 | [Non-line-of-sight imaging with arbitrary illumination and detection pattern](https://www.nature.com/articles/s41467-023-38898-4) — Liu et al. | Nature Communications 2023 | Bayesian CC-SOCR framework for arbitrary illumination/detection patterns, irregular relay sampling, and albedo/surface-normal reconstruction. |
| 2023 | [NLOS-NeuS: Non-line-of-sight Neural Implicit Surface](https://arxiv.org/abs/2303.12280) — Fujimura et al. | ICCV 2023 | Extends Neural Transient Fields to SDF-based neural implicit surfaces for smooth, high-detail hidden-surface reconstruction with first-returning-photon constraints. |
| 2023 | [Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources](https://www.nature.com/articles/s41598-023-31490-2) — Boger-Lombard et al. | Scientific Reports 2023 | Uses passive acoustic correlations from uncontrolled broadband noise to recover Green functions and localize hidden around-corner targets. |
| 2023 | [Non-line-of-sight reconstruction via structure sparsity regularization](https://arxiv.org/abs/2308.02782) — Huang et al. | arXiv 2023 | DLCT-based reconstruction with nuclear-norm structure sparsity regularization for low-SNR transient data. |
| 2023 | [Non-line-of-sight snapshots and background mapping with an active corner camera](https://www.nature.com/articles/s41467-023-39327-2) — Seidel et al. | Nature Communications 2023 | Active corner camera reconstructs moving foreground objects and maps stationary hidden background. |
| 2022 | [Differentiable Transient Rendering](https://arxiv.org/abs/2206.06193) — Yi et al. | ACM TOG 2021 | Provides a differentiable transient path-integral framework that supports NLOS tracking with non-planar relay walls and two-corner NLOS settings, underpinning later inverse-rendering NLOS work. |
| 2022 | [Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction](https://arxiv.org/abs/2203.08657) — Grau et al. | arXiv 2022 | Uses an implicit surface representation to reason about NLOS recoverability and self-occlusion, recovering adaptively tessellated hidden surfaces beyond conservative Fermat-path visibility criteria. |
| 2022 | [High-resolution non-line-of-sight imaging employing active focusing](https://www.nature.com/articles/s41566-022-01009-8) — Cao et al. | Nature Photonics 2022 | Uses wavefront shaping / active focusing to push optical NLOS toward sub-millimeter hidden-target resolution. |
| 2022 | [Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization](https://arxiv.org/abs/2211.15367) — Liu et al. | arXiv 2022 | Extends sparse active NLOS reconstruction with mixed-dimensional priors over measured signals, virtual confocal signals, and hidden surfaces; demonstrates few-shot recovery from very coarse confocal grids. |
| 2022 | [Cramer-Rao Lower Bound Optimization for Hidden Moving Target Sensing via Multi-IRS-Aided Radar](https://arxiv.org/abs/2210.05812) — Esmaeilbeig et al. | arXiv 2022 | Early multi-IRS hidden moving-target sensing work that optimizes Doppler-aware IRS phase shifts via CRLB-guided design. |
| 2022 | [Seeing Around Obstacles with Terahertz Waves](https://arxiv.org/abs/2205.05066) — Cui, Trichopoulos | arXiv 2022 | THz / sub-THz around-obstacle imaging using lossy-mirror environmental surfaces. |
| 2022 | [Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera](https://arxiv.org/abs/2209.13300) — Wang et al. | arXiv 2022 | Introduces event-based passive NLOS for moving targets and the NLOS-ES event-camera dataset. |
| 2021 | [Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging](https://arxiv.org/abs/2103.12622) — Marco et al. | arXiv 2021 | Extends phasor-field virtual wave optics from hidden-geometry reconstruction to hidden-scene light-transport analysis, creating virtual projector-camera pairs for relighting and separation of direct, first-order indirect, and higher-order indirect components. |
| 2021 | [Automatic calibration of time of flight based non-line-of-sight reconstruction](https://arxiv.org/abs/2105.10603) — Sadhu et al. | arXiv 2021 | Makes ToF NLOS reconstruction robust to relay-wall illumination/detection miscalibration by jointly optimizing hidden albedo and virtual scan positions in a differentiable forward model. |
| 2021 | [Non-line-of-sight imaging with picosecond temporal resolution](https://arxiv.org/abs/2106.15798) — Wang et al. | Physical Review Letters 2021 | Up-conversion single-photon detector enables picosecond-scale timing and much finer axial NLOS resolution. |
| 2021 | [Single photon imaging and sensing of obscured objects around the corner](https://arxiv.org/abs/2106.08210) — Zhu et al. | arXiv 2021 | Uses picosecond-gated single-photon detection generated by quantum frequency conversion for photon-efficient around-corner positioning, surface profiling, and vibration sensing. |
| 2021 | [Fast Non-line-of-sight Imaging with Two-step Deep Remapping](https://arxiv.org/abs/2101.10492) — Zhu, Cai | arXiv 2021 | Uses inexpensive commercial LiDAR and a generative two-step deep remapping strategy for fast, high-fidelity, full-color NLOS reconstruction. |
| 2020 | [Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier](https://arxiv.org/abs/2006.02600) — Reza et al. | arXiv 2020 | Quantifies spurious phasor-field signals caused by partial optical coherence, linking aperture roughness, coherence, and P-field signal-to-noise limits. |
| 2020 | [Nonparaxial phasor-field propagation](https://arxiv.org/abs/2006.13775) — Dove, Shapiro | arXiv 2020 | Extends phasor-field propagation beyond the Fresnel/paraxial assumption using Rayleigh--Sommerfeld theory, closer to wide-angle reflective NLOS geometries. |
| 2020 | [Paraxial phasor-field physical optics](https://arxiv.org/abs/2004.14239) — Dove, Shapiro | arXiv 2020 | Shows that ordinary lenses can focus or project phasor fields through diffusers, bridging computational virtual-wave NLOS and physical P-field optics. |
| 2020 | [Efficient Non-Line-of-Sight Imaging from Transient Sinograms](https://arxiv.org/abs/2008.02787) — Isogawa et al. | arXiv 2020 | Introduces circular confocal NLOS (C2NLOS) scanning and transient-sinogram reconstruction, reducing relay-wall measurements while preserving hidden-position and image recovery. |
| 2019 | [Analysis of Feature Visibility in Non-Line-of-Sight Measurements](https://openaccess.thecvf.com/content_CVPR_2019/html/Liu_Analysis_of_Feature_Visibility_in_Non-Line-of-Sight_Measurements_CVPR_2019_paper.html) — Liu, Bauer, Velten | CVPR 2019 | Systematically analyzes which hidden-scene features are recoverable from transient NLOS measurements, clarifying orientation-, aperture-, and capture-geometry-dependent visibility limits that later reconstruction methods must respect. |
| 2019 | [Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path](https://arxiv.org/abs/1912.06727) — Metzler et al. | IEEE TCI 2021 | Introduces single-optical-path active NLOS imaging/tracking; uses hidden-object motion and EM/unknown-view tomography to recover shape and trajectory when only keyhole-like access is available. |
| 2019 | [Wave-like Properties of Phasor Fields: Experimental Demonstrations](https://arxiv.org/abs/1904.01565) — Reza et al. | arXiv 2019 | Experimentally validates wave-like phasor-field behavior and introduces P-field optical elements for practical virtual-wave NLOS systems. |
| 2019 | [Coherent control of light for non-line-of-sight imaging](https://arxiv.org/abs/1908.04094) — Starshynov et al. | arXiv 2019 | Uses coherent phase control / wavefront shaping and the speckle memory effect to refocus light behind an obstacle, enabling sub-millimeter active NLOS imaging. |
| 2019 | [Direct Object Recognition Without Line-of-Sight Using Optical Coherence](https://arxiv.org/abs/1903.07705) — Lei et al. | arXiv 2019 | Uses coherent illumination and diffuse-wall speckle patterns with a deep neural network for direct hidden-object recognition without reconstructing a full hidden 3D scene. |
| 2019 | [Non-line-of-sight 3D imaging with a single-pixel camera](https://arxiv.org/abs/1903.04812) — Musarra et al. | arXiv 2019 | Uses a DMD-based time-resolved single-pixel camera with SPAD/PMT detection for scanning-free, full-color 3D NLOS reconstruction and sub-second Hadamard acquisition. |
| 2019 | [Paraxial Theory of Phasor-Field Imaging](https://arxiv.org/abs/1903.02365) — Dove, Shapiro | arXiv 2019 | Provides a paraxial wave-optics and Wigner-distribution analysis of phasor-field imaging, clarifying which occluded and unoccluded geometries are supported by virtual-wave NLOS models. |
| 2017 | [Non-line-of-sight Imaging with Partial Occluders and Surface Normals](https://arxiv.org/abs/1711.07134) — Heide et al. | ACM TOG 2019 | Introduces a factored NLOS light-transport model that accounts for partial occlusions and surface normals in time-resolved active NLOS reconstruction. |
| 2017 | [Exploiting Occlusion in Non-Line-of-Sight Active Imaging](https://arxiv.org/abs/1711.06297) — Thrampoulidis et al. | arXiv 2017 | Shows that natural hidden-scene occluders can encode useful structure and may reduce reliance on calibrated ultrafast time-resolved hardware. |

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
```

---

## Taxonomy

This repository groups papers by **acquisition regime**, **forward model**, **inverse algorithm**, and **sensor modality**. The README highlights the newest additions; the website provides a searchable paper explorer and the PDF survey provides the detailed narrative.

---

## Citation

If this repository or survey is useful for your research, please cite the original survey:

```bibtex
@article{geng2022recent,
  title={Recent Advances on Non-Line-of-Sight Imaging: Conventional Physical Models, Deep Learning, and New Scenes},
  author={Geng, Ruixu and Hu, Yang and Chen, Yan},
  journal={APSIPA Transactions on Signal and Information Processing},
  volume={11},
  number={1},
  year={2022},
  doi={10.1561/116.00000019}
}
```

---

## Contributing

Corrections, missing papers, and pull requests are welcome. Please include accurate metadata (title, authors, venue/status, year, DOI/arXiv/project links) and a short note explaining why the paper is relevant to NLOS imaging.
