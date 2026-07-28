from pathlib import Path
import re

TITLE = "Feasibility study of non-line-of-sight obstacle location estimation using reflected images from in-vehicle sensors"
DOI = "10.1016/j.iatssr.2026.02.007"
KEY = "shengVehicleReflectionObstacle2026"
KOZAWA_TITLE = "Estimating the 3D Position of Hidden Humans Using Reflections on Vehicle Bodies"


def main() -> None:
    readme_path = Path("README.md")
    readme = readme_path.read_text(encoding="utf-8")
    assert TITLE not in readme and DOI not in readme, "README already contains the paper"
    lines = readme.splitlines(keepends=True)
    row_idx = next(i for i, line in enumerate(lines) if line.startswith("| 2026 |") and KOZAWA_TITLE in line)
    lines.insert(
        row_idx + 1,
        "| 2026 | [Feasibility study of non-line-of-sight obstacle location estimation using reflected images from in-vehicle sensors]"
        "(https://doi.org/10.1016/j.iatssr.2026.02.007) — Sheng, Takatori | IATSS Research 2026 | "
        "Uses stereo observations of virtual obstacle images reflected by adjacent vehicle bodies, estimates the virtual-image position, and geometrically folds it across the reflective surface to recover the hidden obstacle location. Real-world reflection-frequency observations and 1/6-scale experiments report 4.3 cm mean localization error at 1.7–3.7 m; this is passive/specular NLOS localization rather than hidden-scene reconstruction. |\n",
    )
    timeline_idx = next(
        i
        for i, line in enumerate(lines)
        if line.lstrip().startswith("│     Kozawa et al.:") and "vehicle" in line.lower()
    )
    lines.insert(
        timeline_idx + 1,
        "   │     Sheng and Takatori: stereo vehicle-body reflections provide feasibility-validated passive NLOS obstacle localization for intelligent transportation [IATSS Research]\n",
    )
    readme_path.write_text("".join(lines), encoding="utf-8")

    index_path = Path("index.html")
    index = index_path.read_text(encoding="utf-8")
    assert TITLE not in index and DOI not in index, "website already contains the paper"
    lines = index.splitlines(keepends=True)
    object_idx = next(i for i, line in enumerate(lines) if KOZAWA_TITLE in line and "{cat:" in line)
    lines.insert(
        object_idx + 1,
        '      {cat:"latest passive localization specular automotive",title:"Feasibility study of non-line-of-sight obstacle location estimation using reflected images from in-vehicle sensors",authors:"Sheng and Takatori",year:2026,venue:"IATSS Research 2026",url:"https://doi.org/10.1016/j.iatssr.2026.02.007",key:"Stereo observations of vehicle-body reflections recover a virtual-image position and fold it across the estimated reflective surface to localize hidden road obstacles. Real-world reflection-frequency observations and 1/6-scale experiments report 4.3 cm mean error; this is passive/specular localization rather than hidden-scene reconstruction."},\n',
    )
    index = "".join(lines)
    pattern = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)',
        re.S,
    )
    match = pattern.search(index)
    assert match, "website 2026 timeline block is missing"
    sentence = (
        " Sheng and Takatori further showed that stereo observations of reflections on adjacent vehicles can localize NLOS road obstacles by estimating and geometrically unfolding their virtual images, expanding passive specular NLOS toward traffic safety."
    )
    index = index[: match.start(2)] + match.group(2) + sentence + index[match.end(2) :]
    count = len(re.findall(r'\{cat:"', index))
    index, substitutions = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        index,
        count=1,
    )
    assert substitutions == 1, "website tracked-entry counter was not updated"
    index_path.write_text(index, encoding="utf-8")

    passive_path = Path("article/3passive.tex")
    passive = passive_path.read_text(encoding="utf-8")
    assert KEY not in passive, "passive survey already cites the paper"
    anchor = "The output is task-oriented passive NLOS localization rather than a complete hidden image or surface reconstruction."
    assert anchor in passive, "passive survey anchor is missing"
    paragraph = r"""

\vspace{0.8mm}
\noindent \textbf{Stereo vehicle-reflection obstacle localization.}
Sheng and Takatori studied whether reflections already present on adjacent vehicles can act as opportunistic NLOS sensors for an ego vehicle~\cite{shengVehicleReflectionObstacle2026}. A stereo camera estimates the three-dimensional position of a virtual obstacle image and then geometrically folds that estimate across the reflective surface to recover the hidden obstacle location. Real-world observation and microscopic traffic simulation quantify how often usable reflections occur, while $1/6$-scale experiments report a mean error of 4.3~cm for targets 1.7--3.7~m ahead and an approximately 45~mm RMS error under reflective-surface orientation changes. This feasibility study complements reflection-based hidden-pedestrian localization by explicitly analyzing traffic availability and scale, but its output remains obstacle position rather than hidden appearance or complete geometry.
"""
    passive_path.write_text(passive.replace(anchor, anchor + paragraph, 1), encoding="utf-8")

    supplement = Path("egbib_20260728_vehicle_reflection_obstacle.bib")
    assert not supplement.exists(), "dated bibliography supplement already exists"
    supplement.write_text(
        r"""@article{shengVehicleReflectionObstacle2026,
  author = {Sheng, Baili and Takatori, Yusuke},
  title = {Feasibility Study of Non-Line-of-Sight Obstacle Location Estimation Using Reflected Images from In-Vehicle Sensors},
  journal = {IATSS Research},
  volume = {50},
  number = {1},
  pages = {777--785},
  year = {2026},
  month = {April},
  publisher = {Elsevier},
  doi = {10.1016/j.iatssr.2026.02.007},
  url = {https://doi.org/10.1016/j.iatssr.2026.02.007}
}
""",
        encoding="utf-8",
    )

    tex_path = Path("bare_jrnl.tex")
    tex = tex_path.read_text(encoding="utf-8")
    marker = "% 28 July 2026 citation/keyword trace: stereo vehicle-reflection NLOS obstacle localization synchronized."
    assert marker not in tex, "survey marker already exists"
    assert "%% bare_jrnl.tex" in tex, "survey marker anchor is missing"
    tex_path.write_text(tex.replace("%% bare_jrnl.tex", "%% bare_jrnl.tex\n" + marker, 1), encoding="utf-8")

    Path("updates/2026-07-28-vehicle-reflection-obstacle-localization.md").write_text(
        """# Vehicle-reflection NLOS obstacle localization — 28 July 2026

Integrated the DOI-verified IATSS Research paper **Feasibility study of non-line-of-sight obstacle location estimation using reflected images from in-vehicle sensors** (Baili Sheng and Yusuke Takatori, 2026, DOI `10.1016/j.iatssr.2026.02.007`).

The paper is tightly adjacent passive/specular NLOS sensing rather than an incidental transportation citation. A stereo in-vehicle camera observes virtual obstacle images reflected by adjacent vehicles, estimates the virtual-image position, and geometrically folds it across the reflective surface to recover the hidden obstacle location. Real-world observation and traffic simulation analyze reflection availability; 1/6-scale experiments report 4.3 cm mean error for targets at 1.7–3.7 m and approximately 45 mm RMS error under surface-angle changes.

Updated README, website explorer and 2026 timeline, passive survey prose, dated and consolidated BibTeX, survey trace marker, and rebuilt PDF. The work is categorized as localization rather than hidden-scene reconstruction.
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
