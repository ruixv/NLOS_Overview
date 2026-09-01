from pathlib import Path
import re

TODAY_LONG = "2 September 2026"
TODAY_SHORT = "2 Sep 2026"

PAPERS = [
    {
        "key": "tianQCDCQSRNLOS2026",
        "title": "Non-line-of-sight super-resolution imaging with quasi-constant-delay circular pattern",
        "authors": "Tian et al.",
        "year": 2026,
        "venue": "APL Photonics 11(7), 076122 (2026)",
        "url": "https://doi.org/10.1063/5.0331605",
        "doi": "10.1063/5.0331605",
        "cat": "latest active optical transient acquisition super-resolution qcdc qsr spad",
        "summary": "Co-designs quasi-constant-delay circular relay-wall sampling with temporal super-resolution, computationally lifting 200-ps measurements to about 20-ps effective timing resolution while remaining compatible with standard f-k and phasor-field reconstruction backends.",
        "readme_summary": "Jointly designs QCDC relay-wall sampling and QSR temporal super-resolution, computationally lifting 200 ps measurements to about 20 ps effective timing resolution while retaining compatibility with standard f-k and phasor-field reconstruction backends.",
        "bib_candidates": ["egbib_20260830_qcdc_qsr_nlos_gap.bib"],
    },
    {
        "key": "luesialahozStereoNLOS2026",
        "title": "Stereo non-line-of-sight imaging",
        "authors": "Luesia-Lahoz et al.",
        "year": 2026,
        "venue": "The Visual Computer 42, 148 (2026)",
        "url": "https://doi.org/10.1007/s00371-025-04340-7",
        "doi": "10.1007/s00371-025-04340-7",
        "cat": "latest active optical transient phasor-field multi-relay stereo missing-cone geometry orientation",
        "summary": "Uses two relay walls as phasor-field virtual apertures, including cross-wall paths, to improve hidden-surface visibility under the missing-cone limitation and extract view-dependent surface-orientation cues.",
        "readme_summary": "Uses two relay walls as phasor-field virtual apertures, including cross-wall illumination/capture paths, to mitigate missing-cone visibility loss and obtain hidden-surface orientation cues.",
        "bib_candidates": ["egbib_20260901_stereo_nlos_gap.bib"],
    },
    {
        "key": "lopezruizMemoryEfficientGPUNLOS2026",
        "title": "Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction",
        "authors": "López-Ruiz and Royo",
        "year": 2026,
        "venue": "arXiv 2026",
        "url": "https://arxiv.org/abs/2608.28183",
        "doi": "",
        "cat": "latest active optical transient reconstruction acceleration gpu real-time f-k phasor-field systems",
        "summary": "Re-engineers f-k migration and phasor-field reconstruction with fused CUDA kernels, warp-level binning, batched transforms, CUDA graphs and memory-efficient phasor kernels, exposing reconstruction throughput and memory bandwidth as bottlenecks for high-rate SPAD NLOS.",
        "readme_summary": "Re-engineers f-k migration and phasor-field reconstruction for streaming/offline GPU execution with fused CUDA kernels, warp-level photon binning, batched transforms, CUDA graphs and memory-efficient phasor kernels; reports up to 42× streaming speedup and major memory reductions.",
        "bib_candidates": ["egbib_20260901_gpu_pipeline_gap.bib", "egbib_20260831_gpu_pipeline_gap.bib"],
    },
]


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def bib_blocks(text):
    starts = list(re.finditer(r"(?m)^@[A-Za-z]+\{", text))
    blocks = []
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        blocks.append(text[m.start():end].strip())
    return blocks


def field(block, name):
    m = re.search(r"(?mis)^\s*" + re.escape(name) + r"\s*=\s*\{(.*?)\}\s*,?\s*$", block)
    return m.group(1).strip() if m else ""


# ---------- README: latest additions + 2026 development timeline ----------
readme = read("README.md")
latest_start = readme.find("## Latest Additions")
if latest_start < 0:
    raise RuntimeError("README Latest Additions section not found")
latest_end = readme.find("\n## ", latest_start + 4)
if latest_end < 0:
    latest_end = len(readme)
latest = readme[latest_start:latest_end]
sep_match = re.search(r"(?m)^\|[-| ]+\|\s*$", latest)
if not sep_match:
    raise RuntimeError("README Latest Additions table separator not found")
insert_abs = latest_start + sep_match.end() + 1
rows = []
for p in PAPERS:
    if p["title"].lower() not in readme.lower() and (not p["doi"] or p["doi"].lower() not in readme.lower()):
        rows.append(
            f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["readme_summary"]} |\n'
        )
if rows:
    readme = readme[:insert_abs] + "".join(rows) + readme[insert_abs:]

# Keep an explicit 2026 development node if a 2026 header exists; otherwise Latest Additions remains canonical.
if not all((p["key"] + " timeline") in readme for p in PAPERS):
    m = re.search(r"(?m)^(#{2,4})\s+2026\s*$", readme)
    if m:
        timeline_lines = []
        for p in PAPERS:
            marker = p["key"] + " timeline"
            if marker not in readme:
                timeline_lines.append(
                    f'\n- **{p["title"]}** ({p["venue"]}) — {p["readme_summary"]} <!-- {marker} -->'
                )
        readme = readme[:m.end()] + "".join(timeline_lines) + readme[m.end():]

readme = re.sub(r"\*\*Update run: [^*]+\.\*\*", f"**Update run: {TODAY_LONG}.**", readme, count=1)
write("README.md", readme)


# ---------- Canonical website / Paper Explorer data ----------
corpus = read("data/papers-source.html")
arr_anchor = "    const papers=[\n"
if corpus.count(arr_anchor) != 1:
    raise RuntimeError("canonical paper array anchor not unique")
objects = []
for p in PAPERS:
    if p["title"].lower() not in corpus.lower() and (not p["doi"] or p["doi"].lower() not in corpus.lower()):
        safe_summary = p["summary"].replace('"', "'")
        objects.append(
            '      {cat:"%s",title:"%s",authors:"%s",year:%d,venue:"%s",url:"%s",key:"%s"},\n'
            % (p["cat"], p["title"], p["authors"], p["year"], p["venue"], p["url"], safe_summary)
        )
if objects:
    corpus = corpus.replace(arr_anchor, arr_anchor + "".join(objects), 1)
arr_start = corpus.find("    const papers=[")
arr_end = corpus.find("\n    ];", arr_start)
if arr_start < 0 or arr_end < 0:
    raise RuntimeError("paper array boundaries not found")
tracked = corpus[arr_start:arr_end].count("{cat:")
corpus, n = re.subn(
    r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)',
    rf'\g<1>{tracked}\g<2>', corpus, count=1,
)
if n != 1:
    raise RuntimeError("tracked latest entries counter not found")
corpus = re.sub(r"Updated \d{1,2} (?:August|September) 2026", f"Updated {TODAY_LONG}", corpus, count=1)
corpus = re.sub(r"Last updated: \d{1,2} (?:August|September) 2026", f"Last updated: {TODAY_LONG}", corpus, count=1)
write("data/papers-source.html", corpus)


# ---------- V2 wrapper date ----------
index = read("index.html")
index = re.sub(r"Updated \d{1,2} (?:Aug|Sep) 2026", f"Updated {TODAY_SHORT}", index, count=1)
write("index.html", index)


# ---------- Canonical bibliography ----------
bib_path = Path("egbib_merged_20260711.bib")
bib = bib_path.read_text(encoding="utf-8")
for p in PAPERS:
    key_present = re.search(r"@[A-Za-z]+\{" + re.escape(p["key"]) + r",", bib, flags=re.I) is not None
    doi_present = bool(p["doi"] and p["doi"].lower() in bib.lower())
    title_present = p["title"].lower() in bib.lower()
    if key_present or doi_present or title_present:
        continue
    source = None
    for cand in p["bib_candidates"]:
        if Path(cand).exists():
            source = read(cand)
            break
    if source is None:
        raise RuntimeError(f"no staging BibTeX found for {p['key']}")
    matches = [b for b in bib_blocks(source) if p["key"] in b or p["title"].lower() in b.lower() or (p["doi"] and p["doi"].lower() in b.lower())]
    if len(matches) != 1:
        raise RuntimeError(f"expected one staged BibTeX block for {p['key']}, found {len(matches)}")
    bib = bib.rstrip() + "\n\n" + matches[0].strip() + "\n"
write(bib_path, bib)


# ---------- Survey prose in active NLOS section ----------
active_path = Path("article/2active.tex")
active = active_path.read_text(encoding="utf-8")
marker = "% 2 September 2026 pending-integration closure: QCDC temporal super-resolution, stereo multi-relay phasor imaging, and GPU reconstruction systems."
if marker not in active:
    prose = r'''

% 2 September 2026 pending-integration closure: QCDC temporal super-resolution, stereo multi-relay phasor imaging, and GPU reconstruction systems.
\paragraph{Acquisition, aperture, and implementation co-design.}
Recent active NLOS work increasingly treats acquisition geometry, virtual-aperture design, detector timing, and reconstruction implementation as a coupled systems problem rather than optimizing the inverse solver alone. Tian \textit{et al.} co-design a quasi-constant-delay circular relay-wall trajectory with quasi-constant-delay super-resolution, exploiting deliberately shifted transients to improve the effective timing resolution from 200~ps to about 20~ps while preserving compatibility with conventional $f$--$k$ and phasor-field reconstruction backends~\cite{tianQCDCQSRNLOS2026}. This direction transfers part of the temporal-resolution burden from specialized detector hardware to acquisition geometry and computational recovery, which is particularly relevant to lower-cost SPAD systems. Complementing arbitrary-relay-surface formulations, Luesia-Lahoz \textit{et al.} use two relay walls as a generalized stereo phasor-field aperture and incorporate both same-wall and cross-wall transport paths, improving hidden-surface visibility under the missing-cone limitation while turning view-dependent visibility into a cue for surface orientation~\cite{luesialahozStereoNLOS2026}. At the implementation level, L\'opez-Ruiz and Royo re-engineer both $f$--$k$ migration and phasor-field pipelines for GPU execution using fused CUDA kernels, warp-level photon binning, batched transforms, CUDA graph replay, selective half-precision storage, and memory-efficient phasor kernels~\cite{lopezruizMemoryEfficientGPUNLOS2026}. Their results highlight a newer systems bottleneck: as parallel SPAD arrays and sparse/scan-free acquisition raise measurement throughput, memory movement, kernel materialization, and scheduling can dominate the latency of real-time NLOS cameras.
'''
    active = active.rstrip() + prose + "\n"
active_path.write_text(active, encoding="utf-8")


# ---------- Survey provenance/date ----------
tex_path = Path("bare_jrnl.tex")
tex = tex_path.read_text(encoding="utf-8")
note = "% 2 September 2026 consistency pass: integrated QCDC-QSR temporal super-resolution, stereo multi-relay phasor NLOS, and memory-efficient GPU reconstruction across public artifacts.\n"
if note not in tex:
    tex = note + tex
tex = re.sub(r"through \d{1,2} (?:August|September) 2026", "through 2 September 2026", tex, count=1)
tex_path.write_text(tex, encoding="utf-8")


# ---------- Source-level assertions ----------
checks = [
    ("README.md", [p["title"] for p in PAPERS]),
    ("data/papers-source.html", [p["title"] for p in PAPERS]),
    ("article/2active.tex", [p["key"] for p in PAPERS]),
    ("egbib_merged_20260711.bib", [p["key"] for p in PAPERS]),
    ("bare_jrnl.tex", ["2 September 2026 consistency pass"]),
]
for path, needles in checks:
    text = read(path)
    for needle in needles:
        if needle not in text:
            raise RuntimeError(f"missing {needle!r} from {path}")

# Canonical bibliography keys must be unique.
bib = read("egbib_merged_20260711.bib")
for p in PAPERS:
    n = len(re.findall(r"@[A-Za-z]+\{" + re.escape(p["key"]) + r",", bib, flags=re.I))
    if n != 1:
        raise RuntimeError(f"canonical bibliography key {p['key']} occurs {n} times")

print("Integrated pending NLOS records:")
for p in PAPERS:
    print(" -", p["key"], p["title"])
print("Tracked latest entries:", tracked)
