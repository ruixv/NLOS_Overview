# 16 August 2026 white-light NLOS citation-trace update

## Missing historical precursor integrated

Shanshan Zheng, Meihua Liao, Fei Wang, Wenqi He, Xiang Peng, and Guohai Situ, **Non-line-of-sight imaging under white-light illumination: a two-step deep learning approach**, *Optics Express* 29(24), 40091--40105 (2021), DOI 10.1364/OE.443127.

The paper uses a broadband 400--700 nm white-light source and an ordinary sCMOS camera. It embeds a speckle-correlation model in a two-stage DNN: the first network regularizes the scattered-pattern autocorrelation and the second reconstructs the hidden image. This is the direct methodological precursor to the 2025 Applied Optics physics-enhanced white-light method already represented in the repository, and it is repeatedly cited by later passive/steady-state NLOS work.

## Why it was selected

A fresh forward-citation and successor-lineage pass began from the canonical transient and passive core works (Velten 2012, LCT, f-k migration, phasor-field, computational periscopy, major learned transient methods) and cross-checked recent publisher records against README, the canonical V2 corpus, survey prose and bibliography. The recent 2025 white-light physics-enhanced method, 2025 single-shot ambient-light speckle method, and 2025 scan-free spatial-correlation transient method were already present in the survey. Their references exposed this 2021 paper as the missing origin of the white-light learned-speckle lineage rather than a merely tangential citation.

## Synchronization

The workflow inserts the paper into README, the canonical V2 paper corpus and 2021 timeline, the passive-survey white-light lineage, and the merged bibliography. It then rebuilds `bare_jrnl.pdf` and validates title/key/DOI presence, citation resolution, PDF text, and first/last-page rendering before committing the public artifacts.
