# Vector and planar-optics NLOS citation-tracing update — 28 July 2026

## Status

Three direct active-NLOS papers were verified as genuinely missing from the current README, website explorer/timeline, survey prose/table, and consolidated bibliography. Canonical BibTeX is provided in `egbib_20260728_vector_optics_nlos.bib`.

The large public files and `bare_jrnl.pdf` are **not claimed as updated in this record**. A guarded one-run workflow was attempted, but no resulting source/PDF integration commit became visible. To avoid stale-base replacement or truncation, the remaining edits are documented precisely below.

## Verified missing papers

### High-Resolution Non-Line-of-Sight Imaging Based on Liquid Crystal Planar Optical Elements

- Authors: Zhibin Zhao, Qi Zhang, Xiaoyin Li, Yinghui Guo, Mingbo Pu, Fei Zhang, Hengshuo Guo, Zewei Wang, Yulong Fan, Mingfeng Xu, Xiangang Luo
- Venue: *Nanophotonics* 13(12), 2161–2172, 2024
- DOI: `10.1515/nanoph-2023-0655`
- Contribution: inserts a liquid-crystal planar angle-magnification element into a transient NLOS system to enlarge the effective relay-wall aperture. Correlation-aware sparse scanning reduces acquisition time by more than 20% without sacrificing the demonstrated resolution.
- Category: active optical / transient hardware / planar optics / high-resolution acquisition.

### Vectorial-Optics-Enabled Multi-View Non-Line-of-Sight Imaging with High Signal-to-Noise Ratio

- Authors: Zewei Wang, Xiaoyin Li, Mingbo Pu, Lianwei Chen, Fei Zhang, Qi Zhang, Zhibin Zhao, Longfei Yang, Yinghui Guo, Xiangang Luo
- Venue: *Laser & Photonics Reviews* 18(6), 2300909, 2024
- DOI: `10.1002/lpor.202300909`
- Contribution: derives a vector-optical-field relay-reflection model and uses illumination angle, incident polarization, and received polarization as controllable measurement dimensions. The resulting multi-view measurements improve hidden-object reconstruction and recognition under low SNR.
- Category: active optical / vector optics / polarization / multi-view NLOS.

### Vectorial Digitelligent Optics for High-Resolution Non-Line-of-Sight Imaging

- Authors: Yinghui Guo, Yunsong Lei, Mingbo Pu, Fei Zhang, Qi Zhang, Xiaoyin Li, Runzhe Zhang, Zhibin Zhao, Rui Zhou, Yulong Fan, Xiangang Luo
- Venue: *Engineering* 45, 70–78, 2025
- DOI: `10.1016/j.eng.2024.11.013`
- Contribution: jointly optimizes wavefront phase and polarization through a rough relay wall, then raster-scans the optimized focus within the optical-memory-effect range. The measured system reaches 0.40 mm resolution at 0.35 m and retains photon timing for axial separation.
- Category: active optical / vector wavefront shaping / digitelligent optics / near-diffraction-limited NLOS.
- Metadata note: Elsevier/ScienceDirect and DOAJ give the final pagination as 70–78. A secondary journal mirror currently displays 76–84; the publisher-indexed 70–78 record should be used.

## Why these pass the relevance filter

The papers directly reconstruct or recognize hidden targets through relay-wall transport. They are not generic metasurface, polarization, or scattering-media papers that cite NLOS only in passing. Their citation neighborhood connects active focusing, LCT, phasor fields, computational periscopy, and subsequent high-resolution vector-optics NLOS work.

## Precise integration locations

### `README.md`

1. Add all three records at the top of **Latest Additions**.
2. Add the two 2024 works to the 2024 milestone block:
   - liquid-crystal planar angle magnification enlarges the relay aperture while sparse correlated scanning reduces acquisition;
   - vector-optical-field modeling turns illumination view and transmit/receive polarization into high-SNR multi-view measurements.
3. Add the 2025 Engineering paper to the 2025 milestone block as the transition to closed-loop joint phase/polarization focusing.

Suggested concise summaries:

- Zhao et al.: “Uses a liquid-crystal planar angle magnifier to enlarge the effective transient relay aperture, while correlation-aware sparse scanning reduces acquisition time by more than 20% without demonstrated resolution loss.”
- Wang et al.: “Selects illumination angle and transmit/receive polarization using a vector-optical-field reflection model, enabling higher-SNR multi-view hidden-object reconstruction and recognition.”
- Guo et al.: “Jointly optimizes phase and polarization through a scattering relay wall and raster-scans the resulting focus, reaching 0.40 mm resolution at 0.35 m with ToF-resolved axial structure.”

### `index.html`

1. Insert three searchable paper objects near the beginning of `const papers`.
2. Recommended tags:
   - `active high-resolution transient planar-optics liquid-crystal sparse-scanning`
   - `active high-resolution polarization multi-view vector-optics`
   - `active high-resolution wavefront-shaping polarization meta-optics`
3. Increase the tracked latest-entry count from 232 to 235 after confirming the JavaScript object count.
4. Extend the 2024 and 2025 timeline paragraphs with the development trajectory above.

### `article/2active.tex`

1. In Table `tab:active`, add one row after the continuous-laser/conventional-camera row:

```latex
\cite{zhaoLCPlanarNLOS2024,wangVectorialMultiviewNLOS2024,guoVectorialDigitelligentNLOS2025} & Shaped pulsed / continuous laser & SPAD / camera & ToF, intensity, and polarization & High-resolution 2D/3D reconstruction\\
```

2. Immediately after the existing **Active Focusing for High Resolution** paragraph on UNCOVER, add a short subsection-style paragraph titled:

```latex
\noindent \textbf{From planar aperture expansion to vectorial digitelligent focusing.}
```

The paragraph should explain the trajectory from liquid-crystal aperture magnification, to polarization-aware multi-view measurement selection, to closed-loop joint phase/polarization focusing. It should explicitly state that this line moves part of the inverse problem into optical co-design rather than replacing LCT, f-k migration, or phasor-field reconstruction.

### `bare_jrnl.tex`

Add a top-of-file audit marker:

```latex
% 28 July 2026 citation trace: liquid-crystal planar optics, vectorial multi-view sensing, and digitelligent wavefront/polarization focusing integrated.
```

No structural change is otherwise required because the detailed prose belongs in `article/2active.tex`.

### Bibliography

Merge the three records from `egbib_20260728_vector_optics_nlos.bib` into `egbib_merged_20260711.bib`, preserving the citation keys:

- `zhaoLCPlanarNLOS2024`
- `wangVectorialMultiviewNLOS2024`
- `guoVectorialDigitelligentNLOS2025`

## Build and validation

After source integration:

```bash
rm -f bare_jrnl.aux bare_jrnl.bbl bare_jrnl.blg bare_jrnl.log bare_jrnl.out bare_jrnl.toc
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

Verify:

1. each DOI occurs once in README, website, and consolidated bibliography;
2. each citation key appears in the active-system table, survey prose, `.aux`, and bibliography;
3. website paper-object count and displayed count agree at 235;
4. the LaTeX log has no undefined citations or repeated entries;
5. `pdftotext bare_jrnl.pdf -` contains all three titles;
6. first and last PDF pages render correctly;
7. the rebuilt PDF blob differs from the prior one before claiming that `bare_jrnl.pdf` was updated.
