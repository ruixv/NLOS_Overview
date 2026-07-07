# 2026-07-07 update: optical-coherence recognition README surface sync

## Search / citation-tracing conclusion

Fresh keyword searches around July-2026 NLOS imaging, active transient imaging, phasor-field / virtual-wave optics, coherent NLOS, RF/mmWave NLOS, acoustic NLOS, single-photon LiDAR, and learned reconstruction did not reveal a newer high-confidence frontier paper beyond the entries already surfaced in the README and homepage.

The highest-confidence actionable item was a public-surface consistency gap from the previous optical-coherence recognition pass:

- **Direct Object Recognition Without Line-of-Sight Using Optical Coherence** — Lei, He, Tan, Wang, Wang, Du, Fan, Yu, **arXiv 2019**. This is not a full hidden-scene 3D reconstruction method, but it is a genuine NLOS recognition paper. It uses coherent illumination, diffuse-wall speckle patterns, and a deep neural network to recognize hidden objects without explicitly reconstructing a 3D NLOS scene.

Venue/status decision: only arXiv metadata was verified. No final journal or conference venue was verified, so the entry remains labeled **arXiv 2019**.

## Repository changes made

- Updated `README.md` to surface the Lei et al. optical-coherence NLOS recognition paper in the 2019 latest-additions block, next to coherent-control and single-pixel-camera NLOS entries.
- `egbib_20260707_updates.bib` already contains BibTeX key `leiDirectObjectRecognition2019`.
- `article/2active.tex` already cites `leiDirectObjectRecognition2019` in the active detection / tracking / recognition table.

## Remaining homepage patch

`index.html` was not overwritten in this run because it is a compact hand-maintained HTML/JS file with large minified-like lines. To avoid accidental truncation or formatting damage, apply the following precise patch manually or with a safer diff-based editor.

Add this paper object to the homepage paper explorer / latest additions data:

```js
{
  year: 2019,
  title: "Direct Object Recognition Without Line-of-Sight Using Optical Coherence",
  authors: "Lei et al.",
  venue: "arXiv 2019",
  category: "Active / Recognition / Coherent Speckle",
  url: "https://arxiv.org/abs/1903.07705",
  summary: "Uses coherent illumination and diffuse-wall speckle patterns with a deep neural network for direct hidden-object recognition without reconstructing a full hidden 3D scene."
}
```

If the homepage latest-entry count is manually hard-coded, increment it from **65** to **66** after insertion.

## Survey / PDF status

The survey source is partially consistent:

- `article/2active.tex` already cites `leiDirectObjectRecognition2019` in the active recognition table.
- `egbib_20260707_updates.bib` already provides the BibTeX entry.

The remaining consistency task is still to ensure the master LaTeX build includes all supplement bibliography files. If the active build file still uses only `egbib`, change the bibliography line to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates}
```

`bare_jrnl.pdf` was not regenerated in this run. Remaining commands for a local LaTeX environment are:

```bash
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

After successful compilation, upload/commit the regenerated `bare_jrnl.pdf`. Do not claim the PDF has been updated until the binary is actually replaced.
