# 18 July 2026 NLOS citation-gap follow-up

STATUS: STAGED — public sources and PDF have not yet been rebuilt.

## Scope

This update follows forward citations and closely adjacent descendants of the active transient milestones (Velten 2012, LCT, f-k migration, phasor fields), passive computational periscopy, and recent learned/commodity-sensor NLOS branches. Each record below was checked against the current README, homepage paper array, survey section sources, update logs, and consolidated bibliography before staging.

## Verified missing records

1. **Learning-based NLOS imaging with Kolmogorov-Arnold network-enhanced transformer** — Mengge Liu, Shaohui Jin, Zhicheng Liu, Zhihang Yan, Hao Liu, Mingliang Xu. *Optics & Laser Technology* 192, 113463 (2025). DOI: `10.1016/j.optlastec.2025.113463`.
2. **Feature enhanced non-line-of-sight imaging using graph model in latent space** — Weihao Xu, Songmao Chen, Dingjie Wang, Yuyuan Tian, Ning Zhang, Wei Hao, Xiuqin Su. *Optics & Laser Technology* 181, 111538 (2025). DOI: `10.1016/j.optlastec.2024.111538`.
3. **Non-line-of-sight imaging with adaptive artifact cancellation** — Hongyuan Zhou, Ziyang Chen, Jumin Qiu, Sijia Zhong, Dejian Zhang, Tongbiao Wang, Qiegen Liu, Tianbao Yu. *Optics & Laser Technology* 182, 112081 (2025). DOI: `10.1016/j.optlastec.2024.112081`.
4. **Adaptive Attention Based on Mixture Distribution for Zero-Shot Non-Line-of-Sight Imaging** — Qinghua Zhang, Jun Liu, Yuping Duan. *IEEE Signal Processing Letters* 32, 1690–1694 (2025). DOI: `10.1109/LSP.2025.3558458`.
5. **Passive non-line-of-sight pedestrian imaging based on light transport matrix decomposition** — Mingyang Chen, Jiyue Wang, Mengge Liu, Ziqin Xu, Hao Liu, Mingliang Xu. *Optics and Lasers in Engineering* 192, 109032 (2025). DOI: `10.1016/j.optlaseng.2025.109032`.
6. **Non-line-of-sight imaging via scalable scattering mapping using TOF cameras** — Yujie Fang, Junming Wu, Shengming Zhong, Xiaofeng Zhang, Yulei An, Xia Wang, Binghua Su, Kejun Wang. *Photonics Research* 13(8), 2172–2183 (2025). DOI: `10.1364/PRJ.558736`.
7. **Edge-aware dual-spectral NLOS imaging architecture** — Xiabing Shi, Yunzhuo Yang, Hailu Wang, Peng Zheng, Shang Ma, Hao Liu. *Proceedings of SPIE* 14177, 141777B; NDTA 2025, published 11 May 2026. DOI: `10.1117/12.3109634`.

No final-venue version later than the 15 July 2026 JOSA A publication of PICL was verified in this run.

## Intended semantic integration

- `README.md`: seven latest-addition rows and grouped 2025/2026 development-timeline milestones.
- `index.html`: seven searchable paper objects, recalculated tracked-entry count, and timeline additions.
- `article/3passive.tex`: long-range LWIR transport decomposition and dual-spectral edge deployment.
- `article/4datadriven.tex`: KAN-enhanced transient Transformers, latent graph/RED regularization, mixture-distribution zero-shot attention, and measurement-driven artifact cancellation.
- `article/5newscenes.tex`: commodity continuous-wave ToF scalable-scattering mapping.
- `bare_jrnl.tex`: integration marker; substantive text remains in the semantically appropriate included section sources.
- `egbib_merged_20260711.bib`: generated from the canonical update file by the existing bibliography merger.
- `bare_jrnl.pdf`: clean LaTeX/BibTeX rebuild only after source, citation, bibliography, page-rendering, and cross-file checks pass.

## Safety and consistency

The synchronizer is idempotent and checks unique anchors before modifying large files. It does not blindly replace README, homepage, or survey sources. The workflow verifies that every title appears exactly once in README and the homepage, every citation key is present in its intended survey section and exactly once in the merged bibliography, the homepage count equals the paper-array size, LaTeX has no undefined citations, BibTeX has no missing/repeated entries, the PDF is non-empty and renderable, and representative new literature-review phrases are present in the generated PDF.
