# Radar/mmWave/sub-THz NLOS reconstruction lineage — 24 July 2026

## Audit result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found. The newest date-verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

Citation tracing through the active optical NLOS core and the radar reconstruction literature exposed a major modality-level consistency gap. Eight direct hidden-scene reconstruction papers were missing from the README and website. The consolidated bibliography already contained part of the lineage under stable keys; those records were preserved and normalized rather than duplicated. HoloRadar was already mentioned in the survey but lacked a public explorer record and a usable canonical bibliography entry.

## Integrated lineage

1. Wei et al., *Nonline-of-Sight 3-D Imaging Using Millimeter-Wave Radar*, IEEE TGRS 2022, DOI `10.1109/TGRS.2021.3112579`.
2. Cai et al., *Precise Reconstruction Method for Hidden Targets Based on Non-line-of-sight Radar 3D Imaging*, Journal of Radars 2024, DOI `10.12000/JR24060`.
3. Liu et al., *RM-CSTV*, National Science Open 2024, DOI `10.1360/nso/20230085`.
4. Lai et al., *Non-Line-of-Sight 3D Reconstruction with Radar (HoloRadar)*, NeurIPS 2025.
5. Cai et al., *Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement*, IEEE TAP 2025, DOI `10.1109/TAP.2025.3583778`.
6. Cai et al., *Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning*, IEEE TCI 2025, DOI `10.1109/TCI.2025.3597462`.
7. Chen et al., *RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar*, Journal of Radars 2026, DOI `10.12000/JR25132`.
8. Chen et al., *Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging*, Photonics 2026, DOI `10.3390/photonics13050440`.

## Completed changes

- Added all eight papers to README Latest Additions and the principal 2022/2024/2025/2026 milestone blocks.
- Added searchable website explorer records, expanded the website timeline, and changed the tracked-entry count from 193 to 201.
- Added two semantically placed survey paragraphs connecting measured physical radar models, NSIR/RM-CSTV, HoloRadar, ACTE-Net, equivariant threshold learning, RM-operator unfolding, and 121 GHz holographic unfolding.
- Reused stable bibliography keys, replaced preliminary metadata in place, and added only missing canonical records.
- Added the survey trace marker and regenerated `bare_jrnl.pdf` through a clean LaTeX/BibTeX build.

## Validation

- Unique public title and DOI checks.
- One consolidated bibliography record per DOI/title and stable citation key.
- Clean `pdflatex → bibtex → pdflatex ×2` build.
- Every resolved radar-lineage key present in the generated `.bbl`.
- PDF page metadata, extracted text, and rendered pages validated.
