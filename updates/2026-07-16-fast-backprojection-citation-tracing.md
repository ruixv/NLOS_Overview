# 16 July 2026 citation-tracing update: fast GPU back-projection

## Search result

Fresh searches of arXiv, conference and journal indexes, project/lab pages, and recent NLOS keyword combinations did not identify a directly relevant NLOS-imaging paper submitted later than *Non-Line-of-Sight imaging using raster scanning at NIR wavelength* (arXiv:2607.04183, submitted 5 July 2026). The current run therefore prioritized a forward-citation and historical-consistency audit of the repository's core active-transient papers.

## High-confidence missing public entry

**Fast Back-Projection for Non-Line of Sight Reconstruction**  
Victor Arellano, Diego Gutierrez, Adrian Jarabo  
*Optics Express*, 25(10):11574--11583, 2017  
DOI: [10.1364/OE.25.011574](https://doi.org/10.1364/OE.25.011574)  
arXiv: [1703.02016](https://arxiv.org/abs/1703.02016)

The paper directly extends the Velten-era transient back-projection line rather than citing NLOS imaging only in passing. It observes that one time-resolved three-bounce sample defines an ellipsoidal space--time manifold whose foci are the illumination and detection points. Hidden-geometry probability-map construction can therefore be reorganized from repeated voxel-wise evaluation into GPU voxelization of signal-bearing ellipsoids. The paper reports speedups of up to three orders of magnitude with negligible quality loss and demonstrates the method on captured streak-camera, SPAD, and synthetic transient data.

## Repository gap and insertion plan

The paper already had an accurate citation key and a brief generic mention in `article/2active.tex`, and its metadata was present in the consolidated bibliography. It was nevertheless absent from:

- the README latest/completed-paper table;
- the README milestone timeline;
- the website paper explorer;
- the website's 2017 development timeline;
- the active-SPAD summary-table citation list;
- a sufficiently informative survey narrative explaining its algorithmic role.

This run adds one canonical correction record in `egbib_20260716_fast_backprojection_updates.bib`, inserts the paper into the public artifacts, expands the back-projection discussion in the semantically appropriate inverse-method section, and regenerates the consolidated bibliography and survey PDF.

The synchronization workflow also verifies the already integrated ST-Mamba update and preserves its consistency across README, the website explorer/timeline, the active-system table, the survey narrative, bibliography, and rebuilt PDF.

## Verification requirements

The workflow performs the following checks before committing generated artifacts:

1. exactly one README and website explorer entry for each synchronized paper;
2. final venue, DOI, authors, pages, and citation keys in the merged bibliography;
3. active-table and semantically placed survey citations;
4. no undefined citations, missing BibTeX records, or repeated entries;
5. clean LaTeX/BibTeX compilation;
6. non-empty PDF, valid page count, text extraction, and full-page rendering;
7. presence of the new literature-review text in the generated PDF;
8. mutual consistency among README, `index.html`, survey sources, bibliography, and `bare_jrnl.pdf`.

This rebased branch update triggers the pull-request validation and reproducible PDF rebuild against the latest master snapshot.
