# 6 July 2026 — occlusion-based active NLOS gap update

## Search / citation-tracing result

A fresh pass over active optical NLOS, phasor-field / virtual-wave NLOS, passive periscopy, single-photon ToF NLOS, RF/mmWave/RIS NLOS sensing, acoustic NLOS, consumer LiDAR, transient transformers, and differentiable transient rendering did not reveal a newer high-confidence July 2026 frontier paper beyond the already tracked 2026 arXiv entries.

However, citation-tracing around the early active-ToF NLOS and occlusion-aware inverse-imaging papers surfaced two older, direct active NLOS imaging papers that are not currently surfaced in `README.md` or `index.html`:

1. **Non-line-of-sight Imaging with Partial Occluders and Surface Normals** — Felix Heide, Matthew O'Toole, Kai Zang, David B. Lindell, Steven Diamond, Gordon Wetzstein, **arXiv 2017**, <https://arxiv.org/abs/1711.07134>.
   - Direct active NLOS reconstruction paper.
   - Introduces a factored NLOS light-transport representation that models hidden-surface partial occlusion and surface normals, addressing limitations of isotropic / no-occlusion hidden-scene assumptions.
   - No final journal/conference venue was verified in this run, so label as **arXiv 2017** until reliable publisher metadata is found.

2. **Exploiting Occlusion in Non-Line-of-Sight Active Imaging** — Christos Thrampoulidis, Gal Shulkind, Feihu Xu, William T. Freeman, Jeffrey H. Shapiro, Antonio Torralba, Franco N. C. Wong, Gregory W. Wornell, **arXiv 2017**, <https://arxiv.org/abs/1711.06297>.
   - Direct active NLOS imaging / sensing paper.
   - Shows that natural occluders in the hidden scene can encode useful information and may reduce reliance on time-resolved transient measurements.
   - No final journal/conference venue was verified in this run, so label as **arXiv 2017** until reliable publisher metadata is found.

These are not new frontier papers, but they fill an important historical gap between early transient NLOS reconstruction, occlusion-aware passive periscopy, and later arbitrary-relay / sparse-acquisition methods.

## Files updated safely

- `egbib_20260706_updates.bib`
  - Added `heidePartialOccludersNormals2017`.
  - Added `thrampoulidisExploitingOcclusion2017`.
  - Commit: `c6960dc18109fab0553a91634f673300522180dc`.

## README patch

Insert these rows in `README.md` under **Latest Additions**, near the bottom of the table after the 2019 entries, or add a small `2017` block before the table ends:

```markdown
| 2017 | [Non-line-of-sight Imaging with Partial Occluders and Surface Normals](https://arxiv.org/abs/1711.07134) — Heide et al. | arXiv 2017 | Introduces a factored active-NLOS light-transport model that accounts for hidden-surface partial occlusions and surface normals, improving fidelity beyond isotropic no-occlusion assumptions. |
| 2017 | [Exploiting Occlusion in Non-Line-of-Sight Active Imaging](https://arxiv.org/abs/1711.06297) — Thrampoulidis et al. | arXiv 2017 | Shows that hidden-scene occluders can encode useful active-NLOS information and may reduce reliance on expensive time-resolved transient hardware. |
```

## Website patch

`index.html` remains behind the latest README / update-log state. When safely editing the homepage, apply the previously noted metadata fixes and add these two objects near the early active optical entries:

```javascript
{cat:'latest active',title:'Non-line-of-sight Imaging with Partial Occluders and Surface Normals',authors:'Heide et al.',year:2017,venue:'arXiv 2017',url:'https://arxiv.org/abs/1711.07134',key:'Factored active-NLOS light transport with hidden-surface partial occlusions and surface normals.'},
{cat:'latest active',title:'Exploiting Occlusion in Non-Line-of-Sight Active Imaging',authors:'Thrampoulidis et al.',year:2017,venue:'arXiv 2017',url:'https://arxiv.org/abs/1711.06297',key:'Uses natural hidden-scene occluders as informative structure for active NLOS imaging without requiring conventional dense time-resolved acquisition.'},
```

The homepage should also still be synchronized with the README entries already missing from the `const papers` list, including the single-pixel camera, single-photon obscured-corner sensing, phasor-field theory follow-ups, C2NLOS transient sinograms, coherent-control NLOS, and quantized-RIS RCS entries.

## Survey-source patch

Semantically, these belong in the active optical / physical-model discussion, near early ToF formulations, occlusion-aware forward models, and assumptions on hidden-surface visibility / normals. Add a sentence such as:

```tex
Early active NLOS work also began to relax the simplifying assumptions of isotropic, unoccluded hidden scattering. Heide \etal introduced a factored transient light-transport model that explicitly accounts for hidden-surface partial occlusions and surface normals, while Thrampoulidis \etal showed that occluders themselves can provide informative structure for active NLOS reconstruction without relying exclusively on dense time-resolved acquisition~\cite{heidePartialOccludersNormals2017,thrampoulidisExploitingOcclusion2017}.
```

Update `bare_jrnl.tex` bibliography line to include all supplement files:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The available GitHub connector supports safe UTF-8 text updates, but there is still no safe LaTeX build plus binary PDF replacement path here. Rebuild locally after applying the TeX/source patches and upload the regenerated PDF.

## Excluded candidates

General NLOS wireless-channel / communications papers, thermal-light-source papers, and privacy/side-channel papers using the term NLOS were excluded because they are not hidden-scene imaging, NLOS sensing, or tightly adjacent reconstruction papers.
