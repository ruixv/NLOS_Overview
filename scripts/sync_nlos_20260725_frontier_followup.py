#!/usr/bin/env python3
"""Synchronize verified NLOS frontier gaps across public and survey artifacts.

The script is idempotent and fails closed on ambiguous insertion anchors. It
finishes the pending NIF/SCISA synchronization and integrates citation-traced
under-scanning, adaptive f-k, arbitrary-relay 3D-GTR, and Quasi-Fresnel work.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
DATA = ROOT / "article" / "4datadriven.tex"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-25-frontier-followup.md"
KEYS = ROOT / "updates" / "2026-07-25-frontier-followup-keys.txt"
TRACE = "% 25 July 2026 frontier trace: NIF, SCISA-Net, dual-model under-scanning, adaptive neural Stolt resampling, arbitrary-relay 3D-GTR, and Quasi-Fresnel imaging synchronized."

PAPERS = [
    dict(
        key="zhangNeuralIlluminationFields2026",
        title="Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging",
        url="https://doi.org/10.1016/j.optlaseng.2025.109514",
        doi="10.1016/j.optlaseng.2025.109514",
        year=2026, venue="Optics and Lasers in Engineering 2026",
        cats="latest newscenes active shadow two-bounce learning neural implicit",
        summary="Self-supervised Neural Illumination Fields optimize continuous hidden density and illumination-dependent intensity through differentiable shadow rendering, avoiding binary segmentation and retaining centimeter-scale detail under low contrast and ambient illumination.",
        authors="Zhang et al.", readme=False,
        bib=r'''@article{zhangNeuralIlluminationFields2026,
  author = {Zhang, Jingyuan and Zhang, Bochao and Wang, Zijin and Qu, Chao and Bai, Lianfa and Chen, Xiaoyu and Han, Jing and Guo, Baohui},
  title = {Neural Illumination Fields: High-Fidelity and Ambient-Robust Stereo Reconstruction for Two-Bounce Non-Line-of-Sight Imaging},
  journal = {Optics and Lasers in Engineering}, volume = {198}, pages = {109514}, year = {2026},
  doi = {10.1016/j.optlaseng.2025.109514}, url = {https://doi.org/10.1016/j.optlaseng.2025.109514}
}'''),
    dict(
        key="daiSCISANet2026",
        title="SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations",
        url="https://doi.org/10.3390/photonics13060575", doi="10.3390/photonics13060575",
        year=2026, venue="Photonics 2026", cats="latest learning recognition semantic passive",
        summary="Scene-constrained regularized inversion and multi-stage Haar-subband attention infer 31 hidden-display categories from calibrated wall-mediated observations; the task is semantic NLOS sensing rather than complete image or geometry reconstruction.",
        authors="Dai et al.", readme=True,
        bib=r'''@article{daiSCISANet2026,
  author = {Dai, Jihao and Qin, Hongshuai and Li, Guowen and Liu, Jin and Zhang, Xiaoshuai and Qi, Huiyu and Zheng, Zhiwen and Huang, Xingru},
  title = {{SCISA-Net}: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations},
  journal = {Photonics}, volume = {13}, number = {6}, pages = {575}, year = {2026},
  doi = {10.3390/photonics13060575}, url = {https://doi.org/10.3390/photonics13060575}
}'''),
    dict(
        key="yanDualModelUnderscanning2026",
        title="Dual-model guided active NLOS imaging with under-scanning measurements",
        url="https://doi.org/10.1007/s00371-026-04381-6", doi="10.1007/s00371-026-04381-6",
        year=2026, venue="The Visual Computer 2026", cats="latest active learning underscanning reconstruction",
        summary="A spatio-temporal recovery module completes sparse transients before dual LCT and f-k branches recover complementary global structure and fine texture, with adaptive feature fusion for efficient under-scanned reconstruction.",
        authors="Yan et al.", readme=True,
        bib=r'''@article{yanDualModelUnderscanning2026,
  author = {Yan, Zhihang and Liu, Hao and Liu, Mengge and Zhang, Sai and Wang, Huimin and Jin, Shaohui and Xu, Mingliang},
  title = {Dual-Model Guided Active {NLOS} Imaging with Under-Scanning Measurements},
  journal = {The Visual Computer}, volume = {42}, number = {4}, pages = {174}, year = {2026},
  doi = {10.1007/s00371-026-04381-6}, url = {https://doi.org/10.1007/s00371-026-04381-6}
}'''),
    dict(
        key="wangAdaptiveNeuralGrid2026",
        title="Non-line-of-sight imaging based on adaptive neural grid resampling",
        url="https://doi.org/10.2139/ssrn.7022018", doi="10.2139/ssrn.7022018",
        year=2026, venue="SSRN preprint 2026", cats="latest active learning fk calibration preprint",
        summary="A lightweight Grid Offset Network predicts local frequency-domain sampling offsets and adaptively calibrates the f-k Stolt mapping under timing, propagation-speed, and sparse-sampling perturbations while preserving fast migration.",
        authors="Wang et al.", readme=True,
        bib=r'''@misc{wangAdaptiveNeuralGrid2026,
  author = {Wang, Mengfan and Yu, Jiatong and Tang, Xingfen and Zhou, Yongkang and Zhu, Youpan and Yang, Yang and Pang, Huaisheng},
  title = {Non-Line-of-Sight Imaging Based on Adaptive Neural Grid Resampling},
  howpublished = {SSRN preprint}, year = {2026}, note = {Posted 29 June 2026},
  doi = {10.2139/ssrn.7022018}, url = {https://doi.org/10.2139/ssrn.7022018}
}'''),
    dict(
        key="wang3DGTR2026",
        title="Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering",
        url="https://doi.org/10.1145/3799902.3811137", doi="10.1145/3799902.3811137",
        year=2026, venue="SIGGRAPH 2026", cats="latest active arbitrary-relay gaussian differentiable rendering",
        summary="LOS-guided relay geometry and a differentiable 3D Gaussian transient renderer enable confocal and non-confocal reconstruction from spatially limited, sparse, non-planar, and arbitrarily shaped relay surfaces.",
        authors="Wang et al.", readme=False,
        bib=r'''@inproceedings{wang3DGTR2026,
  author = {Wang, Yi and Zhan, Ziyu and Wang, Yuran and Wang, Hao and Liu, Qiang and Shi, Zuoqiang and Qiu, Lingyun and Fu, Xing},
  title = {Non-Line-of-Sight Imaging with Arbitrary Relay Surface Geometries via {3D Gaussian Transient Rendering}},
  booktitle = {SIGGRAPH Conference Papers}, pages = {1--11}, year = {2026}, publisher = {ACM},
  doi = {10.1145/3799902.3811137}, url = {https://doi.org/10.1145/3799902.3811137}, eprint = {2606.21270}, archivePrefix = {arXiv}
}'''),
    dict(
        key="weiQuasiFresnel2026",
        title="Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform",
        url="https://arxiv.org/abs/2508.02003", doi="",
        year=2026, venue="Optica, accepted", cats="latest active transform efficiency accepted",
        summary="Represents common hidden surfaces and aggregated transients as two-dimensional functions and derives a Quasi-Fresnel inversion, reducing runtime and memory by orders of magnitude and enabling high-resolution NLOS on lightweight devices.",
        authors="Wei et al.", readme=True,
        bib=r'''@article{weiQuasiFresnel2026,
  author = {Wei, Yijun and Wang, Jianyu and Xiao, Leping and Shi, Zuoqiang and Fu, Xing and Qiu, Lingyun},
  title = {Fast and Memory-Efficient Non-Line-of-Sight Imaging with Quasi-Fresnel Transform},
  journal = {Optica}, year = {2026}, note = {Accepted; arXiv:2508.02003},
  url = {https://arxiv.org/abs/2508.02003}, eprint = {2508.02003}, archivePrefix = {arXiv}
}'''),
]


def read(p):
    if not p.exists(): raise SystemExit(f"Missing required file: {p.relative_to(ROOT)}")
    return p.read_text(encoding="utf-8")

def write(p, s):
    old = p.read_text(encoding="utf-8") if p.exists() else None
    if old != s:
        p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")

def bib_entry_span(text, key):
    m = re.search(r"(?mi)^@(article|inproceedings|misc|incollection)\{" + re.escape(key) + r",", text)
    if not m: return None
    pos, depth = m.end(), 1
    while pos < len(text) and depth:
        depth += (text[pos] == "{") - (text[pos] == "}"); pos += 1
    if depth: raise SystemExit(f"Unbalanced BibTeX entry: {key}")
    return m.start(), pos

def key_for_doi(text, doi):
    if not doi: return None
    for m in re.finditer(r"(?mi)^@(article|inproceedings|misc|incollection)\{([^,]+),", text):
        start, key = m.start(), m.group(2)
        span = bib_entry_span(text, key)
        if span and doi.lower() in text[span[0]:span[1]].lower(): return key
    return None

def upsert_bib(text, paper):
    key = key_for_doi(text, paper["doi"]) or paper["key"]
    span = bib_entry_span(text, key)
    if span:
        # Normalize only stable/known keys; preserve an existing differently named DOI record.
        if key == paper["key"]: text = text[:span[0]] + paper["bib"] + text[span[1]:]
    else:
        text = text.rstrip() + "\n\n" + paper["bib"] + "\n"
    return text, key

readme, index = read(README), read(INDEX)
active, data, newscenes = read(ACTIVE), read(DATA), read(NEWSCENES)
survey, bib = read(SURVEY), read(BIB)

# Correct the public 3D-GTR link from arXiv to the verified SIGGRAPH DOI.
readme = readme.replace("[Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270)", "[Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://doi.org/10.1145/3799902.3811137)")

# Resolve bibliography keys first, preserving stable existing records when present.
resolved = {}
for p in PAPERS:
    bib, resolved[p["key"]] = upsert_bib(bib, p)

# README additions.
header = "|------|-------|----------------|----------------|\n"
if readme.count(header) != 1: raise SystemExit("README Latest Additions header is ambiguous")
rows = []
for p in PAPERS:
    n = readme.lower().count(p["title"].lower())
    if n == 0 and p["readme"]:
        rows.append(f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["summary"]} |')
    elif n > 1: raise SystemExit(f'Duplicate README title: {p["title"]}')
if rows: readme = readme.replace(header, header + "\n".join(rows) + "\n", 1)
readme = re.sub(r"\*\*Update run: (?:24|25) July 2026\.\*\*", "**Update run: 25 July 2026.**", readme, count=1)
if "## Milestone Timeline" not in readme:
    readme += "\n\n---\n\n## Milestone Timeline\n\n- **2026 — Physics-aware sparse acquisition:** dual LCT/f-k reconstruction, adaptive neural Stolt resampling, and Quasi-Fresnel dimensionality reduction move active NLOS toward faster and lighter deployment.\n- **2026 — Arbitrary relays and semantics:** 3D-GTR supports curved and spatially limited relay surfaces, while NIF and SCISA-Net extend hidden-scene inference toward neural shadow fields and calibrated semantic sensing.\n"

# Website paper explorer.
anchor = "    const papers=[\n" if "    const papers=[\n" in index else "    const papers = [\n"
if index.count(anchor) != 1: raise SystemExit("Website paper-array anchor is ambiguous")
objects, inserted = [], 0
for p in PAPERS:
    n = index.lower().count(p["title"].lower())
    if n == 0:
        objects.append(f'      {{cat:"{p["cats"]}",title:"{p["title"]}",authors:"{p["authors"]}",year:{p["year"]},venue:"{p["venue"]}",url:"{p["url"]}",key:"{p["summary"]}"}},')
        inserted += 1
    elif n > 1: raise SystemExit(f'Duplicate website title: {p["title"]}')
if objects: index = index.replace(anchor, anchor + "\n".join(objects) + "\n", 1)
cm = re.findall(r'<b>(\d+)</b><span>tracked latest entries</span>', index)
if len(cm) != 1: raise SystemExit("Website tracked-entry count is ambiguous")
new_count = int(cm[0]) + inserted
index = re.sub(r'<b>\d+</b><span>tracked latest entries</span>', f'<b>{new_count}</b><span>tracked latest entries</span>', index, count=1)
index = index.replace("Updated 24 July 2026 · 190+ papers", "Updated 25 July 2026 · 190+ papers")
index = index.replace("Last updated: 24 July 2026", "Last updated: 25 July 2026")
index = index.replace("https://arxiv.org/abs/2606.21270", "https://doi.org/10.1145/3799902.3811137")
# Enrich the 2026 historical-development block once.
timeline_sentence = " Dual-model LCT/f-k fusion and adaptive neural Stolt resampling advanced under-scanned reconstruction; Quasi-Fresnel inversion reduced active-NLOS dimensionality; 3D-GTR removed planar-relay assumptions; and SCISA-Net established calibrated wall-mediated semantic inference."
pat = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body">.*?<p>)(.*?)(</p>)', re.S)
m = pat.search(index)
if m and timeline_sentence.strip() not in m.group(2):
    index = index[:m.start()] + m.group(1) + m.group(2) + timeline_sentence + m.group(3) + index[m.end():]

# Semantically placed survey prose.
scisa_key = resolved["daiSCISANet2026"]
if f"\\cite{{{scisa_key}}}" not in data:
    a = "Together with learned feature embeddings and NLOS-R$^2$, these studies establish recognition, action understanding, and clustering as a parallel trajectory to hidden-scene reconstruction."
    if data.count(a) != 1: raise SystemExit("SCISA recognition anchor is ambiguous")
    prose = f'''\n\n\\vspace{{0.8mm}}\n\\noindent \\textbf{{Calibrated wall-mediated semantic inference.}}\nDai~\\etal~use only a calibrated wall-mediated observation of a display outside the camera field of view for 31-way category inference~\\cite{{{scisa_key}}}. Scene-constrained regularized inversion reorganizes weak indirect evidence, while multi-stage Haar-subband attention preserves discriminative mid- and high-frequency cues under attenuation, ambient background, and matched operator re-parameterization. The method performs semantic NLOS sensing rather than full hidden-image, depth, or geometry reconstruction.\n'''
    data = data.replace(a, a + prose, 1)

dual_key = resolved["yanDualModelUnderscanning2026"]
if f"\\cite{{{dual_key}}}" not in data:
    a = "\\subsection{Network combined with physical models} \\label{combined}"
    if data.count(a) != 1: raise SystemExit("Physics-network subsection anchor is ambiguous")
    prose = f'''\n\n\\vspace{{0.8mm}}\n\\noindent \\textbf{{Dual-model guidance for under-scanned transients.}}\nYan~\\etal~first recover sufficient-density measurements from sparse transients with three-dimensional pyramid pooling and window attention, then combine LCT and $f$--$k$ branches to retain complementary global structure and fine texture~\\cite{{{dual_key}}}. Multi-scale refinement and adaptive fusion place classical geometric- and wave-optics inverses inside one learned under-scanning pipeline, extending measurement completion beyond a single fixed reconstruction backend.\n'''
    data = data.replace(a, a + prose, 1)

gon_key, qf_key = resolved["wangAdaptiveNeuralGrid2026"], resolved["weiQuasiFresnel2026"]
if f"\\cite{{{gon_key}}}" not in active or f"\\cite{{{qf_key}}}" not in active:
    a = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Challenges and Prospects}"
    if active.count(a) != 1: raise SystemExit("Active-challenges anchor is ambiguous")
    prose = f'''\\vspace{{0.8mm}}\n\\noindent \\textbf{{Learned Stolt calibration and dimension-reduced inversion.}}\nWang~\\etal~retain the speed of $f$--$k$ migration but replace fixed Stolt interpolation with a lightweight Grid Offset Network that predicts local frequency-domain resampling offsets under timing, propagation-speed, and sparse-sampling perturbations~\\cite{{{gon_key}}}. Wei~\\etal~take an orthogonal efficiency route with the Quasi-Fresnel transform, representing typical hidden surfaces and aggregated measurements as two-dimensional functions and deriving a direct inversion with substantially lower computational and memory complexity~\\cite{{{qf_key}}}. These developments show that practical acceleration can come from calibrating the migration grid or reducing the inverse problem's intrinsic dimensionality, rather than only pruning relay samples.\n\n'''
    active = active.replace(a, prose + a, 1)

gtr_key = resolved["wang3DGTR2026"]
if f"\\cite{{{gtr_key}}}" not in newscenes:
    a = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Scattering-Media NLOS Imaging}"
    if newscenes.count(a) != 1: raise SystemExit("Arbitrary-relay insertion anchor is ambiguous")
    prose = f'''\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{{Arbitrary Relay Surfaces with Gaussian Transient Rendering}}\n\\subsection{{Arbitrary Relay Surfaces with Gaussian Transient Rendering}}\nWang~\\etal~introduced a LOS-guided pipeline that estimates visible relay geometry and represents the hidden scene with 3D Gaussian primitives optimized by a differentiable transient renderer~\\cite{{{gtr_key}}}. The method supports confocal and non-confocal measurements on spatially limited, sparse, planar, and strongly curved relay regions, then synthesizes transients on a virtual relay surface for conventional volumetric reconstruction. This work connects differentiable transient rendering with deployable arbitrary-relay capture and removes the large planar wall from the core geometric assumptions of learned NLOS inversion.\n\n'''
    newscenes = newscenes.replace(a, prose + a, 1)

if TRACE not in survey:
    a = "%% bare_jrnl.tex\n"
    if survey.count(a) != 1: raise SystemExit("Survey marker anchor is ambiguous")
    survey = survey.replace(a, a + TRACE + "\n", 1)

# Final uniqueness checks.
for p in PAPERS:
    if index.lower().count(p["title"].lower()) != 1: raise SystemExit(f'Website title count invalid: {p["title"]}')
    if p["readme"] and readme.lower().count(p["title"].lower()) != 1: raise SystemExit(f'README title count invalid: {p["title"]}')
for key in (scisa_key, dual_key, gon_key, qf_key, gtr_key):
    if not bib_entry_span(bib, key): raise SystemExit(f"Missing bibliography key: {key}")

note = f'''# NLOS frontier follow-up — 25 July 2026

## Result

No direct NLOS publication with a verified publication date later than 22 July 2026 was identified. The newest remains *Iterating the transient light transport matrix for non-line-of-sight imaging* in Nature Communications.

This synchronization completes the pending NIF and SCISA-Net cross-artifact work and integrates three citation/keyword-traced reconstruction advances plus one accepted final-venue update:

- Dual-model guided active NLOS imaging with under-scanning measurements — The Visual Computer 42(4), article 174 (2026), DOI 10.1007/s00371-026-04381-6.
- Non-line-of-sight imaging based on adaptive neural grid resampling — SSRN preprint, posted 29 June 2026, DOI 10.2139/ssrn.7022018; no final venue was verified.
- Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering — SIGGRAPH 2026, DOI 10.1145/3799902.3811137; the public link was corrected from arXiv to the final ACM record.
- Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform — accepted by Optica according to the authors' laboratory publication page; arXiv:2508.02003 remains the source because volume/pages/DOI are not yet available.
- SCISA-Net — Photonics 13(6), 575 (2026), DOI 10.3390/photonics13060575.

## Integration

README, website explorer/timeline, semantically appropriate survey sections, consolidated bibliography, survey trace, and regenerated PDF are validated by the accompanying workflow. Website tracked-entry count after this run: {new_count}.
'''

for p, s in ((README, readme), (INDEX, index), (ACTIVE, active), (DATA, data), (NEWSCENES, newscenes), (SURVEY, survey), (BIB, bib), (NOTE, note)):
    write(p, s)
write(KEYS, "\n".join(dict.fromkeys([scisa_key, dual_key, gon_key, qf_key, gtr_key])) + "\n")
print(f"Frontier follow-up synchronized; website count={new_count}.")
