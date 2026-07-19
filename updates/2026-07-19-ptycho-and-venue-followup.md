# 19 July 2026 ptychographic-correlography and final-venue follow-up

STATUS: STAGED — guarded radar/THz/ptychography source synchronization and PDF rebuild are pending. The passive-acoustic public venue correction is complete.

## Newly verified missing paper

### Ptychography-enhanced correlography for non-line-of-sight imaging

- Authors: Lingfeng Liu, Shuo Zhu, Taotao Qin, Lianfa Bai, Yingjie Shi, Enlai Guo, Jing Han
- Final venue: *Advanced Photonics Nexus*, vol. 5, no. 2, article 026001, 2026
- DOI: `10.1117/1.APN.5.2.026001`
- Publication history: accepted 23 December 2025; published online 22 January 2026; assigned to the March/April 2026 issue.
- Relevance: direct steady-state NLOS reconstruction, not a passing citation. The method combines polarization-differential speckle correlography with overlapping ptychographic relay-wall scanning, jointly improving Fourier-amplitude sampling and phase retrieval for structurally complex hidden targets. Geometry-based scan-position correction addresses practical 3D setup errors.

## Final-venue corrections

### Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors

The repository currently exposes the 2024 arXiv version in README/homepage metadata. The verified final publication is:

- Shida Sun, Yue Li, Yueyi Zhang, Zhiwei Xiong
- IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 25040–25049
- Official CVF open-access record: `https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Generalizable_Non-Line-of-Sight_Imaging_with_Learnable_Physical_Priors_ICCV_2025_paper.html`

The existing citation key `sunGeneralizable2025` is retained; the dated bibliography supplement overrides its preliminary metadata with the final ICCV record.

### Passive acoustic non-line-of-sight localization without a relay surface

The survey section and bibliography already used the final publication, while README/homepage still exposed the 2025 arXiv label at the beginning of this pass. The guarded correction has now synchronized both public records to:

- Tal I. Sommer and Ori Katz
- *Physical Review Applied* 25(2), article 024064, published 20 February 2026
- DOI: `10.1103/p97k-sf71`

This correction required no survey-text or PDF rebuild because the LaTeX source already cited the final journal record.

## Pending radar/THz source integration carried forward

The preceding citation-tracing run verified two direct NLOS 3D reconstruction papers whose metadata files and guarded synchronizer are already present but whose public/source/PDF integration had not reached `master` at the start of this run:

1. *RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar*, Journal of Radars 15(1), 42–63, 2026, DOI `10.12000/JR25132`.
2. *Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging*, Photonics 13(5), 440, 2026, DOI `10.3390/photonics13050440`.

The revised synchronizer integrates these records together with the ptychographic-correlography paper and ICCV venue correction, so all pending changes are validated in one source/PDF pass.

## Intended cross-artifact changes

- `README.md`: add the three missing radar/THz/coherent-optical records; correct Learnable Physical Priors to ICCV 2025; extend the 2025/2026 timeline and audit log. The passive-acoustic final venue is already corrected.
- `index.html`: add three searchable paper objects, correct the ICCV venue/link, update the 2026 development timeline, and recompute the tracked-entry count. The passive-acoustic final venue is already corrected.
- `article/5newscenes.tex`: add semantically placed operator-learned mmWave, sub-THz, and ptychography-enhanced correlography review paragraphs.
- `article/4datadriven.tex`: identify Learnable Physical Priors as the final ICCV 2025 work while retaining its existing citation key and technical discussion.
- `bare_jrnl.tex`: advance coverage through 19 July 2026 and add a source-integration marker.
- `egbib_merged_20260711.bib`: regenerate from canonical dated supplements, including the final ICCV override.
- `bare_jrnl.pdf`: clean-build, reject undefined/repeated citations, render-check all pages, verify new review phrases, and commit only after successful validation.

No direct NLOS imaging publication later than *Non-line-of-sight imaging via physics-informed cascade learning*, published 15 July 2026, was verified during this pass.
