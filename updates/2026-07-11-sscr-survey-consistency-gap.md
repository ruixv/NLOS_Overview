# SSCR citation-tracing and survey consistency update (11 July 2026)

## Search result

Fresh keyword searches and a forward/reference-citation tracing pass from the repository's core active NLOS papers did not reveal a newer high-confidence July 2026 frontier paper beyond the entries already surfaced in the repository.

The tracing pass did, however, expose one survey-source consistency gap for a directly relevant active transient NLOS paper:

- **Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization** — Xintong Liu, Jianyu Wang, Leping Xiao, Xing Fu, Lingyun Qiu, and Zuoqiang Shi, arXiv:2211.15367 (2022).
- The paper develops SSCR, a Bayesian few-shot reconstruction framework that jointly regularizes the measured/estimated transient signal, a 3D voxel representation, and a 2D hidden-surface representation.
- It supports confocal and non-confocal measurements and reports reconstruction from only `5 x 5` confocal measurements on public data.
- No final conference or journal venue was verified, so the status remains **arXiv 2022**.

## Current repository state

`README.md` and `index.html` already surface the paper, but the survey narrative in `article/2active.tex` discusses the preceding CC-SOCR work without integrating the follow-on SSCR method. Consequently, the regenerated survey PDF does not yet provide the corresponding literature-review sentence even though the public paper lists do.

A verified BibTeX record has been added in:

```text
egbib_20260711_sscr_updates.bib
```

with citation key:

```text
liuFewShotSSCR2022
```

## Exact survey-source insertion

In `article/2active.tex`, locate the paragraph under **Extensions to Non-Planar Relay Surfaces** that ends with:

```latex
...greatly broadening the applicability of NLOS systems to irregular or partial relay surfaces encountered in real-world scenarios.
```

Insert the following paragraph immediately after it and before **Higher-Order Bounce Imaging**:

```latex
Moving from arbitrary relay sampling toward extreme measurement sparsity, Liu~\etal~introduced signal-surface collaborative regularization (SSCR), which jointly regularizes the photon-event signal, a three-dimensional voxel representation, and a two-dimensional hidden-surface representation~\cite{liuFewShotSSCR2022}. The method supports both confocal and non-confocal acquisition and reconstructs complex hidden geometry from as few as $5\times5$ confocal measurements, showing how mixed-dimensional physical priors can replace much of the dense raster scan required by earlier transient NLOS systems.
```

This placement preserves the survey's conceptual progression:

1. CC-SOCR generalizes the relay illumination/detection pattern.
2. SSCR reduces the number of measurements by coupling signal, volume, and surface priors.
3. Later methods pursue higher-order transport, learned priors, transformers, diffusion, and arbitrary-relay differentiable rendering.

## Bibliography and PDF steps still required

The repository currently compiles `bare_jrnl.tex` against the generated consolidated file `egbib_merged_20260711.bib`. To complete the integration safely:

1. Apply the paragraph insertion above to `article/2active.tex`.
2. Rerun `scripts/merge_nlos_bibliography.py` so `egbib_20260711_sscr_updates.bib` is included in the duplicate-free consolidated bibliography.
3. Run a clean LaTeX/BibTeX build, for example:

```bash
latexmk -C bare_jrnl.tex
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

4. Reject the build if the log contains undefined citations/references or duplicate BibTeX keys.
5. Verify with `pdfinfo` and `pdftotext` that the replacement `bare_jrnl.pdf` is valid and contains the SSCR title/reference.
6. Commit `article/2active.tex`, `egbib_merged_20260711.bib`, and the regenerated `bare_jrnl.pdf` together.

The large hand-maintained TeX source and generated binary PDF were not overwritten in this pass because the available repository write operation replaces whole files rather than applying a line-level patch. The precise insertion above avoids risking truncation or accidental loss while leaving the repository with verified metadata and an immediately applicable patch.
