# 2026-07-04 — Partial-coherence phasor-field update

## Search and citation-tracing outcome

This run did not find a newer high-confidence 2026 NLOS imaging paper beyond the current July 2026 frontier list. The useful missing item came from the phasor-field / virtual-wave citation-tracing pass around Liu et al.'s virtual-wave/phasor-field NLOS lineage and the related Reza/Dove/Shapiro theory papers.

## Newly recorded missing paper

**Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier** — Syed Azer Reza, Sebastian Bauer, Andreas Velten, arXiv 2020.

Relevance: this paper is not a new reconstruction benchmark, but it is tightly adjacent to active phasor-field NLOS imaging. It analyzes how partial spatial coherence of the optical carrier creates a spurious signal outside the ideal Huygens-like P-field integral, provides a P-field signal-to-noise figure of merit, and clarifies how aperture roughness and carrier coherence affect practical phasor-field/NLOS implementations.

No reliable final journal/conference venue was verified in this run, so the entry is kept as **arXiv 2020**.

## Repository changes applied

Updated `egbib_20260704_updates.bib` with:

- `rezaPartialCoherencePhasor2020`

Commit: `87aa5062834b761c453bff91b25868c891ed92d1`

## README patch still recommended

Insert the following row near the existing phasor-field theory rows in `README.md`:

```markdown
| 2020 | [Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier](https://arxiv.org/abs/2006.02600) — Reza et al. | arXiv 2020 | Quantifies partial-coherence-induced spurious P-field signals and gives a practical signal-to-noise interpretation for phasor-field NLOS systems under imperfect optical-carrier coherence. |
```

The previous phasor-field theory patch note also recommends adding these three rows, which are already present in the same supplemental BibTeX file but not yet surfaced in README:

```markdown
| 2020 | [Nonparaxial phasor-field propagation](https://arxiv.org/abs/2006.13775) — Dove, Shapiro | arXiv 2020 | Extends paraxial phasor-field theory to Rayleigh--Sommerfeld / nonparaxial propagation, addressing practical NLOS geometries where small-angle Fresnel assumptions break down. |
| 2020 | [Paraxial phasor-field physical optics](https://arxiv.org/abs/2004.14239) — Dove, Shapiro | arXiv 2020 | Shows that phasor-field imaging can be interpreted with physical optics, including focusing and projection through diffusers, rather than only computational propagation. |
| 2019 | [Wave-like Properties of Phasor Fields: Experimental Demonstrations](https://arxiv.org/abs/1904.01565) — Reza et al. | arXiv 2019 | Experimentally demonstrates wave-like P-field behavior and phasor-field optical elements, strengthening the physical basis of virtual-wave NLOS imaging. |
```

`README.md` was not directly overwritten in this run because the available write path is whole-file replacement and the file has been receiving frequent updates. To avoid truncation or accidental loss, the exact insertion rows are recorded here.

## Website patch still recommended

If the four phasor-field theory rows are added to the homepage explorer, increase the latest-entry count accordingly and add paper objects under an active / phasor-field theory category. The current homepage already exposes the July 2026 frontier list, but it still does not surface these phasor-field theory supplements.

## Survey patch still recommended

In `article/2active.tex`, after the current phasor-field paragraph in the wave-based methods subsection, insert a compact sentence such as:

```tex
Subsequent phasor-field theory further clarified this virtual-wave interpretation: Reza \etal~experimentally demonstrated wave-like P-field behavior and phasor-field optical elements~\cite{rezaWaveLikePhasorFields2019}, while later work analyzed the influence of partial optical-carrier coherence on P-field signal-to-noise~\cite{rezaPartialCoherencePhasor2020}; Dove and Shapiro further connected phasor-field imaging to physical-optics implementations~\cite{doveParaxialPhysicalOptics2020} and nonparaxial Rayleigh--Sommerfeld propagation~\cite{doveNonparaxialPhasor2020}.
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The bibliography supplement is ready, but the main survey build still needs `bare_jrnl.tex` to use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates}
```

Then the PDF should be rebuilt locally with LaTeX/BibTeX and uploaded. This run did not claim the PDF was updated.
