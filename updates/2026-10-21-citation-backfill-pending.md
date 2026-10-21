# 2026-10-21 — Core-citation NLOS backfill and PDF build status

## Newly integrated peer-reviewed papers

1. Stirling Scholes and Jonathan Leach, **Path Tracing-Inspired Modeling of Non-Line-of-Sight SPAD Data**, *Sensors* 24(20), 6522 (published 10 October 2024), DOI: https://doi.org/10.3390/s24206522. A physics- and sensor-aware Unreal Engine forward model predicts dToF SPAD transient photon-detection likelihoods with material reflectance, occlusion, extended surfaces and secondary scattering. This is simulation/measurement modeling, not a new 3D reconstruction algorithm. The paper directly cites Velten 2012, O'Toole 2018 LCT, Liu 2020 phasor fields, and Geng et al. 2022 survey, among others. Open-source simulation data: https://github.com/HWQuantum/NLOS-SIM.

2. Min Tu, Qiurong Yan, Yongjian Zheng, Xiancheng Xiong, Quan Zou, Qianling Dai and Xiaoqiang Lu, **Poisson Noise Suppression for Single-Photon Non-Line-of-Sight Imaging Based on Deep Learning**, *Laser & Optoelectronics Progress* 60(20), 2011003 (2023), DOI: https://doi.org/10.3788/LOP222969. AEF-Net attention-enhanced Poisson denoising trained on Monte Carlo-simulated NLOS measurements, with physical imaging-system validation. Found by following the 2024 paper's reference list; direct citation of a specific Core paper was not independently established.

## Integration map

- README.md: Latest Additions table and milestone timeline (2023 learned photon denoising; 2024 SPAD forward simulation).
- index.html: historical acquisition/forward-model research paragraph.
- data/papers-source.html: two searchable paper-explorer records and dated development-timeline entries.
- article/2active.tex: SPAD forward-data simulation immediately before the ToF-based forward-model subsection.
- article/4datadriven.tex: AEF-Net historical denoising precursor immediately before SPAD-aware physics-informed cascade learning.
- bare_jrnl.tex: the existing \\input declarations already include article/2active.tex and article/4datadriven.tex; the main file itself was left unchanged because its comment-only write was blocked. The substantive survey sections are updated.
- egbib_merged_20260711.bib: two publisher-verified DOI/venue BibTeX entries.

## PDF status — action required

The source files are updated, but **bare_jrnl.pdf has not been regenerated or uploaded**. The previously verified PDF Git blob SHA is `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`. A full checkout with figures and styles is needed; compile using pdflatex → bibtex → pdflatex → pdflatex, inspect the build log for missing resources/unresolved citations, and commit the changed PDF binary. The local container currently cannot resolve github.com, so no PDF build is claimed.
