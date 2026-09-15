# 2026-09-16 TLTM final-venue correction

## Verified metadata update

The repository already contains **Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging** (Sultan et al.) from the 2024 arXiv preprint, but its tracked venue is stale. The work is now formally published as:

- **Talha Sultan, Eric Brandt, Khadijeh Masumnia-Bisheh, Simone Riccardo, Pavel Polynkin, Alberto Tosi, Andreas Velten**
- **Nature Communications 17, 8951 (2026)**
- DOI: **10.1038/s41467-026-75177-4**
- Published: **22 July 2026**; Version of Record: **25 August 2026**
- Final paper: https://doi.org/10.1038/s41467-026-75177-4

Nature Communications verifies that the method measures a full relay-surface first-order transient light transport matrix (TLTM-1) with dense laser scanning and a gated 16x16 SPAD array, then computationally focuses virtual illumination and detection into the hidden scene to recover TLTM-2. This exposes hidden-patch-to-hidden-patch time-resolved transport, including indirect shadows, interreflections, volumetric scattering, direct/indirect separation, virtual relighting, multi-view reconstruction, and dual photography. The paper explicitly builds on the phasor-field framework and cites the Velten 2012, O'Toole LCT, Lindell f-k, and Liu phasor-field milestones, so it is a high-confidence Core-paper descendant rather than a passing citation.

## Required repository synchronization

The earlier update note `updates/2026-06-30-tltm-emskin-update.md` records this paper as `arXiv 2024`. That metadata should now be superseded everywhere by the final venue above.

1. **README.md**: locate the TLTM entry and change venue/year from `arXiv 2024` to `Nature Communications 17, 8951 (2026)`; point the primary paper link to the DOI. Preserve the arXiv link only as an optional preprint link.
2. **index.html / Paper Explorer / latest additions / timeline**: make the same venue/year/link correction. Timeline placement should be 2026, with a concise contribution summary emphasizing the shift from hidden geometry reconstruction to recovery of higher-order hidden-scene transient transport.
3. **Survey LaTeX**: in the existing `Transient Light-Transport-Matrix Iteration` discussion, update the citation metadata and, if useful, describe the trajectory as `third-bounce geometry reconstruction -> virtual hidden-scene focusing -> experimentally recovered TLTM-2 -> higher-order hidden light transport and relighting`.
4. **Canonical bibliography**: replace/supersede the arXiv-only `sultanIteratingTLTM2024` entry with the verified Nature Communications entry staged in `egbib_20260916_tltm_final_venue.bib`. Avoid duplicate citation keys in the compiled bibliography.
5. **bare_jrnl.pdf**: rebuild only after the canonical bibliography and LaTeX citation are synchronized.

## Search result for this run

A fresh keyword/modality search and Core-paper citation-tracing pass was performed across active/passive optical NLOS, SPAD/transient imaging, thermal, acoustic, RF/mmWave, consumer LiDAR, learned reconstruction, LCT, f-k migration, and phasor-field descendants. Other strong recent hits were already represented in the repository or prior update logs. No additional paper met the threshold for a genuinely new, metadata-verifiable NLOS entry in this run. The meaningful change is therefore this final-venue correction rather than adding a duplicate paper.

## Build status

Large public-facing files were not overwritten from truncated connector payloads. `bare_jrnl.pdf` was not rebuilt in this run. The final-venue BibTeX and this precise synchronization note were committed safely; README/index/survey/canonical-bib/PDF synchronization remains pending until those files can be edited from complete content without truncation risk.
