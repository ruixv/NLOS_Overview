from pathlib import Path
import re

ROOT = Path('.')

TITLES = [
    'Multipath Exploitation-Based 3-D Environmental Perception and NLOS Moving Target Reconstruction for mmWave MIMO Imaging Radar',
    'NLOS Building Layout and Target Estimation in an L-Shaped Corner with Complex Geometries',
    'A Two-Stage NLOS Target Positioning Method Based on 0-1 Non-Coherent Binary Accumulation',
    'A Reflective Surface Estimation Method Based on Multipath Utilization',
    'NLOS Tracking with Distributed Radar Using Multipath-Assisted JPDA',
    'Non-Line-of-Sight Target Localization in Unknown L-Shaped Corridor Based UWB MIMO Radar',
]
KEYS = [
    'zhuMultipathEnvironmentNLOS2026',
    'xueNLOSBuildingLayout2025',
    'wuTwoStageNLOSPositioning2025',
    'luoReflectiveSurfaceMultipath2025',
    'xuDistributedRadarNLOSTracking2025',
    'jiaUnknownCorridorNLOS2025',
]
DOIS = [
    '10.1109/TAES.2025.3647422',
    '10.1109/TIM.2024.3522427',
    '10.1109/TVT.2025.3542117',
    '10.1109/TIM.2025.3541688',
    '10.1109/IGARSS55030.2025.11242772',
    '10.23919/JSEE.2025.000021',
]

README_ROWS = r'''| 2026 | [Multipath Exploitation-Based 3-D Environmental Perception and NLOS Moving Target Reconstruction for mmWave MIMO Imaging Radar](https://doi.org/10.1109/TAES.2025.3647422) — Zhu et al. | IEEE Transactions on Aerospace and Electronic Systems 62, 3569–3587 (2026) | Jointly estimates 3-D environmental/reflector structure and reconstructs NLOS moving targets from mmWave MIMO multipath, transferring estimated reflector parameters into path-oriented hidden-target localization and validating the pipeline experimentally. |
| 2025 | [NLOS Building Layout and Target Estimation in an L-Shaped Corner with Complex Geometries](https://doi.org/10.1109/TIM.2024.3522427) — Xue et al. | IEEE Transactions on Instrumentation and Measurement 74 (2025) | Removes the usual known-layout assumption: tracks multipath ToAs, separates diffraction and first-/second-order reflection paths, localizes the hidden target and reconstructs part of the L-shaped relay geometry with a portable SISO radar. |
| 2025 | [A Two-Stage NLOS Target Positioning Method Based on 0-1 Non-Coherent Binary Accumulation](https://doi.org/10.1109/TVT.2025.3542117) — Wu et al. | IEEE Transactions on Vehicular Technology 74(6), 8866–8878 (2025) | Uses CFAR-derived 0-1 non-coherent binary accumulation and a two-stage estimator to make multipath NLOS target positioning more robust to false alarms and missed detections. |
| 2025 | [A Reflective Surface Estimation Method Based on Multipath Utilization](https://doi.org/10.1109/TIM.2025.3541688) — Luo et al. | IEEE Transactions on Instrumentation and Measurement 74, 1–11 (2025) | Estimates the relay/reflective surface itself from multipath-ellipse tangency, dictionary matching and Kalman smoothing, turning a normally assumed calibration quantity into part of the radar inverse problem. |
| 2025 | [NLOS Tracking with Distributed Radar Using Multipath-Assisted JPDA](https://doi.org/10.1109/IGARSS55030.2025.11242772) — Xu et al. | IEEE IGARSS 2025, 8751–8755 | Extends multipath exploitation from static localization to distributed-radar NLOS tracking with multipath-assisted joint probabilistic data association. |
| 2025 | [Non-Line-of-Sight Target Localization in Unknown L-Shaped Corridor Based UWB MIMO Radar](https://doi.org/10.23919/JSEE.2025.000021) — Jia et al. | Journal of Systems Engineering and Electronics 36(3), 681–693 (2025) | Uses dual backprojection views and diffraction/reflection path-length matching to estimate hidden target positions and the unknown corridor width, remaining effective when some propagation paths are lost. |
'''

INDEX_OBJECTS = r'''    {cat:"latest modality radar mmwave multipath environment reconstruction tracking",title:"Multipath Exploitation-Based 3-D Environmental Perception and NLOS Moving Target Reconstruction for mmWave MIMO Imaging Radar",authors:"Zhu et al.",year:2026,venue:"IEEE TAES 2026",url:"https://doi.org/10.1109/TAES.2025.3647422",key:"Jointly estimates 3-D environmental/reflector structure from weak multipath and transfers the recovered geometry into path-oriented NLOS moving-target reconstruction and localization on measured mmWave MIMO data."},
    {cat:"latest modality radar layout localization",title:"NLOS Building Layout and Target Estimation in an L-Shaped Corner with Complex Geometries",authors:"Xue et al.",year:2025,venue:"IEEE TIM 2025",url:"https://doi.org/10.1109/TIM.2024.3522427",key:"Tracks multipath ToAs and separates diffraction plus first-/second-order reflection paths to jointly localize a hidden target and reconstruct part of an unknown L-shaped building layout."},
    {cat:"latest modality radar localization multipath",title:"A Two-Stage NLOS Target Positioning Method Based on 0-1 Non-Coherent Binary Accumulation",authors:"Wu et al.",year:2025,venue:"IEEE TVT 2025",url:"https://doi.org/10.1109/TVT.2025.3542117",key:"CFAR-derived binary thresholds and 0-1 non-coherent accumulation feed a two-stage NLOS estimator designed to suppress false alarms and missed detections."},
    {cat:"latest modality radar relay geometry multipath",title:"A Reflective Surface Estimation Method Based on Multipath Utilization",authors:"Luo et al.",year:2025,venue:"IEEE TIM 2025",url:"https://doi.org/10.1109/TIM.2025.3541688",key:"Estimates reflective relay geometry from multipath-ellipse tangency, dictionary matching and Kalman smoothing instead of assuming the reflector is known."},
    {cat:"latest modality radar tracking multipath distributed",title:"NLOS Tracking with Distributed Radar Using Multipath-Assisted JPDA",authors:"Xu et al.",year:2025,venue:"IEEE IGARSS 2025",url:"https://doi.org/10.1109/IGARSS55030.2025.11242772",key:"Distributed-radar NLOS tracking incorporates multipath into JPDA data association rather than discarding it as clutter."},
    {cat:"latest modality radar uwb localization layout",title:"Non-Line-of-Sight Target Localization in Unknown L-Shaped Corridor Based UWB MIMO Radar",authors:"Jia et al.",year:2025,venue:"JSEE 2025",url:"https://doi.org/10.23919/JSEE.2025.000021",key:"Dual backprojection views and diffraction/reflection path matching estimate hidden target positions and unknown corridor width even when some multipath components are missing."},
'''

SURVEY_PARAGRAPH = r'''
\vspace{0.8mm}
\noindent \textbf{From assumed relay geometry to joint environment and target inference.}
A parallel radar trajectory removes the common assumption that the reflective environment is known a priori. Luo~\etal~estimate the reflective surface directly from the tangency between the reflector and multipath ellipses, using dictionary matching and temporal smoothing to recover relay geometry from radar measurements~\cite{luoReflectiveSurfaceMultipath2025}. Xue~\etal~jointly recover an NLOS target and part of a complex L-shaped building layout by tracking multipath time-of-arrival sequences and assigning diffraction, first-order reflection, and second-order reflection paths to complementary target- and wall-estimation roles~\cite{xueNLOSBuildingLayout2025}. Jia~\etal~similarly use two backprojection views and path-length consistency to estimate both hidden targets and the width of an unknown L-shaped corridor even when part of the multipath set is missing~\cite{jiaUnknownCorridorNLOS2025}. Once this geometry uncertainty is exposed, the problem also becomes one of robust dynamic inference: Wu~\etal~use CFAR-derived 0--1 non-coherent binary accumulation followed by two-stage positioning to mitigate false alarms and missed detections~\cite{wuTwoStageNLOSPositioning2025}, while Xu~\etal~extend multipath exploitation to distributed-radar tracking with multipath-assisted JPDA~\cite{xuDistributedRadarNLOSTracking2025}. Zhu~\etal~then close this loop by first performing 3-D environmental perception from weak reflector echoes and transferring the inferred reflector parameters into path-oriented NLOS moving-target reconstruction with mmWave MIMO imaging radar~\cite{zhuMultipathEnvironmentNLOS2026}. Together, these works shift RF NLOS from reconstruction under a calibrated relay map toward joint estimation of the environment, propagation paths, hidden-target state, and motion.
'''


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def write(path, text):
    (ROOT / path).write_text(text, encoding='utf-8')


def must_replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly one marker, found {n}')
    return text.replace(old, new, 1)


def append_timeline_sentence(html, year, sentence):
    pattern = re.compile(r'(<div class="tl"><div class="year">' + re.escape(str(year)) + r'</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    matches = list(pattern.finditer(html))
    if len(matches) != 1:
        raise RuntimeError(f'index timeline {year}: expected one entry, found {len(matches)}')
    if sentence in matches[0].group(2):
        return html
    return pattern.sub(lambda m: m.group(1) + m.group(2) + ' ' + sentence + m.group(3), html, count=1)


# README: top-level discovery list and readable development lineage.
readme = read('README.md')
readme = readme.replace('**Update run: 11 August 2026.**', '**Update run: 12 August 2026.**', 1)
if TITLES[0] not in readme:
    marker = '| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n'
    readme = must_replace_once(readme, marker, marker + README_ROWS, 'README latest table')

milestone_anchor = '   │     Lv et al.: mmWave-only relay-reflector reconstruction removes the LiDAR / known-wall prerequisite for around-corner human sensing [INFOCOM]\n'
readme_2025 = (
    '   │     Luo et al.: multipath-ellipse geometry makes the reflective surface itself an estimated radar state [IEEE TIM]\n'
    '   │     Xue et al. and Jia et al.: unknown L-shaped layouts are jointly inferred with hidden targets from diffraction/reflection paths [IEEE TIM / JSEE]\n'
    '   │     Wu et al. and Xu et al.: binary-accumulation positioning and distributed JPDA extend multipath exploitation toward robust NLOS localization and tracking [IEEE TVT / IGARSS]\n'
)
if 'multipath-ellipse geometry makes the reflective surface itself an estimated radar state' not in readme:
    readme = must_replace_once(readme, milestone_anchor, milestone_anchor + readme_2025, 'README 2025 radar milestone')

milestone_2026_anchor = '       │     RISE: AoA/AoD multipath enhancement and hierarchical diffusion enable layout reconstruction and object detection from one static radar [CVPR]\n'
readme_2026 = '       │     Zhu et al.: weak-reflector 3-D environmental perception is coupled to path-oriented NLOS moving-target reconstruction [IEEE TAES]\n'
if 'weak-reflector 3-D environmental perception is coupled to path-oriented NLOS moving-target reconstruction' not in readme:
    readme = must_replace_once(readme, milestone_2026_anchor, milestone_2026_anchor + readme_2026, 'README 2026 radar milestone')
write('README.md', readme)

# Website paper explorer and timeline.
html = read('index.html')
html = html.replace('Updated 11 August 2026 · 210+ papers', 'Updated 12 August 2026 · 210+ papers', 1)
if TITLES[0] not in html:
    m = re.search(r'(const\s+papers\s*=\s*\[\s*\n)', html)
    if not m:
        raise RuntimeError('index.html: const papers array marker not found')
    html = html[:m.end()] + INDEX_OBJECTS + html[m.end():]
html = append_timeline_sentence(
    html, 2025,
    'Reflective-surface estimation and unknown L-shaped-layout reconstruction made relay geometry an inferred state rather than fixed calibration, while binary accumulation and distributed JPDA pushed multipath exploitation toward robust positioning and tracking.'
)
html = append_timeline_sentence(
    html, 2026,
    'Zhu et al. then coupled weak-reflector 3-D environmental perception with path-oriented NLOS moving-target reconstruction, closing the loop from relay estimation to dynamic hidden-target imaging.'
)
actual_count = html.count('{cat:')
stat_pat = re.compile(r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span></div>)')
html, n = stat_pat.subn(lambda m: m.group(1) + str(actual_count) + m.group(2), html, count=1)
if n != 1:
    raise RuntimeError('index.html: tracked-entry stat not found exactly once')
write('index.html', html)

# Survey prose: integrate semantically into the radar subsection.
a5 = read('article/5newscenes.tex')
if KEYS[0] not in a5:
    marker = '\\vspace{0.8mm}\n\\noindent \\textbf{Reconfigurable propagation for physiological NLOS sensing.}'
    a5 = must_replace_once(a5, marker, SURVEY_PARAGRAPH + '\n' + marker, 'article/5newscenes radar insertion')
write('article/5newscenes.tex', a5)

# Maintenance trace in the survey root.
bare = read('bare_jrnl.tex')
comment = '% 12 August 2026 radar citation trace: unknown relay geometry, robust multipath positioning, distributed NLOS tracking, and joint 3-D environment/target reconstruction synchronized.\n'
if not bare.startswith(comment):
    bare = comment + bare
write('bare_jrnl.tex', bare)

# Merge the already verified staging bibliography atomically: all six or none.
bib = read('egbib_merged_20260711.bib')
staged = read('egbib_20260811_radar_multipath_geometry_gap.bib')
present = [bool(re.search(r'^@\\w+\\s*\\{\\s*' + re.escape(k) + r'\\s*,', bib, re.M)) for k in KEYS]
if any(present) and not all(present):
    raise RuntimeError('merged bibliography contains only a subset of the six staged keys; refusing partial merge')
if not any(present):
    for doi in DOIS:
        if doi.lower() in bib.lower():
            raise RuntimeError(f'merged bibliography already contains DOI without expected key: {doi}')
    bib = bib.rstrip() + '\n\n% 12 August 2026 radar unknown-geometry / multipath tracking lineage\n' + staged.strip() + '\n'
write('egbib_merged_20260711.bib', bib)

# Public update note records what is now integrated rather than merely staged.
note = '''# 12 August 2026 — radar unknown-geometry / multipath lineage synchronized\n\nThe six final-venue radar/RF NLOS papers staged on 11 August have now been integrated across the public README, website explorer/timeline, the Radar-Based NLOS Imaging survey narrative, and the merged bibliography. The PDF is rebuilt and validated by the guarded integration workflow before merge.\n\nThe resulting literature trajectory is: **known relay map → reflective-surface estimation → unknown-layout reconstruction → robust multipath localization → distributed NLOS tracking → joint 3-D environment and moving-target reconstruction**.\n\nIntegrated citation keys:\n\n- `zhuMultipathEnvironmentNLOS2026`\n- `xueNLOSBuildingLayout2025`\n- `wuTwoStageNLOSPositioning2025`\n- `luoReflectiveSurfaceMultipath2025`\n- `xuDistributedRadarNLOSTracking2025`\n- `jiaUnknownCorridorNLOS2025`\n\nThe adjacent IEEE IoTJ 2026 through-the-wall joint-layout paper remains intentionally excluded from the main NLOS list because its public framing is TWRI rather than around-corner NLOS.\n'''
write('updates/2026-08-12-radar-geometry-gap-synchronized.md', note)

print(f'Prepared synchronized radar geometry-gap update; website paper count = {actual_count}.')
