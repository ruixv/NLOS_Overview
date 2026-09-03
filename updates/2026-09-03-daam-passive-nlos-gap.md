# 2026-09-03 verified NLOS gap: diffuse-aware passive NLOS

## Verified missing paper

**Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, Li Zhao, “Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,” Optics Express 34(14), 26271–26289 (2026). DOI: 10.1364/OE.601398.**

Verification sources: Optics Express/PubMed metadata. The paper is a direct passive NLOS reconstruction work, not a generic attention paper. It reconstructs occluded targets from ambient-light wall observations and introduces a diffuse-aware attention module (DAAM) built around two physically motivated priors: anisotropic diffuse-reflection structure and channel-dependent SNR. Deformable convolution supplies spatial attention, mean/std pooling supplies channel attention, and a learned gate fuses the two. The module is embedded in a residual-attention encoder and is evaluated against conventional passive-NLOS methods and generic attention alternatives using reconstruction quality metrics including PSNR and LPIPS.

Repository-wide exact-title and DOI searches on the current default branch returned no matches, so this is a genuine corpus gap.

## Why it belongs

Place this work in the passive-NLOS / learned-reconstruction trajectory, specifically after the classical light-transport / computational-periscopy lineage and alongside recent physics-aware passive deep reconstruction. It is useful because it marks a shift from generic CNN/Transformer capacity toward attention modules whose structure is explicitly conditioned by diffuse transport and SNR statistics.

Suggested survey trajectory sentence:

> Recent passive NLOS learning methods increasingly embed transport-specific priors rather than relying on generic visual attention. Wang et al. introduce diffuse-aware attention that combines anisotropic spatial sampling with channel-wise SNR cues, improving weak-signal preservation in ambient-light hidden-scene reconstruction.

## Precise integration targets

### README.md

Add to **Latest Additions** and to the 2026 passive/learned timeline:

`2026 | Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding — Wang et al. | Optics Express 34(14), 26271–26289 (2026) | Introduces diffuse-aware attention for passive NLOS, combining deformable-convolution spatial attention with mean/std channel attention derived from diffuse-reflection anisotropy and channel-wise SNR priors; improves weak-signal preservation and perceptual reconstruction quality.`

### index.html / Paper Explorer

Add one searchable paper record with:
- year: 2026
- modality: passive optical / ambient light
- task: hidden-image reconstruction
- method: physics-aware deep learning / attention
- venue: Optics Express
- DOI: 10.1364/OE.601398
- tags: passive NLOS, diffuse reflection, attention, low SNR, learned reconstruction

Also add it to the website’s 2026 timeline/latest-additions view.

### bare_jrnl.tex / article passive-learning section

Integrate semantically in the passive learned-reconstruction discussion, rather than appending as a standalone list item. Suggested prose preserving survey style:

`More recent passive approaches increasingly encode wall-transport statistics directly into the network architecture. Wang \emph{et al.}~\cite{wangDiffuseAwarePassiveNLOS2026} proposed a diffuse-aware attention module that combines deformable spatial attention, motivated by anisotropic diffuse reflections, with channel attention derived from signal-to-noise statistics. This physics-aware attention design improves preservation of weak wall-encoded signals compared with generic attention modules.`

### Bibliography

Merge the verified entry from `egbib_20260903_daam_passive_gap.bib` into the canonical bibliography using key `wangDiffuseAwarePassiveNLOS2026`, unless an equivalent canonical key already exists at merge time.

### bare_jrnl.pdf

After source integration, rebuild the survey and verify:
1. citation resolves without undefined references;
2. title/venue/year/DOI match the canonical bibliography;
3. README, website, LaTeX source, bibliography, and PDF all contain the same final metadata.

## Current-run literature checks

Fresh keyword searches covered active transient NLOS, passive NLOS, learned reconstruction, SPAD/single-photon systems, consumer LiDAR, RF/mmWave, acoustic, thermal, arbitrary relay surfaces, and differentiable transient rendering. High-priority forward-citation neighborhoods were rechecked around LCT, f-k migration, phasor fields, computational periscopy, dynamic/learned NLOS, and modality-expansion milestones. Several recent items surfaced again but are already in the repository or prior integration lineage, including Compact NLOS Imager at Long Range, TransVID, Learned LCT, Stereo NLOS, consumer-LiDAR NLOS, 3D Gaussian Transient Rendering, MARMOT, and TLTM iteration.

No second paper passed both the relevance and repository-missing checks at comparable confidence in this run.

## Safety note

The main README, website, canonical bibliography, and LaTeX survey are large files. The available GitHub write action replaces full file contents, while current safe reads can be truncated. To avoid data loss, this run does not overwrite those files blindly. The verified BibTeX staging file and this insertion note are committed instead. The PDF therefore has **not** been regenerated in this run.
