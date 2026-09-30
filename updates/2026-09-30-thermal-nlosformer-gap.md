# Integration gap — Thermal NLOSFormer (2026-09-30)

## Verified missing paper

Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, and Feihu Xu, **“Thermal Non-Line-of-Sight Imaging through Rough Surfaces,” ACM Transactions on Graphics, vol. 45, no. 5, pp. 1–21, 2026.** Current corrected article DOI: `10.1145/3811030`.

The ACM record reports acceptance on 14 Apr 2026, online publication on 29 Jun 2026, and a correction/updated version in Aug 2026. The work introduces **NLOSFormer**, a physics-embedded network for passive thermal NLOS through rough relay surfaces. It models wall-mediated thermal transport as a convolution, estimates the transport kernel jointly with the hidden image, introduces the **ThermalNLOS** dataset and geometry-aware augmentation, demonstrates relative-depth estimation, and reports dynamic thermal NLOS reconstruction at 4 fps. This is directly relevant to the survey’s thermal/passive and learned-reconstruction branches and cites the active milestones Velten 2012, O’Toole/LCT 2018, Liu/phasor fields 2019, Lindell/f-k 2019, plus passive computational-periscopy work.

## Required canonical integration

- **README.md:** add to Latest Additions and the 2026 milestone/timeline; categorize under passive / thermal NLOS and deep learning. Suggested concise summary: “Physics-embedded NLOSFormer jointly estimates a rough-wall thermal transport kernel and hidden image, adds the ThermalNLOS dataset, supports relative-depth estimation, and demonstrates dynamic thermal NLOS at 4 fps.”
- **index.html / Paper Explorer:** add the same final-venue metadata and links; place in 2026 latest additions and thermal/passive modality timeline.
- **bare_jrnl.tex:** integrate semantically in the passive/thermal NLOS discussion, after earlier thermal/light-field methods and before/alongside recent learned passive methods. Emphasize the trajectory from reflective/simplified-wall assumptions toward rough-wall, physics-embedded learned reconstruction and dynamic thermal NLOS.
- **Canonical bibliography:** merge the verified BibTeX entry staged in `egbib_20260930_thermal_nlosformer.bib`; avoid duplicate arXiv/preprint entries if any later appear.
- **bare_jrnl.pdf:** rebuild only after the source and bibliography are integrated and compile cleanly.

## Safety note

The GitHub connector currently returns large canonical files as a JSON-wrapped content line that is truncated before the complete file can be reconstructed safely. Therefore this run intentionally did **not** overwrite README.md, index.html, or bare_jrnl.tex from partial content. This note is a precise, non-destructive staging record for the next run that can obtain complete canonical contents.
