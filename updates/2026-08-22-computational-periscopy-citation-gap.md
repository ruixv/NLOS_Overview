# 22 August 2026 — computational-periscopy forward-citation gap

**Integrated on 22 August 2026.** README, the canonical V2 corpus/timeline, passive-survey prose/table, final-venue BibTeX, and the rebuilt survey PDF are synchronized by the guarded integration workflow.

## Why this patch is staged instead of overwriting public artifacts

This run traced the passive computational-periscopy lineage forward from Saunders et al., *Computational periscopy with an ordinary digital camera* (Nature 2019). The current repository already contains two of the resulting works in the survey table / bibliography, but not consistently across README, V2 Paper Explorer, survey prose, and final-venue metadata. Direct whole-file replacement of the large public artifacts is intentionally avoided here. Apply the insertions below in one guarded checkout/build so README, `data/papers-source.html`, survey source, merged BibTeX, and `bare_jrnl.pdf` cannot drift.

## Verified records

### 1. Corner Occluder Computational Periscopy: Estimating a Hidden Scene from a Single Photograph

- Sheila W. Seidel, Yanting Ma, John Murray-Bruce, Charles Saunders, William T. Freeman, Christopher C. Yu, Vivek K. Goyal
- IEEE ICCP 2019, 1–9
- DOI: `10.1109/ICCPHOT.2019.8747342`
- Repository state: canonical BibTeX `DBLP:conf/iccp/SeidelMMSFYG19` and the passive-method table already exist, but the paper is absent from the V2 Paper Explorer / development timeline.
- Contribution: uses the known vertical wall edge as an occluding aperture; from one ordinary-camera photograph of the floor penumbra, jointly estimates unknown floor albedo and a 1-D angular representation of the hidden scene with regularization separating floor texture from hidden-scene variation.

### 2. Multi-Depth Computational Periscopy with an Ordinary Camera

- Charles Saunders, Rishabh Bose, John Murray-Bruce, Vivek K. Goyal
- IEEE ICASSP 2020, 9299–9305
- DOI: `10.1109/ICASSP40776.2020.9054518`
- Repository state: absent from README, V2 Paper Explorer, survey prose/table, and merged bibliography.
- Contribution: extends ordinary-camera computational periscopy from a single hidden depth to two hidden planes; a single photograph recovers both the hidden images and their distances from the visible wall, introducing depth-from-defocus information into passive computational periscopy.

### 3. Two-Dimensional Non-Line-of-Sight Scene Estimation From a Single Edge Occluder

- Sheila W. Seidel, John Murray-Bruce, Yanting Ma, Christopher C. Yu, William T. Freeman, Vivek K. Goyal
- IEEE Transactions on Computational Imaging 7, 58–72 (2021)
- DOI: `10.1109/TCI.2020.3037405`
- Repository state: already cited in the passive-method table as `seidelTwoDimensionalNonLineofSightScene2020`, but the merged bibliography still labels it as arXiv 2020 and lacks the final DOI/venue; it is absent from the V2 Paper Explorer / timeline.
- Required metadata action: **replace the existing BibTeX entry in place with the final IEEE TCI record; do not add a duplicate key.**
- Contribution: upgrades edge-occluder computational periscopy from angular-only hidden-scene estimation to a 2-D angle/range reconstruction from one penumbra photograph, with a radial-falloff forward model, two inversion algorithms, and Cramér–Rao analysis.

### 4. Fast Computational Periscopy in Challenging Ambient Light Conditions through Optimized Preconditioning

- Charles Saunders, Vivek K. Goyal
- IEEE ICCP 2021, 1–9
- DOI: `10.1109/ICCP51581.2021.9466264`
- Repository state: absent from README, V2 Paper Explorer, survey prose/table, and merged bibliography.
- Contribution: replaces simple finite-difference background suppression with an optimized preconditioning / generalized-pseudoinverse formulation that approximately nulls plausible ambient background while conditioning the hidden-scene inverse, improving robustness below unit SBR and enabling substantially faster reconstruction.

## Intended literature trajectory

The passive computational-periscopy discussion should make this evolution explicit:

`Nature computational periscopy (2019)` → `single-photograph corner-edge inversion (ICCP 2019)` → `multi-depth recovery (ICASSP 2020)` → `2-D angle/range edge-camera reconstruction (IEEE TCI 2021)` → `optimized preconditioning for strong ambient light / fast recovery (ICCP 2021)` → later untrained, diffusion, MDUNet, long-range, spectral, and rough-relay passive NLOS.

## Exact public-artifact insertion plan

### `README.md`

Add concise rows under **Latest Additions** for the two entirely missing papers (`saundersMultiDepthPeriscopy2020`, `saundersFastPeriscopy2021`) and one final-venue correction row for the TCI paper. In the historical timeline:

- 2019: after ordinary-camera computational periscopy, add the single-edge one-photograph branch.
- 2020: add multi-depth computational periscopy.
- 2021: add 2-D angle/range single-edge reconstruction and optimized-preconditioning ambient robustness.

Do not duplicate the existing ICCP-2019 BibTeX record.

### `data/papers-source.html`

Add Paper Explorer objects for all four records because none appears in the current V2 canonical corpus. Use categories such as `passive occlusion computational periscopy` and final DOI URLs. Update the tracked-entry counter only after confirming the actual object count.

Suggested concise keys:

- ICCP 2019: `Single ordinary-camera photograph of the floor penumbra jointly estimates floor albedo and a 1-D hidden angular scene using the wall edge as a natural aperture.`
- ICASSP 2020: `Extends ordinary-camera computational periscopy to multi-depth hidden scenes, recovering two hidden images and their wall-relative depths from one photograph.`
- IEEE TCI 2021: `Adds range to edge-occluder angular sensing, reconstructing a 2-D hidden scene from one penumbra photograph with radial-falloff modeling and CRB analysis.`
- ICCP 2021: `Optimized preconditioning suppresses strong ambient background while improving inverse conditioning, enabling robust, substantially faster passive computational periscopy.`

### `article/3passive.tex`

The passive-method table already cites the ICCP-2019 and TCI edge-occluder papers. Add `saundersMultiDepthPeriscopy2020` and `saundersFastPeriscopy2021` to the conventional-camera / partial-occluder row.

Immediately after the introductory conventional-camera / computational-periscopy discussion, add a compact paragraph titled approximately **“From edge apertures to multi-depth and background-robust computational periscopy.”** Explain the four-step trajectory above rather than appending four disconnected paper summaries.

### `egbib_merged_20260711.bib`

- Keep the existing `DBLP:conf/iccp/SeidelMMSFYG19` ICCP-2019 entry.
- Add `saundersMultiDepthPeriscopy2020` from `egbib_20260822_computational_periscopy_gap.bib`.
- Replace existing `seidelTwoDimensionalNonLineofSightScene2020` arXiv metadata with the final IEEE TCI entry from the staging file, keeping the same citation key so existing LaTeX citations remain valid.
- Add `saundersFastPeriscopy2021`.
- Verify one DOI occurrence each for `10.1109/ICCPHOT.2019.8747342`, `10.1109/ICASSP40776.2020.9054518`, `10.1109/TCI.2020.3037405`, and `10.1109/ICCP51581.2021.9466264`.

### `bare_jrnl.tex` / `bare_jrnl.pdf`

Add a 22-August provenance comment only after the source integration succeeds. Rebuild with the repository's normal `pdflatex → bibtex → pdflatex → pdflatex` sequence. Do not publish a PDF update unless all four citation keys resolve, no undefined-citation warnings remain, and rendered pages are visually valid.

## Consistency gate

Before committing public artifacts, verify:

1. README and V2 contain all four computational-periscopy records.
2. `article/3passive.tex` explains the lineage and cites all four.
3. The merged BibTeX has exactly one canonical record per DOI and the TCI paper is no longer labeled arXiv-only.
4. `bare_jrnl.pdf` contains the new computational-periscopy paragraph and resolves the citations.
5. The V2 paper count is recomputed rather than manually guessed.

Until that guarded integration/build is completed, the public `bare_jrnl.pdf` should be treated as the previous validated build; this staging note does **not** claim that the PDF has already been updated.
