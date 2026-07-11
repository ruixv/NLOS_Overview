# Virtual light transport matrix citation-tracing update (11 July 2026)

## Search result

Fresh July 2026 keyword searches did not reveal a newer high-confidence frontier paper beyond the current repository entries. A high-priority citation/reference-tracing pass did, however, identify one direct and previously missing extension of the phasor-field milestone literature:

- **Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging** — Julio Marco, Adrian Jarabo, Ji Hyun Nam, Xiaochun Liu, Miguel Ángel Cosculluela, Andreas Velten, and Diego Gutierrez, arXiv:2103.12622 (2021).

The paper explicitly builds on phasor-field virtual-wave optics. Instead of using the virtual camera only to reconstruct hidden geometry, it constructs virtual projector-camera pairs and estimates a hidden-scene light transport matrix. The resulting representation supports computational relighting and separates direct, first-order indirect, and higher-order indirect transport in cluttered hidden scenes. It is therefore genuinely NLOS light-transport imaging/analysis rather than a paper that cites NLOS work only in passing.

No final conference or journal venue could be verified from the arXiv record, publisher searches, or project/lab-page searches, so the repository conservatively labels it **arXiv 2021**.

Primary source: https://arxiv.org/abs/2103.12622

## Repository comparison before integration

The title, arXiv identifier, and proposed citation key were absent from:

- `README.md`
- `index.html`
- `article/2active.tex`
- `egbib_merged_20260711.bib`

The paper is semantically placed in the wave-based / phasor-field part of the active-NLOS survey because it extends virtual-wave reconstruction into hidden light-transport analysis.

## Intended synchronized changes

1. Add the paper to the README latest-additions table as an active optical NLOS work.
2. Add a searchable homepage object and update the tracked-latest count from 83 to 84.
3. Extend the 2021 timeline milestone with virtual hidden-scene transport matrices.
4. Add a short literature-review paragraph after the core phasor-field discussion in `article/2active.tex`.
5. Add `marcoVirtualLightTransport2021` to a dated BibTeX supplement and rebuild the duplicate-free merged bibliography.
6. Clean-build and validate `bare_jrnl.pdf`, checking the generated PDF text for both the survey paragraph and the complete paper title.

**Build result:** successful clean LaTeX/BibTeX rebuild. README, homepage, survey source, duplicate-free merged bibliography, and `bare_jrnl.pdf` are now synchronized. `pdfinfo`/`pdftotext` passed, no undefined or repeated citation records were detected, and the virtual light-transport source, citation key, and compiled bibliography record were verified (latexmk exit code 0).
