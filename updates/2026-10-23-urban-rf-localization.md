# 23 October 2026 — Urban RF NLOS localization backfill

## Verified entry

Gajewski, Jaromir, and Jerzy Łopatka. “A Hybrid Raytracing and Deep Learning-Based Approach for Single-Site Localization of Radio Emitters in Urban Environment.” *Sensors* **26**(19), 6261 (2026). DOI: 10.3390/s26196261; https://doi.org/10.3390/s26196261. First published **2 October 2026**. Independently corroborated by PubMed PMID 42884461.

## Relevance and limitations

This is directly relevant to NLOS **RF emitter localization**, not dense hidden-scene imaging. The five-element circular SDR array, CM-MUSIC decorrelation, backward ray tracing and CNN sector masking recover urban source positions from measured multipath. Median error 9.22 m; mean error 55.52 m and outliers up to 410.68 m reveal sensitivity to misclassified sectors. Measurements use a stationary monitoring platform and a limited set of emitter positions. This entry was found via targeted RF/NLOS keyword and publisher searches; it is not falsely claimed as a verified optical-core forward citation.

## Exact insertion locations

- README.md: first Latest Additions row; first Milestone Timeline item.
- index.html: first Core Reading Path update; survey-source timestamp.
- data/papers-source.html: first paper-explorer record and first 2026 timeline item; counter now 395.
- article/5newscenes.tex: Radar-Based NLOS Imaging subsection, immediately before 'Higher-order RF paths and joint LOS/NLOS inference'.
- egbib_merged_20260711.bib: key `gajewskiUrbanRFLocalization2026`. The unchanged bare_jrnl.tex includes this chapter and bibliography through existing input/bibliography commands.

## PDF build status: PENDING

bare_jrnl.pdf was **not** regenerated in this update. The execution container has pdflatex but cannot resolve GitHub/raw repository assets and figures. Do not claim the old PDF contains this paper. From a complete checkout run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`; verify successful BibTeX citation resolution, pdfinfo and pdftotext output, then commit the binary. Existing workflow .github/workflows/rebuild_nlos_citation_gap_pdf_20260718.yml has a workflow_dispatch trigger but is not automatically triggered by this source-only update.

## Screening context

Keyword and forward-citation-oriented searches covered LCT, f-k, phasor fields, computational periscopy, learned transient reconstruction, active/passive optical NLOS, acoustic/thermal NLOS, consumer LiDAR and RF/mmWave. PICL (JOSA A 2026), NLOSdiffuser (ICME 2025), Cascaded NLOS (ACM TOG 2026), NIGHT (ECCV 2024 Workshops) and MALCT (arXiv 2026) were checked against the current public corpus and already covered. Exhaustive forward-citation pagination remains incomplete.
