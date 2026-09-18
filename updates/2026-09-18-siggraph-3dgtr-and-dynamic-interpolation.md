# NLOS literature update — 2026-09-18

This patch note records two verified gaps/corrections found in the current literature pass. Large public-facing files were not overwritten from partial connector payloads; integrate these entries into README.md, index.html, bare_jrnl.tex, and the canonical bibliography, then rebuild bare_jrnl.pdf.

## 1. Final-venue correction / missing milestone: 3D Gaussian Transient Rendering

**Yi Wang, Ziyu Zhan, Yuran Wang, Hao Wang, Qiang Liu, Zuoqiang Shi, Lingyun Qiu, and Xing Fu, “Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering,” ACM SIGGRAPH 2026 Conference Papers, 85:1–85:11, DOI: 10.1145/3799902.3811137.**

The work was initially available as arXiv:2606.21270, but DBLP now verifies the final SIGGRAPH 2026 Conference Paper Track publication and DOI. Use **SIGGRAPH 2026**, not arXiv, as the venue. The method represents the hidden scene with 3D Gaussian primitives and optimizes them through differentiable transient rendering while using LOS geometry to support spatially limited, sparse, arbitrary relay surfaces and both confocal/non-confocal measurements.

Recommended integration:
- README Latest Additions: add/venue-correct under Active/Transient NLOS and differentiable rendering / Gaussian representations.
- Timeline: place in 2026 as a step from planar/dense relay assumptions toward arbitrary relay geometry and differentiable transient scene representations.
- Website Paper Explorer: tags `active`, `transient`, `3D Gaussian`, `differentiable rendering`, `arbitrary relay surface`, `SIGGRAPH 2026`.
- bare_jrnl.tex: integrate near arbitrary-relay / neural or differentiable transient rendering discussion, emphasizing that the contribution relaxes planar relay geometry rather than merely replacing the reconstruction backbone.
- Canonical bibliography: use the verified final-venue entry staged in `egbib_20260918_siggraph_gtr_and_dynamic_interp.bib` and supersede any arXiv-only entry.

Suggested survey sentence: “Recent differentiable transient representations further relax acquisition geometry: Wang et al. represent hidden scenes with 3D Gaussian primitives and optimize them through transient rendering, enabling reconstruction from spatially limited and arbitrarily shaped relay surfaces in both confocal and non-confocal settings.”

## 2. Missing dynamic NLOS paper: transient video interpolation

**Shida Sun, Yue Li, Jiacheng Fu, Feihu Xu, and Zhiwei Xiong, “Transient video interpolation for dynamic non-line-of-sight imaging,” Optics Express 34(3), 4882–4894 (2026), DOI: 10.1364/OE.580550.**

This paper directly addresses the dynamic-NLOS acquisition trade-off: increasing frame rate by reducing spatial sampling or integration time sacrifices spatial resolution or transient SNR. It performs interpolation in the transient-video domain to synthesize intermediate transient frames before NLOS reconstruction, providing a distinct trajectory from static-scene learned reconstruction toward temporally dense dynamic NLOS sensing.

Recommended integration:
- README: add under Dynamic NLOS / learned transient processing.
- Timeline: place in 2026 after earlier dynamic NLOS methods, emphasizing temporal interpolation rather than only faster scanning.
- Website Paper Explorer: tags `dynamic NLOS`, `transient video`, `interpolation`, `learned reconstruction`, `Optics Express 2026`.
- bare_jrnl.tex: integrate in the dynamic-scene subsection, near methods that trade spatial samples/integration time for frame rate.
- Canonical bibliography: use `sun2026transientvideo` from the staging BibTeX.

Suggested survey sentence: “For dynamic scenes, Sun et al. interpolate directly in the transient-video domain, increasing temporal sampling without proportionally reducing relay-wall spatial sampling or photon integration, and thereby decoupling part of the frame-rate versus measurement-quality trade-off.”

## Consistency/build checklist

After safe integration, verify both papers in README.md, index.html/Paper Explorer/timeline, bare_jrnl.tex, and the canonical bibliography. Recompile bare_jrnl.pdf and confirm the new citations resolve. Do not treat this note or the staging .bib as a substitute for those public-facing integrations.
