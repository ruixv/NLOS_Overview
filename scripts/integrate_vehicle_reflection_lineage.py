from pathlib import Path
import re

PAPERS = [
    {
        "key": "takatoriReflectedImageNLOS2020",
        "title": "NLOS Obstacle Position Estimation from Reflected Image",
        "year": 2020,
        "venue": "IEEE IV 2020",
        "url": "https://doi.org/10.1109/IV47402.2020.9304553",
        "authors": "Takatori",
        "summary": "Uses stereo observations of virtual road-obstacle images reflected by nearby vehicle bodies or roadside glass and geometrically unfolds the reflection to estimate hidden-obstacle position; a 1/5-scale study establishes the foundational automotive passive/specular NLOS localization formulation.",
    },
    {
        "key": "nakamuraTransparentReflectionNLOS2022",
        "title": "Estimation of NLOS Obstacle Position Using Reflected Image on Transparent Surface",
        "year": 2022,
        "venue": "IEEE ITSC 2022",
        "url": "https://ieeexplore.ieee.org/document/9922107/",
        "authors": "Nakamura, Takatori",
        "summary": "Extends stereo reflected-image NLOS localization to transparent relay surfaces, addressing parallax, incidence angle, and polarization-filter effects; this remains task-oriented obstacle localization rather than hidden-scene reconstruction.",
    },
    {
        "key": "oyamaPaintedReflectionDetection2025",
        "title": "Object Detection Method for Non-Line-of-Sight Obstacles Reflected on Painted Surfaces",
        "year": 2025,
        "venue": "IEEE ITSC 2025",
        "url": "https://doi.org/10.1109/ITSC60802.2025.11423754",
        "authors": "Oyama, Takatori",
        "summary": "Moves the automotive reflection lineage from geometric localization to semantic detection on weak, colour-distorted painted-surface reflections; direct-view normalization followed by a general pretrained detector reports 85.7% overall accuracy.",
    },
    {
        "key": "shengVehicleReflectionObstacle2026",
        "title": "Feasibility study of non-line-of-sight obstacle location estimation using reflected images from in-vehicle sensors",
        "year": 2026,
        "venue": "IATSS Research 2026",
        "url": "https://doi.org/10.1016/j.iatssr.2026.02.007",
        "authors": "Sheng, Takatori",
        "summary": "Combines real-road reflection-frequency observations, microscopic traffic simulation, reflective-surface-angle modeling, and stereo virtual-image unfolding; 1/6-scale experiments report 4.3 cm mean error at 1.7–3.7 m and approximately 45 mm RMS error under reflector-orientation changes.",
    },
]

KOZAWA_TITLE = "Estimating the 3D Position of Hidden Humans Using Reflections on Vehicle Bodies"


def insert_after_year(lines: list[str], year: int, text: str) -> None:
    anchor = f"{year} ──"
    idx = next(i for i, line in enumerate(lines) if line.startswith(anchor))
    lines.insert(idx + 1, text)


def main() -> None:
    readme_path = Path("README.md")
    readme = readme_path.read_text(encoding="utf-8")
    for paper in PAPERS:
        assert paper["title"] not in readme, f"README already contains {paper['title']}"
    lines = readme.splitlines(keepends=True)
    row_idx = next(i for i, line in enumerate(lines) if line.startswith("| 2026 |") and KOZAWA_TITLE in line)
    rows = [
        f"| {p['year']} | [{p['title']}]({p['url']}) — {p['authors']} | {p['venue']} | {p['summary']} |\n"
        for p in PAPERS
    ]
    for offset, row in enumerate(rows, start=1):
        lines.insert(row_idx + offset, row)
    insert_after_year(lines, 2020, "   │     Takatori: stereo virtual-image geometry establishes reflected-obstacle NLOS localization for intelligent vehicles [IEEE IV]\n")
    insert_after_year(lines, 2022, "   │     Nakamura and Takatori: transparent reflective surfaces extend automotive virtual-image localization with parallax and polarization considerations [IEEE ITSC]\n")
    insert_after_year(lines, 2025, "   │     Oyama and Takatori: painted-surface reflections support semantic NLOS obstacle detection after reflection-aware appearance normalization [IEEE ITSC]\n")
    kozawa_timeline = next(i for i, line in enumerate(lines) if line.lstrip().startswith("│     Kozawa et al.:") and "vehicle" in line.lower())
    lines.insert(kozawa_timeline + 1, "   │     Sheng and Takatori: real-road availability analysis and scale/angle experiments validate stereo vehicle-reflection obstacle localization [IATSS Research]\n")
    readme_path.write_text("".join(lines), encoding="utf-8")

    index_path = Path("index.html")
    index = index_path.read_text(encoding="utf-8")
    for paper in PAPERS:
        assert paper["title"] not in index, f"website already contains {paper['title']}"
    lines = index.splitlines(keepends=True)
    object_idx = next(i for i, line in enumerate(lines) if KOZAWA_TITLE in line and "{cat:" in line)
    objects = [
        '      {cat:"latest passive specular automotive reflection stereo localization recognition",'
        f'title:"{p["title"]}",authors:"{p["authors"]}",year:{p["year"]},venue:"{p["venue"]}",url:"{p["url"]}",key:"{p["summary"]}"}},\n'
        for p in PAPERS
    ]
    for offset, obj in enumerate(objects, start=1):
        lines.insert(object_idx + offset, obj)
    index = "".join(lines)
    timeline_sentences = {
        2020: " Takatori introduced stereo virtual-image unfolding for automotive NLOS obstacle localization from reflections on neighboring vehicles or roadside glass.",
        2022: " Nakamura and Takatori extended reflected-image localization to transparent surfaces, analyzing parallax, incidence angle, and polarization filtering.",
        2025: " Oyama and Takatori moved the reflected-image branch toward semantic obstacle detection on painted surfaces using reflection-aware training and appearance normalization.",
        2026: " Sheng and Takatori quantified reflection availability in real traffic and validated stereo virtual-image unfolding across scale and reflector-orientation changes.",
    }
    for year, sentence in timeline_sentences.items():
        pattern = re.compile(rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
        match = pattern.search(index)
        assert match, f"website {year} timeline block missing"
        index = index[: match.start(2)] + match.group(2) + sentence + index[match.end(2) :]
    count = len(re.findall(r'\{cat:"', index))
    index, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        index,
        count=1,
    )
    assert n == 1
    index_path.write_text(index, encoding="utf-8")

    passive_path = Path("article/3passive.tex")
    passive = passive_path.read_text(encoding="utf-8")
    for paper in PAPERS:
        assert paper["key"] not in passive, f"survey already cites {paper['key']}"
    anchor = "The output is task-oriented passive NLOS localization rather than a complete hidden image or surface reconstruction."
    assert anchor in passive
    paragraph = r"""

\vspace{0.8mm}
\noindent \textbf{Vehicle-body reflections as opportunistic automotive NLOS sensors.}
Takatori first used stereo observations of virtual obstacle images reflected by neighboring vehicles or roadside glass to geometrically recover hidden road-obstacle positions~\cite{takatoriReflectedImageNLOS2020}. Nakamura and Takatori extended the formulation to transparent relay surfaces, analyzing stereo parallax, incidence angle, and polarization filtering~\cite{nakamuraTransparentReflectionNLOS2022}. Oyama and Takatori subsequently moved from localization toward semantic detection on weak and color-distorted painted-surface reflections, combining pseudo-reflection augmentation with direct-view normalization and pretrained object detectors~\cite{oyamaPaintedReflectionDetection2025}. Sheng and Takatori then evaluated reflection availability in real traffic and microscopic simulation and validated stereo virtual-image unfolding across reflector orientations~\cite{shengVehicleReflectionObstacle2026}. Together, these studies establish an application-facing passive/specular NLOS branch for intelligent transportation; their outputs are obstacle position or identity rather than hidden appearance or complete geometry.
"""
    passive_path.write_text(passive.replace(anchor, anchor + paragraph, 1), encoding="utf-8")

    lineage_bib = Path("egbib_20260728_vehicle_reflection_lineage.bib")
    merged_path = Path("egbib_merged_20260711.bib")
    assert lineage_bib.exists()
    merged = merged_path.read_text(encoding="utf-8")
    for paper in PAPERS:
        assert paper["key"] not in merged, f"merged bibliography already has {paper['key']}"
    merged_path.write_text(merged.rstrip() + "\n\n" + lineage_bib.read_text(encoding="utf-8").strip() + "\n", encoding="utf-8")

    tex_path = Path("bare_jrnl.tex")
    tex = tex_path.read_text(encoding="utf-8")
    marker = "% 28 July 2026 citation trace: automotive reflected-image passive NLOS lineage synchronized."
    assert marker not in tex
    assert "%% bare_jrnl.tex" in tex
    tex_path.write_text(tex.replace("%% bare_jrnl.tex", "%% bare_jrnl.tex\n" + marker, 1), encoding="utf-8")

    note_path = Path("updates/2026-07-28-vehicle-reflection-nlos-lineage.md")
    note = note_path.read_text(encoding="utf-8")
    current = "The DOI-verified bibliography supplement and this precise integration note are committed. The repository also contains a previously staged single-paper integration workflow for the 2026 IATSS paper, but no subsequent source/PDF integration commit was visible at the end of this run. Therefore README, index.html, the consolidated bibliography, survey source, and `bare_jrnl.pdf` are **not claimed as synchronized yet**. Large public files were not overwritten from a stale or partial snapshot."
    replacement = "README, the website explorer and timeline, passive-survey prose, and the consolidated bibliography are now synchronized for all four records. The PDF is rebuilt and validated by the guarded workflow before the final integration commit is made."
    if current in note:
        note = note.replace(current, replacement)
    note_path.write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
