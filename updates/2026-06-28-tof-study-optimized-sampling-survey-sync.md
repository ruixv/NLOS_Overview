# ToF study and optimized-sampling survey sync — 28 June 2026

This update did not identify a higher-confidence paper that is absent from the current README / website snapshot. The README already lists the two most relevant missing/consistency items found during this run:

| Year | Paper | Status | Current public placement |
|------|-------|--------|--------------------------|
| 2026 | *A comprehensive study of time-of-flight non-line-of-sight imaging* — Marco et al. | arXiv 2026; no final venue verified during this run | README latest additions and ToF-method context |
| 2025 | *Optimized Sampling for Non-Line-of-Sight Imaging Using Modified Fast Fourier Transforms* — Sultan et al. | arXiv 2025; no final venue verified during this run | README latest additions and wave/frequency-domain model table |

## Source changes made

- `egbib_2026_updates.bib`
  - Added `sultanOptimizedSamplingNLOS2025` for the NUFFT/SFFT optimized-sampling paper.
  - Added `marcoComprehensiveToFNLOS2026` for the comparative ToF NLOS study.

- `article/6conclusion.tex`
  - Replaced the previously uncited mention of optimized FFT/NUFFT sampling with an explicit citation.
  - Added a short synthesis sentence explaining why the Marco et al. comparative ToF study matters: it places representative ToF NLOS inverse models under a common forward-model and hardware-aware evaluation framework.

## Metadata decisions

Both papers were first found and verified through arXiv. I did not find reliable evidence of final accepted / published venues in this run, so both are kept as arXiv entries.

## Remaining build status

The source-level survey is more consistent than before, but the PDF was not regenerated in this run. The repository still needs the bibliography line in `bare_jrnl.tex` changed from

```tex
\bibliography{egbib}
```

to

```tex
\bibliography{egbib,egbib_2026_updates}
```

before the new bibliography supplement is picked up by BibTeX. The available GitHub connector can safely replace small text files, but does not provide a patch-only edit or LaTeX compilation path for regenerating and uploading `bare_jrnl.pdf` without risking large-file truncation.
