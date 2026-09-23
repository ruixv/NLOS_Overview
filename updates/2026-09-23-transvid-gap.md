# TransVID integration gap — 2026-09-23

Verified missing paper:

Shida Sun, Yue Li, Jiacheng Fu, Feihu Xu, Zhiwei Xiong, “Transient video interpolation for dynamic non-line-of-sight imaging,” *Optics Express*, vol. 34, no. 3, pp. 4882–4894, 2026. DOI: 10.1364/OE.580550.

## Why it belongs
TransVID is a dynamic active/transient NLOS method that uses latent conditional diffusion with tailored spatial-temporal attention to interpolate transient measurements. It addresses the acquisition trade-off between spatial resolution and frame rate and reports recovery of 128×128 hidden-scene transient video at 16 FPS from 16×16 measurements at 4 FPS. It should be treated as a learned acquisition/reconstruction bridge rather than a generic video-interpolation paper.

## Verified repository gap
Repository-wide searches for the exact title and `TransVID` returned no match before staging this update.

## Safe integration locations
- **README.md / Latest Additions:** add a 2026 Optics Express entry emphasizing diffusion-based transient video interpolation and dynamic NLOS.
- **README.md / Active NLOS + Deep Learning:** place near dynamic NLOS / ST-Mamba / transient-transformer works; distinguish interpolation of the measured transient field from direct hidden-volume reconstruction.
- **Milestone timeline:** `2026 — TransVID: diffusion-based transient video interpolation lifts measured 16×16/4-FPS transient sequences to 128×128/16-FPS for dynamic NLOS.`
- **index.html / Paper Explorer:** category `Active · Transient · Dynamic · Diffusion`; add the same final venue/DOI and concise contribution summary.
- **bare_jrnl.tex:** integrate in the dynamic/learned transient reconstruction discussion after ST-Mamba (or the closest dynamic-NLOS paragraph), noting the shift from reconstructing each captured frame to computationally increasing the transient acquisition frame rate through generative interpolation.
- **canonical bibliography:** merge the verified BibTeX entry staged in `egbib_20260923_transvid_optics_express.bib`.
- **bare_jrnl.pdf:** rebuild only after the canonical TeX and bibliography are safely integrated.

## Consistency status
This note and the verified BibTeX staging file are committed. README.md, index.html, bare_jrnl.tex, the canonical bibliography, and bare_jrnl.pdf still require canonical integration/rebuild; do not claim those artifacts are synchronized until verified.
