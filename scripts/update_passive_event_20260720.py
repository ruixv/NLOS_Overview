#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "article/3passive.tex"
text = path.read_text(encoding="utf-8")
key = "wangEventEnhancedPassiveNLOS2024"

if key not in text:
    row_anchor = (
        "   \\cite{sunAdaptiveMotionNLOS2025} & Ambient light & Conventional RGB camera & "
        "Temporal relay-wall motion & Action recognition\\\\%%%% Table body\n"
    )
    event_row = (
        "   \\cite{wangEventEnhancedPassiveNLOS2024} & Ambient/incoherent illumination & "
        "Event camera + conventional camera & Asynchronous diffusion-pattern motion with "
        "physics-embedded learning & Dynamic 2D reconstruction\\\\%%%% Table body\n"
    )
    if text.count(row_anchor) != 1:
        raise RuntimeError(f"Passive table anchor count: {text.count(row_anchor)}")
    text = text.replace(row_anchor, row_anchor + event_row, 1)

heading = "\\noindent \\textbf{Event-camera passive NLOS for moving objects.}"
if heading not in text:
    next_heading = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Structure-guided adaptive total variation.}"
    )
    prose = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Event-camera passive NLOS for moving objects.}\n"
        "Wang~\\etal~introduced an event-enhanced passive NLOS prototype that records "
        "asynchronous changes in the relay-wall diffusion pattern and combines them with a "
        "physics-embedded reconstruction network~\\cite{wangEventEnhancedPassiveNLOS2024}. "
        "Simulation-based pretraining captures dynamic light transport and sensor characteristics, "
        "while limited measured data are used for fine-tuning. This work extends ordinary-frame "
        "passive NLOS toward neuromorphic acquisition: the event stream emphasizes weak "
        "motion-induced changes that would otherwise be temporally aliased or attenuated in "
        "conventional video.\n\n"
    )
    if text.count(next_heading) != 1:
        raise RuntimeError(f"Passive prose anchor count: {text.count(next_heading)}")
    text = text.replace(next_heading, prose + next_heading, 1)

path.write_text(text, encoding="utf-8")
print("Passive event-camera survey integration completed.")
