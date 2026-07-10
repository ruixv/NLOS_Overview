# 11 July 2026 bibliography deduplication

The survey previously passed every chronological `egbib*.bib` supplement directly to BibTeX. Several supplements intentionally repeated keys to correct venue or metadata, which caused BibTeX to stop with repeated-entry errors before producing `bare_jrnl.bbl`.

This update generates `egbib_merged_20260711.bib` from 13 source files and keeps one highest-priority record for each of 346 unique keys. Keys are compared case-insensitively because BibTeX treats case variants as duplicates. Priority is deterministic: `egbib.bib`, then `egbib_2026_updates.bib`, followed by dated supplements in chronological filename order, so later corrections override older records. `bare_jrnl.tex` now uses only the consolidated bibliography.

## Duplicate keys resolved

- `liTransiT2025`: `egbib.bib` → `egbib_2026_updates.bib`
- `somasundaramRoleTransients2023`: `egbib.bib` → `egbib_2026_updates.bib`
- `sunGeneralizable2025`: `egbib.bib` → `egbib_20260701_updates.bib`
- `caohighresolutionnlos2022`: `egbib.bib` → `egbib_20260702_updates.bib`
- `zhuFastNonlineofsightImaging2021a`: `egbib.bib` → `egbib_20260703_updates.bib`
- `fujimuraNLOSNeuS2023`: `egbib.bib` → `egbib_20260703_updates.bib`
- `suDGNLOS2025`: `egbib.bib` → `egbib_20260703_updates.bib`
- `musarraNonlineofsight3DImaging2019`: `egbib.bib` → `egbib_20260705_updates.bib`
- `leiDirectObjectRecognition2019`: `egbib.bib` → `egbib_20260707_updates.bib`

## Citation-key correction

No verifiable publication matching `saundersMultiDepthComputationalPeriscopy2020` was found. The alias was replaced with the verified key for Saunders et al., *Computational Periscopy with an Ordinary Digital Camera*, Nature 565, 472--475 (2019), DOI 10.1038/s41586-018-0868-6:

- `article/1introduction.tex`: `saundersMultiDepthComputationalPeriscopy2020` → `saundersComputationalPeriscopyOrdinary2019`

The CI workflow performs a clean LaTeX/BibTeX build, rejects undefined citations or repeated entries, validates the PDF with `pdfinfo` and `pdftotext`, and verifies that the newly integrated X-band radar and Neural Illumination Fields records appear in the generated bibliography.
