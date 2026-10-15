# 2026-10-15 bibliography and survey consistency repair

## Scope
Citation tracing and a DOI-level audit against the README, website paper explorer, and all included LaTeX chapters found no independently verified new 2026 core imaging paper in this pass. It did identify seven **already-listed and already-cited** papers whose survey BibTeX still used outdated preprint records or incorrect DOI/author/page metadata. Existing citation keys were deliberately retained.

## Verified bibliography corrections
- `seidelTwoDimensionalNonLineofSightScene2020`: IEEE TCI **7, 58–72 (2021)**; DOI **10.1109/TCI.2020.3037405** (Boston University / DBLP).
- `chenHyperNLOS2024`: *Optics Express* **32(20), 34807–34824 (2024)**; DOI **10.1364/OE.532699**; publisher-indexed author list (PubMed / OpenAlex).
- `yeRealTimeNLOS2024`: *Nature Computational Science* **4(12), 920–927 (2024)**; DOI **10.1038/s43588-024-00722-4**; author list corrected (Nature / PubMed).
- `yePnPDynamic2024`: *ACM TOG* **43(5), Article 155 (2024)**; DOI **10.1145/3665139**; author list corrected (ACM article PDF / scholarly index).
- `shenMARMOT2025`: *Visual Intelligence* **4, Article 22 (2026)**; DOI **10.1007/s44267-026-00125-1**; final author list (Springer).
- `shiN2LoS2025`: *IEEE TMC* **25(5), 6002–6016 (2026)**; DOI **10.1109/TMC.2025.3634623**; final seven authors (Lingnan Scholars).
- `youngNavigationNLOS2024`: *IEEE ICRA* **2025, 4907–4914**; DOI **10.1109/ICRA55743.2025.11128292** (Stony Brook University).

## Survey prose
`article/4datadriven.tex` now cites `yuePermutationTransientAttention2024` in the graph/temporal-attention reconstruction discussion. This 2024 COSI conference-digest paper was already in README, paper explorer, and bibliography but lacked an explicit survey citation. It is identified as a preliminary conference contribution, not a full benchmark paper.

## Cross-artifact notes
README and `data/papers-source.html` already use the correct final DOIs/venues for these papers; they are intentionally unchanged. `bare_jrnl.tex` includes the revised survey chapter through `\\input{article/4datadriven.tex}`. Citation keys are preserved to avoid breaking historical references.

## PDF status — not rebuilt
`bare_jrnl.pdf` is **stale** and has not been compiled or uploaded by this run. The container cannot resolve github.com to retrieve the full repository and binary assets; the connected GitHub read API does not provide a full binary checkout. After a full checkout, run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`, check `bare_jrnl.log`/`bare_jrnl.blg` for missing/duplicate citations, and commit the newly generated PDF. Do not mark the PDF synchronized until its blob changes and build succeeds.
