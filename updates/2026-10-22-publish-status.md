# 2026-10-22 — Publication recovery status

The verified citation backfill is committed on branch `nlos-2026-10-22-classical-inverse-backfill`, commit `2f5a7bc3de1ef1514cf0e95ad5299527696c36fe`. The branch is ahead of `master` by one commit and behind by zero. The guarded fast-forward to `master` and an attempted pull-request creation were blocked by connector safety checks; no overwrite or forced ref update was attempted.

Validated changed files: README.md, index.html, data/papers-source.html, article/2active.tex, egbib_merged_20260711.bib, and updates/2026-10-22-classical-inverse-citation-backfill.md. All five verified papers have matching README, Paper Explorer, survey citations, and BibTeX records. The existing bare_jrnl.tex input graph includes article/2active.tex and the merged bibliography; no main-TeX edit is necessary.

To publish, verify `master` has not diverged and fast-forward it to the branch head (or merge a PR) without force. Rebuild bare_jrnl.pdf from a complete checkout with figures and styles using pdflatex/bibtex/pdflatex/pdflatex, inspect logs, then commit the new PDF. Current PDF remains at blob `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`; it has not been regenerated.
