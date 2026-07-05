# 2026-07-05 update: transient-sinogram / C2NLOS missing active NLOS paper

## Search and verification summary

This run did not surface a new high-confidence 2026 frontier NLOS imaging paper beyond the current July 2026 list. Keyword search and citation-tracing-style checks around confocal/LCT, phasor-field, sparse-scanning, SPAD-array, single-pixel, and transient reconstruction mainly returned papers already covered in the README / website or previous update notes.

One genuinely missing active optical NLOS paper was found and verified as relevant:

- **Efficient Non-Line-of-Sight Imaging from Transient Sinograms** — Mariko Isogawa, Dorian Chan, Ye Yuan, Kris M. Kitani, Matthew O'Toole, **arXiv 2020**.  
  arXiv: <https://arxiv.org/abs/2008.02787>

## Why it belongs

The paper is directly about active ToF NLOS reconstruction. It introduces circular confocal NLOS scanning (**C2NLOS**), observes that circular confocal measurements form transient sinograms, and reconstructs 3D hidden positions / NLOS images from substantially fewer relay-wall measurements than dense raster scanning. It is therefore best categorized under active optical NLOS, sparse / efficient acquisition, and computational reconstruction.

## Repository changes made

- `README.md`: added the paper to **Latest Additions** under 2020.
- `egbib_20260705_updates.bib`: added BibTeX entry `isogawaTransientSinograms2020`.

## Still recommended for full consistency

### `index.html`

Add a paper object to the website paper list and latest additions, e.g.

```js
{
  year: 2020,
  title: 'Efficient Non-Line-of-Sight Imaging from Transient Sinograms',
  authors: 'Isogawa et al.',
  venue: 'arXiv 2020',
  category: 'active',
  url: 'https://arxiv.org/abs/2008.02787',
  key: 'Circular confocal NLOS (C2NLOS) scanning and transient-sinogram reconstruction reduce relay-wall measurements while retaining hidden-position and image recovery.'
}
```

Also increment the homepage latest-entry count by one if the paper is included in `latestGrid`.

### `article/2active.tex`

The most natural semantic location is the active transient / sparse-scanning discussion. A minimal safe patch is to add the citation key to the pulsed-laser/SPAD 3D reconstruction row:

```tex
...,musarraNonlineofsight3DImaging2019,isogawaTransientSinograms2020,liuVirtualWaveOptics2018,...
```

A short narrative sentence could be inserted in the reconstruction / efficient acquisition paragraph:

```tex
Complementary to dense confocal raster scanning, Isogawa \etal\ proposed circular confocal NLOS scanning, where transient measurements along a circular relay-wall path form a transient sinogram that supports efficient hidden-position and image reconstruction from far fewer samples~\cite{isogawaTransientSinograms2020}.
```

### `bare_jrnl.tex` / PDF

`bare_jrnl.tex` still needs to include all supplemental BibTeX files before recompilation:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates}
```

The GitHub connector can safely update text files, but this run did not have a safe LaTeX compilation and binary PDF upload path. Therefore `bare_jrnl.pdf` was **not** regenerated in this run.
