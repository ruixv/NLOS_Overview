# Deep under-scanning NLOS citation-tracing update — 16 July 2026

## Candidate accepted for integration

**Deep Non-line-of-Sight Imaging from Under-scanning Measurements**  
Yue Li, Yueyi Zhang, Juntian Ye, Feihu Xu, and Zhiwei Xiong  
**Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Main Conference Track, pp. 59095–59106**  
Official proceedings: https://proceedings.neurips.cc/paper_files/paper/2023/hash/b91cc0a242e6518ee731f74e82b2eebd-Abstract-Conference.html

## Why this is a genuine missing NLOS work

The paper directly addresses active confocal transient NLOS reconstruction rather than citing NLOS only as background. It introduces an end-to-end transient recovery network (TRN) and a volume reconstruction network (VRN): TRN restores a spatially dense transient grid from under-scanned measurements, while VRN embeds the linear light-path transport model to reconstruct a hidden volume. The official abstract reports robustness down to an 8×8 scan grid and inference roughly 50 times faster than the existing iterative solution.

A recent milestone paper, *Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering* (SIGGRAPH 2026, DOI 10.1145/3799902.3811137), cites this NeurIPS work specifically in its discussion of sparse and arbitrary transient acquisition. This confirms that it belongs to the direct development chain from dense LCT / phasor-field acquisition toward learned sparse-measurement completion and physics-aware inversion.

Exact-title and proceedings-hash searches against the repository found no existing README, homepage, survey, or bibliography entry before this update.

## Integration locations

- `README.md`: add a NeurIPS 2023 latest-addition row and a 2023 milestone line after SSCR.
- `index.html`: add one searchable `latest learning active` paper object, raise the tracked-entry count from 101 to 102, and extend the 2023 timeline.
- `article/2active.tex`: add the paper to the active pulsed-laser/SPAD reconstruction table.
- `article/4datadriven.tex`: add a literature-review paragraph under physics-guided deep learning, before the neural-implicit-surface discussion.
- `egbib_20260716_deep_underscanning_updates.bib`: add the canonical NeurIPS entry without inventing a DOI.
- `egbib_merged_20260711.bib`: regenerate through the repository bibliography merger.
- `bare_jrnl.pdf`: clean-build after source synchronization and validate that the title, narrative, and citation appear in the generated survey.

The accompanying marker-based synchronizer and GitHub Actions workflow refuse ambiguous anchors, audit duplicate/missing BibTeX entries, check cross-file uniqueness, and commit the rebuilt PDF only after validation succeeds.
