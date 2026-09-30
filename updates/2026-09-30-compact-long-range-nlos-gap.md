# Integration note: Compact non-line-of-sight imager at long range

## Verified missing paper

Jianwei Zeng, Chen Dai, Zhongpei Xiao, Yutao Chen, Wenwen Li, and Feihu Xu, “Compact non-line-of-sight imager at long range,” *Optics Express*, 34(9):16911–16921, 2026. DOI: 10.1364/OE.597084.

Verified against PubMed/Optica metadata. Repository-wide exact-title and DOI searches on the default branch returned no match before staging.

## Why it belongs

This is a practical active/ToF NLOS systems milestone rather than a marginal NLOS citation. It reports a compact integrated outdoor NLOS prototype combining optimized collection optics, adaptive temporal gating, high-transmittance optics, and fast control electronics. The system demonstrates daylight kilometer-range NLOS imaging and simple-target imaging at 2 fps; the paper reports roughly 4 cm spatial resolution at kilometer scale. Reconstruction uses a phasor-field algorithm, directly connecting the system contribution to a core NLOS reconstruction lineage.

## Recommended integration

- **README.md:** add to the 2026 active/ToF and practical/long-range systems timeline. Suggested summary: “Compact daylight kilometer-range NLOS prototype with adaptive gating and integrated high-efficiency optics; demonstrates 2-fps simple-target imaging and ~4-cm spatial resolution at kilometer scale.”
- **index.html / Paper Explorer:** add under Active / ToF / Long-range systems and Latest Additions. Emphasize the transition from laboratory transient imaging toward compact outdoor deployment.
- **bare_jrnl.tex:** integrate semantically in the active NLOS systems/practical deployment discussion, near long-range and scan-free/parallel sensing work. A useful trajectory sentence is that recent work increasingly shifts the bottleneck from inverse reconstruction alone to photon efficiency, background suppression, gating, calibration, and integrated system design for outdoor operation.
- **Bibliography:** merge the verified entry from `egbib_20260930_compact_long_range_nlos.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- **bare_jrnl.pdf:** rebuild only after the canonical TeX and bibliography are safely integrated; verify the citation resolves and the PDF contains the new discussion.

## Consistency status

This note and a verified BibTeX staging file are committed. Canonical README/index/TeX/PDF were not overwritten from partial large-file payloads. They remain to be integrated in a later safe full-file edit/build pass.
