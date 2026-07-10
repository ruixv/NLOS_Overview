# 11 July 2026 bibliography deduplication

The survey previously passed every chronological `egbib*.bib` supplement directly to BibTeX. Several supplements intentionally repeated keys to correct venue or metadata, which caused BibTeX to stop with repeated-entry errors before producing `bare_jrnl.bbl`.

This update generates `egbib_merged_20260711.bib` from 13 source files and keeps one highest-priority record for each of 349 unique keys. Priority is deterministic: `egbib.bib`, then `egbib_2026_updates.bib`, followed by dated supplements in chronological filename order, so later corrections override older records. `bare_jrnl.tex` now uses only the consolidated bibliography.

## Duplicate keys resolved

- `liTransiT2025`: `egbib.bib` → `egbib_2026_updates.bib`
- `somasundaramRoleTransients2023`: `egbib.bib` → `egbib_2026_updates.bib`
- `sunGeneralizable2025`: `egbib.bib` → `egbib_20260701_updates.bib`
- `caohighresolutionnlos2022`: `egbib.bib` → `egbib_20260702_updates.bib`
- `fujimuraNLOSNeuS2023`: `egbib.bib` → `egbib_20260703_updates.bib`
- `suDGNLOS2025`: `egbib.bib` → `egbib_20260703_updates.bib`

The CI workflow performs a clean LaTeX/BibTeX build, rejects undefined citations or repeated entries, validates the PDF with `pdfinfo` and `pdftotext`, and verifies that the newly integrated X-band radar and Neural Illumination Fields records appear in the generated bibliography.
