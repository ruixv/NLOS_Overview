# 24 July 2026 ptychography-correlography citation trace

## Verified cross-artifact gap

**Ptychography-enhanced correlography for non-line-of-sight imaging**  
Lingfeng Liu, Shuo Zhu, Taotao Qin, Lianfa Bai, Yingjie Shi, Enlai Guo, and Jing Han  
*Advanced Photonics Nexus* 5(2), 026001 (2026)  
DOI: `10.1117/1.APN.5.2.026001`  
Published online: 22 January 2026

This paper was exposed by citation tracing around steady-state NLOS correlography, computational periscopy, and polarization-speckle imaging. The consolidated bibliography already contained a metadata record under the stable key `liuPtychographyCorrelographyNLOS2026`, but repository-wide comparison confirmed that the paper was absent from `README.md`, the website paper explorer and timeline, and the LaTeX survey discussion. It is therefore a genuine cross-artifact survey gap rather than a completely absent bibliography record.

PEC-NLOS is direct active steady-state NLOS reconstruction. It scans overlapping indirect speckle probes on the relay wall, records partial Fourier-amplitude information with an industrial polarization-sensitive camera, and uses ptychographic phase retrieval to jointly refine the hidden object and illumination probe. A geometry-derived three-dimensional data-correction stage uses non-invasive positional priors to compensate scan-position and probe distortion. The overlapping measurements improve Fourier coverage and conditioning, extending correlography from simple sparse targets to high-spatial-frequency and high-entropy hidden scenes.

## Cross-artifact integration

The guarded synchronizer and build workflow will:

1. Add the final-venue record to `README.md` Latest Additions and the 2026 milestone timeline while preserving the 22 July 2026 TLTM paper as the newest publication.
2. Add a searchable website paper object, append the steady-state ptychography milestone, and increment the tracked-entry count from 192 to 193 only when the DOI is absent.
3. Add a dedicated active-system table row and a semantically placed `Ptychography-enhanced correlography` review paragraph to `article/2active.tex`, immediately after the polarization-differential correlography discussion.
4. Normalize the existing stable-key BibTeX record in `egbib_merged_20260711.bib` without introducing a duplicate key or DOI.
5. Add a traceable citation-audit marker to `bare_jrnl.tex` without altering the already-current 24 July coverage date.
6. Clean-build `bare_jrnl.pdf` and validate DOI coverage, bibliography uniqueness, extracted PDF text, page validity, and unresolved citations.

**Status after automation:** README, website, active-survey prose and table, consolidated bibliography, and rebuilt PDF are mutually synchronized and validated.
