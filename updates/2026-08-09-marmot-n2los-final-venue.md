# 9 August 2026 NLOS citation-trace consistency update

This bounded follow-up completes two outstanding source-consistency items discovered by the citation-tracing workflow.

1. **MARMOT: Masked Autoencoder for Modeling Transient Imaging** (Shen et al., arXiv:2506.08470, 2025) is integrated into the Latest Additions table and the survey's sparse/irregular transient-acquisition discussion. As of 9 August 2026, the arXiv/DBLP records remain preprint/CoRR metadata; no final journal or conference venue was verified.
2. **N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization** is corrected from arXiv-only metadata to its final **IEEE Transactions on Mobile Computing**, vol. 25, no. 5, pp. 6002–6016 (2026), DOI **10.1109/TMC.2025.3634623**. The final record has seven authors: Zhenguo Shi, Yihe Yan, Yanxiang Wang, Wen Hu, Chun Tung Chou, Qingqing Cheng, and Weijie Yuan. It uses a 24 GHz radar and one backscatter tag, HFD signaling, and FS-MUSIC to exploit multipath for measured NLOS localization.

The previously prepared cellular-ISAC lineage remains part of the same public-artifact branch: Tosi et al.'s IEEE SPAWC 2024 feasibility paper and the final ICT 2026 intrusion-detection follow-up. The explorer count remains 268 because this run corrects N2LoS metadata rather than adding a duplicate paper.

Validation requirements for this branch are: README/index/survey/BibTeX agreement; MARMOT and N2LoS presence in the rebuilt PDF; final IEEE TMC DOI/venue visible in the PDF bibliography; successful LaTeX/BibTeX compilation with no undefined citations; and rendered first/radar pages large enough to rule out an empty or corrupt PDF.
