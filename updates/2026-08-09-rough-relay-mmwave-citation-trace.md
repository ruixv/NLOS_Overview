# 9 August 2026 rough-relay mmWave citation-trace update

A forward/backward citation-tracing pass around HoloRadar, RFlect, classical around-corner radar, and recent rough-relay mmWave work exposed a coherent missing branch that was not represented in the public README, website explorer, or survey text.

Integrated records:

- Xu, Liu, Jiang, **Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing**, IEEE Internet of Things Journal 11(6), 10964–10978 (2024), DOI 10.1109/JIOT.2023.3328018.
- Xu et al., **Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface**, IEEE Transactions on Signal Processing 72, 5628–5643 (2024), DOI 10.1109/TSP.2024.3505938.
- Xu et al., **Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces**, IEEE Signal Processing Letters 32, 2075–2079 (2025), DOI 10.1109/LSP.2025.3567216.
- Lv et al., **mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing**, IEEE INFOCOM 2025, 1–10, DOI 10.1109/INFOCOM55648.2025.11044715.
- Mehrotra et al., **Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar**, ACM MobiCom 2024, 1545–1559, DOI 10.1145/3636534.3690710.
- Liu et al., **MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions**, IEEE Aerospace and Electronic Systems Magazine (2026), DOI 10.1109/MAES.2026.3701667.

The survey integration treats these as one trajectory: rough and multi-angle relay surfaces first become useful stochastic/scattering structure, then uncertain relay geometry becomes a latent inference variable, and finally the reflector/environment itself is reconstructed or bypassed through multi-bounce modeling. This complements the already-covered HoloRadar, RFlect, CornerRadar, Mosaic, mmNorm, RISE, and Wave-Former lineage instead of duplicating it.

The searchable website count increases from 268 to 274. The rebuilt PDF must contain the new radar paragraph and all six bibliography entries before this update is considered complete.
