# 13 July 2026 passive-polarization NLOS consistency update

## Search and citation-tracing result

Fresh searches of recent arXiv, conference, journal, project, and laboratory pages did not reveal a directly relevant NLOS-imaging paper newer than the 5 July 2026 NIR raster-scanning preprint already covered by the repository. A reference/citation-tracing pass over the active ToF, phasor-field, computational-periscopy, passive-imaging, and recent comparative-study branches exposed one public-artifact gap:

- **Enhancing Passive Non-Line-of-Sight Imaging Using Polarization Cues** — Kenichiro Tanaka, Yasuhiro Mukaigawa, Achuta Kadambi, arXiv:1911.12906 (2019).

The paper is genuinely passive NLOS imaging rather than a passing citation. It places a polarizer in front of the camera and exploits polarization-axis rotation along oblique indirect paths to improve the conditioning of the wall-to-hidden-scene light-transport inverse problem. Experiments report improved hidden-image recovery both with and without occluders, making it a complementary branch to ordinary-camera computational periscopy.

No final conference or journal publication could be verified from publisher, DOI, author-page, or scholarly-index searches as of 13 July 2026. The repository therefore labels the work **arXiv 2019** and does not infer a final venue.

## Existing repository state

The LaTeX survey already cited the work through the legacy key `tanakaPolarizedNonLineofSightImaging2020` in the passive forward-model table and polarizer subsection, but the current README and homepage paper explorer did not expose the paper. The legacy citation record also needed canonical title, author, arXiv, DOI, and URL metadata. This update closes that consistency gap rather than introducing a duplicate citation key.

## Synchronized changes

The marker-based script `scripts/sync_nlos_20260713_passive_polarization.py` is designed to:

1. add the paper to `README.md` under Latest Additions with an arXiv-2019 venue label and a concise contribution summary;
2. add a searchable passive/hardware object to `index.html` and update the tracked-entry count to 92 after the pending initial-access and commodity-ToF synchronizations;
3. extend the 2019 development-timeline node with polarization-conditioned passive light transport;
4. add a short, semantically placed literature-review paragraph to `article/3passive.tex`, immediately before the coherence subsection;
5. retain the survey's established key `tanakaPolarizedNonLineofSightImaging2020` while allowing the dated supplement `egbib_20260713_polarization_updates.bib` to override incomplete legacy metadata during deterministic bibliography merging.

The script is idempotent and aborts if any insertion marker is absent or ambiguous, avoiding blind whole-file replacement.

## Build and consistency checks

The validation workflow runs the pending 6G initial-access and commodity-ToF synchronizers first, then the passive-polarization synchronizer, regenerates the duplicate-free merged bibliography, and performs a clean LaTeX/BibTeX rebuild. It verifies:

- exactly one README and homepage entry for the polarization paper;
- the 2019 timeline wording and 92-entry homepage count;
- the survey paragraph and canonical citation key;
- one merged BibTeX record containing arXiv:1911.12906 and its DOI;
- zero truly missing citation keys;
- successful `pdfinfo`, `pdftotext`, and full-page PNG rendering checks;
- no undefined citations, missing BibTeX records, or repeated entries;
- the polarization discussion and canonical bibliography record in the rebuilt `bare_jrnl.pdf`.

**Build result:** pending the one-shot GitHub Actions synchronization and clean PDF rebuild. Until the workflow commits a successful result, this note does not claim that README, homepage, merged bibliography, or `bare_jrnl.pdf` have already changed.
