# NLOS literature reconciliation — 18 October 2026 (TE-NLOS)

## Integrated source
Miao, Jinye; Guo, Enlai; Shi, Yingjie; Cai, Fuyao; Bai, Lianfa; Han, Jing. “Super-resolution non-line-of-sight imaging based on temporal encoding.” *Optics Express* **31**(24), 40235–40248 (2023). DOI: https://doi.org/10.1364/OE.504894. Publisher and PubMed PMID 38041329 confirm journal venue, authors, issue and pages. Temporal encoding with spatial–temporal correlation recovers computationally finer transients (reported 20 ps) from nanosecond-scale single-photon timing; this is not a claim that the detector SPTR itself improved.

## Cross-artifact placement
- README: Latest Additions, active transient-reconstruction list, 2023 milestone timeline.
- index.html: Core Reading Path, with previously missing IEEE ICIP 2021 ERTI follow-up direct link.
- data/papers-source.html: 2023 timeline and searchable Paper Explorer entry; date updated.
- article/2active.tex: short literature review immediately before the 2026 temporal-decoupling paragraph.
- bare_jrnl.tex: retains the article/2active.tex input and documents this integration.
- egbib_merged_20260711.bib: unique verified citation key `miaoTemporalEncodingNLOS2023`.

## Literature/citation tracing scope
Publisher, PubMed, arXiv, dblp, recent journal/conference and project-page searches covered active LCT/phasor-field/f-k successors, computational periscopy/ERTI, acoustic and radar/RF, thermal and Gaussian transient rendering. The 2026 Cascaded NLOS (ACM TOG/SIGGRAPH Asia), 3D Gaussian Transient Rendering (SIGGRAPH), passive acoustic diffraction (Physical Review Applied), and TRT-NLOS (arXiv, no verified final venue) are already in the repository. This was a targeted, not exhaustive, forward-citation pass; no additional verified missing paper was added beyond TE-NLOS.

## PDF build outstanding
`bare_jrnl.pdf` was **not** regenerated or uploaded in this source commit. The execution container cannot resolve github.com and cannot obtain the full 52-MB repository with figure assets. On a complete checkout, run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`, check `bare_jrnl.log` and `bare_jrnl.blg` for missing/duplicate citations, verify the new bibliography citation and rendered pages with `pdfinfo`/`pdftotext`, then commit `bare_jrnl.pdf`. Do not mark PDF consistent until its blob SHA changes.
