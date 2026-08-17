#!/usr/bin/env python3
"""Diagnostic wrapper for the guarded scan-free integration."""
from __future__ import annotations

import traceback
import integrate_scanfree_resolution_20260817 as sync

try:
    sync.main()
except Exception as exc:
    msg = f"{type(exc).__name__}: {exc}".replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
    print(f"::error file=scripts/integrate_scanfree_resolution_20260817.py::{msg}")
    traceback.print_exc()
    raise
