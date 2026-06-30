# 2026-07-01 homepage and bibliography consistency sync

## Summary

This run did not identify a new high-confidence NLOS imaging paper that was missing from the current README. Fresh searches and citation-oriented keyword checks mainly returned entries already covered by the repository, including 3D Gaussian Transient Rendering, Marco et al.'s ToF comparative study, TransiT, TLTM iteration, EM-skin radar NLOS, arbitrary-pattern active NLOS, few-shot SSCR, and SSD.

The useful work in this run was therefore a consistency sync across public-facing artifacts:

1. `index.html` was updated from the older 29 June 2026 snapshot to a 1 July 2026 snapshot.
2. The homepage latest-entry count was changed from 31 to 36 to match the README's current latest-addition table.
3. The homepage paper explorer now includes the README entries that were missing from the previous site snapshot:
   - TransiT: Transient Transformer for Non-line-of-sight Videography
   - Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging
   - Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins
   - Non-line-of-sight imaging with arbitrary illumination and detection pattern
   - Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization
4. The homepage SSD metadata was corrected to `arXiv 2026`, matching the README and BibTeX supplement.
5. The previously unverified homepage-only items `Polarization-Based Scanning-Free Single-Pixel NLOS Imaging` and `Super-Field-of-View NLOS via Spatial Encoding` were removed from the paper explorer, consistent with the earlier survey cleanup.
6. `egbib_2026_updates.bib` was updated with the missing `liTransiT2025` BibTeX entry because `article/4datadriven.tex` already cites `\cite{liTransiT2025}`.

## Fresh-search observations

Covered / already present:

- `Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering` — already in README and homepage.
- `A comprehensive study of time-of-flight non-line-of-sight imaging` — already in README and homepage.
- `TransiT: Transient Transformer for Non-line-of-sight Videography` — already in README and survey text; homepage and BibTeX were the missing pieces fixed here.
- `Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging` — already in README and survey text; homepage was synchronized here.
- `Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins` — already in README and survey text; homepage was synchronized here.
- `Non-line-of-sight imaging with arbitrary illumination and detection pattern` — already in README and BibTeX; homepage latest list was synchronized here.
- `Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization` — already in README and BibTeX; homepage latest list was synchronized here.

Checked but not added:

- `Near-losslesss method for generating thermal photon-bunched light` (arXiv:2602.00633) mentions non-line-of-sight imaging as a possible sensing application for photon-bunching sources, but it does not itself demonstrate or propose a concrete NLOS reconstruction/localization/imaging method. It is better treated as adjacent photonics-enabling work rather than a repository entry.

## Files changed

- `index.html`
- `egbib_2026_updates.bib`
- `updates/2026-07-01-homepage-bib-consistency-sync.md`

## Remaining PDF status

The LaTeX source still requires `bare_jrnl.tex` to use:

```tex
\bibliography{egbib,egbib_2026_updates}
```

instead of:

```tex
\bibliography{egbib}
```

The PDF was not regenerated in this run because there was no safe local LaTeX compilation plus binary GitHub upload path available. Source-side consistency is improved, but `bare_jrnl.pdf` still needs local compilation and upload after the bibliography line is changed.
