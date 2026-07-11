# SSCR citation-tracing and survey consistency update (11 July 2026)

## Search result

Fresh keyword searches and a forward-citation tracing pass from the repository's core active NLOS papers did not reveal a newer high-confidence July 2026 frontier paper beyond the entries already surfaced in the repository.

The tracing pass did expose one survey-source consistency gap for a directly relevant active transient NLOS paper:

- **Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization** — Xintong Liu, Jianyu Wang, Leping Xiao, Xing Fu, Lingyun Qiu, and Zuoqiang Shi, arXiv:2211.15367 (2022).
- SSCR jointly regularizes the measured/estimated transient signal, a 3D voxel representation, and a 2D hidden-surface representation.
- It supports confocal and non-confocal measurements and reports reconstruction from only `5 x 5` confocal measurements on public data.
- No final conference or journal venue was verified, so the status remains **arXiv 2022**.

## Synchronized artifacts

- `README.md` and `index.html` already contained the verified paper entry.
- `article/2active.tex` now integrates SSCR directly after CC-SOCR in the arbitrary-relay/sparse-measurement discussion.
- `egbib_20260711_sscr_updates.bib` contains the verified citation key `liuFewShotSSCR2022`.
- `scripts/merge_nlos_bibliography.py` regenerates `egbib_merged_20260711.bib` from all `egbib*.bib` sources before the survey build.

## PDF status

The GitHub Actions workflow performs a clean LaTeX/BibTeX rebuild, rejects undefined or repeated citation records, validates the PDF with `pdfinfo` and `pdftotext`, and confirms that the SSCR title is present in the generated survey. The workflow records the final build result below.

**Build result:** the SSCR source and bibliography integration was applied, but no strictly validated replacement PDF was committed. The prior PDF was preserved. Reason: PDF/reference validation failed (undefined=false, integrated=false, pdfinfo=0, pdftotext=0) (latexmk exit code 0). See `updates/2026-07-11-sscr-build-diagnostic.md`.
