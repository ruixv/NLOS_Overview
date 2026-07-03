# 2026-07-03 update: HDPS passive NLOS with limited prior data

## Newly added paper

- **Passive None-line-of-sight imaging with arbitrary scene condition and detection pattern in small amount of prior data** — Yunting Gui, Yuegang Fu, Xueming Xiao, Meibao Yao, **arXiv 2024**.
  - Link: https://arxiv.org/abs/2404.06015
  - BibTeX key: `guiHDPSPassiveNLOS2024`
  - Metadata decision: arXiv is the only verified venue found in this run; no final journal/conference venue was verified.
  - Relevance: direct passive NLOS imaging. The paper proposes High-Dimensional Projection Selection (HDPS) for estimating passive NLOS target/transport structure under arbitrary scene conditions and detection patterns with limited prior data, so it belongs to the ordinary-camera/passive NLOS branch rather than to general NLOS communication or unrelated side-channel sensing.

## Repository updates made

- `README.md`: added the HDPS paper to **Latest Additions** under 2024.
- `article/5newscenes.tex`: added a new survey paragraph/subsection, **Passive NLOS with Limited Prior Data**, to integrate HDPS into the development narrative from calibrated passive NLOS to adaptation under new transport conditions.
- `egbib_20260703_updates.bib`: added `guiHDPSPassiveNLOS2024`.

## Website patch still recommended

`index.html` was not overwritten in this run because it is a manually maintained HTML/JS file and the available update route requires whole-file replacement. To keep the website fully synchronized, add a paper-explorer/latest-additions object similar to:

```js
{
  year: 2024,
  title: "Passive None-line-of-sight imaging with arbitrary scene condition and detection pattern in small amount of prior data",
  authors: "Gui et al.",
  venue: "arXiv 2024",
  link: "https://arxiv.org/abs/2404.06015",
  category: "Passive / learned transport adaptation",
  summary: "HDPS estimates passive NLOS transport/target structure from limited prior data, targeting arbitrary scene conditions and detection patterns without a separate calibrated model for each setup."
}
```

Also increment the latest-entry count by one and add the paper to the 2024 timeline / passive NLOS category.

## PDF / LaTeX compilation status

The source and BibTeX supplement have been updated, but `bare_jrnl.pdf` was not regenerated. The main file still needs to use all supplement bibliography files:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates}
```

After that change, the survey should be compiled locally with LaTeX/BibTeX and the regenerated `bare_jrnl.pdf` uploaded. No binary PDF update was claimed in this run.
