# 31 July 2026 LEAP final-venue correction

A fresh citation and venue audit did not verify a direct NLOS-imaging paper published later than 22 July 2026. The newest verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* in *Nature Communications*, which is already covered by the repository.

The audit found one Core-paper metadata inconsistency. **Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging (LEAP)** is still labeled as an arXiv-only 2024 work in parts of the repository. Its verified final record is:

- Venue: ECCV 2024
- Proceedings: *Computer Vision -- ECCV 2024*, LNCS 15101
- Pages: 72--89
- DOI: `10.1007/978-3-031-72775-7_5`
- Existing citation key: `choLEAP2024`

The highest-priority source correction is stored in `egbib_20260731_zz_leap_final_venue.bib`. The citation key is intentionally unchanged.

The remaining bounded public-artifact edits are:

1. In `README.md`, replace the LEAP arXiv URL and `arXiv 2024` venue label with the DOI URL and `ECCV 2024, LNCS 15101, 72--89`.
2. In the existing LEAP object in `index.html`, replace the arXiv URL and venue with the DOI URL and `ECCV 2024`. No duplicate explorer entry should be added.
3. Regenerate `egbib_merged_20260711.bib` so the final `@inproceedings` record supersedes the arXiv-only entry.
4. Rebuild `bare_jrnl.pdf` and confirm that the rendered bibliography contains the ECCV record.
5. Apply the already documented CA-SlotNet, LMS-NLOS, MSPDiff, and Suenobu RF inverse-scattering insertions from `updates/20260731_passive_learning_citation_trace.md` and `updates/20260731_rf_inverse_scattering_and_consistency.md` in the same guarded edit.

`README.md`, `index.html`, the survey section files, the consolidated bibliography, and `bare_jrnl.pdf` are not claimed as synchronized by this commit. The available write action only supports complete replacement of those large files, and the connector returned truncated snapshots; overwriting them would risk silent data loss.
