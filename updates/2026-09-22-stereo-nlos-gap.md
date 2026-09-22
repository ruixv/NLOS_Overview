# Integration note — Stereo non-line-of-sight imaging

## Verified missing paper

Pablo Luesia-Lahoz, Sergio Cartiel, and Adolfo Muñoz, **“Stereo non-line-of-sight imaging,”** *The Visual Computer*, vol. 42, article 148, 2026. DOI: 10.1007/s00371-025-04340-7. Published 29 January 2026 (accepted 23 December 2025).

Publisher: https://link.springer.com/article/10.1007/s00371-025-04340-7
Project page: https://p-luesia.github.io/publications/2026-stereo-nlos/

Repository-wide searches for the full title and `Luesia-Lahoz` returned no match before this staging update.

## Why it belongs

This is a direct phasor-field / active transient NLOS lineage paper rather than a tangential citation. It addresses the missing-cone visibility limitation using **two distinct relay walls as generalized virtual camera apertures**. Independent and cross-wall illumination/capture contributions are combined into a common reconstruction, improving hidden-surface visibility. The visibility differences between the two relay-wall views are also used to infer surface-orientation cues. The paper therefore extends the development trajectory from single planar relay apertures toward multi-aperture / generalized-aperture NLOS imaging and complements arbitrary-relay-surface, Virtual Mirrors, TLTM, and Cascaded NLOS work.

## Canonical integration locations

1. **README.md — Latest Additions / Active NLOS / Reconstruction Algorithms**: add the paper with final venue *The Visual Computer* 42, 148 (2026), not as a preprint.
2. **README.md — Milestone Timeline (2026)**: place near arbitrary-relay-surface and higher-order-transport work; summarize as dual-relay-wall phasor-field imaging that reduces the missing cone and extracts orientation cues.
3. **index.html / Paper Explorer / Latest Additions / timeline**: add the same metadata, DOI/project-page links, tags such as `active`, `transient`, `phasor-field`, `multi-aperture`, `missing-cone`, `stereo`.
4. **bare_jrnl.tex**: integrate semantically in the active transient / phasor-field / generalized-relay-aperture discussion, not as an isolated end-of-survey list. Suggested literature-review point: multi-relay-wall phasor-field imaging makes the inverse problem better posed by combining independent and cross-wall views, while the missing-cone visibility itself provides orientation cues. This naturally bridges non-planar/generalized apertures to recent higher-order/cascaded transport methods.
5. **Canonical bibliography**: merge the verified entry staged in `egbib_20260922_stereo_nlos_visual_computer.bib` and cite it from the inserted survey sentence(s).
6. **bare_jrnl.pdf**: rebuild only after canonical TeX/Bib integration; verify the citation resolves and the paper appears consistently across README, website, survey source, bibliography, and PDF.

## Safety / build status

This note is intentionally staged instead of replacing large canonical files from partial connector payloads. `bare_jrnl.pdf` has **not** been regenerated in this update. Do not claim canonical/public-facing synchronization until the source merge and PDF build are actually verified.
