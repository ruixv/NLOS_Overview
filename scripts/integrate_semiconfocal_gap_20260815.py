from pathlib import Path
import re

RUN_DATE='15 August 2026'
RUN_DATE_SHORT='15 Aug 2026'
TITLE='Converting non-confocal measurements into semi-confocal ones with timing-accuracy improving for non-line-of-sight imaging'
DOI='10.1016/j.optlaseng.2024.108067'
URL='https://doi.org/10.1016/j.optlaseng.2024.108067'
KEY='zhengSemiConfocalNLOS2024'
AUTHORS='Yue Zheng, Wenbo Wang, Chenghang Zhang, Yexin Zhang, Qi Zhang, and Lijing Li'
AUTHORS_SHORT='Zheng et al.'
VENUE='Optics and Lasers in Engineering 176, 108067 (2024)'
SUMMARY=('Transforms point-illumination/SPAD-array non-confocal measurements into semi-confocal histograms with sectionalized-ellipsoid interpolation, '
         'using spatial information to improve effective timing accuracy and connect efficient array acquisition to established confocal LCT/f-k reconstruction.')

# README: newly discovered final-venue bridge between SPAD-array non-confocal capture and confocal solvers.
p=Path('README.md'); s=p.read_text(encoding='utf-8')
s=re.sub(r'\*\*Update run: \d{1,2} August 2026\.\*\*',f'**Update run: {RUN_DATE}.**',s,count=1)
anchor='|------|-------|----------------|----------------|'
if s.count(anchor)!=1: raise RuntimeError('README Latest Additions header not unique')
if DOI not in s:
    row=f'| 2024 | [{TITLE}]({URL}) — {AUTHORS_SHORT} | {VENUE} | {SUMMARY} |'
    s=s.replace(anchor,anchor+'\n'+row,1)
if 'sectionalized-ellipsoid interpolation converts SPAD-array non-confocal data into semi-confocal histograms' not in s:
    marker='   │     Yu et al.: spherical-slice transform gives a fast high-resolution non-confocal frequency-domain inverse [Optics Letters]'
    line='   │     Zheng et al.: sectionalized-ellipsoid interpolation converts SPAD-array non-confocal data into semi-confocal histograms [Optics and Lasers in Engineering]\n'
    if marker in s:
        s=s.replace(marker,line+marker,1)
    else:
        pos=s.find('\n## Taxonomy')
        if pos<0: raise RuntimeError('README timeline/taxonomy anchor missing')
        s=s[:pos]+'\nIn 2024, Zheng et al. converted SPAD-array non-confocal measurements into timing-refined semi-confocal histograms via sectionalized-ellipsoid interpolation.\n'+s[pos:]
p.write_text(s,encoding='utf-8')

# Canonical homepage freshness.
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=re.sub(r'<span class="pill">Updated \d{1,2} Aug 2026</span>',f'<span class="pill">Updated {RUN_DATE_SHORT}</span>',s,count=1)
p.write_text(s,encoding='utf-8')

# Canonical V2 paper corpus.
p=Path('data/papers-source.html'); s=p.read_text(encoding='utf-8')
anchor_match=re.search(r'(\bconst\s+papers\s*=\s*\[\s*\n)',s)
if not anchor_match: raise RuntimeError('paper array anchor missing')
if DOI not in s:
    obj=('      {cat:"latest active transient nonconfocal spad-array semi-confocal timing interpolation",title:"'+TITLE.replace('"','\\"')+'",authors:"'+AUTHORS_SHORT+'",year:2024,venue:"'+VENUE+'",url:"'+URL+'",key:"'+SUMMARY.replace('"','\\"')+'"},\n')
    i=anchor_match.end(); s=s[:i]+obj+s[i:]
if 'sectionalized-ellipsoid interpolation converted SPAD-array non-confocal measurements into timing-refined semi-confocal histograms' not in s:
    pat=r'(<div class="tl"><div class="year">2024</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
    m=re.search(pat,s,re.S)
    if m:
        extra=' Zheng et al. used sectionalized-ellipsoid interpolation to convert SPAD-array non-confocal measurements into timing-refined semi-confocal histograms, reconnecting efficient array acquisition to LCT/f-k-style confocal solvers.'
        s=s[:m.start()]+m.group(1)+m.group(2)+extra+m.group(3)+s[m.end():]
s=re.sub(r'Updated \d{1,2} August 2026',f'Updated {RUN_DATE}',s,count=1)
s=re.sub(r'Last updated: \d{1,2} August 2026',f'Last updated: {RUN_DATE}',s,count=1)
count=len(re.findall(r'\{cat:"',s))
s,n=re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',s,count=1)
if n!=1: raise RuntimeError('tracked-entry stat missing in paper source')
p.write_text(s,encoding='utf-8')

# Survey table + semantically placed non-confocal acquisition/reconstruction bridge.
p=Path('article/2active.tex'); s=p.read_text(encoding='utf-8')
if KEY not in s:
    table_anchor='yuSphericalSliceNonconfocalNLOS2024,yuNonconfocalPhaseCompensation2026'
    if table_anchor in s:
        s=s.replace(table_anchor,KEY+',yuSphericalSliceNonconfocalNLOS2024,yuNonconfocalPhaseCompensation2026',1)
    else:
        raise RuntimeError('active-table nonconfocal lineage anchor missing')

para_marker='\\noindent \\textbf{Confocalizing SPAD-array non-confocal measurements.}'
if para_marker not in s:
    anchor='\\vspace{0.8mm}\n\\noindent \\textbf{Non-confocal spherical-slice and reference-function frequency-domain inversion.}'
    if s.count(anchor)!=1: raise RuntimeError('spherical-slice lineage anchor not unique')
    para=(
        '\\vspace{0.8mm}\n\\noindent \\textbf{Confocalizing SPAD-array non-confocal measurements.}\n'
        'A practical route to faster transient acquisition is to replace rastered point detection with a SPAD array, but fixed point illumination and array detection naturally produce non-confocal ellipsoidal measurements for which the fastest confocal inverses are not directly applicable. '
        'Zheng~\\etal~addressed this acquisition--inversion mismatch with sectionalized-ellipsoid interpolation (SEI)~\\cite{zhengSemiConfocalNLOS2024}. The method partitions each non-confocal ellipsoidal constraint into spatial slices and maps those slices into an emulated semi-confocal histogram, using spatial information to refine the effective temporal sampling beyond the detector-bin spacing. '
        'Simulation and measured experiments show improved separation of closely spaced structures relative to filtered backprojection and conventional normal-moveout correction. More importantly, the conversion makes high-throughput SPAD-array measurements compatible with mature confocal back ends such as LCT and $f$--$k$ migration. This work therefore bridges acquisition-side parallelism and reconstruction-side fast transforms, and provides a complementary 2024 route to the direct non-confocal frequency-domain inversion discussed next.\n\n'
    )
    s=s.replace(anchor,para+anchor,1)
p.write_text(s,encoding='utf-8')

# Verified final-venue BibTeX.
p=Path('egbib_merged_20260711.bib'); s=p.read_text(encoding='utf-8')
entry='''@article{zhengSemiConfocalNLOS2024,
  author = {Zheng, Yue and Wang, Wenbo and Zhang, Chenghang and Zhang, Yexin and Zhang, Qi and Li, Lijing},
  doi = {10.1016/j.optlaseng.2024.108067},
  journal = {Optics and Lasers in Engineering},
  pages = {108067},
  publisher = {Elsevier},
  title = {Converting non-confocal measurements into semi-confocal ones with timing-accuracy improving for non-line-of-sight imaging},
  url = {https://doi.org/10.1016/j.optlaseng.2024.108067},
  volume = {176},
  year = {2024}
}'''
if not re.search(r'@[A-Za-z]+\{'+re.escape(KEY)+r',',s,re.I):
    s=s.rstrip()+'\n\n'+entry+'\n'
kc=len(re.findall(r'@[A-Za-z]+\{'+re.escape(KEY)+r',',s,re.I))
dc=len(re.findall(r'(?im)^\s*doi\s*=\s*\{'+re.escape(DOI)+r'\}\s*,?\s*$',s))
if kc!=1 or dc!=1: raise RuntimeError(f'BibTeX duplicate/absence: key={kc}, doi={dc}')
p.write_text(s,encoding='utf-8')

# Living survey provenance; date stays 15 August 2026.
p=Path('bare_jrnl.tex'); s=p.read_text(encoding='utf-8')
note='% 15 August 2026 citation trace: missing semi-confocal conversion bridge for SPAD-array non-confocal capture synchronized.\n'
if note not in s: s=note+s
s=re.sub(r'through \d{1,2} August 2026','through 15 August 2026',s,count=1)
p.write_text(s,encoding='utf-8')

Path('updates/2026-08-15-semiconfocal-nonconfocal-gap.md').write_text(f'''# Semi-confocal conversion lineage synchronized — 15 August 2026

A citation-tracing pass from LCT/f-k and recent non-confocal NLOS papers exposed one final-venue 2024 acquisition/reconstruction bridge missing from the public corpus:

- Yue Zheng, Wenbo Wang, Chenghang Zhang, Yexin Zhang, Qi Zhang, and Lijing Li, “{TITLE},” Optics and Lasers in Engineering 176, 108067 (2024), DOI {DOI}.

The work converts fixed-illumination/SPAD-array non-confocal ellipsoidal measurements into timing-refined semi-confocal histograms using sectionalized-ellipsoid interpolation. This links parallel detector-array acquisition to mature confocal LCT/f-k reconstruction and complements the separately synchronized direct spherical-slice non-confocal inversion of Yu et al. (Optics Letters 2024).

README, canonical V2 corpus, active-method survey prose/table, merged bibliography, and rebuilt PDF are validated together by the integration workflow.
''',encoding='utf-8')
