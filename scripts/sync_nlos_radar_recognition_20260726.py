from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
NEWSCENES = ROOT / "article" / "5newscenes.tex"
LEARNING = ROOT / "article" / "4datadriven.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

PAPERS = [
    {
        "title": "Non-Line-of-Sight Target Recognition Method Based on Multi-Scale Feature Fusion",
        "authors_short": "Zeng et al.",
        "year": 2026,
        "venue": "Journal of Signal Processing 2026",
        "doi": "10.12466/xhcl.2026.03.006",
        "key": "zengMultipathFeatureFusionNLOS2026",
        "cat": "latest modality radar rf recognition semantic measured multipath",
        "summary": "Uses a measured 15 GHz stepped-frequency radar, adaptive multi-scale convolutions and attention to fuse salient multipath and local-scattering cues, classifying four hidden target types with 99.6% accuracy; this is semantic recognition rather than hidden-shape reconstruction.",
    },
    {
        "title": "Multipath Contrastive Learning for Non-line-of-sight Human Activity Recognition Using an Ultrawideband Radar",
        "authors_short": "Zhong et al.",
        "year": 2026,
        "venue": "Journal of Radars 2026 (Online First)",
        "doi": "10.12000/JR25241",
        "key": "zhongMultipathContrastiveNLOS2026",
        "cat": "latest modality radar rf recognition activity self-supervised contrastive measured",
        "summary": "MuPhyCoNet treats separated multipath time-frequency views as natural contrastive positives and adds observation/prediction physics constraints; on 19,500 measured UWB-radar spectrograms it reaches 94.32% six-action accuracy with only 10% labels.",
    },
]

BIB_ENTRIES = r'''
@article{zengMultipathFeatureFusionNLOS2026,
  author = {Zeng, Xiaolu and Yang, Yifei and Zhao, Han and Zhong, Shichao and Yang, Xiaopeng},
  title = {Non-Line-of-Sight Target Recognition Method Based on Multi-Scale Feature Fusion},
  journal = {Journal of Signal Processing},
  volume = {42},
  number = {3},
  pages = {357--370},
  year = {2026},
  doi = {10.12466/xhcl.2026.03.006},
  url = {https://doi.org/10.12466/xhcl.2026.03.006}
}

@article{zhongMultipathContrastiveNLOS2026,
  author = {Zhong, Xiaoling and Zhou, Junlin and Jia, Yong and Zhu, Qingxi and Yao, Guangle and Yi, Shi},
  title = {Multipath Contrastive Learning for Non-line-of-sight Human Activity Recognition Using an Ultrawideband Radar},
  journal = {Journal of Radars},
  year = {2026},
  note = {Online First, available 28 March 2026},
  doi = {10.12000/JR25241},
  url = {https://doi.org/10.12000/JR25241}
}
'''.strip()


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file missing: {path}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, old: str, new: str) -> None:
    if old != new:
        path.write_text(new, encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")
    else:
        print(f"unchanged {path.relative_to(ROOT)}")


def insert_once(text: str, needle: str, addition: str, label: str, before: bool = False) -> str:
    if addition.strip() in text:
        return text
    pos = text.find(needle)
    if pos < 0:
        raise SystemExit(f"Fail-closed: anchor missing for {label}: {needle!r}")
    if before:
        return text[:pos] + addition + text[pos:]
    end = pos + len(needle)
    return text[:end] + addition + text[end:]


def update_readme() -> None:
    old = read(README)
    text = old
    header = "|------|-------|----------------|----------------|\n"
    rows = ""
    for p in PAPERS:
        if p["title"].lower() in text.lower() or p["doi"].lower() in text.lower():
            continue
        rows += (
            f'| {p["year"]} | [{p["title"]}](https://doi.org/{p["doi"]}) — {p["authors_short"]} '
            f'| {p["venue"]} | {p["summary"]} |\n'
        )
    if rows:
        text = insert_once(text, header, rows, "README latest additions")

    text = re.sub(r"\*\*Update run: \d{1,2} July 2026\.\*\*", "**Update run: 26 July 2026.**", text, count=1)
    timeline = (
        "    │     Zeng et al.: measured 15 GHz multipath feature fusion recognizes four hidden target classes from path and scattering structure [Journal of Signal Processing]\n"
        "    │     Zhong et al.: physics-guided cross-path contrastive learning recognizes six hidden human activities from UWB radar with only 10% labels [Journal of Radars, Online First]\n"
    )
    if "physics-guided cross-path contrastive learning recognizes six hidden human activities" not in text:
        text = insert_once(
            text,
            "    │     Chen et al.: range-migration and 121 GHz holographic operators",
            timeline,
            "README 2026 radar recognition timeline",
            before=True,
        )
    write_if_changed(README, old, text)


def js_record(p: dict) -> str:
    def esc(value: str) -> str:
        return value.replace("\\", "\\\\").replace('"', '\\"')
    return (
        f'      {{cat:"{esc(p["cat"])}",title:"{esc(p["title"])}",authors:"{esc(p["authors_short"])}",'
        f'year:{p["year"]},venue:"{esc(p["venue"])}",url:"https://doi.org/{p["doi"]}",key:"{esc(p["summary"])}"}},\n'
    )


def update_index() -> None:
    old = read(INDEX)
    text = old
    marker = "const papers=["
    pos = text.find(marker)
    if pos < 0:
        raise SystemExit("Fail-closed: website paper-array anchor missing")
    array_end = text.find("];", pos)
    if array_end < 0:
        raise SystemExit("Fail-closed: website paper-array end missing")
    arr = text[pos:array_end]
    records = ""
    added = 0
    for p in PAPERS:
        if p["title"].lower() in arr.lower() or p["doi"].lower() in arr.lower():
            continue
        records += js_record(p)
        added += 1
    if records:
        insert_pos = pos + len(marker)
        text = text[:insert_pos] + "\n" + records + text[insert_pos:]

    pos = text.find(marker)
    array_end = text.find("];", pos)
    prefix, arr, suffix = text[:pos], text[pos:array_end], text[array_end:]
    arr = re.sub(r"}(\s*\n\s*)\{cat:", r"},\1{cat:", arr)
    text = prefix + arr + suffix

    if added:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span>)')
        m = pattern.search(text)
        if not m:
            raise SystemExit("Fail-closed: tracked-entry counter missing")
        text = pattern.sub(lambda x: f"{x.group(1)}{int(x.group(2)) + added}{x.group(3)}", text, count=1)

    text = text.replace("Last updated: 25 July 2026", "Last updated: 26 July 2026")
    text = text.replace("Updated 25 July 2026", "Updated 26 July 2026")

    sentence = (
        " Measured multipath-radar learning also expanded the semantic branch: adaptive multi-scale fusion classified four hidden target types from 15 GHz SFCW returns, while physics-guided cross-path contrastive learning recognized six hidden human activities from UWB radar with limited labels."
    )
    if "Measured multipath-radar learning also expanded the semantic branch" not in text:
        year_start = text.find('<div class="tl"><div class="year">2026</div>')
        if year_start < 0:
            raise SystemExit("Fail-closed: website 2026 timeline missing")
        p_end = text.find("</p></div></div>", year_start)
        if p_end < 0:
            raise SystemExit("Fail-closed: website 2026 timeline paragraph end missing")
        text = text[:p_end] + sentence + text[p_end:]
    write_if_changed(INDEX, old, text)


def update_newscenes() -> None:
    old = read(NEWSCENES)
    text = old
    para = r'''
\vspace{0.8mm}
\noindent \textbf{Measured multipath radar recognition and activity understanding.}
Radar NLOS can support semantic decisions even when the measurements are too sparse for hidden-shape reconstruction. Zeng~\etal~used a 15~GHz stepped-frequency system and an adaptive multi-scale residual network to combine fine high-amplitude single-path cues with global multipath structure and attention-weighted local scattering features~\cite{zengMultipathFeatureFusionNLOS2026}. Measured concrete- and wood-wall experiments distinguish pedestrians, weapon-carrying human models, quadrotor drones, and tank models with 99.6\% accuracy. Zhong~\etal~then treated separated UWB-radar propagation paths as natural multiview positives for self-supervised contrastive learning~\cite{zhongMultipathContrastiveNLOS2026}. MuPhyCoNet aligns learned features with observation- and prediction-level physical quantities, reaching 94.32\% six-action accuracy with only 10\% labels on 19,500 measured spectrograms. These studies extend around-corner RF from detection and localization toward target identity and human activity, but should remain categorized as semantic sensing rather than full 2D/3D imaging.

'''
    anchor = "Tornielli Bellini~\\etal~push reflector-assisted RF NLOS imaging"
    if "Measured multipath radar recognition and activity understanding" not in text:
        text = insert_once(text, anchor, para, "radar semantic sensing paragraph", before=True)
    write_if_changed(NEWSCENES, old, text)


def update_learning() -> None:
    old = read(LEARNING)
    text = old
    para = r'''
\vspace{0.8mm}
\noindent \textbf{Physics-informed semantic learning from multipath radar.}
The semantic NLOS trajectory is not limited to optical relay-wall images. Zeng~\etal~fuse local scattering and global multipath structure with adaptive convolution scales for measured hidden-target classification~\cite{zengMultipathFeatureFusionNLOS2026}, whereas Zhong~\etal~use separated radar paths as physically meaningful contrastive views and impose consistency between observed and regressed motion quantities~\cite{zhongMultipathContrastiveNLOS2026}. The latter achieves strong low-label human-activity recognition, illustrating how propagation-path structure can replace generic image augmentations in self-supervised NLOS representation learning.

'''
    anchor = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Network combined with physical models}"
    if "Physics-informed semantic learning from multipath radar" not in text:
        text = insert_once(text, anchor, para, "radar semantic learning paragraph", before=True)
    write_if_changed(LEARNING, old, text)


def update_master() -> None:
    old = read(MASTER)
    marker = "% 26 July 2026 citation trace: measured multipath radar target and activity recognition synchronized.\n"
    text = old if marker in old else old.replace("%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, 1)
    write_if_changed(MASTER, old, text)


def update_bib() -> None:
    old = read(BIB)
    text = old.rstrip() + "\n"
    for p in PAPERS:
        key_token = "{" + p["key"] + ","
        if key_token.lower() in text.lower():
            continue
        if p["doi"].lower() in text.lower():
            raise SystemExit(f"Fail-closed: DOI already exists under another key: {p['doi']}")
        block = re.search(r"@\w+\{" + re.escape(p["key"]) + r",.*?\n\}", BIB_ENTRIES, re.S)
        if not block:
            raise SystemExit(f"Internal BibTeX block missing: {p['key']}")
        text += "\n" + block.group(0).strip() + "\n"
    write_if_changed(BIB, old, text)


def validate() -> None:
    readme = read(README).lower()
    index = read(INDEX).lower()
    newscenes = read(NEWSCENES)
    learning = read(LEARNING)
    bib = read(BIB).lower()
    for p in PAPERS:
        title = p["title"].lower()
        doi = p["doi"].lower()
        if readme.count(title) != 1:
            raise SystemExit(f"README title count is not one: {p['title']}")
        if index.count(title) != 1:
            raise SystemExit(f"index title count is not one: {p['title']}")
        if bib.count(doi) != 1:
            raise SystemExit(f"bibliography DOI count is not one: {p['doi']}")
        if ("{" + p["key"].lower() + ",") not in bib:
            raise SystemExit(f"bibliography key missing: {p['key']}")
        if p["key"] not in newscenes:
            raise SystemExit(f"new-scenes survey citation missing: {p['key']}")
        if p["key"] not in learning:
            raise SystemExit(f"learning survey citation missing: {p['key']}")
    print("Cross-artifact radar-recognition validation passed.")


def main() -> None:
    update_readme()
    update_index()
    update_newscenes()
    update_learning()
    update_master()
    update_bib()
    validate()


if __name__ == "__main__":
    main()
