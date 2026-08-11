# 2026-08-11 V2.3 homepage update

This update addresses three issues reported in the V2 preview.

## 1. Core Reading Path

The page now gives the main-journal **Nature** milestones a dedicated first row instead of mixing them into the general reading path:

- *Confocal non-line-of-sight imaging based on the light-cone transform* — Nature 555, 338–341 (2018).
- *Computational periscopy with an ordinary digital camera* — Nature 565, 472–475 (2019).
- *Non-line-of-sight imaging using phasor-field virtual wave optics* — Nature 572, 620–623 (2019).
- *Imaging hidden objects with consumer LiDAR via motion-induced sampling* — Nature 653, 693–699 (2026).

The general path below them retains the experimental foundation, f-k migration, neural transient fields, transformers, RF/robotics expansion and recent transport-matrix work.

## 2. 3D Paper Graph

`overview-v2.html` now uses `3d-force-graph` / WebGL rather than the 2D Canvas graph.

- true 3D force layout with rotate / zoom / pan / node drag
- substantially larger nodes
- node color = publication year
- node size = verified collaboration degree
- link width = number of verified shared authors
- click a node to focus the camera and inspect its collaboration neighborhood
- Fit and Reset controls
- explicit error state if the 3D engine cannot initialize

The page pins `3d-force-graph` to 1.80.0. `assets/paper-graph-data.js` contains a compatibility bridge for the current constructor-style browser API so the V2.3 call site remains stable.

## 3. Author search

The graph now has a separate **Author** field with a datalist built from resolved BibTeX identities.

Author matching is token-order independent. For example, a query such as `David Lindell` matches a BibTeX display string such as `Lindell, David B.`. The generic paper search also indexes full resolved authors.

Clicking a name in **Most represented verified authors** fills the Author filter and focuses the corresponding paper subgraph.

Abbreviated website strings such as `Liu et al.` still never create identities or graph edges.

## Files

- `overview-v2.html` — V2.3 user interface and 3D graph.
- `assets/paper-graph-data.js` — audited metadata parser / identity resolver plus 3D constructor compatibility bridge.

The existing public `index.html` is intentionally unchanged; V2.3 remains a reversible preview until the graph and metadata coverage are accepted.