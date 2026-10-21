# 2026-10-22 — Publication recovery status

The five-paper citation backfill and recovery note were published to public `master` at commit `1939d7a36da35bc88bda26563af5456a1f79b5e9` using a SHA-guarded non-force fast-forward. Earlier connector safety blocks were transient; the development branch was verified identical to `master` immediately after publication.

Validated changed files: README.md, index.html, data/papers-source.html, article/2active.tex, egbib_merged_20260711.bib, and updates/2026-10-22-classical-inverse-citation-backfill.md. All five verified papers have matching README, Paper Explorer, survey citations, and BibTeX records. The existing bare_jrnl.tex input graph includes article/2active.tex and the merged bibliography; no main-TeX edit is necessary.

Source publication is complete; rebuild bare_jrnl.pdf from a complete checkout with figures and styles using pdflatex/bibtex/pdflatex/pdflatex, inspect logs, then commit the new PDF. Current PDF remains at blob `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`; it has not been regenerated.
