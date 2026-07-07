# 7 July 2026 — Automation 16 citation-tracing and consistency audit

## Search scope

This run re-checked recent and missing NLOS-related work using keyword search and forward-citation-style tracing around the repository's core active/passive/multimodal seeds:

- Velten et al. 2012 experimental active NLOS reconstruction.
- O'Toole et al. 2018 confocal light-cone transform.
- Lindell et al. 2019 f-k migration.
- Liu et al. phasor-field / virtual-wave NLOS papers.
- Saunders et al. computational periscopy.
- Neural Transient Fields, transformer / graph / Mamba-style learned reconstruction, and recent Gaussian transient rendering.
- Modality-expansion lines: consumer LiDAR, acoustic NLOS, RF/mmWave/radar, RIS/IRS, THz, event-camera passive NLOS, and differentiable transient rendering.

## Result

No new high-confidence July 2026 frontier NLOS imaging paper was found beyond the current README/homepage frontier entries. The latest direct NLOS imaging or tightly adjacent sensing results returned by fresh searches remain the already covered arXiv 2026 items, including:

- 3D Gaussian Transient Rendering for arbitrary relay surfaces (`2606.21270`).
- Consumer-LiDAR motion-induced NLOS imaging (`2605.17865`).
- GeRaF 2.0 / RF seeing through boxes (`2605.29098`).
- DENALI low-cost LiDAR NLOS reasoning (`2604.16201`).
- RIS / IRS / ISAC / double-bounce radio sensing and imaging entries already present in README.

## Excluded candidates

The following recent search hits were not added because they are not hidden-scene / NLOS imaging or reconstruction papers under the repository taxonomy:

- `2607.00186`, *A Non-Line-of-Sight, Multi-Modality-based Side-Channel IP Theft Attack on Additive Manufacturing Using Dual Smartphones*: NLOS side-channel G-code reconstruction, not hidden-scene imaging.
- `2602.00633`, *Near-lossless method for generating thermal photon-bunched light*: mentions possible NLOS imaging applications of photon bunching but is primarily a source-generation paper, not an NLOS imaging method.
- `2601.10972`, *DuTrack*: Wi-Fi/acoustic indoor tracking; not around-corner hidden-scene reconstruction/imaging.

## Consistency status

`README.md` already contains the most recent surfaced entry from the previous run:

- Lei et al., *Direct Object Recognition Without Line-of-Sight Using Optical Coherence* (`1903.07705`), arXiv 2019.

`egbib_20260707_updates.bib` already contains the corresponding BibTeX key:

- `leiDirectObjectRecognition2019`.

`article/2active.tex` already references this key in the active recognition table.

## Remaining homepage patch

The public homepage still needs one safe HTML/JS sync after the previous README update:

1. Change the tracked latest-entry count from `65` to `66`.
2. Insert the following paper object after the Starshynov coherent-control entry in `index.html`:

```js
{cat:"latest active learning",title:"Direct Object Recognition Without Line-of-Sight Using Optical Coherence",authors:"Lei et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1903.07705",key:"Coherent illumination creates diffuse-wall speckle patterns that a deep network uses for direct hidden-object recognition rather than full 3D reconstruction."},
```

This run did not whole-file overwrite `index.html` because the current GitHub contents update path requires complete-file replacement and the file is a dense hand-maintained HTML/JS paper list. A patch-style note is safer than risking truncation.

## Remaining survey / PDF build status

`bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

For the updated survey build, replace it with:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates}
```

Then run LaTeX/BibTeX locally and upload the regenerated `bare_jrnl.pdf`. No PDF update is claimed in this run.
