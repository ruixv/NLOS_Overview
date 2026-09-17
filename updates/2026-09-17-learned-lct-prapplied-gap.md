# 2026-09-17 — Learned LCT gap

Verified missing paper:

- Xinqi Gao, Yijie Yang, Lianfang Wang, Xueying Liu, Yong Wang, Yuping Duan, “Learned light-cone transform for fast and accurate non-line-of-sight imaging,” Physical Review Applied 25(4), 044024 (2026). DOI: 10.1103/jsbg-c7l5. Published 9 April 2026.

Why relevant: a direct descendant of O'Toole et al.'s light-cone transform. It replaces the fixed Wiener-filter component with learnable high-frequency-enhanced filtering and adds spatiotemporal feature extraction / volume projection, preserving the analytic LCT structure while learning corrections for reconstruction detail and robustness. APS reports real-data evaluation across different NLOS systems and about 5 dB PSNR improvement over baseline LCT.

Integration plan:
- README.md: add under Active / Transient / Learned reconstruction and Latest Additions; describe as physics-structured learned LCT rather than a generic neural reconstruction method.
- Website/index.html: add to Paper Explorer and 2026 timeline; connect the milestone lineage LCT (2018) -> learned/physics-structured analytic inversion (2026).
- Survey LaTeX: integrate semantically in the active NLOS reconstruction / data-driven reconstruction discussion immediately after LCT and alongside hybrid physics-learning methods. Suggested sentence: “Recent hybrid approaches retain analytic inversion structure while learning its limiting components; Gao et al. replace the fixed Wiener stage of LCT with high-frequency-enhanced learnable filtering and couple it to spatiotemporal feature extraction, improving detail preservation while retaining fast LCT-style reconstruction.”
- Canonical bibliography: merge the verified BibTeX entry staged in `egbib_20260917_learned_lct_prapplied.bib` and avoid duplicate citation keys.
- PDF: rebuild bare_jrnl.pdf only after the canonical survey source and bibliography are safely updated.

Repository title and DOI searches returned no match before staging. Large public-facing files were not overwritten from partial/truncated content in this run.
