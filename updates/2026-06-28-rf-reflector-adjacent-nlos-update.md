# RF reflector-adjacent NLOS update — 2026-06-28

This update pass used keyword search plus citation/context tracing around RF/mmWave and NLOS perception papers already treated as core or emerging milestones in the repository. No new high-confidence optical transient NLOS paper beyond the existing README/homepage snapshot was found in this pass. Two adjacent RF/mmWave NLOS works were judged worth integrating because they explicitly use engineered or naturally occurring reflectors to make non-line-of-sight RF sensing/localization deployable.

## Added to the LaTeX survey source

### 1. mmMirror: Device Free mmWave Indoor NLoS Localization Using Van-Atta-Array IRS

- Authors: Yihe Yan, Zhenguo Shi, Yanxiang Wang, Cheng Jiang, Chun Tung Chou, Wen Hu
- Status used here: arXiv 2025
- Link: https://arxiv.org/abs/2505.10816
- Why relevant: Uses a Van-Atta-array IRS with commodity FMCW radars to support device-free around-corner / NLoS localization with centimeter-level accuracy. This is not full hidden-shape imaging, but it is highly relevant to the repository's RF/mmWave NLOS branch because it treats reflector engineering as part of the NLOS sensing system.

### 2. See and Beam: Leveraging LiDAR Sensing and Specular Surfaces for Indoor mmWave Connectivity

- Authors: Raj Sai Sohel Bandari, Amod Ashtekar, Omar Ibrahim, Mohammed E. Eltayeb
- Status used here: arXiv 2025
- Link: https://arxiv.org/abs/2511.09840
- Why relevant: Uses LiDAR-visible specular surfaces to map NLoS geometry, identify mmWave reflection points, localize NLoS users, and steer 60 GHz beams. It is adjacent to NLOS imaging rather than a conventional reconstruction paper, but it strengthens the survey's discussion of reflector-aware RF/mmWave NLOS perception.

No reliable final accepted/published venue was found for either item during this run, so both are labeled as arXiv.

## Files updated safely

- `article/5newscenes.tex`
  - Expanded the Radar-Based NLOS Imaging subsection with mmMirror and See and Beam.
  - The new text connects engineered IRS/Van-Atta reflectors and naturally occurring specular reflectors to broader NLOS sensing, localization, mapping, and communication/sensing.

- `egbib_2026_updates.bib`
  - Added BibTeX keys:
    - `yanMmMirror2025`
    - `bandariSeeBeam2025`

## README / website patch still needed

The GitHub connector path available in this run still requires full-file replacement for large files. To avoid truncating or overwriting the manually curated README and website, I did not overwrite `README.md` or `index.html`. Suggested README additions:

### Add to `README.md` Latest Additions, near other 2025 RF/mmWave entries

```markdown
| 2025 | [mmMirror: Device Free mmWave Indoor NLoS Localization Using Van-Atta-Array IRS](https://arxiv.org/abs/2505.10816) — Yan et al. | arXiv 2025 | Uses a Van-Atta-array IRS with commodity FMCW radars for device-free around-corner / NLoS localization. |
| 2025 | [See and Beam: Leveraging LiDAR Sensing and Specular Surfaces for Indoor mmWave Connectivity](https://arxiv.org/abs/2511.09840) — Bandari et al. | arXiv 2025 | Uses LiDAR-visible specular surfaces to infer NLoS mmWave reflection paths, localize NLoS users, and steer beams. |
```

### Add to `README.md` Radar / RF / mmWave NLOS table

```markdown
| [mmMirror: Device Free mmWave Indoor NLoS Localization Using Van-Atta-Array IRS](https://arxiv.org/abs/2505.10816) — Yan et al. | arXiv 2025 | Van-Atta-array IRS + commodity FMCW radar for device-free around-corner localization. |
| [See and Beam: Leveraging LiDAR Sensing and Specular Surfaces for Indoor mmWave Connectivity](https://arxiv.org/abs/2511.09840) — Bandari et al. | arXiv 2025 | LiDAR-guided specular-reflector mapping for NLoS mmWave user localization and beam steering. |
```

### Add to `index.html`

Add corresponding paper-explorer cards and RF/mmWave timeline/taxonomy entries. Increase the latest-additions count if these two entries are exposed in the homepage latest list.

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The source-side integration is complete for these two papers, but the root `bare_jrnl.tex` still needs the bibliography line changed from:

```latex
\bibliography{egbib}
```

to:

```latex
\bibliography{egbib,egbib_2026_updates}
```

After that, run the LaTeX/BibTeX compilation sequence and upload the regenerated PDF. This run did not have a safe patch-only update path for `bare_jrnl.tex` or a verified PDF binary upload path, so no PDF update is claimed.
