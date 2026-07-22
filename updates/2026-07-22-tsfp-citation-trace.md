# 22 July 2026 core-citation trace: time-sequential first-photon NLOS acquisition

## Verified missing paper

**Fast non-line-of-sight imaging based on first photon event stamping**  
Zhupeng Li, Xintong Liu, Jianyu Wang, Zuoqiang Shi, Lingyun Qiu, and Xing Fu  
*Optics Letters* 47(8), 1928–1931, 2022  
DOI: `10.1364/OL.446079`  
Publisher history: accepted 10 March 2022; published online 4 April 2022.

The paper was exposed by citation tracing from later transient-rendering and arbitrary-pattern NLOS work and was absent from repository-wide title and DOI searches. It is a direct active-transient NLOS method rather than a passing citation: time-sequential first-photon (TSFP) data explicitly models the SPAD detection process, and synthetic plus measured experiments show substantially shorter acquisition for comparable reconstruction quality. It complements LCT, f-k migration, and phasor-field inversion by reducing the photon-collection burden before reconstruction.

## Intended synchronization

The guarded synchronizer updates:

- `README.md`: one formal Latest Additions row and a 2022 acquisition milestone;
- `index.html`: one searchable paper object, the 2022 timeline, and tracked-entry count 181 → 182;
- `article/2active.tex`: the active-SPAD table and a literature-review paragraph in the SPAD hardware discussion;
- `bare_jrnl.tex`: a dated integration marker while preserving the existing included-section structure;
- `egbib_merged_20260711.bib`: regenerated from canonical bibliography supplements.

The pull-request workflow then performs a clean `pdflatex → bibtex → pdflatex ×2` build, verifies the citation and DOI occur exactly once in the relevant artifacts, checks for undefined citations or repeated BibTeX records, extracts the rebuilt PDF text, and commits `bare_jrnl.pdf` only after all checks pass.

## Exclusion and freshness notes

The search rechecked recent 2026 optical, passive, acoustic, consumer-LiDAR, radar/RF, and learned-reconstruction records already present in the repository, including adaptive spiral scanning, cost-effective FMCW interferometry, diffuse-aware passive encoding, thermal NLOS, learned LCT, and PICL. No direct NLOS publication with a verified online-publication date later than PICL on 15 July 2026 was found in this run.
