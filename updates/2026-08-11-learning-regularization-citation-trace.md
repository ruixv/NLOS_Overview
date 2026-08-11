# 2026-08-11 citation-tracing update: learning, regularization, and adaptive sampling gaps

## Status

Fresh arXiv / journal / venue / project-page search did not verify a direct NLOS-imaging publication newer than Sultan et al., **Iterating the transient light transport matrix for non-line-of-sight imaging**, *Nature Communications*, published online 2026-07-22.

This run instead identified a coherent set of **learning, regularization, adaptive sampling, and radar-ISAR NLOS gaps** that are not found by exact-title searches in the current repository. The public files were not overwritten in this run because the available connector path would require complete replacement of large, frequently edited artifacts. This note and the companion BibTeX file provide exact metadata and integration instructions for the next bounded source/PDF synchronization.

Companion BibTeX file: `egbib_20260811_learning_sampling_updates.bib`.

## Newly verified records to integrate

### 1. Frequency-domain multi-regularization-experts fusion for robust NLOS imaging

- **Paper:** Frequency-Domain Multi-Regularization-Experts Fusion for Robust Non-Line-of-Sight Imaging
- **Authors:** Qinghua Zhang, Xi Ling, Yuping Duan, Jun Liu
- **Venue:** *Pattern Recognition* 173, 112914 (2026)
- **DOI:** `10.1016/j.patcog.2025.112914`
- **Key:** `zhangFMoENLOS2026`
- **Why relevant:** Direct active ToF NLOS reconstruction. Introduces a frequency-domain mixture-of-experts framework; expert weights come from dual variables of an optimization model rather than a learned black-box gate. It explicitly extends LCT / frequency-domain / phasor-style reconstruction and compares against deep methods on real data.
- **Suggested category:** Deep Learning / Physics-Guided Reconstruction; Active NLOS / Reconstruction Algorithms.

### 2. Adaptive attention based on mixture distribution for zero-shot NLOS imaging

- **Paper:** Adaptive Attention Based on Mixture Distribution for Zero-Shot Non-Line-of-Sight Imaging
- **Authors:** Qinghua Zhang, Jun Liu, Yuping Duan
- **Venue:** *IEEE Signal Processing Letters* 32, 1690--1694 (2025)
- **DOI:** `10.1109/LSP.2025.3558458`
- **Key:** `zhangAdaptiveMixtureAttentionNLOS2025`
- **Why relevant:** Direct zero-shot NLOS reconstruction. Models non-Gaussian residuals with a mixture distribution and derives adaptive residual weights in the dual space, functioning as an optimization-derived attention mechanism without paired training.
- **Suggested category:** Optimization / Zero-Shot Reconstruction; Deep Learning / Physics-Guided Networks.

### 3. CMFormer

- **Paper:** CMFormer: Non-Line-of-Sight Imaging with a Memory-Efficient MetaFormer Network
- **Authors:** Shihao Zhang, Shaohui Jin, Hao Liu, Yue Li, Xiaoheng Jiang, Mingliang Xu
- **Venue:** *Optics and Lasers in Engineering* 187, 108875 (2025)
- **DOI:** `10.1016/j.optlaseng.2025.108875`
- **Key:** `zhangCMFormerNLOS2025`
- **Why relevant:** Direct learned active NLOS reconstruction. Uses a memory-efficient MetaFormer-like architecture with convolutional token mixing and cross-layer attention, enabling lower-memory 3D spatiotemporal processing and reported 8 FPS inference on consumer-grade GPUs.
- **Suggested category:** Deep Learning / Efficient Architectures.

### 4. Structure-guided adaptive total variation for passive NLOS

- **Paper:** Structure-Guided Adaptive Total Variation for Parameter-Free Passive Non-Line-of-Sight Imaging
- **Authors:** Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, Guorong Sui
- **Venue:** *Optics Express* 34(3), 5210--5224 (2026)
- **DOI:** `10.1364/OE.587111`
- **Key:** `zhangSGATVPassiveNLOS2026`
- **Why relevant:** Direct passive NLOS reconstruction with a conventional color camera. Computes spatially varying TV weights from structure guidance, reducing manual parameter sensitivity in passive reconstructions.
- **Suggested category:** Passive NLOS / Regularized Reconstruction.

### 5. Adaptive artifact cancellation

- **Paper:** Non-Line-of-Sight Imaging with Adaptive Artifact Cancellation
- **Authors:** Hongyuan Zhou, Ziyang Chen, Jumin Qiu, Sijia Zhong, Dejian Zhang, Tongbiao Wang, Qiegen Liu, Tianbao Yu
- **Venue:** *Optics and Laser Technology* 182, 112081 (2025)
- **DOI:** `10.1016/j.optlastec.2024.112081`
- **Key:** `zhouAdaptiveArtifactCancellationNLOS2025`
- **Why relevant:** Direct ToF active NLOS reconstruction. Introduces TOF-SSIM as a ground-truth-free reconstruction-quality metric and an adaptive artifact-cancellation backprojection method that is tested under confocal and non-confocal settings.
- **Suggested category:** Active NLOS / Robust Backprojection and Metrics.

### 6. TransDiff final TIP record

- **Paper:** TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces
- **Authors:** Xingyu Cui, Huanjing Yue, Shida Sun, Yue Li, Yusen Hou, Zhiwei Xiong, Jingyu Yang
- **Venue:** *IEEE Transactions on Image Processing* 34, 8018--8031 (2025)
- **DOI:** `10.1109/TIP.2025.3637694`
- **Key:** `cuiTransDiffNLOS2025`
- **Why relevant:** Direct unsupervised active NLOS reconstruction for aperture-limited relay surfaces. Uses latent diffusion with measurement consistency to recover fully sampled transients from undersampled inputs. This should be treated as final IEEE TIP metadata, not just a preprint or informal entry.
- **Suggested category:** Deep Learning / Diffusion and Aperture-Limited Acquisition.

### 7. Curvature regularization for under-sampled active NLOS

- **Paper:** Curvature Regularization for Non-Line-of-Sight Imaging from Under-Sampled Data
- **Authors:** Rui Ding, Juntian Ye, Qifeng Gao, Feihu Xu, Yuping Duan
- **Venue:** *IEEE Transactions on Pattern Analysis and Machine Intelligence* 46(12), 8474--8485 (2024)
- **DOI:** `10.1109/TPAMI.2024.3409414`
- **Key:** `dingCurvatureRegularizationNLOS2024`
- **Why relevant:** Direct active NLOS reconstruction from under-sampled transient measurements. Introduces object-domain and dual-domain curvature regularization and GPU-oriented ADMM solvers. It is a natural bridge between sparse scanning, SSCR, TransDiff, and optimized sampling.
- **Suggested category:** Active NLOS / Sparse and Irregular Acquisition; Optimization.

### 8. Adaptive spiral scanning for confocal NLOS

- **Paper:** Adaptive Spiral Scanning for Confocal Non-Line-of-Sight Imaging
- **Authors:** Tomoya Oyama, Yang Dixin, Mariko Isogawa
- **Venue:** *IEEE Open Journal of Signal Processing* 7, 482--491 (2026)
- **DOI:** `10.1109/OJSP.2026.3688052`
- **Key:** `oyamaAdaptiveSpiralNLOS2026`
- **Why relevant:** Direct confocal active NLOS reconstruction. Dynamically shifts the Archimedean spiral center according to sequentially estimated relay-wall return intensity, and uses Voronoi density compensation for nonuniform sampling.
- **Suggested category:** Active NLOS / Adaptive Scanning and Sampling.

### 9. Sparse aperture ISAR NLOS via detail-aware regularization

- **Paper:** Non-Line-of-Sight Sparse Aperture ISAR Imaging via a Novel Detail-Aware Regularization
- **Authors:** Yanbo Wen, Shunjun Wei, Xiang Cai, Yifei Hu, Mou Wang, Guolong Cui, Xiuhe Li, Jinhe Ran
- **Venue:** *IEEE Transactions on Geoscience and Remote Sensing* 62, 1--18 (2024)
- **DOI:** `10.1109/TGRS.2024.3447900`
- **Key:** `wenSparseApertureISARNLOS2024`
- **Why relevant:** Direct radar/ISAR NLOS moving-target imaging. Uses static-clutter filtering, detail-aware regularization, ADMM, and a fast learned variant for sparse-aperture mmWave moving-target NLOS imaging.
- **Suggested category:** Radar / RF / mmWave NLOS Imaging.

## Suggested README Latest Additions rows

Add these to the top section in roughly reverse chronological order, but avoid crowding the top of the README. If the homepage redesign is being planned, consider surfacing only the newest 8--12 entries and moving the rest into the paper explorer.

```markdown
| 2026 | [Frequency-Domain Multi-Regularization-Experts Fusion for Robust Non-Line-of-Sight Imaging](https://doi.org/10.1016/j.patcog.2025.112914) — Zhang et al. | Pattern Recognition 173, 112914 (2026) | Introduces FMoE, a frequency-domain mixture-of-experts reconstruction framework whose soft gating is derived from dual variables rather than learned heuristics, improving robust ToF NLOS reconstruction on synthetic and real data. |
| 2026 | [Structure-Guided Adaptive Total Variation for Parameter-Free Passive Non-Line-of-Sight Imaging](https://doi.org/10.1364/OE.587111) — Zhang et al. | Optics Express 34(3), 5210--5224 (2026) | Uses structure-guided adaptive TV weights for conventional-camera passive NLOS, reducing manual regularization tuning and improving robustness across scenes and color noise. |
| 2026 | [Adaptive Spiral Scanning for Confocal Non-Line-of-Sight Imaging](https://doi.org/10.1109/OJSP.2026.3688052) — Oyama et al. | IEEE Open Journal of Signal Processing 7, 482--491 (2026) | Dynamically shifts Archimedean spiral scans toward high-return relay regions and uses Voronoi density compensation to improve sparse confocal NLOS acquisition. |
| 2025 | [TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces](https://doi.org/10.1109/TIP.2025.3637694) — Cui et al. | IEEE Transactions on Image Processing 34, 8018--8031 (2025) | Uses latent diffusion with measurement consistency to recover dense transients from aperture-limited relay measurements, extending diffusion-based NLOS reconstruction toward constrained real acquisition. |
| 2025 | [Adaptive Attention Based on Mixture Distribution for Zero-Shot Non-Line-of-Sight Imaging](https://doi.org/10.1109/LSP.2025.3558458) — Zhang et al. | IEEE Signal Processing Letters 32, 1690--1694 (2025) | Models non-Gaussian residuals with a mixture distribution and derives dual-space adaptive weights as zero-shot attention for NLOS reconstruction. |
| 2025 | [CMFormer: Non-Line-of-Sight Imaging with a Memory-Efficient MetaFormer Network](https://doi.org/10.1016/j.optlaseng.2025.108875) — Zhang et al. | Optics and Lasers in Engineering 187, 108875 (2025) | Designs a memory-efficient MetaFormer-style network for 3D spatiotemporal NLOS data, enabling lower-memory learned reconstruction and fast inference. |
| 2025 | [Non-Line-of-Sight Imaging with Adaptive Artifact Cancellation](https://doi.org/10.1016/j.optlastec.2024.112081) — Zhou et al. | Optics and Laser Technology 182, 112081 (2025) | Introduces TOF-SSIM and an adaptive artifact-cancellation backprojection method for confocal and non-confocal NLOS reconstructions. |
| 2024 | [Curvature Regularization for Non-Line-of-Sight Imaging from Under-Sampled Data](https://doi.org/10.1109/TPAMI.2024.3409414) — Ding et al. | IEEE TPAMI 46(12), 8474--8485 (2024) | Adds object-domain and dual-domain curvature regularization with GPU ADMM solvers for under-sampled active NLOS reconstruction. |
| 2024 | [Non-Line-of-Sight Sparse Aperture ISAR Imaging via a Novel Detail-Aware Regularization](https://doi.org/10.1109/TGRS.2024.3447900) — Wen et al. | IEEE TGRS 62, 1--18 (2024) | Extends radar NLOS moving-target imaging with clutter suppression, detail-aware regularization, ADMM and a fast learned variant for sparse-aperture ISAR. |
```

## Suggested survey insertion plan

### `article/2active.tex`

Insert under sparse / under-scanned active acquisition:

```tex
A parallel line of work improves under-scanned acquisition by adapting either the sampling pattern or the inverse prior. Curvature-regularized models impose object-domain and joint signal--object-domain curvature penalties to stabilize reconstructions from sparse relay measurements \cite{dingCurvatureRegularizationNLOS2024}. Adaptive spiral scanning moves the Archimedean scan center toward high-return regions estimated online and compensates nonuniform sample density with Voronoi weights \cite{oyamaAdaptiveSpiralNLOS2026}. TransDiff instead treats the aperture-limited transient as a measurement-constrained diffusion problem and recovers the missing relay-aperture information without paired supervision \cite{cuiTransDiffNLOS2025}.
```

Insert under reconstruction / robust backprojection:

```tex
Artifact suppression has also been revisited from the measurement-quality perspective. Adaptive artifact cancellation constructs modified time-of-flight histograms, chooses parameters using a ground-truth-free TOF-SSIM criterion, and backprojects the corrected histograms for confocal and non-confocal NLOS reconstruction \cite{zhouAdaptiveArtifactCancellationNLOS2025}.
```

### `article/3passive.tex`

Insert in passive regularized reconstruction:

```tex
For passive ordinary-camera NLOS, structure-guided adaptive total variation computes spatially varying regularization weights from a preliminary structural estimate, reducing manual parameter tuning and improving robustness to color noise and scene changes \cite{zhangSGATVPassiveNLOS2026}.
```

### `article/4datadriven.tex`

Insert in learned/physics-guided reconstruction:

```tex
Recent learning-based solvers increasingly expose their physical frequency or residual models instead of relying only on generic encoder--decoders. CMFormer uses a memory-efficient MetaFormer-style architecture with convolutional token mixing and cross-layer attention for 3D spatiotemporal transients \cite{zhangCMFormerNLOS2025}. Mixture-distribution attention derives zero-shot spatial residual weights from an optimization dual formulation \cite{zhangAdaptiveMixtureAttentionNLOS2025}, while frequency-domain multi-regularization-experts fusion softly partitions the spectrum and fuses Wiener-filter experts through dual-variable gates \cite{zhangFMoENLOS2026}.
```

### `article/5newscenes.tex`

Insert in radar/RF/mmWave:

```tex
In moving-target radar NLOS, sparse-aperture ISAR imaging has been combined with static-clutter filtering and detail-aware regularization, yielding ADMM and learned-unfolded variants for high-resolution NLOS moving-target reconstruction under sparse echoes \cite{wenSparseApertureISARNLOS2024}.
```

## Validation requirements before claiming public synchronization

1. Merge `egbib_20260811_learning_sampling_updates.bib` into the consolidated bibliography, preserving stable keys and avoiding duplicate DOI entries.
2. Update README and homepage together; recompute the explorer count from unique paper objects rather than incrementing manually from a stale count.
3. Add survey prose to the semantic sections above; do not append a generic recent-work paragraph.
4. Run clean LaTeX/BibTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
5. Check undefined citations, repeated BibTeX entries, duplicate DOI entries, PDF text extraction, and rendered first/last page.
6. Only then claim `README.md`, `index.html`, `bare_jrnl.tex`, `egbib_merged_20260711.bib`, and `bare_jrnl.pdf` are synchronized.
