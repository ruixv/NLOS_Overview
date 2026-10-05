# ICCP 2026 gap: Trapezoidal Grid Reconstruction for Efficient NLOS Imaging

## Verified paper

Talha Sultan, Cheng Gu, Alex Bocchieri, Xiaochun Liu, Pavel Polynkin, Andreas Velten, **“Trapezoidal Grid Reconstruction for Efficient Non-Line-of-Sight Imaging,”** 2026 IEEE International Conference on Computational Photography (ICCP), 2026. DOI: 10.1109/ICCP69532.2026.11668867.

## Why it belongs

This work addresses reconstruction-volume sampling rather than introducing another learned inverse. Standard FFT/Rayleigh–Sommerfeld diffraction (RSD) reconstruction uses a uniform Cartesian voxel grid even though NLOS spatial resolution degrades with distance from the relay surface, causing increasing oversampling at large depth. The paper introduces Scaled RSD, combining RSD with a scaled FFT, to reconstruct directly on a trapezoidal grid that approximates perspective/spherical sampling. The grid follows depth-dependent resolution more closely, reduces the number of voxels needed for a fixed hidden volume, and retains FFT-like per-voxel efficiency.

This is tightly connected to the phasor-field/RSD line and is independently cited as an ICCP 2026 NLOS reconstruction method in the 2026 Nature Communications paper “Iterating the transient light transport matrix for non-line-of-sight imaging.”

## Recommended integration

- **README / timeline:** Active ToF NLOS → efficient / physics-based reconstruction, near phasor-field diffraction, optimized sampling, and fast reconstruction papers.
- **Paper Explorer:** tags `active`, `ToF`, `phasor-field`, `RSD`, `FFT`, `efficient reconstruction`, `adaptive sampling`.
- **Survey:** add to the discussion of frequency-domain/phasor-field reconstruction and computational efficiency. Suggested transition: “Recent work also adapts the reconstruction lattice itself to the depth-dependent resolution of NLOS systems: Scaled RSD reconstructs on trapezoidal grids that approximate perspective sampling, reducing redundant distant voxels while retaining FFT-based efficiency.”
- **Bibliography:** merge the verified entry staged in `egbib_20261005_trapezoidal_grid_gap.bib` into the canonical bibliography.
- **PDF:** rebuild only after canonical README/site/survey/bibliography integration is complete and validate citation resolution.

## Verification / deduplication

Default-branch repository searches for the exact title and for `Sultan Gu Bocchieri` returned no matches before staging. Metadata was cross-checked against an ICCP 2026 proceedings index (DOI 10.1109/ICCP69532.2026.11668867) and the reference list of Sultan et al., “Iterating the transient light transport matrix for non-line-of-sight imaging,” Nature Communications 17, 8951 (2026).

## Remaining canonical work

The large canonical README, website, survey source, bibliography, and generated PDF were not overwritten from partial buffers in this run. Integrate this note and the staged BibTeX using full-file reads/current blob SHAs, then compile and verify the PDF before claiming canonical completion.
