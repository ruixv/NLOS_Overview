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
- `scripts/merge_nlos_bibliography.py` regenerated `egbib_merged_20260711.bib` from all `egbib*.bib` sources; the audit reports zero truly missing citation keys.
- `bare_jrnl.tex` uses the consolidated bibliography.

## PDF status

**Build result:** successful clean LaTeX/BibTeX rebuild. The workflow regenerated and committed `bare_jrnl.pdf` after the SSCR prose and verified BibTeX record had been integrated. `pdfinfo` and `pdftotext` passed, the LaTeX log contained no undefined citations or references, and BibTeX reported no missing or repeated records. The replacement PDF was committed in `1eff6528d145cce00f469a5a230f079757bc772a`.
