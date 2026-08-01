#!/usr/bin/env python3
"""Synchronize two verified frequency-domain active NLOS reconstruction papers.

Edits are bounded and idempotent. The companion workflow consolidates the
bibliography, rebuilds the PDF, and validates every public artifact.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_TITLE = "Fast non-line-of-sight imaging based on product-convolution expansions"
PRODUCT_KEY = "xuProductConvolutionNLOS2022"
RMA_TITLE = (
    "Non-line-of-sight virtual modulated range migration imaging based on "
    "super-resolution histograms"
)
RMA_KEY = "tianVirtualRMAHistograms2025"


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


def insert_after_unique_line(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if marker in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {len(matches)}")
    lines.insert(matches[0] + 1, addition)
    return "".join(lines)


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
    return text[:match.start(2)] + match.group(2) + sentence + text[match.end(2):]


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    product_row = (
        "| 2022 | [Fast non-line-of-sight imaging based on product-convolution "
        "expansions](https://doi.org/10.1364/OL.469719) — Xu et al. | "
        "Optics Letters 47(18), 4680–4683 (2022) | Approximates the shift-variant "
        "non-confocal ellipsoidal forward operator and its adjoint by local "
        "convolutions, then uses FFTs and low-rank matrix decompositions for fast "
        "iterative reconstruction. Public transient datasets show phasor-field-like "
        "quality with substantially lower runtime. |\n"
    )
    rma_row = (
        "| 2025 | [Non-line-of-sight virtual modulated range migration imaging "
        "based on super-resolution histograms](https://doi.org/10.1364/OL.542897) "
        "— Tian et al. | Optics Letters 50(2), 519–522 (2025) | Combines "
        "deconvolution-modified iterative backprojection with virtual modulated "
        "range migration, recovering 50× super-resolved histograms from 1 ns "
        "measurements before high-resolution confocal or non-confocal reconstruction. "
        "It targets inexpensive low-time-resolution NLOS systems and reduces the "
        "required data volume. |\n"
    )
    text = insert_latest_row(text, PRODUCT_TITLE, product_row)
    text = insert_latest_row(text, RMA_TITLE, rma_row)
    text = insert_after_unique_line(
        text,
        "2022 ──",
        "   │     Xu et al.: product-convolution expansions turn the shift-variant "
        "non-confocal ellipsoidal operator into FFT-accelerated local convolutions "
        "[Optics Letters]\n",
        "2022 milestone line",
    )
    text = insert_after_unique_line(
        text,
        "2025 ── Roueinfar & Salmanian",
        "   │     Tian et al.: deconvolution and virtual modulated range migration "
        "recover 50× super-resolution histograms from nanosecond-resolution ToF data "
        "[Optics Letters]\n",
        "2025 milestone line",
    )
    text = text.replace(
        "**Update run: 31 July 2026.**",
        "**Update run: 1 August 2026.**",
        1,
    )
    text = text.replace("Last_Updated-July_2026", "Last_Updated-August_2026", 1)
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    product_record = (
        '      {cat:"latest active reconstruction non-confocal fast fft inverse '
        'operator product-convolution low-rank",title:"Fast non-line-of-sight '
        'imaging based on product-convolution expansions",authors:"Xu et al.",'
        'year:2022,venue:"Optics Letters 47(18), 4680–4683",'
        'url:"https://doi.org/10.1364/OL.469719",key:"The shift-variant '
        'non-confocal ellipsoidal operator and its adjoint are approximated by local '
        'convolutions, enabling FFT acceleration and a low-rank product-convolution '
        'representation validated on public transient datasets."},\n'
    )
    rma_record = (
        '      {cat:"latest active reconstruction super-resolution histogram '
        'low-timing-resolution range-migration confocal non-confocal",title:"'
        'Non-line-of-sight virtual modulated range migration imaging based on '
        'super-resolution histograms",authors:"Tian et al.",year:2025,'
        'venue:"Optics Letters 50(2), 519–522",'
        'url:"https://doi.org/10.1364/OL.542897",key:"Deconvolution-modified '
        'iterative backprojection recovers 50× super-resolved histograms from 1 ns '
        'measurements, followed by virtual modulated range migration for '
        'high-resolution confocal or non-confocal NLOS reconstruction."},\n'
    )
    text = insert_paper_record(text, PRODUCT_TITLE, product_record)
    text = insert_paper_record(text, RMA_TITLE, rma_record)
    text = append_timeline_sentence(
        text,
        2022,
        " Xu et al. additionally approximated the shift-variant non-confocal "
        "ellipsoidal operator with low-rank product-convolution expansions, bringing "
        "FFT acceleration to a general iterative forward/adjoint model.",
        "low-rank product-convolution expansions",
    )
    text = append_timeline_sentence(
        text,
        2025,
        " Tian et al. coupled deconvolution-modified iterative backprojection with "
        "virtual modulated range migration, obtaining 50-fold super-resolved "
        "histograms from 1 ns measurements for both confocal and non-confocal NLOS.",
        "50-fold super-resolved histograms",
    )
    text = text.replace("Updated 31 July 2026", "Updated 1 August 2026", 1)
    text = text.replace("Last updated: 31 July 2026", "Last updated: 1 August 2026", 1)
    text = text.replace("updated July 2026", "updated August 2026", 1)
    actual = text.count("{cat:")
    text, count = re.subn(
        r'<b>\d+</b><span>tracked latest entries</span>',
        f'<b>{actual}</b><span>tracked latest entries</span>',
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("website tracked-entry count anchor not found")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if PRODUCT_KEY not in text or RMA_KEY not in text:
        anchor = (
            "Besides, Liu~ \\etal~\\cite{liuPhasorFieldDiffraction2020,"
            "liuVirtualWaveOptics2018}~and Reza~\\etal~"
        )
        if anchor not in text:
            raise RuntimeError("Wave-based phasor-field anchor was not found")
        paragraph = (
            "\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Fast shift-variant inversion and low-resolution "
            "histogram enhancement.}\n"
            "Two works extend frequency-domain NLOS reconstruction without assuming "
            "that acquisition already provides a dense, picosecond-resolved confocal "
            "transient. Xu~\\etal~approximate the general non-confocal ellipsoidal "
            "forward operator and its adjoint by spatially local product convolutions, "
            "then use FFT evaluation and low-rank matrix decompositions to accelerate "
            "iterative inversion~\\cite{xuProductConvolutionNLOS2022}. Validation on "
            "the Zaragoza and Wisconsin datasets shows reconstruction quality "
            "comparable to phasor-field processing at substantially reduced runtime, "
            "providing an efficient operator-level alternative for shift-variant "
            "transport. Tian~\\etal~address temporal resolution upstream of migration: "
            "deconvolution-modified iterative backprojection first estimates a "
            "super-resolution transient histogram, after which virtual modulated "
            "range migration reconstructs the hidden volume~"
            "\\cite{tianVirtualRMAHistograms2025}. Their experiments recover a "
            "50-fold temporally super-resolved histogram from 1~ns measurements and "
            "support both confocal and non-confocal configurations with less data. "
            "Together, these methods broaden the LCT/$f$--$k$/phasor trajectory from "
            "closed-form confocal transforms toward efficient shift-variant operators "
            "and computational compensation for commodity-scale timing resolution.\n\n"
        )
        text = text.replace(anchor, paragraph + anchor, 1)

    table_anchor = ",wangIRFDeconvolutionNLOS2024}"
    table_addition = (
        ",wangIRFDeconvolutionNLOS2024,xuProductConvolutionNLOS2022,"
        "tianVirtualRMAHistograms2025}"
    )
    if PRODUCT_KEY not in text.split("\\end{table*}", 1)[0]:
        require_once(text, table_anchor, "active table citation tail")
        text = text.replace(table_anchor, table_addition, 1)
    path.write_text(text, encoding="utf-8")

    main = ROOT / "bare_jrnl.tex"
    main_text = main.read_text(encoding="utf-8")
    marker = (
        "% 1 August 2026 citation trace: product-convolution inversion and "
        "super-resolution virtual range migration synchronized across public artifacts.\n"
    )
    if marker not in main_text:
        header = "%% bare_jrnl.tex\n"
        require_once(main_text, header, "bare_jrnl header")
        main_text = main_text.replace(header, header + marker, 1)
        main.write_text(main_text, encoding="utf-8")


def update_note() -> None:
    note = ROOT / "updates/2026-08-01-frequency-domain-reconstruction.md"
    note.write_text(
        """# Frequency-domain active NLOS citation-trace update — 1 August 2026

A forward-reference and related-work audit around the f-k migration, phasor-field,
non-confocal ellipsoidal-operator, and low-timing-resolution branches identified two
peer-reviewed works absent from the README, homepage explorer, survey prose, and
merged bibliography:

- Weihao Xu, Songmao Chen, Yuyuan Tian, Dingjie Wang, and Xiuqin Su,
  **Fast non-line-of-sight imaging based on product-convolution expansions**,
  *Optics Letters* 47(18), 4680–4683 (2022), DOI `10.1364/OL.469719`.
- Xiaorui Tian, Jingping Yu, Kai Qiao, Meng Tang, Siqi Zhang, and Chenfei Jin,
  **Non-line-of-sight virtual modulated range migration imaging based on
  super-resolution histograms**, *Optics Letters* 50(2), 519–522 (2025),
  DOI `10.1364/OL.542897`.

Both are direct active transient NLOS reconstruction papers. The first accelerates a
general non-confocal, shift-variant ellipsoidal forward/adjoint operator with local
product convolutions, FFTs, and low-rank decompositions. The second combines
deconvolution-modified iterative backprojection and virtual modulated range migration
to recover 50-fold super-resolved histograms from 1 ns measurements before confocal or
non-confocal reconstruction.

The synchronized integration adds final journal metadata and concise summaries to the
README and interactive explorer, places both methods in the active wave/frequency-domain
survey trajectory, adds canonical BibTeX records, regenerates the merged bibliography
and PDF, and checks citations, entry counts, PDF semantics, and first/last-page rendering.
""",
        encoding="utf-8",
    )


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    update_note()
    print("Integrated two frequency-domain active NLOS reconstruction papers.")


if __name__ == "__main__":
    main()
