# 22 July 2026 passive soft-shadow and commodity-iToF citation trace

## Verified additions and corrections

This run used keyword searches, author/lab pages, publisher metadata, and forward-citation tracing from computational periscopy, transient NLOS, and edge-resolved imaging milestones.

1. **NIGHT -- Non-Line-of-Sight Imaging from Indirect Time of Flight Data** — Matteo Caligiuri, Adriano Simonetto, Pietro Zanuttigh. Final venue: *Computer Vision -- ECCV 2024 Workshops, Part XIX*, pp. 143--159. DOI: `10.1007/978-3-031-93806-1_12`. The repository previously linked the arXiv preprint; the survey now uses the final Springer record.
2. **Soft Shadow Diffusion (SSD): Physics-Inspired Learning for 3D Computational Periscopy** — Fadlullah A. Raji, John Murray-Bruce. Final venue: *ECCV 2024*, pp. 382--400. DOI: `10.1007/978-3-031-72989-8_22`. The repository previously treated the later January 2026 arXiv upload as an arXiv 2026 paper; the final ECCV 2024 venue takes precedence.
3. **Towards 3D Computational Persicopy with an Ordinary Camera: A Separable Non-Linear Least Squares Formulation** — Fadlullah Raji, John Murray-Bruce. *IEEE ICASSP 2024*, pp. 7475--7479. DOI: `10.1109/ICASSP48485.2024.10446230`. This is the optimization precursor to SSD and directly extends ordinary-camera computational periscopy to joint 3D occluder and 2D radiosity recovery. The publisher's `Persicopy` spelling is retained.
4. **Two-Edge-Resolved 3D Non-Line-of-Sight Imaging: A Fisher Information Equalized Discretization** — Robinson Czajkowski, John Murray-Bruce. *IEEE ICASSP 2024*, pp. 2535--2539. DOI: `10.1109/ICASSP48485.2024.10446406`. This is a conditioning-oriented companion to the TERI Nature Communications paper rather than a duplicate: it allocates depth samples according to Fisher information in the edge-resolved measurement.

All four works are direct NLOS reconstruction papers. SSD and SNLLS explicitly continue the ordinary-camera computational-periscopy lineage; NIGHT expands active NLOS to off-the-shelf indirect-ToF hardware; the Fisher paper refines the numerical representation used by two-edge-resolved passive 3D NLOS.

## Cross-artifact integration

The guarded synchronizer:

- corrects NIGHT and SSD to their final venues and DOI links in `README.md` and `index.html`;
- adds the previously missing SNLLS and Fisher-information papers to the public paper explorer and timeline;
- places NIGHT in the active indirect-ToF discussion and integrates the soft-shadow and Fisher-equalized developments into `article/3passive.tex`;
- adds verified canonical BibTeX records and regenerates the duplicate-free consolidated bibliography;
- rebuilds `bare_jrnl.pdf` and checks source/PDF consistency before committing generated artifacts.

The tracked homepage count increases only for the two genuinely new paper objects. NIGHT and SSD were already represented and are corrected in place.

## Search outcome

No direct NLOS imaging publication with a verified publication date later than 15 July 2026 was found in this pass. The latest date-verifiable direct paper remains *Non-line-of-sight imaging via physics-informed cascade learning* in JOSA A, published 15 July 2026. A SIGGRAPH 2026 transient-polarimetry poster was excluded because publicly available metadata did not establish hidden-scene reconstruction; forward citation alone was not considered sufficient.
