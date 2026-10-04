# Integration gap: Cascaded Non-Line-of-Sight Imaging

Verified on 2026-10-03; venue re-verified and corrected on 2026-10-04.

## Paper
Diego Royo, María Peña, Forrest B. Peterson, Andreas Velten, Julio Marco, Diego Gutierrez, “Cascaded Non-Line-of-Sight Imaging,” ACM Transactions on Graphics, 45(6), Article 205, 12 pages, 2026, DOI: 10.1145/3842503. The authors' Graphics and Imaging Lab lists the paper as ACM Transactions on Graphics (Proc. SIGGRAPH Asia 2026), so the final venue supersedes the earlier arXiv-only staging label.

Links: https://doi.org/10.1145/3842503 ; https://arxiv.org/abs/2609.16017 ; https://graphics.unizar.es/projects/CascadedNLOS/

## Why it belongs
This is a direct ToF NLOS imaging contribution, not a peripheral citation. It extends conventional third-bounce reconstruction to higher-order transport by reconstructing a virtual impulse response on a hidden wall and cascading a second virtual NLOS system. The paper demonstrates fourth- and fifth-bounce imaging, including multi-corner scenes, analyzes wave-based NLOS propagation through rough hidden walls, and uses multiple hidden walls to recover otherwise unseen views.

## Recommended taxonomy / timeline placement
Active ToF NLOS → wave/phasor-field virtual imaging → higher-order transient transport → cascaded / multi-corner NLOS.

It should be discussed alongside recent higher-order-transport work such as iterative transient light-transport matrices, while distinguishing the goals: TLTM work reconstructs hidden-surface transport itself; Cascaded NLOS uses a reconstructed virtual impulse response to chain NLOS systems and reach additional corners/views.

## Required canonical integration
1. README.md: add a concise 2026 entry under active/transient NLOS and the development timeline, with venue `ACM TOG (Proc. SIGGRAPH Asia 2026)` rather than arXiv.
2. index.html / paper explorer: add title, authors, 2026, final TOG/SIGGRAPH Asia venue, active/ToF and higher-order/multi-corner tags, DOI/project/arXiv link, and concise contribution summary.
3. bare_jrnl.tex: integrate semantically in the active ToF / phasor-field / higher-order transport discussion, emphasizing virtual relay propagation and fourth-/fifth-bounce multi-corner imaging rather than appending it as an isolated list item.
4. Canonical bibliography: merge the corrected staged entry from `egbib_20261003_cascaded_nlos_gap.bib`, checking the repository's existing citation-key convention first.
5. bare_jrnl.pdf: rebuild only after the canonical TeX/bibliography update and verify citations resolve.
6. Consistency check: search title, DOI `10.1145/3842503`, arXiv `2609.16017`, and the final citation key across README, website, TeX, bibliography, and generated PDF/source artifacts. Do not retain an arXiv-only venue label in public-facing artifacts.

## Safety note
The canonical large files were not overwritten in this run because a complete read-edit-build-validation cycle was not available. This note and the corrected staged BibTeX entry preserve the verified update without risking truncation or loss of existing survey content.
