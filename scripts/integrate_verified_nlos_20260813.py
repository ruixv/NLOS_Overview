from pathlib import Path
import re

IG_TITLE='A CROSS-REGIONAL NLOS TARGET LOCALIZATION METHOD BASED ON JOINT MULTIPATH GLRT'
IG_URL='https://2026.ieeeigarss.org/search.php?show=search'
IG_KEY='yuCrossRegionalNLOSGLRT2026'
EU_TITLE='Multipath Ghost Correlation-Based NLOS Target Localization and Building Layuot Estimation'
EU_DOI='10.23919/EUSIPCO63237.2025.11226331'
EU_URL='https://doi.org/'+EU_DOI
EU_KEY='weiMultipathGhostNLOS2025'
FU_TITLE='Building Corner and NLOS Target Parameter Estimation Based on Diffraction Signal Utilization'
FU_DOI='10.23919/FUSION65864.2025.11124177'
FU_URL='https://doi.org/'+FU_DOI
FU_KEY='yuDiffractionCornerNLOS2025'
NR_TITLE='NLOS-R²: Alternate Reconstruction and Recognition for Non-Line-of-Sight Understanding'
NR_DOI='10.1109/ICME59968.2025.11209224'
NR_URL='https://doi.org/'+NR_DOI

# README
p=Path('README.md'); s=p.read_text(encoding='utf-8')
s=s.replace('**Update run: 12 August 2026.**','**Update run: 13 August 2026.**')
header='|------|-------|----------------|----------------|'
if s.count(header)!=1: raise RuntimeError('README latest-additions header not unique')
rows=[]
if IG_TITLE not in s:
    rows.append(f'| 2026 | [{IG_TITLE}]({IG_URL}) — Yu et al. | IEEE IGARSS 2026, paper 2579 (TUP1.PC.9) | Cross-regional NLOS target localization based on a joint multipath GLRT; the official conference program lists the work in Object Detection and Recognition. |')
if EU_DOI not in s:
    rows.append(f'| 2025 | [{EU_TITLE}]({EU_URL}) — Wei et al. | EUSIPCO 2025, 2247–2251 | Uses Range–Doppler multipath separation, IAA DoA estimation, and ghost/layout spatial correlation for joint hidden-target and building-layout inference. |')
if FU_DOI not in s:
    rows.append(f'| 2025 | [{FU_TITLE}]({FU_URL}) — Yu et al. | FUSION 2025, 1–6 | Exploits corner-diffraction information for joint building-corner and NLOS-target parameter estimation. |')
if NR_DOI not in s:
    rows.append(f'| 2025 | [{NR_TITLE}]({NR_URL}) — Wang et al. | IEEE ICME 2025, 1–6 | Alternates passive reconstruction and recognition in a mutual-refinement loop. |')
if rows: s=s.replace(header,header+'\n'+'\n'.join(rows),1)
anchor='   │     Wu et al. and Xu et al.: binary-accumulation positioning and distributed JPDA extend multipath exploitation toward robust NLOS localization and tracking [IEEE TVT / IGARSS]'
if anchor in s and 'joint-multipath GLRT extends localization across scene regions [IGARSS 2026]' not in s:
    s=s.replace(anchor,anchor+'\n   │     Yu et al.: diffraction-signal utilization jointly estimates building-corner and hidden-target parameters [FUSION]\n   │     Wei et al.: multipath-ghost spatial correlation jointly estimates NLOS targets and building layout [EUSIPCO]\n   │     Yu et al.: a joint-multipath GLRT extends localization across scene regions [IGARSS 2026]',1)
p.write_text(s,encoding='utf-8')

# index.html
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=s.replace('Updated 12 August 2026','Updated 13 August 2026').replace('Last updated: 12 August 2026','Last updated: 13 August 2026')
anchor='    const papers=[\n'
if s.count(anchor)!=1: raise RuntimeError('index paper-array anchor not unique')
def obj(cat,title,authors,year,venue,url,key):
    return f'    {{cat:"{cat}",title:"{title}",authors:"{authors}",year:{year},venue:"{venue}",url:"{url}",key:"{key}"}},\n'
items=[]
if IG_TITLE not in s: items.append(obj('latest rf radar nlos localization multipath glrt',IG_TITLE,'Yupeng Yu; Shisheng Guo; Zihan Xu; Zhihao Zhu; Yufei Wei; Yisen Zhou; Guolong Cui',2026,'IEEE IGARSS 2026 · paper 2579 · TUP1.PC.9',IG_URL,'Cross-regional NLOS target localization based on a joint multipath GLRT.'))
if EU_DOI not in s: items.append(obj('latest rf radar nlos localization multipath layout',EU_TITLE,'Yufei Wei; Shisheng Guo; Zihan Xu; Xu Hao; Zhihao Zhu; Yupeng Yu; Yisen Zhou; Guolong Cui',2025,'EUSIPCO 2025 · 2247–2251',EU_URL,'Multipath-ghost/layout correlation for joint target and building-layout inference.'))
if FU_DOI not in s: items.append(obj('latest rf radar nlos localization diffraction corner',FU_TITLE,'Yupeng Yu; Shisheng Guo; Zhihao Zhu; Zihan Xu; Yisen Zhou; Yufei Wei; Guolong Cui',2025,'FUSION 2025 · 1–6',FU_URL,'Diffraction-signal utilization for corner and hidden-target parameter estimation.'))
if NR_DOI not in s: items.append(obj('latest passive learning recognition understanding',NR_TITLE,'Yi Wang; Ruixu Geng; Jiarui Zhang; Xiaolong Du; Yan Chen; Yang Hu',2025,'IEEE ICME 2025 · 1–6',NR_URL,'Alternates reconstruction and recognition for mutual refinement.'))
if items: s=s.replace(anchor,anchor+''.join(items),1)
count=len(re.findall(r'\{cat:"',s))
s,n=re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',s,count=1)
if n!=1: raise RuntimeError('website tracked-entry stat missing')
p.write_text(s,encoding='utf-8')

# survey radar lineage
p=Path('article/5newscenes.tex'); s=p.read_text(encoding='utf-8')
conclusion='Together, these works shift RF NLOS from reconstruction under a calibrated relay map toward joint estimation of the environment, propagation paths, hidden-target state, and motion.'
if conclusion not in s: raise RuntimeError('radar-lineage anchor missing')
if IG_KEY not in s:
    addition='The same lineage is reinforced by recent conference work that isolates complementary propagation cues. Yu~\\etal~exploit corner-diffraction information for joint building-corner and hidden-target parameter estimation~\\cite{'+FU_KEY+'}. Wei~\\etal~separate multipath in Range--Doppler space, estimate direction of arrival and multipath-ghost positions, and use ghost--layout spatial correlation to jointly recover target location and wall parameters~\\cite{'+EU_KEY+'}. At IGARSS~2026, Yu~\\etal~present a cross-regional NLOS target-localization formulation based on a joint multipath generalized likelihood ratio test~\\cite{'+IG_KEY+'}. '
    s=s.replace(conclusion,addition+conclusion,1)
p.write_text(s,encoding='utf-8')

# NLOS-R² display consistency
p=Path('article/4datadriven.tex'); s=p.read_text(encoding='utf-8')
if 'wang2025nlos' not in s: raise RuntimeError('wang2025nlos citation missing')
s=s.replace('NLOS-R~2, which alternates','NLOS-R$^2$, which alternates')
p.write_text(s,encoding='utf-8')

# merged bibliography
p=Path('egbib_merged_20260711.bib'); s=p.read_text(encoding='utf-8')
nr='@inproceedings{wang2025nlos,\n  author = {Wang, Yi and Geng, Ruixu and Zhang, Jiarui and Du, Xiaolong and Chen, Yan and Hu, Yang},\n  booktitle = {2025 IEEE International Conference on Multimedia and Expo (ICME)},\n  doi = {10.1109/ICME59968.2025.11209224},\n  pages = {1--6},\n  publisher = {IEEE},\n  title = {{NLOS-R$^2$}: Alternate Reconstruction and Recognition for Non-Line-of-Sight Understanding},\n  url = {https://doi.org/10.1109/ICME59968.2025.11209224},\n  year = {2025}\n}'
s,n=re.subn(r'@inproceedings\{wang2025nlos,.*?\n\}',lambda m:nr,s,count=1,flags=re.S|re.I)
if n!=1: raise RuntimeError('wang2025nlos BibTeX entry not found')
entries=[]
if FU_KEY not in s: entries.append('@inproceedings{yuDiffractionCornerNLOS2025,\n  author = {Yu, Yupeng and Guo, Shisheng and Zhu, Zhihao and Xu, Zihan and Zhou, Yisen and Wei, Yufei and Cui, Guolong},\n  booktitle = {2025 28th International Conference on Information Fusion (FUSION)},\n  doi = {10.23919/FUSION65864.2025.11124177},\n  pages = {1--6},\n  publisher = {IEEE},\n  title = {Building Corner and NLOS Target Parameter Estimation Based on Diffraction Signal Utilization},\n  url = {https://doi.org/10.23919/FUSION65864.2025.11124177},\n  year = {2025}\n}')
if EU_KEY not in s: entries.append('@inproceedings{weiMultipathGhostNLOS2025,\n  author = {Wei, Yufei and Guo, Shisheng and Xu, Zihan and Hao, Xu and Zhu, Zhihao and Yu, Yupeng and Zhou, Yisen and Cui, Guolong},\n  booktitle = {2025 33rd European Signal Processing Conference (EUSIPCO)},\n  doi = {10.23919/EUSIPCO63237.2025.11226331},\n  pages = {2247--2251},\n  publisher = {IEEE},\n  title = {Multipath Ghost Correlation-Based NLOS Target Localization and Building Layuot Estimation},\n  url = {https://doi.org/10.23919/EUSIPCO63237.2025.11226331},\n  year = {2025}\n}')
if IG_KEY not in s: entries.append('@inproceedings{yuCrossRegionalNLOSGLRT2026,\n  author = {Yu, Yupeng and Guo, Shisheng and Xu, Zihan and Zhu, Zhihao and Wei, Yufei and Zhou, Yisen and Cui, Guolong},\n  booktitle = {2026 IEEE International Geoscience and Remote Sensing Symposium (IGARSS)},\n  note = {Paper 2579, poster TUP1.PC.9, presented 11 August 2026},\n  title = {A Cross-Regional NLOS Target Localization Method Based on Joint Multipath GLRT},\n  url = {https://2026.ieeeigarss.org/search.php?show=search},\n  year = {2026}\n}')
if entries: s=s.rstrip()+'\n\n'+'\n\n'.join(entries)+'\n'
p.write_text(s,encoding='utf-8')

p=Path('bare_jrnl.tex'); s=p.read_text(encoding='utf-8')
note='% 13 August 2026 literature sync: IGARSS 2026 cross-regional multipath GLRT, EUSIPCO ghost-correlation layout inference, FUSION diffraction-driven corner estimation, and NLOS-R^2 final ICME metadata synchronized across public artifacts.\n'
if note not in s: s=note+s
p.write_text(s,encoding='utf-8')
