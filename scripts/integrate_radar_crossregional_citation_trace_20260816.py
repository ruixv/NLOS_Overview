from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Building Corner and NLOS Target Parameter Estimation Based on Diffraction Signal Utilization",
        "key": "yuDiffractionCornerNLOS2025",
        "year": 2025,
        "authors": "Yu et al.",
        "venue": "IEEE FUSION 2025, 1–6",
        "url": "https://doi.org/10.23919/FUSION65864.2025.11124177",
        "cat": "latest modality radar rf uwb diffraction multipath localization building-layout unknown-geometry",
        "summary": "Uses electromagnetic corner-diffraction returns to estimate building-corner and hidden-target parameters, extending diffraction-based UWB NLOS localization beyond the earlier assumption that corner geometry is already known.",
    },
    {
        "title": "Multipath Ghost Correlation-Based NLOS Target Localization and Building Layuot Estimation",
        "key": "weiGhostCorrelationNLOS2025",
        "year": 2025,
        "authors": "Wei et al.",
        "venue": "IEEE EUSIPCO 2025, 2247–2251",
        "url": "https://doi.org/10.23919/EUSIPCO63237.2025.11226331",
        "cat": "latest modality radar rf multipath ghost-correlation localization building-layout unknown-geometry",
        "summary": "Separates multipath with Range–Doppler features, estimates DOA and ghost positions with IAA, and spatially matches the ghosts to candidate target and wall parameters for joint NLOS localization and building-layout estimation.",
    },
    {
        "title": "A Cross-Regional NLOS Target Localization Method Based on Joint Multipath GLRT",
        "key": "yuCrossRegionalGLRTNLOS2026",
        "year": 2026,
        "authors": "Yu et al.",
        "venue": "IEEE IGARSS 2026, Paper 2579",
        "url": "https://2026.ieeeigarss.org/view_paper.php?PaperNum=2579&SessionID=1399",
        "cat": "latest modality radar rf multipath glrt localization cross-regional",
        "summary": "A newly presented IGARSS 2026 radar NLOS localization work centered on a joint multipath GLRT for cross-regional target localization; the official program verifies the paper and presentation, while no proceedings DOI was indexed at this update.",
    },
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:160]}")


# README: add three verified missing radar papers without duplicating existing entries.
readme = read("README.md")
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README latest table")
rows = []
for p in PAPERS:
    if p["title"] not in readme:
        rows.append(
            f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["summary"]} |\n'
        )
if rows:
    readme = readme.replace(header, header + "".join(rows), 1)

if "Yu et al.: diffraction-signal utilization estimates building-corner" not in readme:
    anchor = "   │     Zhu et al.: weak-reflector 3-D environmental perception is coupled to path-oriented NLOS moving-target reconstruction [IEEE TAES]\n"
    require(readme, anchor, "README radar timeline")
    addition = (
        "   │     Yu et al.: diffraction-signal utilization estimates building-corner and hidden-target parameters, while Wei et al. correlate multipath ghosts with wall geometry for joint target/layout recovery [IEEE FUSION / EUSIPCO]\n"
        "   │     Yu et al.: cross-regional NLOS localization moves the multipath-detection branch toward joint-GLRT inference across hidden regions [IEEE IGARSS]\n"
    )
    readme = readme.replace(anchor, anchor + addition, 1)
write("README.md", readme)


# Canonical V2 corpus used by the paper explorer and graph.
data = read("data/papers-source.html")
data = data.replace("Updated 15 August 2026 · 210+ papers", "Updated 16 August 2026 · 210+ papers", 1)
anchor = "    const papers=[\n"
require(data, anchor, "canonical paper corpus")
objects = []
added = 0
for p in PAPERS:
    if p["title"] not in data:
        key = p["summary"].replace('"', '&quot;')
        objects.append(
            f'      {{cat:"{p["cat"]}",title:"{p["title"]}",authors:"{p["authors"]}",year:{p["year"]},venue:"{p["venue"]}",url:"{p["url"].replace("&", "&amp;")}",key:"{key}"}},\n'
        )
        added += 1
if objects:
    data = data.replace(anchor, anchor + "".join(objects), 1)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    data = pat.sub(f'<b>{int(m.group(1)) + added}</b><span>tracked latest entries</span>', data, count=1)

if "multipath ghost correlation jointly links target hypotheses" not in data:
    pat25 = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m25 = pat25.search(data)
    if not m25:
        raise RuntimeError("Could not locate 2025 website timeline")
    sentence25 = (
        " Yu et al. exploited diffraction signals to estimate building-corner and NLOS-target parameters, while Wei et al. used multipath ghost correlation to jointly link target hypotheses with unknown wall geometry."
    )
    data = data[:m25.start()] + m25.group(1) + m25.group(2) + sentence25 + m25.group(3) + data[m25.end():]

if "joint multipath GLRT extends radar NLOS localization across regions" not in data:
    pat26 = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m26 = pat26.search(data)
    if not m26:
        raise RuntimeError("Could not locate 2026 website timeline")
    sentence26 = (
        " Yu et al. further reported a cross-regional NLOS target-localization method based on joint multipath GLRT at IGARSS 2026."
    )
    data = data[:m26.start()] + m26.group(1) + m26.group(2) + sentence26 + m26.group(3) + data[m26.end():]
write("data/papers-source.html", data)


# Radar/RF survey narrative: extend the unknown-geometry lineage with diffraction, ghost correlation and the fresh GLRT result.
newscenes = read("article/5newscenes.tex")
if not all(p["key"] in newscenes for p in PAPERS):
    anchor = "Together, these works shift RF NLOS from reconstruction under a calibrated relay map toward joint estimation of the environment, propagation paths, hidden-target state, and motion.\n"
    require(newscenes, anchor, "radar unknown-geometry paragraph")
    para = r"""

\vspace{0.8mm}
\noindent \textbf{Diffraction, multipath-ghost correlation, and cross-regional inference.}
The same unknown-environment trajectory is also visible in recent conference work that makes more explicit use of diffraction and multipath hypotheses. Yu~\etal~use diffraction-signal information to estimate building-corner and NLOS-target parameters rather than treating the corner geometry only as fixed prior knowledge~\cite{yuDiffractionCornerNLOS2025}, extending the earlier diffraction-based around-corner localization lineage. Wei~\etal~jointly estimate hidden-target locations and building layouts by extracting multipath Range--Doppler features, estimating directions and ghost positions with the iterative adaptive approach, and spatially matching the resulting ghosts to candidate targets and walls~\cite{weiGhostCorrelationNLOS2025}. This turns multipath ghosts from nuisance artifacts into geometric constraints that couple target localization and environment reconstruction. At IGARSS 2026, Yu~\etal~further reported a cross-regional NLOS target-localization method based on a joint multipath generalized likelihood ratio test (GLRT)~\cite{yuCrossRegionalGLRTNLOS2026}. The official conference program verifies the paper and its 11 August 2026 presentation; because a proceedings DOI was not yet indexed at the time of this update, we retain the final conference designation without inventing publication metadata. Together, these works sharpen the progression from known-corner diffraction models to joint target--layout inference and then to detection/localization rules designed to combine multipath evidence across hidden regions.
"""
    newscenes = newscenes.replace(anchor, anchor + para, 1)
write("article/5newscenes.tex", newscenes)


# Top-level survey synchronization marker.
tex = read("bare_jrnl.tex")
marker = "% 16 August 2026 citation trace: diffraction, multipath-ghost, and cross-regional radar NLOS localization synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Persistent update note with provenance and conservative venue handling.
note = ROOT / "updates/2026-08-16-radar-crossregional-citation-trace.md"
note.write_text(
    """# 16 August 2026 radar/RF NLOS citation-trace update

## Newly integrated missing works

1. Yupeng Yu et al., **Building Corner and NLOS Target Parameter Estimation Based on Diffraction Signal Utilization**, IEEE FUSION 2025, pp. 1--6, DOI 10.23919/FUSION65864.2025.11124177. The paper continues the electromagnetic-diffraction around-corner lineage by estimating corner/target parameters from diffraction evidence instead of requiring all geometry as prior input.
2. Yufei Wei et al., **Multipath Ghost Correlation-Based NLOS Target Localization and Building Layuot Estimation**, IEEE EUSIPCO 2025, pp. 2247--2251, DOI 10.23919/EUSIPCO63237.2025.11226331. The published paper uses Range--Doppler multipath separation, IAA direction/ghost estimation, and spatial matching to jointly infer hidden targets and building layout.
3. Yupeng Yu et al., **A Cross-Regional NLOS Target Localization Method Based on Joint Multipath GLRT**, IEEE IGARSS 2026, Paper 2579 / TUP1.PC.9, presented 11 August 2026. The official IGARSS program verifies the title, authors, paper number, session, and presentation time. No proceedings DOI was available in the official program when this update was prepared, so the bibliography intentionally uses the official conference page rather than guessing a DOI.

## Citation-trace context

A fresh forward-citation and recent-publication pass from the canonical optical/transient core papers (Velten 2012, LCT, f-k migration, phasor-field, computational periscopy and major learned/transient successors) did not reveal another high-confidence optical gap not already represented in the repository. The three additions above instead close a radar/RF lineage gap adjacent to the already integrated unknown-relay-geometry papers: known diffraction geometry -> diffraction-aided corner/target parameter estimation -> multipath-ghost target/layout matching -> cross-regional joint-GLRT localization.

## Synchronization

The integration workflow updates README, the canonical V2 corpus (`data/papers-source.html`), the radar/RF survey narrative, the merged bibliography, `bare_jrnl.tex`, and a rebuilt `bare_jrnl.pdf`, then validates title/key uniqueness, citations, PDF text and rendering before pushing the public-artifact commit.
""",
    encoding="utf-8",
)

print(f"Radar cross-regional citation-trace integration applied; canonical corpus additions: {added}")
