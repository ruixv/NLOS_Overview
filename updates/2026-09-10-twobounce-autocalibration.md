# 2026-09-10 NLOS literature update: two-bounce auto-calibration gap

## Newly verified missing paper

Xiaoyu Chen, Taiping Lu, Kun Li, Huawei Chen, Jingyuan Zhang, Jing Han, **"Automatic calibration under non-planar illumination wall in two-bounce non-line-of-sight imaging,"** *Optics & Laser Technology*, vol. 204, article 116183, 2026. DOI: 10.1016/j.optlastec.2026.116183.

This work was found during forward-citation tracing from the recent two-bounce / neural-illumination-field lineage. It is genuinely NLOS imaging rather than generic calibration: it establishes a relative coordinate mapping between the two relay-wall surfaces, automatically acquires ray representations for two-bounce shadow imaging when the illumination wall is non-planar, and uses a full-link MLP optimization to correct spot-position and wall-unevenness errors. Reported real-scene scale is 2.37 m x 4.6 m x 3.1 m, with 2 cm lateral resolution and mean point-wise AbsRel 0.0248 over eight sampled real-world points.

## Required cross-artifact integration

### README.md

Insert near the recent two-bounce / deployment-oriented entries in **Latest Additions**:

```markdown
| 2026 | [Automatic calibration under non-planar illumination wall in two-bounce non-line-of-sight imaging](https://doi.org/10.1016/j.optlastec.2026.116183) — Chen et al. | Optics & Laser Technology 204, 116183 (2026) | Removes the pre-calibrated planar-wall assumption from two-bounce shadow NLOS by automatically estimating the relative mapping between two relay surfaces and refining rays/shadows with full-link MLP optimization; real experiments cover a 2.37 m × 4.6 m × 3.1 m scene with 2 cm lateral resolution. |
```

Add a 2026 timeline point after Neural Illumination Fields / D-NeSF, emphasizing the deployment trajectory:

`Chen et al.: automatic calibration for non-planar two-bounce relay walls removes a major geometric-calibration barrier [Optics & Laser Technology]`.

### article/5newscenes.tex / bare_jrnl.tex survey

Integrate semantically in the **Two-bounce NLOS imaging** subsection, after the Neural Illumination Fields and D-NeSF discussion rather than appending it to an unrelated methods list. Suggested survey sentence:

```latex
Moving two-bounce NLOS toward less controlled deployment, Chen~\etal~remove the assumption that the illumination wall is planar and pre-calibrated~\cite{chenAutoCalibrationTwoBounce2026}. Their method automatically estimates the relative coordinate mapping between the two relay surfaces and then jointly refines ray vectors and shadow formation with a full-link MLP optimization, compensating for spot-position errors and wall unevenness. This shifts the two-bounce trajectory from increasingly expressive neural scene representations toward self-calibrating acquisition on irregular real relay geometry.
```

Also add a dated consistency comment to `bare_jrnl.tex` once the citation is wired into the canonical bibliography.

### Bibliography

Verified staging entry is in `egbib_20260910_twobounce_autocalibration.bib`. Merge it into `egbib_merged_20260711.bib` with key `chenAutoCalibrationTwoBounce2026`, or include this staging database in the `\bibliography{...}` declaration until the next canonical merge. Do not leave the survey citation unresolved.

### index.html / Paper Explorer / Latest Additions / Timeline

Add the same final-venue metadata and DOI. Categorize as `Active NLOS`, `Two-bounce / shadow imaging`, and `Calibration / irregular relay geometry`. The short contribution summary should stress automatic two-wall coordinate calibration, non-planar illumination surfaces, MLP refinement of ray/shadow geometry, and real-room validation.

### Existing consistency debt to resolve in the same safe full-file pass

1. `olgunAcousticIdentityNLOS2026` is already integrated in README and `article/5newscenes.tex` but its verified BibTeX still lives in `egbib_20260909_acoustic_identity.bib`; merge it into the canonical bibliography or add that database to `bare_jrnl.tex`.
2. `sultanIteratingTLTM2024` should use the final *Nature Communications* 2026 metadata: volume 17, article 8951, DOI `10.1038/s41467-026-75177-4`, published 22 July 2026. The survey prose is already present.
3. `weiQuasiFresnel2026` should use final *Optica* metadata rather than "accepted": volume 13, issue 9, pages 1785--1795 (2026), DOI `10.1364/OPTICA.604217`; remove any duplicate arXiv-only record if still present.

## PDF rebuild / consistency check

After the canonical bibliography and survey citation are wired, run BibTeX + LaTeX to regenerate `bare_jrnl.pdf`, then verify that README, index.html, article/5newscenes.tex, bare_jrnl.tex, the bibliography and PDF all expose the same venue/year/title and that no newly cited key is undefined.

This update note is intentionally patch-style because the current connector can safely create small verified files but whole-file replacement of the large README/index/survey/bibliography without a complete untruncated source snapshot would risk truncation or data loss.
