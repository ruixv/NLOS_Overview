from pathlib import Path
import re


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly one anchor, found {n}')
    return text.replace(old, new, 1)

# -----------------------------------------------------------------------------
# README: add three verified missing passive-NLOS records and finalize MARMOT.
# -----------------------------------------------------------------------------
readme = read('README.md')

marmot_old = '| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Uses a scanning-pattern mask for self-supervised pretraining on the 500,000-model TransVerse dataset, learning to complete arbitrarily sampled transients and transfer reusable features to downstream NLOS imaging tasks. |'
marmot_new = '| 2026 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://doi.org/10.1007/s44267-026-00125-1) — Shen et al. | Visual Intelligence 4, 22 (2026) | Final journal version of the masked-transient pretraining framework: a scanning-pattern mask supports sparse, irregular, and non-uniform relay sampling, while TransVerse provides one million confocal NLOS transients rendered from 500,000 Objaverse objects for transient completion, reconstruction, classification, albedo estimation, and depth transfer. |'
readme = replace_once(readme, marmot_old, marmot_new, 'README MARMOT venue upgrade')

new_rows = (
    '| 2026 | [Enhanced reflection U-Net reconstruction for passive Non-Line-of-Sight imaging](https://doi.org/10.37188/OPE.20263409.1496) — Yu et al. | Optics and Precision Engineering 34(9), 1496–1506 (2026) | A formally published passive-NLOS U-Net reconstruction study that extends the supervised encoder–decoder branch represented by early passive U-Net/GAN methods and later attention/physics-guided reconstruction. |\n'
    '| 2025 | [Passive Non-Line-of-Sight Imaging via Hyperspectral Autoencoder Net](https://doi.org/10.1117/12.3055610) — Li et al. | Proc. SPIE 13542, 135421R (CITA 2024; published 2025) | HAENet extends Hyper-NLOS with spatial–spectral separation reconstruction and spatial–spectral residual attention, exploiting hyperspectral relay measurements while reducing redundancy across wavelength and spatial dimensions. |\n'
    '| 2024 | [Passive non-line-of-sight imaging for hidden target detection](https://doi.org/10.1117/12.3049350) — Wang et al. | Proc. SPIE 13282, 132820R (AIIP 2024) | A task-oriented passive-NLOS study focused on hidden-target detection, complementing full hidden-image reconstruction and marking the broader shift toward semantic/passive sensing objectives. |\n'
)
for doi in ['10.37188/OPE.20263409.1496', '10.1117/12.3055610', '10.1117/12.3049350']:
    if doi in readme:
        raise RuntimeError(f'README unexpectedly already contains {doi}')
header = '| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n'
readme = replace_once(readme, header, header + new_rows, 'README Latest Additions header')

old_marmot_tl = '   │     Shen et al.: MARMOT shifts transient learning toward reusable masked pretraining on TransVerse, with the retained scan subset acting as arbitrary sampling [arXiv]'
new_marmot_tl = ('   │     Shen et al.: MARMOT shifts transient learning toward reusable masked pretraining on TransVerse, with the retained scan subset acting as arbitrary sampling [Visual Intelligence]\n'
                 '   │     Li et al.: HAENet extends hyperspectral passive NLOS from full-color autoencoding to spatial–spectral separation and residual attention [Proc. SPIE]')
readme = replace_once(readme, old_marmot_tl, new_marmot_tl, 'README MARMOT/HAENet timeline')

hyper_tl = '    │     Chen et al.: Hyper-NLOS introduces wavelength-resolved hyperspectral conditioning, a full-color autoencoder, and spatial–spectral attention for passive hidden-scene reconstruction [Optics Express]'
readme = replace_once(readme, hyper_tl, hyper_tl + '\n    │     Wang et al.: passive hidden-target detection broadens ordinary-camera NLOS from image recovery toward task-oriented hidden-object sensing [Proc. SPIE]', 'README hidden-detection timeline')

dceem_tl = '   │     Wang et al.: DCEEM makes passive feature selection explicitly light-transport-aware, using Bayesian dynamic channel weighting and hierarchical denoising/refinement to suppress low-SNR channel aliasing before vector quantization [Optics Communications]'
readme = replace_once(readme, dceem_tl, dceem_tl + '\n   │     Yu et al.: enhanced-reflection U-Net reconstruction adds a formally published supervised passive-NLOS encoder–decoder branch [Optics and Precision Engineering]', 'README enhanced-U-Net timeline')
write('README.md', readme)

# -----------------------------------------------------------------------------
# Canonical V2 corpus / paper explorer / timeline.
# -----------------------------------------------------------------------------
corpus = read('data/papers-source.html')
old_obj = '{cat:"latest learning active dataset",title:"MARMOT: Masked Autoencoder for Modeling Transient Imaging",authors:"Shen et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2506.08470",key:"Self-supervised masked pretraining for transient/NLOS data and TransVerse-scale data."},'
new_obj = '{cat:"latest learning active dataset",title:"MARMOT: Masked Autoencoder for Modeling Transient Imaging",authors:"Siyuan Shen et al.",year:2026,venue:"Visual Intelligence 4, 22 (2026)",url:"https://doi.org/10.1007/s44267-026-00125-1",key:"Final journal version of MARMOT: masked self-supervised transient pretraining on one million confocal NLOS transients from 500,000 Objaverse objects, supporting sparse/irregular completion and transfer to reconstruction, classification, albedo, and depth tasks."},\n      {cat:"latest passive learning reconstruction",title:"Enhanced reflection U-Net reconstruction for passive Non-Line-of-Sight imaging",authors:"Xiangzhi Yu et al.",year:2026,venue:"Optics and Precision Engineering 34(9), 1496–1506",url:"https://doi.org/10.37188/OPE.20263409.1496",key:"Formally published passive-NLOS U-Net reconstruction study extending the supervised encoder–decoder lineage."},\n      {cat:"latest passive learning hyperspectral",title:"Passive Non-Line-of-Sight Imaging via Hyperspectral Autoencoder Net",authors:"F. Li et al.",year:2025,venue:"Proc. SPIE 13542, 135421R",url:"https://doi.org/10.1117/12.3055610",key:"HAENet uses spatial–spectral separation reconstruction and residual attention to exploit hyperspectral passive-NLOS measurements with reduced spatial/spectral redundancy."},\n      {cat:"latest passive detection semantic",title:"Passive non-line-of-sight imaging for hidden target detection",authors:"Hailu Wang et al.",year:2024,venue:"Proc. SPIE 13282, 132820R",url:"https://doi.org/10.1117/12.3049350",key:"Task-oriented passive-NLOS work focused on hidden-target detection rather than full hidden-image reconstruction."},'
corpus = replace_once(corpus, old_obj, new_obj, 'V2 MARMOT and missing-paper objects')
corpus = replace_once(corpus, '<b>314</b><span>tracked latest entries</span>', '<b>317</b><span>tracked latest entries</span>', 'V2 tracked-count')

old_2024_phrase = 'Hyper-NLOS makes wavelength-resolved hyperspectral diversity an explicit conditioning dimension for passive reconstruction, combining a full-color autoencoder with spatial–spectral attention and the HS-NLOS dataset. Kim and Jang then emphasized robustness to changes in both occluder and hidden-object position in a standard-camera passive system.'
new_2024_phrase = 'Hyper-NLOS makes wavelength-resolved hyperspectral diversity an explicit conditioning dimension for passive reconstruction, combining a full-color autoencoder with spatial–spectral attention and the HS-NLOS dataset. Wang et al. separately broadened passive NLOS toward task-oriented hidden-target detection at AIIP 2024. Kim and Jang then emphasized robustness to changes in both occluder and hidden-object position in a standard-camera passive system.'
corpus = replace_once(corpus, old_2024_phrase, new_2024_phrase, 'V2 2024 passive timeline')

old_2025_phrase = 'White-light physics-enhanced and single-shot speckle methods reduced steady-state acquisition constraints; multispectral clutter separation and hyperspectral band selection strengthened passive reconstruction; CMFormer made transient learning deployable on consumer GPUs.'
new_2025_phrase = 'White-light physics-enhanced and single-shot speckle methods reduced steady-state acquisition constraints; multispectral clutter separation and hyperspectral band selection strengthened passive reconstruction; HAENet further introduced spatial–spectral separation and residual attention for hyperspectral passive NLOS; CMFormer made transient learning deployable on consumer GPUs.'
corpus = replace_once(corpus, old_2025_phrase, new_2025_phrase, 'V2 2025 HAENet timeline')

old_marmot_2025 = 'MARMOT made masked transient pretraining and arbitrary-scan completion reusable across downstream NLOS tasks, while HOLI-1-to-3 combined radiance and transient fields so hidden three-bounce evidence could constrain geometry invisible to a single LOS view.'
new_marmot_2025 = 'The 2025 MARMOT preprint, finalized in Visual Intelligence in 2026, made masked transient pretraining and arbitrary-scan completion reusable across downstream NLOS tasks, while HOLI-1-to-3 combined radiance and transient fields so hidden three-bounce evidence could constrain geometry invisible to a single LOS view.'
corpus = replace_once(corpus, old_marmot_2025, new_marmot_2025, 'V2 MARMOT final-venue timeline note')

old_2026_tail = 'Wang et al. further made passive feature selection explicitly light-transport-aware with DCEEM, combining Bayesian dynamic channel weighting with hierarchical denoising/refinement and vector quantization for low-SNR reconstruction.'</nnew_2026_tail = old_2026_tail + ' Yu et al. added a formally published enhanced-reflection U-Net reconstruction branch for passive NLOS, extending the supervised encoder–decoder lineage alongside attention- and physics-guided models.'
corpus = replace_once(corpus, old_2026_tail, new_2026_tail, 'V2 2026 enhanced-U-Net timeline')
write('data/papers-source.html', corpus)

# -----------------------------------------------------------------------------
# Passive survey: hyperspectral lineage plus task-oriented / U-Net branch.
# -----------------------------------------------------------------------------
passive = read('article/3passive.tex')
hyper_sentence = 'Hyper-NLOS~\\cite{chenHyperNLOS2024} and related multispectral approaches demonstrate that fusing across tens of spectral bands measurably improves reconstruction quality.'
hyper_expanded = ('Hyper-NLOS~\\cite{chenHyperNLOS2024} established hyperspectral wavelength diversity as an explicit conditioning variable for passive reconstruction. '
                  'Li~\\etal~then introduced a hyperspectral autoencoder network (HAENet)~\\cite{liHyperspectralAutoencoderNLOS2025}, combining spatial--spectral separation reconstruction with spatial--spectral residual attention to reduce redundant processing while preserving cross-band context. '
                  'Together with later band-selection and multispectral-unmixing approaches, these works show that wavelength diversity can supply an additional coding dimension when steady-state spatial measurements alone are severely ill-conditioned.')
passive = replace_once(passive, hyper_sentence, hyper_expanded, 'passive hyperspectral lineage')

anchor = '\\vspace{0.8mm}\n\\noindent \\textbf{Light-transport-aware dynamic channel selection.}'
new_para = ('\\vspace{0.8mm}\n'
            '\\noindent \\textbf{Task-oriented detection and enhanced U-Net reconstruction.}\n'
            'Wang~\\etal~reported a passive NLOS formulation centered on hidden-target detection rather than full image recovery~\\cite{wangPassiveHiddenTargetDetection2024}, marking an early task-oriented branch of learned passive sensing. '
            'Yu~\\etal~later published an enhanced-reflection U-Net reconstruction method for passive NLOS~\\cite{yuEnhancedReflectionUNet2026}. '
            'The latter retains the supervised encoder--decoder paradigm while extending the sequence from early passive U-Net/GAN mappings toward the more recent attention-, diffusion-, and light-transport-aware models.\n\n'
            + anchor)
passive = replace_once(passive, anchor, new_para, 'passive detection/U-Net insertion')
write('article/3passive.tex', passive)

# -----------------------------------------------------------------------------
# Data-driven survey: retain citation key but update MARMOT to final publication.
# -----------------------------------------------------------------------------
data = read('article/4datadriven.tex')
old_marmot_prose = ('MARMOT moves reusable representation learning from multi-task supervision to self-supervised transient completion~\\cite{shenMARMOT2025}. '
                    'A Transformer encoder--decoder receives measurements hidden by a scanning-pattern mask; the retained subset is functionally equivalent to an arbitrary relay sampling pattern, and the network predicts the complete transient volume. '
                    'Pretraining on TransVerse, a synthetic collection built from 500,000 three-dimensional models, supports direct feature transfer or decoder fine-tuning for downstream NLOS tasks. '
                    'This development changes the role of a large transient dataset: instead of training one reconstruction mapping, it supplies a modality-level prior that can be adapted across sampling regimes and task heads.')
new_marmot_prose = ('MARMOT moves reusable representation learning from multi-task supervision to self-supervised transient completion~\\cite{shenMARMOT2025}. '
                    'A Transformer encoder--decoder receives measurements hidden by a scanning-pattern mask; the retained subset is functionally equivalent to an arbitrary relay sampling pattern, and the network predicts the complete transient volume. '
                    'In the final Visual Intelligence version, TransVerse contains one million confocal NLOS transients rendered from 500,000 Objaverse objects, enabling pretraining at a scale well beyond earlier task-specific transient datasets. '
                    'The recovered dense transients support sparse-scan NLOS reconstruction, while the pretrained encoder transfers to classification, albedo estimation, and depth estimation. '
                    'This development changes the role of a large transient dataset: instead of training one reconstruction mapping, it supplies a modality-level prior that can be adapted across sampling regimes and task heads.')
data = replace_once(data, old_marmot_prose, new_marmot_prose, 'MARMOT final-publication survey prose')
write('article/4datadriven.tex', data)

# -----------------------------------------------------------------------------
# Bibliography: upgrade MARMOT from arXiv-only to final journal, add 3 gaps.
# -----------------------------------------------------------------------------
bib = read('egbib_merged_20260711.bib')
marmot_pattern = re.compile(r'@misc\{shenMARMOT2025,\n.*?\n\}\n', re.S)
if len(marmot_pattern.findall(bib)) != 1:
    raise RuntimeError('Expected exactly one arXiv MARMOT BibTeX entry')
new_marmot_bib = '''@article{shenMARMOT2025,
  archiveprefix = {arXiv},
  author = {Shen, Siyuan and Wang, Ziheng and Peng, Xingyue and Li, Ruiqian and Sun, Qilin and Li, Shiying and Yu, Jingyi},
  doi = {10.1007/s44267-026-00125-1},
  eprint = {2506.08470},
  journal = {Visual Intelligence},
  note = {Version of record published 18 August 2026; preprint arXiv:2506.08470},
  pages = {22},
  title = {{MARMOT}: Masked Autoencoder for Modeling Transient Imaging},
  url = {https://doi.org/10.1007/s44267-026-00125-1},
  volume = {4},
  year = {2026}
}
'''
bib = marmot_pattern.sub(new_marmot_bib, bib, count=1)

new_bib_entries = '''
@inproceedings{liHyperspectralAutoencoderNLOS2025,
  author = {Li, F. and Miao, F. and Zhang, Y. and Chen, M. and Gao, P. and Chen, P. and Jin, S. and Xu, M. and Liu, H.},
  booktitle = {Fourth International Conference on Computational Imaging ({CITA} 2024)},
  doi = {10.1117/12.3055610},
  pages = {135421R},
  publisher = {SPIE},
  series = {Proceedings of SPIE},
  title = {Passive Non-Line-of-Sight Imaging via Hyperspectral Autoencoder Net},
  url = {https://doi.org/10.1117/12.3055610},
  volume = {13542},
  year = {2025}
}

@article{yuEnhancedReflectionUNet2026,
  author = {Yu, Xiangzhi and Jin, Weiqi and Qiu, Su and Li, Li},
  doi = {10.37188/OPE.20263409.1496},
  journal = {Optics and Precision Engineering},
  number = {9},
  pages = {1496--1506},
  title = {Enhanced Reflection {U-Net} Reconstruction for Passive Non-Line-of-Sight Imaging},
  url = {https://doi.org/10.37188/OPE.20263409.1496},
  volume = {34},
  year = {2026}
}

@inproceedings{wangPassiveHiddenTargetDetection2024,
  author = {Wang, Hailu and Chen, Minsun and Liu, Hao and Lai, Wenchang and Lei, Guozhong and Han, Kai},
  booktitle = {Second Advanced Imaging and Information Processing Conference ({AIIP} 2024)},
  doi = {10.1117/12.3049350},
  pages = {132820R},
  publisher = {SPIE},
  series = {Proceedings of SPIE},
  title = {Passive Non-Line-of-Sight Imaging for Hidden Target Detection},
  url = {https://doi.org/10.1117/12.3049350},
  volume = {13282},
  year = {2024}
}
'''
for doi in ['10.1117/12.3055610', '10.37188/OPE.20263409.1496', '10.1117/12.3049350']:
    if doi.lower() in bib.lower():
        raise RuntimeError(f'Bibliography unexpectedly already contains {doi}')
bib = bib.rstrip() + '\n\n' + new_bib_entries.lstrip()
write('egbib_merged_20260711.bib', bib)

# -----------------------------------------------------------------------------
# Survey provenance marker.
# -----------------------------------------------------------------------------
tex = read('bare_jrnl.tex')
marker = '% 22 August 2026 venue/citation trace: MARMOT finalized in Visual Intelligence; HAENet, passive hidden-target detection, and enhanced-reflection U-Net gaps synchronized.\n'
if marker not in tex:
    tex = marker + tex
write('bare_jrnl.tex', tex)

print('22-Aug citation-trace integration applied successfully.')
