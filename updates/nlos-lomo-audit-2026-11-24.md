# NLOS candidate audit — 2026-11-24

## Candidate requiring cross-artifact integration

**Locating Motionless Human in Through-Wall NLOS Scenarios With a Commercial mmWave Device**. *IEEE Transactions on Human-Machine Systems*, 56(3), 602–614 (June 2026). Online publication: 8 April 2026. DOI: https://doi.org/10.1109/THMS.2025.3633627 . Official IEEE abstract: https://xplorestaging.ieee.org/document/11477882 .

**Scope:** The LoMo method uses coherent accumulation of weak physiological radar echoes, Toeplitz-covariance super-resolution to separate multipath, and adaptive clustering to locate stationary people behind obstacles. This is **through-wall NLOS localization / radar sensing**, not a full hidden-surface 3D imaging method. Its reported localization error is within 17 cm, with a 96.1% correct-identification rate within a ±30 cm tolerance under tested through-wall NLOS conditions. Consider for the radar/RF/mmWave NLOS sensing timeline and the survey's *New NLOS Scenes* radar subsection, explicitly distinguishing localization from scene reconstruction.

**Repository check:** Exact-title/LoMo GitHub code searches of master returned no matches on 24 Nov 2026, but code-search indexing is not an exhaustive proof of absence. README.md, data/papers-source.html, bare_jrnl.tex and article/5newscenes.tex were fetched with blob SHA; full-file duplicate and bibliography-key audit is still needed before integrating. Do not overwrite large files from excerpts.

**Suggested BibTeX staging (metadata verified against publisher):**
```bibtex
@article{lomo_throughwall_2026,
  title = {Locating Motionless Human in Through-Wall NLOS Scenarios With a Commercial mmWave Device},
  journal = {IEEE Transactions on Human-Machine Systems},
  volume = {56},
  number = {3},
  pages = {602--614},
  year = {2026},
  doi = {10.1109/THMS.2025.3633627}
}
```
Authors omitted intentionally pending publisher-author metadata verification.

## Integration and build status

No changes to README, website, LaTeX, bibliography, or PDF in this branch. Prior unresolved audit branches for consumer Flash LiDAR, mmWave pedestrian recognition, and ToF ReSTIR should be reconciled before creating overlapping edits. After source integration, run a full LaTeX/BibTeX build, inspect undefined citations, and verify PDF content and repository commit before publishing. Do not claim the PDF is rebuilt based on a binary diff alone.

## Exclusions

- *Geometric Consensus Convolutional Neural Network for NLOS Identification via Range-Only Measurements in High-GDOP Conditions* (IEEE Communications Letters, 2026; DOI 10.1109/LCOMM.2026.3731212) is NLOS-link classification for ranging, not hidden-scene imaging.
- *Large-array sub-millimeter precision coherent flash three-dimensional imaging* (Nature Communications, 2026) is LOS coherent LiDAR without verified around-corner NLOS imaging.

## Citation tracing

A limited phasor-field/f-k forward-citation-oriented search surfaced the already catalogued GPU pipeline work (arXiv:2608.28183). Full citation-database pagination across all Core seeds is not complete and should not be represented as exhaustive.
