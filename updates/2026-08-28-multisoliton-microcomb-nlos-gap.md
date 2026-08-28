# 2026-08-28 — Multi-soliton microcomb NLOS gap

## Verified missing paper

Jiawen Zhi, Xiaoyang Guo, Xusheng Yang, Brent E. Little, Sai T. Chu, Chenggang Shao, Mengyu Wang, Yan Liang, Peng Xie, Weiqiang Wang, and Hanzhong Wu, **“Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection,”** *Advanced Science*, vol. 13, no. 12, e16806, 2026. DOI: `10.1002/advs.202516806`.

Publisher metadata: Wiley lists Volume 13, Issue 12, e16806, first published 27 January 2026, with the issue dated 27 February 2026. Use the final journal venue, not a preprint label.

## Why this belongs in the NLOS overview

This is primarily a dual-microcomb ranging paper, but it contains a dedicated **Section 2.5, “Non-Line-of-Sight Imaging,”** with a genuine wall-mediated three-bounce NLOS experiment rather than a passing citation. The signal microcomb illuminates a relay wall; scattered light reaches a hidden stepped sample, returns through the wall, and is coherently mixed with a local microcomb. A 2D translation stage supplies lateral sampling at 0.5 mm steps, while dual-comb ranging recovers depth; the reconstructed 3D result resolves the three hidden letters with designed heights of 3, 4, and 4.5 mm. The paper also demonstrates photon-level dual-multi-soliton ranging at femtowatt returned powers and cites Huang et al., *PRL* 2024, “Non-Line-of-Sight Imaging and Vibrometry Using a Comb-Calibrated Coherent Sensor,” as its direct NLOS predecessor.

This makes the work tightly adjacent to the repository’s existing coherent/frequency-comb NLOS lineage:

`comb-calibrated coherent FMCW NLOS imaging/vibrometry (PRL 2024) -> comb-calibrated NLOS tracking / sensitive FMCW ranging (2025) -> dual-multi-soliton microcomb NLOS ranging and 3D imaging (Advanced Science 2026)`.

The contribution should be described conservatively: the novelty of the paper is the multi-soliton dual-comb ranging architecture and its speed/precision/efficiency advantages; NLOS imaging is an experimentally demonstrated application, not the sole focus of the article.

## Repository gap check

On 28 August 2026, repository searches for the exact title, DOI `10.1002/advs.202516806`, and `microcomb` returned no canonical paper record. The current README/survey already contains the direct predecessor `huangCombCalibratedNLOS2024` and the 2025 coherent-FMCW extensions, so this is a missing modality-lineage entry rather than a duplicate.

## Public-artifact integration plan

### README.md

Add a Latest Additions row, preferably near the other coherent/FMCW/comb NLOS entries:

```markdown
| 2026 | [Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection](https://doi.org/10.1002/advs.202516806) — Zhi et al. | Advanced Science 13(12), e16806 (2026) | Extends coherent frequency-comb sensing toward a dual-multi-soliton architecture and demonstrates wall-mediated NLOS 3D ranging as a dedicated experiment. A signal microcomb illuminates the relay wall, the hidden target is laterally sampled at 0.5 mm steps, and coherent dual-comb ranging resolves millimeter-scale depth structure; the broader system also operates at femtowatt returned powers. |
```

In the 2026 milestone timeline, add a concise node such as:

> **Multi-soliton dual-comb NLOS ranging:** coherent/frequency-comb NLOS sensing expands from comb-calibrated FMCW LiDAR to multi-soliton dual-comb ranging, demonstrating 3D hidden-target depth recovery while improving ranging speed, precision, and efficiency.

### Website / Paper Explorer

Update the canonical paper corpus used by the V2 site (`data/papers-source.html` in the current repository architecture; do not duplicate the record in `index.html` if the site continues to load the canonical corpus externally).

Suggested record fields:

- year: `2026`
- title: `Multi-Soliton Microcombs Enable Ultrafast Nanometric-Precision Ranging and Photon-Level Detection`
- authors: `Jiawen Zhi; Xiaoyang Guo; Xusheng Yang; Brent E. Little; Sai T. Chu; Chenggang Shao; Mengyu Wang; Yan Liang; Peng Xie; Weiqiang Wang; Hanzhong Wu`
- venue: `Advanced Science 13(12), e16806 (2026)`
- family: `active`
- key: `zhiMultiSolitonMicrocombNLOS2026`
- url: `https://doi.org/10.1002/advs.202516806`
- contribution: emphasize the dedicated three-bounce dual-comb NLOS 3D imaging experiment and the multi-soliton ranging architecture; do not describe it as a new general NLOS inverse solver.

Add the same coherent-frequency-comb development node to the website timeline.

### Survey source

Integrate semantically in `article/2active.tex`, next to the existing coherent/frequency-swept laser row and prose containing `huangCombCalibratedNLOS2024`, `yeCombCalibratedFMCWTracking2025`, `chenVectorEnhancedFMCWNLOS2025`, and related coherent NLOS sensing.

Recommended literature-review sentence:

```tex
Beyond comb-calibrated FMCW sensing, Zhi \etal~\cite{zhiMultiSolitonMicrocombNLOS2026} demonstrated that dual-multi-soliton microcombs can also support wall-mediated NLOS ranging and three-dimensional imaging. Their experiment sends the signal comb to a relay wall, coherently measures the returned hidden-target path with a local comb, and recovers millimeter-scale depth variation while retaining the high precision and photon-level sensitivity of the multi-soliton ranging architecture. This result broadens coherent NLOS sensing from frequency-comb calibration of FMCW LiDAR toward the frequency-comb source itself serving as the precision ranging engine.
```

Also add `zhiMultiSolitonMicrocombNLOS2026` to the active-method table’s frequency-swept/coherent interferometric row, or create a short adjacent row if the distinction between FMCW and dual-comb ranging is to be preserved explicitly.

### Bibliography

Merge the unique entry from `egbib_20260828_multisoliton_microcomb_nlos_gap.bib` into the canonical bibliography used by `bare_jrnl.tex` (currently `egbib_merged_20260711.bib` in recent builds). Ensure the DOI and citation key each occur once.

### bare_jrnl.tex / PDF

If `bare_jrnl.tex` directly includes `article/2active.tex`, no duplicate prose is needed in the root file beyond any repository-maintained update marker/date. Rebuild with the repository’s normal clean sequence, e.g.:

```text
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

Before publishing, verify:

1. `zhiMultiSolitonMicrocombNLOS2026` resolves in `.aux`/`.bbl` and has no undefined citation warning.
2. DOI `10.1002/advs.202516806` occurs exactly once in the canonical bibliography.
3. README, V2 Paper Explorer, timeline, `article/2active.tex`, bibliography, and extracted PDF text all contain the new entry/lineage.
4. Render at least the affected active-method page(s) and first/last PDF pages to catch layout regressions.
5. Commit the rebuilt `bare_jrnl.pdf` only after the clean build and semantic checks pass.

## Current status

This run intentionally does **not** claim that README, website, survey body, canonical bibliography, or `bare_jrnl.pdf` have already been updated. Large public files are maintained through whole-file writes in the available connector, so this run uses the repository’s safe fallback: verified BibTeX plus a precise, idempotent integration plan rather than risking truncation or partial synchronization.
