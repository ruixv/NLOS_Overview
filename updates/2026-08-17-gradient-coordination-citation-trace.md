# 17 August 2026 gradient-coordination citation-trace update

## Newly verified missing work

Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang, **Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging**, *Symmetry* 18(5), article 711 (2026), DOI `10.3390/sym18050711`.

The paper is direct active transient NLOS reconstruction rather than a generic optimization paper: its experiments use the NLOST-style transient benchmark and physical laser/galvanometer/SPAD measurement setting. The paper cites the modern active NLOS lineage including wave-based f-k migration, phasor-field virtual wave optics, and NLOST, making it a valid forward-citation candidate from the repository's core/milestone seeds.

## Why it is a distinct contribution

Most physics-guided learned reconstruction combines reconstruction, measurement-consistency, noise/statistical, and calibration constraints by summing weighted losses. Ling et al. instead treat their interaction as a gradient-governance problem. The framework combines PCGrad-style soft conflict projection, PhysGuard-style protected physical routing, learnable sensor calibration, and staged unfreezing so a high-magnitude branch does not suppress other physically useful updates in low-SNR reconstruction. This is best placed immediately after the survey's learnable-physical-priors discussion: the trajectory becomes **fixed physical priors -> learnable physical priors -> explicit coordination of competing physical gradients**.

## Venue decision

This is not an arXiv-only record. The verified final publication is *Symmetry*, volume 18, issue 5, article 711 (2026), DOI `10.3390/sym18050711`, with authors Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang. Public metadata reports publication on 23 April 2026.

## Cross-artifact integration

The integration workflow adds the paper to README Latest Additions and the 2026 development timeline, the canonical V2 `data/papers-source.html` corpus/timeline, the semantically appropriate learnable-physics section in `article/4datadriven.tex`, and `egbib_merged_20260711.bib`. It then rebuilds `bare_jrnl.pdf` and checks that the title, citation key, DOI, and PDF semantic markers are mutually consistent before committing public artifacts.
