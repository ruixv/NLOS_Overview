# Frequency-domain active NLOS citation-trace update — 1 August 2026

A forward-reference and related-work audit around the f-k migration, phasor-field,
non-confocal ellipsoidal-operator, and low-timing-resolution branches identified two
peer-reviewed works absent from the README, homepage explorer, survey prose, and
merged bibliography:

- Weihao Xu, Songmao Chen, Yuyuan Tian, Dingjie Wang, and Xiuqin Su,
  **Fast non-line-of-sight imaging based on product-convolution expansions**,
  *Optics Letters* 47(18), 4680–4683 (2022), DOI `10.1364/OL.469719`.
- Xiaorui Tian, Jingping Yu, Kai Qiao, Meng Tang, Siqi Zhang, and Chenfei Jin,
  **Non-line-of-sight virtual modulated range migration imaging based on
  super-resolution histograms**, *Optics Letters* 50(2), 519–522 (2025),
  DOI `10.1364/OL.542897`.

Both are direct active transient NLOS reconstruction papers. The first accelerates a
general non-confocal, shift-variant ellipsoidal forward/adjoint operator with local
product convolutions, FFTs, and low-rank decompositions. The second combines
deconvolution-modified iterative backprojection and virtual modulated range migration
to recover 50-fold super-resolved histograms from 1 ns measurements before confocal or
non-confocal reconstruction.

The synchronized integration adds final journal metadata and concise summaries to the
README and interactive explorer, places both methods in the active wave/frequency-domain
survey trajectory, adds canonical BibTeX records, regenerates the merged bibliography
and PDF, and checks citations, entry counts, PDF semantics, and first/last-page rendering.
