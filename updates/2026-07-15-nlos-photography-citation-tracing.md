# 15 July 2026 citation-tracing update: direct NLOS photography

## Candidate verified

**Towards Non-Line-of-Sight Photography** — Jiayong Peng, Fangzhou Mu, Ji Hyun Nam, Siddeshwar Raghavan, Yin Li, Andreas Velten, and Zhiwei Xiong, arXiv:2109.07783 (2021).

The paper is a direct active transient NLOS reconstruction contribution, not a peripheral citation. It changes the reconstruction target from an intermediate hidden volume or depth map to a high-resolution two-dimensional photograph viewed from the relay-wall location. The learned mapping bypasses explicit 3D geometry and emphasizes lateral detail, texture, and appearance. Searches of arXiv and general scholarly indexes did not identify a verifiable final conference or journal version, so the repository conservatively retains **arXiv 2021** as the venue.

## Why it was missing

The current README, homepage paper explorer, development timeline, survey source, and consolidated bibliography did not contain the title or a corresponding citation key. The work is tightly connected to the repository's core active-transient and learned-reconstruction trajectory, including light-cone / wave-based reconstruction and data-driven transient inversion, and therefore merits inclusion.

## Synchronized insertion locations

- `README.md`: add a Latest Additions row and a 2021 milestone after the real-time SPAD-array result.
- `index.html`: add a searchable paper object, increment the tracked-latest count, and extend the 2021 timeline.
- `article/4datadriven.tex`: insert a short literature-review paragraph after the early transient-to-depth end-to-end reconstruction discussion.
- `egbib_20260715_nlos_photography_updates.bib`: add canonical key `pengTowardsNLOSPhotography2021`.
- `egbib_merged_20260711.bib`: regenerate using `scripts/merge_nlos_bibliography.py`.
- `bare_jrnl.pdf`: clean-build and validate after the source and bibliography synchronization.

## Validation policy

The workflow rejects undefined citations, missing or repeated BibTeX entries, an empty PDF, a missing compiled bibliography record, duplicate homepage entries, or a failure to extract the new survey paragraph from the rebuilt PDF. The generated PDF is committed only after all checks pass.
