# 2026-09-11 THz deep-unfolding NLOS survey consistency update

## Verified paper

Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, and Xiaolin Mi, **“Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging,”** *Photonics*, vol. 13, no. 5, article 440, 2026. DOI: 10.3390/photonics13050440. Published 30 April 2026.

Publisher metadata: https://doi.org/10.3390/photonics13050440

## Why it belongs

This is a genuine measured NLOS 3D imaging paper rather than a generic radar paper. It establishes a looking-around-corner 121 GHz sub-THz radar platform, formulates hidden-target reconstruction as sparse inverse imaging, replaces the prohibitively large sensing matrix with a fast holographic imaging operator, and unfolds FISTA into an interpretable fixed-depth network. The measured targets include a metal letter E, a resolution chart, and scissors. The reported contribution therefore extends the radar/THz NLOS branch from geometry-based mirror folding and conventional sparse inversion toward model-driven deep unfolding on measured near-field data.

## Consistency finding in this run

The current README already lists this paper under the 2026 RF/mmWave/THz development timeline, but the modular LaTeX survey source `article/5newscenes.tex` currently reaches the Terahertz NLOS subsection with the Cui–Trichopoulos active-THz work and does not yet discuss this 2026 deep-unfolding result. The canonical survey bibliography used by `bare_jrnl.tex` is `egbib_merged_20260711.bib`; a verified standalone entry has therefore been staged in `egbib_20260911_thz_deep_unfolding.bib` rather than risking a blind replacement of the large merged bibliography.

## Required insertion in article/5newscenes.tex

Insert in `\subsection{Terahertz NLOS Imaging}`, after the paragraph on Cui and Trichopoulos and before `\subsection{NLOS Human Pose Estimation}`:

```tex
\vspace{0.8mm}
\noindent \textbf{Model-driven deep unfolding for measured sub-THz NLOS.}
Chen~\etal~extend active THz around-corner imaging from geometry-based mirror folding toward learned sparse inversion on a measured $121\,\mathrm{GHz}$ platform~\cite{chenTHzDeepUnfolding2026}. Their formulation replaces the prohibitively large NLOS sensing matrix with a fast holographic imaging operator and unfolds FISTA into a fixed-depth, interpretable reconstruction network whose learned parameters compensate phase error, aperture shadowing, and multipath. Measurements of several hidden metal targets show substantially sharper three-dimensional reconstructions while reducing computation by roughly two orders of magnitude relative to conventional iterative sparse imaging. This result links the radar/THz modality expansion to the broader NLOS trajectory of physics-structured operator learning: the propagation model remains explicit, while data-driven unfolding adapts the inverse to non-ideal reflecting geometry.
```

## Bibliography integration

Merge the verified entry from `egbib_20260911_thz_deep_unfolding.bib` into `egbib_merged_20260711.bib` using citation key `chenTHzDeepUnfolding2026`. Do not retain a second arXiv-only or title-duplicate entry if one is later found.

## README / website

- README already contains the paper; do not duplicate it. Preserve the final venue as *Photonics* 13(5), 440 (2026), not arXiv.
- Verify `index.html` / `data/papers-source.html` Paper Explorer coverage by exact DOI/title. If missing, add the same final-venue record and categorize as `RF/mmWave / THz` plus `learning / model-driven reconstruction`.
- A useful timeline placement is after the 2024 active-THz mirror-folding milestone, making the development explicit: environmental-surface THz imaging → measured sub-THz sparse inversion → physics-structured deep unfolding.

## PDF rebuild

After the LaTeX paragraph and canonical bibliography are merged, run the normal BibTeX/LaTeX build and regenerate `bare_jrnl.pdf`. Verify that the new citation resolves and that README, website explorer, modular survey source, merged bibliography, and PDF all agree before claiming full synchronization.

## Other checks from this run

Three apparent search gaps were false positives caused by code-search/index incompleteness: the survey already contains NANO / noise-adapted neural-operator reconstruction (`wangNoiseAdaptedNeuralOperator2025`), structure-guided adaptive TV (`zhangStructureGuidedATV2026`), and laser–acoustic hidden-human orientation sensing (`doganLaserAcousticOrientationNLOS2026`). They should not be re-added.
