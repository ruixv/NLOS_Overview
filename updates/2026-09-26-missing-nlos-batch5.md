# NLOS literature gap update — 2026-09-26 batch 5

This run verified two relevant papers that were absent from repository-wide title/DOI search at discovery time. A safe BibTeX staging file is committed as `egbib_20260926_missing_nlos_batch5.bib`.

## 1. Learned light-cone transform for fast and accurate non-line-of-sight imaging

Xinqi Gao, Yijie Yang, Lianfang Wang, Xueying Liu, Yong Wang, Yuping Duan. Physical Review Applied 25(4), 044024 (2026). DOI: 10.1103/jsbg-c7l5. Published 9 April 2026.

Why include: L2CT is a direct learned continuation of the O'Toole et al. light-cone-transform lineage. It replaces fixed low-pass Wiener inversion with high-frequency-enhanced learnable filtering and combines this physics-derived reconstruction with spatiotemporal feature extraction and volume projection. APS reports evaluation on real measurements from different NLOS systems and roughly 5 dB PSNR improvement over LCT.

Suggested integration:
- README Latest Additions and 2026 milestone timeline: learned / physics-guided active transient NLOS.
- README Deep Learning for NLOS / Reconstruction Algorithms: position after classical LCT and alongside physics-informed learned inversion rather than as a generic black-box network.
- Website Paper Explorer: tags `Active`, `Transient`, `Learned Reconstruction`, `Physics-guided`, `LCT`.
- `bare_jrnl.tex`: in the learned reconstruction discussion immediately after the classical LCT lineage, noting the trajectory from analytic LCT/Wiener inversion to learnable frequency-selective inversion.
- Merge the staged BibTeX into the canonical bibliography and rebuild `bare_jrnl.pdf`.

## 2. Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding

Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, Li Zhao. Optics Express 34(14), 26271–26289 (2026). DOI: 10.1364/OE.601398. Published July 2026.

Why include: DAAM explicitly injects passive diffuse-scattering priors into attention: deformable convolution models anisotropic spatial structure, mean/std pooling models channel-wise SNR disparity, and a learned gate fuses both. It is therefore a useful bridge from generic passive U-Net/GAN/attention reconstruction toward physics-aware learned passive NLOS. The paper evaluates on NLOS-OT and reports improved PSNR/LPIPS over generic attention and recent passive-NLOS baselines.

Suggested integration:
- README Latest Additions and 2026 passive-NLOS timeline.
- README Passive NLOS / Deep Learning section: place with recent physics-aware, hyperspectral/polarization, and channel-adaptive passive reconstruction methods.
- Website Paper Explorer: tags `Passive`, `RGB`, `Deep Learning`, `Physics-aware Attention`, `Diffuse Reflection`.
- `bare_jrnl.tex`: passive learned-reconstruction paragraph, emphasizing the shift from generic feature attention to attention structures derived from diffuse-reflection and SNR priors.
- Merge the staged BibTeX into the canonical bibliography and rebuild `bare_jrnl.pdf`.

## Safety / consistency status

The canonical README is currently very large and connector responses truncate its JSON payload at a line boundary. This run therefore did not replace README/index/bare_jrnl.tex from partial content. The two entries above should be integrated in the next safe full-file edit together with other staged update notes, then the canonical bibliography and PDF should be rebuilt and checked for mutual consistency. No claim is made here that `bare_jrnl.pdf` has already been regenerated.
