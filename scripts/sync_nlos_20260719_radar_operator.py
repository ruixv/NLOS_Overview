#!/usr/bin/env python3
"""Synchronize two verified learned-operator radar/THz NLOS papers."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar",
        "authors": "Chen et al.",
        "year": 2026,
        "venue": "Journal of Radars 2026",
        "url": "https://doi.org/10.12000/JR25132",
        "cat": "latest radar rf mmwave deep unfolding sparse reconstruction",
        "key": "chenRMOperatorMmWaveNLOS2026",
        "summary": "Embeds a range-migration kernel inside a FISTA-style deep-unfolding network for around-corner near-field mmWave 3D imaging, improving robustness to phase error, aperture shadowing, and multipath while reporting roughly two orders of magnitude faster reconstruction than conventional sparse solvers.",
    },
    {
        "title": "Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging",
        "authors": "Chen et al.",
        "year": 2026,
        "venue": "Photonics 2026",
        "url": "https://doi.org/10.3390/photonics13050440",
        "cat": "latest terahertz sub-thz radar deep unfolding holographic operator",
        "key": "chenDeepUnfoldingTHzNLOS2026",
        "summary": "Combines a fast holographic imaging operator with FISTA-Net for 121-GHz sub-THz around-corner 3D reconstruction, explicitly modeling reflector geometry and multipath and validating learned sparse inversion on measured hidden metal targets.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def insert_before_once(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    return replace_once(text, marker, addition.rstrip() + "\n\n" + marker, label)


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def append_to_homepage_timeline(text: str, year: int, sentence: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if f'<div class="year">{year}</div>' in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    line = lines[matches[0]]
    if sentence.strip() not in line:
        closing = "</p></div></div>"
        if closing not in line:
            raise RuntimeError(f"Timeline closing marker missing for {year}")
        lines[matches[0]] = line.replace(closing, " " + sentence.strip() + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    if "**Update run: 19 July 2026.**" not in text:
        raise RuntimeError("README update date is not 19 July 2026")

    rows = ""
    for p in PAPERS:
        if f"[{p['title']}]" not in text:
            rows += (
                f"| {p['year']} | [{p['title']}]({p['url']}) - {p['authors']} | "
                f"{p['venue']} | {p['summary']} |\n"
            )
    if rows:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + rows, "README latest-additions header")

    timeline_lines = [
        "   │     Chen et al.: RM-operator learning for mmWave NLOS — FISTA unfolding with a fast range-migration kernel for measured around-corner 3D imaging [Journal of Radars]\n",
        "   │     Chen et al.: learned 121-GHz sub-THz NLOS — holographic-operator FISTA-Net for measured hidden-target reconstruction [Photonics]\n",
    ]
    lines = text.splitlines(keepends=True)
    year_matches = [i for i, line in enumerate(lines) if line.startswith("2026 ──")]
    if len(year_matches) != 1:
        raise RuntimeError(f"Expected one README 2026 timeline start, found {len(year_matches)}")
    insert_at = year_matches[0] + 1
    for line in reversed(timeline_lines):
        if line.strip() not in text:
            lines.insert(insert_at, line)
    text = "".join(lines)

    audit = (
        "   |     19 July 2026 radar/THz citation trace: verified learned range-migration and holographic-operator NLOS reconstruction integrated across public, survey, bibliography, and build artifacts\n"
    )
    if "19 July 2026 radar/THz citation trace" not in text:
        marker = "   |     19 July 2026 phasor/polarization citation trace:"
        pos = text.find(marker)
        if pos == -1:
            raise RuntimeError("README phasor/polarization audit marker missing")
        line_start = text.rfind("\n", 0, pos) + 1
        text = text[:line_start] + audit + text[line_start:]

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if "Updated 19 July 2026 · 190+ papers" not in text or "Last updated: 19 July 2026" not in text:
        raise RuntimeError("Homepage date is not synchronized to 19 July 2026")

    additions = [paper_object(p) for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if additions:
        text = replace_once(
            text,
            "    const papers=[\n",
            "    const papers=[\n" + "\n".join(additions) + "\n",
            "homepage paper array",
        )

    text = append_to_homepage_timeline(
        text,
        2026,
        "Operator-learned radar NLOS expanded from range-migration mmWave imaging to 121-GHz holographic deep unfolding, making sparse inversion faster while explicitly retaining reflector and multipath physics.",
    )

    stat = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    match = stat.search(text)
    if not match:
        raise RuntimeError("Homepage tracked-entry statistic not found")
    count = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    if int(match.group(2)) != count:
        text = stat.sub(lambda m: m.group(1) + str(count) + m.group(3), text, count=1)

    path.write_text(text, encoding="utf-8")


def update_new_scenes() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")

    radar = r"""\vspace{0.8mm}
\noindent \textbf{Operator-learned range migration for mmWave NLOS.}
Chen~\etal~formulate looking-around-corner millimeter-wave reconstruction with a fast range-migration kernel and unfold a FISTA sparse solver into a fixed-depth network~\cite{chenRMOperatorMmWaveNLOS2026}. The learned operator retains the reflector-aware propagation model while adapting thresholds and update parameters to phase errors, aperture shadowing, and multipath deviations observed with non-ideal relay surfaces. Near-field measurements of several metallic 3D targets show sharper reconstructions across reduced sampling ratios and approximately two orders of magnitude faster inference than conventional iterative sparse imaging. This work complements HoloRadar's mobile scene-level representation by showing how classical radar migration itself can become a trainable physics layer for controlled around-corner imaging.
"""
    text = insert_before_once(
        text,
        "Recent RF/mmWave work further expands the meaning of NLOS perception beyond monostatic reconstruction.",
        radar,
        "RF/mmWave expansion marker",
    )

    thz = r"""\vspace{0.8mm}
\noindent \textbf{Deep-unfolded sub-THz radar imaging.}
Chen~\etal~extend reflector-aware learned inversion to a 121~GHz sub-terahertz platform~\cite{chenDeepUnfoldingTHzNLOS2026}. Their method replaces the prohibitively large sensing matrix with a fast holographic imaging operator and embeds it in a FISTA-Net architecture whose learned updates compensate phase error, aperture occlusion, and multipath mismatch. Experiments on hidden metal letters, a resolution chart, and scissors demonstrate measured 3D reconstruction with markedly lower memory and computation than matrix-based sparse solvers. Together with earlier mirror-folding sub-THz imaging, this result moves terahertz NLOS from geometric backprojection toward trainable operator inversion while preserving an explicit propagation model.
"""
    text = insert_before_once(
        text,
        "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{NLOS Human Pose Estimation}",
        thz,
        "human-pose section marker",
    )

    path.write_text(text, encoding="utf-8")


def update_master_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = path.read_text(encoding="utf-8")
    text = text.replace("through 18 July 2026", "through 19 July 2026", 1)
    comment = "% 19 July 2026 radar/THz citation trace integrates learned range-migration mmWave and holographic sub-THz NLOS operators.\n"
    if comment.strip() not in text:
        text = replace_once(
            text,
            "\\input{article/5newscenes.tex}",
            comment + "\\input{article/5newscenes.tex}",
            "master new-scenes anchor",
        )
    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-19-radar-operator-citation-trace.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "STATUS: STAGED — source synchronization and PDF rebuild are pending.",
        "STATUS: SYNCHRONIZED — guarded source integration completed; the PDF is committed only after clean-build validation.",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_new_scenes()
    update_master_tex()
    update_note()
    print("Synchronized two verified learned-operator radar and THz NLOS papers.")


if __name__ == "__main__":
    main()
