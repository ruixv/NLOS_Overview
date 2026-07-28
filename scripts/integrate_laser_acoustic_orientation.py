from pathlib import Path
import re

TITLE = "Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments"
DOI = "10.1038/s41598-026-52682-6"
KEY = "doganLaserAcousticOrientationNLOS2026"
URL = f"https://doi.org/{DOI}"

README_ROW = (
    f"| 2026 | [{TITLE}]({URL}) — Doğan | Scientific Reports 2026 | "
    "Fuses 21 laser-chirp and 21 acoustic-chirp features into a 42-feature representation and evaluates conventional classifiers, LAO-Net, and explainable-AI analysis for four hidden-person orientations in controlled NLOS experiments. This is multimodal semantic NLOS sensing, not hidden-image or 3D-geometry reconstruction. |\n"
)

WEBSITE_OBJECT = (
    '      {cat:"latest modality acoustic laser fusion learning recognition orientation",'
    f'title:"{TITLE}",authors:"Doğan",year:2026,venue:"Scientific Reports 2026",url:"{URL}",'
    'key:"Fuses 21 laser-chirp and 21 acoustic-chirp features into a 42-feature representation and uses machine-learning baselines, LAO-Net, and explainable-AI analysis to classify four hidden-person orientations in controlled NLOS experiments; semantic orientation sensing rather than image or geometry reconstruction."},\n'
)

SURVEY_ANCHOR = (
    "This relay-free setting shows that edge diffraction, rather than diffuse reflection alone, "
    "can be treated as an exploitable physical transport path for hidden-scene sensing."
)

SURVEY_PARAGRAPH = r"""

\vspace{0.8mm}
\noindent \textbf{Laser--acoustic fusion for hidden-human orientation sensing.}
Do{\u{g}}an combined laser and acoustic chirp measurements at the feature level for four-class hidden-person orientation recognition~\cite{doganLaserAcousticOrientationNLOS2026}. Each sensing channel contributes 21 engineered features, yielding a 42-dimensional fused representation evaluated with classical classifiers, the proposed LAO-Net, and explainable-AI analysis under controlled NLOS experiments. This work extends acoustic NLOS from source localization and geometric reconstruction toward multimodal semantic inference; its output is an orientation class rather than a hidden image, position map, or 3D surface.
"""


def update_readme() -> None:
    path = Path("README.md")
    text = path.read_text(encoding="utf-8")
    assert TITLE not in text and DOI not in text, "README already contains this record"
    table_anchor = "|------|-------|----------------|----------------|\n"
    assert table_anchor in text, "README Latest Additions table anchor missing"
    text = text.replace(table_anchor, table_anchor + README_ROW, 1)

    lines = text.splitlines(keepends=True)
    year_index = next(i for i, line in enumerate(lines) if line.startswith("2026 ──"))
    timeline_line = (
        "   │     Doğan: laser–acoustic early fusion and LAO-Net extend hidden-human NLOS sensing "
        "from localization/reconstruction toward four-class orientation inference [Scientific Reports]\n"
    )
    lines.insert(year_index + 1, timeline_line)
    path.write_text("".join(lines), encoding="utf-8")


def update_website() -> None:
    path = Path("index.html")
    text = path.read_text(encoding="utf-8")
    assert TITLE not in text and DOI not in text, "website already contains this record"

    lines = text.splitlines(keepends=True)
    object_index = next(i for i, line in enumerate(lines) if '{cat:"' in line)
    lines.insert(object_index, WEBSITE_OBJECT)
    text = "".join(lines)

    pattern = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)',
        re.S,
    )
    match = pattern.search(text)
    assert match, "website 2026 timeline block missing"
    sentence = (
        " Doğan added laser–acoustic early fusion and LAO-Net for four-class hidden-human "
        "orientation sensing, extending acoustic NLOS toward multimodal semantic inference."
    )
    text = text[: match.start(2)] + match.group(2) + sentence + text[match.end(2) :]

    count = len(re.findall(r'\{cat:"', text))
    text, replacements = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    assert replacements == 1, "website tracked-entry counter missing"
    path.write_text(text, encoding="utf-8")


def update_survey_section() -> None:
    path = Path("article/5newscenes.tex")
    text = path.read_text(encoding="utf-8")
    assert KEY not in text and TITLE not in text, "survey section already contains this record"
    assert SURVEY_ANCHOR in text, "acoustic-section insertion anchor missing"
    path.write_text(text.replace(SURVEY_ANCHOR, SURVEY_ANCHOR + SURVEY_PARAGRAPH, 1), encoding="utf-8")


def update_bibliography() -> None:
    supplement = Path("egbib_20260728_laser_acoustic_orientation.bib")
    merged_path = Path("egbib_merged_20260711.bib")
    assert supplement.exists(), "canonical bibliography supplement missing"
    merged = merged_path.read_text(encoding="utf-8")
    assert KEY not in merged and DOI not in merged, "merged bibliography already contains this record"
    merged_path.write_text(
        merged.rstrip() + "\n\n" + supplement.read_text(encoding="utf-8").strip() + "\n",
        encoding="utf-8",
    )


def update_main_tex() -> None:
    path = Path("bare_jrnl.tex")
    text = path.read_text(encoding="utf-8")
    marker = "% 28 July 2026 modality trace: laser--acoustic hidden-human orientation sensing synchronized."
    assert marker not in text, "main survey marker already present"
    assert "%% bare_jrnl.tex" in text, "main survey header anchor missing"
    path.write_text(text.replace("%% bare_jrnl.tex", "%% bare_jrnl.tex\n" + marker, 1), encoding="utf-8")


def update_note() -> None:
    path = Path("updates/2026-07-28-laser-acoustic-orientation.md")
    text = path.read_text(encoding="utf-8")
    status = (
        "\n## Integration status\n\n"
        "README, website explorer/timeline, acoustic-survey prose, and the consolidated bibliography "
        "were synchronized by the guarded workflow. The workflow commits these sources together with "
        "the regenerated survey PDF only after the citation resolves and all validation checks pass.\n"
    )
    assert "## Integration status" not in text
    path.write_text(text.rstrip() + "\n" + status, encoding="utf-8")


def main() -> None:
    update_readme()
    update_website()
    update_survey_section()
    update_bibliography()
    update_main_tex()
    update_note()


if __name__ == "__main__":
    main()
