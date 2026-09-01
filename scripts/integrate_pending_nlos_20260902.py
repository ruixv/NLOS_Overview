from pathlib import Path
import re

TODAY_LONG = "2 September 2026"
TODAY_SHORT = "2 Sep 2026"

PAPERS = [
    dict(key="tianQCDCQSRNLOS2026", marker="qcdc-qsr-2026",
         title="Non-line-of-sight super-resolution imaging with quasi-constant-delay circular pattern",
         authors="Tian et al.", year=2026, venue="APL Photonics 11(7), 076122 (2026)",
         url="https://doi.org/10.1063/5.0331605", token="10.1063/5.0331605",
         cat="latest active optical transient acquisition super-resolution qcdc qsr spad",
         summary="Co-designs quasi-constant-delay circular relay-wall sampling with temporal super-resolution, computationally lifting 200-ps measurements to about 20-ps effective timing resolution while remaining compatible with standard f-k and phasor-field reconstruction backends.",
         readme_summary="Jointly designs QCDC relay-wall sampling and QSR temporal super-resolution, computationally lifting 200 ps measurements to about 20 ps effective timing resolution while retaining compatibility with standard f-k and phasor-field reconstruction backends.",
         bib_candidates=["egbib_20260830_qcdc_qsr_nlos_gap.bib"]),
    dict(key="luesialahozStereoNLOS2026", marker="stereo-nlos-2026",
         title="Stereo non-line-of-sight imaging", authors="Luesia-Lahoz et al.", year=2026,
         venue="The Visual Computer 42, 148 (2026)",
         url="https://doi.org/10.1007/s00371-025-04340-7", token="10.1007/s00371-025-04340-7",
         cat="latest active optical transient phasor-field multi-relay stereo missing-cone geometry orientation",
         summary="Uses two relay walls as phasor-field virtual apertures, including cross-wall paths, to improve hidden-surface visibility under the missing-cone limitation and extract view-dependent surface-orientation cues.",
         readme_summary="Uses two relay walls as phasor-field virtual apertures, including cross-wall illumination/capture paths, to mitigate missing-cone visibility loss and obtain hidden-surface orientation cues.",
         bib_candidates=["egbib_20260901_stereo_nlos_gap.bib"]),
    dict(key="lopezruizMemoryEfficientGPUNLOS2026", marker="gpu-nlos-2026",
         title="Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction",
         authors="López-Ruiz and Royo", year=2026, venue="arXiv 2026",
         url="https://arxiv.org/abs/2608.28183", token="2608.28183",
         cat="latest active optical transient reconstruction acceleration gpu real-time f-k phasor-field systems",
         summary="Re-engineers f-k migration and phasor-field reconstruction with fused CUDA kernels, warp-level binning, batched transforms, CUDA graphs and memory-efficient phasor kernels, exposing reconstruction throughput and memory bandwidth as bottlenecks for high-rate SPAD NLOS.",
         readme_summary="Re-engineers f-k migration and phasor-field reconstruction for streaming/offline GPU execution with fused CUDA kernels, warp-level photon binning, batched transforms, CUDA graphs and memory-efficient phasor kernels; reports up to 42× streaming speedup and major memory reductions.",
         bib_candidates=["egbib_20260901_gpu_pipeline_gap.bib", "egbib_20260831_gpu_pipeline_gap.bib"]),
]


def read(path): return Path(path).read_text(encoding="utf-8")
def write(path, text): Path(path).write_text(text, encoding="utf-8")

def norm(s):
    s = re.sub(r"[{}\\]", "", s.lower())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def bib_blocks(text):
    starts = list(re.finditer(r"(?m)^@[A-Za-z]+\{", text))
    return [text[m.start():(starts[i+1].start() if i+1 < len(starts) else len(text))].strip()
            for i, m in enumerate(starts)]

def bib_key(block):
    m = re.match(r"@[A-Za-z]+\{\s*([^,]+),", block)
    if not m: raise RuntimeError("Malformed BibTeX block")
    return m.group(1).strip()

def matching_blocks(text, p):
    nt = norm(p["title"])
    return [b for b in bib_blocks(text)
            if p["token"].lower() in b.lower() or nt in norm(b)]

# Resolve canonical citation keys before touching prose. Reuse an existing matching entry;
# append a staged entry only when no canonical record exists.
bib_path = Path("egbib_merged_20260711.bib")
bib = read(bib_path)
for p in PAPERS:
    matches = matching_blocks(bib, p)
    if len(matches) > 1:
        raise RuntimeError(f"duplicate canonical BibTeX records for {p['title']}")
    if matches:
        p["cite_key"] = bib_key(matches[0])
        continue
    source = next((read(c) for c in p["bib_candidates"] if Path(c).exists()), None)
    if source is None:
        raise RuntimeError(f"no staged BibTeX available for {p['title']}")
    staged = matching_blocks(source, p)
    if len(staged) != 1:
        raise RuntimeError(f"expected one staged BibTeX record for {p['title']}, found {len(staged)}")
    block = staged[0]
    p["cite_key"] = bib_key(block)
    bib = bib.rstrip() + "\n\n" + block + "\n"
write(bib_path, bib)

# README: Latest Additions plus a compact 2026 timeline node when that section exists.
readme = read("README.md")
latest_start = readme.find("## Latest Additions")
if latest_start < 0: raise RuntimeError("README Latest Additions section not found")
latest_end = readme.find("\n## ", latest_start + 4)
if latest_end < 0: latest_end = len(readme)
latest = readme[latest_start:latest_end]
sep = re.search(r"(?m)^\|[-| ]+\|\s*$", latest)
if not sep: raise RuntimeError("README Latest Additions table separator not found")
insert_at = latest_start + sep.end() + 1
rows = []
for p in PAPERS:
    if p["title"].lower() not in readme.lower() and p["token"].lower() not in readme.lower():
        rows.append(f'| {p["year"]} | [{p["title"]}]({p["url"]}) — {p["authors"]} | {p["venue"]} | {p["readme_summary"]} |\n')
if rows: readme = readme[:insert_at] + "".join(rows) + readme[insert_at:]
year_head = re.search(r"(?m)^(#{2,4})\s+2026\s*$", readme)
if year_head:
    additions = []
    for p in PAPERS:
        tag = f'<!-- {p["marker"]} timeline -->'
        if tag not in readme:
            additions.append(f'\n- **{p["title"]}** ({p["venue"]}) — {p["readme_summary"]} {tag}')
    if additions: readme = readme[:year_head.end()] + "".join(additions) + readme[year_head.end():]
readme = re.sub(r"\*\*Update run: [^*]+\.\*\*", f"**Update run: {TODAY_LONG}.**", readme, count=1)
write("README.md", readme)

# Website/Paper Explorer canonical data.
corpus = read("data/papers-source.html")
anchor = "    const papers=[\n"
if corpus.count(anchor) != 1: raise RuntimeError("canonical paper array anchor not unique")
objects = []
for p in PAPERS:
    if p["title"].lower() not in corpus.lower() and p["token"].lower() not in corpus.lower():
        objects.append('      {cat:"%s",title:"%s",authors:"%s",year:%d,venue:"%s",url:"%s",key:"%s"},\n' %
                       (p["cat"], p["title"], p["authors"], p["year"], p["venue"], p["url"], p["summary"].replace('"', "'")))
if objects: corpus = corpus.replace(anchor, anchor + "".join(objects), 1)
a = corpus.find("    const papers=["); z = corpus.find("\n    ];", a)
if a < 0 or z < 0: raise RuntimeError("paper array boundaries not found")
tracked = corpus[a:z].count("{cat:")
corpus, n = re.subn(r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)', rf'\g<1>{tracked}\g<2>', corpus, count=1)
if n != 1: raise RuntimeError("tracked latest entries counter not found")
corpus = re.sub(r"Updated \d{1,2} (?:August|September) 2026", f"Updated {TODAY_LONG}", corpus, count=1)
corpus = re.sub(r"Last updated: \d{1,2} (?:August|September) 2026", f"Last updated: {TODAY_LONG}", corpus, count=1)
write("data/papers-source.html", corpus)
index = read("index.html")
index = re.sub(r"Updated \d{1,2} (?:Aug|Sep) 2026", f"Updated {TODAY_SHORT}", index, count=1)
write("index.html", index)

# Semantically integrated active-NLOS literature review; use the canonical key actually present.
active_path = Path("article/2active.tex")
active = read(active_path)
marker = "% 2 September 2026 pending-integration closure: QCDC temporal super-resolution, stereo multi-relay phasor imaging, and GPU reconstruction systems."
if marker not in active:
    q, s, g = [p["cite_key"] for p in PAPERS]
    prose = f'''\n\n{marker}\n\\paragraph{{Acquisition, aperture, and implementation co-design.}}\nRecent active NLOS work increasingly treats acquisition geometry, virtual-aperture design, detector timing, and reconstruction implementation as a coupled systems problem rather than optimizing the inverse solver alone. Tian \\textit{{et al.}} co-design a quasi-constant-delay circular relay-wall trajectory with quasi-constant-delay super-resolution, exploiting deliberately shifted transients to improve the effective timing resolution from 200~ps to about 20~ps while preserving compatibility with conventional $f$--$k$ and phasor-field reconstruction backends~\\cite{{{q}}}. This direction transfers part of the temporal-resolution burden from specialized detector hardware to acquisition geometry and computational recovery, which is particularly relevant to lower-cost SPAD systems. Complementing arbitrary-relay-surface formulations, Luesia-Lahoz \\textit{{et al.}} use two relay walls as a generalized stereo phasor-field aperture and incorporate both same-wall and cross-wall transport paths, improving hidden-surface visibility under the missing-cone limitation while turning view-dependent visibility into a cue for surface orientation~\\cite{{{s}}}. At the implementation level, L\\'opez-Ruiz and Royo re-engineer both $f$--$k$ migration and phasor-field pipelines for GPU execution using fused CUDA kernels, warp-level photon binning, batched transforms, CUDA graph replay, selective half-precision storage, and memory-efficient phasor kernels~\\cite{{{g}}}. Their results highlight a newer systems bottleneck: as parallel SPAD arrays and sparse/scan-free acquisition raise measurement throughput, memory movement, kernel materialization, and scheduling can dominate the latency of real-time NLOS cameras.\n'''
    active = active.rstrip() + prose
write(active_path, active)

# Survey provenance/date.
tex = read("bare_jrnl.tex")
note = "% 2 September 2026 consistency pass: integrated QCDC-QSR temporal super-resolution, stereo multi-relay phasor NLOS, and memory-efficient GPU reconstruction across public artifacts.\n"
if note not in tex: tex = note + tex
tex = re.sub(r"through \d{1,2} (?:August|September) 2026", "through 2 September 2026", tex, count=1)
write("bare_jrnl.tex", tex)

# Fail closed on source inconsistency.
for p in PAPERS:
    if p["title"].lower() not in read("README.md").lower(): raise RuntimeError("README missing " + p["title"])
    if p["title"].lower() not in read("data/papers-source.html").lower(): raise RuntimeError("Paper Explorer missing " + p["title"])
    if p["cite_key"] not in read("article/2active.tex"): raise RuntimeError("survey prose missing citation " + p["cite_key"])
    matches = matching_blocks(read(bib_path), p)
    if len(matches) != 1: raise RuntimeError(f"canonical bibliography has {len(matches)} records for {p['title']}")
if "2 September 2026 consistency pass" not in read("bare_jrnl.tex"): raise RuntimeError("survey provenance missing")

print("Integrated pending NLOS records using canonical citation keys:")
for p in PAPERS: print(" -", p["cite_key"], p["title"])
print("Tracked latest entries:", tracked)
