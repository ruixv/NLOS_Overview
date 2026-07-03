# 2026-07-03 Neural implicit NLOS surface sync

## Added / corrected papers

This run focused on forward-citation and keyword tracing around Neural Transient Fields and neural implicit NLOS reconstruction. Two relevant missing or partially synchronized papers were identified:

1. **NLOS-NeuS: Non-line-of-sight Neural Implicit Surface** — Fujimura, Kushida, Funatomi, Mukaigawa, arXiv 2023.
   - Citation-tracing rationale: directly extends Neural Transient Fields (NeTF) to SDF-based neural implicit surface reconstruction.
   - Metadata decision: no reliable final conference/journal venue was verified in this run, so the public entry should be labeled **arXiv 2023** rather than ICCV.
   - Integration status: README latest entry added; BibTeX key `fujimuraNLOSNeuS2023` added. `article/4datadriven.tex` already discusses and cites this work in the neural implicit surfaces paragraph.

2. **Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction** — Grau, Plack, Haehn, Weinmann, Hullin, arXiv 2022.
   - Citation-tracing rationale: directly adjacent neural implicit NLOS surface reconstruction work; uses an implicit representation to unify recoverability and reconstruction for hidden surfaces, including self-occlusion and geometry beyond conservative Fermat-path recoverability.
   - Metadata decision: no reliable final conference/journal venue was verified in this run, so the public entry is labeled **arXiv 2022**.
   - Integration status: README latest entry added; BibTeX key `grauOcclusionFields2022` added.

## Files updated

- `README.md`
  - Added `NLOS-NeuS` to 2023 Latest Additions.
  - Added `Occlusion Fields` to 2022 Latest Additions.
- `egbib_20260703_updates.bib`
  - Added `fujimuraNLOSNeuS2023`.
  - Added `grauOcclusionFields2022`.

## Recommended follow-up patch for `article/4datadriven.tex`

`article/4datadriven.tex` already contains the NLOS-NeuS paragraph. To integrate Occlusion Fields without overwriting the whole file, extend the neural implicit surfaces paragraph as follows:

```tex
\noindent \textbf{Neural implicit surfaces.}
Extending the neural transient field (NeTF)~\cite{shenNonlineofsightImagingNeural2021} to surface representations, Fujimura~\etal~proposed NLOS-NeuS~\cite{fujimuraNLOSNeuS2023}, which represents the hidden scene as a neural implicit surface via a signed distance function (SDF). By introducing SDF constraints based on first-returning photon geometry and volume rendering, NLOS-NeuS reconstructs smooth and detailed 3D surfaces without voxel resolution limitations, representing a major step towards high-fidelity 3D NLOS scene understanding. In parallel, Grau~\etal~introduced Occlusion Fields~\cite{grauOcclusionFields2022}, an implicit surface representation that couples NLOS recoverability with reconstruction and can infer adaptively tessellated hidden surfaces under self-occlusion, extending the neural-implicit line beyond voxel occupancy toward explicit surface geometry and visibility reasoning.
```

## Recommended follow-up patch for `index.html`

The homepage currently lists NLOS-NeuS in the paper explorer as `ICCV` with an empty URL. Because no final venue was verified, change that entry to:

```js
{cat:'latest learning active', title:'NLOS-NeuS: Non-Line-of-Sight Neural Implicit Surface', authors:'Fujimura et al.', year:2023, venue:'arXiv 2023', url:'https://arxiv.org/abs/2303.12280', key:'Extends Neural Transient Fields to SDF-based neural implicit surfaces with first-returning-photon constraints for smooth hidden-surface reconstruction.'},
```

and add:

```js
{cat:'latest learning active', title:'Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction', authors:'Grau et al.', year:2022, venue:'arXiv 2022', url:'https://arxiv.org/abs/2203.08657', key:'Implicit surface representation for NLOS recoverability, self-occlusion, and adaptively tessellated hidden-surface reconstruction.'},
```

The homepage latest-entry count should be incremented after applying these objects. I did not overwrite `index.html` in this run because it is a hand-maintained HTML/JS file and the available GitHub write action requires whole-file replacement.

## PDF status

`bare_jrnl.pdf` was not regenerated. Source-side BibTeX is updated, but the main file still needs to use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates}
```

Then run local LaTeX/BibTeX compilation and upload the regenerated PDF. The current tool path does not provide safe LaTeX compilation or binary PDF upload.
