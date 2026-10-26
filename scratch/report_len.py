#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Report option lengths for a builder module WITHOUT writing the bank."""
import importlib.util
import sys

sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
import ch02_lib

ch02_lib.build = lambda *a, **k: None
sys.modules["ch02_lib"] = ch02_lib

mod = sys.argv[1]
spec = importlib.util.spec_from_file_location("m", mod)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

print("%-30s %-24s %-24s %s" % ("concept", "EN", "AR", "flags"))
for cid, bloom, qe, qa, oe, oa, ee, ea in m.I:
    Le = [len(x) for x in oe]
    La = [len(x) for x in oa]
    flags = []
    if Le[0] == max(Le) and Le.count(max(Le)) == 1:
        flags.append("EN-LONG")
    if La[0] == max(La) and La.count(max(La)) == 1:
        flags.append("AR-LONG")
    if max(Le) / min(Le) > 1.40:
        flags.append("EN-SPREAD")
    if max(La) / min(La) > 1.40:
        flags.append("AR-SPREAD")
    if not (0.88 <= Le[0] / (sum(Le[1:]) / 3.0) <= 1.12):
        flags.append("EN-BAND")
    if not (0.88 <= La[0] / (sum(La[1:]) / 3.0) <= 1.12):
        flags.append("AR-BAND")
    print("%-30s %-24s %-24s %s" % (cid[:30], str(Le), str(La), " ".join(flags)))
