# 2026-09-01 gap: Stereo non-line-of-sight imaging

## Verified missing paper

Pablo Luesia-Lahoz, Sergio Cartiel, and Adolfo Muñoz, **“Stereo non-line-of-sight imaging,”** *The Visual Computer*, vol. 42, article 148, 2026. DOI: 10.1007/s00371-025-04340-7. Version of record published 29 January 2026.

Publisher page: https://doi.org/10.1007/s00371-025-04340-7

## Why it belongs

This is a direct active transient-NLOS imaging paper and a clear forward branch of the phasor-field milestone. It uses two distinct relay walls as generalized virtual camera apertures under the phasor-field formulation, combines same-wall and cross-wall illumination/capture contributions, reduces missing-cone visibility loss, and extracts hidden-surface orientation cues from which relay-wall view contributes to the reconstruction. The paper reports simulated and real-world captures.

Development trajectory:

`single relay aperture -> arbitrary/dynamic relay surfaces -> multiple relay apertures / stereo NLOS -> missing-cone mitigation and orientation-aware reconstruction`

## Repository de-duplication

Exact-title, DOI (`10.1007/s00371-025-04340-7`), and `Stereo NLOS` searches returned no match in the repository at this run, so this is a genuine corpus gap rather than a venue update or duplicate.

## Recommended integration

### README.md

Add to **Latest Additions** and the 2026 milestone/timeline near phasor-field / arbitrary-relay / missing-cone work:

> **Stereo non-line-of-sight imaging** — Luesia-Lahoz, Cartiel, Muñoz. *The Visual Computer* 42, 148 (2026). Uses two relay walls as phasor-field virtual apertures, including cross-wall illumination/capture paths, to improve hidden-surface visibility and turn missing-cone selectivity into orientation cues.

Also place under **Active NLOS Imaging -> Reconstruction Algorithms / Forward Models** as appropriate.

### Website / paper explorer

Add a 2026 active/transient entry with tags such as `active`, `transient`, `phasor-field`, `multi-relay`, `missing-cone`, `geometry`, `orientation` and include it in the latest-additions and timeline views.

### bare_jrnl.tex

Insert semantically in the discussion of phasor fields, non-planar/arbitrary relay surfaces, aperture limitations, and missing-cone visibility rather than appending only to a recent-work list. Suggested survey sentence:

> Extending the virtual-aperture interpretation of phasor fields beyond a single relay surface, Luesia-Lahoz *et al.* combine two relay walls into a generalized stereo NLOS aperture. Their formulation incorporates both independent and cross-wall transport measurements, improving visibility under the missing-cone limitation while using view-dependent visibility itself as a cue to hidden-surface orientation~\cite{luesialahozStereoNLOS2026}.

This provides a useful bridge between arbitrary-relay-surface reconstruction and multi-aperture NLOS acquisition.

### Bibliography

Merge the verified entry from `egbib_20260901_stereo_nlos_gap.bib` into the canonical bibliography using key `luesialahozStereoNLOS2026`.

### PDF and consistency check

After source integration, rebuild `bare_jrnl.pdf` and verify the paper appears consistently in README, website/paper explorer, timeline, survey source, bibliography, and compiled PDF.

## Safety note

The public-facing README and survey/bibliography files are large. In this run they were not overwritten from truncated connector output, because doing so would risk content loss. This patch note and BibTeX staging file record exact insertion locations and verified metadata for safe integration.
