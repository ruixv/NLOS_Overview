# 14 July 2026 — geometric-constrained NLOS surface reconstruction

**Build status:** README, homepage/timeline, survey source, merged bibliography, and regenerated PDF were synchronized; clean build and citation/PDF checks passed.

## Search and citation-tracing result

Fresh arXiv, conference, journal, project-page, and lab-page searches did not reveal a directly relevant NLOS-imaging paper newer than the NIR raster-scanning preprint submitted on 5 July 2026. A forward/reference-citation pass through the active-ToF reconstruction chain, however, identified a high-confidence omission:

- **Geometric Constrained Non-Line-of-Sight Imaging** — Xueying Liu, Lianfang Wang, Jun Liu, Yong Wang, and Yuping Duan, arXiv:2503.17992 (2025).
- Source: https://arxiv.org/abs/2503.17992
- Verified status on 14 July 2026: the arXiv record does not identify a final accepted or published journal/conference version, and no authoritative publisher record was found; the repository therefore labels it **arXiv 2025** rather than assigning an unverified venue.

This is a direct NLOS reconstruction contribution rather than a paper that merely cites the field in passing. It jointly estimates albedo and hidden-surface geometry and uses the Frobenius norm of the depth-map shape operator to regularize spatial variation of the surface-normal field. The paper explicitly develops the Velten/LCT/f-k/phasor-field and surface-reconstruction lineage, evaluates synthetic and experimental transient data, and reports improved surfaces on measurements captured within 15 seconds with approximately 30-fold lower optimization time than an existing surface-reconstruction approach.

## Intended synchronized changes

1. **README.md** — add the paper to Latest Additions and the 2025 milestone path with an arXiv-only status and concise contribution summary.
2. **index.html** — add a searchable paper object, raise the tracked-entry count from 96 to 97, and expand the 2025 timeline with geometric surface-normal priors.
3. **article/2active.tex** — integrate the work into the `Surface` subsection after the LCT/DLCT surface discussion, and include it in the active-SPAD reconstruction table.
4. **Bibliography** — add canonical key `liuGeometricConstrainedNLOS2025` in `egbib_20260714_geometric_constraints_updates.bib`, then regenerate the duplicate-free consolidated bibliography.
5. **bare_jrnl.pdf** — perform a clean LaTeX/BibTeX rebuild and validate the resulting binary by metadata inspection, text extraction, page rendering, citation-key checks, and missing/duplicate bibliography audits.

The synchronization script is marker-based and idempotent. It aborts when an expected insertion anchor is missing or duplicated rather than replacing large files blindly. The validation workflow is enabled on `master` and records completion only after the clean PDF build and consistency checks pass.
