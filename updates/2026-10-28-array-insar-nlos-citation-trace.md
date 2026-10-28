# NLOS citation-trace update — 28 October 2026

## Citation-tracing scope
The forward-citation audit used the repository's core and milestone lineage as seeds: Velten et al. (2012), O'Toole et al. (2018, LCT), Lindell et al. (2019, f-k migration), phasor-field reconstruction, computational periscopy, PAC-Net, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Search results were cross-checked against the README catalog, the homepage/paper explorer, `data/papers-source.html`, the included survey chapters, and the consolidated BibTeX source.

## Newly recovered missing work
**Yuqing Lin, Xiaolan Qiu, Yitong Luo, and Chibiao Ding, “Multipath Exploitation: Non-Line-of-Sight Target Relocation in Array-InSAR 3-D Imaging,” IEEE Transactions on Geoscience and Remote Sensing, vol. 62, article 4708414 (2024), DOI: 10.1109/TGRS.2024.3463003.**

The publisher record confirms that the UAV-borne array-InSAR method uses a spherical-wavefront 3D model, fits building reflection planes, analyzes multipath-reachable regions, and relocates virtual NLOS targets to physical positions in urban canyons. The reported imageable ground range expands by 41.62%, the 3D area by 76.57%, and localization errors are typically below 0.5 m. This is genuine radar NLOS 3D imaging/reconstruction, not merely NLOS communication or link localization.

Metadata verification:
- IEEE Xplore: https://ieeexplore.ieee.org/abstract/document/10683719
- DOI: https://doi.org/10.1109/TGRS.2024.3463003
- DBLP record: https://dblp.org/rec/journals/tgrs/LinQLD24

## Repository synchronization
- Added a catalog row and a 2024 milestone to `README.md`.
- Added a searchable paper record to `data/papers-source.html` and a linked milestone paragraph to `index.html`.
- Integrated the paper in the radar NLOS imaging section of `article/5newscenes.tex`.
- Added `linArrayInSARNLOSTargetRelocation2024` to `egbib_merged_20260711.bib`.
- Updated the survey's stated coverage date in `bare_jrnl.tex` to 28 October 2026.

## Build status
The existing master-branch survey-build workflow is expected to rebuild and validate `bare_jrnl.pdf` after these source changes are merged. The PDF must not be considered refreshed until the workflow run and resulting PDF commit are verified.
