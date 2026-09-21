# Cascaded NLOS final-venue update — 2026-09-22

## Verified metadata correction

**Cascaded Non-Line-of-Sight Imaging** — Diego Royo, María Peña, Forrest B. Peterson, Andreas Velten, Julio Marco, Diego Gutierrez.

- Final venue: **ACM Transactions on Graphics (Proceedings of SIGGRAPH Asia 2026)**
- Volume: **45**, Issue: **6**, Article **205**
- DOI: **10.1145/3842503**
- arXiv: **2609.16017** (useful open-access/preprint link, but no longer the venue label)
- Verification: Universidad de Zaragoza Graphics and Imaging Lab publication page lists the paper as “ACM Transactions on Graphics (Proc. SIGGRAPH Asia 2026)”; the manuscript metadata/DOI identifies TOG 45(6), Article 205.

## Required canonical integration

This corrects the earlier staging/update note that treated the paper as arXiv-only. On the next safe canonical-file edit, update every occurrence consistently:

1. **README.md** — label the paper `ACM Transactions on Graphics (Proc. SIGGRAPH Asia 2026)` rather than `arXiv 2026`; retain the contribution summary emphasizing higher-order (fourth/fifth-bounce) transport, virtual hidden relay walls, and multi-corner imaging.
2. **index.html / paper explorer / latest additions / timeline** — make the same venue correction and add DOI `10.1145/3842503` as the canonical publication link; arXiv may remain as a secondary link.
3. **bare_jrnl.tex** — integrate the work in the active-ToF / phasor-field / higher-order-light-transport discussion. Suggested trajectory: three-bounce transient NLOS → phasor-field virtual-wave propagation → virtual mirrors / higher-order transport → cascaded virtual relay surfaces for fourth/fifth-bounce and two-corner imaging.
4. **Canonical bibliography** — use the verified TOG entry staged in `egbib_20260922_cascaded_nlos_tog_siggraph_asia.bib`; do not cite it as `@misc`/arXiv when describing the final publication.
5. **bare_jrnl.pdf** — rebuild only after the source and bibliography are safely integrated; verify the PDF contains the corrected TOG/SIGGRAPH Asia citation.

## Consistency note

Do not claim the public artifacts or PDF are synchronized until README, website, survey source, canonical bibliography, and rebuilt PDF have all been checked. This file is a safe patch note because the large canonical files were not overwritten from partial payloads in this run.
