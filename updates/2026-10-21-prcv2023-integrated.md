# PRCV 2023 citation-trace integration — 21 October 2026

Two publisher-verified missing NLOS papers were integrated into the living survey source:

1. Chang, Yue, Ni and Hu, "An Efficient Way for Active None-Line-of-Sight: End-to-End Learned Compressed NLOS Imaging," PRCV 2023, LNCS 14430, pp. 28–40, DOI 10.1007/978-981-99-8537-1_3. End-to-end learned compressive acquisition for active transient NLOS; >=1.4 dB depth PSNR versus partial Hadamard masks.
2. Liu et al., "DFAR-Net: Dual-Input Three-Branch Attention Fusion Reconstruction Network for Polarized Non-Line-of-Sight Imaging," PRCV 2023, LNCS 14430, pp. 41–52, DOI 10.1007/978-981-99-8537-1_4. Learned polarized infrared intensity/degree fusion on PI-ND.

Publisher records: https://link.springer.com/chapter/10.1007/978-981-99-8537-1_3 and https://link.springer.com/chapter/10.1007/978-981-99-8537-1_4. Both first online 26 December 2023. Springer book citation sometimes uses 2024; conference is PRCV 2023.

Source targets: README latest/timeline; index.html latest; data/papers-source.html explorer/timeline; article/2active.tex (sparse acquisition); article/3passive.tex (polarization); egbib_merged_20260711.bib (two keys). The top-level bare_jrnl.tex already inputs both chapters. The standalone comment-only edit to bare_jrnl.tex was blocked and is not necessary to include the new citations in the survey source.

PDF **not rebuilt**. Local pdflatex exists but github.com DNS resolution fails in the container, preventing complete checkout/assets. Do not claim bare_jrnl.pdf is synchronized until a full LaTeX build and binary upload are verified. The preexisting PDF must remain untouched.

Forward citation relevance: Chang explicitly cites Velten 2012, LCT 2018, f-k migration 2019 and phasor-field 2019; DFAR-Net cites Computational Periscopy, NLOS-OT and polarized NLOS. Both are actual hidden-scene reconstruction, not incidental references.
