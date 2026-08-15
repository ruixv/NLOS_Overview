from pathlib import Path
import re

RUN_DATE='15 August 2026'
RUN_DATE_SHORT='15 Aug 2026'
TITLE='High-resolution non-confocal non-line-of-sight imaging based on spherical-slice transform from spatial and temporal frequency to space and time'
DOI='10.1364/OL.528300'
URL='https://doi.org/10.1364/OL.528300'
KEY='yuSphericalSliceNonconfocalNLOS2024'
AUTHORS='Jingping Yu, Guiyan Xie, Jie Yang, Xiaorui Tian, Xiaojie Shi, Meng Tang, Siqi Zhang, and Chenfei Jin'
AUTHORS_SHORT='Yu et al.'
VENUE='Optics Letters 49(13), 3806–3809 (2024)'
SUMMARY=('Maps non-confocal transient measurements from spatial/temporal frequency to space/time with a spherical-slice transform, '
         'achieving high-resolution reconstruction with reduced artifacts, shape distortion, and position offset; GPU acceleration '
         'reduces reconstruction to several hundred milliseconds for a 32×32 PF32 photon-array camera.')

# README: add a newly discovered final-venue predecessor and place it in the 2024 timeline.
p=Path('README.md'); s=p.read_text(encoding='utf-8')
s=re.sub(r'\*\*Update run: \d{1,2} August 2026\.\*\*',f'**Update run: {RUN_DATE}.**',s,count=1)
anchor='|------|-------|----------------|----------------|'
if s.count(anchor)!=1: raise RuntimeError('README Latest Additions header not unique')
if DOI not in s:
    row=f'| 2024 | [{TITLE}]({URL}) — {AUTHORS_SHORT} | {VENUE} | {SUMMARY} |'
    s=s.replace(anchor,anchor+'\n'+row,1)
if 'spherical-slice transform gives a fast high-resolution non-confocal frequency-domain inverse' not in s:
    # Prefer the ASCII milestone timeline. Insert before the first 2025 marker so chronology stays intact.
    marker='2025 ── Chen et al.: hierarchical-NeRF implicit ray carving makes two-bounce shadow reconstruction more efficient [Optics Express]'
    line='   │     Yu et al.: spherical-slice transform gives a fast high-resolution non-confocal frequency-domain inverse [Optics Letters]\n'
    if marker in s:
        s=s.replace(marker,line+marker,1)
    else:
        # Fallback: preserve the historical-development interpretation before Taxonomy.
        pos=s.find('\n## Taxonomy')
        if pos<0: raise RuntimeError('README timeline/taxonomy anchor missing')
        s=s[:pos]+'\nIn 2024, Yu et al. introduced a spherical-slice frequency-domain transform for fast high-resolution non-confocal transient NLOS reconstruction.\n'+s[pos:]
p.write_text(s,encoding='utf-8')

# Canonical V2 landing page freshness. Paper explorer/graph reads data/papers-source.html.
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=re.sub(r'<span class="pill">Updated \d{1,2} Aug 2026</span>',f'<span class="pill">Updated {RUN_DATE_SHORT}</span>',s,count=1)
p.write_text(s,encoding='utf-8')

# Canonical paper corpus powering graph/trends/explorer.
p=Path('data/papers-source.html'); s=p.read_text(encoding='utf-8')
anchor_match=re.search(r'(\bconst\s+papers\s*=\s*\[\s*\n)',s)
if not anchor_match: raise RuntimeError('paper array anchor missing')
if DOI not in s:
    obj=('      {cat:"latest active transient nonconfocal frequency-domain spherical-slice real-time",title:"'+TITLE.replace('"','\\"')+'",authors:"'+AUTHORS_SHORT+'",year:2024,venue:"'+VENUE+'",url:"'+URL+'",key:"'+SUMMARY.replace('"','\\"')+'"},\n')
    i=anchor_match.end(); s=s[:i]+obj+s[i:]
if 'spherical-slice transform for fast high-resolution non-confocal transient inversion' not in s:
    pat=r'(<div class="tl"><div class="year">2024</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
    m=re.search(pat,s,re.S)
    if m:
        extra=' Yu et al. additionally introduced a spherical-slice transform for fast high-resolution non-confocal transient inversion, providing a frequency-domain precursor to later reference-function phase compensation.'
        s=s[:m.start()]+m.group(1)+m.group(2)+extra+m.group(3)+s[m.end():]
s=re.sub(r'Updated \d{1,2} August 2026',f'Updated {RUN_DATE}',s,count=1)
s=re.sub(r'Last updated: \d{1,2} August 2026',f'Last updated: {RUN_DATE}',s,count=1)
count=len(re.findall(r'\{cat:"',s))
s,n=re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',s,count=1)
if n!=1: raise RuntimeError('tracked-entry stat missing in paper source')
p.write_text(s,encoding='utf-8')

# Survey: integrate into the active reconstruction lineage, not as an appendix/list item.
p=Path('article/2active.tex'); s=p.read_text(encoding='utf-8')
# Add to the active transient reconstruction table if not already present.
if KEY not in s:
    table_anchor='yuNonconfocalPhaseCompensation2026,tianSparseBayesianNLOS2026'
    if table_anchor in s:
        s=s.replace(table_anchor,KEY+',yuNonconfocalPhaseCompensation2026,tianSparseBayesianNLOS2026',1)
    else:
        raise RuntimeError('active-table nonconfocal anchor missing')

para_marker='\\noindent \\textbf{Non-confocal spherical-slice and reference-function frequency-domain inversion.}'
if para_marker not in s:
    anchor='\\vspace{0.8mm}\n\\noindent \\textbf{Nonuniform and scaled Fourier sampling.}'
    if s.count(anchor)!=1: raise RuntimeError('wave-based sampling anchor not unique')
    para=(
        '\\vspace{0.8mm}\n\\noindent \\textbf{Non-confocal spherical-slice and reference-function frequency-domain inversion.}\n'
        'Yu~\\etal~introduced a spherical-slice transform that maps non-confocal transient measurements from spatial and temporal frequency to space and time~\\cite{yuSphericalSliceNonconfocalNLOS2024}. '
        'The formulation directly addresses the lower resolution and scene dependence of earlier non-confocal reconstructions, suppressing artifacts, shape distortion, and position offset while reaching several-hundred-millisecond reconstruction on a GPU for a $32\\times32$ PF32 photon-array measurement. '
        'This 2024 result forms a useful frequency-domain precursor to two later developments from the same non-confocal branch: virtual modulated range migration uses super-resolved histograms to recover resolution from coarse timing hardware~\\cite{tianVirtualRMAHistograms2025}, whereas reference-function phase compensation transfers a single-input/multiple-output frequency-domain formulation to optical NLOS and further reduces phase-induced distortion and artifacts~\\cite{yuNonconfocalPhaseCompensation2026}. '
        'Together, the sequence shows how non-confocal transient NLOS has moved from direct spherical-slice inversion toward timing-resolution recovery and explicit phase compensation without reverting to dense confocal scanning.\n\n'
    )
    s=s.replace(anchor,para+anchor,1)
p.write_text(s,encoding='utf-8')

# Verified final-venue BibTeX.
p=Path('egbib_merged_20260711.bib'); s=p.read_text(encoding='utf-8')
entry='''@article{yuSphericalSliceNonconfocalNLOS2024,
  author = {Yu, Jingping and Xie, Guiyan and Yang, Jie and Tian, Xiaorui and Shi, Xiaojie and Tang, Meng and Zhang, Siqi and Jin, Chenfei},
  doi = {10.1364/OL.528300},
  journal = {Optics Letters},
  number = {13},
  pages = {3806--3809},
  publisher = {Optica Publishing Group},
  title = {High-resolution non-confocal non-line-of-sight imaging based on spherical-slice transform from spatial and temporal frequency to space and time},
  url = {https://doi.org/10.1364/OL.528300},
  volume = {49},
  year = {2024}
}'''
if not re.search(r'@[A-Za-z]+\{'+re.escape(KEY)+r',',s,re.I):
    s=s.rstrip()+'\n\n'+entry+'\n'
kc=len(re.findall(r'@[A-Za-z]+\{'+re.escape(KEY)+r',',s,re.I))
dc=len(re.findall(r'(?im)^\s*doi\s*=\s*\{'+re.escape(DOI)+r'\}\s*,?\s*$',s))
if kc!=1 or dc!=1: raise RuntimeError(f'BibTeX duplicate/absence: key={kc}, doi={dc}')
p.write_text(s,encoding='utf-8')

# Living survey provenance; date is already 15 August 2026 in this run.
p=Path('bare_jrnl.tex'); s=p.read_text(encoding='utf-8')
note='% 15 August 2026 citation trace: missing 2024 spherical-slice non-confocal frequency-domain precursor synchronized.\n'
if note not in s: s=note+s
s=re.sub(r'through \d{1,2} August 2026','through 15 August 2026',s,count=1)
p.write_text(s,encoding='utf-8')

# Update/provenance note.
Path('updates/2026-08-15-nonconfocal-spherical-slice-gap.md').write_text(f'''# Non-confocal spherical-slice lineage synchronized — 15 August 2026

A citation-tracing and publisher-index pass found one final-venue predecessor missing from the public corpus and survey:

- Jingping Yu, Guiyan Xie, Jie Yang, Xiaorui Tian, Xiaojie Shi, Meng Tang, Siqi Zhang, and Chenfei Jin, “{TITLE},” Optics Letters 49(13), 3806–3809 (2024), DOI {DOI}.

The paper maps non-confocal transient measurements from spatial/temporal frequency to space/time via a spherical-slice transform and reports high-resolution, artifact-resistant reconstruction with several-hundred-millisecond GPU runtime for a 32×32 PF32 photon-array camera. The survey now places it before the already-covered 2025 virtual-modulated range-migration work and the 2026 reference-function phase-compensation method, making the non-confocal frequency-domain trajectory explicit.

README, canonical V2 corpus, active-method survey prose/table, merged bibliography, and rebuilt PDF are validated together by the integration workflow.
''',encoding='utf-8')
