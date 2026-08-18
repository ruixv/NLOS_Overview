#!/usr/bin/env python3
"""Integrate the verified IEEE Access acoustic-NLOS liveness paper.

The work was found in the acoustic NLOS citation lineage after source-localization
and ANLOS-R material-recognition papers. It is a final IEEE Access publication,
not an arXiv-only record.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = "cetinAcousticLivenessNLOS2026"
DOI = "10.1109/ACCESS.2026.3692353"
URL = f"https://doi.org/{DOI}"
TITLE = "Comparative Analysis of Deep Latent Representation and Statistical Fusion Strategies Under Model Inductive Bias in Multichannel Acoustic Live Subject Detection"


def read(path: str | Path) -> str:
    p = path if isinstance(path, Path) else ROOT / path
    return p.read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    p = path if isinstance(path, Path) else ROOT / path
    p.write_text(text, encoding="utf-8")


def insert_after_line(text: str, needle: str, addition: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if not matches:
        raise RuntimeError(f"{label}: anchor not found: {needle}")
    i = matches[-1]
    lines.insert(i + 1, addition if addition.endswith("\n") else addition + "\n")
    return "".join(lines)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    row = (
        f"| 2026 | [{TITLE}]({URL}) — Cetin et al. | IEEE Access 14, 73343–73356 (2026) | "
        "Extends acoustic NLOS semantic sensing from hidden material recognition to live-human versus inanimate-object discrimination in cluttered scenes; compares raw eight-channel measurements, arithmetic averaging, and convolutional-transformer latent fusion across deep and classical classifiers, showing that the best fusion strategy depends strongly on model inductive bias. |\n"
    )
    if DOI not in text:
        text = insert_after_line(text, "Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net", row, "README acoustic liveness row")

    timeline = (
        "   │     Cetin et al.: multichannel wall-mediated echoes extend acoustic NLOS semantics from hidden-material recognition to live-human versus debris discrimination, exposing strong representation–classifier inductive-bias interactions [IEEE Access]\n"
    )
    if "live-human versus debris discrimination" not in text:
        text = insert_after_line(text, "Alakuş and Türkoğlu: wall-mediated chirp echoes", timeline, "README acoustic semantic timeline")

    text = text.replace("**Update run: 17 August 2026.**", "**Update run: 18 August 2026.**", 1)
    write(path, text)


def update_website_source() -> None:
    path = "data/papers-source.html"
    text = read(path)
    paper_obj = (
        '      {cat:"latest modality acoustic learning semantic detection search-rescue",'
        f'title:"{TITLE}",authors:"Cetin et al.",year:2026,venue:"IEEE Access 14, 73343–73356 (2026)",'
        f'url:"{URL}",'
        'key:"Uses wall-mediated multichannel acoustic echoes for live-human versus inanimate-object discrimination in cluttered NLOS scenes, and compares raw, arithmetic-mean, and convolutional-transformer latent fusion to expose strong interactions between representation choice and classifier inductive bias."},\n'
    )
    if DOI not in text:
        text = insert_after_line(text, "Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net", paper_obj, "website acoustic liveness paper")

    if "acoustic NLOS liveness detection" not in text:
        pattern = re.compile(
            r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            flags=re.S,
        )
        m = pattern.search(text)
        if not m:
            raise RuntimeError("website 2026 timeline block missing")
        sentence = (
            " Cetin et al. added acoustic NLOS liveness detection for search-and-rescue: multichannel wall-mediated echoes distinguish live humans from inanimate clutter while a common evaluation across raw, averaged, and convolutional-transformer latent representations exposes strong fusion–classifier inductive-bias interactions."
        )
        text = text[:m.start(2)] + m.group(2) + sentence + text[m.end(2):]

    text = text.replace("Updated 17 August 2026", "Updated 18 August 2026", 1)
    text = text.replace("Last updated: 17 August 2026", "Last updated: 18 August 2026", 1)

    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.S)
    if not array:
        raise RuntimeError("website paper array missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    text, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError("website tracked-count badge missing")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    text = re.sub(r"Updated 17 Aug 2026", "Updated 18 Aug 2026", text, count=1)
    text = re.sub(r"Updated 17 August 2026", "Updated 18 August 2026", text, count=1)
    text = re.sub(r"Last updated: 17 August 2026", "Last updated: 18 August 2026", text, count=1)
    write(path, text)


def update_acoustic_survey() -> None:
    path = "article/5newscenes.tex"
    text = read(path)
    if KEY not in text:
        anchor = (
            "Together, the two works extend acoustic NLOS from localization and geometry toward dataset-driven material-aware environmental perception."
        )
        if anchor not in text:
            raise RuntimeError("acoustic material-recognition survey anchor missing")
        addition = r'''

\vspace{0.8mm}
\noindent \textbf{Acoustic liveness detection in cluttered NLOS scenes.}
Cetin~\etal~extend acoustic NLOS semantic sensing from hidden-source localization and material recognition to live-human versus inanimate-object discrimination for search-and-rescue settings~\cite{cetinAcousticLivenessNLOS2026}. Their blocked-path multichannel setup measures wall-mediated echoes from hidden people and clutter, and compares raw eight-channel signals, arithmetic channel averaging, and a convolutional--transformer autoencoder latent representation across convolutional, recurrent, and classical ensemble classifiers. The results expose a representation--model interaction: fusion that suppresses apparently redundant signal structure can improve one classifier while removing local phase/temporal cues needed by another. In the acoustic NLOS trajectory, this work therefore follows relay-free/source-localization and ANLOS-R material recognition with a task-oriented liveness branch, shifting evaluation from recovering hidden geometry or material labels toward deciding whether an occluded return corresponds to a living person or debris.'''
        text = text.replace(anchor, anchor + addition, 1)
    write(path, text)


def merge_bibliography() -> None:
    path = "egbib_merged_20260711.bib"
    text = read(path)
    lower = text.lower()
    if KEY.lower() in lower:
        if DOI.lower() not in lower:
            raise RuntimeError("BibTeX key exists without expected DOI")
        return
    if DOI.lower() in lower:
        raise RuntimeError("DOI already exists under another BibTeX key")

    staging = ROOT / "egbib_20260818_acoustic_liveness_gap.bib"
    if staging.exists():
        entry = staging.read_text(encoding="utf-8").strip()
    else:
        entry = r'''@article{cetinAcousticLivenessNLOS2026,
  author = {Cetin, Yunus Emre and Nergiz, Mehmet Ercan and Olgun, Nevzat and Calisan, Mucahit and Dogan, Ferdi and G{\"u}rg{\"o}ze, G{\"u}rkan and Turkoglu, Ibrahim},
  title = {Comparative Analysis of Deep Latent Representation and Statistical Fusion Strategies Under Model Inductive Bias in Multichannel Acoustic Live Subject Detection},
  journal = {IEEE Access},
  volume = {14},
  pages = {73343--73356},
  year = {2026},
  doi = {10.1109/ACCESS.2026.3692353},
  url = {https://doi.org/10.1109/ACCESS.2026.3692353}
}'''.strip()
    text = text.rstrip() + "\n\n" + entry + "\n"
    write(path, text)


def update_master() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    text = text.replace(
        "extends coverage to include significant advances from 2022 through 17 August 2026.",
        "extends coverage to include significant advances from 2022 through 18 August 2026.",
        1,
    )
    marker = "% 18 August 2026 acoustic citation trace: multichannel acoustic NLOS liveness detection synchronized after ANLOS-R material sensing.\n"
    if marker not in text:
        text = marker + text
    write(path, text)


def update_note_and_cleanup() -> None:
    note = ROOT / "updates/2026-08-18-acoustic-liveness-detection-gap.md"
    if note.exists():
        text = note.read_text(encoding="utf-8")
        status = "\n\n## Integration status\n\nSource integration is complete once this script's guarded build passes; the public PDF must only be committed after the clean LaTeX/BibTeX, citation, semantic-text, and render checks succeed.\n"
        if "## Integration status" not in text:
            text = text.rstrip() + status
        note.write_text(text, encoding="utf-8")
    staging = ROOT / "egbib_20260818_acoustic_liveness_gap.bib"
    if staging.exists():
        staging.unlink()


def validate() -> None:
    readme = read("README.md")
    website = read("data/papers-source.html")
    survey = read("article/5newscenes.tex")
    bib = read("egbib_merged_20260711.bib")
    master = read("bare_jrnl.tex")
    for name, text in (("README", readme), ("website", website), ("bib", bib)):
        if DOI not in text:
            raise RuntimeError(f"{name} missing DOI {DOI}")
    if survey.count(KEY) != 1:
        raise RuntimeError(f"survey citation count for {KEY}: {survey.count(KEY)}")
    if bib.lower().count("{" + KEY.lower() + ",") != 1:
        raise RuntimeError("BibTeX key is not unique")
    if bib.lower().count(DOI.lower()) != 2:  # DOI field + DOI URL in the canonical entry
        raise RuntimeError("BibTeX DOI metadata is not unique/canonical")
    if "**Update run: 18 August 2026.**" not in readme:
        raise RuntimeError("README update date not synchronized")
    if "18 August 2026" not in website:
        raise RuntimeError("website date not synchronized")
    if "through 18 August 2026." not in master:
        raise RuntimeError("survey snapshot date not synchronized")


def main() -> None:
    update_readme()
    update_website_source()
    update_index()
    update_acoustic_survey()
    merge_bibliography()
    update_master()
    update_note_and_cleanup()
    validate()
    print("Integrated IEEE Access acoustic-NLOS liveness paper.")


if __name__ == "__main__":
    main()
