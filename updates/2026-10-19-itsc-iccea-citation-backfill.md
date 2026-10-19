# Verified NLOS backfill candidates — 19 October 2026

1. Li, Ziwei; Hirano, Masahiro; Guo, Qitong; Jia, Ruoyu; Yamakawa, Yuji. **SG-NLOSTrack: Semantic-Guided Non-Line-of-Sight Target Tracking.** IEEE ITSC 2025, pp. 3510–3516. DOI: 10.1109/ITSC60802.2025.11423163. 4D radar, semantic-guided reflected-path tracking; 0.419 m MAE and 80% tracking success; adjacent sensing, not dense imaging.
2. Liu, Zhicheng; Li, Guangpeng. **Active Non-Line-Of-Sight Imaging Based on Fusion of Physical Prior and Deep Learning.** IEEE ICCEA 2025, pp. 268–271. DOI: 10.1109/ICCEA65460.2025.11102151. Dual-branch channel/spatial attention and dilated multi-scale kernels for active hidden-target reconstruction.

Verified against IEEE Xplore and DBLP/proceedings indexes. Both missing from master README and Paper Explorer on 19 October 2026.

Insertion locations: README Latest Additions, active-learning table, radar table, Milestone Timeline; data/papers-source.html papers array and 2025 timeline; index.html latest research prose; article/2active.tex transformer/learning section; article/5newscenes.tex Radar-Based NLOS Imaging; egbib_merged_20260711.bib keys liSGNLOSTrack2025 and liuPhysicalPriorActiveNLOS2025. bare_jrnl.tex already inputs these sections.

PDF remains outdated. Rebuild complete source with latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex, validate citations and pages, then commit binary bare_jrnl.pdf separately.