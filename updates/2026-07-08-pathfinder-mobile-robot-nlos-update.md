# 2026-07-08 update: PathFinder mobile-robot NLOS tracking gap

## Search conclusion

Fresh keyword search and citation-tracing-style checks did not reveal a newer high-confidence July 2026 frontier NLOS imaging paper beyond the README's current 2026 entries such as arbitrary-relay 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, DENALI, GeRaF 2.0, RIS/radar, and distributed MIMO/ISAC items.

However, a missing 2024 data-driven / robotic NLOS tracking paper was found:

- **PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot** — Shenbagaraj Kannapiran, Sreenithy Chandran, Suren Jayasuriya, Spring Berman, **arXiv 2024**.  
  Link: https://arxiv.org/abs/2404.05024  
  Reason to include: directly addresses NLOS perception with a moving standard RGB camera on a small mobile robot / drone, estimating the 2D trajectory of a hidden moving person in Manhattan-world environments using an attention-based network and a plane-selection metric. It is not full 3D transient reconstruction, but it is tightly within the repository's detection/tracking/recognition and robotic NLOS-perception scope.

No final conference/journal venue was verified in this run, so the conservative label is **arXiv 2024**.

## Repository updates completed

Updated `egbib_20260708_updates.bib` with:

```bibtex
@misc{kannapiranPathFinder2024,
  title   = {PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot},
  author  = {Kannapiran, Shenbagaraj and Chandran, Sreenithy and Jayasuriya, Suren and Berman, Spring},
  year    = {2024},
  eprint  = {2404.05024},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/2404.05024}
}
```

## README patch still needed

Insert this row in `README.md` under **Latest Additions**, in the 2024 block near Event-enhanced Passive NLOS and Low-Cost / Robotic NLOS entries:

```markdown
| 2024 | [PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot](https://arxiv.org/abs/2404.05024) — Kannapiran et al. | arXiv 2024 | Uses a standard RGB camera on a mobile robot / drone and an attention-based network to track hidden moving people from ordinary LOS videos, connecting passive NLOS cues to low-cost robotic perception. |
```

Suggested update line:

```markdown
**Update run: 8 July 2026.** This section tracks newly found or newly completed entries that were not explicitly covered in the previous README / homepage snapshot.
```

## Homepage / index.html patch still needed

`index.html` currently still shows `Updated 7 July 2026` and `65 tracked latest entries`, while README already has the 8 July 2026 additions. With Sadhu 2021, Yi 2022, Choi 2023, Lei 2019, and this PathFinder 2024 object, the homepage latest count should be updated from **65** to **70**.

Insert the following object into the `papers` array near the 2024 passive/robotic entries:

```js
{cat:"latest passive learning modality",title:"PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot",authors:"Kannapiran et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2404.05024",key:"Standard RGB camera on a mobile robot / drone plus attention-based sequence modeling for dynamic hidden-person tracking in ordinary LOS videos."},
```

Also update the header/footer strings:

```html
Updated 8 July 2026 · 190+ papers
Last updated: 8 July 2026
```

## Survey-source patch still needed

A natural insertion point is `article/5newscenes.tex`, subsection **Robotic Exploration with NLOS Perception**, after the paragraph discussing Young et al. and SuperEx.

Suggested sentence:

```tex
PathFinder~\cite{kannapiranPathFinder2024} complements these active single-photon-LiDAR systems from the passive/mobile side: instead of reconstructing a dense hidden volume, it uses a standard RGB camera mounted on a small mobile robot or drone, selects informative vertical relay planes, and applies attention-based temporal modeling to estimate the 2D trajectory of a hidden moving person. This line suggests that robotic NLOS perception may be useful even when the system only needs task-level hidden-state estimates such as motion or position, rather than metrically complete 3D reconstructions.
```

## Bibliography / PDF status

`egbib_20260708_updates.bib` now contains the PathFinder BibTeX key. `bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

It should be changed to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

`bare_jrnl.pdf` was not regenerated in this run. After the survey-source and bibliography-line updates, rebuild locally with LaTeX/BibTeX and upload the resulting PDF.

## Safety note

I did not overwrite `README.md`, `index.html`, or `article/5newscenes.tex` through a whole-file replacement because the current safe write path is still complete-file replacement and these files contain dense hand-maintained Markdown / HTML-JS / LaTeX content. The exact patches above are provided to avoid truncation or formatting loss.
