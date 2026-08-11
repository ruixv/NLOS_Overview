# Homepage V2 research-map redesign — correctness and promotion notes

Date: 2026-08-11

## Why this redesign exists

The current homepage is information-rich but tries to serve four jobs at once: latest-news feed, long-form historical timeline, field tutorial, and full paper catalogue. This makes the frontier and structure of the field difficult to see at a glance.

`overview-v2.html` is an isolated preview that reorganizes the homepage around four layers:

1. **Overview** — a small set of data-derived KPIs.
2. **Paper Graph** — each unique curated paper is one node.
3. **Trends** — publication-year and primary-family distributions plus collaboration/metadata diagnostics.
4. **Explorer** — the complete catalogue remains searchable, but defaults to a compact table rather than hundreds of large cards.

The previous long timeline is replaced on the default view by a short Core Reading Path. The full historical narrative remains available in the survey PDF / repository and can later be exposed through an optional expanded view.

## Data provenance and correctness policy

### Paper nodes

The V2 preview does **not** maintain a second hand-written paper catalogue. At runtime it reads the current `index.html` paper array and deduplicates exact normalized title + year pairs. This keeps the preview tied to the same curated records already used by the public explorer.

### Co-author edges

The abbreviated author strings in `index.html` are **display metadata only**. Many records use forms such as `Zhang et al.` or surname-only abbreviations; those strings must never be used to infer paper-to-paper co-authorship.

For graph construction, V2 independently matches a paper against `egbib.bib` using, in priority order:

1. exact DOI when the catalogue URL is a DOI URL;
2. otherwise exact normalized paper title, preferring matching publication year.

An author name can generate an edge only when the BibTeX record contains a sufficiently informative full name. The current normalization is deliberately strict: no surname-only matching, no expansion of `et al.`, and no fuzzy author alias inference. A missing true edge is preferable to a false collaboration edge.

The UI exposes the matched-paper coverage rate, isolated-node count, and other graph-health diagnostics so incomplete metadata is visible rather than hidden.

### Edge meaning

An edge means that the two matched BibTeX records contain at least one identical normalized high-confidence author-name string. Edge weight is the number of such shared names. This is a bibliographic co-authorship relation, not a citation relation and not a claim about institutional collaboration.

### Year colors

Node color comes directly from each curated paper's numeric `year` field. The color scale is computed from the minimum and maximum years present in the loaded catalogue; no publication-year counts are manually entered.

### Research-family shapes

Shape encodes a **primary display family**, not an exclusive scientific taxonomy. The primary family is deterministically derived from existing repository tags plus explicit modality keywords, with dedicated handling for acoustic/ultrasound, RF/radar/mmWave/THz, passive optical, learning/inverse-model, resource/survey/dataset, and active optical records.

Because some papers legitimately belong to multiple scientific categories, the full existing tag string is retained in the underlying paper record. Before V2 replaces the main homepage, category rules should be spot-checked against the repository taxonomy and ambiguous multi-category papers should be reviewed rather than silently relabeled.

### Statistics

All V2 counts and charts are computed from the same deduplicated paper-node set used by the graph. The publication-by-year chart is explicitly described as **repository coverage**, not as a bibliometric claim that the repository contains every NLOS publication in existence.

The author ranking is calculated only from the strict BibTeX-matched subset and is labeled accordingly. It must not be described as a global author-impact or citation ranking.

## Elements intentionally removed from the default experience

- large ASCII inverse-problem illustration in the hero;
- hundreds of full-size paper cards on initial load;
- full verbose year-by-year historical prose on the main scrolling path;
- redundant taxonomy cards that repeat information already available through graph shapes and explorer filters;
- manually presented headline counts when the same number can be computed from the paper data.

These are not deleted from the repository's scholarly record. The goal is progressive disclosure: concise overview first, details on demand.

## Proposed community-value extensions after V2 validation

- author/lab collaboration communities using externally disambiguated identifiers (ORCID/OpenAlex/Semantic Scholar), not surname heuristics;
- citation edges once a versioned, auditable citation dataset is available;
- venue and modality growth views;
- “core / milestone / emerging” reading-path presets;
- metadata-quality badges and a contribution workflow for correcting titles, venues, DOIs, authors, categories, and links;
- downloadable structured paper metadata so other NLOS researchers can reuse the curated dataset.

## Promotion requirements

Do not replace `index.html` with this preview until all of the following are satisfied:

1. Browser-side dependencies load reliably on GitHub Pages.
2. The paper-node count is reconciled against the current catalogue after title/year deduplication.
3. BibTeX matching coverage and a random sample of positive co-author edges are manually audited.
4. No edge is produced from an abbreviated website-only author string.
5. Primary-family classifications are spot-checked, particularly multi-modal and learning-based active NLOS papers.
6. Search/filter behavior is checked on desktop and mobile widths.
7. The data source is extracted from the legacy `index.html` array into a reusable structured source (for example `data/papers.js` or JSON) before V2 itself becomes `index.html`; otherwise V2 would recursively read itself rather than the legacy catalogue.
8. The existing survey PDF, README catalogue, and website continue to refer to the same canonical paper metadata.

Until those checks pass, `overview-v2.html` remains a safe preview and the current public homepage is intentionally unchanged.
