# Final-venue and citation consistency audit — 29 October 2026

## Outcome

No new unique paper was added in this run. Citation tracing and the cross-chapter audit found that the recent, relevant candidates already appear in the repository catalog and in semantically appropriate survey sections. The actionable gaps were bibliographic consistency and two public timeline records that still exposed preprint-only labels despite verified final publications.

## Verified corrections

- **Fast Non-Line-of-Sight Imaging with Two-Step Deep Remapping** — Dayu Zhu and Wenshan Cai, *ACS Photonics* 9(6), 2046–2055 (2022), DOI [10.1021/acsphotonics.2c00186](https://doi.org/10.1021/acsphotonics.2c00186). The prior BibTeX DOI was incorrect; the official ACS record confirms the DOI, venue, issue, and pages.
- **Seeing Around Obstacles Using Active Terahertz Imaging** — Yiran Cui and Georgios C. Trichopoulos, *IEEE Transactions on Terahertz Science and Technology* 14(4), 433–445 (2024), DOI [10.1109/TTHZ.2024.3401041](https://doi.org/10.1109/TTHZ.2024.3401041). The 2022 arXiv title is an earlier version of this final journal paper and is no longer listed as a separate catalog item.
- Historical BibTeX aliases for Keyhole Imaging, self-calibrating differentiable NLOS inverse rendering, MARMOT, consumer-LiDAR NLOS, DG-NLOS, Quasi-Fresnel reconstruction, iterative transient-light-transport matrices, passive acoustic localization, arbitrary illumination/detection patterns, and RIS-assisted around-corner radar now resolve to their verified final publication metadata rather than arXiv-only records.
- The bibliography merge source retains citation-compatible legacy keys while assigning final venue, year, DOI, and pagination wherever verified. Truly preprint-only works remain labeled arXiv.

## Citation-tracing coverage

Forward-citation and scholarly-index checks revisited Velten et al. (2012), LCT, f-k migration, phasor fields, computational periscopy, PAC-Net/NLOS-Track, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Recent candidate papers—including MALCT, rough-wall thermal NLOS, higher-order TLTM recovery, sub-THz deep unfolding, and X-band radar NLOS—were verified as already represented. No additional unique, verified missing paper warranted a new catalog entry.

## Files updated

- `README.md`: removed the obsolete THz preprint timeline duplicate, corrected two-step deep-remapping metadata, and recorded the audit.
- `data/papers-source.html`: changed the THz and two-step deep-remapping Paper Explorer records to final venue metadata.
- `egbib.bib`, `egbib_2026_updates.bib`, `egbib_merged_20260711.bib`, and `egbib_zz_20261029_final_venue_audit.bib`: corrected the publisher DOI and reconciled historical citation aliases.
- `bare_jrnl.tex`: recorded the metadata audit in the source-history comment; the existing survey prose already covers the verified papers in the appropriate sections.
- `index.html`: a short audit-status entry is added alongside the existing citation-trace log.

## Build validation

Result: successful clean LaTeX/BibTeX rebuild and source validation in [GitHub Actions run #40805416147](https://github.com/ruixv/NLOS_Overview/actions/runs/40805416147). The build checked for undefined citations/references and missing/repeated BibTeX records, and the survey title plus required recent citation/text checks passed. The PDF is 72 pages and 2,383,677 bytes; its committed blob SHA is `707e83934476cebb747aae8d53816708cb20f12b`. The generated PDF was byte-identical, so the workflow correctly skipped a redundant binary commit. The recurring paper-source synchronizers were repaired to write catalog entries to `data/papers-source.html`, keep the index count synchronized, and avoid the obsolete `index.html` paper-array anchor. The legacy update-horizon helper now leaves a reworded/absent scope sentence unchanged instead of aborting the full synchronization.
