# Public master recovery — 20 October 2026

The Metasight (SenSys 2023) and accepted MobiCom 2026 RIS demonstration source update is now on public master. The fast-forward was verified at commit `859f191344ae31b06bb6cf2babdc3b0c5a66c0e5`; comparison against `nlos-2026-10-20-metasight-ris-validated-v2` returned ahead 0, behind 0.

Post-merge source audit: 648 unique BibTeX keys, 498 distinct LaTeX citation keys, zero duplicate bibliography keys and zero missing citations. The two studies are represented in README, homepage, Paper Explorer, article/5newscenes.tex and egbib_merged_20260711.bib.

**PDF still pending.** The PDF blob SHA remains `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`. To finish: compile `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex` in a full checkout, verify BibTeX/LaTeX logs and text-extracted new citations, then commit the regenerated PDF. A new Actions workflow creation attempt was blocked; the PDF was not regenerated.

This note supersedes the temporary development-branch status in `updates/2026-10-20-metasight-ris-citation-trace.md`. The recurring literature search remains active.
