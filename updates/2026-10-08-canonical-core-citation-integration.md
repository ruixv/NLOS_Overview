# 8 October 2026: NLOS survey source integration

Verified papers: Cascaded Non-Line-of-Sight Imaging (ACM TOG 45(6), 205 / SIGGRAPH Asia 2026; DOI 10.1145/3842503), Trapezoidal Grid Reconstruction for Efficient Non-Line-of-Sight Imaging (IEEE ICCP 2026; DOI 10.1109/ICCP69532.2026.11668867), and Reconstruction and Range Characterization for a Directional Confocal Non-Line-of-Sight Imaging Model (arXiv 2609.26846, no verified final venue).

This change updates README.md, data/papers-source.html, article/2active.tex (imported by bare_jrnl.tex), and egbib_merged_20260711.bib. The public Paper Explorer uses data/papers-source.html. The trapezoidal BibTeX author is Chaoying Gu, as in the publisher record.

Remaining: index.html static Core Reading Path not updated due a connector write block. The bare_jrnl.tex wrapper already imports article/2active.tex, but the PDF has NOT been rebuilt. Compile bare_jrnl.tex from the repository root, verify all three references, and commit bare_jrnl.pdf before claiming PDF synchronization. Regenerating the merged bibliography should preserve final TOG/ICCP metadata and deduplicate citation keys.
