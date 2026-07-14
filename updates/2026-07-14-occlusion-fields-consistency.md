# 14 July 2026 Occlusion Fields consistency update

**Build status:** the survey integration and PDF rebuild passed; a final duplicate-row correction for README.md is staged for clean validation.

## Search and citation-tracing result

Fresh arXiv, conference, journal, project-page, and lab-page searches did not reveal a directly relevant NLOS-imaging paper newer than the NIR raster-scanning preprint submitted on 5 July 2026. A high-priority citation/reference-tracing pass through the Velten, LCT, f-k migration, phasor-field, Fermat-path, and neural-surface reconstruction line identified a high-confidence cross-artifact consistency gap:

- **Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction** — Javier Grau, Markus Plack, Patrick Haehn, Michael Weinmann, and Matthias Hullin, arXiv:2203.08657 (2022).
- Source: https://arxiv.org/abs/2203.08657
- Verified status on 14 July 2026: no authoritative conference or journal publication record was found, and the arXiv record does not identify a final venue; the repository therefore retains **arXiv 2022**.

This is a direct active transient NLOS reconstruction paper rather than a work that cites NLOS only in passing. It explicitly develops the Velten/LCT/f-k/phasor-field, surface-reconstruction, Fermat-path, feature-visibility, and Neural Transient Fields lineage. The method represents the hidden surface as the boundary between relay-wall-visible and target-occluded 3D space, predicts an implicit occlusion field from time-resolved measurements, extracts adaptive meshes, and demonstrates recovery beyond the conservative specular Fermat-path criterion under substantial self-occlusion.

README.md and the homepage paper explorer already contained terse records, while the LaTeX survey narrative, canonical bibliography supplement, consolidated bibliography, and compiled PDF did not. This update enriches the existing public records and repairs the survey/PDF consistency gap without increasing the existing homepage tracked-entry count.

## Synchronized changes

1. **README.md** — retain exactly one enriched paper row with verified arXiv-only status and add a 2022 milestone between the real-time 2021 and differentiable-rendering 2023 milestones.
2. **index.html** — enrich the existing searchable paper object while preserving the existing count of 96 tracked entries and the existing 2022 timeline placement.
3. **article/2active.tex** — integrate the paper into the `Surface` subsection immediately after the Fermat-path discussion, and include it in the active-SPAD reconstruction table.
4. **Bibliography** — add canonical key `grauOcclusionFields2022` in `egbib_20260714_occlusion_fields_updates.bib`, then regenerate the duplicate-free consolidated bibliography.
5. **bare_jrnl.pdf** — perform a clean LaTeX/BibTeX rebuild and validate the regenerated binary using metadata inspection, text extraction, page rendering, citation-key checks, and missing/duplicate bibliography audits.

The synchronization script is marker-based and idempotent. It removes the older terse README row when necessary, preserves one enriched entry, and aborts when any remaining insertion anchor is missing or duplicated rather than replacing large files blindly.
