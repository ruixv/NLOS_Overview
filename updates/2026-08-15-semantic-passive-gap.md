# 15 August 2026 semantic/passive NLOS gap synchronization

This citation-tracing and public-artifact consistency pass integrates two verified 2024 papers that were absent from the repository and closes one survey-only consistency gap for a 2025 paper already present in README/website/BibTeX.

## Newly integrated papers

1. Sreenithy Chandran, Tatsuya Yatagawa, Hiroyuki Kubo, and Suren Jayasuriya, **Learning-Based Spotlight Position Optimization for Non-Line-of-Sight Human Localization and Posture Classification**, IEEE/CVF WACV 2024, DOI `10.1109/WACV57701.2024.00417`.
   - Off-the-shelf projector + camera.
   - Message-passing network learns scene structure and selects the spotlight position that maximizes downstream NLOS localization/posture performance.
   - Important because acquisition/illumination placement becomes a learned variable and the system is not restricted to a fixed planar relay geometry.

2. Yuzhe Li and Yuning Zhang, **Deep-Learning-Based Real-Time Passive Non-Line-of-Sight Imaging for Room-Scale Scenes**, Sensors 24(19), 6480 (2024), DOI `10.3390/s24196480`.
   - USEEN targets room-scale passive hidden-person reconstruction through diffuse relay surfaces.
   - Reports 12.2 ms inference and explicitly evaluates ambient-light robustness.
   - Adds a practical real-time indoor branch between computational periscopy and later attention/diffusion/thermal passive models.

## Consistency repair

The already-public **Non-line-of-sight multi-person pose sensing** (Hou et al., Optics Express 2025, DOI `10.1364/OE.570120`) already existed in README/website/BibTeX but was not cited in the survey body. The active-method pose table and deep-learning narrative now include it, describing the LCT + 3D U-Net + body-center-guided SMPL pipeline for adaptive multi-person 3D pose sensing.

## Public artifacts

The synchronized integration updates README, the canonical website corpus in `data/papers-source.html`, the active/passive/deep-learning survey sections, top-level `bare_jrnl.tex`, merged bibliography, and rebuilt `bare_jrnl.pdf`. The canonical `index.html` consumes the paper corpus from `data/papers-source.html`, so Paper Explorer/latest/timeline changes are reflected without duplicating the historical paper array in `index.html`.
