# 18 July 2026 reconstruction, pose, and public-artifact consistency audit

## Findings

A cross-file comparison of `README.md`, `index.html`, survey sections, update logs, and the merged bibliography found two distinct gaps:

1. Five final-venue papers were absent from the public repository and survey.
2. Five papers already visible in README and the website had not been integrated into survey prose and/or the merged bibliography.

The latest direct NLOS imaging paper independently verified in this run remains **Non-line-of-sight imaging via physics-informed cascade learning**, published in *JOSA A* on **15 July 2026**. No later direct NLOS paper or arXiv submission was verified.

## Newly added final-venue papers

- **Non-line-of-sight human pose estimation**, *Optics and Lasers in Engineering* 201, 109658 (2026), DOI `10.1016/j.optlaseng.2026.109658`. Directly estimates semantic body joints from transient-derived intensity/depth features, with physics-based training synthesis and measured low-SNR evaluation.
- **Frequency-domain multi-regularization-experts fusion for robust non-line-of-sight imaging**, *Pattern Recognition* 173, 112914 (2026), DOI `10.1016/j.patcog.2025.112914`. Uses optimization-derived frequency-expert gating for robust active reconstruction.
- **Canny operator-based artifact identification and suppression for non-line-of-sight imaging**, *Optics & Laser Technology* 195, 114542 (2026), DOI `10.1016/j.optlastec.2025.114542`. Provides reference-free artifact segmentation and transient correction for backprojection.
- **Nonconfocal non-line-of-sight imaging with specular-flight-path regularization for complex multi-orientation objects**, *Photonics Research* 14(4), 1125–1134 (2026), DOI `10.1364/PRJ.579183`. Uses local transport-matrix structure to select informative paths for complex non-confocal scenes.
- **Super-resolution non-line-of-sight imaging with laser pulses multiplexing**, *Optics and Lasers in Engineering* 199, 109558 (2026), DOI `10.1016/j.optlaseng.2025.109558`. Recovers 64 ps transients from 704 ps timing hardware via deterministic pulse offsets and NNLS.

## Public entries integrated into survey and bibliography

- **Beyond λ/2: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?**, arXiv:2602.07515.
- **Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform**, arXiv:2508.02003.
- **N²LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization**, arXiv:2505.08240.
- **SuperEx: Enhancing Indoor Mapping and Exploration using Non-Line-of-Sight Perception**, arXiv:2510.10506.
- **mitransient: Transient light transport in Mitsuba 3**, arXiv:2510.25660.

No final accepted or published venues were verified for these five preprints, so arXiv remains the venue.

## Metadata correction

**Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding** now uses its verified final DOI, `10.1364/OE.601398`, and complete *Optics Express* 34(14), 26271–26289 metadata instead of an abstract-only link.

## Integration mechanism

- `egbib_20260718_reconstruction_pose_consistency.bib` contains ten new canonical records and the corrected diffuse-aware record.
- `scripts/sync_nlos_20260718_reconstruction_pose_consistency.py` performs guarded, idempotent updates across README, homepage, active survey, learning/dataset discussion, new-modality/robotics/RF discussion, and timeline.
- `scripts/finalize_nlos_20260718_public_counts.py` invokes this synchronizer before reconciling the paper-explorer count.
- The existing pull-request validation workflow merges all bibliography fragments, clean-builds the LaTeX survey, checks undefined and duplicate citations, extracts and renders the PDF, and commits synchronized source files plus `bare_jrnl.pdf` only after successful validation.

Public files and the PDF must not be reported as updated until the workflow succeeds and the pull request is merged.
