# NLOS literature update patch — 17 July 2026

This patch note records one verified missing paper and two verified final-venue corrections found during the 17 July 2026 literature and forward-citation-tracing pass. It is intentionally committed as a patch-style note rather than overwriting the repository's large public-facing files through a whole-file replacement API.

## 1. New missing paper: MDUNet

**MDUNet: Multimodal Decoding UNet for Passive Occluder-Aided Non-line-of-sight 3D Imaging**  
Fadlullah Raji and John Murray-Bruce  
**IEEE/CVF WACV 2026**, pp. 461–471  
DOI: <https://doi.org/10.1109/WACV61042.2026.00053>  
CVF paper page: <https://openaccess.thecvf.com/content/WACV2026/html/Raji_MDUNet_Multimodal_Decoding_UNet_for_Passive_Occluder-Aided_Non-line-of-sight_3D_Imaging_WACV_2026_paper.html>

### Why it is relevant

MDUNet is a direct passive NLOS imaging paper rather than an adjacent citation. It reconstructs two complementary hidden-scene representations from one ordinary soft-shadow photograph: a 3D signed-distance-field/mesh representation of hidden occluders and a transverse 2D radiosity image of non-occluding hidden content. A shared encoder couples two specialized decoder paths. The paper reports over 100× faster inference than its diffusion-based SSD baseline and over 1000× faster inference than the iterative optimization baseline, while improving robustness to noise, textured relay surfaces, and ambient illumination. It is trained on simulation and evaluated on real measurements.

### Citation-tracing verification

The paper's related-work and method sections directly connect it to the passive computational-periscopy lineage. It cites the ordinary-camera occluder-aided literature, including Saunders et al.'s computational periscopy, and explicitly builds on the authors' preceding separable nonlinear inverse formulations and Soft Shadow Diffusion. This makes it a high-confidence forward development of the repository's passive-NLOS core papers, not a work that merely mentions NLOS in passing.

### Suggested README.md insertion

Add to `## Latest Additions`, preferably near the existing 2026 passive entries:

```markdown
| 2026 | [MDUNet: Multimodal Decoding UNet for Passive Occluder-Aided Non-line-of-sight 3D Imaging](https://doi.org/10.1109/WACV61042.2026.00053) — Raji, Murray-Bruce | WACV 2026 | Jointly reconstructs a 3D hidden-occluder mesh and a 2D non-occluding radiosity image from one ordinary soft-shadow photograph. A shared encoder and multimodal decoder paths replace the slower hybrid diffusion/physics pipeline, improving robustness to ambient light and noise while reporting over 100× faster inference than SSD and over 1000× faster inference than iterative optimization. |
```

Update the README run date from `16 July 2026` to `17 July 2026` and append a 2026 timeline item describing the transition from physics/diffusion-based 3D computational periscopy to fast fully learned multimodal passive reconstruction.

### Suggested index.html insertion

1. Change the header/footer update date to `17 July 2026`.
2. Increase `tracked latest entries` from `106` to `107`.
3. Add the following paper object near the existing Soft Shadow Diffusion entry:

```javascript
{cat:"latest passive learning",title:"MDUNet: Multimodal Decoding UNet for Passive Occluder-Aided Non-line-of-sight 3D Imaging",authors:"Raji and Murray-Bruce",year:2026,venue:"WACV 2026",url:"https://doi.org/10.1109/WACV61042.2026.00053",key:"A shared encoder and two specialized decoder paths jointly recover a 3D SDF/mesh of hidden occluders and a 2D radiosity image of non-occluding hidden content from one soft-shadow photograph; trained only on simulation, MDUNet generalizes to real measurements and reports over 100× faster inference than SSD and over 1000× faster inference than iterative optimization."},
```

4. Extend the 2026 timeline title/body to include fully learned passive occluder-aided 3D reconstruction and the progression from SSD to MDUNet.

### Suggested survey insertion

In `article/3passive.tex`, add a row to Table `tab:passive` after the existing learned passive entries:

```latex
\cite{rajiMDUNet2026} & Ambient light & Conventional camera & Soft-shadow occlusion with coupled learned 2D/3D decoding & Joint 2D radiosity and 3D occluder reconstruction\\
```

After the final paragraph of the `Partial occluder` subsection, add:

```latex
\vspace{0.8mm}
\noindent \textbf{Fully learned multimodal computational periscopy.}
Recent passive NLOS methods have begun to reconstruct both the hidden occluding geometry and the non-occluding radiance distribution rather than treating the occluder only as a known coding element. Raji and Murray-Bruce proposed MDUNet, which uses a shared encoder and separate 3D-SDF and 2D-radiosity decoder paths to couple these two outputs from a single soft-shadow photograph~\cite{rajiMDUNet2026}. Compared with the preceding hybrid Soft Shadow Diffusion pipeline, the fully trained model substantially reduces inference time while improving robustness to ambient illumination and measurement noise, marking a shift from physics-plus-generative optimization toward direct multimodal passive reconstruction.
```

In `bare_jrnl.tex`, update the title-footnote repository count from `150+ NLOS papers` to `190+ NLOS papers`. Keep the existing `\bibliography{egbib_merged_20260711}` line after merging the entry below into that consolidated file.

### BibTeX entry

```bibtex
@inproceedings{rajiMDUNet2026,
  author    = {Raji, Fadlullah and Murray-Bruce, John},
  title     = {{MDUNet}: Multimodal Decoding {UNet} for Passive Occluder-Aided Non-line-of-sight 3D Imaging},
  booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
  pages     = {461--471},
  month     = mar,
  year      = {2026},
  publisher = {IEEE},
  doi       = {10.1109/WACV61042.2026.00053},
  url       = {https://doi.org/10.1109/WACV61042.2026.00053}
}
```

## 2. Final-venue correction: GeRaF 2.0

The repository currently labels **Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals** as arXiv 2026 in some public-facing locations. Its final venue is verified as:

- **CVPR 2026**, pp. 1221–1230
- Official page: <https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_Radar_Signals_CVPR_2026_paper.html>

Replace `arXiv 2026` with `CVPR 2026`, replace the arXiv link with the official CVF page where appropriate, and use:

```bibtex
@inproceedings{luSeeingThroughBoxes2026,
  author    = {Lu, Jiachen and Shanbhag, Hailan and Al Hassanieh, Haitham},
  title     = {Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {1221--1230},
  month     = jun,
  year      = {2026},
  url       = {https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_Radar_Signals_CVPR_2026_paper.html}
}
```

## 3. Final-venue correction: DENALI

The repository currently labels **DENALI: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost LiDARs** as arXiv 2026 in some public-facing locations. Its final venue is verified as:

- **CVPR 2026**, pp. 3046–3055
- Official CVPR listing: <https://openaccess.thecvf.com/CVPR2026?day=2026-06-05>

Replace `arXiv 2026` with `CVPR 2026` and retain the arXiv page only as a supplementary source where useful.

```bibtex
@inproceedings{behariDENALI2026,
  author    = {Behari, Nikhil and Rivero, Diego and Apostolides, Luke and Ghosh, Suman and Liang, Paul Pu and Raskar, Ramesh},
  title     = {{DENALI}: A Dataset Enabling Non-Line-of-Sight Spatial Reasoning with Low-Cost {LiDARs}},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {3046--3055},
  month     = jun,
  year      = {2026},
  url       = {https://openaccess.thecvf.com/CVPR2026?day=2026-06-05}
}
```

## Remaining integration and validation steps

The patch should be applied consistently to `README.md`, `index.html`, `article/3passive.tex`, `bare_jrnl.tex`, and `egbib_merged_20260711.bib`. After application:

1. Run a clean LaTeX/BibTeX build of `bare_jrnl.tex`.
2. Regenerate and commit `bare_jrnl.pdf`.
3. Confirm `rajiMDUNet2026` is defined exactly once and has no undefined citation.
4. Confirm MDUNet appears once in README and once in the website paper array.
5. Confirm the website tracked-entry count is 107.
6. Confirm GeRaF 2.0 and DENALI use CVPR 2026, not arXiv, across README, website, survey text, bibliography, and PDF.
7. Extract PDF text and verify the MDUNet paragraph and citation are present.

No claim is made here that `bare_jrnl.pdf` has already been regenerated; the binary remains unchanged until this patch is applied and compiled.
