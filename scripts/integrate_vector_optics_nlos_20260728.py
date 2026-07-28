#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article/2active.tex"
BARE = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates/2026-07-28-vector-optics-nlos-lineage.md"

DOIS = [
    "10.1515/nanoph-2023-0655",
    "10.1002/lpor.202300909",
    "10.1016/j.eng.2024.11.013",
]
KEYS = [
    "zhaoLCPlanarNLOS2024",
    "wangVectorialMultiviewNLOS2024",
    "guoVectorialDigitelligentNLOS2025",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def require_once(text: str, needle: str, label: str) -> None:
    count = text.count(needle)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label}; found {count}: {needle[:100]!r}")


def insert_after(text: str, anchor: str, addition: str, label: str) -> str:
    require_once(text, anchor, label)
    return text.replace(anchor, anchor + addition, 1)


# Fail closed if any record is already partly integrated.
for path in (README, INDEX, ACTIVE, BARE, BIB):
    content = read(path)
    for doi in DOIS:
        if doi in content:
            raise RuntimeError(f"Refusing partial/duplicate integration: {doi} already appears in {path}")

# README: paper table and development timeline.
readme = read(README)
header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
rows = (
    "| 2025 | [Vectorial Digitelligent Optics for High-Resolution Non-Line-of-Sight Imaging](https://doi.org/10.1016/j.eng.2024.11.013) — Guo et al. | Engineering 45, 70–78 (2025) | Jointly optimizes wavefront and polarization through a scattering relay wall, raster-scans the resulting focus within the optical-memory-effect range, and reaches 0.40 mm resolution at 0.35 m with strongly enhanced echo SNR; a physical-illumination route complementary to transient inverse operators. |\n"
    "| 2024 | [Vectorial-Optics-Enabled Multi-View Non-Line-of-Sight Imaging with High Signal-to-Noise Ratio](https://doi.org/10.1002/lpor.202300909) — Wang et al. | Laser & Photonics Reviews 18(6), 2300909 (2024) | Derives a vector-optical-field relay-reflection model to select illumination angle, incident polarization, and received polarization, enabling polarization-aware multi-view hidden-object reconstruction and recognition at low SNR. |\n"
    "| 2024 | [High-resolution non-line-of-sight imaging based on liquid crystal planar optical elements](https://doi.org/10.1515/nanoph-2023-0655) — Zhao et al. | Nanophotonics 13(12), 2161–2172 (2024) | Uses a liquid-crystal planar angle-magnification element to enlarge the effective relay scan aperture for higher-resolution transient NLOS, while correlation-aware sparse scanning reduces acquisition time by more than 20% without sacrificing the demonstrated resolution. |\n"
)
readme = insert_after(readme, header, rows, "README latest-additions table header")
anchor_2024 = "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
add_2024 = (
    "   │     Zhao et al.: liquid-crystal planar angle magnification enlarges the relay aperture while correlation-aware sparse scanning cuts acquisition time [Nanophotonics]\n"
    "   │     Wang et al.: vector-optical-field modeling turns illumination angle and polarization into multi-view, low-SNR NLOS measurement degrees of freedom [Laser & Photonics Reviews]\n"
)
readme = insert_after(readme, anchor_2024, add_2024, "README 2024 timeline anchor")
anchor_2025 = "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics move steady-state NLOS toward inexpensive white-light and ambient-light operation [Applied Optics / Optics Communications]\n"
add_2025 = "     │     Guo et al.: vectorial digitelligent optics jointly optimizes phase and polarization to refocus through a rough relay wall and attain near-diffraction-limited 0.40-mm NLOS imaging [Engineering]\n"
readme = insert_after(readme, anchor_2025, add_2025, "README 2025 timeline anchor")
write(README, readme)

# Website: explorer records, count, and timeline narrative.
index = read(INDEX)
require_once(index, '<b>232</b><span>tracked latest entries</span>', "website paper count")
index = index.replace('<b>232</b><span>tracked latest entries</span>', '<b>235</b><span>tracked latest entries</span>', 1)
objects_anchor = "    const papers=[\n"
objects = (
    '      {cat:"latest active high-resolution wavefront-shaping polarization meta-optics",title:"Vectorial Digitelligent Optics for High-Resolution Non-Line-of-Sight Imaging",authors:"Guo et al.",year:2025,venue:"Engineering 2025",url:"https://doi.org/10.1016/j.eng.2024.11.013",key:"Joint feedback optimization of phase and polarization refocuses light through a rough relay wall; memory-effect raster scanning reaches 0.40 mm resolution at 0.35 m and supports ToF-resolved hidden 3D structure with substantially enhanced echo SNR."},\n'
    '      {cat:"latest active high-resolution polarization multi-view vector-optics",title:"Vectorial-Optics-Enabled Multi-View Non-Line-of-Sight Imaging with High Signal-to-Noise Ratio",authors:"Wang et al.",year:2024,venue:"Laser & Photonics Reviews 2024",url:"https://doi.org/10.1002/lpor.202300909",key:"A generalized vector-optical-field reflection model selects illumination view and transmit/receive polarization, improving low-SNR echo strength and enabling multi-view hidden-object reconstruction and recognition."},\n'
    '      {cat:"latest active high-resolution transient planar-optics liquid-crystal sparse-scanning",title:"High-resolution non-line-of-sight imaging based on liquid crystal planar optical elements",authors:"Zhao et al.",year:2024,venue:"Nanophotonics 2024",url:"https://doi.org/10.1515/nanoph-2023-0655",key:"A liquid-crystal planar angle magnifier expands the effective relay-wall scan aperture for high-resolution transient reconstruction, while measurement-correlation-aware sparse scanning reduces acquisition time by more than 20 percent without demonstrated resolution loss."},\n'
)
index = insert_after(index, objects_anchor, objects, "website papers-array anchor")

def append_timeline_sentence(html: str, year: str, sentence: str) -> str:
    pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(pattern, html, flags=re.S)
    if not match:
        raise RuntimeError(f"Missing website timeline block for {year}")
    if sentence in match.group(2):
        raise RuntimeError(f"Timeline sentence already present for {year}")
    replacement = match.group(1) + match.group(2) + " " + sentence + match.group(3)
    return html[:match.start()] + replacement + html[match.end():]

index = append_timeline_sentence(
    index,
    "2024",
    "Liquid-crystal planar angle magnification enlarged the effective transient scan aperture while preserving resolution under correlation-aware sparse sampling, and vector-optical-field modeling converted illumination angle plus transmit/receive polarization into complementary multi-view measurements with higher echo SNR.",
)
index = append_timeline_sentence(
    index,
    "2025",
    "Vectorial digitelligent optics then closed the loop between vector-wavefront control and hidden-target sensing, jointly optimizing phase and polarization through the relay wall to attain near-diffraction-limited 0.40-mm reconstruction at 0.35 m.",
)
write(INDEX, index)

# Survey prose and active-system table.
active = read(ACTIVE)
table_anchor = "    \\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,roueinfarNIRRaster2025,liuPolarizationDifferentialCorrelography2025} & Continuous laser & Conventional camera & Intensity &  3D reconstruction\\\\%%%% Table body\n"
table_row = "    \\cite{zhaoLCPlanarNLOS2024,wangVectorialMultiviewNLOS2024,guoVectorialDigitelligentNLOS2025} & Shaped pulsed / continuous laser & SPAD / camera & ToF, intensity, and polarization & High-resolution 2D/3D reconstruction\\\\%%%% Table body\n"
active = insert_after(active, table_anchor, table_row, "active-system table anchor")
focus_anchor = "At a target distance of 0.55\\,m, UNCOVER achieves a spatial resolution of $\\sim0.6\\,\\text{mm}$, demonstrating the potential of active-optics-based NLOS imaging for millimeter-scale resolution.\n"
focus_paragraph = (
    "\n\\vspace{0.8mm}\n"
    "\\noindent \\textbf{From planar aperture expansion to vectorial digitelligent focusing.}\n"
    "A complementary high-resolution lineage modifies the physical illumination and relay aperture before reconstruction. Zhao~\\etal~inserted a liquid-crystal planar angle-magnification element into a transient NLOS system, enlarging the effective relay-wall scan aperture while using measurement correlation for sparse sampling that reduced acquisition time by more than 20\\% without sacrificing the demonstrated resolution~\\cite{zhaoLCPlanarNLOS2024}. Wang~\\etal~then formulated a vector-optical-field reflection model that selects illumination angle, incident polarization, and received polarization, converting polarization diversity into multi-view measurements with stronger echoes for hidden-object reconstruction and recognition under low SNR~\\cite{wangVectorialMultiviewNLOS2024}. Guo~\\etal~closed the loop with vectorial digitelligent optics: feedback jointly optimizes phase and polarization to refocus through a random scattering wall, after which the focus is raster-scanned within the optical-memory-effect range~\\cite{guoVectorialDigitelligentNLOS2025}. Their measured 0.40\\,mm resolution at 0.35\\,m approaches the diffraction limit, and the retained photon timing also supports axial separation. Together, these papers shift part of the NLOS inverse problem into optical co-design---aperture magnification, polarization-aware view selection, and closed-loop vector wavefront control---rather than relying only on a more powerful LCT, $f$--$k$, or phasor-field back end.\n"
)
active = insert_after(active, focus_anchor, focus_paragraph, "active-focusing prose anchor")
write(ACTIVE, active)

# Main source trace marker.
bare = read(BARE)
marker_anchor = "%% bare_jrnl.tex\n"
marker = "% 28 July 2026 citation trace: liquid-crystal planar optics, vectorial multi-view sensing, and digitelligent wavefront/polarization focusing synchronized.\n"
bare = insert_after(bare, marker_anchor, marker, "bare_jrnl header")
write(BARE, bare)

# DOI-verified bibliography records.
bib = read(BIB).rstrip() + "\n\n"
bib += r'''@article{zhaoLCPlanarNLOS2024,
  author    = {Zhao, Zhibin and Zhang, Qi and Li, Xiaoyin and Guo, Yinghui and Pu, Mingbo and Zhang, Fei and Guo, Hengshuo and Wang, Zewei and Fan, Yulong and Xu, Mingfeng and Luo, Xiangang},
  title     = {High-Resolution Non-Line-of-Sight Imaging Based on Liquid Crystal Planar Optical Elements},
  journal   = {Nanophotonics},
  year      = {2024},
  volume    = {13},
  number    = {12},
  pages     = {2161--2172},
  publisher = {De Gruyter},
  doi       = {10.1515/nanoph-2023-0655},
  url       = {https://doi.org/10.1515/nanoph-2023-0655},
  note      = {Published online 10 January 2024}
}

@article{wangVectorialMultiviewNLOS2024,
  author    = {Wang, Zewei and Li, Xiaoyin and Pu, Mingbo and Chen, Lianwei and Zhang, Fei and Zhang, Qi and Zhao, Zhibin and Yang, Longfei and Guo, Yinghui and Luo, Xiangang},
  title     = {Vectorial-Optics-Enabled Multi-View Non-Line-of-Sight Imaging with High Signal-to-Noise Ratio},
  journal   = {Laser \& Photonics Reviews},
  year      = {2024},
  volume    = {18},
  number    = {6},
  pages     = {2300909},
  publisher = {Wiley},
  doi       = {10.1002/lpor.202300909},
  url       = {https://doi.org/10.1002/lpor.202300909},
  note      = {Published online 15 February 2024}
}

@article{guoVectorialDigitelligentNLOS2025,
  author    = {Guo, Yinghui and Lei, Yunsong and Pu, Mingbo and Zhang, Fei and Zhang, Qi and Li, Xiaoyin and Zhang, Runzhe and Zhao, Zhibin and Zhou, Rui and Fan, Yulong and Luo, Xiangang},
  title     = {Vectorial Digitelligent Optics for High-Resolution Non-Line-of-Sight Imaging},
  journal   = {Engineering},
  year      = {2025},
  volume    = {45},
  pages     = {70--78},
  publisher = {Elsevier},
  doi       = {10.1016/j.eng.2024.11.013},
  url       = {https://doi.org/10.1016/j.eng.2024.11.013},
  note      = {Published online 23 December 2024; final paginated issue February 2025}
}
'''
write(BIB, bib)

note = """# Vector/planar-optics NLOS citation-tracing update — 28 July 2026

This guarded update integrates three direct active-NLOS papers missing from the README, website explorer/timeline, survey prose/table, and consolidated bibliography.

## Added lineage

1. **Zhao et al., Nanophotonics 2024** — liquid-crystal planar angle magnification enlarges the effective transient relay aperture; correlation-aware sparse scanning reduces acquisition time by more than 20% without demonstrated resolution loss. DOI: `10.1515/nanoph-2023-0655`.
2. **Wang et al., Laser & Photonics Reviews 2024** — a vector-optical-field reflection model jointly selects illumination view and transmit/receive polarization for higher-SNR multi-view reconstruction and recognition. DOI: `10.1002/lpor.202300909`.
3. **Guo et al., Engineering 2025** — feedback-controlled vectorial digitelligent optics jointly optimizes phase and polarization through a rough relay wall, reaching 0.40 mm resolution at 0.35 m. DOI: `10.1016/j.eng.2024.11.013`.

The papers were surfaced by tracing the active-focusing, LCT, phasor-field, and computational-periscopy citation neighborhood and were retained only after confirming direct hidden-scene reconstruction experiments. The Engineering record uses Elsevier/ScienceDirect and DOAJ final pagination, **45:70–78**; a secondary journal mirror currently displays 76–84, so that conflicting mirror pagination was not used.

## Semantic placement

- `README.md`: Latest Additions plus 2024/2025 development milestones.
- `index.html`: searchable Active Optical entries, timeline narrative, and tracked-entry count 232 → 235.
- `article/2active.tex`: active-system table and the high-resolution active-focusing discussion, immediately after UNCOVER.
- `egbib_merged_20260711.bib`: DOI-verified final journal records.
- `bare_jrnl.tex`: synchronization marker.
- `bare_jrnl.pdf`: rebuilt only after citation and cross-artifact checks pass.
"""
write(NOTE, note)

# Cross-artifact assertions before the build.
for doi in DOIS:
    for path in (README, INDEX, BIB):
        if read(path).count(doi) != 1:
            raise RuntimeError(f"Expected one {doi} in {path}")
for key in KEYS:
    if read(ACTIVE).count(key) != 2:  # table + prose
        raise RuntimeError(f"Expected table and prose citations for {key}")
    if read(BIB).count("{" + key + ",") != 1:
        raise RuntimeError(f"Expected one BibTeX record for {key}")
if read(INDEX).count("{cat:") != 235:
    raise RuntimeError(f"Website explorer count mismatch: {read(INDEX).count('{cat:')} objects")
print("Vector/planar-optics NLOS lineage integrated and validated at source level.")
