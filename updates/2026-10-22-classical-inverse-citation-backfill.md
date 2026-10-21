# 2026-10-22 — Classical inverse NLOS forward-citation backfill

## Verified missing or incompletely surfaced works

The publisher, PubMed and OpenAlex metadata were checked for five relevant papers. None of the five DOI records was present in the public README or Paper Explorer before this run. The first paper already had a survey citation/BibTeX key but lacked DOI metadata and was missing from the public-facing timelines.

1. Chenfei Jin, Jiaheng Xie, Siqi Zhang, ZiJing Zhang and Yuan Zhao, "Reconstruction of multiple non-line-of-sight objects using back projection based on ellipsoid mode decomposition," *Optics Express* **26**(16), 20089–20101 (2018). DOI: https://doi.org/10.1364/OE.26.020089. Separates multi-object ellipsoid modes to reduce cross-object aliasing. Existing survey key `jinReconstructionMultipleNonlineofsight2018` was retained and its BibTeX DOI/URL completed.
2. The same five authors, "Richardson–Lucy deconvolution of time histograms for high-resolution non-line-of-sight imaging based on a back-projection method," *Optics Letters* **43**(23), 5885–5888 (2018). DOI: https://doi.org/10.1364/OL.43.005885. Uses line-of-sight backscatter priors to deconvolve measured transients before 3D backprojection.
3. Zhengyang Shi, Xia Wang, Yang Li, Zhibin Sun and Wenxi Zhang, "Edge re-projection method for high-quality edge reconstruction in non-line-of-sight imaging," *Applied Optics* **59**(6), 1793–1800 (2020). DOI: https://doi.org/10.1364/AO.376403. Reweights measurement contributions based on estimated object-edge voxels.
4. Xiaohua Feng and Liang Gao, "Improving non-line-of-sight image reconstruction with weighting factors," *Optics Letters* **45**(14), 3921–3924 (2020). DOI: https://doi.org/10.1364/OL.394742. Combines aperture apodization and spatial-coherence weighting for noise-robust FBP. Direct references include Velten 2012, LCT 2018, phasor-field 2019 and Computational Periscopy 2019.
5. Xiaojie Chen, Mengyue Li, Tiantian Chen and Shuyue Zhan, "Long-Range Non-Line-of-Sight Imaging Based on Projected Images from Multiple Light Fields," *Photonics* **10**(1), 25 (2023 issue; first online 26 December 2022). DOI: https://doi.org/10.3390/photonics10010025. Learns hidden-scene recovery from multi-light-field projections; experiments include sensor-to-relay distance above 50 m. Its reference list includes LCT and earlier backprojection work.

## Citation-tracing relevance

Jin 2018 ellipsoid-mode decomposition cites earlier ultrafast optical NLOS; its 2018 Richardson–Lucy successor cites Velten 2012. Feng and Gao 2020 directly cite Velten, LCT, phasor-field and Computational Periscopy. Chen et al. 2023 cite both Jin papers, LCT and other backprojection milestones. These are genuine active NLOS imaging papers, not incidental citations. The five entries bridge classic backprojection, multi-target aliasing, histogram deconvolution, edge/noise weighting, and long-range learned light-field acquisition.

## Integration and validation

- README: five Latest Additions rows and three historical milestone timeline paragraphs.
- index.html: one historical inverse-method and long-range learning overview paragraph.
- data/papers-source.html: five Paper Explorer records and 2018/2020/2023 timeline nodes.
- article/2active.tex: four classic inverse-method citations in the inverse-reconstruction discussion; 2023 long-range learned acquisition in the long-range methods discussion.
- egbib_merged_20260711.bib: four new DOI-verified BibTeX entries; DOI/URL added to the existing 2018 ellipsoid-mode entry.
- bare_jrnl.tex: unchanged; its existing input of article/2active.tex and bibliography reference already incorporate all five papers.

## PDF status

**bare_jrnl.pdf is not rebuilt in this run.** The previous observed PDF Git blob SHA was `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`. The container cannot reach GitHub to obtain a complete build checkout. Build with pdflatex → bibtex → pdflatex → pdflatex, inspect unresolved citations and missing resources, then upload the changed PDF binary. Do not report the PDF as synchronized until the new binary and build log are verified.
