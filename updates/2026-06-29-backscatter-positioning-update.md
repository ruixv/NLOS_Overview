# Backscatter-assisted RF NLOS positioning update — 2026-06-29

This pass used keyword search plus forward/citation-style tracing around the repository's current RF/mmWave NLOS branch, especially N2LoS, RIS-assisted radar sensing, distributed MIMO/ISAC imaging, mmMirror, See and Beam, MITO, Park et al.'s T-junction localization work, and HoloRadar/GeRaF-style RF NLOS perception.

## Added to the LaTeX survey source

### Backscatter Assisted Indoor NLOS Positioning

- Authors: Kalle Ruttik, Huseyin Yigitler, Jingyi Liao, Alexander Sheverdyaev, Riku Jantti
- Status used here: arXiv 2026
- Link: https://arxiv.org/abs/2606.17325
- Why relevant: Uses passive backscatter devices as virtual anchors for indoor corridor NLOS positioning. It is not conventional hidden-shape reconstruction, but it is tightly adjacent to the repository's RF/mmWave NLOS branch because it converts multipath and passive environmental tags into useful NLOS localization evidence.
- Metadata decision: No reliable final conference/journal venue was found during this run, so the entry is labeled as arXiv 2026.

## Files updated safely

- `article/5newscenes.tex`
  - Expanded the Radar-Based NLOS Imaging subsection with Backscatter Assisted Indoor NLOS Positioning.
  - Connected it to N2LoS, mmMirror, See and Beam, MITO, Park et al., distributed MIMO/ISAC, and RIS-assisted radar as part of a broader RF/mmWave NLOS localization and environment-aware radio perception trend.

- `egbib_2026_updates.bib`
  - Added BibTeX key: `ruttikBackscatterNLOS2026`.

## README / website patch still needed

The current connector path still requires full-file replacement for large public-facing files. To avoid truncating or overwriting the manually curated README and homepage, I did not overwrite `README.md` or `index.html` in this run. Suggested additions:

### Add to `README.md` Latest Additions near the 2026 RF/mmWave entries

```markdown
| 2026 | [Backscatter Assisted Indoor NLOS Positioning](https://arxiv.org/abs/2606.17325) — Ruttik et al. | arXiv 2026 | Uses passive backscatter devices as virtual anchors for robust indoor corridor NLOS positioning. |
```

### Add to `README.md` Radar / RF / mmWave NLOS table

```markdown
| [Backscatter Assisted Indoor NLOS Positioning](https://arxiv.org/abs/2606.17325) — Ruttik et al. | arXiv 2026 | Passive asynchronous backscatter devices as virtual anchors for sub-meter indoor NLOS corridor tracking. |
```

### Add to `index.html`

Add a corresponding paper-explorer card and RF/mmWave timeline/taxonomy entry. If it is exposed in the homepage latest list, increase the latest-additions count accordingly.

## Related candidates checked but not added

- `Lightweight Non-Line-of-Sight Channel Detection for ML-assisted Bluetooth Direction Finding` (arXiv 2026): rejected for now because it is LOS/NLOS channel classification for Bluetooth direction finding, not NLOS imaging, hidden-scene perception, or RF NLOS reconstruction/localization in the sense used by the repository.
- `Multi-modal Data Driven Virtual Base Station Construction for Massive MIMO Beam Alignment` (arXiv 2026): rejected for now because it mainly targets beam alignment/connectivity. It uses LiDAR-derived reflector geometry, but the NLOS component is communication-channel modeling rather than hidden-space sensing or reconstruction.

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The source-side integration is complete for this paper, but the root `bare_jrnl.tex` still needs the bibliography line changed from:

```latex
\bibliography{egbib}
```

to:

```latex
\bibliography{egbib,egbib_2026_updates}
```

After that, run the LaTeX/BibTeX compilation sequence and upload the regenerated PDF. This run did not have a verified local LaTeX build path or a safe binary PDF upload path, so no PDF update is claimed.