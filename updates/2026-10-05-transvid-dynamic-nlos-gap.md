# TransVID dynamic NLOS integration note — 2026-10-05

## Verified missing paper

Shida Sun, Yue Li, Jiacheng Fu, Feihu Xu, and Zhiwei Xiong, “Transient video interpolation for dynamic non-line-of-sight imaging,” *Optics Express*, vol. 34, no. 3, pp. 4882–4894, 2026. DOI: 10.1364/OE.580550.

Publisher/index metadata was cross-checked against PubMed/Optica records. The paper is a final journal publication, not an arXiv-only item.

## Why it belongs

TransVID addresses the acquisition bottleneck in dynamic active NLOS imaging rather than treating video reconstruction as an ordinary post-processing problem. It takes consecutive low-resolution, low-frame-rate transient measurements, uses spatial-temporal encoding plus conditional latent diffusion to synthesize intermediate high-resolution transient frames, and then applies NLOS reconstruction. The reported setting maps 16×16 transient measurements at 4 FPS to 128×128 transient videos at 16 FPS, with synthetic-to-real validation on a custom confocal NLOS system.

This makes it a useful development node after high-speed/sparse dynamic acquisition and ST-Mamba: hardware/sampling-limited dynamic NLOS → temporal-consistency reconstruction → transient-domain video interpolation/diffusion that computationally increases both spatial sampling and frame rate.

## Canonical integration plan

- **README timeline / latest additions:** add under 2026 active/learned/dynamic NLOS. Suggested summary: “Introduces TransVID, a latent-diffusion transient-video interpolation framework that converts low-resolution 4-FPS confocal measurements into high-resolution 16-FPS transient video, mitigating the spatial-resolution/frame-rate trade-off for dynamic NLOS imaging.”
- **Website / Paper Explorer:** category tags: Active NLOS; Dynamic NLOS; Learned Reconstruction; Diffusion; Transient Interpolation.
- **Survey source:** integrate semantically near the dynamic-NLOS discussion containing ST-Mamba and sparse/high-speed acquisition. Suggested literature-review transition: “Beyond reconstructing each acquired transient frame, recent work also moves temporal super-resolution into the measurement domain: TransVID uses conditional latent diffusion to interpolate high-resolution transient frames between sparsely sampled acquisitions, computationally relaxing the frame-rate–spatial-resolution trade-off of dynamic NLOS capture.”
- **Bibliography:** merge the verified entry staged in `egbib_20261005_transvid_gap.bib` into the canonical bibliography and cite it from the survey text.
- **PDF:** rebuild only after the canonical source/bibliography edits are safely applied; verify the new citation resolves and the regenerated PDF contains the TransVID discussion.

## Consistency / safety status

Repository default-branch code search for the exact title and `TransVID` returned no match before staging, so this is a genuine current gap. Large canonical files were not overwritten from partial connector buffers in this run. README, website, survey source, canonical bibliography, and PDF still require a full-buffer guarded integration/build pass; do not claim those artifacts are synchronized until that pass succeeds.
