# 15 July 2026 self-calibrating NLOS inverse-rendering consistency update

**Build status:** README, homepage/paper explorer, survey source, merged bibliography, and regenerated PDF are mutually consistent; clean build, citation, bibliography, text-extraction, and page-render checks passed.

## Search and citation-tracing result

Fresh searches of recent arXiv, conference, journal, project-page, and laboratory-page updates did not identify a high-confidence direct NLOS imaging paper newer than the repository's 5 July 2026 NIR raster-scanning entry.

The high-priority forward-citation pass did identify a cross-artifact consistency gap for:

- **Self-Calibrating, Fully Differentiable NLOS Inverse Rendering** — Kiseok Choi, Inchul Kim, Dongyoung Choi, Julio Marco, Diego Gutiérrez, and Min H. Kim, ACM TOG / SIGGRAPH Asia 2023, DOI `10.1145/3610548.3618140`.

The paper directly cites the field-defining Velten 2012, LCT, f-k migration, Fermat-path, and phasor-field lines, and is itself treated by the 2026 3D Gaussian Transient Rendering paper as an important predecessor in differentiable transient inverse rendering. It is genuinely active ToF NLOS reconstruction rather than a passing citation: the method couples phasor-field volumetric imaging with differentiable path-space transient rendering and jointly self-calibrates virtual-illumination filters, laser/sensor temporal response, hidden geometry, normals, and albedo from measured transients.

## Existing repository state

The title was already present in `README.md` and the homepage paper explorer, so this update must not increment the tracked-entry count. However:

1. the public links pointed to arXiv rather than the verified ACM DOI;
2. the public venue omitted the ACM TOG publication context;
3. the 2023 timeline did not explain the paper's specific self-calibration contribution;
4. `article/2active.tex` did not contain a dedicated literature-review paragraph or citation;
5. the consolidated bibliography and rebuilt PDF did not include the paper.

## Intended synchronization

The marker-based script `scripts/sync_nlos_20260715_selfcal.py` will:

- update the README and homepage metadata to **ACM TOG / SIGGRAPH Asia 2023** and the DOI link;
- preserve the homepage tracked-entry count at **96**;
- add an explicit 2023 milestone for end-to-end self-calibrating differentiable NLOS inverse rendering;
- insert the paper into the active-SPAD reconstruction table;
- add a semantic paragraph immediately after the fast differentiable transient-rendering discussion;
- merge `egbib_20260715_selfcal_updates.bib` into the duplicate-free bibliography;
- clean-build and validate `bare_jrnl.pdf`.

The workflow rejects missing anchors, non-idempotent edits, undefined citations, missing BibTeX records, repeated BibTeX entries, empty PDFs, failed text extraction, and a rebuilt PDF with fewer rendered pages than the previous version.
