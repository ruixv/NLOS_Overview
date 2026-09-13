# 2026-09-13 update: NLOSdiffuser

Verified missing paper:

- Xian Gao, Luyang Wang, Jiacheng Ruan, Yuyang Zhang, Zongyun Zhang, Ting Liu, and Yuzhuo Fu, **“NLOSdiffuser: Generalized Steady-State Non-Line-of-sight Imaging toward Indoor Scenarios,”** 2025 IEEE International Conference on Multimedia and Expo (ICME), pp. 1–6, 2025. DOI: 10.1109/ICME59968.2025.11210160.

## Why it belongs

NLOSdiffuser is a direct steady-state/passive NLOS reconstruction paper rather than a generic diffusion application. It targets indoor relay-wall measurements with a two-stage reconstruction pipeline: pixel-level coarse inversion produces an intermediate representation, followed by semantic refinement with a pretrained diffusion model. Training uses synthetic indoor scenes while evaluation includes diverse real indoor scenarios, making it relevant to the trajectory from early steady-state inversion toward generative priors with improved cross-scene generalization.

## Safe integration targets

1. **README.md — Latest Additions / Passive NLOS / Deep Learning.** Add the final ICME 2025 venue, DOI, and a concise summary emphasizing steady-state indoor generalization and pretrained diffusion refinement.
2. **article/3passive.tex.** Insert after the discussion of supervised/attention-based passive reconstruction and before or alongside later diffusion-guided passive methods. Suggested prose:

   `Gao et al. introduced NLOSdiffuser for generalized steady-state indoor NLOS imaging~\cite{gaoNLOSdiffuser2025}. A coarse pixel-level reconstruction first maps diffuse relay-wall observations into an intermediate representation, after which a pretrained diffusion model performs semantic refinement. Training on synthetic indoor scenes and validation across varied real environments shift steady-state learned inversion from fixed-scene mappings toward generative priors designed for cross-scene generalization.`

3. **egbib_merged_20260711.bib.** Merge the verified `gaoNLOSdiffuser2025` entry from `egbib_20260913_nlosdiffuser.bib`.
4. **index.html / paper explorer / timeline.** Categorize as `Passive / steady-state / learned reconstruction / diffusion`, venue `ICME 2025`, year 2025.
5. **bare_jrnl.pdf.** Recompile only after the survey source and canonical bibliography have been integrated. Verify the final PDF bibliography resolves `gaoNLOSdiffuser2025` and that README, website, TeX, bibliography, and PDF agree.

## Verification notes

- IEEE Xplore lists the paper in ICME 2025 (conference dates 30 June–4 July 2025; DOI above).
- DBLP independently lists all seven authors and pages 1–6.
- Repository-wide GitHub search returned no hit for the title, `NLOSdiffuser`, or DOI `11210160`; the public README snapshot likewise contains no `NLOSdiffuser` string.
- Large public-facing files were not overwritten from truncated connector reads. This note and the verified BibTeX entry are staged specifically to avoid partial-file data loss.
