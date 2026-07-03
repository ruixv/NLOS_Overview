# 2026-07-03 update: commercial-LiDAR deep-remapping NLOS sync

## Added / synchronized paper

- **Fast Non-line-of-sight Imaging with Two-step Deep Remapping** — Dayu Zhu, Wenshan Cai, **arXiv 2021**.  
  Link: https://arxiv.org/abs/2101.10492

## Why it was included

This paper is a genuine NLOS reconstruction work and is tightly relevant to the repository's low-cost / consumer-LiDAR trajectory. It applies inexpensive commercial LiDAR for NLOS detection and uses a generative two-step deep remapping strategy for fast, high-fidelity reconstruction, including full-color NLOS examples. It is also already semantically discussed in `article/4datadriven.tex` through `\cite{zhuFastNonlineofsightImaging2021a}`, but the BibTeX key was missing and the paper was not visible in the README Latest Additions.

No final journal or conference venue was verified in this run, so the venue/status remains **arXiv 2021**.

## Files updated in this run

- `README.md`
  - Added the Zhu/Cai commercial-LiDAR deep-remapping paper to Latest Additions under 2021.
- `egbib_20260703_updates.bib`
  - Added `zhuFastNonlineofsightImaging2021a` so the existing survey citation can resolve once the supplementary bibliography files are included.

## Website patch still recommended

`index.html` was not overwritten in this run because it remains a hand-maintained single-file HTML/JS artifact and connector writes require whole-file replacement. Apply the following safe edits in a local editor:

1. Change the hero/footer/update count:

```html
Updated 3 July 2026 · 190+ papers
```

```html
<div class="stat"><b>44</b><span>tracked latest entries</span></div>
```

```html
Last updated: 3 July 2026
```

2. Insert this paper object into the `papers` array near the other 2021 latest entries:

```js
{cat:'latest learning active modality', title:'Fast Non-line-of-sight Imaging with Two-step Deep Remapping', authors:'Zhu and Cai', year:2021, venue:'arXiv 2021', url:'https://arxiv.org/abs/2101.10492', key:'Commercial-LiDAR NLOS reconstruction using generative two-step deep remapping for millisecond-scale, full-color hidden-scene recovery.'},
```

3. Also sync the website with the earlier README-only latest entries that are still absent from `index.html`: LEAP, scattering-media phasor fields, HDPS passive limited-prior NLOS, passive acoustic around-corner correlation, active focusing / UNCOVER, RIS/ISAC RF sensing entries, and commercial-LiDAR deep remapping.

## Survey / PDF status

`article/4datadriven.tex` already contains the semantic survey discussion and citation for this work, so this run only fixed the missing BibTeX metadata.

The PDF was not regenerated. To compile the updated survey, first change the bibliography line in `bare_jrnl.tex` to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates}
```

Then run LaTeX/BibTeX locally and upload the regenerated `bare_jrnl.pdf`.
