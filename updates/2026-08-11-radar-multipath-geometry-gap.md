# 11 August 2026 — citation-tracing gap: unknown relay geometry, multipath localization and radar NLOS tracking

## Scope of this run

A fresh keyword/project-page/journal search was combined with a forward-citation pass from the repository's core NLOS lineage (Velten 2012, LCT, f-k migration, phasor fields, computational periscopy, learned transient models, HoloRadar and the modality-expansion papers). The active-optical/passive/learned citation descendants surfaced by this pass were already represented in the current README/site/survey (for example learned LCT, stereo NLOS, geometry-constrained reconstruction, transient-video interpolation, thermal rough-wall NLOS and current sparse/real-time methods).

The meaningful remaining gap is a coherent **radar/RF NLOS lineage in which relay geometry is not assumed known**. Six final-venue papers were verified and are absent by title from the current public artifacts. Together they bridge reflector estimation, unknown-corridor/layout recovery, robust target positioning, distributed NLOS tracking and full 3-D environmental perception plus moving-target reconstruction.

## Verified missing papers

| Year | Paper | Final venue | DOI | Recommended role in survey |
|---|---|---|---|---|
| 2026 | **Multipath Exploitation-Based 3-D Environmental Perception and NLOS Moving Target Reconstruction for mmWave MIMO Imaging Radar** — Zhihao Zhu, Zihan Xu, Jiahui Chen, Shisheng Guo, Guolong Cui, Xiaobo Yang | IEEE Transactions on Aerospace and Electronic Systems 62, 3569–3587 | `10.1109/TAES.2025.3647422` | Highest-priority addition. Jointly treats the environment and hidden moving target: weak reflector echoes support 3-D environmental perception, reflector parameters are transferred into path-oriented NLOS reconstruction/localization, and measured experiments validate the pipeline. |
| 2025 | **NLOS Building Layout and Target Estimation in an L-Shaped Corner with Complex Geometries** — Shucheng Xue, Jiahui Chen, Shisheng Guo, Mikko Valkama, Zhihao Zhu, Zihan Xu, Peilun Wu, Guolong Cui | IEEE Transactions on Instrumentation and Measurement 74 | `10.1109/TIM.2024.3522427` | Important unknown-layout precursor. Tracks multipath ToAs, identifies diffraction/first-/second-order reflection paths, uses the first two for target localization and second-order paths for partial wall-shape reconstruction with a portable SISO radar. |
| 2025 | **A Two-Stage NLOS Target Positioning Method Based on 0-1 Non-Coherent Binary Accumulation** — Peilun Wu, Shisheng Guo, Jiahui Chen, Haixu Chen, Guolong Cui, Lingjiang Kong, Xiaobo Yang | IEEE Transactions on Vehicular Technology 74(6), 8866–8878 | `10.1109/TVT.2025.3542117` | Robust target-positioning branch. Builds a round-trip multipath model, derives CFAR-based binary thresholds, forms 0-1 non-coherent accumulation images, and uses a two-stage estimator to reduce false alarms and missed detections. |
| 2025 | **A Reflective Surface Estimation Method Based on Multipath Utilization** — Haolan Luo, Shisheng Guo, Meiqiu Jiang, Jiahui Chen, Guolong Cui | IEEE Transactions on Instrumentation and Measurement 74, 1–11 | `10.1109/TIM.2025.3541688` | Enabling relay-geometry paper. Uses the tangency between a reflector and the multipath ellipse, multipath-dictionary matching and Kalman smoothing to estimate reflective surfaces rather than assuming them known. |
| 2025 | **NLOS Tracking with Distributed Radar Using Multipath-Assisted JPDA** — Hao Xu, Shisheng Guo, Yu Yao, Peilun Wu, Yufei Wei, Zihan Xu, Guolong Cui | IEEE IGARSS 2025, 8751–8755 | `10.1109/IGARSS55030.2025.11242772` | Dynamic extension. Incorporates multipath-assisted data association into distributed-radar JPDA for NLOS target tracking rather than treating multipath only as clutter. |
| 2025 | **Non-Line-of-Sight Target Localization in Unknown L-Shaped Corridor Based UWB MIMO Radar** — Chao Jia, Caiping Song, Lingyu Wang, Guolong Cui, Shisheng Guo, Jie Gu, Yong Jia | Journal of Systems Engineering and Electronics 36(3), 681–693 | `10.23919/JSEE.2025.000021` | Unknown-scene localization branch. Uses two backprojection views plus diffraction/reflection path-length matching to estimate both hidden target positions and corridor width, including experiments with missing propagation paths. |

### Primary/metadata verification used

- Tampere University publication record for Xue et al.: https://researchportal.tuni.fi/en/publications/nlos-building-layout-and-target-estimation-in-an-l-shaped-corner-/
- Official Journal of Systems Engineering and Electronics record for Jia et al.: https://www.jseepub.com/EN/10.23919/JSEE.2025.000021
- Official IGARSS 2025 accepted-paper/session records for Xu et al.: https://2025.ieeeigarss.org/papers/accepted_papers.php and https://www.2025.ieeeigarss.org/view_session.php?SessionID=1116
- DBLP final bibliographic record for Zhu et al. (IEEE TAES 62:3569–3587, 2026): https://dblp.org/rec/journals/taes/ZhuXCGCY26
- DBLP final bibliographic record for Wu et al. (IEEE TVT 74(6):8866–8878, 2025): https://dblp.org/rec/journals/tvt/WuGCCCKY25
- DOI metadata / indexed journal references for Luo et al.: DOI `10.1109/TIM.2025.3541688`, IEEE TIM 74, 1–11 (2025).

## Scope-screened but not proposed for the main NLOS list

**Joint Reconstruction of Building Layouts and Concealed Targets via Structural-Prior-Guided Compressive Sensing**, IEEE Internet of Things Journal 13(12), 26949–26962 (2026), DOI `10.1109/JIOT.2026.3678323`, was screened. Its public abstract frames the problem primarily as **through-the-wall radar imaging (TWRI)**. It is technically adjacent to the unknown-layout NLOS branch, but is not proposed for the main around-corner/NLOS list in this patch to avoid scope creep. It can be added later if the repository intentionally expands the RF taxonomy to include general TWRI.

## Exact public-artifact patch plan

### 1. `README.md`

**Insertion A — `## Latest Additions`:** place the following immediately after the table header, before the current RIS vital-sign entries. The 2026 TAES paper should be the highest-priority new item; the 2025 papers document the missing precursor lineage.

```markdown
| 2026 | [Multipath Exploitation-Based 3-D Environmental Perception and NLOS Moving Target Reconstruction for mmWave MIMO Imaging Radar](https://doi.org/10.1109/TAES.2025.3647422) — Zhu et al. | IEEE Transactions on Aerospace and Electronic Systems 62, 3569–3587 (2026) | Jointly estimates 3-D environmental/reflector structure and reconstructs NLOS moving targets from mmWave MIMO multipath, transferring estimated reflector parameters into path-oriented hidden-target localization and validating the pipeline experimentally. |
| 2025 | [NLOS Building Layout and Target Estimation in an L-Shaped Corner with Complex Geometries](https://doi.org/10.1109/TIM.2024.3522427) — Xue et al. | IEEE Transactions on Instrumentation and Measurement 74 (2025) | Removes the usual known-layout assumption: tracks multipath ToAs, separates diffraction and first-/second-order reflection paths, localizes the hidden target and reconstructs part of the L-shaped relay geometry with a portable SISO radar. |
| 2025 | [A Two-Stage NLOS Target Positioning Method Based on 0-1 Non-Coherent Binary Accumulation](https://doi.org/10.1109/TVT.2025.3542117) — Wu et al. | IEEE Transactions on Vehicular Technology 74(6), 8866–8878 (2025) | Uses CFAR-derived 0-1 non-coherent binary accumulation and a two-stage estimator to make multipath NLOS target positioning more robust to false alarms and missed detections. |
| 2025 | [A Reflective Surface Estimation Method Based on Multipath Utilization](https://doi.org/10.1109/TIM.2025.3541688) — Luo et al. | IEEE Transactions on Instrumentation and Measurement 74, 1–11 (2025) | Estimates the relay/reflective surface itself from multipath-ellipse tangency, dictionary matching and Kalman smoothing, turning a normally assumed calibration quantity into part of the radar inverse problem. |
| 2025 | [NLOS Tracking with Distributed Radar Using Multipath-Assisted JPDA](https://doi.org/10.1109/IGARSS55030.2025.11242772) — Xu et al. | IEEE IGARSS 2025, 8751–8755 | Extends multipath exploitation from static localization to distributed-radar NLOS tracking with multipath-assisted joint probabilistic data association. |
| 2025 | [Non-Line-of-Sight Target Localization in Unknown L-Shaped Corridor Based UWB MIMO Radar](https://doi.org/10.23919/JSEE.2025.000021) — Jia et al. | Journal of Systems Engineering and Electronics 36(3), 681–693 (2025) | Uses dual backprojection views and diffraction/reflection path-length matching to estimate hidden target positions and the unknown corridor width, remaining effective when some propagation paths are lost. |
```

**Insertion B — RF/mmWave category table:** add the same six records beside the current measured radar / HoloRadar / unknown-relay / multipath entries rather than only leaving them in Latest Additions.

**Insertion C — `## Milestone Timeline`:** augment the 2025 radar sentence after the current “Bayesian relay-angle inference and LiDAR-free reflector reconstruction…” sentence with:

> Reflective-surface estimation and unknown L-shaped-layout reconstruction further made the relay environment an estimated state rather than fixed calibration, while binary-accumulation positioning and distributed JPDA extended multipath exploitation toward robust localization and tracking.

Augment the 2026 radar paragraph after the current range-migration/FISTA radar sentence with:

> Zhu et al. then unified weak-reflector 3-D environmental perception with path-oriented NLOS moving-target reconstruction, closing the loop from relay estimation to dynamic hidden-target imaging in one measured mmWave MIMO framework.

### 2. `index.html`

The website’s `const papers = [...]` array uses objects of the form `{cat,title,authors,year,venue,url,key}`. Insert these near the current HoloRadar / ACTE-Net / RM-operator radar objects:

```javascript
{cat:"latest modality radar mmwave multipath environment reconstruction tracking",title:"Multipath Exploitation-Based 3-D Environmental Perception and NLOS Moving Target Reconstruction for mmWave MIMO Imaging Radar",authors:"Zhu et al.",year:2026,venue:"IEEE TAES 2026",url:"https://doi.org/10.1109/TAES.2025.3647422",key:"Jointly estimates 3-D environmental/reflector structure from weak multipath and transfers the recovered geometry into path-oriented NLOS moving-target reconstruction and localization on measured mmWave MIMO data."},
{cat:"latest modality radar layout localization",title:"NLOS Building Layout and Target Estimation in an L-Shaped Corner with Complex Geometries",authors:"Xue et al.",year:2025,venue:"IEEE TIM 2025",url:"https://doi.org/10.1109/TIM.2024.3522427",key:"Tracks multipath ToAs and separates diffraction plus first-/second-order reflection paths to jointly localize a hidden target and reconstruct part of an unknown L-shaped building layout."},
{cat:"latest modality radar localization multipath",title:"A Two-Stage NLOS Target Positioning Method Based on 0-1 Non-Coherent Binary Accumulation",authors:"Wu et al.",year:2025,venue:"IEEE TVT 2025",url:"https://doi.org/10.1109/TVT.2025.3542117",key:"CFAR-derived binary thresholds and 0-1 non-coherent accumulation feed a two-stage NLOS estimator designed to suppress false alarms and missed detections."},
{cat:"latest modality radar relay geometry multipath",title:"A Reflective Surface Estimation Method Based on Multipath Utilization",authors:"Luo et al.",year:2025,venue:"IEEE TIM 2025",url:"https://doi.org/10.1109/TIM.2025.3541688",key:"Estimates reflective relay geometry from multipath-ellipse tangency, dictionary matching and Kalman smoothing instead of assuming the reflector is known."},
{cat:"latest modality radar tracking multipath distributed",title:"NLOS Tracking with Distributed Radar Using Multipath-Assisted JPDA",authors:"Xu et al.",year:2025,venue:"IEEE IGARSS 2025",url:"https://doi.org/10.1109/IGARSS55030.2025.11242772",key:"Distributed-radar NLOS tracking incorporates multipath into JPDA data association rather than discarding it as clutter."},
{cat:"latest modality radar uwb localization layout",title:"Non-Line-of-Sight Target Localization in Unknown L-Shaped Corridor Based UWB MIMO Radar",authors:"Jia et al.",year:2025,venue:"JSEE 2025",url:"https://doi.org/10.23919/JSEE.2025.000021",key:"Dual backprojection views and diffraction/reflection path matching estimate hidden target positions and unknown corridor width even when some multipath components are missing."},
```

**Latest cards:** include the Zhu 2026 TAES paper in `latestGrid`; Xue 2025 is the best second card if more than one radar addition is surfaced.

**Timeline:** apply the same 2025/2026 trajectory sentences proposed for README so the homepage tells the progression from assumed relay geometry → estimated relay geometry → robust localization/tracking → joint environment + moving-target reconstruction.

### 3. `article/5newscenes.tex` / `bare_jrnl.tex`

`bare_jrnl.tex` currently includes `article/5newscenes.tex`, and its bibliography is `egbib_merged_20260711`. Therefore the semantically correct survey edit is in **`article/5newscenes.tex`, subsection `Radar-Based NLOS Imaging`**, not as an appended list at the end of `bare_jrnl.tex`.

Insert the following paragraph after the current discussion of LiDAR-free reflector reconstruction / practical multipath exploitation and before (or immediately after) the current RIS paragraph:

```tex
\vspace{0.8mm}
\noindent \textbf{From assumed relay geometry to joint environment and target inference.}
A parallel radar trajectory removes the common assumption that the reflective environment is known a priori. Luo~\etal~estimate the reflective surface directly from the tangency between the reflector and multipath ellipses, using dictionary matching and temporal smoothing to recover relay geometry from radar measurements~\cite{luoReflectiveSurfaceMultipath2025}. Xue~\etal~jointly recover an NLOS target and part of a complex L-shaped building layout by tracking multipath time-of-arrival sequences and assigning diffraction, first-order reflection, and second-order reflection paths to complementary target- and wall-estimation roles~\cite{xueNLOSBuildingLayout2025}. Jia~\etal~similarly use two backprojection views and path-length consistency to estimate both hidden targets and the width of an unknown L-shaped corridor even when part of the multipath set is missing~\cite{jiaUnknownCorridorNLOS2025}. Once this geometry uncertainty is exposed, the problem also becomes one of robust dynamic inference: Wu~\etal~use CFAR-derived 0--1 non-coherent binary accumulation followed by two-stage positioning to mitigate false alarms and missed detections~\cite{wuTwoStageNLOSPositioning2025}, while Xu~\etal~extend multipath exploitation to distributed-radar tracking with multipath-assisted JPDA~\cite{xuDistributedRadarNLOSTracking2025}. Zhu~\etal~then close this loop by first performing 3-D environmental perception from weak reflector echoes and transferring the inferred reflector parameters into path-oriented NLOS moving-target reconstruction with mmWave MIMO imaging radar~\cite{zhuMultipathEnvironmentNLOS2026}. Together, these works shift RF NLOS from reconstruction under a calibrated relay map toward joint estimation of the environment, propagation paths, hidden-target state, and motion.
```

At the top of `bare_jrnl.tex`, add a one-line maintenance comment such as:

```tex
% 11 August 2026 radar citation/lineage trace: unknown relay geometry, robust multipath positioning, distributed NLOS tracking, and joint 3-D environment/target reconstruction staged.
```

### 4. Bibliography

A verified staging bibliography has been committed as:

`egbib_20260811_radar_multipath_geometry_gap.bib`

with the citation keys used above:

- `zhuMultipathEnvironmentNLOS2026`
- `xueNLOSBuildingLayout2025`
- `wuTwoStageNLOSPositioning2025`
- `luoReflectiveSurfaceMultipath2025`
- `xuDistributedRadarNLOSTracking2025`
- `jiaUnknownCorridorNLOS2025`

When applying the public patch, merge these entries into `egbib_merged_20260711.bib` (or regenerate that merged file from the source bibs) and run a duplicate-key/duplicate-DOI check.

### 5. PDF build and consistency checks required after the patch

Do **not** consider the living PDF synchronized until all public source edits above have been applied. Then rebuild from the repository root with the same validated sequence used by the current project:

```text
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

Required checks:

1. No undefined citations for the six keys above.
2. Each of the six titles appears in README and the searchable website.
3. The survey prose cites all six through `article/5newscenes.tex`.
4. `egbib_merged_20260711.bib` contains exactly one entry per DOI/key.
5. Extracted PDF text contains at least the Zhu 2026 TAES title/author phrase and the “joint environment and target inference” paragraph.
6. Render the regenerated `bare_jrnl.pdf` and inspect the radar subsection for overfull text, broken references, or bibliography layout regressions.

## Why this run does not overwrite the public files directly

The available GitHub connector can safely create small text artifacts but its file-update action replaces an entire UTF-8 file. In this run there is no reliable full repository checkout in the execution environment, so replacing the very large `README.md`, `index.html`, `article/5newscenes.tex`, `egbib_merged_20260711.bib`, or the binary PDF would risk truncation or loss of concurrent repository content. Following the repository-update instruction, this run therefore **does not blindly overwrite those files**. It commits the verified BibTeX staging file and this exact insertion patch instead.

Accordingly, **`bare_jrnl.pdf` has not been regenerated in this run**. The PDF from the preceding synchronized commit remains the current public PDF until this patch is applied and compiled.
