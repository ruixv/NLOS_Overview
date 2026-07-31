#!/usr/bin/env python3
"""Synchronize two verified NLOS gaps across public and survey artifacts.

The bounded, idempotent edits integrate an ICASSP 2026 audio-visual semantic
NLOS paper and complete the already-staged ICEE 2025 NIR raster-scanning paper
whose final venue and survey citation were not yet synchronized with the
public explorer and bibliography.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
AUDIO_TITLE = "Non-line-of-sight vehicle detection via audio-visual fusion"
AUDIO_KEY = "wangAudioVisualNLOS2026"
NIR_TITLE = "Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength"
NIR_KEY = "roueinfarNIRRaster2025"


def require_once(text: str, needle: str, label: str) -> None:
    count = text.count(needle)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {count}")


def insert_latest_row(text: str, title: str, row: str) -> str:
    if title in text:
        return text
    anchor = "|------|-------|----------------|----------------|\n"
    require_once(text, anchor, "Latest Additions table separator")
    return text.replace(anchor, anchor + row, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")

    audio_row = (
        "| 2026 | [Non-line-of-sight vehicle detection via audio-visual fusion]"
        "(https://doi.org/10.1109/ICASSP55912.2026.11465095) — Wang et al. | "
        "IEEE ICASSP 2026, 11807–11811 | Uses bird's-eye-view scene geometry "
        "together with time-frequency and spatiotemporal acoustic spectra in a "
        "CNN–LSTM–Conformer network for detecting fully occluded vehicles. The "
        "published experiments report 94.1% and 97.0% accuracy on the OVAD and "
        "AOVD datasets, extending acoustic NLOS from localization and reconstruction "
        "toward scene-conditioned semantic perception. |\n"
    )
    text = insert_latest_row(text, AUDIO_TITLE, audio_row)

    nir_row = (
        "| 2025 | [Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength]"
        "(https://doi.org/10.1109/ICEE67339.2025.11213924) — Roueinfar and Salmanian | "
        "IEEE ICEE 2025, 1175–1179 | Demonstrates a low-cost steady-state three-bounce "
        "system using a 500 mW 808 nm laser on a pan–tilt raster scanner and a "
        "conventional NIR camera. A 16×16 relay-wall scan reconstructs three hidden "
        "targets and is evaluated with MSE/RMSE. The July 2026 arXiv upload is labeled "
        "by its verified final 2025 IEEE conference venue. |\n"
    )
    text = insert_latest_row(text, NIR_TITLE, nir_row)

    timeline_anchor = (
        "   │     Doğan: laser–acoustic early fusion and LAO-Net extend hidden-human "
        "NLOS sensing from localization/reconstruction toward four-class orientation "
        "inference [Scientific Reports]\n"
    )
    audio_line = (
        "   │     Wang et al.: scene-aware audio–visual fusion conditions acoustic "
        "spectra on BEV geometry for semantic detection of fully occluded vehicles "
        "[IEEE ICASSP]\n"
    )
    if audio_line not in text:
        require_once(text, timeline_anchor, "2026 acoustic milestone")
        text = text.replace(timeline_anchor, timeline_anchor + audio_line, 1)

    # The NIR paper was already present as a 2025 timeline milestone. Its missing
    # pieces were the structured public entry, final-venue bibliography, and PDF.
    nir_timeline = (
        "2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster "
        "scanning [IEEE ICEE]"
    )
    if nir_timeline not in text:
        raise RuntimeError("Expected the existing 2025 NIR timeline milestone")

    path.write_text(text, encoding="utf-8")


def insert_paper_record(text: str, title: str, record: str) -> str:
    if f'title:"{title}"' in text:
        return text
    anchor = "    const papers=[\n"
    require_once(text, anchor, "paper explorer array")
    return text.replace(anchor, anchor + record, 1)


def append_timeline_sentence(text: str, year: int, sentence: str, marker: str) -> str:
    if marker in text:
        return text
    pattern = re.compile(
        rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">'
        r'<strong>.*?</strong><p>)(.*?)(</p>)',
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f"Could not locate the {year} website timeline entry")
    return text[: match.start(2)] + match.group(2) + sentence + text[match.end(2) :]


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    audio_record = (
        '      {cat:"latest modality learning acoustic audio-visual vehicle detection '
        'semantic scene-aware",title:"Non-line-of-sight vehicle detection via '
        'audio-visual fusion",authors:"Wang et al.",year:2026,venue:"IEEE ICASSP '
        '2026",url:"https://doi.org/10.1109/ICASSP55912.2026.11465095",key:"A '
        'scene-aware CNN–LSTM–Conformer combines BEV visual geometry with acoustic '
        'time-frequency and spatiotemporal spectra for fully occluded vehicle '
        'detection, reporting 94.1% and 97.0% accuracy on OVAD and AOVD."},\n'
    )
    text = insert_paper_record(text, AUDIO_TITLE, audio_record)

    nir_record = (
        '      {cat:"latest active hardware steady-state NIR raster-scan low-cost '
        'conventional-camera",title:"Non-Line-of-Sight Imaging Using Raster Scanning '
        'at NIR Wavelength",authors:"Roueinfar & Salmanian",year:2025,venue:"IEEE '
        'ICEE 2025",url:"https://doi.org/10.1109/ICEE67339.2025.11213924",key:"A '
        '500 mW 808 nm laser and pan–tilt unit raster-scan a relay wall while a '
        'conventional NIR camera records steady-state three-bounce returns. A 16×16 '
        'scan reconstructs three hidden targets; the verified IEEE venue supersedes '
        'the later arXiv upload."},\n'
    )
    text = insert_paper_record(text, NIR_TITLE, nir_record)

    text = append_timeline_sentence(
        text,
        2026,
        " Scene-aware audio-visual acoustic fusion further extends this trajectory "
        "to semantic detection of fully occluded vehicles by conditioning acoustic "
        "spectra on BEV scene geometry.",
        "Scene-aware audio-visual acoustic fusion further extends this trajectory",
    )
    text = append_timeline_sentence(
        text,
        2025,
        " Low-cost 808 nm steady-state raster scanning also showed that a pan–tilt "
        "laser and conventional NIR camera can recover simple hidden targets without "
        "transient timing hardware.",
        "Low-cost 808 nm steady-state raster scanning also showed",
    )

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
    acoustic = ROOT / "article/5newscenes.tex"
    text = acoustic.read_text(encoding="utf-8")
    if AUDIO_KEY not in text:
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
        acoustic.write_text(text, encoding="utf-8")

    active = (ROOT / "article/2active.tex").read_text(encoding="utf-8")
    if NIR_KEY not in active or "Low-cost NIR steady-state raster scanning" not in active:
        raise RuntimeError("The staged NIR survey paragraph/table citation is missing")

    main = ROOT / "bare_jrnl.tex"
    main_text = main.read_text(encoding="utf-8")
    marker = (
        "% 31 July 2026 modality trace: audio-visual acoustic NLOS and final-venue "
        "NIR raster-scanning records synchronized.\n"
    )
    if marker not in main_text:
        anchor = "%% bare_jrnl.tex\n"
        require_once(main_text, anchor, "bare_jrnl header")
        main_text = main_text.replace(anchor, anchor + marker, 1)
        main.write_text(main_text, encoding="utf-8")


def update_note() -> None:
    note = ROOT / "updates/2026-07-31-audio-visual-and-nir-nlos.md"
    note.write_text(
        """# 31 July 2026 audio-visual and NIR NLOS synchronization

## Added or completed works

- Huaxuan Wang, Huilong Yu, Ruizeng Zhang, Wei Zhou, and Junqiang Xi, **Non-line-of-sight vehicle detection via audio-visual fusion**, IEEE ICASSP 2026, pp. 11807--11811, DOI: `10.1109/ICASSP55912.2026.11465095`.
- Mohammad Roueinfar and Mahdi Salmanian, **Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength**, IEEE ICEE 2025, pp. 1175--1179, DOI: `10.1109/ICEE67339.2025.11213924`.

## Scope and venue decisions

The audio-visual paper is included as tightly adjacent semantic NLOS sensing rather than hidden-image reconstruction. It targets vehicles outside the visual line of sight and conditions acoustic time-frequency and spatiotemporal representations on bird's-eye-view scene geometry.

The NIR work was first rediscovered through its July 2026 arXiv upload, but the PDF and scholarly indexes verify that it had already appeared at IEEE ICEE on 13 May 2025. The repository therefore uses the final conference venue. Its timeline and active-method survey paragraph were already staged; this update adds the canonical final-venue BibTeX record, structured README/website entries, resolved citations, and regenerated PDF.

## Artifact synchronization

The guarded workflow updates `README.md`, `index.html`, `article/5newscenes.tex`, `bare_jrnl.tex`, and the consolidated bibliography, then performs a clean LaTeX/BibTeX build of `bare_jrnl.pdf`. Validation requires unique structured public entries, canonical BibTeX records, resolved survey citations, matching website counts, extracted PDF text, and successful first/last-page rendering before committing.
""",
        encoding="utf-8",
    )


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    update_note()
    print("Integrated audio-visual and NIR NLOS records across source artifacts.")


if __name__ == "__main__":
    main()
