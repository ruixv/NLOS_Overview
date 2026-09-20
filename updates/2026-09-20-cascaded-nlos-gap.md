# Cascaded NLOS integration gap — 2026-09-20

## Verified missing work

Diego Royo, María Peña, Forrest B. Peterson, Andreas Velten, Julio Marco, and Diego Gutierrez, **“Cascaded Non-Line-of-Sight Imaging,”** arXiv:2609.16017, 2026. No final conference/journal venue was verifiable as of 2026-09-20, so retain arXiv as the venue.

Paper: https://arxiv.org/abs/2609.16017

## Why it belongs

This is a genuine active ToF NLOS imaging paper, not an incidental NLOS citation. It explicitly moves beyond the standard three-bounce assumption by using measured higher-order (fourth- and fifth-bounce) transport. A measured impulse response at a visible relay wall is transformed into a virtual impulse response at a hidden wall, effectively cascading a second virtual NLOS imaging system. The method demonstrates multi-corner imaging, hidden-object views from different perspectives, and analyzes wave-based visibility through rough hidden walls.

## Recommended integration

- **README.md / Latest Additions:** add under Active / ToF NLOS. Concise summary: “Cascades measured and virtual transient transport to exploit fourth- and fifth-bounce photons, enabling multi-corner NLOS imaging and new hidden viewpoints beyond the conventional three-bounce model.”
- **Development timeline (2026):** place after mature three-bounce wave/phasor-field methods as a milestone in higher-order and multi-corner transient transport.
- **index.html / Paper Explorer:** category `Active / ToF / Higher-order transport / Multi-corner`; venue `arXiv 2026`; link above.
- **bare_jrnl.tex:** integrate semantically in the active ToF / phasor-field or emerging acquisition/reconstruction discussion. Suggested literature-review sentence: “Recent work extends the conventional three-bounce NLOS model to cascaded higher-order transport, synthesizing virtual impulse responses on hidden relay surfaces to exploit fourth- and fifth-bounce paths for multi-corner imaging and viewpoint expansion.” Cite the new BibTeX key `royo2026cascaded`.
- **Canonical bibliography:** merge the verified staging entry in `egbib_20260920_cascaded_nlos.bib` into the bibliography used by `bare_jrnl.tex`.
- **PDF:** rebuild `bare_jrnl.pdf` only after the canonical TeX and bibliography are safely integrated.

## Consistency status

This run intentionally did not overwrite large canonical public-facing files from partial/truncated payloads. The staging BibTeX and this patch note are committed and verified; README.md, index.html, bare_jrnl.tex, canonical bibliography, and bare_jrnl.pdf still require safe canonical integration/build in a later run.
