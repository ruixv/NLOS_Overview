# 2026-08-29 — Symmetry-aware gradient coordination NLOS gap

## Verified missing paper

Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang, **“Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging,”** *Symmetry*, vol. 18, no. 5, article 711, 2026. DOI: `10.3390/sym18050711`.

Publisher metadata: published 23 April 2026. This is a final journal publication, not an arXiv-only entry.

## Why it belongs

This is a direct transient NLOS reconstruction paper rather than a paper that merely cites NLOS in passing. It studies physics-guided NLOS training under low-SNR transient measurements and treats heterogeneous reconstruction, measurement-consistency, Poisson-statistics, and sensor-calibration objectives as a gradient-coordination problem. The method combines PCGrad-style conflict projection, PhysGuard hard routing, learnable IRF/gain/background calibration, and staged freeze–unfreeze training. The paper reports improved held-out reconstruction quality over its LPP-style baseline and qualitative validation on seven real captured scenes. It explicitly evaluates within an NLOST-style benchmark/protocol, making it tightly connected to the repository's learned transient-reconstruction lineage.

## Repository check

Repository searches for the exact title and DOI `10.3390/sym18050711` returned no matches, so this is a genuine corpus gap at the time of this update.

## Safe integration targets

The current GitHub connector replaces whole UTF-8 files rather than applying line-level patches. Because README.md, the website corpus, and the survey sources are large and have accumulated many recent edits, do **not** overwrite them from partial fetches. Integrate this entry in the next guarded full-source edit as follows.

### README.md

Add to **Latest Additions** (2026) and the learned/physics-guided NLOS timeline. Suggested concise summary:

> Coordinates conflicting reconstruction, physical-consistency, and sensor-calibration gradients instead of scalarizing them into one loss; combines PCGrad, PhysGuard routing, staged calibration, and low-SNR transient supervision, with qualitative validation on seven real captures.

Recommended category: **Deep Learning for NLOS / Physics-guided reconstruction** rather than hardware or new-modality sensing.

### Website / Paper Explorer

Add the same paper to the canonical paper data source used by `index.html` / Paper Explorer, with tags such as `active`, `transient`, `learned reconstruction`, `physics-guided`, `low-SNR`, `sensor calibration`, `NLOST`. Add a 2026 timeline node only if the website timeline already represents methodological optimization advances at this granularity.

### Survey LaTeX

Integrate into the semantically appropriate learned/physics-guided reconstruction section (likely the data-driven / deep-learning section rather than only appending to a recent-paper list). Suggested literature-review sentence:

> Recent work has also shifted attention from adding physical priors as scalar loss terms to coordinating their optimization dynamics: Ling *et al.* \cite{lingSymmetryAwareNLOS2026} route conflicting reconstruction, measurement-consistency, and sensor-calibration gradients separately, improving low-SNR generalization while retaining explicit transient-physics constraints.

This paper is useful for the trajectory **physics-inspired architecture → learnable sensor/forward models → optimization-level governance of heterogeneous physical constraints**.

### Bibliography

Merge the staged entry from `egbib_20260829_symmetry_gradient_coordination_gap.bib` into the canonical BibTeX source used by `bare_jrnl.tex`, preserving key `lingSymmetryAwareNLOS2026` unless a repository naming collision exists.

### PDF rebuild and consistency checks

After the guarded source integration:

1. clean auxiliary files;
2. run the repository's normal `pdflatex → bibtex → pdflatex → pdflatex` (or equivalent) build;
3. verify `lingSymmetryAwareNLOS2026` resolves in `.aux/.bbl`;
4. confirm the DOI appears exactly once in the canonical bibliography;
5. verify README, website/Paper Explorer, survey prose, canonical `.bib`, and regenerated `bare_jrnl.pdf` all contain the same final venue metadata;
6. visually inspect the PDF page containing the added learned-reconstruction paragraph and bibliography entry.

## Current-run limitation

`bare_jrnl.pdf` was **not** regenerated in this run. This note intentionally stages an exact, metadata-verified patch rather than risking truncation or loss of accumulated edits in large public-facing files.
