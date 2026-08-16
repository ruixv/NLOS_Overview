# 16 August 2026 radar/RF NLOS citation-trace update

## Newly integrated missing works

1. Yupeng Yu et al., **Building Corner and NLOS Target Parameter Estimation Based on Diffraction Signal Utilization**, IEEE FUSION 2025, pp. 1--6, DOI 10.23919/FUSION65864.2025.11124177. The paper continues the electromagnetic-diffraction around-corner lineage by estimating corner/target parameters from diffraction evidence instead of requiring all geometry as prior input.
2. Yufei Wei et al., **Multipath Ghost Correlation-Based NLOS Target Localization and Building Layuot Estimation**, IEEE EUSIPCO 2025, pp. 2247--2251, DOI 10.23919/EUSIPCO63237.2025.11226331. The published paper uses Range--Doppler multipath separation, IAA direction/ghost estimation, and spatial matching to jointly infer hidden targets and building layout.
3. Weijia Yu et al., **NLoS target localization in IRS-assisted FDA-MIMO radar: A tensor decomposition perspective**, Digital Signal Processing 161 (2025), 105093, DOI 10.1016/j.dsp.2025.105093. The paper uses an IRS to establish the hidden path, estimates target count with sequential MDL, factorizes a third-order FDA-MIMO echo tensor with PARAFAC, and combines DOD/range plus 2-D DOA estimates for multi-target localization.
4. Yupeng Yu et al., **A Cross-Regional NLOS Target Localization Method Based on Joint Multipath GLRT**, IEEE IGARSS 2026, Paper 2579 / TUP1.PC.9, presented 11 August 2026. The official IGARSS program verifies the title, authors, paper number, session, and presentation time. No proceedings DOI was available in the official program when this update was prepared, so the bibliography intentionally uses the official conference page rather than guessing a DOI.

## Citation-trace context

A fresh forward-citation and recent-publication pass from the canonical optical/transient core papers (Velten 2012, LCT, f-k migration, phasor-field, computational periscopy and major learned/transient successors) did not reveal another high-confidence optical gap not already represented in the repository. The additions above instead close two coupled radar/RF lineage gaps: known diffraction geometry -> diffraction-aided corner/target parameter estimation -> multipath-ghost target/layout matching -> cross-regional joint-GLRT localization; and fixed environmental relays -> IRS-created NLoS paths -> tensor-based multi-target localization.

## Synchronization

The integration workflow updates README, the canonical V2 corpus (`data/papers-source.html`), the radar/RF survey narrative, the merged bibliography, `bare_jrnl.tex`, and a rebuilt `bare_jrnl.pdf`, then validates title/key uniqueness, citations, PDF text and rendering before pushing the public-artifact commit.


## Latest RIS tensor successors added in the same pass

5. Qian-Peng Xie et al., **Covariance Tensor Decomposition for NLOS Direction Finding in RIS-Aided Bistatic MIMO Radar**, IEEE Signal Processing Letters 33, 574--578 (2026), DOI 10.1109/LSP.2026.3652124. A fourth-order covariance tensor plus HOSVD and Khatri--Rao reconstruction yields paired DOD/DOA estimates for RIS-aided hidden targets.
6. Weijia Yu et al., **Fast Angle Estimation of NLoS Coherent and Noncoherent Targets via Tensor Decomposition in RIS-Assisted Bistatic MIMO Radar**, IEEE Transactions on Aerospace and Electronic Systems 62, 8574--8584 (2026), DOI 10.1109/TAES.2026.3651424. The work extends the tensor/RIS lineage to efficient angle estimation for both coherent and noncoherent NLoS targets.

These two 2026 journal papers were found by tracing forward from the verified 2025 Digital Signal Processing IRS/FDA-MIMO localization paper. They are direct NLOS radar successors rather than generic RIS communications papers and are therefore integrated into the survey's RIS-assisted angular-sensing lineage.
