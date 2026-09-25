# NLOS update gap: iterative transient light transport matrix (2026-09-25)

## Verified missing paper

Talha Sultan, Eric Brandt, Khadijeh Masumnia-Bisheh, Simone Riccardo, Pavel Polynkin, Alberto Tosi, and Andreas Velten, **“Iterating the transient light transport matrix for non-line-of-sight imaging,” Nature Communications 17, 8951 (2026)**. DOI: 10.1038/s41467-026-75177-4. Published 22 July 2026 (version of record 25 August 2026).

Repository-wide searches for the full title and `TLTM` returned no match before staging this update.

## Why it belongs in the survey

This is a direct extension of the active ToF / phasor-field lineage. Instead of collapsing relay-wall transients into hidden geometry, the paper captures a full-dimensional first-order transient light transport matrix (TLTM-1) using dense laser scanning and a gated 16×16 SPAD array, then computationally focuses virtual illumination and detection independently on hidden surfaces to recover a second-order hidden-surface transport matrix (TLTM-2). The recovered representation exposes higher-order transport including indirect shadows, interreflections and volumetric scattering, and supports direct/indirect separation, relighting and dual photography. It therefore marks a trajectory from hidden geometry reconstruction toward hidden light-transport characterization and iterative TLTM-n recovery around additional corners.

## Canonical integration locations

- **README.md**: add under 2026 active/transient or higher-order/multi-bounce NLOS. Suggested summary: `Full relay-wall TLTM + gated SPAD array; iterates TLTM-1 into hidden-surface TLTM-2 for higher-order transport, relighting, indirect shadows, and volumetric scattering.`
- **Website / index.html / Paper Explorer**: add venue `Nature Communications 2026`; tags: `Active`, `Transient`, `SPAD`, `Higher-order transport`, `Phasor field`, `Multi-bounce`.
- **Development timeline**: place after phasor-field / virtual light-transport work and alongside 2026 cascaded NLOS. Emphasize the shift `hidden geometry -> hidden light-transport matrix -> iterative higher-order transport`.
- **bare_jrnl.tex**: integrate semantically in the active transient / phasor-field / higher-order transport discussion, not as a detached recent-work list. Suggested literature-review sentence: `Recent work extends virtual-wave NLOS beyond hidden geometry: Sultan et al. capture the full relay-surface transient light transport matrix and computationally iterate it to recover time-resolved transport between hidden-surface patches, exposing higher-order interreflections, shadows, and volumetric scattering.`
- **Bibliography**: merge `egbib_20260925_tltm_nature_communications.bib` into the canonical bibliography and cite it from the inserted survey sentence.
- **bare_jrnl.pdf**: rebuild only after canonical source/bibliography integration succeeds.

## Consistency status

This run safely staged the verified BibTeX and integration plan. It did **not** claim that README.md, index.html, bare_jrnl.tex, the canonical bibliography, or bare_jrnl.pdf were rebuilt, because a complete safe canonical-file edit/build was not available in this run. These artifacts should remain on the next integration checklist until all are mutually consistent.
