# 2026-09-28 gap: acoustic secondary-echo identity sensing

## Verified missing work

Nevzat Olgun, “Topological-spectral fusion of secondary acoustic echoes for identity recognition in non-line-of-sight environments,” *Scientific Reports*, vol. 16, article 27404, 2026. DOI: 10.1038/s41598-026-68944-2. Published 31 August 2026.

Official article: https://doi.org/10.1038/s41598-026-68944-2
Reproducibility repository: https://github.com/nevzatolgun/NLOS_acoustic_identity_recognition

## Why it belongs

This is directly an NLOS sensing paper rather than a generic acoustics paper. It studies identity recognition from delayed multipath/secondary acoustic echoes in a controlled NLOS setup with eight speakers and eight microphones and ten subjects. It explicitly treats multipath as useful target-dependent information instead of suppressing it. Spectral STFT and LPVG topological features are fused for classification, with Leave-One-Scene-Out evaluation over changing object configurations. It therefore extends the acoustic-NLOS trajectory from hidden-scene reconstruction/localization toward semantic/biometric inference from indirect propagation.

## Safe integration plan

- README.md: add under 2026 acoustic / multimodal / task-oriented NLOS sensing, with a concise summary emphasizing secondary echoes, acoustic biometrics, and spectral-topological fusion. Do not describe it as geometric imaging.
- index.html / Paper Explorer: add tags such as Acoustic NLOS, Semantic Sensing, Identity Recognition, Multipath, Learned/Feature-based Inference; include in latest additions and the 2026 timeline.
- bare_jrnl.tex: integrate semantically in the acoustic-NLOS/emerging-modality discussion after acoustic reconstruction/localization papers. Suggested trajectory sentence: acoustic NLOS is expanding beyond geometric recovery and localization toward semantic inference, with delayed multipath echoes being exploited as person-specific biometric evidence.
- Bibliography: merge the verified entry staged in `egbib_20260928_acoustic_identity_secondary_echo.bib` into the canonical bibliography used by bare_jrnl.tex.
- PDF: rebuild bare_jrnl.pdf only after the canonical LaTeX and bibliography are safely updated and compile cleanly.

## Consistency / caution

The reported best fusion accuracy is 96.17% ± 4.07% in the paper's controlled protocol. Avoid presenting this as general real-world performance: the study uses ten subjects and a controlled room, and the authors note that the selected secondary-echo segment can contain room reverberation as well as delayed subject-environment interactions.

This note is intentionally staged instead of replacing large canonical files from partial/truncated content. README.md, index.html, bare_jrnl.tex, the canonical bibliography, and bare_jrnl.pdf remain to be synchronized in a later safe full-file update/build pass.
