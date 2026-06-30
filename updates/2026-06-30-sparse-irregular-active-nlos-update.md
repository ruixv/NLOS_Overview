# 2026-06-30 update: sparse and irregular active NLOS acquisition

## Added / integrated papers

This run did not find a brand-new 2026 NLOS paper beyond the current README / homepage frontier, but citation-tracing around the signal-object collaborative regularization / arbitrary-pattern NLOS branch surfaced two highly relevant active-NLOS entries that were not consistently represented in the repository.

1. **Non-line-of-sight imaging with arbitrary illumination and detection pattern**
   - Authors: Xintong Liu, Jianyu Wang, Leping Xiao, Zuoqiang Shi, Xing Fu, Lingyun Qiu
   - Venue: **Nature Communications 2023**
   - DOI: `10.1038/s41467-023-38898-4`
   - Link: https://www.nature.com/articles/s41467-023-38898-4
   - Contribution: Bayesian CC-SOCR framework for arbitrary illumination and detection points. It introduces virtual confocal signals and signal-object collaborative regularization to reconstruct hidden albedo and surface normals under irregular, fragmented, or sparse relay sampling.

2. **Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization**
   - Authors: Xintong Liu, Jianyu Wang, Leping Xiao, Xing Fu, Lingyun Qiu, Zuoqiang Shi
   - Venue/status: **arXiv 2022**
   - Link: https://arxiv.org/abs/2211.15367
   - Contribution: few-shot/sparse active NLOS reconstruction using mixed-dimensional priors over measured transient signals, virtual confocal signals, and hidden-surface structure. It is especially relevant to very coarse confocal scans such as `5 x 5` relay grids.

## Repository changes made

- `README.md`
  - Added both papers to **Latest Additions**.
  - Labeled the arbitrary-pattern paper as **Nature Communications 2023** after verifying the Nature article page.
  - Kept the few-shot SSCR paper as **arXiv 2022**, since no final venue was verified in this run.

- `article/5newscenes.tex`
  - Added a new subsection: **Sparse and Irregular Active NLOS Acquisition**.
  - Integrated CC-SOCR arbitrary-pattern NLOS and few-shot SSCR as a coherent development path between classical dense relay scanning and newer arbitrary-relay / mobile NLOS acquisition.

- `article/6conclusion.tex`
  - Added sparse and irregular active acquisition to the conclusion's discussion of forward models and reconstruction infrastructure.

- `egbib_2026_updates.bib`
  - Added BibTeX entries:
    - `liuArbitraryPatternNLOS2023`
    - `liuFewShotSSCR2022`

## Website patch still recommended

I did **not** directly overwrite `index.html` in this run because the file is a compact, single-page website and the available GitHub connector still requires whole-file replacement. The current `index.html` already contains the Nature Communications arbitrary-pattern paper in the main active-paper list, but it should still be patched as follows:

1. Change the latest-entry count from `31` to `33`.
2. Add the few-shot SSCR paper to the `papers` JavaScript array, ideally near the arbitrary-pattern / sparse active acquisition entries:

```js
{cat:'latest active', title:'Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization', authors:'Xintong Liu et al.', year:2022, venue:'arXiv 2022', url:'https://arxiv.org/abs/2211.15367', key:'Few-shot active NLOS with signal-surface collaborative regularization and mixed-dimensional priors for very coarse relay scans.'},
```

3. Optionally add the arbitrary-pattern Nature Communications paper to the `latest` category as well, since README now treats it as a newly completed missing entry.
4. Fix stale website metadata that still appears in the current `index.html` snapshot:
   - `Soft Shadow Diffusion (SSD)` should be `arXiv 2026`, not `ECCV 2024`, unless an official venue is later verified.
   - Remove or quarantine the unverified `Polarization-Based Scanning-Free Single-Pixel NLOS Imaging` and `Super-Field-of-View NLOS via Spatial Encoding` entries unless metadata can be verified.

## PDF / LaTeX build status

The LaTeX source and BibTeX supplement were updated. The PDF was **not** regenerated in this run because the available tools do not provide a safe LaTeX compilation plus binary PDF upload path.

Important remaining build step:

```tex
\bibliography{egbib}
```

should be changed to:

```tex
\bibliography{egbib,egbib_2026_updates}
```

in `bare_jrnl.tex` before compiling the updated survey PDF.
