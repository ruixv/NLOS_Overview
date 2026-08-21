#!/usr/bin/env python3
'''Integrate verified radar/acoustic NLOS gaps found on 22 August 2026.'''
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CORRIDOR_TITLE = "A dual-branch fusion network for footstep sound source localization in non-line-of-sight corridors"
CORRIDOR_KEY = "wangCorridorLocNet2026"
DART_TITLE = "Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation"
DART_KEY = "kimDartingOutNLOS2025"
REFLECT_TITLE = "Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization"
REFLECT_KEY = "parkReflectionAwareNLOS2026"
MULTI_KEY = "jeonTJunctionMmWaveNLOS2025"

def require_once(text, needle, label):
    n = text.count(needle)
    if n != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {n}")

def insert_latest_row(text, title, row):
    if title in text:
        return text
    anchor = "|------|-------|----------------|----------------|\n"
    require_once(text, anchor, "Latest Additions separator")
    return text.replace(anchor, anchor + row, 1)

def insert_after_unique_line(text, marker, addition, label):
    if addition.strip() in text:
        return text
    lines = text.splitlines(keepends=True)
    idx = [i for i, line in enumerate(lines) if marker in line]
    if len(idx) != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {len(idx)}")
    lines.insert(idx[0] + 1, addition)
    return "".join(lines)

def insert_paper_record(text, title, record):
    if f'title:"{title}"' in text:
        return text
    anchor = "    const papers=[\n"
    require_once(text, anchor, "paper array")
    return text.replace(anchor, anchor + record, 1)

def append_timeline_sentence(text, year, sentence, marker):
    if marker in text:
        return text
    pat = re.compile(
        rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">'
        r'<strong>.*?</strong><p>)(.*?)(</p>)', re.DOTALL)
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"Could not locate website timeline year {year}")
    return text[:m.start(2)] + m.group(2) + sentence + text[m.end(2):]

def update_readme():
    p = ROOT / "README.md"
    t = p.read_text(encoding="utf-8")
    rows = [
        (CORRIDOR_TITLE,
         "| 2026 | [A dual-branch fusion network for footstep sound source localization in non-line-of-sight corridors](https://doi.org/10.1121/10.0044386) — Wang, Chen, Yin | The Journal of the Acoustical Society of America 160(2), 1400–1412 (2026) | CorridorLocNet fuses Mel-spectrogram and GCC-PHAT cues with residual-CNN and lightweight-Conformer branches plus cross-attention, learning multipath-dependent footstep position directly from a real around-corner corridor dataset; it reports 98.83% classification accuracy and 2.56 m lower average error than the compared reflection-aware localization baseline. |\n"),
        (REFLECT_TITLE,
         "| 2026 | [Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization](https://bingurrr.github.io/reflection-aware-nlos/) — Park, Jeon, Kim | ECCV 2026 (accepted; project page available before proceedings metadata) | Extends automotive mmWave NLOS localization to a moving ego-vehicle: camera/radar cross-attention predicts reflection type and reflective-surface structure in BEV, then physics-guided ray tracing unfolds distorted multipath. The real outdoor benchmark contains 120 scenarios / 12,539 frames and reports 1.23 m localization accuracy. |\n"),
        (DART_TITLE,
         "| 2025 | [Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation](https://doi.org/10.1109/IROS60139.2025.11246930) — Kim et al. | IEEE/RSJ IROS 2025, 21352–21359 | Uses monocular vehicle segmentation/depth to infer temporary parked-vehicle occluders, refines that geometry with 2D mmWave radar points, and then interprets reflected/diffracted returns to localize pedestrians before they emerge into line of sight in measured urban driving experiments. |\n")
    ]
    for title, row in rows:
        t = insert_latest_row(t, title, row)

    t = insert_after_unique_line(
        t,
        "Park et al.: camera-derived T-junction geometry conditions mmWave multipath",
        "   │     Jeon et al.: static-point layout inference plus multipath ray tracing localizes multiple hidden pedestrians at real outdoor T-junctions [IEEE IV]\n"
        "   │     Kim et al.: camera-derived parked-vehicle geometry plus radar refinement handles temporary darting-out occluders in real urban NLOS driving [IEEE/RSJ IROS]\n",
        "Park T-junction timeline line")
    t = insert_after_unique_line(
        t,
        "Yu et al.: cross-regional NLOS localization moves the multipath-detection branch",
        "   │     Park et al.: reflection-aware camera/radar BEV fusion plus physics-guided ray tracing extends hidden-pedestrian localization to moving ego-vehicle scenarios [ECCV]\n",
        "2026 radar timeline line")
    t = insert_after_unique_line(
        t,
        "Zhai et al.: Biot–Tolstoy–Medwin edge diffraction supplies a physics-aware steering vector",
        "   │     Wang et al.: CorridorLocNet learns real around-corner footstep position from Mel/GCC-PHAT multipath cues with CNN–Conformer cross-attention [JASA]\n",
        "2026 acoustic timeline line")
    p.write_text(t, encoding="utf-8")

def update_website():
    p = ROOT / "data/papers-source.html"
    t = p.read_text(encoding="utf-8")
    records = [
        (CORRIDOR_TITLE,
         '      {cat:"latest modality acoustic passive localization learning corridor multipath footstep",title:"A dual-branch fusion network for footstep sound source localization in non-line-of-sight corridors",authors:"Wang, Chen, Yin",year:2026,venue:"JASA 160(2), 1400–1412 (2026)",url:"https://doi.org/10.1121/10.0044386",key:"CorridorLocNet fuses Mel-spectrogram and GCC-PHAT features through residual-CNN and lightweight-Conformer branches with cross-attention, learning hidden footstep position from a measured around-corner corridor dataset."},\n'),
        (REFLECT_TITLE,
         '      {cat:"latest modality radar rf mmwave automotive localization camera fusion reflection reasoning ray-tracing measured eccv",title:"Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization",authors:"Park, Jeon, Kim",year:2026,venue:"ECCV 2026 (accepted)",url:"https://bingurrr.github.io/reflection-aware-nlos/",key:"Camera/radar BEV fusion predicts reflection type and reflective-surface structure, after which physics-guided ray tracing unfolds multipath for hidden pedestrian localization with a moving ego-vehicle; validated on 120 real scenarios."},\n'),
        (DART_TITLE,
         '      {cat:"latest modality radar rf mmwave automotive localization camera fusion darting-out parked-vehicle measured",title:"Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation",authors:"Kim et al.",year:2025,venue:"IEEE/RSJ IROS 2025, 21352–21359",url:"https://doi.org/10.1109/IROS60139.2025.11246930",key:"Monocular segmentation/depth estimates temporary parked-vehicle occluders, radar points refine that geometry, and reflected/diffracted mmWave returns localize pedestrians before they emerge into direct view in real urban driving experiments."},\n')
    ]
    for title, rec in records:
        t = insert_paper_record(t, title, rec)

    t = append_timeline_sentence(
        t, 2025,
        " Automotive mmWave NLOS localization also became more deployment-oriented: Jeon et al. ray-traced multipath for multiple hidden pedestrians at real T-junctions, Park et al. conditioned radar on camera-extracted road layout, and Kim et al. inferred temporary parked-vehicle occluders for darting-out scenarios.",
        "temporary parked-vehicle occluders for darting-out scenarios")
    t = append_timeline_sentence(
        t, 2026,
        " Reflection-aware camera/radar reasoning then extended this automotive branch to moving ego-vehicles at ECCV, while CorridorLocNet learned around-corner footstep localization directly from multipath acoustic features in a real corridor.",
        "CorridorLocNet learned around-corner footstep localization")
    actual = t.count("{cat:")
    t, n = re.subn(r'<b>\d+</b><span>tracked latest entries</span>',
                   f'<b>{actual}</b><span>tracked latest entries</span>', t, count=1)
    if n != 1:
        raise RuntimeError("website tracked-entry count anchor not found")
    p.write_text(t, encoding="utf-8")

def update_survey():
    p = ROOT / "article/5newscenes.tex"
    t = p.read_text(encoding="utf-8")
    old = (
        "Park~\\etal~use camera-derived road layout to interpret mmWave radar point clouds "
        "for NLOS pedestrian localization at urban T-junctions, connecting around-corner "
        "radar perception to autonomous-driving scene understanding~\\cite{parkTjunctionPedestrian2025}.")
    if REFLECT_KEY not in t or DART_KEY not in t or MULTI_KEY not in t:
        require_once(t, old, "Park T-junction survey sentence")
        new = (
            "Jeon~\\etal~first infer T-junction layout from static 2D mmWave points and ray-trace dynamic multipath returns to localize multiple hidden pedestrians in measured outdoor experiments~\\cite{jeonTJunctionMmWaveNLOS2025}. "
            "Park~\\etal~then use camera-derived road layout to interpret multipath-distorted mmWave point clouds for NLOS pedestrian localization at urban T-junctions~\\cite{parkTjunctionPedestrian2025}. "
            "Kim~\\etal~address a less stationary darting-out regime in which parked vehicles form temporary occluders: monocular segmentation and depth estimate the current vehicle geometry, 2D radar points refine that geometry, and the resulting spatial interpretation supports early hidden-pedestrian localization in real urban driving experiments~\\cite{kimDartingOutNLOS2025}. "
            "Park~\\etal~subsequently move the same automotive NLOS branch into ego-dynamic driving with reflection-aware reasoning~\\cite{parkReflectionAwareNLOS2026}. Their camera--radar BEV fusion predicts reflection-type labels and reflective-surface structure before physics-guided ray tracing unfolds distorted multipath; the project reports 120 real outdoor scenarios, 12,539 frames, and 1.23-m localization accuracy with a moving ego-vehicle. "
            "Together, these works trace a progression from map/layout-assisted single-target localization to multi-target ray tracing, temporary-obstacle reasoning, and learned reflection-aware multipath interpretation under vehicle motion.")
        t = t.replace(old, new, 1)

    if CORRIDOR_KEY not in t:
        anchor = (
            "Together, these systems extend the acoustic trajectory beyond relay-wall tomography "
            "toward passive tracking and diffraction-aware source localization in practical occluded environments.")
        require_once(t, anchor, "acoustic localization paragraph")
        addition = (
            anchor +
            "\n\nWang~\\etal~take a complementary data-driven route with CorridorLocNet~\\cite{wangCorridorLocNet2026}. "
            "Instead of requiring an explicit room or edge model, the network concatenates Mel-spectrogram and GCC-PHAT observations, extracts local time--frequency structure with a residual convolutional branch and long-range temporal dependencies with a lightweight Conformer branch, and uses cross-attention to regress the hidden footstep position. "
            "A real dataset captured with footsteps behind a corridor corner yields 98.83\\% classification accuracy and a 2.56-m reduction in average localization error relative to the compared reflection-aware method. "
            "This result complements physics-explicit diffraction localization by showing that complex corridor multipath can also serve as a learned spatial fingerprint for passive acoustic NLOS sensing.")
        t = t.replace(anchor, addition, 1)
    p.write_text(t, encoding="utf-8")

    main = ROOT / "bare_jrnl.tex"
    mt = main.read_text(encoding="utf-8")
    marker = "% 22 August 2026 radar/acoustic trace: ego-dynamic reflection-aware automotive NLOS localization, darting-out radar-camera sensing, and CorridorLocNet synchronized; existing IV 2025 multi-target radar work integrated into survey prose.\n"
    if marker not in mt:
        main.write_text(marker + mt, encoding="utf-8")

def append_bib():
    p = ROOT / "egbib_merged_20260711.bib"
    t = p.read_text(encoding="utf-8")
    entries = [
        (CORRIDOR_KEY, "10.1121/10.0044386", '''@article{wangCorridorLocNet2026,
  author = {Wang, Xiaonan and Chen, Zhe and Yin, Fuliang},
  doi = {10.1121/10.0044386},
  journal = {The Journal of the Acoustical Society of America},
  number = {2},
  pages = {1400--1412},
  title = {A Dual-Branch Fusion Network for Footstep Sound Source Localization in Non-Line-of-Sight Corridors},
  url = {https://doi.org/10.1121/10.0044386},
  volume = {160},
  year = {2026}
}'''),
        (DART_KEY, "10.1109/IROS60139.2025.11246930", '''@inproceedings{kimDartingOutNLOS2025,
  author = {Kim, Hee-Yeun and Park, Byeonggyu and Choi, Byonghyok and Cho, Hansang and Kim, Byungkwan and Lee, Soomok and Jeon, Mingu and Seo, Seung-Woo and Kim, Seong-Woo},
  booktitle = {2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  doi = {10.1109/IROS60139.2025.11246930},
  pages = {21352--21359},
  publisher = {IEEE},
  title = {Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation},
  url = {https://doi.org/10.1109/IROS60139.2025.11246930},
  year = {2025}
}'''),
        (REFLECT_KEY, "", '''@inproceedings{parkReflectionAwareNLOS2026,
  author = {Park, Byeonggyu and Jeon, Mingu and Kim, Seong-Woo},
  booktitle = {European Conference on Computer Vision (ECCV)},
  note = {Accepted at ECCV 2026; proceedings DOI/pages were not yet public at the 22 August 2026 update},
  title = {Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization},
  url = {https://bingurrr.github.io/reflection-aware-nlos/},
  year = {2026}
}''')
    ]
    for key, doi, entry in entries:
        if re.search(rf'@\w+\{{{re.escape(key)},', t):
            continue
        if doi and doi.lower() in t.lower():
            raise RuntimeError(f"DOI {doi} already exists under another key")
        t = t.rstrip() + "\n\n" + entry + "\n"
    p.write_text(t, encoding="utf-8")

def write_note():
    p = ROOT / "updates/2026-08-22-radar-acoustic-nlos-citation-trace.md"
    p.write_text('''# Radar/acoustic NLOS citation-trace update — 22 August 2026

This run combined recent publisher/project/lab-page searches with forward-citation and lineage tracing from the repository's established optical, radar, and acoustic NLOS milestones. Three high-confidence missing works were verified:

1. Xiaonan Wang, Zhe Chen, and Fuliang Yin, **A dual-branch fusion network for footstep sound source localization in non-line-of-sight corridors**, *The Journal of the Acoustical Society of America* 160(2), 1400–1412 (2026), DOI `10.1121/10.0044386`. CorridorLocNet fuses Mel-spectrogram and GCC-PHAT features with residual-CNN and lightweight-Conformer branches plus cross-attention, using a real around-corner footstep dataset.
2. Hee-Yeun Kim et al., **Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation**, *IEEE/RSJ IROS 2025*, 21352–21359, DOI `10.1109/IROS60139.2025.11246930`. The final conference record supersedes the arXiv-only version.
3. Byeonggyu Park, Mingu Jeon, and Seong-Woo Kim, **Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization**, accepted to *ECCV 2026*. The project page and independent lab publication lists verify acceptance; proceedings DOI/pages were not yet public, so the repository uses the accepted final venue plus project page without fabricating missing metadata.

The audit also found a cross-artifact consistency gap for Jeon et al., **Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar**, *IEEE IV 2025*, DOI `10.1109/IV64158.2025.11097630`: it was already present in the canonical website corpus and merged bibliography, but not in the radar survey prose. This integration closes that gap.

The automotive radar narrative is now: measured multi-target T-junction ray tracing → camera-conditioned road-layout interpretation → temporary parked-vehicle/darting-out geometry → reflection-aware ego-dynamic multimodal reasoning. The acoustic narrative is extended from physics-explicit edge diffraction and passive vehicle tracking to learned corridor-multipath spatial fingerprints.

The guarded workflow rebuilds `bare_jrnl.pdf`, checks the new citations in `.aux/.bbl`, validates README / `data/papers-source.html` / survey / bibliography consistency, and renders relevant PDF pages before the public changes are committed.
''', encoding="utf-8")

def validate_source():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    site = (ROOT / "data/papers-source.html").read_text(encoding="utf-8")
    survey = (ROOT / "article/5newscenes.tex").read_text(encoding="utf-8")
    bib = (ROOT / "egbib_merged_20260711.bib").read_text(encoding="utf-8")
    for title in (CORRIDOR_TITLE, DART_TITLE, REFLECT_TITLE):
        if readme.count(title) < 1:
            raise RuntimeError(f"README missing {title}")
        if site.count(f'title:"{title}"') != 1:
            raise RuntimeError(f"website should contain exactly one {title}")
    for key in (CORRIDOR_KEY, DART_KEY, REFLECT_KEY, MULTI_KEY):
        if key not in survey:
            raise RuntimeError(f"survey missing {key}")
        if bib.count("{" + key + ",") != 1:
            raise RuntimeError(f"bib should contain exactly one {key}")
    actual = site.count("{cat:")
    m = re.search(r'<b>(\d+)</b><span>tracked latest entries</span>', site)
    if not m or int(m.group(1)) != actual:
        raise RuntimeError(f"website count mismatch: badge={m.group(1) if m else None}, actual={actual}")
    if "Updated 22 August 2026" not in site:
        raise RuntimeError("website date not 22 August 2026")

def main():
    update_readme()
    update_website()
    update_survey()
    append_bib()
    write_note()
    validate_source()
    print("Integrated radar/acoustic NLOS citation-trace gaps.")

if __name__ == "__main__":
    main()
