#!/usr/bin/env python3
"""Synchronize the verified ICASSP 2026 audio-visual NLOS paper.

The edit is deliberately bounded and idempotent. It updates the README, the
interactive paper explorer and timeline, the semantically relevant acoustic
survey subsection, and the survey update log. Bibliography consolidation and
PDF compilation are handled by the guarded GitHub Actions workflow.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Non-line-of-sight vehicle detection via audio-visual fusion"
KEY = "wangAudioVisualNLOS2026"
DOI = "10.1109/ICASSP55912.2026.11465095"


def require_once(text: str, needle: str, label: str) -> None:
    count = text.count(needle)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {count}")


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    if TITLE in text:
        return

    table_anchor = "|------|-------|----------------|----------------|\n"
    require_once(text, table_anchor, "Latest Additions table separator")
    row = (
        "| 2026 | [Non-line-of-sight vehicle detection via audio-visual fusion]"
        "(https://doi.org/10.1109/ICASSP55912.2026.11465095) — Wang et al. | "
        "IEEE ICASSP 2026, 11807–11811 | Uses bird's-eye-view scene geometry "
        "together with time-frequency and spatiotemporal acoustic spectra in a "
        "CNN–LSTM–Conformer network for detecting fully occluded vehicles. The "
        "published experiments report 94.1% and 97.0% accuracy on the OVAD and "
        "AOVD datasets, extending acoustic NLOS from localization and reconstruction "
        "toward scene-conditioned semantic perception. |\n"
    )
    text = text.replace(table_anchor, table_anchor + row, 1)

    timeline_anchor = "## Milestone Timeline\n"
    require_once(text, timeline_anchor, "Milestone Timeline heading")
    timeline = (
        "\n- **2026 — Scene-aware audio-visual acoustic NLOS detection:** Wang et al. "
        "combine BEV scene structure with acoustic time-frequency and spatiotemporal "
        "features, moving hidden-vehicle sensing beyond audio-only localization toward "
        "multimodal semantic detection under occlusion.\n"
    )
    text = text.replace(timeline_anchor, timeline_anchor + timeline, 1)

    category_anchor = "## New NLOS Scenes and Modalities\n"
    require_once(text, category_anchor, "New NLOS Scenes and Modalities heading")
    category = (
        "\n- **Audio-visual acoustic perception:** [Wang et al., ICASSP 2026]"
        "(https://doi.org/10.1109/ICASSP55912.2026.11465095) fuse visual BEV scene "
        "geometry with acoustic spectra for semantic detection of vehicles that are "
        "outside the camera's line of sight; this is task-level NLOS sensing rather "
        "than hidden-image or hidden-shape reconstruction.\n"
    )
    text = text.replace(category_anchor, category_anchor + category, 1)
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if f'title:"{TITLE}"' in text:
        return

    papers_anchor = "    const papers=[\n"
    require_once(text, papers_anchor, "paper explorer array")
    record = (
        '      {cat:"latest modality learning acoustic audio-visual vehicle detection '
        'semantic scene-aware",title:"Non-line-of-sight vehicle detection via '
        'audio-visual fusion",authors:"Wang et al.",year:2026,venue:"IEEE ICASSP '
        '2026",url:"https://doi.org/10.1109/ICASSP55912.2026.11465095",key:"A '
        'scene-aware CNN–LSTM–Conformer combines BEV visual geometry with acoustic '
        'time-frequency and spatiotemporal spectra for fully occluded vehicle '
        'detection, reporting 94.1% and 97.0% accuracy on OVAD and AOVD."},\n'
    )
    text = text.replace(papers_anchor, papers_anchor + record, 1)

    pattern = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body">'
        r'<strong>.*?</strong><p>)(.*?)(</p>)',
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise RuntimeError("Could not locate the 2026 website timeline entry")
    sentence = (
        " Scene-aware audio-visual acoustic fusion further extends this trajectory "
        "to semantic detection of fully occluded vehicles by conditioning acoustic "
        "spectra on BEV scene geometry."
    )
    text = text[: match.start(2)] + match.group(2) + sentence + text[match.end(2) :]

    actual = text.count("{cat:")
    text, n = re.subn(
        r'<b>\d+</b><span>tracked latest entries</span>',
        f'<b>{actual}</b><span>tracked latest entries</span>',
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError("Could not update the website paper count")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")
    if KEY in text:
        return

    section_start = text.find(r"\subsection{Acoustic NLOS Imaging}")
    if section_start < 0:
        raise RuntimeError("Acoustic NLOS Imaging subsection was not found")
    next_section = text.find(r"\bookmark[", section_start + 1)
    if next_section < 0:
        raise RuntimeError("Could not locate the subsection following Acoustic NLOS Imaging")

    paragraph = (
        "\n\nAt the task level, Wang~\\etal~combine bird's-eye-view scene geometry with "
        "time--frequency and spatiotemporal acoustic spectra for detecting vehicles "
        "that are fully occluded from the camera~\\cite{wangAudioVisualNLOS2026}. "
        "Their scene-aware network uses CNN, LSTM, and Conformer modules to model "
        "local spectral structure, temporal evolution, and long-range cross-modal "
        "context, reporting 94.1\\% and 97.0\\% accuracy on the OVAD and AOVD "
        "datasets, respectively. Unlike acoustic echo tomography or diffraction-based "
        "source localization, this work does not reconstruct hidden geometry; it "
        "establishes a complementary semantic branch in which visible environment "
        "layout conditions the interpretation of sound propagated from an unseen "
        "traffic participant.\n"
    )
    text = text[:next_section].rstrip() + paragraph + "\n" + text[next_section:]
    path.write_text(text, encoding="utf-8")

    main = ROOT / "bare_jrnl.tex"
    main_text = main.read_text(encoding="utf-8")
    marker = "% 31 July 2026 modality trace: scene-aware audio-visual acoustic NLOS vehicle detection synchronized.\n"
    if marker not in main_text:
        anchor = "%% bare_jrnl.tex\n"
        require_once(main_text, anchor, "bare_jrnl header")
        main_text = main_text.replace(anchor, anchor + marker, 1)
        main.write_text(main_text, encoding="utf-8")


def update_note() -> None:
    note = ROOT / "updates/2026-07-31-audio-visual-acoustic-nlos.md"
    note.write_text(
        """# 31 July 2026 audio-visual acoustic NLOS update

## Added work

- Huaxuan Wang, Huilong Yu, Ruizeng Zhang, Wei Zhou, and Junqiang Xi, **Non-line-of-sight vehicle detection via audio-visual fusion**, IEEE ICASSP 2026, pp. 11807--11811, DOI: `10.1109/ICASSP55912.2026.11465095`.

## Scope decision

The paper is included as tightly adjacent semantic NLOS sensing rather than hidden-image reconstruction. It explicitly targets vehicles outside the visual line of sight, derives acoustic time-frequency and spatiotemporal representations, conditions them on bird's-eye-view scene geometry, and evaluates on dedicated occluded-vehicle datasets. The repository description and survey text label this distinction directly.

## Artifact synchronization

The guarded workflow updates `README.md`, `index.html`, `article/5newscenes.tex`, `bare_jrnl.tex`, and the consolidated bibliography, then performs a clean LaTeX/BibTeX build of `bare_jrnl.pdf`. Validation checks require one structured README row, one explorer object, one canonical BibTeX record, a resolved survey citation, matching website counts, extracted PDF text, and successful first/last-page rendering before committing.
""",
        encoding="utf-8",
    )


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    update_note()
    print(f"Integrated {TITLE} across source artifacts.")


if __name__ == "__main__":
    main()
