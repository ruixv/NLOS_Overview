# NLOS frontier follow-up — staged update (25 July 2026)

## Search and citation-tracing result

No direct NLOS imaging publication with independently verified publication metadata later than **22 July 2026** was found. The latest date-verified direct paper remains:

- Talha Sultan et al., **Iterating the transient light transport matrix for non-line-of-sight imaging**, *Nature Communications* (published 22 July 2026), DOI `10.1038/s41467-026-75177-4`.

The current keyword, project/lab-page, final-venue, and forward-citation pass identified the following genuine repository gaps or corrections.

## Papers to integrate

### 1. Dual-model guided active NLOS imaging with under-scanning measurements

Zhihang Yan, Hao Liu, Mengge Liu, Sai Zhang, Huimin Wang, Shaohui Jin, Mingliang Xu  
*The Visual Computer* 42(4), article 174 (2026)  
DOI: `10.1007/s00371-026-04381-6`

A spatio-temporal recovery module transforms sparse under-scanned transients into a sufficient-scanning representation. Dual LCT and f-k reconstruction branches then recover complementary global structure and fine texture, followed by adaptive feature fusion. This is a direct citation-traced continuation of LCT, f-k migration, LEAP, and deep under-scanning NLOS.

### 2. Non-line-of-sight imaging based on adaptive neural grid resampling

Mengfan Wang, Jiatong Yu, Xingfen Tang, Yongkang Zhou, Youpan Zhu, Yang Yang, Huaisheng Pang  
SSRN preprint, posted 29 June 2026  
DOI: `10.2139/ssrn.7022018`

The method adds a lightweight Grid Offset Network to f-k migration. It predicts local frequency-domain resampling offsets and adapts the Stolt mapping under trigger-delay, propagation-speed, and low-density-sampling perturbations. No final journal or conference venue was verified, so it must remain labeled as an SSRN preprint.

### 3. Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform

Yijun Wei, Jianyu Wang, Leping Xiao, Zuoqiang Shi, Xing Fu, Lingyun Qiu  
**Optica, accepted**; arXiv:2508.02003

The authors' laboratory publication page now labels the paper as accepted by *Optica*. Volume, pages, and DOI are not yet public, so the repository should use the accepted venue while retaining arXiv as the link/source. The method represents common hidden surfaces and aggregated transient measurements as two-dimensional functions and derives a Quasi-Fresnel inversion with substantially lower runtime and memory complexity.

### 4. SCISA-Net

Jihao Dai, Hongshuai Qin, Guowen Li, Jin Liu, Xiaoshuai Zhang, Huiyu Qi, Zhiwen Zheng, Xingru Huang  
*Photonics* 13(6), 575 (2026)  
DOI: `10.3390/photonics13060575`

SCISA-Net uses scene-constrained regularized inversion and multi-stage Haar-subband attention for 31-way category inference from calibrated wall-mediated observations. It should be explicitly labeled as NLOS semantic sensing/recognition, not full hidden-image, depth, or geometry reconstruction.

## Cross-artifact gaps and corrections

- **Neural Illumination Fields** is already present in `README.md`, `article/5newscenes.tex`, and the bibliography, but still needs website explorer/timeline synchronization.
- **3D Gaussian Transient Rendering** is already listed in `README.md`, but its public link still points to arXiv. Replace it with the final SIGGRAPH 2026 DOI `10.1145/3799902.3811137`, and ensure the website, survey prose, and consolidated bibliography use the final ACM venue.

## Required insertion locations

1. `README.md`
   - Add rows for Dual-model guided NLOS, adaptive neural grid resampling, Quasi-Fresnel, and SCISA-Net immediately after the Latest Additions table header.
   - Replace the 3D-GTR arXiv URL with its ACM DOI.
   - Add a 2026 milestone describing physics-aware sparse acquisition, adaptive Stolt calibration, dimension-reduced inversion, arbitrary relay geometry, and semantic inference.

2. `index.html`
   - Add searchable records for NIF, SCISA-Net, Dual-model guided NLOS, adaptive neural grid resampling, 3D-GTR, and Quasi-Fresnel.
   - Extend the 2026 timeline with the corresponding development trajectory.
   - Recalculate the tracked-entry count from the actual number of inserted records rather than hard-coding it.

3. `article/2active.tex`
   - Before **Challenges and Prospects**, add a paragraph titled **Learned Stolt calibration and dimension-reduced inversion** covering adaptive neural grid resampling and Quasi-Fresnel.

4. `article/4datadriven.tex`
   - Immediately after the recognition/action/clustering trajectory, add **Calibrated wall-mediated semantic inference** for SCISA-Net.
   - Immediately after the **Network combined with physical models** subsection heading, add **Dual-model guidance for under-scanned transients**.

5. `article/5newscenes.tex`
   - Preserve the existing NIF paragraph.
   - Before the scattering-media subsection, add **Arbitrary Relay Surfaces with Gaussian Transient Rendering** and cite the final SIGGRAPH record.

6. `egbib_merged_20260711.bib`
   - Add DOI-verified final records for Dual-model guided NLOS, SCISA-Net, and 3D-GTR.
   - Add the SSRN record for adaptive neural grid resampling.
   - Add Quasi-Fresnel as an accepted *Optica* article, retaining arXiv metadata until final volume/pages/DOI become available.
   - Preserve existing stable citation keys when a DOI record already exists.

7. `bare_jrnl.tex` / `bare_jrnl.pdf`
   - Add a trace marker, run `pdflatex → bibtex → pdflatex ×2`, reject undefined/duplicate citations, verify PDF text and page rendering, and commit the regenerated binary only after all cross-artifact checks pass.

## Guarded integration assets

- `scripts/sync_nlos_20260725_frontier_followup.py`
- `.github/workflows/sync_nlos_frontier_followup_20260725.yml`
- `updates/trigger-frontier-followup-20260725.txt`

At the time this note was committed, no subsequent source-integration/PDF-rebuild commit was visible. Therefore the public artifacts and `bare_jrnl.pdf` are **not claimed as updated** by this staged note.
