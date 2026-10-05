# Geometry-Constrained NLOS imaging gap — 2026-10-06

## Verified missing paper

Xueying Liu, Lianfang Wang, Jun Liu, Yong Wang, and Yuping Duan, “Geometry-Constrained Non-Line-of-Sight Imaging,” *IEEE Transactions on Visualization and Computer Graphics*, vol. 32, no. 7, pp. 6524–6536, 2026. DOI: 10.1109/TVCG.2026.3684832.

The work first appeared as the 2025 preprint “Geometric Constrained Non-Line-of-Sight Imaging” (arXiv:2503.17992), but the repository should use the verified final TVCG 2026 venue and final title.

## Why it belongs

This is an active/transient NLOS geometry-reconstruction paper rather than a peripheral NLOS sensing citation. It jointly reconstructs hidden-scene albedo and surface geometry/normals, using a shape-operator regularizer to control variation of the normal field. The method targets a limitation of intensity/occupancy-only reconstructions: surface normals provide additional geometric and lighting information. The paper reports synthetic and experimental validation; on transient data captured within 15 s, the surface-normal-regularized model gives more accurate surfaces and is reported as roughly 30× faster than the compared surface-reconstruction approach.

## Recommended development-line placement

Place in the active ToF / geometry-aware reconstruction line, near work on albedo-normal recovery, surface reconstruction, and physics/geometry priors. A useful trajectory is:

**volumetric/albedo reconstruction → explicit surface/normal recovery → geometry-regularized joint albedo–surface reconstruction → neural/learned geometry priors.**

Suggested concise survey sentence:

> Beyond recovering hidden occupancy or albedo, Liu et al. regularize the hidden normal field through the surface shape operator, enabling efficient joint albedo–surface reconstruction and highlighting explicit differential geometry as a complementary prior for transient NLOS inversion.

## Canonical integration checklist

- README.md: add under 2026 active/transient NLOS, categorized as geometry-aware/model-based reconstruction.
- Website/index.html Paper Explorer: add final TVCG metadata, DOI, and a short geometry-aware reconstruction summary.
- Timeline/latest additions: connect it to explicit surface/normal recovery rather than learned reconstruction.
- Survey source: integrate semantically in the active-ToF reconstruction discussion near surface/albedo/normal estimation and regularization-based inverse methods; do not append as an isolated list item.
- Canonical bibliography: merge the staged entry in `egbib_20261006_geometry_constrained_gap.bib`; avoid retaining a duplicate arXiv-only entry under the earlier title “Geometric Constrained Non-Line-of-Sight Imaging.”
- Rebuild and verify bare_jrnl.pdf after canonical source integration.

## Verification

Repository default-branch searches for the exact final title and DOI returned no match before staging. Metadata was cross-checked against PubMed, OpenAlex, DBLP, and the final IEEE TVCG record metadata surfaced by those scholarly indexes. The final bibliographic record is volume 32, issue 7, pages 6524–6536, DOI 10.1109/TVCG.2026.3684832.

Large canonical files were not overwritten from partial buffers in this run. This note and the verified BibTeX staging file preserve a safe, precise integration path for the next full read-edit-build-validation pass.
