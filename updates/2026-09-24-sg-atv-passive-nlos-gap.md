# NLOS literature gap: SG-ATV passive NLOS (2026-09-24)

## Verified missing paper

Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, and Guorong Sui, “Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging,” *Optics Express*, 34(3), 5210–5224, 2026. DOI: 10.1364/OE.587111.

Repository-wide searches for the full title and DOI returned no hit before staging.

## Why it belongs

This is genuine passive optical NLOS imaging using a conventional color camera and an experimentally measured optical transport matrix. SG-ATV derives spatially varying TV weights from a preliminary reconstruction, dynamically adapting regularization to local structure instead of requiring manually tuned fixed TV parameters. It is a useful optimization-based counterpoint to the repository’s learned passive-NLOS line: it emphasizes interpretable, scene-adaptive priors rather than large-scale training.

The paper explicitly situates itself against field-defining NLOS work including Saunders et al. computational periscopy, O’Toole et al. LCT, Velten et al. 2012, Liu et al. phasor fields, and the broader active/passive literature, so it is tightly within the NLOS lineage rather than an incidental citation.

## Integration plan

- **README.md**: add under Passive NLOS / computational reconstruction, venue `Optics Express 2026`; concise contribution: parameter-free structure-guided adaptive TV for conventional-camera passive NLOS, with spatially varying regularization derived from preliminary reconstructions.
- **Development timeline (2026)**: place on the passive/optimization branch, after classical transport-matrix/regularized inversion and alongside recent physics-aware passive reconstruction. Suggested trajectory: fixed-prior passive inversion → learned passive reconstruction → self-adaptive interpretable regularization.
- **index.html / Paper Explorer / Latest Additions**: add title, authors, Optics Express 2026, DOI, tags `Passive`, `Optimization`, `Total Variation`, `Conventional Camera`, `Physics/Structure Prior`.
- **bare_jrnl.tex**: integrate semantically in the passive computational-NLOS / inverse-problem discussion, not as an isolated list item. A suitable literature-review point is that recent work revisits optimization-based passive NLOS with scene-adaptive structural priors, reducing dependence on hand-tuned regularization while retaining physical interpretability; cite `zhang2026sgatv`.
- **Bibliography**: merge the staged entry in `egbib_20260924_sg_atv_passive_nlos.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- **bare_jrnl.pdf**: rebuild only after the canonical source and bibliography are safely integrated; do not claim the PDF is updated until compilation and upload are verified.

## Verification sources

- Optica, *Optics Express* 34(3) table of contents: title/authors/pages.
- PubMed PMID 41715541: final journal metadata, pages 5210–5224, DOI 10.1364/OE.587111, and abstract.

## Safety note

This staging note is intentional: do not replace large canonical files from truncated/partial connector payloads. Integrate through complete-file reads/current blob SHAs or a guarded branch, then compile and verify cross-artifact consistency.
