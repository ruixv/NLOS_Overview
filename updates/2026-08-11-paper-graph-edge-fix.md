# 2026-08-11 Paper Graph edge fix

## Problem

`overview-v2.html` rendered paper nodes correctly but could render zero co-author edges. The original preview delegated BibTeX parsing to the external `bibtex-parse-js` browser bundle and intentionally returned an empty BibTeX array when that dependency was unavailable. Because node metadata came independently from `index.html`, this failure mode looked superficially healthy: nodes appeared, but the author graph had no edges.

## Fix

The V2.1 preview removes the external BibTeX-parser dependency and parses the fields needed for the graph locally from the repository's canonical `egbib.bib` file. It still uses the public `index.html` paper array as the curated node set.

Paper-to-BibTeX matching is conservative:

1. DOI exact match when the paper URL is a DOI URL.
2. Otherwise normalized exact title match, preferring the same publication year.
3. The abbreviated website author strings (`et al.`, surname-only display strings, etc.) never create graph edges.

Author identity resolution is also conservative. Full given-name tokens plus family name form the primary identity. Initial-only variants are resolved only when the corresponding family-name + initials signature maps unambiguously to one full identity in the matched corpus. Ambiguous initials are excluded rather than guessed.

## Graph semantics

- node = one deduplicated curated paper (`normalized title + year`)
- edge = at least one verified shared author identity
- edge weight = number of verified shared authors
- node color = publication year
- node shape = primary research family
- node size = verified graph degree

The graph now provides edge modes for all verified links, strong links (2+ shared authors), and hidden edges. Selecting a node emphasizes incident edges and its collaboration neighborhood.

## Integrity regression test

The live page runs a known-edge audit after graph construction:

- **Positive:** `Confocal Non-Line-of-Sight Imaging Based on the Light-Cone Transform` (LCT) must connect to `Wave-Based Non-Line-of-Sight Imaging Using Fast f-k Migration`; the repository BibTeX records share Matthew O'Toole, David B. Lindell, and Gordon Wetzstein.
- **Negative:** `Recovering Three-Dimensional Shape around a Corner Using Ultrafast Time-of-Flight Imaging` (Velten et al. 2012) must not acquire a spurious co-author edge to LCT.

If the graph produces zero edges or the known-edge audit fails, the page now reports an integrity failure instead of silently presenting an edgeless graph.

## Local unit test used for this fix

The local parser/identity test produced three BibTeX entries, matched all three reference papers, generated exactly one test paper-pair edge (LCT ↔ f-k) with weight 3, and generated no Velten-2012 ↔ LCT edge.

## Public preview

`overview-v2.html` is still a preview and does not replace the existing `index.html` homepage. This keeps the visualization redesign reversible while its metadata coverage and interaction behavior are audited.