#!/usr/bin/env python3
"""Synchronize verified finite-aperture and hidden-human NLOS records."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Finite-Aperture Limits for Yaw Estimation in Confocal Non-Line-of-Sight Imaging",
        "authors": "Romanelli et al.",
        "year": 2026,
        "venue": "Journal of Imaging 2026",
        "url": "https://doi.org/10.3390/jimaging12060248",
        "cat": "latest active theory",
        "key": "romanelliFiniteApertureYawNLOS2026",
        "summary": "Derives a finite-relay-wall switch-line criterion and Fisher-information bounds for yaw observability in confocal transient NLOS. Simulated and measured f-k/backprojection results show how angular information degrades as informative transient features are clipped, providing quantitative guidance for relay-aperture placement and orientation recovery.",
    },
    {
        "title": "Machine Learning-Based Human Detection Using Active Non-Line-of-Sight Laser Sensing",
        "authors": "Celebi, Turkoglu",
        "year": 2026,
        "venue": "Sensors 2026",
        "url": "https://doi.org/10.3390/s26072046",
        "cat": "latest active detection",
        "key": "celebiHumanDetectionNLOS2026",
        "summary": "Uses real SPAD-TCSPC transient measurements from controlled rubble-like scenes to compare CNN, GRU, and random-forest classifiers for hidden-human presence across poses, orientations, and object layouts. All models reach full sensitivity, while random forest provides the strongest specificity and weighted F1 under limited photon counts.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def add_citation_to_row(text: str, needle: str, key: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {label} row, found {len(matches)}")
    line = lines[matches[0]]
    match = re.search(r"\\cite\{([^}]*)\}", line)
    if not match:
        raise RuntimeError(f"Could not locate citation list in {label} row")
    keys = [item.strip() for item in match.group(1).split(",") if item.strip()]
    if key not in keys:
        keys.append(key)
        line = line[: match.start(1)] + ",".join(keys) + line[match.end(1) :]
        lines[matches[0]] = line
    return "".join(lines)


def insert_after_heading_block(text: str, heading: str, block: str, label: str) -> str:
    marker = f"\\noindent \\textbf{{{heading}}}"
    starts = [match.start() for match in re.finditer(re.escape(marker), text)]
    if len(starts) != 1:
        raise RuntimeError(f"Expected one {label} heading, found {len(starts)}")
    end = text.find("\n\n", starts[0])
    if end < 0:
        raise RuntimeError(f"Could not locate paragraph end after {label}")
    return text[: end + 2] + block.strip("\n") + "\n\n" + text[end + 2 :]


def append_homepage_timeline(text: str) -> str:
    marker = "Finite-aperture theory quantifies yaw observability"
    if marker in text:
        return text
    lines = text.splitlines(keepends=True)
    needle = '<div class="year">2026</div>'
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage 2026 timeline row, found {len(matches)}")
    closing = "</p></div></div>"
    line = lines[matches[0]]
    if closing not in line:
        raise RuntimeError("Homepage 2026 timeline row has an unexpected structure")
    sentence = (
        " Finite-aperture theory quantifies yaw observability and relay-wall design limits, "
        "while real SPAD-TCSPC data supports learned hidden-human detection without full scene reconstruction."
    )
    lines[matches[0]] = line.replace(closing, sentence + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = ""
    for paper in PAPERS:
        if f"[{paper['title']}]" in text:
            continue
        rows += (
            f"| {paper['year']} | [{paper['title']}]({paper['url']}) - {paper['authors']} | "
            f"{paper['venue']} | {paper['summary']} |\n"
        )
    if rows:
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + rows, "README latest-additions table")

    if "Romanelli et al.: finite-aperture" not in text:
        anchor = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
        additions = (
            "   |     Romanelli et al.: finite-aperture switch-line and Fisher-information analysis quantifies yaw observability [Journal of Imaging]\n"
            "   |     Celebi and Turkoglu: real SPAD-TCSPC measurements enable learned hidden-human detection [Sensors]\n"
        )
        text = replace_once(text, anchor, additions + anchor, "README 2026 citation-tracing timeline")
    path.write_text(text, encoding="utf-8")


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    new_lines = ""
    for paper in PAPERS:
        if f'title:"{paper["title"]}"' not in text:
            new_lines += paper_object(paper) + "\n"
    if new_lines:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + new_lines, "homepage paper array")
    text = append_homepage_timeline(text)
    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    text = add_citation_to_row(
        text,
        "& Pulsed laser & SPAD & Time of fight &  Pose estimation",
        "romanelliFiniteApertureYawNLOS2026",
        "active pose-estimation",
    )
    text = add_citation_to_row(
        text,
        "& Pulsed laser & SPAD & Time of fight &  Detection/ Tracking/ Identification",
        "celebiHumanDetectionNLOS2026",
        "active detection",
    )

    if "Finite-aperture yaw observability." not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Finite-aperture yaw observability.}
Romanelli~\etal~characterized how a finite sampled relay wall limits orientation recovery in confocal transient NLOS~\cite{romanelliFiniteApertureYawNLOS2026}. A geometric switch-line criterion identifies when the endpoint ordering that supports unique planar reconstruction leaves the measured aperture, while a Fisher-information analysis shows that yaw sensitivity decays continuously rather than disappearing abruptly. Simulated and experimental $f$--$k$ and backprojection results connect this loss of angular information to edge-like or spatially ambiguous reconstructions. The study turns the qualitative missing-cone and feature-visibility limitation into quantitative guidance for relay-wall size, placement, and pose estimation.
"""
        text = insert_after_heading_block(text, "Visibility limits and recoverability.", paragraph, "visibility-limits")

    if "Real-measurement hidden-human detection." not in text:
        anchor = "Therefore, NLOS recognition is typically  based on data-driven methods (see Sec.~\\ref{sec4} for details)."
        paragraph = r"""

\vspace{0.8mm}
\noindent \textbf{Real-measurement hidden-human detection.}
Celebi and Turkoglu built an active SPAD--TCSPC NLOS sensing system and collected transient waveforms for hidden people across multiple poses, orientations, and rubble-like object configurations~\cite{celebiHumanDetectionNLOS2026}. CNN, GRU, and random-forest models all detected the human-present class with full sensitivity, while the random forest achieved the strongest specificity and weighted F1 under the available photon statistics. This result complements image reconstruction and tracking by showing that low-cost transient hardware can support a high-level search-and-rescue decision directly from measured histograms, without first recovering a detailed hidden scene.
"""
        text = replace_once(text, anchor, anchor + paragraph, "active recognition prose")
    path.write_text(text, encoding="utf-8")


def validate() -> None:
    files = {
        "readme": (ROOT / "README.md").read_text(encoding="utf-8"),
        "index": (ROOT / "index.html").read_text(encoding="utf-8"),
        "active": (ROOT / "article/2active.tex").read_text(encoding="utf-8"),
        "bib": (ROOT / "egbib_20260718_visibility_detection_updates.bib").read_text(encoding="utf-8"),
    }
    for paper in PAPERS:
        title = str(paper["title"])
        key = str(paper["key"])
        if files["readme"].lower().count("[" + title.lower() + "]") != 1:
            raise RuntimeError(f"README entry missing or duplicated: {title}")
        if files["index"].lower().count('title:"' + title.lower() + '"') != 1:
            raise RuntimeError(f"Homepage entry missing or duplicated: {title}")
        if key not in files["active"]:
            raise RuntimeError(f"Survey citation missing: {key}")
        if files["bib"].lower().count("{" + key.lower() + ",") != 1:
            raise RuntimeError(f"Canonical BibTeX record missing or duplicated: {key}")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    validate()
    print("Synchronized finite-aperture yaw analysis and real-measurement hidden-human NLOS detection.")


if __name__ == "__main__":
    main()
