# 2026-10-13 NLOS integration status

Verified: Shi et al., Optics Express 32(6), 10104-10118 (2024), DOI 10.1364/OE.519222. Passive multi-object reconstruction through a large transmissive window, cited in ECCV 2024 Domain Reduction Strategy.

Integrated in README.md, data/papers-source.html, index.html, article/3passive.tex, and egbib_merged_20260711.bib. The survey main file imports article/3passive.tex. Audit: 629 bibliography keys, 979 citations, no missing or duplicate keys.

PDF pending: bare_jrnl.pdf remains blob 6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6. Complete repository checkout unavailable in build container; PDF not compiled/uploaded. In a complete checkout run latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex, validate the result, commit the PDF, and verify the new SHA.
