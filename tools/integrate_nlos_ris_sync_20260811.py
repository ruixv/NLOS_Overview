#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def load(p): return (ROOT / p).read_text(encoding="utf-8")
def save(p, s): (ROOT / p).write_text(s, encoding="utf-8")

def require_replace(text, old, new, label):
    if new in text:
        return text
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {n}")
    return text.replace(old, new, 1)

def insert_before(text, anchor, block, marker, label):
    if marker in text:
        return text
    n = text.count(anchor)
    if n != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {n}")
    return text.replace(anchor, block + anchor, 1)

def insert_after_line(text, title_fragment, block, marker, label):
    if marker in text:
        return text
    pat = re.compile(r'^.*' + re.escape(title_fragment) + r'.*$', re.M)
    matches = list(pat.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one matching row, found {len(matches)}")
    m = matches[0]
    return text[:m.end()] + "\n" + block.rstrip("\n") + text[m.end():]

def update_readme():
    s = load("README.md")
    old = "](https://arxiv.org/abs/2508.02348) — Park et al. | arXiv 2025 |"
    new = "](https://doi.org/10.1109/IROS60139.2025.11246461) — Park et al. | IEEE/RSJ IROS 2025, 19661–19668 |"
    if old in s:
        s = s.replace(old, new)
    elif "10.1109/IROS60139.2025.11246461" not in s:
        raise RuntimeError("README: Park record not found")

    latest = (
        "| 2025 | [Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring](https://doi.org/10.1109/IMBioC63524.2025.10989670) — Tripathy et al. | IEEE MTT-S IMBioC 2025 | A liquid-crystal RIS and self-injection-locked radar actively redirect sensing energy into an occluded region for measured contactless respiration/heartbeat monitoring. |\n"
        "| 2025 | [Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces](https://doi.org/10.12263/DZXB.20240674) — Li et al. | Acta Electronica Sinica 53(1), 1–13 (2025) | Visually aided RIS coding redirects RF illumination toward a hidden subject; improved variational-mode decomposition recovers breathing and heartbeat, extending NLOS sensing from geometry/localization to physiological semantics. |\n"
    )
    if s.count("Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces") == 0:
        hdr = "|------|-------|----------------|----------------|\n"
        start = s.find("## Latest Additions")
        i = s.find(hdr, start)
        if i < 0: raise RuntimeError("README: Latest Additions table header missing")
        i += len(hdr)
        s = s[:i] + latest + s[i:]

    main = (
        "| 2025 | [Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces](https://doi.org/10.12263/DZXB.20240674) — Li et al. | Acta Electronica Sinica 53(1), 1–13 (2025) | Uses visual target localization to program a reconfigurable intelligent surface so RF sensing energy is redirected into a hidden human region, then estimates respiration and heartbeat with an improved VMD pipeline. This is NLOS physiological sensing rather than hidden-shape reconstruction. |\n"
        "| 2025 | [Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring](https://doi.org/10.1109/IMBioC63524.2025.10989670) — Tripathy et al. | IEEE MTT-S IMBioC 2025 | Integrates a phase-reconfigurable liquid-crystal RIS with a self-injection-locked radar, electronically steering the sensing path into an NLOS region and experimentally demonstrating contactless vital-sign monitoring. |\n"
    )
    if s.count("Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces") < 2:
        s = insert_after_line(s, "Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface", main,
                              "Uses visual target localization to program a reconfigurable intelligent surface", "README RF/RIS list")

    timeline = "   │     RIS-enabled RF sensing becomes actively reconfigurable: programmable and liquid-crystal surfaces steer energy into hidden regions for around-corner radar and physiological monitoring [IEEE RadarConf / IMBioC / Acta Electronica Sinica]\n"
    if timeline.strip() not in s:
        anchor = "2025 ── mmNorm: mmWave surface-normal estimation advances hidden RF sensing from localization to 3D object geometry [MobiSys]\n"
        if anchor not in s: raise RuntimeError("README: RF timeline anchor missing")
        s = s.replace(anchor, anchor + timeline, 1)
    save("README.md", s)

def update_index():
    s = load("index.html")
    old = '{cat:"latest modality",title:"mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera",authors:"Park et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2508.02348",key:"Camera-derived road layout helps interpret mmWave radar point clouds for NLOS pedestrian localization."}'
    new = '{cat:"latest modality rf mmwave localization robotics camera-fusion",title:"mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera",authors:"Park et al.",year:2025,venue:"IEEE/RSJ IROS 2025, 19661–19668",url:"https://doi.org/10.1109/IROS60139.2025.11246461",key:"Camera-derived T-junction road geometry conditions multipath-distorted mmWave point clouds for hidden-pedestrian localization on a real vehicle; final IROS 2025 venue verified."}'
    if old in s: s = s.replace(old, new, 1)
    elif "10.1109/IROS60139.2025.11246461" not in s: raise RuntimeError("index: Park record missing")

    objects = (
        '      {cat:"latest modality rf radar ris vital-sign",title:"Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces",authors:"Li et al.",year:2025,venue:"Acta Electronica Sinica 53(1), 1–13 (2025)",url:"https://doi.org/10.12263/DZXB.20240674",key:"Visually aided RIS coding redirects RF sensing energy toward a hidden human target; improved VMD estimates respiration and heartbeat, making this physiological NLOS sensing rather than geometric reconstruction."},\n'
        '      {cat:"latest modality rf radar ris vital-sign",title:"Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring",authors:"Tripathy et al.",year:2025,venue:"IEEE MTT-S IMBioC 2025",url:"https://doi.org/10.1109/IMBioC63524.2025.10989670",key:"A phase-reconfigurable liquid-crystal RIS integrated with a self-injection-locked radar electronically steers the sensing path into an NLOS region for measured contactless vital-sign monitoring."},\n'
    )
    if "Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces" not in s:
        anchor = '      {cat:"latest modality",title:"Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface"'
        i = s.find(anchor)
        if i < 0: raise RuntimeError("index: dual-beam RIS anchor missing")
        s = s[:i] + objects + s[i:]
    s = s.replace('<div class="stat"><b>275</b><span>tracked latest entries</span></div>', '<div class="stat"><b>277</b><span>tracked latest entries</span></div>')
    marker = "Programmable and liquid-crystal RISs additionally turned the relay path into a controllable component, steering RF sensing energy into hidden regions for around-corner radar and contactless vital-sign monitoring."
    if marker not in s:
        pat = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
        m = pat.search(s)
        if not m: raise RuntimeError("index: 2025 timeline block missing")
        s = s[:m.start()] + m.group(1) + m.group(2).rstrip() + " " + marker + m.group(3) + s[m.end():]
    save("index.html", s)

def update_active():
    s = load("article/2active.tex")
    marker = "Measurement-adaptive regularization and transient completion."
    block = r'''
\vspace{0.8mm}
\noindent \textbf{Measurement-adaptive regularization and transient completion.}
Recent active NLOS work revisits robustness and sparse acquisition without abandoning the physical forward operator. Zhou~\etal~construct a ground-truth-free TOF-SSIM criterion and adaptively modify transient histograms before backprojection, suppressing reconstruction artifacts in both confocal and non-confocal geometries~\cite{zhouAdaptiveArtifactCancellationNLOS2025}. Ding~\etal~stabilize under-sampled recovery with object-domain and joint signal--object-domain curvature regularization and GPU-oriented ADMM solvers~\cite{dingCurvatureRegularizationNLOS2024}. Cui~\etal~instead treat aperture-limited acquisition as a measurement-constrained latent-diffusion problem: TransDiff restores dense transient information without paired supervision before hidden-scene reconstruction~\cite{cuiTransDiffNLOS2025}. Oyama~\etal~move adaptation into acquisition itself, shifting an Archimedean spiral toward relay-wall regions with stronger sequential returns and compensating the resulting nonuniform density with Voronoi weights~\cite{oyamaAdaptiveSpiralNLOS2026}. Together, these methods make data quality, relay-aperture support, and sample placement explicit optimization variables rather than fixed assumptions inherited from dense rectangular scanning.

'''
    if marker not in s:
        # Keep the paragraph in the active-method reconstruction section, before its final challenge discussion when available.
        m = re.search(r'\\bookmark\[dest=\\HyperLocalCurrentHref,level=2\]\{Challenges[^}]*\}', s)
        if m: s = s[:m.start()] + block + s[m.start():]
        else: s = s.rstrip() + "\n\n" + block
    save("article/2active.tex", s)

def update_learning():
    s = load("article/4datadriven.tex")
    marker = "Optimization-derived attention and frequency-domain expert fusion."
    block = r'''
\vspace{0.8mm}
\noindent \textbf{Optimization-derived attention and frequency-domain expert fusion.}
A parallel physics-guided trajectory derives adaptive network-like weighting directly from optimization variables instead of learning every gate from paired data. Zhang~\etal~model non-Gaussian NLOS residuals with a mixture distribution and obtain dual-space adaptive weights that act as zero-shot attention inside an alternating solver~\cite{zhangAdaptiveMixtureAttentionNLOS2025}. Their later frequency-domain multi-regularization-experts formulation partitions the inverse problem across complementary regularized Wiener-style experts and fuses them with gates derived from dual variables~\cite{zhangFrequencyMoENLOS2026}. These methods complement CMFormer, NLOST, and transient Transformers by showing that attention and mixture-of-experts behavior can emerge from the inverse model itself, retaining interpretability and avoiding a fully supervised gating network.

'''
    anchor = "\\noindent \\textbf{Dual-model guidance for under-scanned transients.}"
    s = insert_before(s, anchor, block, marker, "learning survey")
    save("article/4datadriven.tex", s)

def update_newscenes():
    s = load("article/5newscenes.tex")
    sparse_marker = "Adaptive sparse acquisition beyond fixed relay grids."
    sparse = r'''
\vspace{0.8mm}
\noindent \textbf{Adaptive sparse acquisition beyond fixed relay grids.}
The sparse-acquisition branch now spans both prior design and measurement design. Curvature regularization supplies higher-order geometric priors when relay samples are severely under-sampled~\cite{dingCurvatureRegularizationNLOS2024}; TransDiff recovers missing aperture information through an unsupervised measurement-consistent diffusion prior~\cite{cuiTransDiffNLOS2025}; and adaptive spiral scanning reallocates confocal measurements online toward high-return wall regions while correcting nonuniform sampling density~\cite{oyamaAdaptiveSpiralNLOS2026}. This progression moves sparse NLOS from merely tolerating missing measurements toward choosing where measurements should be made and learning how incomplete apertures should be completed.

'''
    anchor = "\\noindent \\textbf{Masked transient pretraining.}"
    s = insert_before(s, anchor, sparse, sparse_marker, "new-scenes sparse paragraph")

    needle = "A follow-on dual-beam RIS radar study~\\cite{yasmeenDualBeamRIS2026} examines a lower-complexity one-bit quantized RIS configuration that produces dual symmetric beams, benchmarking the resulting beam steering and radar cross-section against metal reflectors and ideal single-beam RIS baselines."
    ris = " The same controllable-propagation idea is now being used for physiological NLOS sensing rather than only angle, location, or micro-Doppler recovery. Li~\\etal~use visual target localization to program a reconfigurable intelligent surface so RF energy is redirected toward a hidden subject, then estimate respiration and heartbeat with an improved variational-mode-decomposition pipeline~\\cite{liRISVitalSignNLOS2025}. Tripathy~\\etal~integrate a liquid-crystal RIS with a self-injection-locked radar; phase-controlled wavefront steering places the sensing beam in an occluded region and measured experiments demonstrate contactless vital-sign monitoring~\\cite{tripathyLCRISVitalSign2025}. These studies should be interpreted as semantic/physiological NLOS sensing, not hidden-shape reconstruction."
    if "liRISVitalSignNLOS2025" not in s:
        if s.count(needle) != 1: raise RuntimeError("new-scenes: dual-beam RIS sentence missing")
        s = s.replace(needle, needle + ris, 1)

    old = r"\href{https://arxiv.org/abs/2508.02348}{Park~\etal} use camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, connecting around-corner radar perception to autonomous-driving scene understanding."
    new = r"Park~\etal~use camera-derived road layout to interpret multipath-distorted mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, with a real-vehicle outdoor evaluation reported in the final IROS publication~\cite{parkTjunctionPedestrian2025}."
    if old in s: s = s.replace(old, new, 1)
    elif "parkTjunctionPedestrian2025" not in s: raise RuntimeError("new-scenes: Park arXiv prose missing")

    isar_marker = "Sparse-aperture moving-target RF reconstruction."
    isar = r'''
\vspace{0.8mm}
\noindent \textbf{Sparse-aperture moving-target RF reconstruction.}
Wen~\etal~extend NLOS radar from static reflectivity and localization to sparse-aperture ISAR imaging of moving targets~\cite{wenSparseApertureISARNLOS2024}. Static-clutter filtering isolates useful echoes, a detail-aware regularizer preserves target structure during ADMM reconstruction, and a learned fast variant reduces iterative cost. This branch links automotive/mmWave around-corner sensing to inverse-synthetic-aperture imaging, where target motion and sparse coherent apertures become part of the hidden-scene formation model.

'''
    rf_anchor = "Recent RF/mmWave work further expands the meaning of NLOS perception beyond monostatic reconstruction."
    s = insert_before(s, rf_anchor, isar, isar_marker, "new-scenes ISAR paragraph")
    save("article/5newscenes.tex", s)

def update_bare():
    s = load("bare_jrnl.tex")
    comment = "% 11 August 2026 RF/RIS synchronization: final IROS metadata, RIS vital-sign sensing, and pending learning/sparse-acquisition prose integrated.\n"
    if not s.startswith(comment): s = comment + s
    save("bare_jrnl.tex", s)

def update_note():
    note = r'''# 11 August 2026 — NLOS citation-trace and RF/RIS synchronization

A fresh keyword and forward-citation-oriented pass was run around the repository's core active, passive, learned, and modality-expansion seeds. The newest direct optical papers surfaced by the search (including geometry-constrained TVCG reconstruction, rough-wall thermal NLOS, diffuse-aware passive encoding, long-range/all-day SPAD systems, cost-effective FMCW interferometry, Neural Illumination Fields, physics-informed cascade learning, and recent sparse/irregular acquisition methods) were already present in the current repository corpus. No additional post-July-2026 direct NLOS-imaging record passed the relevance and metadata checks in this run.

The audit identified a cross-artifact gap in the RF/RIS branch and one venue correction:

1. **Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces** — Acta Electronica Sinica 53(1), 1–13 (2025), DOI `10.12263/DZXB.20240674`.
2. **Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring** — IEEE MTT-S IMBioC 2025, DOI `10.1109/IMBioC63524.2025.10989670`.
3. **mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera** — corrected from arXiv-only labeling to IEEE/RSJ IROS 2025, pp. 19661–19668, DOI `10.1109/IROS60139.2025.11246461`.

The two vital-sign papers are classified as **NLOS physiological/semantic sensing**, not hidden-shape imaging. The survey prose is also synchronized with previously catalogued records that lacked equivalent narrative integration: adaptive artifact cancellation, curvature regularization, TransDiff, adaptive spiral scanning, optimization-derived zero-shot attention, frequency-domain multi-regularization experts, and sparse-aperture ISAR NLOS imaging.

The bibliography merge consumes `egbib_20260811_ris_vitalsign_updates.bib` and the other dated supplements, so the final merged database uses verified conference/journal records rather than stale arXiv metadata. CI rebuilds `bare_jrnl.pdf` and validates source/bibliography/README/website/PDF consistency before the public merge.
'''
    save("updates/2026-08-11-ris-vitalsign-public-integration-patch.md", note)

def main():
    update_readme(); update_index(); update_active(); update_learning(); update_newscenes(); update_bare(); update_note()
    print("Applied bounded NLOS RF/RIS and survey synchronization.")

if __name__ == "__main__":
    main()
