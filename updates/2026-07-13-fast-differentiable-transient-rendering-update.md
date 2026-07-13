# 13 July 2026 fast differentiable transient rendering update

## Search and citation-tracing result

The fresh July 2026 arXiv, conference, journal, project-page, and modality search did not identify a direct NLOS-imaging paper newer than the already tracked 5 July 2026 NIR raster-scanning work. A forward-reference pass from the 2026 3D Gaussian Transient Rendering paper, however, exposed a missing milestone in the transient inverse-rendering branch:

- **Fast Differentiable Transient Rendering for Non-Line-of-Sight Reconstruction** — Markus Plack, Clara Callenberg, Monika Schneider, Matthias B. Hullin, **WACV 2023**, pp. 3067–3076.
- Official CVF page: https://openaccess.thecvf.com/content/WACV2023/html/Plack_Fast_Differentiable_Transient_Rendering_for_Non-Line-of-Sight_Reconstruction_WACV_2023_paper.html

This is genuinely an NLOS reconstruction paper rather than a passing citation. It develops a physically based differentiable transient renderer specifically to accelerate analysis-by-synthesis NLOS reconstruction from hours to minutes on consumer hardware, improve optimization stability, and support self-supervised learning. The official CVF proceedings page verifies the accepted WACV 2023 venue, full author list, and page range.

## Repository synchronization

The marker-based synchronizer updates the following artifacts consistently:

1. `README.md`
   - adds the verified WACV 2023 paper to Latest Additions;
   - adds the fast differentiable transient-rendering milestone to the 2023 development timeline.
2. `index.html`
   - adds a searchable paper-explorer object;
   - updates the tracked-latest count from 93 to 94;
   - expands the 2023 timeline to connect differentiable transient rendering with later self-calibrating and neural inverse-rendering methods.
3. `article/2active.tex`
   - inserts a literature-review paragraph in the **Inverse Rendering** discussion rather than appending a disconnected list.
4. `egbib_20260713_plack_updates.bib`
   - provides the final-venue BibTeX entry under citation key `plackFastDifferentiableTransient2023`.
5. `egbib_merged_20260711.bib`, `bare_jrnl.tex`, and `bare_jrnl.pdf`
   - are regenerated and validated by the temporary CI workflow.

## Validation requirements

The workflow performs an idempotent synchronization, duplicate-free bibliography merge, clean LaTeX/BibTeX build, citation-key audit, PDF metadata and text extraction, and page rendering. It rejects undefined citations, missing bibliography records, repeated BibTeX entries, a stale homepage count, or a PDF that does not contain the new WACV paper.

**Build result:** pending CI execution.
