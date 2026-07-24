# SFPR survey-prose consistency integration — 24 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found in this run. The newest date-verified direct NLOS publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

The citation-tracing and cross-artifact audit instead found one semantic integration gap. The following final-venue paper was already present in `README.md`, the website explorer/timeline, the active-system table, and the consolidated bibliography, but it lacked a dedicated literature-review discussion in the LaTeX survey:

- **Nonconfocal non-line-of-sight imaging with specular-flight-path regularization for complex multi-orientation objects** — Xiaojie Shi, Jie Yang, Xiaorui Tian, Zhou Yang, Kai Qiao, Meng Tang, Siqi Zhang, and Chenfei Jin; *Photonics Research* 14(4), 1125–1134 (2026); DOI `10.1364/PRJ.579183`; published 19 March 2026.

## Changes made

1. Added a dedicated paragraph to `article/2active.tex` after reference-free artifact correction and before inverse rendering. It explains local transport-matrix conditioning, specular-flight-path regions, voxel-wise specular weights, TV/ADMM optimization, and the paper's role in nonconfocal multi-orientation reconstruction.
2. Preserved the stable citation key `shiSpecularFlightPathNLOS2026` and added the verified March publication month/date to `egbib_merged_20260711.bib`.
3. Added a trace marker to `bare_jrnl.tex` without changing the already-current 24 July 2026 public coverage date.
4. Left `README.md`, `index.html`, the 193-entry explorer count, and the timeline unchanged because they already contained the correct record and contribution summary.
5. Rebuilt and validated `bare_jrnl.pdf` in the guarded workflow.

## Consistency checks

- Exactly one DOI record in README and website, plus one canonical DOI field in the consolidated bibliography.
- Exactly one canonical BibTeX key and one dedicated survey heading.
- Existing active-system-table citation retained.
- Clean `pdflatex → bibtex → pdflatex ×2` build.
- No undefined citations or multiply defined BibTeX entries.
- PDF page metadata and extracted text checked; the new SFPR discussion is present in the regenerated PDF.
