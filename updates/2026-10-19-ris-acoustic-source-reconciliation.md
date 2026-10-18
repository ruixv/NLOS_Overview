# NLOS survey reconciliation — 2026-10-19

Verified existing 2026 references are now cited in `article/5newscenes.tex`: `coloneRISAidedDetection2026`, `sanjeevaBiStaticIRSCRB2026`, `yasmeenRCSQuantizedRIS2026`, and `wangAcousticNLOSLocalizationReview2026`. `article/2active.tex` already cites `zhiMultiSolitonMicrocombNLOS2026`. The updated `index.html` links to the corresponding sources. All five already have entries in `egbib_merged_20260711.bib` and public paper lists; no duplicate entries were introduced. The main `bare_jrnl.tex` includes both modified chapters. These RIS and acoustic studies primarily concern sensing/localization, not dense hidden 3D imaging.

PDF rebuild is pending. On a complete checkout run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`, validate `pdfinfo`, `pdftotext`, BibTeX warnings and citations, then commit the regenerated `bare_jrnl.pdf`. Do not claim the PDF is current until its Git blob changes.
