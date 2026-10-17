# NLOS source integration and PDF build status — 17 October 2026, 22:00 CST

## Scope and verification
Integrated three previously staged, publication-verified NLOS references:
1. Yingjie Shi et al., *Transient non-line-of-sight temporal super-resolution based on temporal decoupling*, *Optics and Lasers in Engineering* (2026), article 110054, DOI 10.1016/j.optlaseng.2026.110054. Full text not reviewed; no quantitative performance claims.
2. John Murray-Bruce, Charles Saunders, Vivek K. Goyal, *Occlusion-based computational periscopy with consumer cameras*, SPIE Wavelets and Sparsity XVIII (2019), 11138/111380X, DOI 10.1117/12.2528322. Historical passive periscopy conference paper.
3. Robinson Czajkowski and John Murray-Bruce, *Turning Door Frames into Cameras for 3D Non-Line-of-Sight Imaging*, IEEE RAPID 2022, pp. 1–2, DOI 10.1109/RAPID54472.2022.9911582. Two-page passive 3D precursor, not the full 2024 TERI journal article.

Corrected the legacy BibTeX alias `czajkowskiTwoEdge2024` to Robinson Czajkowski, *Nature Communications* 15, 1162 (2024), DOI 10.1038/s41467-024-45397-7; retained its citation key to avoid breaking the survey.

## Files and integration map
- `README.md`: Latest Additions and Milestone Timeline.
- `data/papers-source.html`: three searchable Paper Explorer records, Latest Additions, and three chronological timeline milestones.
- `index.html`: Core Reading Path and updated source timestamp.
- `article/2active.tex`: temporal-decoupling paragraph next to sparse Bayesian transient restoration.
- `article/3passive.tex`: consumer-camera and doorway-frame precursors next to other computational periscopy methods.
- `bare_jrnl.tex`: integration comment; existing \input references pull in the modified active and passive chapters.
- `egbib_merged_20260711.bib`: three new entries from verified staging file and corrected TERI alias.
- `updates/2026-10-17-verified-bibtex-staging.bib`: retained for audit history; merged BibTeX is the compilation source.

## PDF pending — do not claim it is current
`bare_jrnl.pdf` was **not** regenerated in this run. The original binary Git blob SHA was `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`. The execution container has `pdflatex` and `latexmk` but cannot resolve github.com to clone the full repository and its figure assets. GitHub connector tools can update text sources but cannot upload a newly built binary without a valid PDF artifact. The existing PDF is stale relative to the newly updated source.

To complete: obtain the full repository with image assets in a LaTeX-capable environment, run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex` (including BibTeX passes), check citation resolution and PDF page rendering, then commit the regenerated `bare_jrnl.pdf`. If using GitHub Actions, create/trigger a suitable build workflow only after reviewing its permissions.

## Audit
Bibliography citation keys must remain unique; all newly inserted `\\cite{}` keys resolve to the merged bibliography. Website JavaScript and paper-card data must parse. The 2019/2022 conference precursors are not to be conflated with the 2024 *Nature Communications* TERI article.

The literature search also checked recent LCT/phasor-field, passive periscopy, arbitrary relay geometry, RF/mmWave, acoustic, LiDAR, and learned transient work; no additional high-confidence uncatalogued work was confirmed in this pass. Forward-citation tracing beyond the previously reviewed Saunders 2019 network remains non-exhaustive.
