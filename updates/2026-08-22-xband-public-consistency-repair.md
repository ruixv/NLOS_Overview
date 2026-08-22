# 22 August 2026 — X-band Radar public-artifact consistency repair

**Integrated by guarded workflow.** The public README/V2 regression is repaired; the existing survey citation/BibTeX are preserved and the survey PDF is rebuilt and revalidated.

## Finding

A repository-wide audit found a cross-artifact regression for **Du et al., “X-band Radar Non-Line-of-Sight Imaging,” CVPR 2026, pp. 5647–5658**. The paper is still correctly integrated in `article/5newscenes.tex` through citation key `duXBandRadarNLOS2026`, remains present as a canonical final-venue BibTeX entry in `egbib_merged_20260711.bib`, and was previously integrated into the public repository in July 2026. However, later public-file rewrites removed its explicit paper entry from both `README.md` and the canonical V2 corpus `data/papers-source.html`.

Primary-source metadata is the CVPR 2026 Open Access record:
`https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html`.

The verified contribution summary is: X-band operation makes common relay interactions substantially more specular than optical/77-GHz sensing; a learned dense-prediction stage followed by geometry-aware recovery reconstructs hidden objects, and the prototype demonstrates real-world NLOS reconstruction at ranges up to 40 m.

## Guarded repair

Run `scripts/repair_xband_public_consistency_20260822.py` in a clean checkout. It must:

1. Assert that `article/5newscenes.tex` already cites `duXBandRadarNLOS2026`.
2. Assert that `egbib_merged_20260711.bib` contains exactly one final CVPR entry with pages 5647–5658 and the CVF publication URL.
3. Restore one README Latest-Additions row.
4. Restore one canonical V2 Paper Explorer object and one concise 2026 timeline sentence.
5. Recompute the V2 tracked-entry count from the canonical object array.
6. Add only a provenance comment to `bare_jrnl.tex`; do not duplicate the existing survey prose or BibTeX record.
7. Clean-build `bare_jrnl.pdf` and validate the citation, semantic PDF text, and endpoint rendering before committing public artifacts.

The repair is intentionally idempotent and fail-closed so a later run cannot create duplicate X-band records.
