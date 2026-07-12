# 12 July 2026 — 6G initial-access NLOS imaging update

## Search and citation-tracing result

Fresh searches across arXiv, publisher pages, project/lab pages, and scholarly indexes did not reveal a newer high-confidence direct NLOS-imaging paper than the 5 July 2026 NIR raster-scanning paper already tracked by the repository. Citation and development-chain tracing of the repository's radar/RF branch did identify one relevant missing work:

- **Enabling NLOS Imaging Capabilities at the Initial Access of 6G Base Stations** — Davide Tornielli Bellini, Dario Tagliaferri, Pietro Grassi, Davide Scazzoli, Stefano Tebaldini, and Umberto Spagnolini, arXiv:2511.15416 (2025).

This is genuinely NLOS imaging rather than a paper that cites NLOS in passing. It defines radio imaging as recovery of an environmental reflectivity map and target shape, integrates monostatic hidden-region imaging into a standard-compliant base-station initial-access beam sweep, jointly designs a low-cost static modular reflector and imaging-specific beam-codebook entries, coherently combines multiple reflected viewpoints, derives near-field spatial resolution and effective-aperture expressions, compensates moving-target velocity, quantifies communication–imaging trade-offs, and reports numerical and experimental validation.

The paper is also a direct development of the repository's existing **Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins** branch: its related-work section identifies the earlier EM-skin and multi-view ISAC contributions as preliminary NLOS-imaging systems, then addresses the previously untreated cost and performance trade-offs of integrating imaging into cellular initial access.

## Venue verification

As checked on 12 July 2026, the arXiv record lists no journal reference or accepted conference/journal venue. The repository therefore labels the work **arXiv 2025** rather than inferring a final venue.

## Safe patch locations

The connector can safely create compact source and update files, but connector-generated GitHub events did not start the repository Actions workflow in this run. To avoid replacing large hand-maintained files blindly, the public-facing edits are preserved as an idempotent marker-based synchronizer in `scripts/sync_nlos_20260712_initial_access.py`. Its exact insertions are summarized below.

### `README.md`

Insert immediately before the existing 2025 MITO row in **Latest Additions**:

```markdown
| 2025 | [Enabling NLOS Imaging Capabilities at the Initial Access of 6G Base Stations](https://arxiv.org/abs/2511.15416) — Tornielli Bellini et al. | arXiv 2025 | Integrates coherent reflector-assisted NLOS imaging into the standard initial-access beam sweep of a next-generation base station; jointly designs a static modular reflector and imaging-specific codebook, derives near-field resolution/effective-aperture and moving-target trade-offs, and validates the system experimentally. |
```

### `index.html`

1. Change the tracked-latest count from `88` to `89`.
2. Insert immediately before the MITO paper object:

```javascript
{cat:"latest modality active",title:"Enabling NLOS Imaging Capabilities at the Initial Access of 6G Base Stations",authors:"Tornielli Bellini et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2511.15416",key:"Integrates coherent reflector-assisted NLOS imaging into a 5G/6G base-station initial-access beam sweep, deriving effective-aperture and moving-target trade-offs and validating the system experimentally."},
```

3. Extend the 2025 timeline heading with **6G initial-access imaging** and add **reflector-assisted base-station initial-access imaging** to its summary.

### `article/5newscenes.tex`

Insert at the end of **Radar-Based NLOS Imaging**, immediately before the `Acoustic NLOS Imaging` bookmark:

```latex
Tornielli Bellini~\etal~push reflector-assisted RF NLOS imaging toward communication infrastructure by embedding a monostatic hidden-scene imaging mode into the initial-access beam sweep of a next-generation base station~\cite{tornielliInitialAccessNLOS2025}. A low-cost non-reconfigurable modular reflector and imaging-specific codebook extend the standard communication beams; coherent processing across the resulting viewpoints forms an effective aperture for near-field reflectivity imaging, while a maximum-likelihood velocity estimator compensates moving targets. By deriving resolution, aperture, latency, SNR, and communication--imaging trade-offs and validating the design experimentally, this work connects earlier electromagnetic-skin NLOS prototypes to standard-aware 6G ISAC deployment.
```

### Bibliography and PDF

- `egbib_20260712_initial_access_updates.bib` contains the canonical record `tornielliInitialAccessNLOS2025`.
- After applying the text patch, run `python scripts/merge_nlos_bibliography.py` to regenerate `egbib_merged_20260711.bib` and audit missing/duplicate keys.
- Then run a clean `latexmk -pdf bare_jrnl.tex`, verify the citation in `.aux`/`.bbl`, check for undefined or repeated entries, and replace `bare_jrnl.pdf` only after `pdfinfo` and `pdftotext` validation pass.

Source: https://arxiv.org/abs/2511.15416

**Build result:** the canonical BibTeX record, exact marker-based synchronizer, workflow definition, and this patch note were committed. `README.md`, `index.html`, `article/5newscenes.tex`, the merged bibliography, and `bare_jrnl.pdf` were not claimed as updated because the connector-triggered workflow did not start; replacing those large files without executing and validating the synchronizer would risk truncation or inconsistency.
