# 27 July 2026 — RIS-assisted NLOS direction-estimation update

## Status

Two DOI-verified RF/NLOS sensing papers were found that are absent from the current `README.md`, `index.html`, survey source, and consolidated bibliography. They are genuinely NLOS target sensing papers, but they estimate target direction rather than reconstructing a hidden image or 3D surface. Both rely on simulated measurements, so the survey should label them as **RIS-assisted NLOS angular sensing (simulation)** rather than experimental NLOS imaging.

A canonical BibTeX supplement has been committed as `egbib_20260727_ris_doa.bib`. The large public artifacts were not replaced in this run because the available repository write action requires complete whole-file replacement; staging precise insertions avoids truncation, stale-base overwrites, and conflicts with the frequently updated 200+ paper explorer. Consequently, `bare_jrnl.pdf` has **not** been regenerated in this commit.

## Verified missing records

### Reconfigurable intelligent surface-enabled gridless DoA estimation system for NLoS scenarios

- Jiawen Yuan, Gong Zhang, Kaitao Meng, Henry Chi Ming Leung
- *Signal Processing*, vol. 233, article 109934, August 2025
- DOI: `10.1016/j.sigpro.2025.109934`
- Contribution: An RIS establishes a controllable virtual-LOS path to hidden targets. The method forms a covariance-domain signal model for a limited receive array, estimates noise variance, reconstructs a Hermitian Toeplitz matrix through atomic-norm minimization, and uses ADMM for lower-complexity gridless multi-target DoA estimation. The paper derives a CRLB and validates the method numerically.
- Scope label: `RF / RIS / NLOS localization / gridless DoA / simulation`.

### RIS-aided monostatic radar for NLOS target DOA estimation based on steering vector decoupling

- Yujia Zhang, Peng Yang, Yu Zhou, Lijun Liu, Haoran Mo, Lan Du
- *Signal Processing*, vol. 248, article 110685, 2026; available online 6 May 2026
- DOI: `10.1016/j.sigpro.2026.110685`
- Contribution: In an L-shaped-corridor model, the monostatic radar signal follows radar–RIS–target–RIS–radar transport. A RIS phase-codebook scans hidden directions, matrix operations recover the outer-product matrix of the target steering vector from element-wise superposition, and Root-MUSIC estimates high-resolution target angles. Validation is simulation-only.
- Scope label: `RF / RIS / monostatic radar / NLOS DoA / simulation`.

## Required source insertions

### `README.md`

1. Add both records to **Latest Additions** with the scope limitations above.
2. Add them to the RF/RIS portion of **New NLOS Scenes and Modalities**, adjacent to:
   - *Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface*;
   - *Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface*;
   - *Beyond λ/2: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?*
3. Add a 2025 timeline clause for covariance-domain gridless RIS DoA and a 2026 clause for steering-vector-decoupled monostatic RIS DoA.
4. Do not describe either work as hidden-scene reconstruction or measured radar imaging.

Suggested concise rows:

```markdown
| 2025 | [Reconfigurable intelligent surface-enabled gridless DoA estimation system for NLoS scenarios](https://doi.org/10.1016/j.sigpro.2025.109934) — Yuan et al. | Signal Processing 2025 | Uses an RIS-created virtual-LOS path, covariance-domain denoising, atomic-norm minimization and ADMM for gridless multi-target direction estimation with limited receive hardware; numerical validation only. |
| 2026 | [RIS-aided monostatic radar for NLOS target DOA estimation based on steering vector decoupling](https://doi.org/10.1016/j.sigpro.2026.110685) — Zhang et al. | Signal Processing 2026 | Scans hidden directions with an RIS codebook, decouples the target steering-vector outer product from the composite monostatic echo and applies Root-MUSIC for NLOS angle estimation; simulation-only, not hidden-shape reconstruction. |
```

### `index.html`

1. Add two paper-explorer objects with category `modality` and tags including `radar`, `RF`, `RIS`, `NLOS localization`, `DoA`, and `simulation`.
2. Insert corresponding 2025 and 2026 timeline text near the existing engineered-reflector/RIS branch.
3. Recalculate the explorer total from the paper array rather than hard-coding it; with the current snapshot this should move from 223 to 225 if no other paper is merged first.
4. Keep the public date synchronized with the README after integration.

### `article/5newscenes.tex`

Insert the following paragraph in **Radar-Based NLOS Imaging**, immediately after the broad paragraph that discusses RIS-assisted around-corner radar, the dual-beam one-bit RIS, EM skins, EMVS arrays, `mmMirror`, and `See and Beam`:

```tex
\vspace{0.8mm}
\noindent \textbf{RIS-assisted gridless and monostatic angular sensing.}
A complementary RIS trajectory targets hidden-object direction rather than reflectivity or surface reconstruction. Yuan~\etal~formulated RIS-enabled NLOS direction finding in the covariance domain~\cite{yuanRISGridlessDoA2025}: after estimating the noise variance, atomic-norm minimization recovers a Hermitian Toeplitz representation and an ADMM solver provides gridless multi-source DoA estimates with limited receive hardware. Zhang~\etal~considered a monostatic radar--RIS--target--RIS--radar path~\cite{zhangRISMonostaticDOA2026}. A phase-codebook scans the hidden angular sector, steering-vector decoupling recovers the target outer-product matrix from the RIS-element superposition, and Root-MUSIC estimates the target angles. Both studies are numerical, so they should be read as theoretical RIS-assisted NLOS localization advances rather than measured hidden-scene imaging systems.
```

### Consolidated bibliography

Merge `egbib_20260727_ris_doa.bib` into `egbib_merged_20260711.bib` while preserving the keys:

- `yuanRISGridlessDoA2025`
- `zhangRISMonostaticDOA2026`

Before merging, verify that each DOI occurs exactly once and that no title-normalized duplicate exists under another key.

### `bare_jrnl.tex` and PDF

The survey body is split across included section files, so no detached recent-paper list is needed in `bare_jrnl.tex`. After the semantic insertion and bibliography merge:

```bash
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

Then verify:

- both citation keys resolve and appear in `bare_jrnl.pdf`;
- neither DOI/title is duplicated;
- README, explorer, timeline, survey prose and bibliography contain both papers;
- both entries are explicitly labeled simulation-only angular sensing;
- the PDF modification/blob SHA changes only after a successful clean build;
- no undefined citations, multiply defined labels, missing bibliography entries, or truncated pages remain.

## Latest-publication check

These papers do not supersede the repository's latest date-verified direct NLOS publication. *Iterating the transient light transport matrix for non-line-of-sight imaging* remains the newest verified direct NLOS paper, published online by *Nature Communications* on 22 July 2026.
