# 2026-07-05 Venue Verification and Homepage/PDF Consistency Pass

## Search result

This pass did not find a new high-confidence NLOS imaging paper that is both genuinely relevant and not already represented in the repository frontier list. Fresh keyword searches and a citation-tracing-oriented pass around active ToF / LCT / f-k / phasor-field / NeTF / passive periscopy / consumer-LiDAR / RF-RIS seeds mainly returned already-covered entries.

Excluded examples:

- `A Non-Line-of-Sight, Multi-Modality-based Side-Channel IP Theft Attack on Additive Manufacturing Using Dual Smartphones` (`arXiv:2607.00186`): uses a non-line-of-sight experimental setup but is a side-channel G-code reconstruction/security paper, not NLOS imaging or hidden-scene reconstruction.
- `DuTrack: Long-Term Indoor Human Tracking with Dual-Channel Sensing and Inference` (`arXiv:2601.10972`): mentions NLoS Wi-Fi propagation zones, but the contribution is indoor tracking/fusion rather than NLOS imaging, transient reconstruction, around-corner localization, or hidden-scene sensing.
- `Multi-modal Data Driven Virtual Base Station Construction for Massive MIMO Beam Alignment` (`arXiv:2602.22796`): communication/beam-alignment work using LiDAR-derived virtual base stations, not a NLOS sensing/imaging paper.

## Metadata corrections recommended

The pass also checked whether several arXiv-first latest entries had a verifiable final venue. Search results did not verify the final venues currently shown for the following README/homepage entries. Under the repository rule "use arXiv as the venue when no final accepted/published venue can be verified," these should be relabeled to arXiv unless a reliable venue page is later found.

Recommended README replacements:

```diff
-| 2026 | [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | SIGGRAPH 2026 | Uses 3D Gaussian primitives and differentiable transient rendering; targets spatially limited, non-planar, arbitrary relay surfaces. |
+| 2026 | [Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270) — Wang et al. | arXiv 2026 | Uses 3D Gaussian primitives and differentiable transient rendering; targets spatially limited, non-planar, arbitrary relay surfaces. |

-| 2026 | [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865) — Somasundaram et al. | Nature 2026 | Demonstrates plug-and-play NLOS using smartphone-grade / consumer LiDAR with motion-induced aperture sampling. |
+| 2026 | [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865) — Somasundaram et al. | arXiv 2026 | Demonstrates plug-and-play NLOS using smartphone-grade / consumer LiDAR with motion-induced aperture sampling. |

-| 2026 | [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals](https://arxiv.org/abs/2605.29098) — Lu et al. | CVPR 2026 | GeRaF 2.0: neural RF geometry reconstruction that combines LoS visual priors with NLoS radar propagation. |
+| 2026 | [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals](https://arxiv.org/abs/2605.29098) — Lu et al. | arXiv 2026 | GeRaF 2.0: neural RF geometry reconstruction that combines LoS visual priors with NLoS radar propagation. |
```

Recommended homepage replacements in `index.html`:

```diff
-<div class="eyebrow">Updated 4 July 2026 · 190+ papers</div>
+<div class="eyebrow">Updated 5 July 2026 · 190+ papers</div>

-<p style="margin-top:1rem;">Last updated: 4 July 2026</p>
+<p style="margin-top:1rem;">Last updated: 5 July 2026</p>

-venue:'SIGGRAPH 2026'
+venue:'arXiv 2026'

-venue:'Nature 2026'
+venue:'arXiv 2026'

-venue:'CVPR 2026'
+venue:'arXiv 2026'
```

## Public-artifact consistency backlog

`README.md` currently includes several entries that still need to be surfaced in `index.html` / the paper explorer, including the single-pixel-camera NLOS paper and the phasor-field theory/experiment papers added in the previous passes. The homepage latest-entry count also remains stale (`53`) relative to the README additions.

Recommended homepage additions still pending:

- Zhu et al., `Single photon imaging and sensing of obscured objects around the corner`, arXiv 2021.
- Dove and Shapiro, `Paraxial Theory of Phasor-Field Imaging`, arXiv 2019.
- Reza et al., `Wave-like Properties of Phasor Fields: Experimental Demonstrations`, arXiv 2019.
- Dove and Shapiro, `Paraxial phasor-field physical optics`, arXiv 2020.
- Dove and Shapiro, `Nonparaxial phasor-field propagation`, arXiv 2020.
- Reza et al., `Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier`, arXiv 2020.
- Musarra et al., `Non-line-of-sight 3D imaging with a single-pixel camera`, arXiv 2019.

## Survey/PDF status

`bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

To compile with all accumulated update entries, it should use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates}
```

The PDF was not regenerated in this pass. The available GitHub connector writes files via whole-file replacement and does not provide a safe LaTeX build / binary upload path in this run, so the source-level status and the remaining compile step are recorded here rather than claiming `bare_jrnl.pdf` is updated.
