# NLOS literature audit — 2026-11-23

## Verified missing adjacent paper: ToF ReSTIR (SIGGRAPH 2026)

**Kim, Juhyeon; Jarosz, Wojciech; Pediredla, Adithya.** “ToF ReSTIR: Time-of-Flight Rendering with Spatio-temporal Reservoir Resampling.” *ACM Transactions on Graphics* **45**(4), Article 89, pp. 1–18 (SIGGRAPH 2026). DOI: https://doi.org/10.1145/3811299. Project: https://juhyeonkim95.github.io/project-pages/tof_restir/ . arXiv: https://arxiv.org/abs/2605.11536 .

**Relevance and scope:** Adjacent NLOS-enabling transient forward rendering, not a new standalone NLOS inverse solver. Path-length-aware shift mapping makes spatio-temporal reservoir reuse physically valid for time-gated and transient light transport; authors explicitly demonstrate an NLOS hidden-geometry reconstruction application, in addition to navigation. Cite under transient rendering / differentiable and efficient forward simulation, not as direct active NLOS reconstruction SOTA.

**Verified publication:** Author's project and Dartmouth faculty publication page explicitly state ACM TOG (SIGGRAPH 2026); DBLP confirms 45(4), article 89 and DOI 10.1145/3811299. Do not label as arXiv-only.

**Repository audit:** Full master README.md and data/papers-source.html fetched on 2026-11-23 and searched for the exact title / “ToF ReSTIR”: absent. article/5newscenes.tex also checked. Other survey chapters and bibliography must be searched before insertion to prevent duplicate references.

**Suggested README and website entry:** 2026 | ToF ReSTIR: Time-of-Flight Rendering with Spatio-temporal Reservoir Resampling — Kim et al. | ACM TOG / SIGGRAPH 2026 | Accelerates physically valid time-gated/transient light-transport simulation using path-length-aware reservoir resampling, with a demonstrated NLOS reconstruction use case. Category: Transient rendering / NLOS-enabling computational methods.

**Suggested survey insertion:** In the discussion of time-resolved forward transport and differentiable / efficient transient rendering, add: “Recent transient-rendering work has extended reservoir-based path reuse to time-of-flight measurements: Kim et al. introduce path-length-aware shift mapping for interactive time-gated and transient simulation, demonstrating downstream NLOS reconstruction, although the contribution is a forward renderer rather than an inverse reconstruction algorithm \\cite{kim2026tofrestir}.”

**Verified BibTeX staging:**
```bibtex
@article{kim2026tofrestir,
  author = {Kim, Juhyeon and Jarosz, Wojciech and Pediredla, Adithya},
  title = {{ToF} {ReSTIR}: Time-of-Flight Rendering with Spatio-temporal Reservoir Resampling},
  journal = {ACM Transactions on Graphics},
  volume = {45},
  number = {4},
  articleno = {89},
  pages = {1--18},
  year = {2026},
  doi = {10.1145/3811299},
  url = {https://doi.org/10.1145/3811299}
}
```

## Additional candidate requiring verification

Xu, Zihan et al., “Joint Estimation of Target State and Building Layout Based on Range-Doppler Topology in NLOS Scenarios,” reported as *IEEE Transactions on Aerospace and Electronic Systems* (online 2026-11-02), DOI https://doi.org/10.1109/TAES.2026.3749544 . Secondary scholarly index only; primary IEEE abstract and scope still need verification. Potential radar NLOS scene-layout estimation, **do not integrate as verified yet**.

## Pending consistency and build work

This commit is a staging audit, **not** a claim that README.md, website, LaTeX, BibTeX, or bare_jrnl.pdf were updated. Before merge: check all survey subfiles and bibliography for duplicate entries, insert in semantic section, synchronize README and website paper explorer/latest/timeline, compile and validate bare_jrnl.pdf, then verify commit and artifact consistency. The previously staged Flash LiDAR and radar-pedestrian papers remain separate pending integrations; do not duplicate them.
