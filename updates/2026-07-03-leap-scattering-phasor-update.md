# 2026-07-03 — LEAP and scattering-media phasor NLOS update

## Summary

This run found two high-confidence missing or under-integrated NLOS papers through keyword search and phasor-field citation-tracing style queries.

1. **Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging** — Cho, Shim, Kim, arXiv 2024.
   - arXiv: https://arxiv.org/abs/2407.18574
   - Reason for inclusion: directly relevant active optical / learning-based NLOS work. LEAP predicts clean full-aperture phasor fields from noisy partial measurements, constraining the network to the informative frequency band of phasor-field propagation. It is especially relevant to sparse sampling, smaller scan apertures, and practical acquisition.
   - Venue decision: no verified final venue found in this run; keep as **arXiv 2024**.

2. **Non-line-of-sight imaging in the presence of scattering media using phasor fields** — Luesia, Crespo, Jarabo, Redo-Sanchez, arXiv 2023.
   - arXiv: https://arxiv.org/abs/2311.09223
   - Reason for inclusion: directly relevant phasor-field NLOS work that studies hidden scenes submerged in scattering media, extending virtual-wave NLOS analysis beyond clean surface-only propagation.
   - Venue decision: no verified final venue found in this run; keep as **arXiv 2023**.

## Repository updates committed

- `README.md`
  - Updated latest-run date to **3 July 2026**.
  - Added LEAP as a 2024 latest addition.
  - Added scattering-media phasor-field NLOS as a 2023 latest addition.
  - Commit: `6452f437c4039825d779c069b8312d0917dc0e25`

- `article/5newscenes.tex`
  - Added LEAP to the **Sparse and Irregular Active NLOS Acquisition** subsection.
  - Added a new **Scattering-Media NLOS Imaging** subsection for Luesia et al.
  - Updated the section overview sentence to mention phasor-field enhancement and scattering-media robustness.
  - Commit: `c2f73ca7cdd26f72ba13e6c9e105b8085a10e9e7`

- `article/6conclusion.tex`
  - Added LEAP to the deep-learning / sparse-acquisition / forward-model summary.
  - Added scattering-media NLOS to the new-modality / geometry summary.
  - Commit: `4cea8128b6dac65ceea4b1f0e385b3e650abd5c9`

- `egbib_20260703_updates.bib`
  - Added BibTeX entries `choLEAP2024` and `luesiaScatteringPhasor2023`.
  - Commit: `fbba8634a1b1ed882d468270704428801eed6152`

## Website patch still needed

`index.html` is not overwritten in this run to avoid accidental damage to the manually curated JavaScript paper list via whole-file replacement. To keep the homepage fully synchronized with README, apply the following targeted updates:

1. Change the tracked latest count from `40` to `48` if synchronizing all README latest entries, or at minimum to `42` if adding only the two papers from this run.
2. Change the header/footer date from `2 July 2026` to `3 July 2026`.
3. Add these objects to the `papers` array near the other 2024/2023 latest entries:

```js
{cat:'latest learning active', title:'Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging', authors:'Cho et al.', year:2024, venue:'arXiv 2024', url:'https://arxiv.org/abs/2407.18574', key:'LEAP predicts clean full-aperture phasor fields from noisy partial measurements for sparse sampling and smaller scan apertures.'},
{cat:'latest active', title:'Non-line-of-sight imaging in the presence of scattering media using phasor fields', authors:'Luesia et al.', year:2023, venue:'arXiv 2023', url:'https://arxiv.org/abs/2311.09223', key:'Extends phasor-field NLOS analysis to hidden scenes affected by fog/smoke-like volumetric scattering.'},
```

The website is also still missing several README entries synchronized in prior runs, including Tosi et al. ISAC intrusion detection, Sanjeeva Reddy & Vinod Veera Reddy IRS CRB, Colone et al. RIS-aided low-RCS detection, Boger-Lombard et al. passive acoustic localization, Cao et al. active focusing as a latest entry, and Esmaeilbeig et al. multi-IRS hidden moving target sensing.

## PDF compilation status

`bare_jrnl.pdf` was not regenerated in this run. The remaining build step is to update the bibliography line in `bare_jrnl.tex` to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates}
```

Then compile locally with LaTeX/BibTeX and upload the regenerated PDF. The available GitHub connector can update text files, but does not provide a safe LaTeX build plus binary PDF upload path in this run.
