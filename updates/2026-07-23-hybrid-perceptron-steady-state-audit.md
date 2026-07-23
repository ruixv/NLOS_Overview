# 23 July 2026 active steady-state NLOS citation trace

## Verified missing paper

**A hybrid perceptron with cross-domain transferability towards active steady-state non-line-of-sight imaging**  
Rui Liang, Xi Tong, Jiangxin Yang, Yanpeng Cao  
*Signal Processing*, vol. 237, article 110072, 2025  
DOI: `10.1016/j.sigpro.2025.110072`

The final Elsevier record identifies HP-CDT as a direct active steady-state NLOS reconstruction method. Its hybrid perceptron combines hierarchical pooling and feature fusion with local convolutional and global Transformer-style perception. Its cross-domain transfer stage uses LOS latent representations as priors for NLOS feature extraction. The work evaluates both rendering data and measurements from a practical active steady-state setup and emphasizes lightweight deployment.

Repository-wide title, DOI, and method-name checks found no existing README, homepage, survey, or bibliography record before this update.

## Semantic integration plan

- `README.md`: add a final-venue entry to Latest Additions and a 2025 active steady-state learning milestone.
- `index.html`: add one searchable paper object, expand the 2025 timeline, and update tracked entries from 191 to 192.
- `article/4datadriven.tex`: insert a literature-review paragraph immediately after the original learned steady-state U-Net discussion, explaining the trajectory from direct end-to-end mapping to LOS-to-NLOS representation transfer.
- `bare_jrnl.tex`: add a dated citation-trace marker without changing the survey structure.
- `egbib_merged_20260711.bib`: regenerate from the canonical supplement and retain exactly one DOI/key record.
- `bare_jrnl.pdf`: perform a clean `pdflatex -> bibtex -> pdflatex x2` rebuild, reject undefined citations or repeated BibTeX entries, and verify extracted PDF text.

**Status after source synchronization:** README, website, survey source, and bibliography integrated; PDF rebuild pending validation.
