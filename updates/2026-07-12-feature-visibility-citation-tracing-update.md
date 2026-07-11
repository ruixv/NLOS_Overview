# NLOS feature-visibility citation-tracing update (12 July 2026)

## Search outcome

Fresh arXiv, publisher, project-page, and lab-page searches did not identify a direct NLOS imaging paper newer than the 5 July 2026 NIR raster-scanning paper already covered by the repository. A citation/reference-tracing pass through the repository's active-ToF milestones and the 2026 comparative ToF study did, however, expose a public-artifact consistency gap for an important foundational analysis:

- **Analysis of Feature Visibility in Non-Line-of-Sight Measurements** — Xiaochun Liu, Sebastian Bauer, Andreas Velten, CVPR 2019.

The paper is directly about transient NLOS imaging rather than a passing citation. It analyzes which hidden-scene features are recoverable and how surface orientation, finite relay-wall aperture, and acquisition geometry create visibility limits. This provides a limit-aware bridge between early filtered-backprojection methods and later LCT, f-k migration, phasor-field, normal-aware, and occlusion-aware reconstruction.

The survey source and consolidated bibliography already contained the canonical citation key `liuAnalysisFeatureVisibility2019`, but the paper was absent from `README.md`, the homepage paper explorer, and the development timeline. The existing survey mention was also only a brief ill-posedness citation, so this update adds a semantically placed literature-review paragraph without creating a duplicate bibliography record.

## Repository synchronization

The anchor-checked script `scripts/sync_nlos_20260712_feature_visibility.py` performs the following idempotent updates:

1. Adds the verified CVPR 2019 paper to `README.md` and advances the update date to 12 July 2026.
2. Adds a searchable paper object to `index.html`, updates the 2019 development timeline, synchronizes both homepage dates, and changes the tracked-latest count from 84 to 85.
3. Inserts a short `Visibility limits and recoverability` literature-review paragraph into `article/2active.tex` beside the phasor-field/light-transport discussion rather than appending an isolated list.
4. Reuses the existing canonical BibTeX key `liuAnalysisFeatureVisibility2019` in `egbib_merged_20260711.bib`; no additional `.bib` file or duplicate record is introduced.
5. Regenerates the duplicate-free consolidated bibliography and rebuilds `bare_jrnl.pdf` through the repository's validated LaTeX workflow.

## Metadata decision

The final venue is **CVPR 2019**, not arXiv. The canonical repository bibliography already records the complete authors, conference, title, year, and page range 10140--10148. The public-facing entry links to the CVF Open Access paper page. No unverified DOI is asserted.

## Consistency requirements

The update is considered complete only when all of the following hold:

- the title is present in `README.md` and `index.html`;
- the new literature-review paragraph cites `liuAnalysisFeatureVisibility2019` in `article/2active.tex`;
- the merged bibliography contains exactly one `liuAnalysisFeatureVisibility2019` record;
- LaTeX/BibTeX report no missing or repeated citation entries;
- `pdfinfo` and `pdftotext` succeed on the rebuilt PDF; and
- both the paper title and the `Visibility limits and recoverability` discussion are found in the generated PDF text.
