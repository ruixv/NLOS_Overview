#!/usr/bin/env python3
"""Synchronize verified passive recognition and NLOS understanding papers."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "QSS-Net: A Quanta-State-Slot Network for Non-line-of-Sight Classification",
        "authors": "Lin et al.",
        "year": 2026,
        "venue": "FLINS-ISKE / Springer LNCS 2026",
        "url": "https://doi.org/10.1007/978-981-92-2487-6_3",
        "cat": "latest learning recognition",
        "key": "linQSSNetNLOS2026",
        "summary": "Formalizes a recognition-oriented NLOS direction with a Quanta-State-Slot network, shifting the target from complete hidden 3D recovery toward efficient semantic classification for time-sensitive perception.",
    },
    {
        "title": "Multi-view clustering for non-line-of-sight imaging with neighborhood consistency reweighting",
        "authors": "Lin et al.",
        "year": 2026,
        "venue": "Neurocomputing 2026",
        "url": "https://doi.org/10.1016/j.neucom.2026.133462",
        "cat": "latest learning recognition",
        "key": "linNCRMultiViewNLOS2026",
        "summary": "Refines photon-corrupted neighborhood graphs across multiple NLOS reconstructions using shared-neighbor consistency, Huber-smoothed dual consistency gates, and adaptive view weighting, with closed-form alternating updates and convergence guarantees.",
    },
    {
        "title": "Adaptive motion enhancement for passive non-line-of-sight action recognition",
        "authors": "Sun et al.",
        "year": 2025,
        "venue": "Neurocomputing 2025",
        "url": "https://doi.org/10.1016/j.neucom.2025.131372",
        "cat": "latest passive recognition",
        "key": "sunAdaptiveMotionNLOS2025",
        "summary": "Introduces AME-Net for recognizing hidden human actions from ordinary RGB videos of a visible relay wall and releases NLOS-Action, the first passive NLOS action-recognition dataset, with 2,000 synthetic and more than 500 real sequences.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def append_to_timeline_year(text: str, year: int, sentence: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if f'<div class="year">{year}</div>' in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    if sentence.strip() not in lines[matches[0]]:
        closing = "</p></div></div>"
        if closing not in lines[matches[0]]:
            raise RuntimeError(f"Timeline closing marker missing for {year}")
        lines[matches[0]] = lines[matches[0]].replace(closing, " " + sentence.strip() + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = ""
    for paper in PAPERS:
        if f"[{paper['title']}]" not in text:
            rows += (
                f"| {paper['year']} | [{paper['title']}]({paper['url']}) - {paper['authors']} | "
                f"{paper['venue']} | {paper['summary']} |\n"
            )
    if rows:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + rows, "README latest-additions header")

    audit_anchor = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
    audit_lines = (
        "   |     Sun et al.: ordinary RGB relay-wall video enables passive hidden-action recognition and the NLOS-Action benchmark [Neurocomputing]\n"
        "   |     Lin et al.: neighborhood-consistency reweighting extends NLOS understanding to robust multi-view clustering [Neurocomputing]\n"
        "   |     QSS-Net: recognition-oriented quanta-state-slot modeling advances efficient NLOS semantic classification [FLINS-ISKE / Springer LNCS]\n"
        "   |     18 July 2026 recognition and clustering citation trace: semantic NLOS records integrated into the survey and bibliography\n"
    )
    if "18 July 2026 recognition and clustering citation trace" not in text:
        text = replace_once(text, audit_anchor, audit_lines + audit_anchor, "README core-citation audit marker")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    additions = [paper_object(p) for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if additions:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + "\n".join(additions) + "\n", "homepage paper array")

    stat_pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    match = stat_pattern.search(text)
    if not match:
        raise RuntimeError("Homepage tracked-entry statistic not found")
    expected = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    current = int(match.group(2))
    if current != expected:
        text = stat_pattern.sub(lambda m: m.group(1) + str(expected) + m.group(3), text, count=1)

    text = append_to_timeline_year(
        text,
        2025,
        "AME-Net and NLOS-Action moved ordinary-camera passive sensing from hidden-image recovery toward robust hidden-action recognition from subtle relay-wall motion.",
    )
    text = append_to_timeline_year(
        text,
        2026,
        "NCR-MVC and QSS-Net broadened learned NLOS from reconstruction toward photon-robust clustering and efficient semantic classification.",
    )
    path.write_text(text, encoding="utf-8")


def insert_passive_table_row(text: str) -> str:
    if "sunAdaptiveMotionNLOS2025" in text:
        return text
    row_pattern = re.compile(
        r"^(?P<indent>\s*)\\cite\{boumanTurningCornersCameras2017\}[^\n]*Detection/\s*Tracking/\s*Identification[^\n]*\n",
        flags=re.MULTILINE,
    )
    matches = list(row_pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one passive Bouman recognition row, found {len(matches)}")
    match = matches[0]
    table_row = (
        f"{match.group('indent')}\\cite{{sunAdaptiveMotionNLOS2025}} & Ambient light & Conventional RGB camera "
        "& Temporal relay-wall motion & Action recognition\\\\%%%% Table body\n"
    )
    return text[: match.end()] + table_row + text[match.end() :]


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")
    text = insert_passive_table_row(text)

    heading = "Passive action recognition from relay-wall video."
    if heading not in text:
        anchor_heading = "Long-range passive NLOS under severe background."
        marker = f"\\noindent \\textbf{{{anchor_heading}}}"
        starts = [m.start() for m in re.finditer(re.escape(marker), text)]
        if len(starts) != 1:
            raise RuntimeError(f"Expected one passive heading anchor, found {len(starts)}")
        end = text.find("\n\n", starts[0])
        if end < 0:
            raise RuntimeError("Could not find paragraph end for passive heading anchor")
        block = r'''
\vspace{0.8mm}
\noindent \textbf{Passive action recognition from relay-wall video.}
Passive computational periscopy has primarily reconstructed static hidden intensity, whereas many safety and assistive applications require only the hidden activity class. Sun~\etal~introduced AME-Net, which recognizes actions from standard RGB videos of a visible relay wall by adaptively amplifying weak frame-to-frame motion while reducing environment-specific variation~\cite{sunAdaptiveMotionNLOS2025}. Its alternating recurrent feature extractor combines raw and enhanced frames, and the accompanying NLOS-Action benchmark contains 2,000 synthetic and more than 500 measured videos. This work extends passive NLOS from image recovery and tracking toward semantic temporal understanding without active illumination.
'''
        text = text[: end + 2] + block.strip("\n") + "\n\n" + text[end + 2 :]
    path.write_text(text, encoding="utf-8")


def update_learning() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    heading = "From reconstruction to recognition and clustering."
    if heading not in text:
        anchor = "This alternate training strategy achieves superior performance on both reconstruction and recognition tasks simultaneously, demonstrated on IEEE ICME 2025.\n"
        block = r'''

\vspace{0.8mm}
\noindent \textbf{From reconstruction to recognition and clustering.}
Recent work increasingly treats reconstructed NLOS observations as inputs to semantic inference rather than as final outputs. Sun~\etal~introduced AME-Net for passive hidden-action recognition from subtle relay-wall video and released the NLOS-Action synthetic/real benchmark~\cite{sunAdaptiveMotionNLOS2025}. Lin~\etal~then considered multiple photon-corrupted NLOS reconstructions as complementary views: NCR-MVC repairs inconsistent neighborhood graphs with shared-neighbor reweighting, Huber-smoothed dual consistency gates, and adaptive inverse-loss view weights, while retaining closed-form alternating updates and a convergence guarantee~\cite{linNCRMultiViewNLOS2026}. QSS-Net further makes efficient NLOS classification itself the target, representing the field's shift from complete geometric recovery toward time-sensitive semantic decisions~\cite{linQSSNetNLOS2026}. Together with learned feature embeddings and NLOS-R$^2$, these studies establish recognition, action understanding, and clustering as a parallel trajectory to hidden-scene reconstruction.
'''
        text = replace_once(text, anchor, anchor + block, "learning recognition paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_passive()
    update_learning()
    print("Synchronized three verified NLOS recognition and clustering papers.")


if __name__ == "__main__":
    main()
