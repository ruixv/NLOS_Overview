# 2026-10-24: Final-venue deduplication and explorer count audit

After adding the verified 2020 moving-relay NLOS milestone, the Paper Explorer had 403 records but only 396 distinct normalized paper titles. Seven repeated the same research work, sometimes as a later arXiv upload alongside an already verified final journal publication.

We retained the richer, final-venue explorer record in every case and deleted only the redundant second entry:
- Yasmeen et al., *Around-the-Corner Radar Sensing Using Reconfigurable Intelligent Surface* — IEEE MAPCON 2024 (same DOI in both records).
- Yasmeen et al., *Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface* — IEEE RadarConf25 2025 (same DOI in both).
- Dove and Shapiro, *Paraxial theory of phasor-field imaging* — *Optics Express* 2019; removed separate arXiv catalog alias.
- Dove and Shapiro, *Paraxial phasor-field physical optics* — *Optics Express* 2020; removed separate arXiv alias.
- Dove and Shapiro, *Nonparaxial phasor-field propagation* — *Optics Express* 2020; removed separate arXiv alias.
- Sun et al., *CUDA-accelerated non-line-of-sight imaging with irregular relay surfaces* — *Optics and Lasers in Engineering* 2026 (same DOI in both).
- Mu et al., *Physics to the Rescue: Deep Non-Line-of-Sight Reconstruction for High-Speed Imaging* — *IEEE TPAMI* 2025 (same DOI in both).

After removal: **396 explorer records, 396 distinct normalized titles, 369 records categorized as latest, and no repeated DOI among explorer records that provide DOI links**. Retained source records have the accurate publisher links and stronger contribution descriptions. Site statistics were updated to 390+ curated papers and 369 latest items; the README papers badge was changed from its obsolete 210+ value to the conservative 390+.

The changes are catalog/UI-only. No survey citation or bibliography was removed; no LaTeX source changed and the regenerated PDF from the preceding dynamic-relay paragraph remains applicable. An unrelated historical PR synchronization job can fail because `scripts/sync_nlos_20260718_passive_geometry.py` assumes the retired "geometry-constrained homepage record" is present; it should be repaired separately rather than blindly replaying stale synchronizers against the modern website.
