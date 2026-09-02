# Incremental NLOS literature gaps — 2 September 2026

This note records verified papers that are still absent from the current public-facing corpus and gives precise integration guidance. Large canonical files were not blindly replaced because the available connector may truncate whole-file reads; integration should be performed by a local checkout or a safe patch-capable workflow.

## 1. Adaptive windowing for photon-efficient non-line-of-sight imaging under high ambient light

**Metadata**
- Jinye Miao, Fuyao Cai, Taotao Qin, Lianfa Bai, Enlai Guo, Yingjie Shi, Jing Han
- *Optics Express* 33(21), 44522–44542 (2025)
- DOI: 10.1364/OE.575419

**Why it belongs**
This is a direct active transient NLOS reconstruction paper. AW-NLOS models signal/background photon-arrival statistics, clusters correlated spatio-temporal pixels to estimate per-pixel short range windows, suppresses overwhelming ambient detections, and then uses TV-regularized reconstruction. It reports operation down to SBR 2.12 and signal flux around 0.02 photons/pixel. It is also a forward-citation successor to the authors' 2025 under-scanning DO-NLOS work, so it is particularly useful in the acquisition-efficiency / photon-starved branch.

**README / website placement**
- Latest Additions: add a 2025 row.
- Active NLOS Imaging → Reconstruction Algorithms / photon-efficient acquisition.
- Timeline near under-scanning / sparse acquisition / real-time work.

**Suggested concise summary**
> Uses probabilistic photon-arrival modeling and per-pixel adaptive temporal windows to suppress strong ambient background before TV-regularized reconstruction, enabling active NLOS under very low SBR and photon flux.

**Survey placement**
In the active-NLOS section that discusses sparse acquisition, photon efficiency, and acquisition/reconstruction co-design, add a sentence after under-scanning methods such as DO-NLOS:

> Beyond reducing the number of spatial samples, photon efficiency under strong ambient illumination can be improved by adapting the temporal support of each measurement. AW-NLOS estimates per-pixel short-duration range windows from clustered photon statistics and couples the resulting background suppression with total-variation reconstruction, extending transient NLOS operation to severe background and photon-starved regimes~\cite{miaoAdaptiveWindowingNLOS2025}.

## 2. Machine Learning-Based Human Detection Using Active Non-Line-of-Sight Laser Sensing

**Metadata**
- Semra Çelebi, İbrahim Türkoğlu
- *Sensors* 26(7), 2046 (2026)
- DOI: 10.3390/s26072046

**Why it belongs**
This is task-oriented active NLOS sensing rather than full hidden-scene reconstruction. A pulsed laser, SPAD and TCSPC system records real time–photon histograms over a 50×50 relay-wall scan in controlled debris-like scenarios. CNN, bidirectional-GRU and random-forest classifiers are compared for hidden-human presence detection. The work is tightly adjacent to reconstruction and belongs with NLOS detection / semantic sensing papers rather than in the core 3D-reconstruction sequence.

**README / website placement**
- Latest Additions: add a 2026 row.
- Active NLOS Imaging → Detection, Tracking and Recognition.
- Semantic/task-oriented sensing timeline, near HiddenPose / NLOS-Track / laser-acoustic orientation work.

**Suggested concise summary**
> Uses real SPAD–TCSPC time-photon histograms from a scanned active NLOS setup to detect hidden human presence, comparing CNN, bidirectional GRU and random-forest classifiers in debris-like scenes.

**Survey placement**
In the detection / recognition subsection:

> Recent work further shifts active transient NLOS from full reconstruction toward task-oriented semantic sensing. Çelebi and Türkoğlu use real SPAD–TCSPC time-photon histograms acquired across a relay-wall scan to classify hidden human presence, comparing convolutional, recurrent and ensemble models under controlled debris-like conditions~\cite{celebiActiveNLOSHumanDetection2026}.

## 3. Previously verified but still not integrated: Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging

**Metadata**
- Yijun Ling, Wenjin Zhao, Mengjia Zhao, Jie Yang
- *Symmetry* 18(5), 711 (2026)
- DOI: 10.3390/sym18050711

**Why it belongs**
This previously verified paper remains absent from current repository search results. It treats NLOS reconstruction as a multi-constraint optimization problem and coordinates reconstruction, physical-consistency and sensor-calibration gradients via PCGrad, PhysGuard and staged training. Real captured scenes are included qualitatively.

**README / website placement**
- Deep Learning for NLOS / physics-guided reconstruction.
- Timeline after NLOST / learned physical priors and near recent neural-operator / transformer methods.

**Suggested survey sentence**
> Physics-guided NLOS learning is also moving from adding physical penalties to controlling how heterogeneous objectives update shared parameters. Ling et al. coordinate reconstruction, measurement-consistency and sensor-calibration gradients through projected conflict resolution, hard physical routing and staged training, highlighting optimization-time constraint governance as an additional design axis for low-SNR transient reconstruction~\cite{lingSymmetryAwareNLOS2026}.

## Citation-tracing notes from this run

A high-priority forward-citation pass was performed around the LCT / f-k / phasor-field and computational-periscopy families. A useful branch emerged from the 2025 DO-NLOS paper: its citing works include AW-NLOS (missing, added above), the 2026 reference-function non-confocal frequency-domain method (already present in the current README), and the 2026 Super-FoV translated-PSF paper (already present in the current README). This reduces the risk of adding citation-neighborhood duplicates while still filling the photon-efficiency gap.

Fresh searches also re-surfaced TLTM iteration, MARMOT, 3D Gaussian Transient Rendering, thermal rough-surface NLOS, passive acoustic diffraction localization, learned LCT, and the 2026 passive diffuse-aware attention paper; these are already represented in the repository/update lineage and should not be duplicated.

## Bibliography

Verified BibTeX entries for the three pending papers are staged in:

`egbib_20260902_incremental_nlos_gaps.bib`

Before the next PDF build, merge these entries into the canonical bibliography used by `bare_jrnl.tex`, then add the corresponding citations to the semantically appropriate survey sections.

## Consistency checklist after safe integration

1. Add the same papers to README Latest Additions / timeline and the website paper explorer.
2. Add AW-NLOS and the active-human-detection paper to their appropriate survey sections rather than appending an isolated list.
3. Integrate the previously verified Symmetry paper at the same time so README/website/update logs do not outrun the survey.
4. Merge the staged BibTeX entries into the canonical bibliography with no duplicate keys/DOIs.
5. Rebuild `bare_jrnl.pdf` from `bare_jrnl.tex` and inspect unresolved citations.
6. Confirm exact-title / DOI presence across README.md, index.html, bare_jrnl.tex, bibliography and the regenerated PDF.
