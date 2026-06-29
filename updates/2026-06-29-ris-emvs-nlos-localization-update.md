# 2026-06-29 Update: RIS/EMVS NLOS Localization

## Newly added candidate

### Beyond $\lambda/2$: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?
- **Authors:** Hua Chen, Zhenhao Yu, Tuo Wu, Wei Liu, Maged Elkashlan, Hyundong Shin, Matthew C. Valenti, Robert Schober
- **Status:** arXiv 2026
- **arXiv:** https://arxiv.org/abs/2602.07515
- **Category:** Radar / RF / mmWave NLOS; RIS-assisted NLOS localization; array-geometry design
- **Reason for inclusion:** The paper is not hidden-shape reconstruction, but it is tightly adjacent to the repository's RF/mmWave NLOS sensing and localization branch. It studies RIS-aided NLOS bistatic MIMO radar and asks whether arbitrary electromagnetic vector sensor (EMVS) arrays can remain unambiguous beyond the conventional $\lambda/2$ inter-element spacing constraint. This complements the existing N2LoS / RIS radar / distributed MIMO-ISAC / mmMirror / See and Beam line by adding the array-design and polarimetric ambiguity-resolution perspective.

## Metadata decision

No final journal or conference venue was verified in this run. The entry is therefore labeled **arXiv 2026**.

## Applied repository changes

### `article/5newscenes.tex`

Integrated the work into the `Radar-Based NLOS Imaging` subsection. The paragraph now places Chen et al. together with MITO, N2LoS, Backscatter-assisted NLOS positioning, camera-assisted mmWave pedestrian localization, distributed MIMO/ISAC, RIS-assisted radar, mmMirror, and See and Beam.

### `egbib_2026_updates.bib`

Added:

```bibtex
@misc{chenBeyondLambdaEMVS2026,
  title   = {Beyond $\lambda/2$: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?},
  author  = {Chen, Hua and Yu, Zhenhao and Wu, Tuo and Liu, Wei and Elkashlan, Maged and Shin, Hyundong and Valenti, Matthew C. and Schober, Robert},
  year    = {2026},
  eprint  = {2602.07515},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/2602.07515}
}
```

## README patch to apply when safe

Because direct full-file replacement of `README.md` risks overwriting unrelated recent content, the following patch is recorded instead of blindly replacing the file.

### Latest Additions

Insert near the other 2026 RF/mmWave entries:

```markdown
| 2026 | [Beyond $\lambda/2$: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?](https://arxiv.org/abs/2602.07515) — Chen et al. | arXiv 2026 | RIS-aided bistatic MIMO radar localization with arbitrary EMVS arrays; uses polarimetric measurements and PARAFAC-style factorization to resolve phase ambiguities beyond the conventional $\lambda/2$ spacing limit. |
```

### Milestone Timeline

Add below the 2026 RIS/distributed-MIMO lines:

```markdown
        Chen et al.: EMVS/RIS-aided NLOS localization beyond the λ/2 array-spacing limit
```

### New NLOS Scenes and Modalities → Radar / RF / mmWave NLOS

Add after the RIS-assisted radar line:

```markdown
| [Beyond $\lambda/2$: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?](https://arxiv.org/abs/2602.07515) — Chen et al. | arXiv 2026 | RIS-aided NLOS bistatic MIMO radar localization with arbitrary EMVS arrays and polarimetric phase-disambiguation beyond the conventional $\lambda/2$ spacing limit. |
```

## Website patch to apply when safe

Add this object to the `papers` array in `index.html` near the other RF/mmWave modality entries:

```javascript
{cat:'latest modality', title:'Beyond λ/2: Can Arbitrary EMVS Arrays Achieve Unambiguous NLOS Localization?', authors:'Chen et al.', year:2026, venue:'arXiv', url:'https://arxiv.org/abs/2602.07515', key:'RIS-aided NLOS bistatic MIMO radar localization with arbitrary EMVS arrays and polarimetric phase-disambiguation beyond the conventional λ/2 spacing limit.'},
```

## Not added after screening

- **Sensing-Assisted LoS/NLoS Identification in Dynamic UAV Positioning Systems**: useful for communication-assisted localization, but mainly a LoS/NLoS classifier rather than NLOS hidden-scene imaging or reconstruction/localization using an exploitable indirect propagation path.
- **A New Location Estimator for Mixed LOS & NLOS scenarios** and **Optimal Anchor Placement for Wireless Localization in Mixed LOS and NLOS Scenarios**: relevant to general wireless localization theory, but too broad for the current NLOS imaging/perception survey unless the RF localization branch is intentionally expanded further.
- **Non-Line-of-Sight Confocal Spectromicroscopy for SiC Micropipe Sidewalls**: uses a non-line-of-sight optical probing phrase, but the target application is semiconductor defect spectroscopy rather than hidden-scene NLOS imaging.

## PDF build status

The LaTeX source and BibTeX supplement were updated, but `bare_jrnl.pdf` was not regenerated in this run. The remaining build prerequisite is still to change `bare_jrnl.tex` from:

```tex
\bibliography{egbib}
```

to:

```tex
\bibliography{egbib,egbib_2026_updates}
```

Then run BibTeX/LaTeX locally and upload the regenerated PDF.
