# 5 August 2026 THz deep-unfolding NLOS consistency update

## Verified paper

**Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging** — Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, and Xiaolin Mi; *Photonics* 13(5), 440 (2026). DOI: `10.3390/photonics13050440`.

The publisher record reports publication on 30 April 2026. The study builds a measured 121 GHz near-field around-corner radar platform and embeds fast holographic forward/adjoint operators in a FISTA-derived deep-unfolding network. Experiments reconstruct hidden metal letters, a resolution chart, and scissors while addressing phase errors, aperture shadowing, and multipath artifacts.

## Scope and citation-lineage decision

This is genuine NLOS imaging rather than propagation-condition classification: coherent wall-reflected radar echoes are inverted into hidden three-dimensional scattering geometry. It extends the THz lineage from geometric mirror folding to physics-guided learned reconstruction and connects the radar/RF, sparse-inversion, and model-driven-learning branches.

## Cross-artifact audit

The title, DOI, contribution summary, and 2026 trajectory are already present exactly once in `README.md` and `index.html`, including the website's `latest` category. The paper is not yet integrated into the LaTeX survey section, merged bibliography, or rendered PDF. The bounded insertion is encoded in `scripts/integrate_thz_deep_unfolding_nlos_20260805.py` and is intentionally anchored in the existing **Terahertz NLOS Imaging** subsection rather than appended as a detached list.

## Exact remaining source insertion

Insert the following paragraph after the existing Cui--Trichopoulos THz mirror-folding paragraph in `article/5newscenes.tex`, immediately before the `NLOS Human Pose Estimation` subsection:

```tex
\vspace{0.8mm}
\noindent \textbf{Model-driven learned THz reconstruction.}
Chen~\etal~extend this modality from geometric mirror folding to learned sparse 3D inversion with a measured 121~GHz platform~\cite{chenDeepUnfoldingTHzNLOS2026}. Their formulation represents near-field around-corner transport with efficient holographic forward and adjoint operators, then unfolds FISTA into a fixed-depth network whose step, threshold, and momentum parameters are learned from simulated NLOS echoes. Measurements of hidden metal letters, a resolution chart, and scissors show that the physics-guided network suppresses phase-error, aperture-shadowing, and multipath artifacts while avoiding the memory cost of an explicit large sensing matrix. This work marks a transition in the THz branch from direct geometric relocation toward interpretable model-driven learning, while retaining coherent measured-data validation.
```

Add the dated synchronization comment immediately below `%% bare_jrnl.tex`:

```tex
% 5 August 2026 modality/citation trace: measured THz radar deep unfolding integrated across public artifacts.
```

The publisher-verified BibTeX entry is stored in `egbib_20260805_thz_deep_unfolding.bib` under key `chenDeepUnfoldingTHzNLOS2026`.

## Build and validation still required

1. Run `python3 scripts/merge_nlos_bibliography.py` to regenerate `egbib_merged_20260711.bib` and its deduplication audit.
2. Clean auxiliary files and run `pdflatex`, `bibtex`, followed by enough `pdflatex` passes to resolve references.
3. Verify the citation key occurs once in the section and merged bibliography and is present in `.aux` and `.bbl`.
4. Confirm the PDF contains the THz subsection paragraph and paper title, has no unresolved/repeated citations, and has a changed binary hash.
5. Render and inspect the first and last PDF pages before committing `bare_jrnl.pdf`.

The public README and website must not receive a duplicate paper entry or an incremented explorer count during this consistency repair.
