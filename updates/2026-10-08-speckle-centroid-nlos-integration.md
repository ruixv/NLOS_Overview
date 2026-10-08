# 8 October 2026 — Passive speckle-centroid NLOS tracking integration and PDF rebuild

## Verified literature addition
Aiping Zhai, Wenjing Ji, Yan Wang, Xiyuan Luo, Wenjing Zhao, Dong Wang, and Fei Liu, “Non-Invasively Tracking an Arbitrary Deformable Object Through Scattering Media and Around Corners via Speckle Correlations,” *Advanced Science*, vol. 13, no. 34, article e75072 (2026). DOI: https://doi.org/10.1002/advs.75072. First published 3 April 2026 (publisher record).

SCCLM uses centroids of successive speckle auto- and cross-correlations to recover relative displacements despite hidden-object deformation. The authors demonstrate an around-corner case as well as tracking through static/dynamic scattering media. This is **passive NLOS trajectory tracking**, not full hidden-image reconstruction; it is classified as tightly adjacent NLOS sensing rather than a core volumetric reconstruction milestone.

## Canonical source changes
- README.md: latest additions, main literature table, 2026 milestone timeline.
- data/papers-source.html: Paper Explorer entry and 2026 historical timeline; index.html dynamically loads this data, so its static Core Reading Path needs no tracking-only entry.
- article/3passive.tex: contextual literature-review paragraph; bare_jrnl.tex imports the chapter unchanged.
- egbib_2026_updates.bib and egbib_merged_20260711.bib: verified publisher metadata, citation key `zhaiSpeckleCentroidTracking2026`.

Development-branch checks: DOI in README, website data, and both bibliography sources; exactly one matching entry in merged bibliography; one passive-chapter citation; balanced braces in modified chapter and merged bibliography.

## PDF status and recovery
**bare_jrnl.pdf is not yet verified as rebuilt.** The existing workflow `.github/workflows/rebuild_nlos_citation_gap_pdf_20260718.yml` will be triggered by a harmless workflow-comment update reaching master. Check the actual workflow run, LaTeX/BibTeX logs, and PDF binary commit. If it fails, preserve source changes and retry without disabling subsequent literature checks. Never report PDF synchronization without verifying the binary commit.
