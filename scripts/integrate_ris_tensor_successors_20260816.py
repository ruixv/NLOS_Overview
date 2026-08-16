from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Covariance Tensor Decomposition for NLOS Direction Finding in RIS-Aided Bistatic MIMO Radar",
        "key": "xieCovarianceTensorRISNLOS2026",
        "year": 2026,
        "authors": "Xie et al.",
        "venue": "IEEE Signal Processing Letters 33 (2026), 574–578",
        "url": "https://doi.org/10.1109/LSP.2026.3652124",
        "cat": "latest modality radar rf ris tensor covariance hosvd direction-finding dod doa",
        "summary": "Builds a fourth-order covariance tensor for RIS-aided bistatic MIMO radar, extracts the signal subspace with HOSVD, reconstructs steering structure through the Khatri–Rao product, and estimates paired NLOS DOD/DOA efficiently.",
    },
    {
        "title": "Fast Angle Estimation of NLoS Coherent and Noncoherent Targets via Tensor Decomposition in RIS-Assisted Bistatic MIMO Radar",
        "key": "yuFastAngleRISNLOS2026",
        "year": 2026,
        "authors": "Yu et al.",
        "venue": "IEEE TAES 62 (2026), 8574–8584",
        "url": "https://doi.org/10.1109/TAES.2026.3651424",
        "cat": "latest modality radar rf ris tensor angle-estimation coherent noncoherent dod doa",
        "summary": "Extends tensor-based RIS-assisted bistatic MIMO radar processing to fast angle estimation for both coherent and noncoherent hidden targets, strengthening the reconfigurable-propagation direction-finding branch.",
    },
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:180]}")


# README latest additions.
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

if "covariance-tensor HOSVD and fast coherent/noncoherent angle estimation" not in readme:
    anchor = "   │     Yu et al.: an IRS-assisted FDA-MIMO tensor model turns a controllable hidden path into multi-target range/angle localization [Digital Signal Processing]\n"
    require(readme, anchor, "README IRS tensor timeline")
    addition = "   │     Xie et al. / Yu et al.: covariance-tensor HOSVD and fast coherent/noncoherent angle estimation extend RIS-assisted hidden-target direction finding [IEEE SPL / TAES]\n"
    readme = readme.replace(anchor, anchor + addition, 1)
write("README.md", readme)


# Canonical V2 paper corpus and 2026 development timeline.
data = read("data/papers-source.html")
anchor = "    const papers=[\n"
require(data, anchor, "canonical paper corpus")
objects = []
added = 0
for p in PAPERS:
    if p["title"] not in data:
        key = p["summary"].replace('"', '&quot;')
        objects.append(
            f'      {{cat:"{p["cat"]}",title:"{p["title"]}",authors:"{p["authors"]}",year:{p["year"]},venue:"{p["venue"]}",url:"{p["url"]}",key:"{key}"}},\n'
        )
        added += 1
if objects:
    data = data.replace(anchor, anchor + "".join(objects), 1)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    data = pat.sub(f'<b>{int(m.group(1)) + added}</b><span>tracked latest entries</span>', data, count=1)

if "covariance-tensor HOSVD and fast tensor angle estimation" not in data:
    pat26 = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m26 = pat26.search(data)
    if not m26:
        raise RuntimeError("Could not locate 2026 website timeline")
    sentence = (
        " The RIS-assisted radar branch also advanced through covariance-tensor HOSVD and fast tensor angle estimation for NLOS DOD/DOA recovery, including coherent and noncoherent hidden targets."
    )
    data = data[:m26.start()] + m26.group(1) + m26.group(2) + sentence + m26.group(3) + data[m26.end():]
write("data/papers-source.html", data)


# Consolidate the 2025 DSP paper and its 2026 successors in the angular-sensing section.
newscenes = read("article/5newscenes.tex")
misplaced = r" Yu~\etal~use an IRS to establish a controllable NLoS path for bistatic FDA--MIMO radar, construct the received echoes as a third-order tensor, estimate target number by sequential MDL, and apply PARAFAC factorization to decouple DOD/range and recover 2-D DOA before geometric multi-target localization~\cite{yuIRSFdaMimoNLOS2025}. This extends reconfigurable propagation from beam redirection and physiological sensing toward explicit hidden-target localization with multidimensional radar parameter estimation."
if misplaced in newscenes:
    newscenes = newscenes.replace(misplaced, "", 1)

if not all(p["key"] in newscenes for p in PAPERS):
    anchor = "Both studies are numerical, so they should be read as theoretical RIS-assisted NLOS localization advances rather than measured hidden-scene imaging systems.\n"
    require(newscenes, anchor, "RIS angular-sensing paragraph")
    para = r"""

A closely related tensor-processing branch uses reconfigurable propagation together with multidimensional radar structure. Yu~\etal~use an IRS to establish a controllable NLoS path for bistatic FDA--MIMO radar, estimate target count by sequential MDL, and factorize a third-order echo tensor with PARAFAC to decouple DOD/range and recover 2-D DOA before geometric multi-target localization~\cite{yuIRSFdaMimoNLOS2025}. Xie~\etal~then construct a fourth-order covariance tensor for RIS-aided bistatic MIMO radar, extract its signal subspace with HOSVD, reconstruct the receive steering matrix through Khatri--Rao structure, and obtain automatically paired DOD/DOA estimates~\cite{xieCovarianceTensorRISNLOS2026}. Yu~\etal~further address fast angle estimation for both coherent and noncoherent NLoS targets with tensor decomposition~\cite{yuFastAngleRISNLOS2026}. These works trace a progression from IRS-created hidden paths and full target localization to increasingly structured and efficient angle inference; the current evidence is primarily simulation-based, so this branch should remain distinct from measured around-corner imaging and reconstruction systems.
"""
    newscenes = newscenes.replace(anchor, anchor + para, 1)
write("article/5newscenes.tex", newscenes)


# Survey synchronization marker.
tex = read("bare_jrnl.tex")
marker = "% 16 August 2026 citation trace: RIS tensor NLOS direction-finding successors synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Extend the provenance note created by the main radar citation-trace script.
note = ROOT / "updates/2026-08-16-radar-crossregional-citation-trace.md"
text = note.read_text(encoding="utf-8") if note.exists() else "# 16 August 2026 radar/RF NLOS citation-trace update\n"
if "Covariance Tensor Decomposition for NLOS Direction Finding" not in text:
    text += """

## Latest RIS tensor successors added in the same pass

5. Qian-Peng Xie et al., **Covariance Tensor Decomposition for NLOS Direction Finding in RIS-Aided Bistatic MIMO Radar**, IEEE Signal Processing Letters 33, 574--578 (2026), DOI 10.1109/LSP.2026.3652124. A fourth-order covariance tensor plus HOSVD and Khatri--Rao reconstruction yields paired DOD/DOA estimates for RIS-aided hidden targets.
6. Weijia Yu et al., **Fast Angle Estimation of NLoS Coherent and Noncoherent Targets via Tensor Decomposition in RIS-Assisted Bistatic MIMO Radar**, IEEE Transactions on Aerospace and Electronic Systems 62, 8574--8584 (2026), DOI 10.1109/TAES.2026.3651424. The work extends the tensor/RIS lineage to efficient angle estimation for both coherent and noncoherent NLoS targets.

These two 2026 journal papers were found by tracing forward from the verified 2025 Digital Signal Processing IRS/FDA-MIMO localization paper. They are direct NLOS radar successors rather than generic RIS communications papers and are therefore integrated into the survey's RIS-assisted angular-sensing lineage.
"""
note.write_text(text, encoding="utf-8")

print(f"RIS tensor successor integration applied; canonical corpus additions: {added}")
