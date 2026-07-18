# 18 July 2026 irregular-relay and Flatland citation trace

STATUS: SYNCHRONIZED — source artifacts were updated by the guarded workflow; PDF validity is checked before its separate commit.

## Scope

This pass followed forward citations and close descendants of the active transient milestones (Velten 2012, LCT, f-k migration, phasor-field propagation), the sparse/irregular acquisition line (CC-SOCR, under-scanning reconstruction, Virtual Scanning, TransDiff), and non-planar relay work. Candidates were retained only when their primary contribution was direct NLOS reconstruction, transient recovery, or an enabling NLOS simulation framework.

## Verified records

### CUDA-accelerated Non-line-of-sight imaging with irregular relay surfaces

- Yi Sun, Yu Hong, Ziheng Qiu, Wei Li, Wenwen Li, Qilin Sun, Feihu Xu
- *Optics and Lasers in Engineering*, vol. 200, article 109591, May 2026
- DOI: `10.1016/j.optlaseng.2025.109591`
- Directly applies filtered back projection to native non-planar relay geometry and arbitrary nonuniform scans. The CUDA implementation reports at least two orders of magnitude acceleration over CPU execution and is evaluated against CC-SOCR, Virtual Scanning, and 3D RSD.

### Reprojection-Guided Non-Line-of-Sight Imaging Under Irregular Undersampling

- Xingyu Cui, Huanjing Yue, Jing-Yu Yang
- *IEEE Journal of Selected Topics in Signal Processing*, vol. 19, no. 8, pp. 1739–1751, 2025
- DOI: `10.1109/JSTSP.2025.3620710`
- Recovers dense denoised transients from irregularly undersampled or fragmented relay measurements. Range-space reprojection generates physical guidance that spatio-temporal modulation blocks inject adaptively, extending under-scanning and Virtual Scanning toward stronger cross-layout generalization.

### Looking Around Flatland: End-to-End 2D Real-Time NLOS Imaging

- María Peña, Diego Gutierrez, Julio Marco
- *IEEE Transactions on Computational Imaging*, vol. 11, pp. 189–200, 2025
- DOI: `10.1109/TCI.2025.3536092`
- Reformulates transient light transport in self-contained 2D worlds and couples it to phasor-field camera models. It supplies real-time progressive simulation and reconstruction, with reported speedups of up to five orders of magnitude over equivalent 3D experiments, for controlled analysis of NLOS assumptions and parameters.

## Intended synchronized artifacts

- `README.md`: three Latest Additions rows and milestone-timeline entries.
- `index.html`: three paper-explorer records, updated count, and 2025/2026 timeline text.
- `article/2active.tex`: active-SPAD table citations plus semantically placed review paragraphs on native arbitrary-relay back projection and the Flatland testbed.
- `article/4datadriven.tex`: a review paragraph connecting reprojection-guided recovery to under-scanning, Virtual Scanning, and TransDiff.
- `bare_jrnl.tex`: integration marker in the master source.
- `egbib_merged_20260711.bib`: canonical final-venue metadata merged from `egbib_20260718_irregular_relay_flatland_updates.bib`.
- `bare_jrnl.pdf`: clean LaTeX/BibTeX rebuild after source and bibliography validation.

## Validation requirements

The guarded workflow must verify unique README and homepage records, citation presence in the relevant survey section, one canonical BibTeX entry per key, a homepage count matching the paper array, no undefined or repeated bibliography entries, nonempty rendered PDF pages, and recognizable new review text and references in the generated PDF. The PDF must be committed only after all checks pass.

## Hardware-table clarification

Flatland is an enabling 2D transient simulation and analysis framework, not a pulsed-laser/SPAD hardware experiment. It is integrated in the active-method literature review and bibliography, but intentionally excluded from the hardware-specific active-SPAD summary row.
