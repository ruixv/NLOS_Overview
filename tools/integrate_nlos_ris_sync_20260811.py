#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def insert_before_once(text, anchor, block, label):
    if block.strip() in text:
        return text
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(anchor, block + anchor, 1)


def insert_after_line_matching(text, pattern, block, label):
    if block.strip() in text:
        return text
    matches = list(re.finditer(pattern, text, flags=re.M))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one matching line, found {len(matches)}")
    m = matches[0]
    return text[:m.end()] + "\n" + block.rstrip("\n") + text[m.end():]


def update_readme():
    text = read("README.md")

    # Correct Park et al. from the arXiv-only public record to its final IROS 2025 venue.
    old = "](https://arxiv.org/abs/2508.02348) — Park et al. | arXiv 2025 |"
    new = "](https://doi.org/10.1109/IROS60139.2025.11246461) — Park et al. | IEEE/RSJ IROS 2025, 19661–19668 |"
    if old in text:
        text = text.replace(old, new)
    elif "10.1109/IROS60139.2025.11246461" not in text:
        raise RuntimeError("README: Park final-venue record not found for correction")

    main_rows = (
        "| 2025 | [Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces](https://doi.org/10.12263/DZXB.20240674) — Li et al. | Acta Electronica Sinica 53(1), 1–13 (2025) | Uses visual target localization to program a reconfigurable intelligent surface so RF sensing energy is redirected into a hidden human region, then estimates respiration and heartbeat with an improved VMD pipeline. This is NLOS physiological sensing rather than hidden-shape reconstruction. |\n"
        "| 2025 | [Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring](https://doi.org/10.1109/IMBioC63524.2025.10989670) — Tripathy et al. | IEEE MTT-S IMBioC 2025 | Integrates a phase-reconfigurable liquid-crystal RIS with a self-injection-locked radar, electronically steering the sensing path into an NLOS region and experimentally demonstrating contactless vital-sign monitoring. |\n"
    )
    # Put the new physiological-sensing branch beside the already verified dual-beam RIS lineage.
    if text.count("Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces") < 1:
        text = insert_after_line_matching(
            text,
            r'^\| 2025 \| \[Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface\].*$',
            main_rows,
            "README RF/RIS main-list insertion",
        )

    latest_rows = (
        "| 2025 | [Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring](https://doi.org/10.1109/IMBioC63524.2025.10989670) — Tripathy et al. | IEEE MTT-S IMBioC 2025 | A liquid-crystal RIS and self-injection-locked radar actively redirect sensing energy into an occluded region for measured contactless respiration/heartbeat monitoring. |\n"
        "| 2025 | [Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces](https://doi.org/10.12263/DZXB.20240674) — Li et al. | Acta Electronica Sinica 53(1), 1–13 (2025) | Visually aided RIS coding redirects RF illumination toward a hidden subject; improved variational-mode decomposition recovers breathing and heartbeat, extending NLOS sensing from geometry/localization to physiological semantics. |\n"
    )
    if text.count("Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces") < 2:
        header = "|------|-------|----------------|----------------|\n"
        idx = text.find(header, text.find("## Latest Additions"))
        if idx < 0:
            raise RuntimeError("README Latest Additions table header not found")
        pos = idx + len(header)
        text = text[:pos] + latest_rows + text[pos:]

    # Add one concise trajectory marker in the milestone timeline.
    timeline_line = "   │     RIS-enabled RF sensing becomes actively reconfigurable: dual-beam and liquid-crystal surfaces steer energy into hidden regions for around-corner radar and physiological monitoring [IEEE RadarConf / IMBioC / Acta Electronica Sinica]\n"
    if timeline_line.strip() not in text:
        anchor = "2025 ── mmNorm: mmWave surface-normal estimation advances hidden RF sensing from localization to 3D object geometry [MobiSys]\n"
        if anchor not in text:
            raise RuntimeError("README 2025 RF timeline anchor not found")
        text = text.replace(anchor, anchor + timeline_line, 1)

    write("README.md", text)


def update_index():
    text = read("index.html")

    old_obj = '{cat:"latest modality",title:"mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera",authors:"Park et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2508.02348",key:"Camera-derived road layout helps interpret mmWave radar point clouds for NLOS pedestrian localization."}'
    new_obj = '{cat:"latest modality rf mmwave localization robotics camera-fusion",title:"mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera",authors:"Park et al.",year:2025,venue:"IEEE/RSJ IROS 2025, 19661–19668",url:"https://doi.org/10.1109/IROS60139.2025.11246461",key:"Camera-derived T-junction road geometry conditions multipath-distorted mmWave point clouds for hidden-pedestrian localization on a real vehicle; final IROS 2025 venue verified."}'
    if old_obj in text:
        text = text.replace(old_obj, new_obj, 1)
    elif "10.1109/IROS60139.2025.11246461" not in text:
        raise RuntimeError("index.html: Park object not found for final-venue correction")

    new_objects = (
        '      {cat:"latest modality rf radar ris vital-sign",title:"Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces",authors:"Li et al.",year:2025,venue:"Acta Electronica Sinica 53(1), 1–13 (2025)",url:"https://doi.org/10.12263/DZXB.20240674",key:"Visually aided RIS coding redirects RF sensing energy toward a hidden human target; improved VMD estimates respiration and heartbeat, making this physiological NLOS sensing rather than geometric reconstruction."},\n'
        '      {cat:"latest modality rf radar ris vital-sign",title:"Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring",authors:"Tripathy et al.",year:2025,venue:"IEEE MTT-S IMBioC 2025",url:"https://doi.org/10.1109/IMBioC63524.2025.10989670",key:"A phase-reconfigurable liquid-crystal RIS integrated with a self-injection-locked radar electronically steers the sensing path into an NLOS region for measured contactless vital-sign monitoring."},\n'
    )
    if "Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces" not in text:
        anchor = '      {cat:"latest modality",title:"Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface"'
        idx = text.find(anchor)
        if idx < 0:
            raise RuntimeError("index.html: dual-beam RIS object anchor not found")
        text = text[:idx] + new_objects + text[idx:]

    # Keep the displayed explorer count synchronized with the two new objects.
    text = text.replace('<div class="stat"><b>275</b><span>tracked latest entries</span></div>', '<div class="stat"><b>277</b><span>tracked latest entries</span></div>')

    # Extend the 2025 timeline with the reconfigurable-propagation branch.
    marker = "Programmable and liquid-crystal RISs additionally turned the relay path into a controllable component, steering RF sensing energy into hidden regions for around-corner radar and contactless vital-sign monitoring."
    if marker not in text:
        pattern = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
        m = pattern.search(text)
        if not m:
            raise RuntimeError("index.html: 2025 timeline block not found")
        repl = m.group(1) + m.group(2).rstrip() + " " + marker + m.group(3)
        text = text[:m.start()] + repl + text[m.end():]

    write("index.html", text)


def update_active_survey():
    text = read("article/2active.tex")
    block = r'''
\vspace{0.8mm}
\noindent \textbf{Measurement-adaptive regularization and transient completion.}
Recent active NLOS work revisits robustness and sparse acquisition without abandoning the physical forward operator. Zhou~\etal~construct a ground-truth-free TOF-SSIM criterion and adaptively modify transient histograms before backprojection, suppressing reconstruction artifacts in both confocal and non-confocal geometries~\cite{zhouAdaptiveArtifactCancellationNLOS2025}. Ding~\etal~stabilize under-sampled recovery with object-domain and joint signal--object-domain curvature regularization and GPU-oriented ADMM solvers~\cite{dingCurvatureRegularizationNLOS2024}. Cui~\etal~instead treat aperture-limited acquisition as a measurement-constrained latent-diffusion problem: TransDiff restores dense transient information without paired supervision before hidden-scene reconstruction~\cite{cuiTransDiffNLOS2025}. Oyama~\etal~move adaptation into acquisition itself, shifting an Archimedean spiral toward relay-wall regions with stronger sequential returns and compensating the resulting nonuniform density with Voronoi weights~\cite{oyamaAdaptiveSpiralNLOS2026}. Together, these methods make data quality, relay-aperture support, and sample placement explicit optimization variables rather than fixed assumptions inherited from dense rectangular scanning.

'''
    # Insert before the active-method challenges section; the exact bookmark wording varies only once.
    if "Measurement-adaptive regularization and transient completion" not in text:
        m = re.search(r'\\bookmark\[dest=\\HyperLocalCurrentHref,level=2\]\{Challenges', text)
        if not m:
            raise RuntimeError("article/2active.tex: challenges anchor not found")
        text = text[:m.start()] + block + text[m.start():]
    write("article/2active.tex", text)


def update_learning_survey():
    text = read("article/4datadriven.tex")
    block = r'''
\vspace{0.8mm}
\noindent \textbf{Optimization-derived attention and frequency-domain expert fusion.}
A parallel physics-guided trajectory derives adaptive network-like weighting directly from optimization variables instead of learning every gate from paired data. Zhang~\etal~model non-Gaussian NLOS residuals with a mixture distribution and obtain dual-space adaptive weights that act as zero-shot attention inside an alternating solver~\cite{zhangAdaptiveMixtureAttentionNLOS2025}. Their later frequency-domain multi-regularization-experts formulation partitions the inverse problem across complementary regularized Wiener-style experts and fuses them with gates derived from dual variables~\cite{zhangFrequencyMoENLOS2026}. These methods complement CMFormer, NLOST, and transient Transformers by showing that attention and mixture-of-experts behavior can emerge from the inverse model itself, retaining interpretability and avoiding a fully supervised gating network.

'''
    anchor = r"\vspace{0.8mm}" + "\n" + r"\noindent \textbf{Dual-model guidance for under-scanned transients.}"
    text = insert_before_once(text, anchor, block, "article/4datadriven optimization-derived paragraph")
    write("article/4datadriven.tex", text)


def update_new_scenes_survey():
    text = read("article/5newscenes.tex")

    sparse_block = r'''
\vspace{0.8mm}
\noindent \textbf{Adaptive sparse acquisition beyond fixed relay grids.}
The sparse-acquisition branch now spans both prior design and measurement design. Curvature regularization supplies higher-order geometric priors when relay samples are severely under-sampled~\cite{dingCurvatureRegularizationNLOS2024}; TransDiff recovers missing aperture information through an unsupervised measurement-consistent diffusion prior~\cite{cuiTransDiffNLOS2025}; and adaptive spiral scanning reallocates confocal measurements online toward high-return wall regions while correcting nonuniform sampling density~\cite{oyamaAdaptiveSpiralNLOS2026}. This progression moves sparse NLOS from merely tolerating missing measurements toward choosing where measurements should be made and learning how incomplete apertures should be completed.

'''
    anchor = r"\vspace{0.8mm}" + "\n" + r"\noindent \textbf{Masked transient pretraining.}"
    text = insert_before_once(text, anchor, sparse_block, "article/5 sparse-acquisition paragraph")

    ris_sentences = (
        " The same controllable-propagation idea is now being used for physiological NLOS sensing rather than only angle, location, or micro-Doppler recovery. Li~\\etal~use visual target localization to program a reconfigurable intelligent surface so RF energy is redirected toward a hidden subject, then estimate respiration and heartbeat with an improved variational-mode-decomposition pipeline~\\cite{liRISVitalSignNLOS2025}. Tripathy~\\etal~integrate a liquid-crystal RIS with a self-injection-locked radar; phase-controlled wavefront steering places the sensing beam in an occluded region and measured experiments demonstrate contactless vital-sign monitoring~\\cite{tripathyLCRISVitalSign2025}. These studies should be interpreted as semantic/physiological NLOS sensing, not hidden-shape reconstruction."
    needle = "A follow-on dual-beam RIS radar study~\\cite{yasmeenDualBeamRIS2026} examines a lower-complexity one-bit quantized RIS configuration that produces dual symmetric beams, benchmarking the resulting beam steering and radar cross-section against metal reflectors and ideal single-beam RIS baselines."
    if ris_sentences.strip() not in text:
        if text.count(needle) != 1:
            raise RuntimeError("article/5: dual-beam RIS sentence anchor not found")
        text = text.replace(needle, needle + ris_sentences, 1)

    # Replace the Park arXiv hyperlink with the final IROS citation.
    old_park = r"\href{https://arxiv.org/abs/2508.02348}{Park~\etal} use camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, connecting around-corner radar perception to autonomous-driving scene understanding."
    new_park = r"Park~\etal~use camera-derived road layout to interpret multipath-distorted mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, with a real-vehicle outdoor evaluation reported in the final IROS publication~\cite{parkTjunctionPedestrian2025}."
    if old_park in text:
        text = text.replace(old_park, new_park, 1)
    elif "parkTjunctionPedestrian2025" not in text:
        raise RuntimeError("article/5: Park arXiv prose not found for final-venue correction")

    isar_block = r'''
\vspace{0.8mm}
\noindent \textbf{Sparse-aperture moving-target RF reconstruction.}
Wen~\etal~extend NLOS radar from static reflectivity and localization to sparse-aperture ISAR imaging of moving targets~\cite{wenSparseApertureISARNLOS2024}. Static-clutter filtering isolates useful echoes, a detail-aware regularizer preserves target structure during ADMM reconstruction, and a learned fast variant reduces iterative cost. This branch links automotive/mmWave around-corner sensing to inverse-synthetic-aperture imaging, where target motion and sparse coherent apertures become part of the hidden-scene formation model.

'''
    marker = "Recent RF/mmWave work further expands the meaning of NLOS perception beyond monostatic reconstruction."
    if "Sparse-aperture moving-target RF reconstruction" not in text:
        if text.count(marker) != 1:
            raise RuntimeError("article/5: RF expansion anchor not found")
        text = text.replace(marker, isar_block + marker, 1)

    write("article/5newscenes.tex", text)


def update_bare():
    text = read("bare_jrnl.tex")
    comment = "% 11 August 2026 RF/RIS synchronization: final IROS metadata, RIS vital-sign sensing, and pending learning/sparse-acquisition prose integrated.\n"
    if not text.startswith(comment):
        text = comment + text
    write("bare_jrnl.tex", text)


def write_update_note():
    note = r'''# 11 August 2026 — NLOS citation-trace and RF/RIS synchronization

A fresh keyword and forward-citation-oriented pass was run around the repository's core active, passive, learned, and modality-expansion seeds. The newest direct optical papers surfaced by the search (including geometry-constrained TVCG reconstruction, rough-wall thermal NLOS, diffuse-aware passive encoding, long-range/all-day SPAD systems, cost-effective FMCW interferometry, Neural Illumination Fields, physics-informed cascade learning, and recent sparse/irregular acquisition methods) were already present in the current repository corpus. No additional post-July-2026 direct NLOS-imaging record passed the relevance and metadata checks in this run.

The audit did identify a real cross-artifact gap in the RF/RIS branch and one venue correction:

1. **Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces** — Acta Electronica Sinica 53(1), 1–13 (2025), DOI `10.12263/DZXB.20240674`. Visual target localization programs an RIS to redirect RF sensing energy into a hidden region; improved VMD estimates respiration and heartbeat.
2. **Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring** — 2025 IEEE MTT-S IMBioC, DOI `10.1109/IMBioC63524.2025.10989670`. A liquid-crystal RIS and self-injection-locked radar electronically steer the sensing path into an occluded region for measured contactless vital-sign monitoring.
3. **mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera** — corrected from the repository's arXiv-only public label to the final IEEE/RSJ IROS 2025 record, pp. 19661–19668, DOI `10.1109/IROS60139.2025.11246461`.

The two vital-sign papers are deliberately classified as **NLOS physiological/semantic sensing**, not hidden-shape imaging.

The survey prose is also synchronized with previously added records that had public README/website entries or update metadata but lacked equivalent narrative integration: adaptive artifact cancellation, curvature regularization, TransDiff, adaptive spiral scanning, optimization-derived zero-shot attention, frequency-domain multi-regularization experts, and sparse-aperture ISAR NLOS imaging. Existing CMFormer, SG-ATV, thermal NLOS, Neural Illumination Fields, diffuse-aware passive encoding, FMCW, long-range/all-day, and other recent records were confirmed already integrated in the survey source.

The bibliography merge step consumes `egbib_20260811_ris_vitalsign_updates.bib` and the other dated supplements, so the final merged database uses the verified conference/journal records rather than stale arXiv metadata. The CI workflow rebuilds `bare_jrnl.pdf` with BibTeX and checks the new DOI/title strings in the source, bibliography, homepage, README, and extracted PDF text before committing the synchronized artifacts.
'''
    write("updates/2026-08-11-ris-vitalsign-public-integration-patch.md", note)


def main():
    update_readme()
    update_index()
    update_active_survey()
    update_learning_survey()
    update_new_scenes_survey()
    update_bare()
    write_update_note()
    print("Applied bounded NLOS RF/RIS and survey consistency synchronization.")


if __name__ == "__main__":
    main()
