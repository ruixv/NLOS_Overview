# Learned Feature Embeddings citation-tracing and consistency update

Date: 16 July 2026

## Candidate and verification

**Learned Feature Embeddings for Non-Line-of-Sight Imaging and Recognition** — Wenzheng Chen, Fangyin Wei, Kiriakos N. Kutulakos, Szymon Rusinkiewicz, and Felix Heide, ACM Transactions on Graphics 39(6), Proceedings of SIGGRAPH Asia 2020, article 230, DOI `10.1145/3414685.3417825`.

The paper is directly about active transient NLOS imaging rather than an incidental citation. It learns a shared physics-structured representation for hidden-scene reconstruction, classification, and 2.5D detection. Its differentiable pipeline contains transient propagation, visibility, rendering, and depth-estimation components, and its authors provide real-capture reconstruction results, synthetic-to-real detection, code, and datasets.

Metadata was checked against the authors' project/code repository and the published reference list of the original NLOS survey. The paper is also a direct milestone in the learned-reconstruction branch that follows LCT, f-k migration, and phasor-field reconstruction and precedes later physics-guided multi-task networks, masked transient pretraining, transformers, and neural operators.

## Repository gap found

The LaTeX survey already cited the key `chen_learned_2020` in the active-SPAD table and deep-learning narrative, but neither `egbib.bib` nor the consolidated bibliography contained that key. The paper was also absent from README Latest Additions, the website paper explorer, and the public development timeline. This created both an undefined-citation risk and a public-facing consistency gap.

## Intended synchronized changes

- Add canonical BibTeX metadata under the existing citation key `chen_learned_2020`.
- Add one README entry with final ACM TOG / SIGGRAPH Asia 2020 venue and DOI.
- Add one searchable website entry and change the tracked-latest count from 102 to 103.
- Expand the 2020 timeline to record learned multi-task NLOS feature embeddings.
- Replace the survey's short generic description with a dedicated literature-review paragraph in `article/4datadriven.tex`.
- Regenerate the duplicate-free consolidated bibliography and `bare_jrnl.pdf` through the validation workflow.

## Validation requirements

The workflow must fail on undefined citations, missing or repeated BibTeX entries, duplicate README/homepage records, missing generated bibliography text, missing survey narrative in the regenerated PDF, or an incorrect homepage count. It must also render every PDF page to ensure the generated binary is readable.

A pull-request validation pass is used as an independent check before final integration.
