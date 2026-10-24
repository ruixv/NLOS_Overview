# 2026-10-24: Citation-traced dynamic-relay NLOS milestone

## Verified bibliographic record

Marco La Manna, Ji-Hyun Nam, Syed Azer Reza, and Andreas Velten, "Non-line-of-sight-imaging using dynamic relay surfaces," *Optics Express*, vol. 28, no. 4, pp. 5331–5339, 2020. DOI: [10.1364/OE.383586](https://doi.org/10.1364/OE.383586). PubMed PMID [32121756](https://pubmed.ncbi.nlm.nih.gov/32121756/); [OpenAlex W3001211904](https://openalex.org/W3001211904).

## Why it belongs in the survey

The paper reconstructs occluded objects while the non-planar relay surface itself moves during the photon time-of-flight acquisition. Two time-resolved detection paths allow the changing relay origin to be estimated separately from the hidden-scene return. This is genuine active NLOS imaging, not merely an adjacent localization citation, and is an earlier milestone on dynamic/nonplanar relay surfaces preceding the later 2023 3D-RSD proxy-plane solver and arbitrary-relay CUDA backprojection. It references Velten 2012, O'Toole 2018 LCT, Lindell 2019 f-k migration, and the Liu phasor-field lineage, and remains relevant to later non-planar relay systems.

## Repository coverage and planned integration

The bibliography already contains accurate entry `mannaNonlineofsightimagingUsingDynamic2020`, and the LaTeX active-hardware comparison table already mentions it. However, at the start of this run, neither README, index.html, nor data/papers-source.html contained its title or DOI, and the survey lacked a substantive historical discussion. This backfill belongs in README's 2020 active acquisition/timeline sections, the homepage Core Reading Path, the searchable paper explorer, and `article/2active.tex` under non-planar relay-surface handling. The BibTeX metadata/key remain unchanged to avoid duplicating a published record.

Previous audit candidates apparently lacking survey references were false positives due to multiple BibTeX keys with the same DOI (CorridorLocNet, mining Radar–LiDAR, human SPAD detection, thermal rough-wall NLOS, adaptive artifact cancellation, zero-shot mixture, TransDiff); each already has an alternate cited key and corresponding survey discussion. No duplicate paper entries have been added for those.

## Build verification

This note is written alongside text-source integration. `bare_jrnl.pdf` must be regenerated **after** the source commit, preferably by the existing GitHub Actions LaTeX build; an earlier successful PDF is not proof that this new paragraph has been included. Verify the subsequent workflow succeeds and the PDF binary blob SHA changes before claiming PDF/survey synchronization. If it is still building or fails, PDF remains pending without affecting subsequent research runs.
