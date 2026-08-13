from pathlib import Path
import re

TITLE='Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net and Multimodal Fusion With the ANLOS-R Dataset'
DOI='10.1109/ACCESS.2026.3664294'
URL='https://doi.org/'+DOI
KEY='alakusANLOSR2026'
FOLLOW='alakusAcousticMaterialNLOS2026'

# README: add the missing final IEEE Access precursor to Latest Additions.
p=Path('README.md'); s=p.read_text(encoding='utf-8')
s=s.replace('**Update run: 12 August 2026.**','**Update run: 13 August 2026.**')
header='|------|-------|----------------|----------------|'
if s.count(header)!=1: raise RuntimeError('README latest-additions header not unique')
if DOI not in s:
    row=f'| 2026 | [{TITLE}]({URL}) — Alakuş and Türkoğlu | IEEE Access 14, 26983–27004 (2026) | Introduces ANLOS-R, a 1,440-sample wall-mediated acoustic NLOS dataset collected with an 8-speaker/8-microphone multi-position setup, together with attention-U-Net reflection isolation and multimodal spectral-temporal fusion for hidden-material recognition. It is the dataset/multimodal precursor to the later Sensors 2026 wavelet-feature follow-up. |'
    s=s.replace(header,header+'\n'+row,1)
p.write_text(s,encoding='utf-8')

# Canonical V2 homepage: make the living-survey freshness visible without exposing internal graph metrics.
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=s.replace('<span class="pill">Updated through 2026</span>','<span class="pill">Updated 13 Aug 2026</span>')
p.write_text(s,encoding='utf-8')

# Canonical paper corpus used by V2 graph, trends and explorer.
p=Path('data/papers-source.html'); s=p.read_text(encoding='utf-8')
anchor='    const papers=[\n'
if s.count(anchor)!=1: raise RuntimeError('paper array anchor not unique')
if DOI not in s:
    obj='      {cat:"latest modality acoustic dataset learning recognition semantic",title:"'+TITLE+'",authors:"Alakuş and Türkoğlu",year:2026,venue:"IEEE Access 14, 26983–27004 (2026)",url:"'+URL+'",key:"Introduces the 1,440-sample ANLOS-R wall-mediated acoustic dataset and an attention-U-Net reflection-isolation plus multimodal spectral-temporal fusion pipeline for hidden-material recognition; it precedes the later Sensors 2026 wavelet-feature and SHAP study."},\n'
    s=s.replace(anchor,anchor+obj,1)
old='Alakuş and Türkoğlu further use wall-mediated chirp echoes, wavelet–acoustic feature fusion, and explainable recurrent learning to identify nine hidden material classes, extending acoustic NLOS semantics from people and vehicles to physical surface properties.'
if old in s and 'ANLOS-R first established the measured multi-position acoustic dataset' not in s:
    new='ANLOS-R first established the measured multi-position acoustic dataset, attention-U-Net reflection isolation, and multimodal spectral-temporal fusion for hidden-material recognition. '+old
    s=s.replace(old,new,1)
# Keep the legacy source metadata current because V2 uses this file as its corpus source.
s=s.replace('Updated 12 August 2026','Updated 13 August 2026').replace('Last updated: 11 August 2026','Last updated: 13 August 2026')
# Refresh legacy tracked-entry count, which is still useful when inspecting the source directly.
count=len(re.findall(r'\{cat:"',s))
s,n=re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',s,count=1)
if n!=1: raise RuntimeError('tracked-entry stat missing in paper source')
p.write_text(s,encoding='utf-8')

# Survey prose: explicitly distinguish the IEEE Access ANLOS-R precursor from the Sensors follow-up.
p=Path('article/5newscenes.tex'); s=p.read_text(encoding='utf-8')
pattern=r'(\\vspace\{0\.8mm\}\n\\noindent \\textbf\{Material recognition from wall-mediated acoustic echoes\.\}\n).*?(?=\\bookmark\[dest=\\HyperLocalCurrentHref,level=2\]\{Robotic Exploration with NLOS Perception\})'
m=re.search(pattern,s,flags=re.S)
if not m: raise RuntimeError('acoustic material-recognition section anchor missing')
if KEY not in m.group(0):
    body=(m.group(1)+
        'Alaku{\\c{s}} and T{\\"u}rko{\\u{g}}lu first introduced ANLOS-R as a dedicated multi-channel acoustic NLOS dataset and semantic-sensing benchmark~\\cite{'+KEY+'}. '
        'The acquisition uses eight loudspeakers and eight microphones facing a relay wall while the direct path to the target is blocked, records three sensor positions and single-channel, combined/MIMO, and background measurements, and contains 1,440 echo samples. '
        'Their accompanying pipeline isolates target-related reflection regions with an attention-enhanced U-Net and fuses spectral and temporal representations for material classification. '
        'Building on the same acquisition, the subsequent Sensors study~\\cite{'+FOLLOW+'} combines classical acoustic descriptors with multi-scale wavelet energy and entropy into a 70-dimensional representation, uses recurrent models for hidden-material recognition, and adds SHAP-based interpretation. '
        'Together, the two works extend acoustic NLOS from localization and geometry toward dataset-driven material-aware environmental perception.\n\n')
    s=s[:m.start()]+body+s[m.end():]
p.write_text(s,encoding='utf-8')

# Merge verified final-venue BibTeX from the staged entry; then remove the staging file.
p=Path('egbib_merged_20260711.bib'); s=p.read_text(encoding='utf-8')
stage=Path('egbib_20260813_acoustic_anlos_r_gap.bib')
if KEY not in s:
    if not stage.exists(): raise RuntimeError('staged ANLOS-R BibTeX missing')
    staged=stage.read_text(encoding='utf-8')
    mm=re.search(r'@article\{'+re.escape(KEY)+r',.*?\n\}',staged,flags=re.S|re.I)
    if not mm: raise RuntimeError('ANLOS-R BibTeX entry not found in staging file')
    s=s.rstrip()+'\n\n'+mm.group(0).strip()+'\n'
# Strong duplicate checks before writing.
if len(re.findall(r'@[A-Za-z]+\{'+re.escape(KEY)+r',',s,re.I))!=1: raise RuntimeError('ANLOS-R BibTeX key duplication')
if s.lower().count(DOI.lower())!=1: raise RuntimeError('ANLOS-R DOI duplication in merged bibliography')
p.write_text(s,encoding='utf-8')
if stage.exists(): stage.unlink()

# Living survey date/sync note.
p=Path('bare_jrnl.tex'); s=p.read_text(encoding='utf-8')
note='% 13 August 2026 acoustic citation trace: ANLOS-R IEEE Access dataset/multimodal precursor synchronized with the Sensors wavelet-acoustic follow-up.\n'
if note not in s: s=note+s
s=s.replace('through 11 August 2026','through 13 August 2026')
p.write_text(s,encoding='utf-8')

# Mark the old gap note as resolved while retaining provenance.
p=Path('updates/2026-08-13-acoustic-anlos-r-gap.md')
s=p.read_text(encoding='utf-8')
mark='> **Resolved:** integrated into public artifacts and rebuilt survey PDF on 13 August 2026.\n\n'
if mark not in s: s=s.replace('# 13 August 2026 — acoustic ANLOS-R gap\n','# 13 August 2026 — acoustic ANLOS-R gap\n\n'+mark,1)
p.write_text(s,encoding='utf-8')
