# Integration gap: Cascaded Non-Line-of-Sight Imaging

Verified on 2026-09-26.

## Paper
Diego Royo, María Peña, Forrest B. Peterson, Andreas Velten, Julio Marco, Diego Gutierrez, **“Cascaded Non-Line-of-Sight Imaging,”** arXiv:2609.16017 (2026). Submitted 3 Sep 2026. No final conference/journal venue was verified in this run, so the venue should remain arXiv.

Link: https://arxiv.org/abs/2609.16017

## Why it belongs
This is a direct extension of the active transient / phasor-field lineage. Instead of restricting reconstruction to conventional three-bounce paths, it computes a virtual impulse response at a hidden relay wall and cascades a second virtual NLOS system. This exposes useful fourth- and fifth-bounce transport, enabling difficult target orientations, two-corner imaging, hidden-scene viewpoints, and analysis of wave-based propagation through rough hidden walls.

## Repository check
A repository-wide exact-title search returned no match on the default branch on 2026-09-26. The paper is therefore missing from the current indexed repository state.

## Required canonical integration
- README.md: add to Latest Additions and the 2026 milestone timeline; categorize under Active NLOS / higher-order transient transport / multi-corner imaging.
- index.html: add to latest additions, paper explorer, and timeline with tags such as Active, ToF, transient, higher-order transport, multi-corner, phasor-field.
- bare_jrnl.tex: integrate semantically after discussion of phasor-field / virtual-wave formulations and alongside higher-order transient transport. Emphasize the trajectory from three-bounce hidden geometry to virtual hidden-wall impulse responses and cascaded fourth/fifth-bounce imaging.
- bibliography: merge the staged entry in `egbib_20260926_cascaded_nlos.bib` into the canonical bibliography, preserving the repository citation-key convention.
- bare_jrnl.pdf: rebuild only after the canonical TeX/bibliography edits are complete and compile successfully.

Do not claim canonical synchronization until README.md, index.html, bare_jrnl.tex, bibliography, and regenerated bare_jrnl.pdf have all been verified.
