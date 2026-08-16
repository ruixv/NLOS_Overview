from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Seeing Around Obstacles Using Active Terahertz Imaging",
        "key": "cuiActiveTHzNLOS2024",
        "year": 2024,
        "authors": "Cui and Trichopoulos",
        "venue": "IEEE Transactions on Terahertz Science and Technology 14(4), 433–445 (2024)",
        "url": "https://doi.org/10.1109/TTHZ.2024.3401041",
        "cat": "latest modality thz sub-thz rf radar active around-corner imaging mirror-folding multipath",
        "summary": "Uses 270–300 GHz active THz imaging and a mirror-folding reconstruction that treats ordinary building surfaces as lossy mirrors, recovering hidden-object geometry and pose with centimeter-scale resolution without prior scene geometry or material properties.",
    },
    {
        "title": "Around-the-Corner Radar Sensing Using Reconfigurable Intelligent Surface",
        "key": "yasmeenAroundCornerRIS2024",
        "year": 2024,
        "authors": "Yasmeen et al.",
        "venue": "IEEE MAPCON 2024",
        "url": "https://doi.org/10.1109/MAPCON61407.2024.10923061",
        "cat": "latest modality radar rf ris metasurface around-corner micro-doppler measured",
        "summary": "Demonstrates a custom 1-bit RIS with a 5.5 GHz monostatic radar in a real corridor, electronically redirecting illumination around a corner and recovering hidden-human walking micro-Doppler signatures; the final MAPCON venue supersedes the later arXiv upload.",
    },
    {
        "title": "Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface",
        "key": "yasmeenDualBeamRIS2026",
        "year": 2025,
        "authors": "Yasmeen et al.",
        "venue": "IEEE RadarConf25, 1254–1259 (2025)",
        "url": "https://doi.org/10.1109/RadarConf2559087.2025.11205052",
        "cat": "latest modality radar rf ris metasurface around-corner dual-beam quantized measured",
        "summary": "Studies practical RIS phase quantization for radar sensing: a 1-bit implementation produces dual symmetric beams, and measured/simulated radar cross-section is benchmarked against ideal single-beam RIS and metal-reflector baselines; the final RadarConf25 venue supersedes the later arXiv upload.",
    },
    {
        "title": "“Around-the-Corner” Radar: Particle Filters for Non-Line-of-Sight Target Tracking in the Presence of Ambiguities",
        "key": "phamParticleFilterAroundCorner2025",
        "year": 2025,
        "authors": "Pham et al.",
        "venue": "IEEE Transactions on Aerospace and Electronic Systems 61(3), 5505–5519 (2025)",
        "url": "https://doi.org/10.1109/TAES.2024.3503560",
        "cat": "latest modality radar rf around-corner multipath particle-filter tracking ambiguity",
        "summary": "Formulates multipath around-corner tracking when several propagation hypotheses create ambiguous likelihood modes, and uses particle filtering to maintain the competing target-state hypotheses instead of collapsing onto a wrong trajectory.",
    },
    {
        "title": "Single-Antenna Non-Line-of-Sight Matrix Imaging via Reconfigurable Intelligent Surfaces",
        "key": "goicoecheaSingleAntennaRISNLOS2025",
        "year": 2025,
        "authors": "Goïcoechea et al.",
        "venue": "arXiv:2512.12359 (2025)",
        "url": "https://arxiv.org/abs/2512.12359",
        "cat": "latest modality radar rf microwave ris metasurface reflection-matrix synthetic-array imaging tracking",
        "summary": "Shows that one transmit–receive antenna plus programmable RIS masks can reconstruct the full reflection matrix, effectively synthesizing an array for high-fidelity NLOS imaging, selective focusing through clutter, and moving-target tracking; no final peer-reviewed venue was verified as of this update.",
    },
    {
        "title": "Improving SNR for NLoS Target Detection Using Multi-RIS-Assisted Monostatic Radar",
        "key": "liaquatMultiRISNLOS2025",
        "year": 2025,
        "authors": "Liaquat et al.",
        "venue": "IEEE Open Journal of Vehicular Technology 6, 774–789 (2025)",
        "url": "https://doi.org/10.1109/OJVT.2025.3547163",
        "cat": "latest modality radar rf ris multi-ris monostatic detection snr link-budget",
        "summary": "Derives received-power, path-loss, and SNR models for monostatic NLOS radar assisted by multiple RIS relays, quantifying when additional programmable surfaces recover otherwise blocked sensing links and improve target detectability.",
    },
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:180]}")


# README: public paper list and historical trajectory.
readme = read("README.md")
readme = re.sub(
    r"\*\*Update run: \d{1,2} [A-Za-z]+ 2026\.\*\*",
    "**Update run: 17 August 2026.**",
    readme,
    count=1,
)
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

if "active 270–300 GHz THz imaging treats building surfaces as lossy mirrors" not in readme:
    anchor = "   │     Tosi et al.: 27.4-GHz 5G/mmWave ISAC proves fully NLOS target detection with TDD-artifact-aware CSI processing [IEEE SPAWC]\n"
    require(readme, anchor, "README 2024 RF timeline")
    addition = (
        "   │     Cui and Trichopoulos: active 270–300 GHz THz imaging treats building surfaces as lossy mirrors and folds multi-reflection paths for centimeter-scale hidden-object geometry and pose [IEEE T-TST]\n"
        "   │     Yasmeen et al.: a measured 5.5 GHz one-bit RIS redirects a monostatic radar around a corridor corner for hidden-human micro-Doppler sensing [IEEE MAPCON]\n"
    )
    readme = readme.replace(anchor, anchor + addition, 1)

if "ambiguity-aware particle filtering tracks around-corner radar targets" not in readme:
    anchor = "   │     Zhu et al.: weak-reflector 3-D environmental perception is coupled to path-oriented NLOS moving-target reconstruction [IEEE TAES]\n"
    require(readme, anchor, "README 2025 radar timeline")
    addition = (
        "   │     Pham et al.: ambiguity-aware particle filtering tracks around-corner radar targets when similar multipath hypotheses yield competing likelihood modes [IEEE TAES]\n"
        "   │     Yasmeen et al.: one-bit RIS quantization produces dual symmetric beams and benchmarks practical around-corner illumination against ideal RIS and metal-reflector baselines [IEEE RadarConf]\n"
        "   │     Liaquat et al.: multi-RIS monostatic radar analysis quantifies link-budget and SNR gains for blocked-target detection [IEEE OJVT]\n"
        "   │     Goïcoechea et al.: a single antenna plus programmable RIS reconstructs a full reflection matrix for hidden-scene imaging and moving-target tracking [arXiv]\n"
    )
    readme = readme.replace(anchor, anchor + addition, 1)
write("README.md", readme)


# Canonical V2 corpus used by Paper Explorer and the 3-D graph.
data = read("data/papers-source.html")
data = data.replace("16 August 2026", "17 August 2026")
anchor = "    const papers=[\n"
require(data, anchor, "canonical paper corpus")
objects = []
added = 0
for p in PAPERS:
    if p["title"] not in data:
        def esc(value):
            return str(value).replace("\\", "\\\\").replace('"', '\\"')
        objects.append(
            f'      {{cat:"{esc(p["cat"])}",title:"{esc(p["title"])}",authors:"{esc(p["authors"])}",year:{p["year"]},venue:"{esc(p["venue"])}",url:"{esc(p["url"])}",key:"{esc(p["summary"])}"}},\n'
        )
        added += 1
if objects:
    data = data.replace(anchor, anchor + "".join(objects), 1)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    data = pat.sub(f'<b>{int(m.group(1)) + added}</b><span>tracked latest entries</span>', data, count=1)

if "lossy-mirror THz around-obstacle imaging" not in data:
    pat24 = re.compile(r'(<div class="tl"><div class="year">2024</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m24 = pat24.search(data)
    if not m24:
        raise RuntimeError("Could not locate 2024 website timeline")
    sentence24 = (
        " Cui and Trichopoulos added active 270–300 GHz lossy-mirror THz around-obstacle imaging with centimeter-scale hidden geometry/pose recovery, while Yasmeen et al. experimentally redirected a 5.5 GHz monostatic radar around a corridor corner using a one-bit RIS for hidden-human micro-Doppler sensing."
    )
    data = data[:m24.start()] + m24.group(1) + m24.group(2) + sentence24 + m24.group(3) + data[m24.end():]

if "single-antenna RIS reflection-matrix imaging" not in data:
    pat25 = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m25 = pat25.search(data)
    if not m25:
        raise RuntimeError("Could not locate 2025 website timeline")
    sentence25 = (
        " Radar/RF NLOS also broadened from ambiguity-aware particle-filter tracking and quantized dual-beam RIS experiments to multi-RIS link-budget-aware target detection and single-antenna RIS reflection-matrix imaging."
    )
    data = data[:m25.start()] + m25.group(1) + m25.group(2) + sentence25 + m25.group(3) + data[m25.end():]
write("data/papers-source.html", data)


# Survey prose: close the THz final-venue gap and extend radar/RIS trajectories.
newscenes = read("article/5newscenes.tex")
if "cuiActiveTHzNLOS2024" not in newscenes:
    old = r"\href{https://arxiv.org/abs/2205.05066}{Cui and Trichopoulos} showed"
    require(newscenes, old, "THz precursor hyperlink")
    newscenes = newscenes.replace(old, r"Cui and Trichopoulos~\cite{cuiActiveTHzNLOS2024} showed", 1)

if "phamParticleFilterAroundCorner2025" not in newscenes:
    old = r"Once this geometry uncertainty is exposed, the problem also becomes one of robust dynamic inference: Wu~\etal~use"
    require(newscenes, old, "radar dynamic-inference paragraph")
    replacement = (
        r"Once this geometry uncertainty is exposed, the problem also becomes one of robust dynamic inference: "
        r"Pham~\etal~explicitly model the multimodal likelihoods created when several multipath hypotheses are difficult to distinguish, and use particle filtering to preserve competing hidden-target states rather than committing to an incorrect path association~\cite{phamParticleFilterAroundCorner2025}. "
        r"Wu~\etal~use"
    )
    newscenes = newscenes.replace(old, replacement, 1)

need_matrix = "goicoecheaSingleAntennaRISNLOS2025" not in newscenes
need_multiris = "liaquatMultiRISNLOS2025" not in newscenes
if need_matrix or need_multiris:
    anchor = "ideal single-beam RIS baselines.\n"
    require(newscenes, anchor, "RIS practical-beam paragraph")
    additions = []
    if need_multiris:
        additions.append(
            r"Liaquat~\etal~extend reconfigurable propagation from a single engineered relay to multi-RIS-assisted monostatic radar, deriving received-power, path-loss, and SNR expressions that quantify when additional programmable surfaces recover blocked sensing links and improve NLOS target detectability~\cite{liaquatMultiRISNLOS2025}."
        )
    if need_matrix:
        additions.append(
            r"Go{\"i}coechea~\etal~move beyond beam redirection to matrix imaging: a single transmit--receive antenna interrogates programmable RIS masks to reconstruct the full reflection matrix, effectively synthesizing an array for hidden-scene imaging, selective focusing through clutter, and moving-target tracking~\cite{goicoecheaSingleAntennaRISNLOS2025}."
        )
    newscenes = newscenes.replace(anchor, anchor + " " + " ".join(additions) + "\n", 1)
write("article/5newscenes.tex", newscenes)


# Top-level survey snapshot date and provenance marker.
tex = read("bare_jrnl.tex")
tex = tex.replace("through 16 August 2026", "through 17 August 2026", 1)
marker = "% 17 August 2026 citation trace: active THz final venue, ambiguity-aware radar tracking, and programmable-RIS sensing/imaging gaps synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Persistent update note: exact scope, provenance, and venue decisions.
note = ROOT / "updates/2026-08-17-thz-ris-matrix-tracking-citation-trace.md"
note.write_text(
    """# 17 August 2026 THz / RIS / radar citation-trace update

## Verified missing or inconsistent works

1. Yiran Cui and Georgios C. Trichopoulos, **Seeing Around Obstacles Using Active Terahertz Imaging**, IEEE Transactions on Terahertz Science and Technology 14(4), 433--445 (2024), DOI 10.1109/TTHZ.2024.3401041. The survey previously mentioned the 2022 arXiv precursor only as a raw hyperlink; this update records the final IEEE journal publication, adds formal bibliography metadata, and makes the THz milestone discoverable in README/V2.
2. Kainat Yasmeen, Debidas Kundu, and Shobha Sundar Ram, **Around-the-Corner Radar Sensing Using Reconfigurable Intelligent Surface**, IEEE MAPCON 2024, DOI 10.1109/MAPCON61407.2024.10923061. The survey and merged bibliography already used the final venue, but the public README/V2 paper corpus lacked the entry; this update closes that cross-artifact gap.
3. Kainat Yasmeen, Shobha Sundar Ram, and Debidas Kundu, **Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface**, IEEE RadarConf25 (2025), pp. 1254--1259, DOI 10.1109/RadarConf2559087.2025.11205052. The survey/bibliography already contain the final RadarConf record; README/V2 are synchronized here rather than labeling the later arXiv upload as the venue.
4. Ba-Huy Pham et al., **“Around-the-Corner” Radar: Particle Filters for Non-Line-of-Sight Target Tracking in the Presence of Ambiguities**, IEEE Transactions on Aerospace and Electronic Systems 61(3), 5505--5519 (2025), DOI 10.1109/TAES.2024.3503560. This is a genuine missing dynamic radar-NLOS work: particle filtering is used to maintain ambiguous multipath target hypotheses instead of forcing brittle path association.
5. Antton Goïcoechea et al., **Single-Antenna Non-Line-of-Sight Matrix Imaging via Reconfigurable Intelligent Surfaces**, arXiv:2512.12359 (2025). A single antenna plus programmable RIS masks reconstructs the full reflection matrix and supports imaging, focusing, and tracking. No final peer-reviewed venue could be verified as of 17 August 2026, so the repository intentionally keeps arXiv as the venue.
6. Salman Liaquat et al., **Improving SNR for NLoS Target Detection Using Multi-RIS-Assisted Monostatic Radar**, IEEE Open Journal of Vehicular Technology 6, 774--789 (2025), DOI 10.1109/OJVT.2025.3547163. The paper broadens the reconfigurable-relay branch to multiple RISs and quantifies NLOS radar received power, path loss, SNR, and target-detection gains.

## Citation-trace context

The run prioritized forward citations and successors of the repository's active optical milestones (Velten 2012, LCT, f--k migration, phasor field), passive computational-periscopy lineage, learned transient methods, and modality-expansion seeds. The fresh 2026 optical/transient hits with strong relevance -- including PICL, 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, geometry-constrained reconstruction, thermal rough-wall NLOS, and the common-model ToF study -- were already represented in the repository. The remaining high-confidence gap therefore lies in the THz/RF trajectory, especially the transition from naturally occurring lossy-mirror relays and ambiguous multipath tracking to controllable RIS relays, multiple programmable surfaces, and RIS-synthesized reflection-matrix imaging.

## Venue policy

Final publisher venues are used whenever verified. In particular, the Yasmeen papers are labeled MAPCON 2024 and RadarConf25 2025 even though later arXiv versions appeared in 2026. Goïcoechea et al. remains arXiv because no accepted/published final venue was verified.

## Synchronization

The integration workflow updates README, the canonical V2 corpus (`data/papers-source.html`), `article/5newscenes.tex`, the merged bibliography, and `bare_jrnl.tex`; then it cleanly rebuilds `bare_jrnl.pdf` and validates cross-artifact titles/citations, final-venue identifiers, undefined citations, PDF text, and first/last-page rendering before pushing the generated public-artifact commit.
""",
    encoding="utf-8",
)

print(f"THz/RIS/radar citation-gap integration applied; canonical corpus additions: {added}")
