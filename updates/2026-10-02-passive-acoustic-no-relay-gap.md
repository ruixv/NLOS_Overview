# Integration gap: passive acoustic NLOS localization without a relay surface

## Verified paper

Tal I. Sommer and Ori Katz, “Passive acoustic non-line-of-sight localization without a relay surface,” *Physical Review Applied*, vol. 25, no. 2, 024064, 2026. DOI: 10.1103/p97k-sf71. Published 20 February 2026.

Publisher: https://journals.aps.org/prapplied/abstract/10.1103/p97k-sf71
ArXiv preprint: https://arxiv.org/abs/2506.08471

## Why it belongs

This is a genuine NLOS sensing/localization paper and a useful modality-expansion milestone. Unlike relay-surface acoustic NLOS methods, it exploits obstacle-edge diffraction to localize a hidden acoustic point source in 3D without requiring a visible relay wall. It treats doorway and convex-corner configurations: doorway edges act as virtual detector arrays, while a single knife edge is localized through its frequency-dependent diffraction signature. The paper explicitly cites the active NLOS milestones Velten 2012, O’Toole/LCT 2018, Lindell f-k 2019, and Liu phasor-field reconstruction, as well as prior passive acoustic NLOS localization, making it a strong citation-tracing hit rather than a keyword-only candidate.

## Recommended integration

- README / timeline: 2026 → Acoustic / multimodal NLOS. Suggested summary: “Passive acoustic NLOS localization without a relay surface — uses knife-edge diffraction at doorways/corners for 3D hidden-source localization, extending acoustic NLOS beyond reflected relay-wall signals.”
- Website / paper explorer: modality = Acoustic; task = localization / sensing; passive = yes; key tag = edge diffraction / no relay surface.
- bare_jrnl.tex: place after discussion of passive acoustic localization around corners. Suggested trajectory sentence: “Recent acoustic NLOS work has begun to remove the relay-surface assumption altogether: Sommer and Katz exploit knife-edge diffraction at doorway and corner boundaries to localize hidden sound sources in three dimensions without relying on reflected signals from a visible wall.”
- Bibliography: merge the verified entry staged in `egbib_20261002_passive_acoustic_no_relay_gap.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- Rebuild `bare_jrnl.pdf` after canonical source integration and verify README/index/survey/bibliography/PDF consistency.

## Current limitation

This run did not overwrite large canonical files without a complete safe read-edit-build-validation cycle. The staged BibTeX and this note preserve the verified metadata and precise insertion plan for the next safe integration pass.
