#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

LI_TITLE = "Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces"
TRIP_TITLE = "Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring"
PARK_TITLE = "mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera"
ROUEINFAR_TITLE = "Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def insert_after_once(text, anchor, addition, label):
    if addition.strip() in text:
        return text
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(anchor, anchor + addition, 1)


def update_readme():
    path = "README.md"
    text = read(path)

    latest_anchor = "|------|-------|----------------|----------------|\n"
    latest_rows = (
        f"| 2025 | [{LI_TITLE}](https://doi.org/10.12263/DZXB.20240674) — Li et al. | Acta Electronica Sinica 53(1), 1–13 (2025) | Uses visual-aided programmable RIS beam control to redirect RF sensing energy into a hidden human region, then estimates respiration and heartbeat with an improved VMD pipeline. This is physiological NLOS sensing rather than hidden-shape reconstruction. |\n"
        f"| 2025 | [{TRIP_TITLE}](https://doi.org/10.1109/IMBioC63524.2025.10989670) — Tripathy et al. | IEEE IMBioC 2025 | Integrates a liquid-crystal RIS with a self-injection-locked radar, electronically steering the sensing path into an NLOS region for experimentally validated contactless vital-sign monitoring. |\n"
        f"| 2025 | [{ROUEINFAR_TITLE}](https://doi.org/10.1109/ICEE67339.2025.11213924) — Roueinfar and Salmanian | IEEE ICEE 2025, 1175–1179 | A low-cost steady-state active-NLOS baseline using a 500 mW 808 nm laser, pan–tilt relay-wall raster scanning, and an NIR camera; the final IEEE record supersedes the later arXiv copy. |\n"
    )
    # Add only rows whose titles are not already explicit in the Latest Additions block.
    latest_start = text.index("## Latest Additions")
    latest_end = text.find("\n## ", latest_start + 5)
    latest_block = text[latest_start: latest_end if latest_end != -1 else len(text)]
    rows_to_add = []
    for title, row in [(LI_TITLE, latest_rows.splitlines(True)[0]), (TRIP_TITLE, latest_rows.splitlines(True)[1]), (ROUEINFAR_TITLE, latest_rows.splitlines(True)[2])]:
        if title not in latest_block:
            rows_to_add.append(row)
    if rows_to_add:
        if text.count(latest_anchor) < 1:
            raise RuntimeError("README latest table separator not found")
        text = text.replace(latest_anchor, latest_anchor + "".join(rows_to_add), 1)

    # Correct Park from arXiv-only labeling to the verified IROS 2025 final record.
    lines = text.splitlines(True)
    park_seen = 0
    for i, line in enumerate(lines):
        if PARK_TITLE in line:
            park_seen += 1
            line = line.replace("https://arxiv.org/abs/2508.02348", "https://doi.org/10.1109/IROS60139.2025.11246461")
            line = re.sub(r"\| arXiv 2025 \|", "| IEEE/RSJ IROS 2025, 19661–19668 |", line)
            lines[i] = line
    if park_seen == 0:
        raise RuntimeError("README Park paper not found for final-venue correction")
    text = "".join(lines)

    # Put the two newly public RIS vital-sign papers next to the existing dual-beam RIS row.
    category_marker = "<!-- 2026-08-11-ris-vitalsign-category -->"
    if category_marker not in text:
        lines = text.splitlines(True)
        idx = next((i for i, line in enumerate(lines) if "Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface" in line and line.lstrip().startswith("|")), None)
        if idx is None:
            raise RuntimeError("README dual-beam RIS row anchor not found")
        category_rows = (
            f"{category_marker}\n"
            f"| 2025 | [{LI_TITLE}](https://doi.org/10.12263/DZXB.20240674) — Li et al. | Acta Electronica Sinica 53(1), 1–13 (2025) | Programmable-RIS NLOS physiological sensing: vision guides metasurface beam control toward the hidden chest region, followed by respiration/heartbeat estimation. |\n"
            f"| 2025 | [{TRIP_TITLE}](https://doi.org/10.1109/IMBioC63524.2025.10989670) — Tripathy et al. | IEEE IMBioC 2025 | Liquid-crystal RIS plus self-injection-locked radar for experimentally validated hidden-region vital-sign monitoring. |\n"
        )
        lines.insert(idx + 1, category_rows)
        text = "".join(lines)

    timeline_marker = "Li et al.: programmable RIS beam control enables hidden-region respiration and heartbeat sensing"
    if timeline_marker not in text:
        lines = text.splitlines(True)
        idx = next((i for i, line in enumerate(lines) if "Yuan et al.: RIS-enabled covariance-domain gridless DoA" in line), None)
        if idx is None:
            raise RuntimeError("README 2025 RIS timeline anchor not found")
        addition = (
            "   │     Li et al.: programmable RIS beam control enables hidden-region respiration and heartbeat sensing [Acta Electronica Sinica]\n"
            "   │     Tripathy et al.: liquid-crystal RIS + SIL radar experimentally monitors NLOS vital signs [IEEE IMBioC]\n"
            "   │     Park et al.: camera-derived T-junction geometry conditions mmWave multipath for hidden-pedestrian localization [IEEE/RSJ IROS]\n"
        )
        lines.insert(idx + 1, addition)
        text = "".join(lines)

    write(path, text)


def update_index():
    path = "index.html"
    text = read(path)

    # Correct Park final venue and DOI wherever the paper object appears.
    park_pat = re.compile(r'\{cat:"([^"]*)",title:"' + re.escape(PARK_TITLE) + r'",authors:"Park et al\.",year:2025,venue:"[^"]*",url:"[^"]*",key:"([^"]*)"\},')
    m = park_pat.search(text)
    if not m:
        raise RuntimeError("index.html Park paper object not found")
    park_obj = '{cat:"' + m.group(1) + '",title:"' + PARK_TITLE + '",authors:"Park et al.",year:2025,venue:"IEEE/RSJ IROS 2025",url:"https://doi.org/10.1109/IROS60139.2025.11246461",key:"Uses camera-derived T-junction road geometry to interpret multipath-distorted mmWave point clouds and localize hidden pedestrians in real outdoor driving scenes."},'
    text = text[:m.start()] + park_obj + text[m.end():]

    dual_anchor = '      {cat:"latest modality",title:"Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface",authors:"Yasmeen et al.",year:2025,venue:"IEEE RadarConf25 2025",url:"https://doi.org/10.1109/RadarConf2559087.2025.11205052",key:"A practical 1-bit dual-beam RIS is compared with metal and ideal single-beam reflectors in simulations and measurements, widening hidden-region radar coverage and enabling simultaneous multi-direction sensing."},\n'
    if text.count(dual_anchor) != 1:
        raise RuntimeError(f"index dual-beam anchor count={text.count(dual_anchor)}")
    new_objs = ""
    if LI_TITLE not in text:
        new_objs += f'      {{cat:"latest modality rf ris sensing vital-sign",title:"{LI_TITLE}",authors:"Li et al.",year:2025,venue:"Acta Electronica Sinica 2025",url:"https://doi.org/10.12263/DZXB.20240674",key:"Visual-aided programmable RIS beam control redirects RF sensing into an NLOS human region; improved VMD estimates respiration and heartbeat. Physiological NLOS sensing, not hidden-shape reconstruction."}},\n'
    if TRIP_TITLE not in text:
        new_objs += f'      {{cat:"latest modality rf radar ris vital-sign",title:"{TRIP_TITLE}",authors:"Tripathy et al.",year:2025,venue:"IEEE IMBioC 2025",url:"https://doi.org/10.1109/IMBioC63524.2025.10989670",key:"A liquid-crystal RIS dynamically steers a self-injection-locked radar into hidden regions for experimentally validated contactless vital-sign monitoring."}},\n'
    if new_objs:
        text = text.replace(dual_anchor, dual_anchor + new_objs, 1)

    trajectory = " RF NLOS also moved from passively exploiting multipath to controlling propagation: programmable and liquid-crystal RISs redirected radar energy into hidden regions for around-corner coverage and physiological sensing, while camera-derived road geometry conditioned mmWave multipath for hidden-pedestrian localization at real T-junctions."
    if trajectory.strip() not in text:
        anchor = "Bayesian relay-angle inference and LiDAR-free reflector reconstruction made relay geometry an estimated part of the inverse problem."
        if text.count(anchor) != 1:
            raise RuntimeError(f"index 2025 timeline anchor count={text.count(anchor)}")
        text = text.replace(anchor, anchor + trajectory, 1)

    # Keep the public explorer count tied to actual paper objects rather than a manually incremented stale number.
    paper_count = len(re.findall(r'\{cat:"', text))
    text, n = re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>', f'<div class="stat"><b>{paper_count}</b><span>tracked latest entries</span></div>', text, count=1)
    if n != 1:
        raise RuntimeError("index tracked-latest stat not found")

    write(path, text)


def update_survey():
    path = "article/5newscenes.tex"
    text = read(path)

    old_park = "\\href{https://arxiv.org/abs/2508.02348}{Park~\\etal} use camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, connecting around-corner radar perception to autonomous-driving scene understanding."
    new_park = "Park~\\etal~use camera-derived road layout to interpret mmWave radar point clouds for NLOS pedestrian localization at urban T-junctions, connecting around-corner radar perception to autonomous-driving scene understanding~\\cite{parkTjunctionPedestrian2025}."
    if old_park in text:
        text = text.replace(old_park, new_park, 1)
    elif "parkTjunctionPedestrian2025" not in text:
        raise RuntimeError("survey Park arXiv sentence/citation not found")

    marker = "Reconfigurable propagation for physiological NLOS sensing"
    if marker not in text:
        anchor = "A follow-on dual-beam RIS radar study~\\cite{yasmeenDualBeamRIS2026} examines a lower-complexity one-bit quantized RIS configuration that produces dual symmetric beams, benchmarking the resulting beam steering and radar cross-section against metal reflectors and ideal single-beam RIS baselines."
        if text.count(anchor) != 1:
            raise RuntimeError(f"survey dual-beam anchor count={text.count(anchor)}")
        addition = (
            "\n\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Reconfigurable propagation for physiological NLOS sensing.}\n"
            "A complementary RF branch treats the relay path as a controllable component rather than a fixed environmental reflector. Li~\\etal~combine visual target localization with programmable RIS beam control so that the sensing field is redirected toward a hidden chest region, and then estimate respiration and heartbeat from the returned signal using an improved variational-mode-decomposition pipeline~\\cite{liRISVitalSignNLOS2025}. Tripathy~\\etal~integrate a liquid-crystal RIS with a self-injection-locked radar and experimentally demonstrate contactless vital-sign monitoring after electronically steering the sensing path into an NLOS region~\\cite{tripathyLCRISVitalSign2025}. These works extend NLOS RF from geometry, localization, and micro-Doppler toward physiological sensing; they should therefore be interpreted as hidden-region semantic/biomedical sensing rather than hidden-shape reconstruction.\n"
        )
        text = text.replace(anchor, anchor + addition, 1)

    write(path, text)

    tex_path = "bare_jrnl.tex"
    tex = read(tex_path)
    comment = "% 11 August 2026 RF/RIS citation trace: final IROS/RadarConf metadata and measured programmable/liquid-crystal RIS NLOS vital-sign sensing synchronized.\n"
    if not tex.startswith(comment):
        tex = comment + tex
    write(tex_path, tex)


def write_note():
    note = ROOT / "updates/2026-08-11-ris-nlos-synchronized.md"
    note.write_text("""# 11 August 2026 — RF/RIS NLOS public synchronization

This bounded synchronization follows a fresh keyword, venue, arXiv, project-page, and forward-citation-oriented pass around the repository's core NLOS papers. No additional recent direct NLOS-imaging paper survived the relevance and metadata checks beyond the already curated 2026 frontier. The actionable gap was a small RF/RIS branch plus two final-venue/cross-artifact corrections.

## Integrated / corrected

1. **Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces** — *Acta Electronica Sinica* 53(1), 1–13 (2025), DOI `10.12263/DZXB.20240674`. Added as physiological RF/RIS NLOS sensing, not geometric imaging.
2. **Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring** — IEEE IMBioC 2025, DOI `10.1109/IMBioC63524.2025.10989670`. Added as experimentally validated NLOS vital-sign sensing.
3. **Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface** — final IEEE RadarConf25 2025 record, DOI `10.1109/RadarConf2559087.2025.11205052`; the later arXiv copy remains auxiliary metadata only.
4. **mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera** — corrected from arXiv-only labeling to final IEEE/RSJ IROS 2025, DOI `10.1109/IROS60139.2025.11246461`.
5. **Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength** — the final IEEE ICEE 2025 record was already present in the website, survey source, and bibliography; this run adds an explicit README Latest Additions entry so the public artifacts no longer disagree.

The existing supplemental bibliography `egbib_20260811_ris_vitalsign_updates.bib` is the canonical source for the four RF/RIS records. The merge step regenerates `egbib_merged_20260711.bib` and normalizes the survey citations to those final records.

## Search decisions

The fresh pass also screened adjacent shadow/gesture semantic work and other 2026 NLOS-adjacent submissions. Items without a verified final venue or without a sufficiently direct NLOS sensing/reconstruction contribution were not promoted merely because they cite NLOS core papers.

## Synchronization target

The CI integration updates `README.md`, `index.html`, `article/5newscenes.tex`, `bare_jrnl.tex`, the merged BibTeX database, and the compiled `bare_jrnl.pdf`, then validates source/PDF consistency before committing the public artifacts.
""", encoding="utf-8")


def main():
    update_readme()
    update_index()
    update_survey()
    write_note()
    print("Applied bounded RF/RIS NLOS public synchronization.")


if __name__ == "__main__":
    main()
