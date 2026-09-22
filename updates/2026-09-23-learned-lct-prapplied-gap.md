# Integration gap: Learned Light-Cone Transform (Physical Review Applied, 2026)

Verified missing paper for integration into the canonical NLOS Overview artifacts.

## Paper
Xinqi Gao, Yijie Yang, Lianfang Wang, Xueying Liu, Yong Wang, Yuping Duan, **“Learned light-cone transform for fast and accurate non-line-of-sight imaging,”** *Physical Review Applied*, 25(4), 044024, 2026. DOI: 10.1103/jsbg-c7l5. Published 9 April 2026.

## Why it belongs
This is a direct learned extension of the field-defining Light-Cone Transform (LCT) lineage. It replaces the fixed low-pass behavior of conventional Wiener-filtered LCT with a learnable high-frequency-enhanced Wiener filtering stage and combines it with spatiotemporal feature extraction and volume projection. The authors report real-data evaluation across multiple NLOS systems and approximately 5 dB PSNR improvement over conventional LCT. It is best categorized as physics-guided / learned active transient NLOS reconstruction, rather than as a generic deep network.

## Canonical integration locations
- **README.md**: add to 2026/latest additions and learned/active transient reconstruction section. Suggested concise contribution: “Learned LCT makes the classical light-cone inversion trainable through high-frequency-enhanced Wiener filtering plus spatiotemporal feature extraction, improving detail recovery while retaining the LCT physics prior.”
- **Development timeline**: place on the trajectory `LCT (2018) -> physics-guided learned inversion -> learned LCT (2026)`.
- **index.html / Paper Explorer**: add under Active / Transient / Learned / Physics-guided; venue must be *Physical Review Applied 2026*, not arXiv.
- **bare_jrnl.tex**: integrate semantically where LCT and learned transient reconstruction are discussed. A suitable literature-review transition is: “Recent work has also made classical transient inversion itself learnable: Gao et al. augment LCT with high-frequency-enhanced learnable Wiener filtering and spatiotemporal feature extraction, preserving the analytic LCT prior while recovering details attenuated by conventional low-pass regularization.”
- **Canonical bibliography**: merge the verified entry staged in `egbib_20260923_learned_lct_prapplied.bib`.
- **bare_jrnl.pdf**: rebuild only after the canonical TeX and bibliography have been safely integrated and validated.

## Verification / deduplication
Repository-wide searches for the full title and DOI `10.1103/jsbg-c7l5` returned no match before staging. APS confirms *Physical Review Applied* 25, 044024, published 9 April 2026; DOI `10.1103/jsbg-c7l5`.

## Remaining work
Canonical large files were not overwritten from partial/truncated payloads in this run. Integrate this staged entry into README, website, survey source, and canonical bibliography using complete-file reads/current blob SHAs, then compile and verify `bare_jrnl.pdf`.
