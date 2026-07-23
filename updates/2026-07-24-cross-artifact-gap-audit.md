# 24 July 2026 NLOS cross-artifact consistency audit

## Scope and result

This run repeated recent-keyword, final-venue, project-page, lab-page, and core-paper citation tracing around active transient NLOS, computational periscopy, coherent optical ranging, learned reconstruction, and scattering/single-pixel imaging.

No direct NLOS paper with an independently verified publication date later than 22 July 2026 was found. The latest remains:

- Talha Sultan et al., **Iterating the transient light transport matrix for non-line-of-sight imaging**, *Nature Communications* (published online 22 July 2026), DOI `10.1038/s41467-026-75177-4`.

Three candidates were re-verified in detail during the search. The guarded synchronizer then established that all three were already present in the README Latest Additions, website paper explorer and timeline, semantically appropriate LaTeX sections, and merged bibliography. Consequently, it inserted no duplicate paper records and left the website tracked-entry count unchanged at 192.

## Re-verified records

### Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding

- Authors: Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, Li Zhao
- Venue: *Optics Express* 34(14), 26271–26289 (2026)
- DOI: `10.1364/OE.601398`
- Classification: direct passive ordinary-camera NLOS reconstruction
- Contribution: diffuse-aware attention-enhanced encoding emphasizes weak relay-wall features that survive diffuse transport, extending passive NLOS beyond generic image-to-image backbones.

### Submillimeter non-line-of-sight ranging and imaging via cost-effective FMCW interferometry

- Authors: Huan Liang, Lingchuan Wei, Taotao Qin, Lianfa Bai, Yingjie Shi, Enlai Guo, Jing Han
- Venue: *Photonics Research* 14(7), 3005–3018 (2026)
- DOI: `10.1364/PRJ.595776`
- Classification: direct coherent optical NLOS ranging and imaging
- Contribution: fixed-delay-fiber dual-path calibration and dynamic temporal phase subdivision compensate nonlinear FMCW sweeps without optical-frequency-comb calibration, retaining submillimeter ranging and millimeter-scale imaging.

### High-resolution Fourier single-pixel non-line-of-sight imaging employing diffusion model

- Authors: Shengjie Fu, Haoran Fang, Yuheng Yu, Nuo Shen, Yuqing Yuan, Hao Liu, Guolin Liu, Ziqi Peng, Zizhun Xia, Xuan Liu, Qiegen Liu, Xianlin Song
- Venue: *Optics and Lasers in Engineering* 201, 109724 (2026)
- DOI: `10.1016/j.optlaseng.2026.109724`
- Classification: tightly adjacent transmissive/scattering NLOS, not classical relay-wall around-corner imaging
- Contribution: a diffusion prior recovers high-frequency Fourier coefficients under compressed single-pixel acquisition while measured low-frequency spectra enforce consistency; experiments operate through multiple paper layers at sampling rates down to 3%.

## Completed validation

The guarded workflow:

1. Confirmed that each DOI occurs exactly once in `README.md` and `index.html` and once as a DOI plus once as a URL in the merged bibliography.
2. Confirmed semantic survey integration through `wangDiffuseAwarePassive2026`, `liangFMCWNLOS2026`, and `fuFourierSinglePixelDiffusion2026` in the passive, active, and learning sections respectively.
3. Normalized minor publication metadata fields while preserving stable citation keys and rejecting duplicate keys or DOIs.
4. Updated the public audit date and survey coverage date to 24 July 2026 without changing the paper count.
5. Clean-built `bare_jrnl.pdf`, checked extracted text, page validity, undefined citations, and repeated bibliography entries.

**Status after automation:** no genuinely new or missing paper required insertion; README, website, semantically placed survey prose, normalized bibliography, and rebuilt PDF are mutually synchronized and validated.
