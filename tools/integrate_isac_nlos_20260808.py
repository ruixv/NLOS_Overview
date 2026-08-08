from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

SPAWC_TITLE = "Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave"
ICT_TITLE = "Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware"

SPAWC_README_ROW = "| 2024 | [Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave](https://doi.org/10.1109/SPAWC60668.2024.10694426) — Tosi et al. | IEEE SPAWC 2024, 331–335 | Demonstrates fully NLOS target detection with a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment; CSI processing suppresses TDD-induced spectral replicas and establishes the experimental precursor to the 2026 ICT intrusion-detection and tracking system. |"
ICT_README_ROW = "| 2026 | [Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware](https://arxiv.org/abs/2604.07032) — Tosi et al. | International Conference on Telecommunications (ICT 2026), 25–30 | Uses 5G/mmWave ISAC hardware and large-surface reflections for fully occluded industrial intrusion sensing; range–Doppler processing and PHD-based tracking improve target persistence and false-alarm robustness beyond the earlier feasibility study. |"

SPAWC_OBJECT = '{cat:"latest modality radar rf mmwave isac detection industrial measured",title:"Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",authors:"Tosi et al.",year:2024,venue:"IEEE SPAWC 2024, 331–335",url:"https://doi.org/10.1109/SPAWC60668.2024.10694426",key:"Commercial 27.4-GHz 5G/mmWave ISAC hardware detects fully NLOS targets in a factory-like environment; CSI processing mitigates TDD-induced spectral replicas and establishes the experimental precursor to the 2026 ICT tracking system."},'
ICT_OBJECT = '{cat:"latest modality radar rf mmwave isac detection tracking industrial measured",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al.",year:2026,venue:"ICT 2026, 25–30",url:"https://arxiv.org/abs/2604.07032",key:"5G/mmWave ISAC hardware uses large-surface reflections, range–Doppler processing, and PHD-based tracking for reliable fully NLOS intrusion detection in an industrial environment."},'

SPAWC_BIB = r'''@inproceedings{tosiFeasibilityISACNLOS2024,
  author = {Tosi, Paolo and Henninger, Marcus and Giroto de Oliveira, Lucas and Mandelli, Silvio},
  title = {Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave},
  booktitle = {2024 IEEE 25th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)},
  pages = {331--335},
  year = {2024},
  doi = {10.1109/SPAWC60668.2024.10694426},
  url = {https://doi.org/10.1109/SPAWC60668.2024.10694426}
}'''

ICT_BIB = r'''@inproceedings{tosiReliableISACNLOS2026,
  author = {Tosi, Paolo and Bauhofer, Maximilian and Henninger, Marcus and Schmalen, Laurent and Mandelli, Silvio},
  title = {Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware},
  booktitle = {32nd International Conference on Telecommunications (ICT 2026)},
  pages = {25--30},
  year = {2026},
  address = {Thessaloniki, Greece},
  month = {May},
  note = {Also available as arXiv:2604.07032},
  url = {https://arxiv.org/abs/2604.07032}
}'''

SURVEY_PARAGRAPH = r'''\vspace{0.8mm}
\noindent \textbf{Cellular ISAC hardware for NLOS sensing.}
A complementary 5G/6G ISAC trajectory asks whether communication hardware can use multipath as an around-corner sensor rather than treating it only as a channel impairment. Tosi~\etal~first demonstrated the feasibility of NLOS target detection with a 27.4~GHz commercial mmWave ISAC proof-of-concept, including channel-state-information processing that suppresses spectral replicas caused by time-division-duplex gaps~\cite{tosiFeasibilityISACNLOS2024}. The later ICT study moved from feasibility to reliable intrusion monitoring of fully occluded moving targets, adding range--Doppler detection and probability-hypothesis-density filtering for tracking and false-alarm rejection in an industrial testbed~\cite{tosiReliableISACNLOS2026}. Together, these works connect radar NLOS with standards-compatible cellular infrastructure and show a deployment path in which communication radios become opportunistic hidden-region sensors.'''


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one exact anchor, found {n}")
    return text.replace(old, new, 1)


def remove_bib_entries_containing(text, needles):
    lower_needles = [n.lower() for n in needles]
    out = []
    pos = 0
    removed = 0
    while True:
        at = text.find('@', pos)
        if at < 0:
            out.append(text[pos:])
            break
        brace = text.find('{', at)
        if brace < 0:
            out.append(text[pos:])
            break
        depth = 0
        end = None
        for i in range(brace, len(text)):
            c = text[i]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise RuntimeError("Malformed BibTeX entry while scanning")
        entry = text[at:end]
        if any(n in entry.lower() for n in lower_needles):
            out.append(text[pos:at])
            removed += 1
        else:
            out.append(text[pos:end])
        pos = end
    return ''.join(out), removed


def patch_readme():
    path = "README.md"
    text = read(path)
    # Correct all stale/public instances of the ICT record.
    row_re = re.compile(r'^\|\s*2026\s*\|\s*\[Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware\]\(https://arxiv\.org/abs/2604\.07032\)\s*—\s*Tosi et al\.\s*\|.*?\|.*?\|$', re.M)
    text, n = row_re.subn(ICT_README_ROW, text)
    if n < 1:
        raise RuntimeError("README: ICT row not found")

    # Add the missing SPAWC paper beside the existing ICT lineage in the detailed table.
    if SPAWC_README_ROW not in text:
        idx = text.find(ICT_README_ROW)
        if idx < 0:
            raise RuntimeError("README: corrected ICT row anchor missing")
        text = text[:idx] + SPAWC_README_ROW + "\n" + text[idx:]

    # Ensure it is also visible in Latest Additions, not only in the detailed modality table.
    latest_start = text.find("## Latest Additions")
    if latest_start < 0:
        raise RuntimeError("README: Latest Additions heading missing")
    latest_end = text.find("\n---", latest_start)
    if latest_end < 0:
        raise RuntimeError("README: Latest Additions terminator missing")
    latest = text[latest_start:latest_end]
    if SPAWC_TITLE not in latest:
        header = "|------|-------|----------------|----------------|"
        hpos = text.find(header, latest_start, latest_end)
        if hpos < 0:
            raise RuntimeError("README: Latest Additions table header missing")
        insert = hpos + len(header)
        text = text[:insert] + "\n" + SPAWC_README_ROW + text[insert:]

    # Historical trajectory: connect 2024 feasibility to the 2026 follow-up.
    tl_2024 = "    2024 ── RFlect: practical poles and curved/composite reflectors support hidden-shape mmWave imaging beyond planar-wall assumptions [MobiCom]"
    if "Tosi et al.: 27.4-GHz 5G/mmWave ISAC" not in text:
        text = replace_once(text, tl_2024, tl_2024 + "\n   │     Tosi et al.: 27.4-GHz 5G/mmWave ISAC proves fully NLOS target detection with TDD-artifact-aware CSI processing [IEEE SPAWC]", "README 2024 timeline")
    if "ICT follow-up: industrial 5G/mmWave ISAC" not in text:
        matches = list(re.finditer(r'^2026 ──.*$', text, re.M))
        if not matches:
            raise RuntimeError("README: no 2026 timeline anchor")
        m = matches[0]
        line = m.group(0)
        text = text[:m.start()] + line + "\n   │     ICT follow-up: industrial 5G/mmWave ISAC adds range--Doppler detection and PHD tracking for reliable fully NLOS intrusion monitoring [ICT 2026]" + text[m.end():]

    write(path, text)


def patch_index():
    path = "index.html"
    text = read(path)
    text = replace_once(text, '<div class="stat"><b>267</b><span>tracked latest entries</span></div>', '<div class="stat"><b>268</b><span>tracked latest entries</span></div>', "index explorer count")
    if "Last updated: 6 August 2026" in text:
        text = text.replace("Last updated: 6 August 2026", "Last updated: 8 August 2026", 1)

    obj_re = re.compile(r'\{cat:"latest modality",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al\.",year:2026,venue:"arXiv 2026",url:"https://arxiv\.org/abs/2604\.07032",key:"[^"]*"\},')
    text, n = obj_re.subn(ICT_OBJECT, text)
    if n != 1:
        raise RuntimeError(f"index: stale ICT object expected once, found {n}")
    text = text.replace(ICT_OBJECT, SPAWC_OBJECT + "\n      " + ICT_OBJECT, 1)

    def append_timeline(t, year, sentence, sentinel):
        if sentinel in t:
            return t
        pattern = re.compile(r'(<div class="tl"><div class="year">' + str(year) + r'</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
        m = pattern.search(t)
        if not m:
            raise RuntimeError(f"index: timeline {year} block missing")
        middle = m.group(2).rstrip()
        replacement = m.group(1) + middle + " " + sentence + m.group(3)
        return t[:m.start()] + replacement + t[m.end():]

    text = append_timeline(text, 2024,
        "Tosi et al. also demonstrated fully NLOS target detection with a commercial 27.4-GHz 5G/mmWave ISAC prototype, compensating TDD-induced spectral replicas in the sensing channel.",
        "commercial 27.4-GHz 5G/mmWave ISAC prototype")
    text = append_timeline(text, 2026,
        "The ICT follow-up converted that cellular-ISAC feasibility result into industrial NLOS intrusion monitoring with explicit range–Doppler detection, PHD tracking, and false-alarm stress tests.",
        "cellular-ISAC feasibility result")

    if text.count(f'title:"{SPAWC_TITLE}"') != 1:
        raise RuntimeError("index: SPAWC paper object is not unique")
    if text.count(f'title:"{ICT_TITLE}"') != 1:
        raise RuntimeError("index: ICT paper object is not unique")
    write(path, text)


def patch_survey():
    path = "article/5newscenes.tex"
    text = read(path)
    if "tosiFeasibilityISACNLOS2024" not in text:
        anchor = "The radar approach is complementary to optical NLOS: it operates through walls and in total darkness, but at lower spatial resolution than optical methods."
        text = replace_once(text, anchor, anchor + "\n\n" + SURVEY_PARAGRAPH, "survey radar insertion")
    write(path, text)

    path = "bare_jrnl.tex"
    text = read(path)
    comment = "% 8 August 2026 ISAC citation trace: SPAWC 2024 cellular-mmWave NLOS precursor integrated and ICT 2026 follow-up corrected to its final venue."
    if comment not in text:
        first = "% 8 August 2026 forward-citation trace: RF/mmWave milestone lineage, second-order acoustic diffraction, and four final-venue corrections synchronized."
        text = replace_once(text, first, first + "\n" + comment, "bare_jrnl maintenance comment")
    write(path, text)


def patch_bibliography():
    merged = ROOT / "egbib_merged_20260711.bib"
    if not merged.exists():
        raise RuntimeError("Merged bibliography missing")

    # Upgrade any existing canonical source record for the ICT paper.
    found_source = False
    for p in sorted(ROOT.glob("*.bib")):
        if p.name in {merged.name, "egbib_20260808_isac_updates.bib"}:
            continue
        text = p.read_text(encoding="utf-8")
        if ICT_TITLE.lower() in text.lower():
            text, _ = remove_bib_entries_containing(text, [ICT_TITLE, SPAWC_TITLE])
            text = text.rstrip() + "\n\n" + ICT_BIB + "\n"
            p.write_text(text, encoding="utf-8")
            found_source = True

    fragment = SPAWC_BIB + "\n"
    if not found_source:
        fragment += "\n" + ICT_BIB + "\n"
    (ROOT / "egbib_20260808_isac_updates.bib").write_text(fragment, encoding="utf-8")

    text = merged.read_text(encoding="utf-8")
    text, _ = remove_bib_entries_containing(text, [ICT_TITLE, SPAWC_TITLE])
    text = text.rstrip() + "\n\n" + SPAWC_BIB + "\n\n" + ICT_BIB + "\n"
    merged.write_text(text, encoding="utf-8")


def patch_update_note():
    path = ROOT / "updates/2026-08-08-isac-nlos-final-venue-citation-trace.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    old = "Because the public-facing files are large and the available repository interface requires full-file replacement, this run does **not** overwrite README.md, index.html, article/5newscenes.tex, the merged bibliography, or bare_jrnl.pdf. The exact bounded changes below should be applied together and followed by a LaTeX rebuild so no public artifact is left inconsistent."
    new = "**Integration completed on 8 August 2026.** The bounded changes described below were applied to README.md, index.html, article/5newscenes.tex, bare_jrnl.tex, and the bibliography, followed by a clean LaTeX/BibTeX rebuild and PDF consistency checks. The note is retained as the provenance record for the cellular-ISAC citation trace."
    if old in text:
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


def validate_sources():
    readme = read("README.md")
    index = read("index.html")
    survey = read("article/5newscenes.tex")
    bare = read("bare_jrnl.tex")
    bib = read("egbib_merged_20260711.bib")
    assert SPAWC_TITLE in readme and ICT_TITLE in readme
    assert "ICT 2026" in readme and "IEEE SPAWC 2024" in readme
    assert index.count(f'title:"{SPAWC_TITLE}"') == 1
    assert index.count(f'title:"{ICT_TITLE}"') == 1
    assert '<div class="stat"><b>268</b><span>tracked latest entries</span></div>' in index
    assert "tosiFeasibilityISACNLOS2024" in survey and "tosiReliableISACNLOS2026" in survey
    assert "egbib_merged_20260711" in bare
    assert bib.count("tosiFeasibilityISACNLOS2024") == 1
    assert bib.count("tosiReliableISACNLOS2026") == 1
    assert "10.1109/SPAWC60668.2024.10694426" in bib
    # No unverified DOI is attached to the ICT paper.
    ict_entry = bib[bib.index("tosiReliableISACNLOS2026"):]
    ict_entry = ict_entry[:ict_entry.find("\n}") + 2]
    assert "doi =" not in ict_entry.lower()


if __name__ == "__main__":
    patch_readme()
    patch_index()
    patch_survey()
    patch_bibliography()
    patch_update_note()
    validate_sources()
    print("ISAC NLOS source integration complete and source-level checks passed.")
