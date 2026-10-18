# NLOS literature / survey reconciliation — 18 October 2026 evening

## Verified venue update
The already-indexed paper **RIS-aided Radar Detection Architectures with Application to Low-RCS Targets** now has a final 2026 *IEEE Transactions on Aerospace and Electronic Systems* record, DOI **10.1109/TAES.2026.3736025**, verified from the University of Pisa institutional record and an author's ORCID. The journal-listed author order is Yan, Gao, Colone, Costa, Hao, Manara, Orlando, whereas the arXiv preprint 2601.10846 has Colone first. Final issue and page numbers were not independently verified. It is adjacent RIS-assisted target detection, not dense hidden-scene imaging.

## Previously indexed works still needing LaTeX citation reconciliation
The repository already includes bibliography entries and public README/Paper Explorer listings for (1) Zhi et al., *Advanced Science* 2026, multi-soliton microcomb ranging with an NLOS imaging proof of concept (key `zhiMultiSolitonMicrocombNLOS2026`); (2) Yan et al., *IEEE TAES* 2026 RIS-assisted radar low-RCS detection (`coloneRISAidedDetection2026`); (3) Sanjeeva Reddy S and Vinod Veera Reddy, arXiv 2026 bistatic IRS CRLB (`sanjeevaBiStaticIRSCRB2026`); (4) Yasmeen et al., arXiv 2026 quantized RIS radar cross-section and micro-Doppler sensing (`yasmeenRCSQuantizedRIS2026`); (5) Wang et al., *Journal of Data Acquisition and Processing* 2026 acoustic NLOS localization overview (`wangAcousticNLOSLocalizationReview2026`). These five were not cited in the active and modality LaTeX chapters at the start of this run. Other apparently uncited 2026 bibliography keys mostly alias works already cited under different keys.

## Precise source insertion plan
- `article/2active.tex`: immediately after the paragraph ending "interferometric calibration and coherence control." add a brief dual-microcomb hardware/NLOS proof-of-concept discussion with `\cite{zhiMultiSolitonMicrocombNLOS2026}`.
- `article/5newscenes.tex`: after the paragraph ending "measured hidden-scene imaging systems." in the RIS angular sensing subsection, discuss RIS detection, CRLB bounds, and quantized-surface micro-Doppler using the three RIS keys above. After the opening acoustic subsection paragraph ending "underwater or through highly opaque materials.", add the 2026 acoustic localization survey citation.
- `egbib_merged_20260711.bib`: replace only the existing `coloneRISAidedDetection2026` arXiv entry with a journal `@article` using DOI 10.1109/TAES.2026.3736025 and the journal-listed author order; preserve arXiv eprint 2601.10846.
- `README.md`: change its single existing RIS detection row and add the final-venue correction to Latest Additions.
- `data/papers-source.html`: update the existing RIS paper record's venue, URL, and author order; do not add a duplicate.
- `index.html`: update the source date to 18 Oct and link the microcomb, RIS final DOI, and acoustic survey from Core Reading Path.
- `bare_jrnl.tex`: add a comment noting source reconciliation; its `\input` structure already includes both edited chapters.

## Citation-tracing scope
Recent arXiv, journal/publisher and targeted forward-citation searches examined Velten 2012, LCT, f-k migration, phasor-field, Computational Periscopy, neural transients, consumer LiDAR, thermal, acoustic and RIS/radar NLOS. No independently verified new unlisted NLOS imaging paper was confirmed. This was targeted rather than an exhaustive crawl of every citing work.

## PDF pending
`bare_jrnl.pdf` has **not** been regenerated or uploaded. The container cannot resolve github.com to clone the full repository and figure assets. On a complete checkout run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`; inspect LaTeX/BibTeX logs, `pdfinfo`, and `pdftotext`, then commit only the validated PDF. Do not mark the PDF current until its blob SHA changes.

## Write safety
The full `index.html` Git Objects blob creation and GitHub Contents API update were blocked by connector safety checks; the existing file was preserved. A verified README blob was staged but not yet committed at the point this note was drafted. Do not claim cross-artifact integration complete without a verified commit and reread.
