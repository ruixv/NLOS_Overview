# Integration gap: Iterating the transient light transport matrix for NLOS imaging

Verified missing paper for the NLOS Overview corpus on 2026-09-21.

## Paper
Talha Sultan, Eric Brandt, Khadijeh Masumnia-Bisheh, Simone Riccardo, Pavel Polynkin, Alberto Tosi, Andreas Velten, **“Iterating the transient light transport matrix for non-line-of-sight imaging,” Nature Communications 17, 8951 (2026)**. DOI: 10.1038/s41467-026-75177-4. Published 22 July 2026.

## Why it belongs
This is a direct Core-lineage active transient NLOS contribution from the Velten/Tosi line of work. Instead of using only lower-dimensional slices of transient transport for geometry recovery, it measures a full-dimensional first-order transient light transport matrix (TLTM-1) between relay-wall patches and computationally recovers TLTM-2 between hidden-scene patches. Independent virtual illumination/detection in the hidden scene turns the relay wall into a synthetic ToF camera. The recovered higher-order transport exposes indirect shadows, interreflections, volumetric scattering, direct/indirect separation, virtual relighting, and dual photography, and motivates iteration toward TLTM-n.

## Suggested integration
- README Latest Additions / Active transient NLOS: add the Nature Communications 2026 paper and describe the transition from geometry-centric three-bounce reconstruction to recovery/iteration of higher-order transient transport.
- Development timeline (2026): add `full-dimensional TLTM-1 -> virtual hidden-scene illumination/detection -> TLTM-2 / higher-order transport` as a milestone near cascaded NLOS.
- Website Paper Explorer: category `Active / transient / higher-order light transport`; venue `Nature Communications 2026`; DOI above.
- bare_jrnl.tex: integrate in the active ToF / phasor-field / emerging higher-order-transport discussion, ideally adjacent to cascaded NLOS. A concise literature-review point is that full-dimensional relay-wall transport can synthesize independently focused hidden illumination and detection, extending NLOS from geometry recovery toward recovering and manipulating hidden-scene light transport itself.
- Canonical bibliography: merge the verified BibTeX staged in `egbib_20260921_tltm_nature_communications.bib`.
- Rebuild bare_jrnl.pdf after source and canonical bibliography integration.

## Consistency status
At this run the exact title and `TLTM` were absent from repository-wide code search. The large canonical README/index/TeX files were not overwritten from partial payloads. This note and verified BibTeX are intentionally staged so a later safe full-file integration can update README.md, index.html, bare_jrnl.tex, the canonical bibliography, and then regenerate bare_jrnl.pdf without truncation risk.
