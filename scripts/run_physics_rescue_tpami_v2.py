#!/usr/bin/env python3
from __future__ import annotations

import run_physics_rescue_tpami as base


def patch_active_fixed() -> None:
    text = base.ACTIVE.read_text(encoding="utf-8")
    if base.KEY not in text:
        anchor = "miaoAdaptiveWindowingNLOS2025,yinAllDayNLOS2026"
        if text.count(anchor) != 1:
            base.die("active SPAD-table sequence anchor is not unique")
        text = text.replace(anchor, base.KEY + "," + anchor, 1)
    base.ACTIVE.write_text(text, encoding="utf-8")


base.patch_active = patch_active_fixed
base.main()
