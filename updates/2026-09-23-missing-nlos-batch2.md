# Verified missing NLOS papers — 2026-09-23 batch 2

This pass found three metadata-verifiable papers absent from repository-wide title search. They should be integrated into README.md, index.html/Paper Explorer/timeline, bare_jrnl.tex, and the canonical bibliography before rebuilding bare_jrnl.pdf.

## 1. Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging
Alexander Spaett, Stéphane Schertzer, Thai-An Nguyen, Martin Laurenzis. Optics Express 34(12), 22596–22613 (2026). DOI: 10.1364/OE.584776.

Category: Active / transient / SPAD hardware calibration.
Contribution: corrects pixel-dependent TCSPC/SPAD-array time-bin errors with a precomputed lookup table and establishes absolute timing from intrinsic LOS features, avoiding external time-reference calibration; demonstrated for NLOS reconstruction in non-confocal experiments and confocal simulation.
Suggested survey placement: transient acquisition / SPAD-array instrumentation, after discussion of detector timing resolution and array-based acquisition. Timeline significance: moves practical NLOS toward calibrated parallel SPAD-array capture rather than treating detector timing nonuniformity as negligible.

## 2. Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding
Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, Li Zhao. Optics Express 34(14), 26271–26289 (2026). DOI: 10.1364/OE.601398.

Category: Passive optical / learned reconstruction / physics-aware attention.
Contribution: DAAM embeds diffuse-reflection anisotropy and channel-wise SNR disparity into deformable spatial attention and frequency-aware channel attention, targeting weak-signal preservation in passive NLOS reconstruction.
Suggested survey placement: passive learned reconstruction, alongside PAC-Net/NLOS-Track and later physics-guided passive methods. Timeline significance: generic learned passive inversion -> physically informed attention for diffuse transport.

## 3. Passive acoustic non-line-of-sight localization without a relay surface
Tal I. Sommer, Ori Katz. Physical Review Applied 25, 024064 (2026). DOI: 10.1103/p97k-sf71.

Category: Acoustic NLOS / passive localization / diffraction-based sensing.
Contribution: uses knife-edge diffraction rather than a visible relay surface for 3D hidden-source localization. Door edges act as virtual detector arrays; for a convex corner, spectral diffraction signatures provide localization cues. The paper explicitly cites Velten 2012, LCT 2018, Lindell 2019, and phasor-field reconstruction, making it a strong Core-paper forward-lineage candidate rather than a passing NLOS citation.
Suggested survey placement: acoustic modality expansion, after relay-surface passive acoustic localization. Timeline significance: relay-surface acoustic NLOS -> edge-diffraction NLOS localization without a relay surface.

## Integration/build status
The three entries are staged in `egbib_20260923_missing_nlos_batch2.bib`. Large canonical files were not overwritten from partial connector payloads. Remaining work: integrate the entries and concise summaries into README.md, index.html, bare_jrnl.tex, and the canonical bibliography; compile bare_jrnl.pdf; then verify all five public-facing artifacts are mutually consistent.
