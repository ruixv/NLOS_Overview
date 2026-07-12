# 12 July 2026 — 6G initial-access NLOS imaging update

## Search and citation-tracing result

Fresh searches across arXiv, publisher pages, project/lab pages, and scholarly indexes did not reveal a newer high-confidence direct NLOS-imaging paper than the 5 July 2026 NIR raster-scanning paper already tracked by the repository. Citation and development-chain tracing of the repository's radar/RF branch did identify one relevant missing work:

- **Enabling NLOS Imaging Capabilities at the Initial Access of 6G Base Stations** — Davide Tornielli Bellini, Dario Tagliaferri, Pietro Grassi, Davide Scazzoli, Stefano Tebaldini, and Umberto Spagnolini, arXiv:2511.15416 (2025).

This is genuinely NLOS imaging rather than a paper that cites NLOS in passing. It defines radio imaging as recovery of an environmental reflectivity map and target shape, integrates monostatic hidden-region imaging into a standard-compliant base-station initial-access beam sweep, jointly designs a low-cost static modular reflector and imaging-specific beam-codebook entries, coherently combines multiple reflected viewpoints, derives near-field spatial resolution and effective-aperture expressions, compensates moving-target velocity, quantifies communication–imaging trade-offs, and reports numerical and experimental validation.

The paper is also a direct development of the repository's existing **Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins** branch: its related-work section identifies the earlier EM-skin and multi-view ISAC contributions as preliminary NLOS-imaging systems, then addresses the previously untreated cost and performance trade-offs of integrating imaging into cellular initial access.

## Venue verification

As checked on 12 July 2026, the arXiv record lists no journal reference or accepted conference/journal venue. The repository therefore labels the work **arXiv 2025** rather than inferring a final venue.

## Repository integration

The synchronization workflow is designed to update the following artifacts consistently:

- `README.md`: add the paper to Latest Additions with verified metadata and a concise contribution summary.
- `index.html`: add a searchable paper-explorer record, update the tracked-entry count from 88 to 89, and extend the 2025 development-timeline description.
- `article/5newscenes.tex`: add a literature-review paragraph to the radar/RF NLOS section, connecting static EM-skin prototypes to standard-aware 6G ISAC deployment.
- `egbib_20260712_initial_access_updates.bib`: provide the canonical BibTeX record `tornielliInitialAccessNLOS2025`.
- `egbib_merged_20260711.bib`: regenerate the duplicate-free consolidated bibliography and verify zero missing citation keys.
- `bare_jrnl.pdf`: perform a clean LaTeX/BibTeX rebuild and validate the source citation, generated bibliography, and searchable PDF text.

Source: https://arxiv.org/abs/2511.15416

**Build result:** pending the automated clean LaTeX/BibTeX synchronization and validation run.
