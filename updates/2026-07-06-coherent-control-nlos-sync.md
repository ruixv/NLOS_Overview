# 2026-07-06 coherent-control NLOS update

## Search outcome

Fresh keyword and citation-tracing style searches did not reveal a new high-confidence July 2026 frontier NLOS imaging paper beyond the already tracked 2026 arXiv entries on arbitrary-relay 3D Gaussian transient rendering, consumer-LiDAR NLOS, GeRaF 2.0 / radar hidden-object reconstruction, ISAC / RIS / MIMO NLOS sensing, and low-cost LiDAR datasets.

The main missing directly relevant paper found in this run is:

- **Coherent control of light for non-line-of-sight imaging** — Ilya Starshynov, Omair Ghafur, James Fitches, Daniele Faccio, **arXiv 2019**. This active optical NLOS paper uses coherent phase control / wavefront shaping to refocus light behind an occluder and then uses the speckle memory effect to scan the focused spot across the hidden scene. It reports improved SNR with temporal gating and sub-millimeter resolution, making it a useful precursor to later active focusing / high-resolution NLOS work.

No final journal or conference venue was verified during this run, so the repository should label it as **arXiv 2019**.

## Files updated safely

- Added `egbib_20260706_updates.bib` with BibTeX key `starshynovCoherentControlNLOS2019`.

## README patch

Insert the following row in `README.md` under **Latest Additions**, in the 2019 block after `Wave-like Properties of Phasor Fields: Experimental Demonstrations` and before `Non-line-of-sight 3D imaging with a single-pixel camera`:

```markdown
| 2019 | [Coherent control of light for non-line-of-sight imaging](https://arxiv.org/abs/1908.04094) — Starshynov et al. | arXiv 2019 | Uses wavefront shaping and speckle-memory-effect scanning to refocus coherent light behind an occluder, improving SNR and demonstrating sub-millimeter active NLOS resolution. |
```

## Website patch

`index.html` is still behind `README.md`: it reports **Updated 4 July 2026** and **53** latest entries, while README now contains later additions. When safely editing the website paper list, update:

- hero eyebrow: `Updated 6 July 2026 · 190+ papers`
- latest count: `62 tracked latest entries` after adding the coherent-control paper and the README entries still missing from the homepage
- footer date: `Last updated: 6 July 2026`
- the three 2026 venue labels that were previously over-claimed in the homepage should remain `arXiv 2026` unless final venue pages are verified:
  - 3D Gaussian Transient Rendering
  - Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling
  - Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals

Add this paper object to `const papers`, near the 2019 active optical entries:

```javascript
{cat:'latest active',title:'Coherent control of light for non-line-of-sight imaging',authors:'Starshynov et al.',year:2019,venue:'arXiv 2019',url:'https://arxiv.org/abs/1908.04094',key:'Wavefront shaping and speckle-memory-effect scanning refocus coherent light behind an occluder, improving SNR and demonstrating sub-millimeter active NLOS resolution.'},
```

The homepage is also still missing the previously surfaced README entries: Zhu 2021 single-photon obscured-corner sensing; Dove 2019 paraxial theory; Reza et al. 2019 wave-like phasor-field demonstrations; Dove & Shapiro 2020 paraxial physical optics; Dove & Shapiro 2020 nonparaxial propagation; Reza et al. 2020 partial-coherence phasor-field statistics; Isogawa et al. 2020 transient sinograms / C2NLOS; and Musarra et al. 2019 single-pixel-camera NLOS.

## Survey-source patch

Add a short sentence in `article/2active.tex` around the active focusing / high-resolution or coherent-control discussion:

```tex
Complementary to computational refocusing, Starshynov \etal used coherent phase control of the outgoing laser wavefront to refocus light behind an occluder and then scanned the focused spot through the speckle memory effect, demonstrating a wavefront-shaping route toward high-SNR, sub-millimeter active NLOS imaging \cite{starshynovCoherentControlNLOS2019}.
```

Update `bare_jrnl.tex` bibliography line to include all supplement files:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The available GitHub connector supports safe UTF-8 text updates but not a safe LaTeX build plus binary PDF replacement path. After the bibliography line and TeX insertion above are applied locally, run LaTeX/BibTeX and upload the regenerated PDF.
