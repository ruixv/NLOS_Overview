# 2026-10-05 update: 3D-GTR final SIGGRAPH 2026 venue

## Verified paper

Yi Wang, Ziyu Zhan, Yuran Wang, Hao Wang, Qiang Liu, Zuoqiang Shi, Lingyun Qiu, and Xing Fu, **“Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering,”** SIGGRAPH Conference Papers 2026, paper 85, pp. 85:1–85:11. DOI: 10.1145/3799902.3811137. arXiv:2606.21270.

The authors’ project page, DBLP, and institutional publication record all identify the final venue as SIGGRAPH 2026. Do not label this work as arXiv-only in canonical artifacts.

## Why it belongs

3D-GTR removes the planar, dense relay-wall assumption common in ToF NLOS imaging. It recovers relay geometry from LOS ToF measurements, represents the hidden scene with 3D Gaussian primitives, and optimizes those primitives through differentiable transient rendering. It supports confocal and non-confocal measurements and demonstrates reconstruction with spatially limited, sparse, and non-planar relay surfaces.

Recommended trajectory placement: planar/dense relay assumptions → sparse/limited measurements → neural/differentiable transient representations → arbitrary relay-surface geometry via 3D Gaussian Transient Rendering.

## Canonical integration required

1. **README.md** — add/update the paper in the 2026 active/transient NLOS timeline and learned/differentiable reconstruction category. Venue must be **SIGGRAPH 2026**, not arXiv.
2. **index.html / Paper Explorer / latest additions / timeline** — expose the same final venue, DOI, project/arXiv links, and concise contribution summary.
3. **Survey source (`bare_jrnl.tex` and/or modular article source)** — integrate semantically in the active ToF section discussing practical relay geometry, sparse/limited acquisition, neural fields/differentiable rendering, and arbitrary relay surfaces. Suggested literature-review point: recent differentiable transient representations move beyond planar-wall assumptions; 3D-GTR combines LOS-derived relay geometry with Gaussian scene primitives and differentiable transient rendering to support irregular relay surfaces and both confocal/non-confocal capture.
4. **Canonical bibliography** — merge the verified BibTeX entry staged in `egbib_20261005_3dgtr_siggraph_gap.bib`; prefer DOI 10.1145/3799902.3811137 and final SIGGRAPH venue while retaining arXiv as an auxiliary source.
5. **PDF** — rebuild only after source and bibliography integration; verify the generated PDF contains the citation and final venue.
6. **Consistency check** — confirm README, website, survey source, bibliography, and PDF all use the same final venue and metadata.

## Safety note

This run did not overwrite large canonical files because a complete safe read-edit-build-validation buffer was not established. The staging BibTeX and this integration note preserve the verified change without risking truncation or data loss.
