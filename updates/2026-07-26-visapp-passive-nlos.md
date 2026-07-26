# 26 July 2026 — VISAPP passive NLOS integration record

## Verified missing works

### 3D Reconstruction of Hidden Objects from Simultaneous Recovery of Light Source and Environment

- Authors: Yuma Matsubara, Fumihiko Sakaue, Jun Sato
- Venue: Proceedings of the 21st International Conference on Computer Vision Theory and Applications (VISAPP 2026), Volume 3, pp. 576–583
- DOI: 10.5220/0014435000004084
- Category: passive thermal NLOS; inverse rendering; learned 3D reconstruction
- Contribution: reconstructs moving hidden far-infrared luminous points from wall/floor reflections while jointly estimating unknown scene parameters. It combines self-supervised real-measurement reprojection with supervised synthetic training.

### Estimating the 3D Position of Hidden Humans Using Reflections on Vehicle Bodies

- Authors: Hiroto Kozawa, Fumihiko Sakaue, Jun Sato
- Venue: Proceedings of the 21st International Conference on Computer Vision Theory and Applications (VISAPP 2026), Volume 3, pp. 568–575
- DOI: 10.5220/0014434900004084
- Category: passive/specular NLOS sensing; automotive hidden-pedestrian localization
- Contribution: treats curved vehicle bodies as opportunistic convex mirrors. A temporal detector finds distorted pedestrian reflections, while monocular depth, surface normals, and a specular-reflection constraint estimate the hidden pedestrian's 3D road position. This is localization rather than full hidden-scene reconstruction.

## Required cross-artifact changes

The guarded updater at `scripts/integrate_visapp2026_passive_nlos.py`, invoked through `scripts/run_visapp2026_passive_nlos.py`, specifies the exact source transformation:

1. Add both papers to `README.md` Latest Additions and the 2026 milestone timeline.
2. Add searchable records and a 2026 timeline sentence to `index.html`; recalculate the explorer count from the paper array.
3. Insert two semantically placed paragraphs and two table records in `article/3passive.tex`, immediately before the interferometer subsection.
4. Add canonical BibTeX records to `egbib_merged_20260711.bib` using keys `matsubaraJointThermalNLOS2026` and `kozawaVehicleReflectionNLOS2026`.
5. Add a trace marker and update the survey coverage date in `bare_jrnl.tex`; update the abstract paper-count wording.
6. Clean-build `bare_jrnl.pdf` with LaTeX/BibTeX and validate DOI uniqueness, resolved citations, extracted PDF text, and cross-artifact coverage.

## Current state

The source updater and validation workflow have been committed, but no subsequent commit containing the transformed public artifacts and rebuilt PDF was visible at the final check. Therefore `README.md`, `index.html`, `article/3passive.tex`, `egbib_merged_20260711.bib`, `bare_jrnl.tex`, and `bare_jrnl.pdf` must not yet be described as synchronized for these two papers.

The workflow file is `.github/workflows/integrate-visapp2026-passive-nlos.yml`. It is fail-closed and commits the source/PDF update only after compilation and consistency validation pass.
