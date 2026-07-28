#!/usr/bin/env python3
from pathlib import Path
import re

script = Path(__file__).with_name("integrate_vector_optics_nlos_20260729.py")
source = script.read_text(encoding="utf-8")
old = '    r"^2025 ──[^\\n]*\\n",\n'
new = '    r"^2025 ── Roueinfar & Salmanian: low-cost 808 nm steady-state NIR raster scanning \\[IEEE ICEE\\]\\n",\n'
if source.count(old) != 1:
    raise RuntimeError(f"Expected one broad 2025 timeline anchor, found {source.count(old)}")
source = source.replace(old, new, 1)
namespace = {"__file__": str(script), "__name__": "__main__"}
exec(compile(source, str(script), "exec"), namespace)

index = script.parents[1] / "index.html"
html = index.read_text(encoding="utf-8")
actual = html.count("{cat:")
pattern = r"<b>\d+</b><span>tracked latest entries</span>"
if len(re.findall(pattern, html)) != 1:
    raise RuntimeError("Could not uniquely identify website tracked-entry counter")
html = re.sub(pattern, f"<b>{actual}</b><span>tracked latest entries</span>", html, count=1)
index.write_text(html, encoding="utf-8")
print(f"Website explorer synchronized at {actual} entries")
