# Integration gap: Cascaded Non-Line-of-Sight Imaging

Verified on 2026-10-03.

## Paper
Diego Royo, María Peña, Forrest B. Peterson, Andreas Velten, Julio Marco, Diego Gutierrez, “Cascaded Non-Line-of-Sight Imaging,” arXiv:2609.16017, 2026. No final conference/journal venue was verified in this run, so the venue should remain arXiv until a final publication is confirmed.

Link: https://arxiv.org/abs/2609.16017

## Why it belongs
This is a direct ToF NLOS imaging contribution, not a peripheral citation. It extends conventional third-bounce reconstruction to higher-order transport by reconstructing a virtual impulse response on a hidden wall and cascading a second virtual NLOS system. The paper demonstrates fourth- and fifth-bounce imaging, including multi-corner scenes, analyzes wave-based NLOS propagation through rough hidden walls, and uses multiple hidden walls to recover otherwise unseen views.

## Recommended taxonomy / timeline placement
Active ToF NLOS → wave/phasor-field virtual imaging → higher-order transient transport → cascaded / multi-corner NLOS.

It should be discussed alongside recent higher-order-transport work such as iterative transient light-transport matrices, while distinguishing the goals: TLTM work reconstructs hidden-surface transport itself; Cascaded NLOS uses a reconstructed virtual impulse response to chain NLOS systems and reach additional corners/views.

## Required canonical integration
1. README.md: add a concise 2026 entry under active/transient NLOS and the development timeline.
2. index.html / paper explorer: add title, authors, 2026, arXiv venue, active/ToF and higher-order/multi-corner tags, link, and concise contribution summary.
3. bare_jrnl.tex: integrate semantically in the active ToF / phasor-field / higher-order transport discussion, emphasizing virtual relay propagation and fourth-/fifth-bounce multi-corner imaging rather than appending it as an isolated list item.
4. Canonical bibliography: merge the verified staged entry from `egbib_20261003_cascaded_nlos_gap.bib`, checking the repository's existing citation-key convention first.
5. bare_jrnl.pdf: rebuild only after the canonical TeX/bibliography update and verify citations resolve.
6. Consistency check: search title, `2609.16017`, and the final citation key across README, website, TeX, bibliography, and generated PDF/source artifacts.

## Safety note
The canonical large files were not overwritten in this run because a complete read-edit-build-validation cycle was not available. This note and the staged BibTeX entry preserve the verified update without risking truncation or loss of existing survey content.
