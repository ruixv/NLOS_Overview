# 24 July 2026 NLOS cross-artifact consistency audit

## Scope

This run repeated recent-keyword, final-venue, project-page, lab-page, and core-paper citation tracing around active transient NLOS, computational periscopy, coherent optical ranging, learned reconstruction, and scattering/single-pixel imaging. No direct NLOS paper with an independently verified publication date later than 22 July 2026 was found. The latest remains:

- Talha Sultan et al., **Iterating the transient light transport matrix for non-line-of-sight imaging**, *Nature Communications* (published online 22 July 2026), DOI `10.1038/s41467-026-75177-4`.

The audit found three papers that were already discussed in the LaTeX section sources and development timeline but were not consistently exposed in the README Latest Additions, website paper explorer, and normalized merged bibliography.

## Verified records

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

## Planned synchronization

The guarded synchronizer `scripts/sync_nlos_20260724_cross_artifact_gaps.py` will:

1. Add all three final-venue records to `README.md` Latest Additions while preserving the 22 July TLTM paper as the newest item.
2. Add searchable paper objects to `index.html`, update the public date to 24 July 2026, and increment the tracked-entry count only for genuinely absent objects.
3. Validate that the three papers remain semantically integrated in `article/2active.tex`, `article/3passive.tex`, and `article/4datadriven.tex` rather than appending a detached list.
4. Normalize their stable citation-key records in `egbib_merged_20260711.bib`, rejecting duplicate keys or DOIs.
5. Update the coverage date and audit marker in `bare_jrnl.tex`.
6. Clean-build `bare_jrnl.pdf` and validate citations, bibliography uniqueness, extracted PDF text, and cross-artifact DOI coverage.

**Status after automation:** README, website, semantically placed survey prose, normalized bibliography, and rebuilt PDF are mutually synchronized and validated.
