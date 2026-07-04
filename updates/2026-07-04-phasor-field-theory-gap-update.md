# 2026-07-04 — Phasor-field theory and experimental-demo gap update

## Search and citation-tracing outcome

This run did not find a newer high-confidence 2026 NLOS imaging paper beyond the current July 2026 frontier list. The useful gap came from citation tracing around the phasor-field / virtual-wave lineage. The README already contained the paraxial phasor-field theory entry, but several closely adjacent theory and experimental-demonstration papers were not explicitly represented in the public latest list or supplemental bibliography.

## Newly recorded missing papers

1. **Wave-like Properties of Phasor Fields: Experimental Demonstrations** — Syed Azer Reza, Marco La Manna, Sebastian Bauer, Andreas Velten, arXiv 2019.  
   Relevance: validates the optical-wave analogy of phasor fields experimentally and introduces phasor-field optical elements, making it a useful bridge between the original virtual-wave model and later physical-/computational-optics treatments.

2. **Paraxial phasor-field physical optics** — Justin Dove, Jeffrey H. Shapiro, arXiv 2020.  
   Relevance: proves that P-field imaging can in principle be performed with ordinary physical optics, including focusing/projecting P-fields through diffusers, rather than only computational backpropagation.

3. **Nonparaxial phasor-field propagation** — Justin Dove, Jeffrey H. Shapiro, arXiv 2020.  
   Relevance: extends the paraxial P-field theory toward Rayleigh--Sommerfeld / nonparaxial propagation, which is important because many practical reflective NLOS geometries violate the small-angle paraxial assumptions.

No reliable final journal/conference venue was verified for these three entries in this run, so they are kept as **arXiv 2019/2020** rather than upgraded to a final venue.

## Repository changes applied

- Updated `egbib_20260704_updates.bib` with:
  - `rezaWaveLikePhasorFields2019`
  - `doveParaxialPhysicalOptics2020`
  - `doveNonparaxialPhasor2020`

Commit: `f58cec37231498d8b8bf3a883edf06bc7489147c`

## README patch still recommended

Insert the following rows near the existing phasor-field theory rows in `README.md`:

```markdown
| 2020 | [Nonparaxial phasor-field propagation](https://arxiv.org/abs/2006.13775) — Dove, Shapiro | arXiv 2020 | Extends paraxial phasor-field theory to Rayleigh--Sommerfeld / nonparaxial propagation, addressing practical NLOS geometries where small-angle Fresnel assumptions break down. |
| 2020 | [Paraxial phasor-field physical optics](https://arxiv.org/abs/2004.14239) — Dove, Shapiro | arXiv 2020 | Shows that phasor-field imaging can be interpreted with physical optics, including focusing and projection through diffusers, rather than only computational propagation. |
| 2019 | [Wave-like Properties of Phasor Fields: Experimental Demonstrations](https://arxiv.org/abs/1904.01565) — Reza et al. | arXiv 2019 | Experimentally demonstrates wave-like P-field behavior and phasor-field optical elements, strengthening the physical basis of virtual-wave NLOS imaging. |
```

`README.md` was not directly overwritten in this run because the available write path is whole-file replacement and the file has been receiving frequent concurrent-style updates. To avoid truncation or accidental loss, the precise insertion is recorded here.

## Website patch still recommended

- Increase latest-entry count from `53` to `56` if these three entries are added to the homepage explorer.
- Add the same three paper objects to `index.html` under the active / phasor-field category.
- Update the 2019 and 2020 timeline text to mention phasor-field experimental validation, physical optics, and nonparaxial theory if a short narrative expansion is desired.

## Survey patch still recommended

In `article/2active.tex`, after the current sentence discussing phasor-field methods in the wave-based model subsection, insert a compact sentence such as:

```tex
Subsequent phasor-field theory further clarified this virtual-wave interpretation: Reza \etal~experimentally demonstrated wave-like P-field behavior and phasor-field optical elements~\cite{rezaWaveLikePhasorFields2019}, while Dove and Shapiro analyzed both physical-optics implementations~\cite{doveParaxialPhysicalOptics2020} and nonparaxial Rayleigh--Sommerfeld propagation~\cite{doveNonparaxialPhasor2020}, reducing the gap between idealized virtual-wave propagation and practical wide-angle reflective NLOS geometries.
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The bibliography supplement is ready, but the main survey build still needs `bare_jrnl.tex` to use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates}
```

Then the PDF should be rebuilt locally with LaTeX/BibTeX and uploaded. This run did not claim the PDF was updated.
