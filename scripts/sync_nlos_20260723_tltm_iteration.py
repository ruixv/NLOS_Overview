#!/usr/bin/env python3
"""Fail-closed synchronization of the iterated-TLTM NLOS milestone."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1038/s41467-026-75177-4"
KEY = "sultanIteratingTLTM2026"
MARKER = "% 23 July 2026 citation trace: iterated transient light-transport matrices integrated."


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, repl, label: str, flags: int = 0) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return out


def integrated() -> bool:
    if DOI not in read("README.md"):
        return False
    expected = {
        "README.md": DOI,
        "index.html": DOI,
        "article/2active.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    missing = [path for path, needle in expected.items() if needle not in read(path)]
    if missing:
        raise RuntimeError("Partial iterated-TLTM integration: " + ", ".join(missing))
    return True


def update_readme() -> None:
    text = read("README.md")
    if "**Update run: 23 July 2026.**" not in text:
        raise RuntimeError("Unexpected README update date")

    row = (
        "| 2026 | [Iterating the transient light transport matrix for non-line-of-sight imaging]"
        "(https://doi.org/10.1038/s41467-026-75177-4) — Sultan et al. | "
        "Nature Communications 2026 | Measures the full first-order transient light-transport "
        "matrix with dense relay-wall illumination and a gated 16×16 SPAD array, then independently "
        "focuses virtual illumination and detection inside the hidden scene to recover hidden-to-hidden "
        "TLTM-2. The recovered transport exposes indirect shadows, interreflections, and volumetric "
        "scattering and supports direct/indirect separation, virtual relighting, and dual photography. |"
    )
    text = regex_once(
        text,
        r"(?m)^(\|------\|-------\|----------------\|----------------\|\s*)$",
        lambda m: m.group(1) + "\n" + row,
        "README latest-additions header",
    )

    anchor = (
        "   │     Zhang et al.: D-NeSF — spatiotemporally disentangled neural shadow fields extend "
        "two-bounce NLOS stereo reconstruction from static scenes to moving hidden targets "
        "[ICGIP / Proceedings of SPIE]"
    )
    milestone = (
        "   │     Sultan et al.: iterated transient light transport matrices — full relay-wall TLTM "
        "recovers hidden-to-hidden time-resolved transport for indirect-shadow analysis, relighting, "
        "and dual photography [Nature Communications]"
    )
    text = replace_once(text, anchor, anchor + "\n" + milestone, "README 2026 milestone")
    write("README.md", text)


def update_index() -> None:
    text = read("index.html")
    text = replace_once(
        text,
        '<b>185</b><span>tracked latest entries</span>',
        '<b>186</b><span>tracked latest entries</span>',
        "homepage tracked-paper count",
    )
    if "Updated 23 July 2026 · 190+ papers" not in text:
        raise RuntimeError("Unexpected homepage hero date")
    if "Last updated: 23 July 2026" not in text:
        raise RuntimeError("Unexpected homepage footer date")

    paper = (
        '      {cat:"latest active transient spad array light transport matrix phasor relighting",'
        'title:"Iterating the transient light transport matrix for non-line-of-sight imaging",'
        'authors:"Sultan et al.",year:2026,venue:"Nature Communications 2026",'
        'url:"https://doi.org/10.1038/s41467-026-75177-4",'
        'key:"A dense laser scan and gated 16×16 SPAD array measure the full relay-wall TLTM-1; '
        'independent virtual illumination and detection focus recover hidden-to-hidden TLTM-2 for '
        'indirect-shadow analysis, direct/indirect separation, relighting, and dual photography."},'
    )
    text = regex_once(
        text,
        r"(?m)^(\s*const papers=\[\s*)$",
        lambda m: m.group(1) + "\n" + paper,
        "homepage paper array",
    )

    pattern = r'(<div class="tl"><div class="year">2026</div>.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError("Missing homepage 2026 timeline")
    addition = (
        " Sultan et al. then sampled the full relay-wall transient light-transport matrix and "
        "iterated it into hidden-to-hidden transport, moving active NLOS beyond geometry toward "
        "indirect-shadow analysis, interreflection separation, relighting, and dual photography."
    )
    if "sampled the full relay-wall transient light-transport matrix" in match.group(2):
        raise RuntimeError("Iterated-TLTM timeline already exists")
    text = (
        text[: match.start()]
        + match.group(1)
        + match.group(2).rstrip()
        + addition
        + match.group(3)
        + text[match.end() :]
    )
    write("index.html", text)


def update_active() -> None:
    text = read("article/2active.tex")
    old = (
        "luesiaZeroPhasePhasor2025,marcoVirtualLightTransport2021,liFirstPhotonStamping2022}"
    )
    new = (
        "luesiaZeroPhasePhasor2025,marcoVirtualLightTransport2021,"
        "sultanIteratingTLTM2026,liFirstPhotonStamping2022}"
    )
    text = replace_once(text, old, new, "active-system table citation")

    anchor = (
        "The latter work was formally published at ICCV 2021; the repository therefore uses the "
        "final conference record rather than its earlier arXiv-only label."
    )
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Iterating measured transient light-transport matrices.}\n"
        "Sultan~\\etal~expanded the virtual-transport-matrix idea from a reconstructed "
        "projector--camera operator to a full-dimensional measured first-order transient "
        "light-transport matrix (TLTM-1) between relay-wall illumination and detection "
        "patches~\\cite{sultanIteratingTLTM2026}. A dense laser scan and gated $16\\times16$ "
        "SPAD array sample this matrix, after which phasor-field beamforming independently focuses "
        "virtual illumination and detection within the hidden scene. The resulting hidden-to-hidden "
        "TLTM-2 exposes indirect shadows, interreflections, and volumetric scattering and supports "
        "direct--indirect separation, virtual relighting, and dual photography. This work shifts "
        "active NLOS beyond recovering only geometry: iterating TLTM-$n$ treats the hidden scene as "
        "a synthetic time-of-flight camera whose internal transport can itself be measured "
        "computationally."
    )
    text = replace_once(text, anchor, anchor + paragraph, "iterated-TLTM survey paragraph")
    write("article/2active.tex", text)


def update_master() -> None:
    text = read("bare_jrnl.tex")
    text = regex_once(
        text,
        r"(?m)^%% bare_jrnl\.tex\s*$",
        "%% bare_jrnl.tex\n" + MARKER,
        "master survey header",
    )
    if "through 23 July 2026" not in text:
        raise RuntimeError("Unexpected survey coverage date")
    write("bare_jrnl.tex", text)


def validate() -> None:
    expected = {
        "README.md": (DOI, 1),
        "index.html": (DOI, 1),
        "article/2active.tex": (KEY, 2),
        "bare_jrnl.tex": (MARKER, 1),
    }
    for path, (needle, count) in expected.items():
        actual = read(path).count(needle)
        if actual != count:
            raise RuntimeError(f"{path}: expected {count} occurrences of {needle}, found {actual}")
    if '<b>186</b><span>tracked latest entries</span>' not in read("index.html"):
        raise RuntimeError("Homepage count was not updated")
    if "**Update run: 23 July 2026.**" not in read("README.md"):
        raise RuntimeError("README date changed unexpectedly")
    if "through 23 July 2026" not in read("bare_jrnl.tex"):
        raise RuntimeError("Survey date changed unexpectedly")


def main() -> None:
    if integrated():
        print("Iterated-TLTM NLOS paper already fully integrated")
        return
    update_readme()
    update_index()
    update_active()
    update_master()
    validate()
    print("Iterated-TLTM NLOS paper synchronized across source artifacts")


if __name__ == "__main__":
    main()
