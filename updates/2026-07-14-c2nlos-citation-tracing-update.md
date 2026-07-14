# 14 July 2026 C2NLOS citation-tracing and venue-consistency update

## Search result

Fresh searches across arXiv, conference and journal indexes, project pages, and recent NLOS modality keywords did not reveal a directly relevant, metadata-verifiable NLOS imaging paper newer than the 5 July 2026 NIR raster-scanning paper already covered by the repository.

The high-priority citation/reference-tracing pass did identify a survey-consistency gap for an existing repository entry:

- **Efficient Non-Line-of-Sight Imaging from Transient Sinograms** — Mariko Isogawa, Dorian Chan, Ye Yuan, Kris M. Kitani, Matthew O'Toole.
- The repository previously labeled the work as **arXiv 2020**.
- The arXiv record states that it appeared at **ECCV 2020**, and the authors' project page supplies an ECCV `@InProceedings` record. The public-facing venue should therefore be **ECCV 2020**, while the arXiv record remains a useful manuscript link.

## Why the paper is a high-confidence NLOS milestone

C2NLOS is a direct active transient NLOS imaging method, not a paper that merely cites NLOS in passing. It extends the confocal acquisition introduced with the light-cone transform and explicitly discusses the dense raster-scan limitation of LCT and fast f-k migration. Instead of scanning a two-dimensional relay-wall grid, it scans one circular confocal path. After the LCT time reparameterization, hidden scatterers form sinusoids in a transient sinogram; their amplitude, phase, and offset encode three-dimensional position. The paper develops Hough-voting, inverse-Radon, and compact linear reconstruction procedures and validates them on simulated and real measurements, using roughly an order of magnitude fewer measurements than conventional dense scans.

This contribution belongs in the development trajectory between the 2018--2019 fast confocal inverses and later sparse, irregular, few-shot, and learned acquisition methods.

## Repository synchronization

The marker-based synchronizer updates the following artifacts without blind whole-file replacement:

1. `README.md`: corrects the venue to ECCV 2020, expands the contribution summary, and adds C2NLOS to the 2020 milestone timeline.
2. `index.html`: corrects the searchable paper metadata and expands the 2020 timeline. The tracked-entry count remains unchanged because the paper was already present.
3. `article/2active.tex`: adds the canonical citation to the active-SPAD table and inserts a literature-review paragraph immediately after the LCT discussion.
4. `egbib_20260714_c2nlos_updates.bib`: adds a final-venue `@inproceedings` record without inventing unverified DOI or page metadata.
5. `egbib_merged_20260711.bib` and `bare_jrnl.tex`: regenerated through the repository's duplicate-aware bibliography merger.
6. `bare_jrnl.pdf`: rebuilt only after clean LaTeX/BibTeX, citation, bibliography, text-extraction, and page-rendering checks pass.

**Build status:** README, homepage/timeline, survey source, merged bibliography, and regenerated PDF were synchronized; clean build and citation/PDF checks passed.
