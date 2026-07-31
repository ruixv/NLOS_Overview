# Acoustic NLOS localization citation-trace update — 1 August 2026

A modality-focused search and citation audit of the acoustic NLOS branch identified two peer-reviewed works absent from the README, website explorer, survey prose, and merged bibliography:

- Mingu Jeon, Jae Kyung Cho, Hee Yeun Kim, Byeonggyu Park, Seung Woo Seo, and Seong Woo Kim, **Non-Line-of-Sight Vehicle Localization Based on Sound**, *IEEE Transactions on Intelligent Transportation Systems* 26(2), 2321–2338 (2025), DOI `10.1109/TITS.2024.3510582`.
- Qingbo Zhai, Libin Du, and Zhaojing Su, **Localizing acoustic sources in non-line-of-sight scenarios using irregular-grid beamforming and first-order edge diffraction**, *Measurement* 256, 117944 (2025), DOI `10.1016/j.measurement.2025.117944`.

Both are genuine NLOS sensing works rather than papers that mention NLOS propagation incidentally. Jeon et al. estimate the positions and trajectories of fully occluded vehicles from reflected/diffracted sound using an Acoustic-Spatial Pseudo-Likelihood particle filter and release the ARIL dataset with BEV ground truth. Zhai et al. explicitly model finite-edge diffraction with the Biot–Tolstoy–Medwin response and use it to construct a non-free-field steering vector for experimentally validated hidden-source beamforming.

The synchronized integration adds final-venue metadata and concise summaries to README and the interactive explorer, expands the 2025 acoustic timeline, inserts a literature-review paragraph into the Acoustic NLOS Imaging subsection, adds canonical BibTeX records, regenerates the merged bibliography and survey PDF, and verifies source/PDF consistency and first/last-page rendering.
