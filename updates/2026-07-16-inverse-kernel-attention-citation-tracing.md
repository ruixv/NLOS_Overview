# Learnable inverse-kernel NLOS citation-tracing and consistency update

Date: 16 July 2026

## Candidate and verification

**Enhancing Non-Line-of-Sight Imaging via Learnable Inverse Kernel and Attention Mechanisms** — Yanhua Yu, Siyuan Shen, Zi Wang, Binbin Huang, Yuehan Wang, Xingyue Peng, Suan Xia, Ping Liu, Ruiqian Li, and Shiying Li, IEEE/CVF International Conference on Computer Vision (ICCV), pages 10563--10573, 2023.

The final ICCV paper and pagination were verified from the official CVF proceedings link and from the full reference metadata in later NLOS reconstruction work. No separate arXiv version or later journal extension was verified, so the repository records the final ICCV 2023 venue rather than labeling the work as arXiv.

The paper is directly about active transient NLOS reconstruction. It introduces a learnable inverse kernel tailored to the imaging-system point-spread function and combines it with attention mechanisms to recover hidden intensity and depth. Later work treats the method, abbreviated I-K, as a principal learned NLOS baseline alongside LCT, f-k migration, phasor-field/RSD, Learned Feature Embeddings, and NLOST, confirming that it is part of the core learned-reconstruction trajectory rather than an incidental citation.

## Citation-tracing route

The candidate was recovered from the learned-reconstruction references of recent arbitrary-relay / differentiable transient work and then cross-checked through *Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors*. That paper explicitly evaluates I-K as a CNN-based NLOS reconstruction baseline and provides the full ICCV citation. This forward/reference tracing connects I-K to the field-defining LCT, f-k, phasor-field, LFE, and NLOST sequence.

## Repository gap found

The exact paper title, official CVF proceedings URL, author list, and citation key were absent from README, the website paper explorer, the development timeline, `article/2active.tex`, `article/4datadriven.tex`, and the consolidated bibliography. The omission left a visible gap between the repository's 2020 Learned Feature Embeddings milestone and its 2023 transformer/generalizable-physics entries.

## Intended synchronized changes

- Add canonical ICCV 2023 BibTeX metadata under `yuLearnableInverseKernel2023`.
- Add one README Latest Additions entry with the final conference venue and a concise contribution summary.
- Add one searchable website entry and change the tracked-latest count from 103 to 104.
- Expand the 2023 timeline to include learnable inverse kernels and attention-based transient inversion.
- Add the paper to the active pulsed-laser/SPAD reconstruction table.
- Insert a dedicated literature-review paragraph in `article/4datadriven.tex` between shared learned feature embeddings and later transformer/adaptive-prior models.
- Regenerate the duplicate-free consolidated bibliography and `bare_jrnl.pdf` through the validation workflow.

## Fresh-search result

The current keyword, project-page, lab-page, and citation-tracing pass did not identify a metadata-verifiable direct NLOS imaging paper newer than the repository's 5 July 2026 NIR raster-scanning entry. This run therefore prioritizes the high-confidence ICCV 2023 omission rather than adding a weak or merely adjacent candidate.

## Validation requirements

The workflow must fail on undefined citations, missing or repeated BibTeX entries, duplicate README/homepage records, an incorrect homepage count, missing survey prose, or a generated PDF that is empty, unreadable, or lacks the new literature-review text. Every PDF page is rendered during validation.
