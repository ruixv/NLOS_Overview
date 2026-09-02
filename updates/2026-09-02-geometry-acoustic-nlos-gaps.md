# Verified NLOS corpus gaps — 2 September 2026

This search pass combined recent keyword/web searches with citation-neighborhood checks around the active NLOS core (Velten 2012, LCT, f-k migration, phasor fields), passive computational periscopy, learned transient reconstruction, and modality-expansion branches. Two high-confidence papers were verified as genuinely relevant and absent from the current repository by exact-title/DOI search.

## 1. Geometry-Constrained Non-Line-of-Sight Imaging

- Xueying Liu, Lianfang Wang, Jun Liu, Yong Wang, Yuping Duan.
- **IEEE Transactions on Visualization and Computer Graphics**, 32(7):6524–6536, 2026.
- DOI: `10.1109/TVCG.2026.3684832`
- Earlier preprint: arXiv:2503.17992, titled *Geometric Constrained Non-Line-of-Sight Imaging*.
- Verified final venue: IEEE TVCG; therefore the repository should use the final journal venue rather than arXiv.
- Contribution: jointly reconstructs hidden-scene albedo/surface geometry while regularizing the normal field through the shape operator. It reports more accurate hidden surfaces from transient data acquired within 15 s and substantially faster optimization than prior surface-reconstruction approaches.
- Recommended categorization: Active optical / transient reconstruction / geometry-aware inverse methods / normal-field regularization.
- Suggested timeline summary: “Introduces shape-operator regularization for joint hidden albedo and surface reconstruction, explicitly treating surface normals as a geometric prior for higher-fidelity transient NLOS recovery.”
- Survey insertion: `article/2active.tex`, near geometry-aware inverse methods / albedo-normal or surface-reconstruction discussion. Suggested literature-review sentence: “Beyond intensity/depth recovery, Liu et al. explicitly regularize the hidden normal field through the shape operator and jointly estimate albedo and surface geometry, illustrating a shift toward higher-order geometric constraints in transient NLOS inversion.”

## 2. A dual-branch fusion network for footstep sound source localization in non-line-of-sight corridors

- Xiaonan Wang, Zhe Chen, Fuliang Yin.
- **The Journal of the Acoustical Society of America**, 160(2):1400–1412, 2026.
- DOI: `10.1121/10.0044386`
- Contribution: proposes CorridorLocNet for real-world acoustic NLOS localization around corridor corners. The model fuses Mel-spectrogram and GCC-PHAT cues with residual-convolution and lightweight-Conformer branches plus cross-attention, and evaluates on a real footstep dataset collected behind a corridor corner.
- Recommended categorization: Acoustic NLOS / passive localization / learned multimodal-feature fusion / robotics sensing.
- Suggested timeline summary: “Moves acoustic NLOS localization from explicit propagation models toward learned time-frequency/spatial-feature fusion, using real behind-corner footsteps rather than simulated sources.”
- Survey insertion: acoustic/ultrasound NLOS subsection, after physics-/diffraction-aware acoustic localization. Suggested literature-review sentence: “Recent acoustic NLOS work also moves beyond explicit room or diffraction models: Wang et al. fuse Mel-spectral and GCC-PHAT spatial cues with convolutional and Conformer branches to localize real footstep sources around corridor corners.”

## Cross-artifact update plan

1. Add both papers to `README.md` Latest Additions and the 2026 development timeline.
2. Add both to the website/Paper Explorer (`data/papers-source.html` and the generated `index.html` metadata/date where appropriate).
3. Integrate the geometry paper into the active transient reconstruction discussion and the acoustic paper into the modality-expansion/acoustic subsection rather than appending an isolated list.
4. Merge the staged entries from `egbib_20260902_geometry_acoustic_gaps.bib` into the canonical bibliography, reusing an existing canonical key if a metadata-equivalent entry is discovered during integration.
5. Rebuild `bare_jrnl.pdf` and verify README, website, survey source, bibliography, AUX/BBL citation resolution, and PDF semantic text together.

## Safety note

The current connector can safely create this staged metadata and patch-style integration note, but direct replacement of large existing source files is unsafe when only partial/truncated reads are available. Do not overwrite README, website, survey, or the canonical bibliography blindly. Use the repository's guarded integration/CI mechanism or a full checkout before applying these insertions and rebuilding the PDF.
