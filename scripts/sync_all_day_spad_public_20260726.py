from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

TITLE = "All-day non-line-of-sight imaging based on Si-SPAD and phase-congruency-based structured ε-regularization"
DOI = "10.1016/j.optlaseng.2026.109919"
KEY = "yinAllDayNLOS2026"
SUMMARY = (
    "Co-designs Si-SPAD detector selection and phase-congruency-based structured ε-regularization for robust active NLOS under extreme daylight; "
    "reports an 18× SBR gain over InGaAs-SPAD capture, 200 m imaging under 94,314 lx, and 4 cm lateral / 1 cm axial resolution."
)


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file missing: {path}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, old: str, new: str) -> None:
    if new != old:
        path.write_text(new, encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")
    else:
        print(f"unchanged {path.relative_to(ROOT)}")


def update_readme() -> None:
    old = read(README)
    text = old
    if TITLE.lower() not in text.lower() and DOI.lower() not in text.lower():
        separator = "|------|-------|----------------|----------------|\n"
        if separator not in text:
            raise SystemExit("Fail-closed: README latest-additions table anchor missing")
        row = (
            f"| 2026 | [{TITLE}](https://doi.org/{DOI}) — Yin et al. | Optics and Lasers in Engineering 2026 | {SUMMARY} |\n"
        )
        text = text.replace(separator, separator + row, 1)

    timeline = (
        "2026 ── Yin et al.: Si-SPAD and phase-congruency regularization enable 200 m all-day active NLOS under 94,314 lx sunlight [Optics and Lasers in Engineering]\n"
    )
    if timeline not in text:
        marker = "2026 ── "
        pos = text.find(marker, text.find("## Milestone Timeline"))
        if pos < 0:
            raise SystemExit("Fail-closed: README 2026 timeline anchor missing")
        text = text[:pos] + timeline + text[pos:]

    write_if_changed(README, old, text)


def update_index() -> None:
    old = read(INDEX)
    text = old
    marker = "const papers=["
    start = text.find(marker)
    end = text.find("];", start)
    if start < 0 or end < 0:
        raise SystemExit("Fail-closed: website paper array missing")
    array = text[start:end]
    added = False
    if TITLE.lower() not in array.lower() and DOI.lower() not in array.lower():
        record = (
            '\n      {cat:"latest active tof spad phasor-field daylight long-range",'
            f'title:"{TITLE}",authors:"Yin et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",'
            f'url:"https://doi.org/{DOI}",key:"{SUMMARY}"}},\n'
        )
        text = text[: start + len(marker)] + record + text[start + len(marker) :]
        added = True

    start = text.find(marker)
    end = text.find("];", start)
    prefix, array, suffix = text[:start], text[start:end], text[end:]
    array = re.sub(r"}(\s*\n\s*)\{cat:", r"},\1{cat:", array)
    text = prefix + array + suffix

    if added:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span>)')
        match = pattern.search(text)
        if not match:
            raise SystemExit("Fail-closed: website tracked-entry counter missing")
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", text, count=1)

    sentence = (
        " Si-SPAD detector modeling and phase-congruency regularization extended active NLOS to 200 m under 94,314 lx daylight."
    )
    if sentence.strip() not in text:
        year_pos = text.find('<div class="tl"><div class="year">2026</div>')
        if year_pos < 0:
            raise SystemExit("Fail-closed: website 2026 timeline missing")
        p_end = text.find("</p></div></div>", year_pos)
        if p_end < 0:
            raise SystemExit("Fail-closed: website 2026 timeline paragraph end missing")
        text = text[:p_end] + sentence + text[p_end:]

    write_if_changed(INDEX, old, text)


def validate() -> None:
    readme = read(README).lower()
    index = read(INDEX).lower()
    active = read(ACTIVE)
    bib = read(BIB).lower()
    assert readme.count(TITLE.lower()) == 1
    assert index.count(TITLE.lower()) == 1
    assert KEY in active
    assert ("{" + KEY.lower() + ",") in bib
    assert DOI.lower() in bib
    print("All-day SPAD public-artifact consistency passed.")


def main() -> None:
    update_readme()
    update_index()
    validate()


if __name__ == "__main__":
    main()
