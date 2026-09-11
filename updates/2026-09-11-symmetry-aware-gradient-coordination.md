# 2026-09-11 consistency update: physics-guided gradient coordination for NLOS

## Verified missing paper

Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang, "Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging," *Symmetry*, 18(5):711, 2026. DOI: 10.3390/sym18050711. Published 23 April 2026.

This is a genuine transient NLOS reconstruction paper rather than a generic optimization paper that merely cites NLOS. It studies low-SNR transient NLOS reconstruction on synthetic and real captured scenes, with NLOST/LPP-style reconstruction backbones and explicit physical-consistency / sensor-calibration objectives. The contribution is to move physics guidance from scalar loss weighting to gradient-level coordination: PCGrad resolves soft conflicts, PhysGuard blocks anti-physical updates, learnable sensor calibration estimates nuisance parameters, and staged training delays hard physical constraints until a stable representation is learned. The full staged model reports 20.49 dB PSNR / 0.71 SSIM on unseen synthetic scenes versus 19.09 dB / 0.67 for the reproduced baseline, with qualitative validation on seven real scenes and robustness checks at 48, 28, and 25 dB SNR.

## Recommended integration

### README.md
Add to the 2026 learned / physics-guided reconstruction entries and Latest Additions:

| 2026 | [Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging](https://doi.org/10.3390/sym18050711) — Ling et al. | Symmetry 18(5), 711 (2026) | Recasts multi-constraint physics-guided NLOS training as a gradient-coordination problem rather than scalar loss balancing: PCGrad resolves conflicting reconstruction/physics gradients, PhysGuard blocks anti-physical updates, learnable sensor calibration estimates nuisance parameters, and staged training improves low-SNR generalization on synthetic and real transient data. |

### Survey source
Insert in the deep-learning / physics-guided reconstruction section near NLOST and learnable-physical-prior methods, not as a detached end-of-survey list. Suggested prose:

"Recent work has also shifted physics guidance from the architecture and loss level to the optimization dynamics themselves. Ling et al. treat reconstruction, measurement consistency, and sensor calibration as potentially conflicting gradient sources rather than terms to be combined by fixed scalar weights. Their symmetry-aware framework combines soft gradient projection, hard physics-preserving routing, learnable sensor calibration, and staged activation of physical constraints, improving robustness under low-SNR transient measurements. This direction complements physics-embedded architectures by asking not only which physical priors should be imposed, but also how competing priors should be allowed to update shared reconstruction parameters."

Cite with `\cite{lingSymmetryAwareGradientNLOS2026}`.

### Canonical bibliography
Merge `egbib_20260911_symmetry_gradient_coordination.bib` into the bibliography actually referenced by `bare_jrnl.tex` (currently the merged bibliography lineage), avoiding duplicate keys.

### Website / Paper Explorer
Add under 2026 > Active / Learned Reconstruction / Physics-guided learning. Contribution tags: `physics-guided`, `gradient coordination`, `sensor calibration`, `low-SNR`, `transient NLOS`.

### PDF consistency
After canonical bibliography and survey prose are integrated, rebuild `bare_jrnl.pdf` and verify that README, website/Paper Explorer, survey source, bibliography, and PDF all contain the entry.

## Safety note
Large public-facing files were not overwritten from truncated connector responses. This note records precise insertion content and locations until a run can safely patch the complete files.
