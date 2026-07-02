# 2026-07-02 README sync: pending RF/ISAC, passive acoustic, and active focusing entries

This automation run did not find a newer high-confidence optical/transient NLOS imaging paper beyond the already tracked July 2026 frontier entries. Keyword search and citation-oriented checks mainly returned papers already present in the current README or already recorded in prior update notes.

## Public README entries synchronized in this run

The current README was missing several entries that had already been metadata-verified and added to supplemental BibTeX / update notes. This run synchronized the README Latest Additions table with the following entries:

1. **Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware** — Tosi et al., arXiv 2026, `https://arxiv.org/abs/2604.07032`.
2. **Cramer-Rao Bounds for Target Parameter Estimation in a Bi-Static IRS-Assisted Radar Configuration** — Sanjeeva Reddy S and Vinod Veera Reddy, arXiv 2026, `https://arxiv.org/abs/2603.01660`.
3. **RIS-aided Radar Detection Architectures with Application to Low-RCS Targets** — Colone et al., arXiv 2026, `https://arxiv.org/abs/2601.10846`.
4. **Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources** — Boger-Lombard et al., Scientific Reports 2023, `https://www.nature.com/articles/s41598-023-31490-2`.
5. **High-resolution non-line-of-sight imaging employing active focusing** — Cao et al., Nature Photonics 2022, `https://www.nature.com/articles/s41566-022-01009-8`.
6. **Cramer-Rao Lower Bound Optimization for Hidden Moving Target Sensing via Multi-IRS-Aided Radar** — Esmaeilbeig et al., arXiv 2022, `https://arxiv.org/abs/2210.05812`.

## Repository updates performed

- `README.md` was updated to include the six entries above in the Latest Additions table.
- No new BibTeX was needed: all six corresponding BibTeX entries were already present in `egbib_20260702_updates.bib`.
- `article/2active.tex` already contains the Cao et al. active-focusing discussion and cites `caohighresolutionnlos2022`.

## Remaining consistency work

The website and survey PDF still need the following follow-up work before all public artifacts are fully consistent:

1. Update `index.html` latest count from **40** to **46** and add the six paper objects above to the JavaScript `papers` array.
2. Extend the 2026 timeline sentence to mention ISAC intrusion detection, IRS/CRB estimation bounds, and RIS-aided low-RCS detection.
3. Extend the 2023 timeline sentence to mention passive acoustic correlation-based NLOS localization.
4. Extend the 2022 timeline sentence to mention active focusing / UNCOVER and multi-IRS hidden-target sensing.
5. Add short RF/ISAC and passive-acoustic sentences to `article/5newscenes.tex` if not already covered elsewhere.
6. Compile the survey only after `bare_jrnl.tex` is changed from:

```tex
\bibliography{egbib}
```

to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates}
```

The PDF was not regenerated in this run because the available GitHub connector does not provide a safe LaTeX compilation and binary PDF upload path.
