# 22 August 2026 — X-band Radar public-artifact consistency audit

**Integrated by guarded workflow.** The audit confirmed that the canonical README paper entry, V2 Paper Explorer object, survey citation, and final-venue BibTeX record were already present. The actual public-facing gap was that the 2026 development timeline did not explicitly place the X-band result in the RF/NLOS trajectory. The guarded workflow added that timeline context and rebuilt/revalidated the survey PDF without duplicating the existing paper records.

## Finding

A repository-wide audit rechecked **Du et al., “X-band Radar Non-Line-of-Sight Imaging,” CVPR 2026, pp. 5647–5658** after later public-file rewrites. The paper remains correctly integrated in `article/5newscenes.tex` through citation key `duXBandRadarNLOS2026`, remains present as a canonical final-venue BibTeX entry in `egbib_merged_20260711.bib`, and is already present in both `README.md` and the canonical V2 corpus `data/papers-source.html`. The missing piece was explicit placement in the V2 2026 development timeline.

Primary-source metadata is the CVPR 2026 Open Access record:
`https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html`.

The verified contribution summary is: X-band operation makes common relay interactions substantially more specular than optical/77-GHz sensing; a learned dense-prediction stage followed by geometry-aware recovery reconstructs hidden objects, and the prototype demonstrates real-world NLOS reconstruction at ranges up to 40 m.

## Guarded audit/repair behavior

The integration helper `scripts/repair_xband_public_consistency_20260822.py` was intentionally idempotent. In the clean checkout it:

1. Asserted that `article/5newscenes.tex` already cites `duXBandRadarNLOS2026`.
2. Asserted that `egbib_merged_20260711.bib` contains exactly one final CVPR entry with pages 5647–5658 and the CVF publication URL.
3. Detected the existing README entry and therefore did not duplicate it.
4. Detected the existing canonical V2 Paper Explorer object and therefore did not duplicate it.
5. Added the missing concise 2026 timeline sentence and rechecked the V2 tracked-entry count.
6. Added only a provenance comment to `bare_jrnl.tex`; it did not duplicate the existing survey prose or BibTeX record.
7. Clean-built `bare_jrnl.pdf` and passed citation, semantic PDF-text, and endpoint-rendering checks before the public commit was created.

Public integration commit: `0eeec751b83e176a29a9e7c3ea23e9f93aaa19c9` (`Restore X-band radar public survey entry`). The commit title is retained for history; this note records the more precise result of the idempotent audit.
