# Quasi-Fresnel NLOS integration gap — 2026-09-20

## Verified missing/final-venue update

**Yijun Wei, Jianyu Wang, Leping Xiao, Zuoqiang Shi, Xing Fu, and Lingyun Qiu, “Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform,” Optica 13, 1785 (2026), DOI: 10.1364/OPTICA.604217.**

This work was originally available as arXiv:2508.02003 (2025), but the authors’ Tsinghua publication page now verifies the final venue as **Optica, volume 13, page 1785 (2026)**. Use the final Optica venue in all public-facing artifacts; retain the arXiv link only as a supplementary/preprint source if useful.

## Contribution / historical placement

The method challenges the standard 3D-voxel computational formulation for transient NLOS when the recoverable hidden content is effectively a visible 2D surface. It represents hidden reflectance/depth with 2D functions and derives a Quasi-Fresnel transform that directly maps aggregated transient measurements to the hidden scene. The resulting explicit inversion substantially reduces runtime and memory, with the authors reporting sub-second reconstruction and <50 MB memory for 1024×1024 reconstruction, compared with roughly 100 s / 100 GB for representative volumetric baselines.

Recommended trajectory placement:

**3D transient inversion (LCT / f-k / phasor-field) → fast analytic transforms → dimensionality-aware 2D inversion → Quasi-Fresnel transform → lightweight / embedded high-resolution NLOS.**

This is best treated as an analytic/physics-based efficiency milestone, not as generic learned reconstruction.

## Required integration locations

1. **README.md** — add under latest additions and active/transient reconstruction; venue `Optica 2026`; concise summary: direct 2D Quasi-Fresnel inversion for high-resolution NLOS with orders-of-magnitude lower compute/memory than volumetric reconstruction.
2. **index.html / paper explorer** — add a 2026 Optica entry and a timeline point under efficient analytic reconstruction / practical deployment.
3. **bare_jrnl.tex** — integrate semantically in the active ToF analytic reconstruction discussion after LCT/f-k/phasor-field and/or the computational-efficiency paragraph. Suggested literature-review point: recent work questions the necessity of volumetric 3D scene parameterization when NLOS recovers visible hidden surfaces, deriving a Quasi-Fresnel transform that reduces the inverse problem to efficient 2D operations and enables high-resolution reconstruction on lightweight platforms.
4. **Canonical bibliography** — merge the verified BibTeX staged in `egbib_20260920_quasi_fresnel_optica.bib`.
5. **bare_jrnl.pdf** — rebuild after source/bibliography integration and verify that the citation resolves.

## Verification

- Full title and DOI searches returned no match in the repository before staging.
- Final venue is independently corroborated by the corresponding author/team publication page: Optica 13, 1785 (2026), DOI 10.1364/OPTICA.604217.
- Do not leave this item labeled only as arXiv 2025 in public-facing artifacts.

## Remaining consistency work

The canonical large files were not overwritten in this run because a safe complete-file edit/build path was not established. This note is intentionally a staging/integration patch, not a claim that README/index/survey/PDF are already synchronized.
