# 2026-11-17 Flash LiDAR integration branch: validation and build pending

Branch: `audit/flash-lidar-integration-20261117` (based on master). This branch contains guarded, SHA-based complete-file updates to:
- `README.md`: 2026 Latest Additions entry
- `data/papers-source.html`: Paper Explorer record tagged active optical / SPAD / detection
- `article/2active.tex`: literature-review paragraph before active light source/interferometry
- `egbib_merged_20260711.bib`: BibTeX key `qiuSimulationDrivenOcclusionNLOS2026`

Paper: Qiu, Olowe, Zang, Gyongy, Chitnis, *Simulation-Driven Approach for Occlusion-Based Non-Line-Of-Sight Detection Using a Low-Cost Flash LiDAR*, arXiv:2611.04068, submitted 2 Nov 2026, https://arxiv.org/abs/2611.04068. No verified final venue. This is occlusion-based detection, **not** 3D scene reconstruction.

After writing, each changed file was fetched again from the branch and checked for the identifier or citation key. `bare_jrnl.tex` was inspected: it already uses `\\input{article/2active.tex}`, so the new survey paragraph is included transitively without modifying the main source.

**Not yet built / merged**: `bare_jrnl.pdf` is unchanged. Although pdflatex/latexmk are installed in the execution container, the complete GitHub repository cannot be cloned there (GitHub DNS resolution fails), so compilation, bibliography resolution, and PDF visual checks could not be performed. Do not merge or claim a new PDF until the full LaTeX project is available and compilation succeeds. Suggested build: `latexmk -pdf -interaction=nonstopmode bare_jrnl.tex` with the project's existing bibliography toolchain; inspect missing citations and pages, commit PDF, then merge this branch after validating website and survey consistency. If the existing GitHub Actions PDF build is available, use that instead.

Citation tracing and repository-wide reconciliation of other recent papers remain incomplete; this branch only integrates the verified Flash LiDAR gap. The recurring NLOS literature task should continue.
