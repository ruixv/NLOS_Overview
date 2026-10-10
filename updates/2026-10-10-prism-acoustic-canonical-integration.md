# NLOS literature integration — 10 October 2026

Verified additions and source integration:

1. Aadesh Madnaik and Karthikeyan Sundaresan, *Practical Design and Orchestration of Frequency-Shifting RIS for NLoS mmWave Sensing*, ACM MobiHoc 2025, pp. 91–100, DOI `10.1145/3704413.3764440`; BibTeX key `madnaikPRISMRISNLOS2025`. PRISM performs frequency-shift RIS coding for hidden mmWave multi-target localization; this is adjacent sensing rather than 3D scene reconstruction.
2. Mario Sroka, Ennes Sarradj, and Mathias Lemke, *Physics-informed localization of sound sources in reflective environments including hidden sources*, JASA 160(3), 2237–2248 (2026), DOI `10.1121/10.0046471`; BibTeX key `srokaPhysicsInformedAcousticNLOS2026`. Boundary-aware adjoint acoustic inversion localizes fully hidden sound sources; this is adjacent sensing rather than volumetric scene imaging.

README, `data/papers-source.html`, `article/5newscenes.tex`, and `egbib_merged_20260711.bib` have been synchronized in this commit. The main `bare_jrnl.tex` includes the changed chapter with `\input{article/5newscenes.tex}` and does not require an additional prose copy. The Sensors 2026 SPAD/TCSPC hidden-human detection paper is already integrated and was not duplicated.

**Incomplete artifacts:** Direct Git-blob and SHA-guarded contents writes of `index.html` were blocked by connector safety checks. The static homepage Core Reading Path therefore lacks these two links; the Paper Explorer's data source includes them. An optional header comment in `bare_jrnl.tex` was also blocked and intentionally omitted to preserve the file. **The binary `bare_jrnl.pdf` has not been regenerated.** In a full checkout, run `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex`, verify `.bbl`, log warnings and `pdfinfo`, then commit the new PDF. Until the PDF blob SHA changes, it remains stale. Historical duplicate DOI groups remain a separate task.
