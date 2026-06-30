# 2026-06-30 Update: TransiT NLOS Videography Sync

## Added / synchronized

### 1. TransiT: Transient Transformer for Non-line-of-sight Videography

- **Authors:** Ruiqian Li, Siyuan Shen, Suan Xia, Ziheng Wang, Xingyue Peng, Chengxuan Song, Yingsheng Zhu, Tao Wu, Shiying Li, Jingyi Yu
- **Year / status:** arXiv 2025
- **arXiv:** https://arxiv.org/abs/2503.11328
- **Reason for inclusion:** This is a direct dynamic / video NLOS reconstruction paper and is already discussed in `article/4datadriven.tex` through `\cite{liTransiT2025}`, but it was missing from the README Latest Additions table. It is also part of the transformer-based dynamic NLOS line together with NLOST, ST-Mamba, and TRT/TRT-NLOS.
- **Metadata decision:** No reliable final conference/journal venue was verified during this run, so it is labeled as **arXiv 2025**.

## Repository changes made in this run

- `README.md`: added TransiT to Latest Additions.

## Remaining safe patches

The following patches should still be applied when a safe patch-only or full-file-edit path is available.

### 1. Add BibTeX entry to `egbib_2026_updates.bib`

```bibtex
@misc{liTransiT2025,
  title   = {TransiT: Transient Transformer for Non-line-of-sight Videography},
  author  = {Li, Ruiqian and Shen, Siyuan and Xia, Suan and Wang, Ziheng and Peng, Xingyue and Song, Chengxuan and Zhu, Yingsheng and Wu, Tao and Li, Shiying and Yu, Jingyi},
  year    = {2025},
  eprint  = {2503.11328},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/2503.11328}
}
```

This is important because `article/4datadriven.tex` already cites `liTransiT2025` in the transformer-based networks, generalization, and dynamic NLOS paragraphs.

### 2. Add TransiT to `index.html`

In the `papers` JavaScript array, insert near the other 2025 learning / transient transformer entries:

```javascript
{cat:'latest learning active', title:'TransiT: Transient Transformer for Non-line-of-sight Videography', authors:'Ruiqian Li et al.', year:2025, venue:'arXiv 2025', url:'https://arxiv.org/abs/2503.11328', key:'Transient transformer for high-speed NLOS videography, reconstructing 10 fps videos from sparse 16×16 transient scans with transfer learning for synthetic-to-real adaptation.'},
```

Also update the latest-entry count from `31` to `32`, and optionally mention TransiT in the 2025 timeline item alongside TRT, NANO, MARMOT, and ST-Mamba.

### 3. Keep `bare_jrnl.tex` bibliography synchronized

The PDF build still requires the main file to include the supplement bibliography:

```tex
\bibliography{egbib,egbib_2026_updates}
```

instead of

```tex
\bibliography{egbib}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The current blocker is still the lack of a safe LaTeX compilation and binary PDF upload path in the available tool environment. Once the BibTeX patch above and the bibliography-line patch in `bare_jrnl.tex` are applied, the survey should be recompiled and the generated `bare_jrnl.pdf` uploaded.
