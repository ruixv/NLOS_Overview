#!/usr/bin/env python3
"""Finalize the 2026 website timeline after all July synchronizers have run."""
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "index.html"
text = path.read_text(encoding="utf-8")
pattern = re.compile(r'^\s*<div class="tl"><div class="year">2026</div>.*$', re.MULTILINE)
replacement = '      <div class="tl"><div class="year">2026</div><div class="tl-body"><strong>Deployable sensing, stereo relay geometry, learned physical operators, sparse real-time optimization, dynamic transient completion, thermal/passive reconstruction, consumer LiDAR, and RF geometry</strong><p>PICL and learned LCT embed detector and inverse physics in trainable models; TransVID densifies dynamic transient video; NLOSFormer, MDUNet, and diffuse-aware attention broaden passive sensing; stereo phasor-field acquisition uses two relay walls to reduce the missing cone and recover orientation cues; MD-NLOS decomposes sparse non-negative inversion for rapid reconstruction; compact gated-SPAD hardware reaches kilometer-scale daylight operation; consumer LiDAR and radar/LiDAR benchmarks broaden deployable modalities; and Gaussian transient rendering supports arbitrary relay geometry.</p></div></div>'
if len(pattern.findall(text)) != 1:
    raise RuntimeError("Expected exactly one 2026 website timeline row")
text = pattern.sub(replacement, text, count=1)
path.write_text(text, encoding="utf-8")
print("Finalized the 2026 website timeline.")
