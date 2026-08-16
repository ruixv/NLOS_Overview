# 17 August 2026 THz / RIS / radar citation-trace update

## Verified missing or inconsistent works

1. Yiran Cui and Georgios C. Trichopoulos, **Seeing Around Obstacles Using Active Terahertz Imaging**, IEEE Transactions on Terahertz Science and Technology 14(4), 433--445 (2024), DOI 10.1109/TTHZ.2024.3401041. The survey previously mentioned the 2022 arXiv precursor only as a raw hyperlink; this update records the final IEEE journal publication, adds formal bibliography metadata, and makes the THz milestone discoverable in README/V2.
2. Kainat Yasmeen, Debidas Kundu, and Shobha Sundar Ram, **Around-the-Corner Radar Sensing Using Reconfigurable Intelligent Surface**, IEEE MAPCON 2024, DOI 10.1109/MAPCON61407.2024.10923061. The survey and merged bibliography already used the final venue, but the public README/V2 paper corpus lacked the entry; this update closes that cross-artifact gap.
3. Kainat Yasmeen, Shobha Sundar Ram, and Debidas Kundu, **Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface**, IEEE RadarConf25 (2025), pp. 1254--1259, DOI 10.1109/RadarConf2559087.2025.11205052. The survey/bibliography already contain the final RadarConf record; README/V2 are synchronized here rather than labeling the later arXiv upload as the venue.
4. Ba-Huy Pham et al., **“Around-the-Corner” Radar: Particle Filters for Non-Line-of-Sight Target Tracking in the Presence of Ambiguities**, IEEE Transactions on Aerospace and Electronic Systems 61(3), 5505--5519 (2025), DOI 10.1109/TAES.2024.3503560. This is a genuine missing dynamic radar-NLOS work: particle filtering is used to maintain ambiguous multipath target hypotheses instead of forcing brittle path association.
5. Antton Goïcoechea et al., **Single-Antenna Non-Line-of-Sight Matrix Imaging via Reconfigurable Intelligent Surfaces**, arXiv:2512.12359 (2025). A single antenna plus programmable RIS masks reconstructs the full reflection matrix and supports imaging, focusing, and tracking. No final peer-reviewed venue could be verified as of 17 August 2026, so the repository intentionally keeps arXiv as the venue.
6. Salman Liaquat et al., **Improving SNR for NLoS Target Detection Using Multi-RIS-Assisted Monostatic Radar**, IEEE Open Journal of Vehicular Technology 6, 774--789 (2025), DOI 10.1109/OJVT.2025.3547163. The paper broadens the reconfigurable-relay branch to multiple RISs and quantifies NLOS radar received power, path loss, SNR, and target-detection gains.

## Citation-trace context

The run prioritized forward citations and successors of the repository's active optical milestones (Velten 2012, LCT, f--k migration, phasor field), passive computational-periscopy lineage, learned transient methods, and modality-expansion seeds. The fresh 2026 optical/transient hits with strong relevance -- including PICL, 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, geometry-constrained reconstruction, thermal rough-wall NLOS, and the common-model ToF study -- were already represented in the repository. The remaining high-confidence gap therefore lies in the THz/RF trajectory, especially the transition from naturally occurring lossy-mirror relays and ambiguous multipath tracking to controllable RIS relays, multiple programmable surfaces, and RIS-synthesized reflection-matrix imaging.

## Venue policy

Final publisher venues are used whenever verified. In particular, the Yasmeen papers are labeled MAPCON 2024 and RadarConf25 2025 even though later arXiv versions appeared in 2026. Goïcoechea et al. remains arXiv because no accepted/published final venue was verified.

## Synchronization

The integration workflow updates README, the canonical V2 corpus (`data/papers-source.html`), `article/5newscenes.tex`, the merged bibliography, and `bare_jrnl.tex`; then it cleanly rebuilds `bare_jrnl.pdf` and validates cross-artifact titles/citations, final-venue identifiers, undefined citations, PDF text, and first/last-page rendering before pushing the generated public-artifact commit.
