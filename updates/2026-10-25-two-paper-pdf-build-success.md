# 25 October 2026: verified PDF rebuild after two-paper backfill

A new **71-page `bare_jrnl.pdf`** was cleanly built and committed after the FDDA and neural transient-field additions (GitHub Actions run [#40154349930](https://github.com/ruixv/NLOS_Overview/actions/runs/40154349930), conclusion **success** on 25 October 2026 at 02:27 UTC).

- Source commit: `baf6d5e7a23e06c9b141fb9a18d789e83930a45d`, containing both paper additions.
- Binary rebuild commit: `8d5fef20dd6b367bed85edc23f8aca8e00094ea0`.
- New PDF Git blob SHA: `ed849672a716cccdbd054ad48092ab13cfb2b929` (2,389,853 bytes), changed from previous `b934e8318f17e5e0034f3872c66bae5c89821a59`.
- GitHub Actions `Clean-build survey`, `Validate survey`, and `Commit regenerated PDF` all succeeded. Build log: `Output written on bare_jrnl.pdf (71 pages, 2389853 bytes)`; `pdfinfo`, `pdftotext`, and missing-citation checks passed.
- Public PDF: https://ruixv.github.io/NLOS_Overview/bare_jrnl.pdf.
- The author-maintained PDF extension is **not separately peer reviewed**; the APSIPA TSIP 2022 article remains the original peer-reviewed survey.
- Bibliography and survey source audit after both papers: **669 unique BibTeX entries**, **525 distinct cited keys**, **0 missing citations**, **0 duplicate entries**. Website explorer: **398 unique paper records** and **371 Latest entries**, with valid inline JavaScript.
- New papers: Yang et al. JEI 2026 DOI 10.1117/1.JEI.35.5.053013; Xu et al. ICCPA/SPIE 2026 DOI 10.1117/12.3120476.
- The previous source update notes correctly mark their pre-rebuild status; this note records the completed resolution.

No LaTeX source change is made by this status-only update.
