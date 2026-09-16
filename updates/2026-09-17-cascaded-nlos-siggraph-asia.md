# 2026-09-17 — Cascaded NLOS / SIGGRAPH Asia 2026

## Newly verified missing paper

Diego Royo, María Peña, Forrest B. Peterson, Andreas Velten, Julio Marco, and Diego Gutierrez, **“Cascaded Non-Line-of-Sight Imaging,” ACM Transactions on Graphics (Proc. SIGGRAPH Asia 2026)**, 2026. Preprint: arXiv:2609.16017.

The authors’ Graphics and Imaging Lab publication page explicitly identifies the final venue as ACM Transactions on Graphics (Proc. SIGGRAPH Asia 2026), so this entry should not be labeled merely as arXiv.

## Why it matters

Most transient NLOS reconstruction assumes three-bounce transport through one visible relay wall. Cascaded NLOS computes a virtual impulse response at a hidden wall from a captured visible-wall impulse response, effectively concatenating another virtual NLOS imaging stage. This exploits fourth- and fifth-bounce transport, reconstructs objects with difficult orientations and objects hidden around two corners, and uses multiple hidden walls to obtain alternative virtual viewpoints. The paper also analyzes the interaction between wave-based NLOS imaging and rough hidden walls.

This is a direct continuation of the higher-order / virtual-mirror branch of transient NLOS and is strongly connected to the Velten / phasor-field lineage rather than a paper that merely cites NLOS work in passing.

## Required integration

- **README.md / Latest Additions:** add as a 2026 active transient NLOS paper. Suggested summary: “Cascades virtual NLOS stages by synthesizing an impulse response at hidden relay walls, exploiting fourth- and fifth-bounce transport to image challenging orientations and objects around two corners; also analyzes rough hidden-wall visibility and multi-view reconstruction.”
- **README.md / Milestone Timeline:** place after Virtual Mirrors / higher-order transport and alongside the 2026 TLTM work as a milestone in moving beyond conventional three-bounce transport.
- **Website (`index.html`, Paper Explorer, latest additions, timeline):** add under Active / Transient / Higher-order light transport / Multi-corner NLOS; final venue = ACM TOG (Proc. SIGGRAPH Asia 2026).
- **Survey LaTeX:** integrate semantically in the active NLOS / phasor-field / higher-order transport discussion, not as a detached recent-work list. Recommended narrative: “Recent work further extends virtual-wave NLOS beyond a single hidden relay: Cascaded NLOS synthesizes a virtual impulse response at a hidden wall and recursively applies an additional NLOS stage, thereby exploiting fourth- and fifth-bounce paths for difficult surface orientations and multi-corner scenes.”
- **Bibliography:** merge `egbib_20260917_cascaded_nlos_siggraphasia.bib` into the bibliography actually consumed by the survey. Preserve the final ACM TOG / SIGGRAPH Asia 2026 venue; keep arXiv:2609.16017 only as a preprint link until volume/issue/pages/DOI are publicly verified.
- **PDF:** rebuild `bare_jrnl.pdf` only after README/site/LaTeX/bibliography integration is complete and verify the new citation resolves.

## Consistency / safety note

Repository title and arXiv-ID searches returned no existing entry before staging. Large public-facing files were not overwritten from truncated connector payloads. This note and the verified BibTeX staging file are therefore the safe integration artifact for this run; README/index/survey/PDF remain to be synchronized in a later safe full-file edit/build.
