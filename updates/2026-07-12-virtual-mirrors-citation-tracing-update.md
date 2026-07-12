# 12 July 2026 citation-tracing update: Virtual Mirrors

## Search outcome

Fresh keyword searches across recent arXiv and public paper/project pages did not identify a newer high-confidence direct NLOS-imaging paper than the already tracked 5 July 2026 NIR raster-scanning preprint. A forward/reference-tracing pass from the repository's active-NLOS core papers did reveal a public-artifact consistency gap for:

- **Virtual Mirrors: Non-Line-of-Sight Imaging Beyond the Third Bounce** — Diego Royo, Talha Sultan, Adolfo Muñoz, Khadijeh Masumnia-Bisheh, Eric Brandt, Diego Gutierrez, Andreas Velten, and Julio Marco, ACM Transactions on Graphics 42(4), SIGGRAPH 2023, DOI `10.1145/3592429`.

The paper is directly relevant rather than a passing NLOS citation. It develops the phasor-field / computational-wave line of work beyond the usual third-bounce assumption. In the computational wave domain, planar diffuse surfaces can act as “virtual mirrors”; propagating captured transients to these surfaces creates secondary virtual apertures that recover limited-visibility geometry and objects hidden behind a second corner, without requiring physical specular reflectors.

The tracing pass confirmed that the paper explicitly builds on the core active-NLOS trajectory represented by Velten et al. 2012, O'Toole et al. 2018, Lindell et al. 2019, and Liu et al.'s phasor-field / virtual-wave papers. Its related-work discussion also situates the method against passive computational periscopy and other multi-bounce NLOS approaches.

## Repository gap

Before this update:

- `article/2active.tex` already contained a short higher-order-bounce paragraph and cited `royoVirtualMirrors2023`;
- the paragraph inaccurately described the method as relying on specular hidden surfaces rather than computationally specular diffuse surfaces;
- `egbib_merged_20260711.bib` did not contain `royoVirtualMirrors2023`, leaving a source-level citation inconsistency;
- `README.md` and `index.html` did not expose the paper in the latest additions, paper explorer, or historical timeline;
- the existing `bare_jrnl.pdf` therefore could not be considered mutually consistent with the survey source and bibliography.

## Synchronization plan

The marker-based synchronizer associated with this note performs the following idempotent changes:

1. Add the final ACM TOG / SIGGRAPH 2023 record and a concise contribution summary to `README.md`.
2. Add a searchable homepage paper object, update the tracked-entry count from 87 to 88, and extend the 2023 timeline with higher-order / two-corner NLOS imaging.
3. Correct the higher-order-bounce paragraph in `article/2active.tex` to explain computational virtual mirrors, secondary virtual apertures, and two-corner recovery accurately.
4. Merge `egbib_20260712_virtual_mirrors_updates.bib` into the duplicate-free bibliography and verify that `royoVirtualMirrors2023` appears exactly once with the final DOI and venue.
5. Clean-build `bare_jrnl.pdf`, reject undefined citations and duplicate BibTeX entries, and validate the rendered PDF with `pdfinfo` and `pdftotext`.

The synchronizer aborts rather than overwriting public-facing files when an expected marker is absent or ambiguous.

**Build result:** pending the automated source synchronization, clean LaTeX/BibTeX rebuild, and PDF validation triggered by this update.
