# 13 July 2026 occlusion-coded active NLOS update

## Search and citation-tracing result

The fresh arXiv, conference, journal, project-page, and lab-page pass did not identify a direct NLOS imaging paper newer than the 5 July 2026 NIR raster-scanning preprint already covered by the repository. Forward/reference tracing from the active-NLOS milestone chain did, however, expose an incompletely represented branch built around natural hidden-scene occluders.

Two works meet the inclusion threshold:

1. **Exploiting Occlusion in Non-Line-of-Sight Active Imaging** — Christos Thrampoulidis, Gal Shulkind, Feihu Xu, William T. Freeman, Jeffrey H. Shapiro, Antonio Torralba, Franco N. C. Wong, and Gregory W. Wornell, arXiv:1711.06297 (2017). The theory formalizes the visibility masks cast by natural hidden-scene occluders and shows that they improve the conditioning of the active light-transport inverse problem sufficiently to remove the need for fine time-resolved measurements in the modeled static setting. No final conference or journal version was verified, so the repository labels it as arXiv 2017.

2. **Revealing hidden scenes by photon-efficient occlusion-based opportunistic active imaging** — Feihu Xu, Gal Shulkind, Christos Thrampoulidis, Jeffrey H. Shapiro, Antonio Torralba, Franco N. C. Wong, and Gregory W. Wornell, *Optics Express* 26(8), 9945–9961 (2018), DOI: 10.1364/OE.26.009945. This is the experimental continuation of the theory paper rather than an incidental citation: it uses a physical three-bounce forward model, known natural occlusion, background-light terms, and a binomial single-photon likelihood to reconstruct meter-scale hidden-surface reflectivity from integrated, non-time-resolved SPAD measurements. The paper reports requiring about sixteen times fewer detected photons than the preceding Gaussian-noise treatment.

The repository previously cited the theory key inside `article/2active.tex` and included it in the homepage core-paper explorer, but did not surface it in README/latest additions or explain the theory-to-experiment trajectory. The experimental Optics Express paper was absent throughout. This update therefore repairs a historical-development and survey-consistency gap rather than inflating the collection with loosely adjacent papers.

## Intended synchronized changes

The marker-based script `scripts/sync_nlos_20260713_occlusion.py` performs the following idempotent edits and aborts if expected hand-maintained markers are absent or ambiguous:

- add both papers to `README.md` with verified venue/status, links, and concise contribution summaries;
- preserve the existing searchable theory object, add the missing 2018 experiment to `index.html`, update the tracked-latest count from 92 to 93, and refine the 2017–2018 timeline from occlusion theory to photon-efficient room-scale validation;
- separate occlusion-coded integrated-photon sensing from the generic pulsed-SPAD/ToF row in the active-system table;
- expand the semantically appropriate `Occlusion-based active NLOS imaging model` discussion in `article/2active.tex` with the theory-to-experiment trajectory;
- add canonical BibTeX records in `egbib_20260713_occlusion_updates.bib`, letting the deterministic bibliography merge override stale metadata for the existing theory key and introduce the final Optics Express record;
- regenerate the duplicate-free merged bibliography and rebuild `bare_jrnl.pdf` from a clean LaTeX/BibTeX state.

## Validation requirements

The publication workflow must verify all of the following before writing regenerated artifacts to `master`:

- each title occurs exactly once in README and homepage data;
- the homepage tracked-latest count is 93 and the 2017/2018 timeline changes are present;
- both canonical citation keys occur in `article/2active.tex`, the merged bibliography, LaTeX auxiliary file, and generated bibliography;
- the bibliography audit reports zero truly missing citation keys;
- a clean `latexmk` build succeeds without undefined citations or repeated/missing BibTeX entries;
- `pdfinfo`, text extraction, and page rendering succeed on the regenerated PDF;
- extracted PDF text includes the occlusion-coded theory/experiment narrative and both bibliography records.

**Build result:** pending the pull-request validation and clean survey rebuild. No regenerated PDF is claimed until those checks pass.
