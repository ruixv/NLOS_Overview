# 2026-07-07 update: optical-coherence NLOS recognition gap

## Search / citation-tracing conclusion

Fresh keyword search and a citation-tracing-style pass around active NLOS, phasor-field / virtual-wave optics, coherent NLOS, and learned NLOS recognition did not reveal a newer high-confidence July-2026 frontier paper beyond the entries already surfaced in the README and homepage.

However, the pass found one earlier missing paper that is directly relevant to the repository's `Detection, Tracking and Recognition` branch:

- **Direct Object Recognition Without Line-of-Sight Using Optical Coherence** — Lei, He, Tan, Wang, Wang, Du, Fan, Yu, **arXiv 2019**. This work uses coherent illumination and wall-scattered speckle patterns with a deep neural network to recognize hidden objects without explicitly reconstructing a 3D hidden scene. It is not a full NLOS reconstruction method, but it is a genuine NLOS recognition paper and is semantically aligned with the survey's detection/recognition category.

Venue/status decision: only arXiv metadata was verified in this run. No final journal or conference venue was verified, so the entry should be labeled **arXiv 2019**.

## Repository changes made

- Added `egbib_20260707_updates.bib` with BibTeX key:
  - `leiDirectObjectRecognition2019`

## Recommended README patch

Insert the following row in `README.md` within the 2019 block, near `Coherent control of light for non-line-of-sight imaging` and `Non-line-of-sight 3D imaging with a single-pixel camera`:

```markdown
| 2019 | [Direct Object Recognition Without Line-of-Sight Using Optical Coherence](https://arxiv.org/abs/1903.07705) — Lei et al. | arXiv 2019 | Uses coherent illumination and diffuse-wall speckle patterns with a deep neural network for direct hidden-object recognition without reconstructing a full hidden 3D scene. |
```

## Recommended homepage patch

Add a paper object to the `latestPapers` / paper explorer data in `index.html`:

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

If the homepage latest-entry count is manually hard-coded, increment it by one after insertion.

## Recommended survey-source patch

The most appropriate location is `article/2active.tex`, in or near the active NLOS detection / tracking / recognition discussion. Suggested sentence:

```tex
Beyond geometric reconstruction, coherent illumination can also turn the relay wall into a speckle encoder for recognition: Lei \etal used wall-scattered coherent speckle patterns and a deep neural network to directly recognize hidden objects without explicitly reconstructing a 3D NLOS scene \cite{leiDirectObjectRecognition2019}.
```

Then update the bibliography line in `bare_jrnl.tex` to include the new supplement:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The remaining steps are still:

```bash
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

After successful compilation, upload/commit the regenerated `bare_jrnl.pdf`. Do not claim the PDF has been updated until the binary is actually replaced.
