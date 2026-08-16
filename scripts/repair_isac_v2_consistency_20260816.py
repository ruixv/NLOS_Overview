from pathlib import Path
import re

README = Path("README.md")
CORPUS = Path("data/papers-source.html")
SURVEY = Path("article/5newscenes.tex")
BIB = Path("egbib_merged_20260711.bib")
TEX = Path("bare_jrnl.tex")
NOTE = Path("updates/2026-08-08-isac-nlos-final-venue-citation-trace.md")

papers = [
    {
        "title": "Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",
        "object": '{cat:"latest modality radar rf mmwave isac cellular multipath detection tracking",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al.",year:2026,venue:"32nd International Conference on Telecommunications (ICT 2026), 25–30",url:"https://arxiv.org/abs/2604.07032",key:"Uses 5G/mmWave ISAC hardware and large-surface reflections for fully occluded industrial intrusion sensing; range–Doppler processing and PHD-based tracking improve target persistence and false-alarm robustness beyond the earlier feasibility study."},',
    },
    {
        "title": "Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",
        "object": '{cat:"latest modality radar rf mmwave isac cellular multipath detection",title:"Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",authors:"Tosi et al.",year:2024,venue:"IEEE SPAWC 2024, 331–335",url:"https://doi.org/10.1109/SPAWC60668.2024.10694426",key:"Demonstrates fully NLOS target detection with a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment; CSI processing suppresses TDD-induced spectral replicas and establishes the experimental precursor to the 2026 ICT intrusion-detection and tracking system."},',
    },
]

# Before touching the canonical website corpus, verify that the other public
# artifacts already contain the two works. This repair intentionally closes a
# V2 Paper Explorer regression rather than duplicating survey or bibliography
# content that is already correct.
readme = README.read_text(encoding="utf-8")
survey = SURVEY.read_text(encoding="utf-8")
bib = BIB.read_text(encoding="utf-8")

required = [
    (readme, papers[0]["title"], "README ICT 2026 title"),
    (readme, papers[1]["title"], "README SPAWC 2024 title"),
    (readme, "10.1109/SPAWC60668.2024.10694426", "README SPAWC DOI"),
    (survey, "tosiReliableISACNLOS2026", "survey ICT citation"),
    (survey, "tosiFeasibilityISACNLOS2024", "survey SPAWC citation"),
    (bib, "@inproceedings{tosiReliableISACNLOS2026", "ICT BibTeX key"),
    (bib, "@inproceedings{tosiFeasibilityISACNLOS2024", "SPAWC BibTeX key"),
]
for text, needle, label in required:
    if needle not in text:
        raise SystemExit(f"Refusing unsafe repair: missing {label}: {needle!r}")

corpus = CORPUS.read_text(encoding="utf-8")
anchor = "const papers=["
if anchor not in corpus:
    raise SystemExit("Refusing unsafe repair: canonical papers array anchor not found")

missing = [p for p in papers if f'title:"{p["title"]}"' not in corpus]
if missing:
    insertion = "\n  " + "\n  ".join(p["object"] for p in missing)
    corpus = corpus.replace(anchor, anchor + insertion, 1)

    count_pat = re.compile(r'(<b>)(\d+)(</b><span>tracked latest entries</span>)')
    m = count_pat.search(corpus)
    if not m:
        raise SystemExit("Refusing unsafe repair: tracked-entry counter not found")
    corpus = count_pat.sub(
        lambda x: x.group(1) + str(int(x.group(2)) + len(missing)) + x.group(3),
        corpus,
        count=1,
    )

# Keep the V2 footer synchronized with the current public update date. Do not
# globally replace dates because historical timeline prose may legitimately
# contain earlier dates.
corpus = corpus.replace("Last updated: 15 August 2026", "Last updated: 16 August 2026")

# Postconditions: exactly one paper object per restored record and displayed
# tracked-entry count equals the actual number of paper objects.
for p in papers:
    n = corpus.count(f'title:"{p["title"]}"')
    if n != 1:
        raise SystemExit(f"Canonical corpus must contain exactly one {p['title']!r}; found {n}")

objects = len(re.findall(r'\{cat:"', corpus))
cm = re.search(r'<b>(\d+)</b><span>tracked latest entries</span>', corpus)
if not cm:
    raise SystemExit("Tracked-entry counter disappeared")
displayed = int(cm.group(1))
if displayed != objects:
    raise SystemExit(f"Tracked-entry counter mismatch after repair: displayed={displayed}, objects={objects}")

CORPUS.write_text(corpus, encoding="utf-8")

# The survey prose and citations were already integrated, but the title-note
# snapshot was one day stale relative to the README. Updating this source line
# requires rebuilding the PDF so source and binary remain mutually consistent.
tex = TEX.read_text(encoding="utf-8")
old = "through 15 August 2026."
new = "through 16 August 2026."
if old in tex:
    tex = tex.replace(old, new, 1)
elif new not in tex:
    raise SystemExit("Refusing unsafe repair: survey coverage-date anchor not found")
comment = "% 16 August 2026 consistency audit: restored cellular-ISAC SPAWC/ICT entries to the canonical V2 Paper Explorer and synchronized the survey snapshot date.\n"
if comment.strip() not in tex:
    tex = comment + tex
TEX.write_text(tex, encoding="utf-8")

# Append an explicit audit trail to the original ISAC citation-trace note.
note = NOTE.read_text(encoding="utf-8")
marker = "## 16 August 2026 V2 consistency repair"
if marker not in note:
    note += "\n\n" + marker + "\n\n"
    note += (
        "A later V2 synchronization retained both Tosi et al. works in `README.md`, the development timeline, "
        "`article/5newscenes.tex`, and `egbib_merged_20260711.bib`, but their individual paper objects were no longer "
        "present in the canonical `data/papers-source.html` array used by the Paper Explorer and 3D paper graph. "
        "This repair restores the IEEE SPAWC 2024 feasibility precursor and the ICT 2026 intrusion-detection follow-up "
        "without duplicating survey prose or BibTeX records, updates the tracked-paper counter accordingly, and synchronizes "
        "the V2 footer and survey coverage date to 16 August 2026. The validation workflow rebuilds `bare_jrnl.pdf` and checks "
        "the two citations, bibliography uniqueness, canonical paper count, and rendered PDF before committing the public artifacts.\n"
    )
    NOTE.write_text(note, encoding="utf-8")

print(f"Restored {len(missing)} missing canonical paper object(s); tracked entries={displayed}.")
