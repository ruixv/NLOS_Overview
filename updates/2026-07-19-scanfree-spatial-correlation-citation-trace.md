# Scan-free and spatial-correlation NLOS citation trace — 19 July 2026

**STATUS: STAGED — verified metadata is committed, but guarded source integration and the PDF rebuild remain pending.**

This update records two directly relevant active transient NLOS papers that are missing from the current public README/homepage snapshot and should be integrated as a connected scan-free acquisition lineage. Large public files were not replaced blindly in this run.

## 1. Verified missing papers

### Real-time scan-free non-line-of-sight imaging

- **Authors:** Wenjun Zhang, Enlai Guo, Shuo Zhu, Chenyang Huang, Lijia Chen, Lingfeng Liu, Lianfa Bai, Edmund Y. Lam, Jing Han
- **Venue:** APL Photonics 9(12), 126101 (2024)
- **DOI:** `10.1063/5.0235687`
- **Publisher URL:** https://doi.org/10.1063/5.0235687
- **Canonical BibTeX key:** `zhangRealTimeScanFreeNLOS2024`
- **Contribution:** Introduces a scan-free boundary-migration pipeline using a SPAD array rather than relay-wall raster scanning. The system reports 151-fps transient acquisition and 19-fps end-to-end hidden-scene imaging, supports outdoor/daytime measurements, and includes a plug-and-play super-resolution module that reduces the required detector array from 32x32 to 8x8.
- **Relevance check:** This is direct active transient NLOS reconstruction, not detection-only sensing. It belongs beside scannerless SPAD-array work and the low-latency/real-time NLOS lineage.

### High-resolution and real-time non-line-of-sight imaging based on spatial correlation

- **Authors:** Wenjun Zhang, Shuo Zhu, Lijia Chen, Lianfa Bai, Edmund Y. Lam, Enlai Guo, Jing Han
- **Venue:** Optics and Lasers in Engineering 193, 109100 (2025)
- **DOI:** `10.1016/j.optlaseng.2025.109100`
- **Publisher URL:** https://doi.org/10.1016/j.optlaseng.2025.109100
- **Canonical BibTeX key:** `zhangSpatialCorrelationNLOS2025`
- **Contribution:** Develops SCBSF-NLOS, a scan-free non-confocal architecture with a three-dimensional blur-kernel/forward-evolution model and spatial-correlation resampling. It reports approximately 2-cm lateral resolution and 5-fps reconstruction of dynamic hidden scenes with a 16x16 detector.
- **Relevance check:** The paper directly reconstructs hidden three-dimensional scenes and explicitly situates itself after Velten-style transient NLOS, LCT, f-k migration, and phasor-field reconstruction. It is therefore a genuine forward-citation/modality-development candidate rather than a passing citation.

The verified BibTeX records are stored in `egbib_20260719_scanfree_spatial_correlation.bib`.

## 2. README.md insertions

Insert the following rows immediately after the `Latest Additions` table header, preserving the current newest-first/update-run formatting:

```markdown
| 2025 | [High-resolution and real-time non-line-of-sight imaging based on spatial correlation](https://doi.org/10.1016/j.optlaseng.2025.109100) — Zhang et al. | Optics and Lasers in Engineering 2025 | Develops SCBSF-NLOS, a scan-free non-confocal system with a 3D blur-kernel forward model and spatial-correlation resampling; reports about 2 cm lateral resolution and 5 fps dynamic hidden-scene reconstruction using a 16x16 detector. |
| 2024 | [Real-time scan-free non-line-of-sight imaging](https://doi.org/10.1063/5.0235687) — Zhang et al. | APL Photonics 2024 | Replaces relay-wall raster scanning with SPAD-array boundary migration, reaching 151 fps transient acquisition and 19 fps end-to-end NLOS imaging; a plug-and-play super-resolution module reduces the detector requirement from 32x32 to 8x8. |
```

Add the following historical-development entries to the milestone timeline:

- Under **2024**, after the existing real-time/dynamic NLOS milestones:

```text
   │     Zhang et al.: real-time scan-free NLOS — SPAD-array boundary migration reaches 151-fps acquisition and 19-fps end-to-end reconstruction without relay-wall raster scanning [APL Photonics]
```

- Under **2025**, after the under-scanning/sampling milestones:

```text
   │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D blur-kernel model and correlation resampling recover 2-cm detail at 5 fps from a 16x16 detector [Optics and Lasers in Engineering]
```

Add a dated audit line before the existing 19 July phasor/polarization audit:

```text
   |     19 July 2026 scan-free citation trace: SPAD-array boundary migration and spatial-correlation super-resolution added as a connected real-time NLOS acquisition lineage
```

## 3. Website / index.html insertions

Add these paper-explorer objects to the `papers` array, using the repository's existing object formatting:

```javascript
{cat:"active transient hardware scan-free SPAD array real-time",title:"Real-time scan-free non-line-of-sight imaging",authors:"Zhang et al.",year:2024,venue:"APL Photonics 2024",url:"https://doi.org/10.1063/5.0235687",key:"Scan-free SPAD-array boundary migration reaches 151-fps transient acquisition and 19-fps end-to-end reconstruction; plug-and-play super-resolution reduces the required array from 32x32 to 8x8."},
{cat:"active transient scan-free non-confocal spatial correlation real-time",title:"High-resolution and real-time non-line-of-sight imaging based on spatial correlation",authors:"Zhang et al.",year:2025,venue:"Optics and Lasers in Engineering 2025",url:"https://doi.org/10.1016/j.optlaseng.2025.109100",key:"SCBSF-NLOS combines a 3D blur-kernel forward model with spatial-correlation resampling, reporting 2-cm lateral resolution and 5-fps dynamic reconstruction from a 16x16 detector."},
```

Update the tracked-paper statistic by **+2 after deduplication**, rather than hard-coding a stale total. Add matching 2024 and 2025 timeline text, and retain the page's current 19 July 2026 update date.

## 4. Survey-source integration

### `article/2active.tex`

1. In the active-system summary table, add `zhangRealTimeScanFreeNLOS2024,zhangSpatialCorrelationNLOS2025` to the row for **pulsed laser + SPAD array + ToF + 3D reconstruction**, currently containing the scannerless/low-latency SPAD-array citations.

2. Insert the following literature-review text directly after the paragraph ending with the discussion of SPAD arrays and scanning-free technologies (`jinScannerlessNonlineofsightThree2020`, `nam_real-time_2020`, and `pei_dynamic_2021`):

```latex
\vspace{0.8mm}
\noindent \textbf{Scan-free transient acquisition.}
Zhang~\etal~eliminated relay-wall raster scanning by combining a SPAD array with a boundary-migration reconstruction pipeline~\cite{zhangRealTimeScanFreeNLOS2024}. The reported prototype acquires transient measurements at 151 frames per second and produces end-to-end hidden-scene reconstructions at 19 frames per second, while a plug-and-play super-resolution module reduces the detector requirement from a $32\times32$ array to $8\times8$. This work complements sparse-scan acceleration: instead of selecting fewer wall positions, it changes the acquisition architecture so the relay aperture is captured in parallel.

\vspace{0.8mm}
\noindent \textbf{Spatial-correlation super-resolution for scan-free NLOS.}
The subsequent SCBSF-NLOS system models scan-free non-confocal measurements with a three-dimensional blur kernel and a forward-evolution operator, then uses spatial-correlation resampling to recover high-frequency hidden-scene structure~\cite{zhangSpatialCorrelationNLOS2025}. Experiments report approximately 2\,cm lateral resolution and 5-fps reconstruction of dynamic scenes with a $16\times16$ detector. Together, these two papers establish a progression from parallel transient capture to model-based spatial super-resolution, showing that real-time NLOS hardware and inversion should be co-designed rather than treated as separate bottlenecks.
```

3. Where the survey discusses low-latency NLOS and SPAD arrays, connect these papers to Nam et al. and scannerless SPAD-array imaging rather than appending them only in a miscellaneous list.

### `bare_jrnl.tex`

No standalone paper list should be appended. Preserve the master structure and include the papers through the semantically integrated `article/2active.tex` discussion. Update the coverage/audit comment only if the repository uses such comments for recent synchronization runs.

## 5. Bibliography merge

Merge the two entries from `egbib_20260719_scanfree_spatial_correlation.bib` into the bibliography source actually used by `bare_jrnl.tex`. Before merging, verify that neither DOI nor canonical key already exists. Preserve one canonical record per paper.

## 6. Build and consistency validation still required

The following work remains before this update can be described as fully integrated:

1. Apply the README, `index.html`, `article/2active.tex`, and bibliography insertions with guarded unique-anchor checks.
2. Confirm that previously staged ptychography, radar/THz, and ICCV final-venue corrections are either integrated or explicitly marked pending; the current public snapshot still lags some staged metadata files.
3. Run a clean LaTeX/BibTeX build of `bare_jrnl.tex`.
4. Check for undefined citations, duplicate BibTeX keys/DOIs, missing references, and overfull/critical LaTeX errors.
5. Render or inspect every page of the regenerated `bare_jrnl.pdf` and confirm that the two new paragraphs and bibliography records are present.
6. Commit the regenerated `bare_jrnl.pdf` only after the source and PDF checks pass.
7. Recheck that README, website, survey source, bibliography, and PDF each contain both papers exactly once.

**`bare_jrnl.pdf` was not regenerated in this run, and this note must not be interpreted as a claim that the public artifacts are already synchronized.**
