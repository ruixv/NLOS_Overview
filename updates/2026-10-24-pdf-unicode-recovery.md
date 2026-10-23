# 2026-10-24 survey PDF build recovery: BibTeX Unicode

## Verified failure
The GitHub Actions run [39966480148](https://github.com/ruixv/NLOS_Overview/actions/runs/39966480148) completed with **failure** during the `Clean-build survey` step on 2026-10-23. Its log shows `! LaTeX Error: Unicode character 基 (U+57FA) not set up for use with LaTeX`, in `bare_jrnl.bbl` line 1253. The triggering entry is `fangGeneticDeconvolutionToFNLOS2023`, where a `note` field had included the original Chinese-language title verbatim. `pdflatex` cannot typeset that character without additional CJK configuration.

## Applied source fix
Replaced **only** the non-ASCII `note` field in `egbib_merged_20260711.bib` with an ASCII-only note pointing readers to the original Chinese title in the publisher record. The English journal title, author list, venue, volume, issue, article number, year, DOI, URL and citation key remain unchanged. This avoids altering the existing IEEEtran/pdflatex workflow or its survey prose.

## Validation and outstanding work
- Confirm the BibTeX entry is complete, its key is unchanged, and its note no longer contains Chinese characters.
- On merging this source fix into `master`, the `egbib_merged_20260711.bib` path is configured to trigger `.github/workflows/rebuild_nlos_citation_gap_pdf_20260718.yml`.
- **Do not mark the PDF current until** the new workflow run completes successfully, the regenerated `bare_jrnl.pdf` has a new blob SHA, and the compiled bibliography/citations are verified. First-pass undefined-citation warnings in the failed run are not evidence of missing BibTeX keys because LaTeX was halted before its iterative passes finished.
- If a subsequent build fails for another reason, inspect the new job logs and correct the specific root cause; do not overwrite the existing PDF with an incomplete artifact.

## Literature
This is a build recovery, not a new paper addition. Searches on 2026-10-24 rechecked recent arXiv, publisher pages, and selected core-paper forward-citation descendants. No verified missing paper was added in this patch. Existing public paper records and survey prose remain unchanged.
