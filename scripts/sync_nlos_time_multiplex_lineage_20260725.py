#!/usr/bin/env python3
"""Integrate the few-channel and time-multiplexed active-NLOS lineage.

The update is idempotent and fail-closed. It adds only records absent from each
public artifact, preserves existing bibliography keys, places the papers in the
active acquisition/tracking discussion, and leaves PDF rebuilding to CI.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
SURVEY = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-25-time-multiplex-lineage.md"
KEYS = ROOT / "updates" / "2026-07-25-time-multiplex-lineage-keys.txt"
TRACE = "% 25 July 2026 citation trace: few-channel hidden-size inference, single-channel time-multiplexed tracking, and time-multiplexed NLOS imaging synchronized."

PAPERS = [
    dict(
        key="liTimeMultiplexingNLOS2025",
        title="Time-multiplexing non-line-of-sight imaging",
        authors="Li et al.", year=2025, venue="Chinese Optics Letters 2025",
        url="https://doi.org/10.3788/COL202523.071102", doi="10.3788/COL202523.071102",
        cats="latest active acquisition transient time-multiplexing efficient scanning",
        summary="Introduces delayed multi-beam temporal multiplexing so one time-resolved channel separates echoes from multiple relay points; the proof-of-concept system reconstructs hidden scenes with half the conventional relay scans.",
        bib=r'''@article{liTimeMultiplexingNLOS2025,
  author = {Li, Tailin and Zheng, Xianmin and Zhao, Kaiyuan and Li, Min and Xia, Shiye and Liu, Yaqing and Ren, Ge and Luo, Yihan},
  title = {Time-Multiplexing Non-Line-of-Sight Imaging},
  journal = {Chinese Optics Letters},
  volume = {23},
  number = {7},
  pages = {071102},
  year = {2025},
  publisher = {Chinese Laser Press},
  doi = {10.3788/COL202523.071102},
  url = {https://doi.org/10.3788/COL202523.071102}
}'''),
    dict(
        key="zhengSingleChannelTimeMultiplexNLOS2024",
        title="Non-Line-of-Sight Target Tracking With a Single Time Multiplexed Channel",
        authors="Zheng et al.", year=2024, venue="IEEE Photonics Journal 2024",
        url="https://doi.org/10.1109/JPHOT.2024.3471070", doi="10.1109/JPHOT.2024.3471070",
        cats="latest active tracking transient single-photon time-multiplexing low-cost",
        summary="Uses two delayed illumination paths to encode multiple hidden-target echoes into one single-pixel single-photon histogram, enabling centimeter-precision positioning and tracking with a single time-correlated detection channel.",
        bib=r'''@article{zhengSingleChannelTimeMultiplexNLOS2024,
  author = {Zheng, Xianmin and Li, Tailin and Luo, Yihan and Ding, Ke},
  title = {Non-Line-of-Sight Target Tracking With a Single Time Multiplexed Channel},
  journal = {IEEE Photonics Journal},
  volume = {16},
  number = {6},
  pages = {1--6},
  year = {2024},
  publisher = {IEEE},
  doi = {10.1109/JPHOT.2024.3471070},
  url = {https://doi.org/10.1109/JPHOT.2024.3471070}
}'''),
    dict(
        key="liFewChannelSizeNLOS2024",
        title="Non-line-of-sight target 2D size detection with few channels at a time",
        authors="Li et al.", year=2024, venue="Expert Systems with Applications 2024",
        url="https://doi.org/10.1016/j.eswa.2023.122996", doi="10.1016/j.eswa.2023.122996",
        cats="latest active sensing recognition few-channel learning size detection",
        summary="Learns a rectangle-based mapping from only two or three transient detection channels to hidden-target width and height, extending scan-free few-channel NLOS from localization to coarse 2D size inference rather than full scene reconstruction.",
        bib=r'''@article{liFewChannelSizeNLOS2024,
  author = {Li, Tailin and Luo, Yihan and Zhao, Kaiyuan and Liu, Yaqing and Xia, Shiye and Ren, Ge and Xie, Zongliang},
  title = {Non-Line-of-Sight Target 2D Size Detection with Few Channels at a Time},
  journal = {Expert Systems with Applications},
  volume = {246},
  pages = {122996},
  year = {2024},
  publisher = {Elsevier},
  doi = {10.1016/j.eswa.2023.122996},
  url = {https://doi.org/10.1016/j.eswa.2023.122996}
}'''),
]


def read(path):
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write(path, text):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def entry_span(text, key):
    m = re.search(r"(?mi)^@(article|inproceedings|misc|incollection)\{" + re.escape(key) + r",", text)
    if not m:
        return None
    pos, depth = m.end(), 1
    while pos < len(text) and depth:
        depth += (text[pos] == "{") - (text[pos] == "}")
        pos += 1
    if depth:
        raise SystemExit(f"Unbalanced BibTeX entry: {key}")
    return m.start(), pos


def key_for_doi(text, doi):
    for m in re.finditer(r"(?mi)^@(article|inproceedings|misc|incollection)\{([^,]+),", text):
        key = m.group(2)
        span = entry_span(text, key)
        if span and doi.lower() in text[span[0]:span[1]].lower():
            return key
    return None


def upsert_bib(text, paper):
    key = key_for_doi(text, paper["doi"]) or paper["key"]
    span = entry_span(text, key)
    if span:
        if key == paper["key"]:
            text = text[:span[0]] + paper["bib"] + text[span[1]:]
    else:
        text = text.rstrip() + "\n\n" + paper["bib"] + "\n"
    return text, key


readme, index = read(README), read(INDEX)
active, survey, bib = read(ACTIVE), read(SURVEY), read(BIB)
resolved = {}
for paper in PAPERS:
    bib, resolved[paper["key"]] = upsert_bib(bib, paper)

# README latest additions.
header = "|------|-------|----------------|----------------|\n"
if readme.count(header) != 1:
    raise SystemExit("README Latest Additions header is ambiguous")
rows = []
for paper in PAPERS:
    count = readme.lower().count(paper["title"].lower())
    if count == 0:
        rows.append(f'| {paper["year"]} | [{paper["title"]}]({paper["url"]}) — {paper["authors"]} | {paper["venue"]} | {paper["summary"]} |')
    elif count > 1:
        raise SystemExit(f'Duplicate README title: {paper["title"]}')
if rows:
    readme = readme.replace(header, header + "\n".join(rows) + "\n", 1)

# Website explorer and tracked count.
anchor = "    const papers=[\n" if "    const papers=[\n" in index else "    const papers = [\n"
if index.count(anchor) != 1:
    raise SystemExit("Website paper-array anchor is ambiguous")
objects, inserted = [], 0
for paper in PAPERS:
    count = index.lower().count(paper["title"].lower())
    if count == 0:
        objects.append(f'      {{cat:"{paper["cats"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{paper["summary"]}"}},')
        inserted += 1
    elif count > 1:
        raise SystemExit(f'Duplicate website title: {paper["title"]}')
if objects:
    index = index.replace(anchor, anchor + "\n".join(objects) + "\n", 1)
counts = re.findall(r'<b>(\d+)</b><span>tracked latest entries</span>', index)
if len(counts) != 1:
    raise SystemExit("Website tracked-entry count is ambiguous")
new_count = int(counts[0]) + inserted
index = re.sub(r'<b>\d+</b><span>tracked latest entries</span>', f'<b>{new_count}</b><span>tracked latest entries</span>', index, count=1)

# Add concise historical trajectory sentences.
def append_timeline(text, year, sentence):
    pat = re.compile(r'(<div class="tl"><div class="year">' + str(year) + r'</div><div class="tl-body">.*?<p>)(.*?)(</p>)', re.S)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"Website {year} timeline anchor is missing")
    if sentence.strip() in m.group(2):
        return text
    return text[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + text[m.end():]

index = append_timeline(index, 2024, " Few-channel transient sensing then progressed from rectangle-based 2D size inference with two or three detectors to centimeter-precision tracking with one temporally multiplexed single-photon channel.")
index = append_timeline(index, 2025, " Time-multiplexed illumination subsequently encoded multiple relay samples into one detector timeline and demonstrated hidden-scene imaging with half the relay scans.")

# Active system table: classify size/tracking as sensing, and imaging as reconstruction.
tracking_key = resolved["zhengSingleChannelTimeMultiplexNLOS2024"]
size_key = resolved["liFewChannelSizeNLOS2024"]
imaging_key = resolved["liTimeMultiplexingNLOS2025"]
tracking_row = r"\cite{chanNonlineofsightTrackingPeople2017a,celebiHumanDetectionNLOS2026}(long range),\cite{caramazzaNeuralNetworkIdentification2017,musarraDetectionIdentificationTracking2019}(single point)"
if tracking_key not in active or size_key not in active:
    if active.count(tracking_row) != 1:
        raise SystemExit("Active detection/tracking table row is ambiguous")
    active = active.replace(tracking_row, tracking_row + f",\\cite{{{tracking_key},{size_key}}}(few/time-multiplexed channels)", 1)

spad_row = r"\cite{buttafavaNonlineofsightImagingUsing2015,laurenzisMultiplereturnSinglephotonCounting2015,heideNonlineofsightImagingPartial2017,jinReconstructionMultipleNonlineofsight2018,arellanoFastBackprojectionNonline2017,mannaErrorBackprojectionAlgorithms2018,otooleConfocalNonlineofsightImaging2018,Lindell:2019:Wave,tsaiVolumetricAlbedoSurface2019,pediredlaSNLOSNonlineofsightScanning2019,xinTheoryFermatPaths2019,musarraNonlineofsight3DImaging2019,liuVirtualWaveOptics2018,liuPhasorFieldDiffraction2020,Ahn_2019_ICCV,chopiteDeepNonLineofSightReconstruction2020,Young:2020:dlct,iseringhausen:2018,mannaNonlineofsightimagingUsingDynamic2020,liMambaTemporalConsistency2024,chen_learned_2020,yuLearnableInverseKernel2023,wuNonLineofsightImaging2021,yeCompressedSensingActive2021,isogawaTransientSinograms2020,wuMiniaturizedTCSPC2024,liuGeometricConstrainedNLOS2025,grauOcclusionFields2022,choiSelfCalibratingNLOS2023,guFastNLOSNonPlanar2023,sultanOptimizedSamplingNLOS2025,liDeepNLOSUnderscanning2023,yinAllDayNLOS2026,gaoLearnedLCT2026,sunTransVID2026,weiMultiSurfaceNLOS2025,luesiaStereoNLOS2026,zengCompactLongRangeNLOS2026,yangModelDecompositionNLOS2026,oyamaAdaptiveSpiralNLOS2026,wangLaserReflectiveTomography2026,yuNonconfocalPhaseCompensation2026,tianSparseBayesianNLOS2026,zhouPolarizationSpeckleNLOS2026,miaoLaserPulseMultiplexingNLOS2026,weiQuasiFresnelNLOS2025,zhangFrequencyMoENLOS2026,chenCannyArtifactNLOS2026,shiSpecularFlightPathNLOS2026,sunCUDAIrregularRelayNLOS2026,garciaPueyoForwardInversePhasor2025,pueyoTimeGatedPolarization2024,sultanAccurateTransportModel2024,redoSanchezCohesiveDiracNLOS2024,luesiaZeroPhasePhasor2025,marcoVirtualLightTransport2021,sultanIteratingTLTM2026,liFirstPhotonStamping2022}"
if imaging_key not in active:
    if active.count(spad_row) != 1:
        raise SystemExit("Active SPAD reconstruction table row is ambiguous")
    active = active.replace(spad_row, spad_row[:-1] + "," + imaging_key + "}", 1)

# Semantic survey insertion after first-photon acquisition.
heading = r"\noindent \textbf{From few-channel inference to time-multiplexed imaging.}"
if heading not in active:
    insert_anchor = "\n\n\\vspace{0.8mm}\n\\noindent \\textbf{Pulsed laser}"
    if active.count(insert_anchor) != 1:
        raise SystemExit("Time-multiplex literature insertion anchor is ambiguous")
    prose = f'''\n\n\\vspace{{0.8mm}}
\\noindent \\textbf{{From few-channel inference to time-multiplexed imaging.}}
Li~\\etal~showed that dense relay scanning is not necessary when the desired output is a coarse target descriptor: a rectangle-based multilayer perceptron maps only two or three transient channels to hidden-target width and height~\\cite{{{size_key}}}. Zheng~\\etal~then introduced delayed multi-beam illumination so that echoes from two relay points occupy separable windows in one single-pixel single-photon histogram, enabling centimeter-precision positioning and motion tracking with a single time-correlated channel~\\cite{{{tracking_key}}}. The subsequent imaging system generalized this coding idea from target state estimation to hidden-scene reconstruction: delayed illumination channels multiplex several relay samples onto one detector timeline and halve the demonstrated scan count~\\cite{{{imaging_key}}}. This trajectory distinguishes three levels of information recovery---coarse size, position and motion, and reconstructed appearance---while showing that acquisition complexity can be reduced by optical temporal coding rather than only by learned transient completion or detector arrays.
'''
    active = active.replace(insert_anchor, prose + insert_anchor, 1)

if TRACE not in survey:
    marker = "%% bare_jrnl.tex\n"
    if survey.count(marker) != 1:
        raise SystemExit("Survey trace anchor is ambiguous")
    survey = survey.replace(marker, marker + TRACE + "\n", 1)

# Final checks.
for paper in PAPERS:
    if readme.lower().count(paper["title"].lower()) != 1:
        raise SystemExit(f'README title count invalid: {paper["title"]}')
    if index.lower().count(paper["title"].lower()) != 1:
        raise SystemExit(f'Website title count invalid: {paper["title"]}')
for key in (size_key, tracking_key, imaging_key):
    if not entry_span(bib, key):
        raise SystemExit(f"Missing bibliography key: {key}")
    if f"\\cite{{{key}" not in active and f",{key}" not in active:
        raise SystemExit(f"Missing active-survey citation: {key}")

note = f'''# Few-channel and time-multiplexed active-NLOS lineage — 25 July 2026

Citation tracing from the Velten, LCT, f-k migration, Fermat-path, phasor-field, and keyhole-imaging lineage identified three previously uncovered papers. The sequence moves from scan-free 2D hidden-target size inference with two or three detector channels, to one-channel temporally multiplexed target tracking, to temporally multiplexed hidden-scene imaging with half the demonstrated relay scans.

The records are integrated in README, the website explorer and 2024/2025 timeline, the active-system table, the single-photon acquisition discussion, and the consolidated bibliography. Website tracked-entry count after synchronization: {new_count}. The tracking and size papers are explicitly categorized as sensing/inference rather than full 3D reconstruction.
'''

for path, text in ((README, readme), (INDEX, index), (ACTIVE, active), (SURVEY, survey), (BIB, bib), (NOTE, note)):
    write(path, text)
write(KEYS, "\n".join((size_key, tracking_key, imaging_key)) + "\n")
print(f"Time-multiplexed NLOS lineage synchronized; website count={new_count}.")
