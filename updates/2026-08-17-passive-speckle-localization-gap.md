# 17 August 2026 passive speckle imaging/localization gap

## Newly verified missing work

Zhiyuan Wang, Huiling Huang, Haoran Li, Ziyang Chen, Jun Han, and Jixiong Pu, **Non-line-of-sight imaging and location determination using deep learning**, *Optics and Lasers in Engineering* 169, article 107701 (2023), DOI `10.1016/j.optlaseng.2023.107701`.

Elsevier's final article record describes a passive NLOS system that takes a single-shot speckle pattern and uses SPIR-Net to reconstruct hidden-object appearance while simultaneously determining object position. The method specifically removes the pulsed-laser and time-gating requirements normally used to obtain location in active transient NLOS. The reported network combines modified LeNet, U-Net, and cGAN components.

## Why it belongs in the survey

This is not a generic scattering-media paper: the experiment is explicitly framed as around-corner/passive NLOS, with light observed after reflection from a rough relay surface and the target hidden from direct view. Its contribution fills a historical gap between early steady-state passive learned reconstruction/recognition and later tracking/action-recognition systems by making spatial location a co-estimated output of the wall-mediated speckle measurement.

The paper was also cited by later learned NLOS reconstruction work, which makes it a useful citation-lineage predecessor even though it was surfaced in this run by exact passive-NLOS/learning search rather than a directly enumerable scholarly forward-citation list.

## Venue decision

Use the final Elsevier publication rather than a preprint label: *Optics and Lasers in Engineering*, volume 169, October 2023, article 107701, DOI `10.1016/j.optlaseng.2023.107701`.

## Cross-artifact integration

The integration workflow adds the work to README Latest Additions and the 2023 trajectory, the canonical V2 `data/papers-source.html` corpus/timeline, and the semantically appropriate passive/deep-learning discussion in `article/3passive.tex`. The verified BibTeX record is merged into `egbib_merged_20260711.bib`, then `bare_jrnl.pdf` is rebuilt and checked for citation resolution, semantic presence, and renderability before the synchronized public artifacts are committed.
