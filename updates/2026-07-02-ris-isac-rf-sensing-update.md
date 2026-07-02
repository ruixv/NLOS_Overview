# 2026-07-02 RIS / ISAC RF-NLOS sensing update

## Added candidates

This run did not find a new optical/transient NLOS reconstruction paper beyond the current README and homepage snapshot. It did find four relevant RF/RIS/ISAC NLOS sensing papers that were not present in the repository search results. These are adjacent to the repository's current RF/mmWave NLOS branch rather than classical optical hidden-shape reconstruction.

1. **Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware** — Paolo Tosi, Maximilian Bauhofer, Marcus Henninger, Laurent Schmalen, Silvio Mandelli, arXiv 2026. Demonstrates fully NLOS intrusion detection and tracking with a 27.4 GHz 5G/ISAC proof-of-concept, using a large environmental reflector, range-Doppler processing, and a PHD filter in an industrial ARENA2036 setting.
2. **Cramer-Rao Bounds for Target Parameter Estimation in a Bi-Static IRS-Assisted Radar Configuration** — Sanjeeva Reddy S, Vinod Veera Reddy, arXiv 2026. Derives Fisher-information / CRB limits for target angle estimation in an IRS-static radar configuration that uses a Target → IRS → Radar path to emulate a bistatic viewpoint while avoiding a full distributed receiver.
3. **RIS-aided Radar Detection Architectures with Application to Low-RCS Targets** — Fabiola Colone, Filippo Costa, Yiding Gao, Chengpeng Hao, Linjie Yan, Giuliano Manara, Danilo Orlando, arXiv 2026. Proposes RIS-aided monostatic/bistatic radar detection architectures for low-RCS NLOS/low-observable targets and provides RIS design guidelines and CFAR-style detectors.
4. **Cramer-Rao Lower Bound Optimization for Hidden Moving Target Sensing via Multi-IRS-Aided Radar** — Zahra Esmaeilbeig, Kumar Vijay Mishra, Arian Eamaz, Mojtaba Soltanalian, arXiv 2022. Earlier theoretical work on hidden/NLOS moving-target estimation using multiple IRS panels and Doppler-aware IRS phase optimization.

## Metadata decision

No reliable final journal or conference venue was verified for these four entries during this run. They should therefore be labeled as **arXiv** entries until publisher/venue metadata can be confirmed.

## Repository updates performed

- Updated `egbib_20260702_updates.bib` with BibTeX entries:
  - `coloneRISAidedDetection2026`
  - `sanjeevaBiStaticIRSCRB2026`
  - `tosiNLOSIntrusionISAC2026`
  - `esmaeilbeigMultiIRSHiddenTarget2022`

## Recommended README.md patch

Add the three 2026 entries near the existing RIS / RF / ISAC latest additions, and add the 2022 multi-IRS entry near the 2022 modality entries if the latest-additions list is intended to include missing historical entries:

```md
| 2026 | [Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware](https://arxiv.org/abs/2604.07032) — Tosi et al. | arXiv 2026 | 5G/mmWave ISAC proof-of-concept for fully NLOS intrusion detection and tracking in an industrial environment using large-surface reflections and PHD filtering. |
| 2026 | [Cramer-Rao Bounds for Target Parameter Estimation in a Bi-Static IRS-Assisted Radar Configuration](https://arxiv.org/abs/2603.01660) — Sanjeeva Reddy S, Vinod Veera Reddy | arXiv 2026 | Analyzes IRS-static radar target-parameter estimation limits for a Target → IRS → Radar path that emulates a bistatic NLOS sensing viewpoint. |
| 2026 | [RIS-aided Radar Detection Architectures with Application to Low-RCS Targets](https://arxiv.org/abs/2601.10846) — Colone et al. | arXiv 2026 | Uses RIS-aided monostatic/bistatic processing to redirect otherwise lost low-RCS target scattering back to the radar for NLOS/low-observable detection. |
| 2022 | [Cramer-Rao Lower Bound Optimization for Hidden Moving Target Sensing via Multi-IRS-Aided Radar](https://arxiv.org/abs/2210.05812) — Esmaeilbeig et al. | arXiv 2022 | Early multi-IRS hidden/NLOS moving-target sensing analysis with Doppler-aware phase-shift optimization and CRLB-guided design. |
```

If all four are added to the homepage latest list, update the tracked latest count from `40` to `44`.

## Recommended index.html patch

Add the following paper objects near the other RF/mmWave/RIS latest entries:

```js
{cat:'latest modality', title:'Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware', authors:'Tosi et al.', year:2026, venue:'arXiv 2026', url:'https://arxiv.org/abs/2604.07032', key:'5G/mmWave ISAC proof-of-concept for fully NLOS intrusion detection and tracking using large-surface reflections and PHD filtering.'},
{cat:'latest modality', title:'Cramer-Rao Bounds for Target Parameter Estimation in a Bi-Static IRS-Assisted Radar Configuration', authors:'Sanjeeva Reddy S and Vinod Veera Reddy', year:2026, venue:'arXiv 2026', url:'https://arxiv.org/abs/2603.01660', key:'IRS-static radar target-parameter estimation limits for a Target → IRS → Radar path that emulates bistatic NLOS sensing.'},
{cat:'latest modality', title:'RIS-aided Radar Detection Architectures with Application to Low-RCS Targets', authors:'Colone et al.', year:2026, venue:'arXiv 2026', url:'https://arxiv.org/abs/2601.10846', key:'RIS-aided monostatic/bistatic detection architectures redirect low-RCS target scattering toward the radar for hidden-target detection.'},
{cat:'latest modality', title:'Cramer-Rao Lower Bound Optimization for Hidden Moving Target Sensing via Multi-IRS-Aided Radar', authors:'Esmaeilbeig et al.', year:2022, venue:'arXiv 2022', url:'https://arxiv.org/abs/2210.05812', key:'Multi-IRS hidden moving-target sensing analysis with CRLB-guided Doppler-aware phase optimization.'},
```

Recommended 2026 timeline wording: add "ISAC NLOS intrusion detection, IRS-static radar estimation limits, RIS-aided low-RCS detection" to the 2026 RF/RIS sentence. If adding the historical 2022 item to the timeline, mention "multi-IRS hidden-target CRLB design" as an early RF/RIS NLOS estimation precursor.

## Recommended article/5newscenes.tex insertion

In `\subsection{Radar-Based NLOS Imaging}`, after the RIS / dual-beam RIS discussion, add:

```tex
Other RIS/IRS radar works emphasize estimation limits and deployment-oriented sensing rather than reconstruction. Colone~\etal~study RIS-aided monostatic/bistatic radar detection architectures for low-RCS targets~\cite{coloneRISAidedDetection2026}, while Sanjeeva Reddy~S and Vinod Veera Reddy derive CRB limits for target-parameter estimation in an IRS-static geometry that exploits the Target--IRS--Radar path~\cite{sanjeevaBiStaticIRSCRB2026}. Earlier, Esmaeilbeig~\etal~used multi-IRS phase optimization to improve hidden moving-target estimation bounds~\cite{esmaeilbeigMultiIRSHiddenTarget2022}. In a more deployment-driven ISAC direction, Tosi~\etal~demonstrate reliable NLOS intrusion detection and tracking with 5G/mmWave communication hardware by using a large environmental reflector and a PHD-filter tracking pipeline~\cite{tosiNLOSIntrusionISAC2026}.
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The bibliography supplement has been updated, but the main survey build still needs `bare_jrnl.tex` to use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates}
```

Then LaTeX/BibTeX should be run locally and the regenerated PDF should be uploaded. This run did not overwrite `README.md`, `index.html`, or large LaTeX files because the available GitHub write path is whole-file replacement; the patch above provides exact insertion text to avoid accidental truncation or escaping damage.
