# 2026-06-29 Double-Bounce Radio SLAM NLOS Update

## Newly integrated paper

- **Exploiting Double-Bounce Paths in Snapshot Radio SLAM: Bounds, Algorithms and Experiments**  
  Xi Zhang, Yu Ge, Ossi Kaltiokallio, Musa Furkan Keskin, Henk Wymeersch, Mikko Valkama.  
  arXiv:2603.02832, 2026.  
  URL: https://arxiv.org/abs/2603.02832

## Why it was added

The paper is not a classical optical hidden-shape reconstruction method, but it is a strong fit for the repository's expanding **Radar / RF / mmWave NLOS localization, mapping, and sensing** branch. It explicitly treats higher-order NLoS propagation as useful information rather than nuisance multipath. In particular, it shows that double-bounce NLoS paths can improve snapshot radio SLAM and reveal landmarks that are not observable from single-bounce paths alone.

## Metadata decision

No reliable final journal or conference venue was found during this run, so the entry is labeled **arXiv 2026**.

## Files updated

- `article/5newscenes.tex`  
  Added Zhang et al. to the RF/mmWave NLOS paragraph and updated the summary sentence to include higher-order radio-SLAM multipath exploitation.

- `egbib_2026_updates.bib`  
  Added BibTeX key: `zhangDoubleBounceRadioSLAM2026`.

- `README.md`  
  Synced the Latest Additions table with this run and previous recent additions that had been recorded in update notes but not yet reflected in the README, including DENALI, MITO, Park et al., mmMirror, See and Beam, Backscatter-assisted positioning, Chen et al. EMVS/RIS localization, SuperEx, mitransient, structure-sparsity NLOS, active corner camera, THz NLOS, and PRL picosecond NLOS.

- `index.html`  
  Synced the homepage latest-entry count and searchable paper explorer with the same set of latest additions.

## PDF / LaTeX build status

The LaTeX source subfiles and bibliography supplement were updated, but `bare_jrnl.pdf` was **not regenerated** in this run. The available GitHub connector supports safe text-file updates but does not provide a safe binary-PDF upload path or a LaTeX build environment. The remaining build step is:

```tex
% in bare_jrnl.tex
\bibliography{egbib,egbib_2026_updates}
```

followed by a local LaTeX/BibTeX build and upload of the regenerated `bare_jrnl.pdf`.

## Consistency note

After this update, README, homepage, `article/5newscenes.tex`, and `egbib_2026_updates.bib` are aligned for the newly added double-bounce radio-SLAM entry and the previously accumulated recent additions. The remaining inconsistency is that `bare_jrnl.pdf` has not been regenerated from the updated source and bibliography supplement.
