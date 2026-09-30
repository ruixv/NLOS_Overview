# Integration gap: Iterating the transient light transport matrix for NLOS imaging

Verified 2026-10-01 against the default branch by exact-title and DOI search: this paper is not currently indexed in the repository.

## Paper
Talha Sultan, Eric Brandt, Khadijeh Masumnia-Bisheh, Simone Riccardo, Pavel Polynkin, Alberto Tosi, Andreas Velten, "Iterating the transient light transport matrix for non-line-of-sight imaging," Nature Communications, vol. 17, art. 8951, 2026. DOI: 10.1038/s41467-026-75177-4. Published 22 July 2026.

## Why it belongs
This work moves active ToF NLOS beyond conventional third-bounce geometry reconstruction. A dense laser scan and gated 16x16 SPAD array measure the full relay-surface first-order transient light transport matrix (TLTM-1). Computational focusing of virtual illumination and detection on hidden surfaces recovers TLTM-2, exposing time-resolved transport between hidden-surface patches. Demonstrations include higher-order interreflections and shadows, volumetric scattering, direct/indirect separation, virtual relighting, dual photography, and a path toward iterative TLTM-n recovery around additional corners.

## Recommended integration
- README Latest Additions: add under 2026 active/ToF systems.
- Milestone Timeline: place after phasor-field / SPAD-array developments as a transition from hidden geometry reconstruction to hidden light-transport reconstruction and higher-order transport.
- Active NLOS / Forward Models or Reconstruction Algorithms: discuss full TLTM acquisition and iterative recovery of hidden-surface transport.
- Hardware Devices: mention the gated 16x16 SPAD-array full-spatial-diversity acquisition when discussing parallel transient sensing.
- Website index.html / paper explorer / timeline: mirror the README entry and tag Active, ToF, SPAD array, transient light transport, higher-order/multi-bounce.
- bare_jrnl.tex: integrate semantically near phasor-field / higher-order transient-light-transport discussion rather than appending only to a recent-work list. Suggested trajectory sentence: full-dimensional relay-surface transient measurements can be computationally refocused into a second-order hidden-surface light-transport matrix, extending NLOS from geometry recovery toward analysis and control of higher-order hidden-scene transport.
- Canonical bibliography: merge the verified entry staged in `egbib_20261001_iterative_tltm_nlos.bib`.
- Rebuild `bare_jrnl.pdf` after source integration and verify README, website, TeX, bibliography, and PDF consistency.

## Verification sources
- Nature Communications version of record: https://doi.org/10.1038/s41467-026-75177-4
- PubMed PMID 42637733 confirms journal, authors, volume/issue, DOI, and 22 July 2026 publication date.

Canonical large files were not overwritten from a truncated connector payload in this run; this note records the exact safe insertion plan until a complete-file edit/build can be validated.
