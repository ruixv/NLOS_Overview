# 15 July 2026 citation-tracing update: surface optimization beyond volumetric albedo

## Search outcome

A fresh pass over recent arXiv results, conference/journal pages, project pages, and modality-expansion searches did not identify a direct NLOS-imaging paper newer than the 5 July 2026 NIR raster-scanning preprint already covered by the repository.

The high-priority citation-tracing pass did reveal a public-facing consistency gap in the inverse-rendering lineage. The survey source already cited the CVPR 2019 paper below in its generic inverse-rendering discussion, and recent differentiable/Gaussian transient-rendering literature identifies it as an early explicit surface-reconstruction milestone, but the paper had no dedicated README entry, homepage explorer object, timeline explanation, or focused survey paragraph.

## Integrated paper

**Beyond Volumetric Albedo -- A Surface Optimization Framework for Non-Line-of-Sight Imaging**  
Chia-Yin Tsai, Aswin C. Sankaranarayanan, Ioannis Gkioulekas  
CVPR 2019, pp. 1545--1555  
Official CVF page: https://openaccess.thecvf.com/content_CVPR_2019/html/Tsai_Beyond_Volumetric_Albedo_--_A_Surface_Optimization_Framework_for_Non-Line-Of-Sight_CVPR_2019_paper.html

The method directly optimizes hidden surface geometry and reflectance instead of reconstructing only a volumetric albedo field. Its radiometric renderer computes derivatives with respect to NLOS geometry and reflectance, and combines them with stochastic optimization and geometry processing to recover substantially finer surfaces than earlier volumetric methods.

## Repository synchronization

The marker-based synchronizer performs the following changes only when the expected anchors are present:

- inserts one CVPR 2019 row in `README.md` and one 2019 milestone;
- adds one searchable/latest object to `index.html`, expands the 2019 development timeline, and changes the tracked-entry count from 100 to 101;
- inserts a dedicated literature-review paragraph in the inverse-rendering subsection of `article/2active.tex` before the Iseringhausen--Hullin analysis-by-synthesis discussion;
- keeps the established citation key `tsaiVolumetricAlbedoSurface2019` and supplies canonical CVF metadata in `egbib_20260715_tsai_surface_updates.bib`;
- regenerates the duplicate-free consolidated bibliography and clean-builds `bare_jrnl.pdf` in CI.

The workflow rejects duplicate public entries, missing/undefined citations, repeated BibTeX records, an empty PDF, a PDF without extractable text, or an unexpected homepage count. It then commits the synchronized source files and regenerated PDF to the update branch.
