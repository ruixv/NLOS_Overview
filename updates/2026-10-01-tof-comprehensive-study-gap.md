# Missing NLOS paper integration note — 2026-10-01

## Verified missing paper

Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, Andreas Velten, **“A comprehensive study of time-of-flight non-line-of-sight imaging,”** arXiv:2603.09548, 2026.

- arXiv: https://arxiv.org/abs/2603.09548
- DBLP currently records the work as CoRR abs/2603.09548 (2026); no final conference/journal venue was verified in this run.
- Repository-wide exact-title search returned no result before staging.

## Why it belongs

This work is unusually relevant to the survey because it places representative ToF NLOS reconstruction families under a common forward-model and hardware framework. It explicitly connects simplified NLOS inverse models to Radon-transform formulations and frequency-domain / phasor-field interpretations, then compares representative methods using the same capture hardware and similar photon budgets. It therefore provides a useful synthesis/reference point linking the Velten-era transient formulation, LCT, f-k migration, and phasor-field families, while highlighting shared resolution, visibility, and noise limitations under controlled hardware conditions.

## Recommended integration

1. **README.md** — add to 2026 / theory-and-benchmarking timeline, categorized as `Active / ToF`, `Theory / Benchmark`, and `Survey / Comparative Study`. Suggested one-line summary: “Unifies representative ToF NLOS methods under a common forward/Radon formulation and controlled hardware comparison, clarifying relationships among spatial-, frequency-, and phasor-domain reconstruction families.”
2. **index.html / Paper Explorer** — add the same metadata and tags; include in Latest Additions if that panel reflects the most recent repository additions rather than publication date alone.
3. **bare_jrnl.tex** — integrate semantically near the discussion that relates ellipsoidal/spherical Radon formulations, LCT, f-k migration, and phasor-field reconstruction. This paper is best used as a synthesis citation rather than appended as a disconnected recent-work item. A suitable literature-review sentence is: “A recent controlled study places representative ToF NLOS methods under a common forward model and acquisition setup, showing that many apparently different spatial-, frequency-, and phasor-domain formulations share closely related resolution, visibility, and noise limitations when evaluated under matched hardware and photon budgets.”
4. **Bibliography** — merge the verified staging entry from `egbib_20261001_tof_comprehensive_study.bib` into the canonical bibliography used by `bare_jrnl.tex`, preserving the repository’s citation-key convention.
5. **PDF** — rebuild `bare_jrnl.pdf` after canonical source/bibliography integration and verify the new citation resolves.

## Consistency / build status

This run intentionally did not overwrite large canonical files without a complete safe read-edit-validation cycle. `README.md`, `index.html`, `bare_jrnl.tex`, the canonical bibliography, and `bare_jrnl.pdf` therefore still require integration/rebuild. The staged BibTeX file and this note are the recoverable handoff for a later run; do not claim the PDF has been regenerated until the build is actually verified.
