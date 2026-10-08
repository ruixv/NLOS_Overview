# NLOS canonical integration audit — 2026-10-08

## Verified new candidate
**FermatFormer: A Fermat Optics Based Neural Architecture for Non-line-of-sight Imaging** — Siyuan Shen, Ziheng Wang, Guan Huang, Xingyue Peng, Qilin Sun, Shiying Li, Jingyi Yu (2026).

Source: https://sci2020.github.io/ (authors' laboratory page); paper: https://openreview.net/forum?id=DwPgaoaxWd. The laboratory reports IEEE TPAMI acceptance and an ICCP 2026 Best Paper Honorable Mention. A publisher DOI, volume, pages, and online-publication date were **not** independently verified, so the bibliography marks the acceptance as author-reported and omits invented metadata.

Contribution: physics-guided representation of transient measurements through stable Fermat points, designed to improve synthetic-to-real transfer for learned NLOS reconstruction. Categorize under active transient NLOS, learned physical representations, and the 2026 development timeline.

## Previously indexed works integrated into the survey
- Two-edge-resolved three-dimensional non-line-of-sight imaging with an ordinary camera — Nature Communications 15, 1162 (2024), DOI 10.1038/s41467-024-45397-7.
- Visible Occluders as Opportunistic Apertures for Wide Field of View Non-Line-of-Sight 3D Imaging — EUSIPCO 2025, DOI 10.23919/EUSIPCO63237.2025.11226155.
- Passive Non-line-of-sight Imaging for Moving Targets with an Event Camera — arXiv:2209.13300 (2022).
- Dual-branch Graph Feature Learning for NLOS Imaging — AAAI 2025, DOI 10.1609/aaai.v39i7.32757.
- 3D Reconstruction from Transient Measurements with Time-Resolved Transformer — arXiv:2510.09205 (2025), no independently verified final venue in this run.
- GenPIE: A Time-Resolved Plenoptic Imager — ACM TOG 45(4), Article 81 (2026), DOI 10.1145/3811281; adjacent transient transport rather than a canonical NLOS reconstruction method.
- The survey's TLTM iteration citation is normalized to the published Nature Communications 17, 8951 (2026), DOI 10.1038/s41467-026-75177-4, rather than its 2024 preprint.

## PDF rebuild and validation still required
The modular LaTeX sources and merged bibliography are updated, but **bare_jrnl.pdf must not be treated as current until a clean build and binary commit are verified**. This runtime can read and write GitHub text/blob objects but cannot download the entire repository into its local TeX environment; attempted workflow-file writes were blocked by connector safety checks.

Run from a full repository checkout:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdfinfo bare_jrnl.pdf
pdftotext -layout bare_jrnl.pdf /tmp/nlos-survey.txt
grep -i FermatFormer /tmp/nlos-survey.txt
grep -E 'undefined citations|Citation .* undefined|There were undefined references' bare_jrnl.log && exit 1 || true
grep -E 'Repeated entry|Warning--I didn.t find a database entry' bare_jrnl.blg && exit 1 || true
git add bare_jrnl.pdf
git commit -m 'Rebuild NLOS survey PDF after 2026 literature integration'
```

Do not overwrite the PDF or report full cross-artifact consistency if the build/validation fails. The website Paper Explorer uses `data/papers-source.html` via the `assets/paper-graph-data.js` fetch shim; `index.html` contains the static Core Reading Path.
