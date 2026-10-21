"""Equation audit: numbering, internal references, and numeric recomputation."""
import math
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent
MD = (BASE / "ch7_part1.md").read_text(encoding="utf-8")
lines = MD.split("\n")
fails = []


def check(cond, label, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + label + ("" if cond else f"   {detail}"))
    if not cond:
        fails.append(label)


print("=== 1. equation inventory ===")
eqs = []
for line in lines:
    s = line.strip()
    m = re.search(r"\(7\.(\d+)\)\s*$", s)
    if m and "=" in s and s.startswith("*"):
        eqs.append((int(m.group(1)), s))
print(f"  found {len(eqs)} numbered equations")
nums = [n for n, _ in eqs]
check(nums == list(range(1, len(nums) + 1)), "numbering 7.1..7.%d sequential" % len(nums), nums)

body = re.sub(r"^\*.*\(7\.\d+\)\s*$", "", MD, flags=re.M)
for n, s in eqs:
    refs = len(re.findall(rf"\((7\.{n})\)", body))
    print(f"  7.{n:<3} referenced {refs}x in text")

print("\n=== 2. formula integrity (each equation vs. the model it states) ===")
formula_tests = [
    (1, "λ₀ (1 − μ/V₀)", lambda L0, V0, mu: L0 * (1 - mu / V0)),
    (3, "V₀[1 − exp(−λ₀τ/V₀)]", lambda L0, V0, tau: V0 * (1 - math.exp(-L0 * tau / V0))),
    (4, "λ₀ exp(−λ₀τ/V₀)", lambda L0, V0, tau: L0 * math.exp(-L0 * tau / V0)),
    (8, "λ₀/(λ₀θτ+1)", lambda L0, th, tau: L0 / (L0 * th * tau + 1)),
    (9, "(1/θ)ln(λ₀θτ+1)", lambda L0, th, tau: (1 / th) * math.log(L0 * th * tau + 1)),
]
L0, V0, th = 20.0, 200.0, 0.025
for n, label, f in formula_tests:
    if n in (1,):
        v = f(L0, V0, 100)          # μ=100 -> λ=10
        check(abs(v - 10) < 1e-9, f"7.{n}: λ(μ=100)=10", v)
    elif n in (3, 4):
        v3 = 200 * (1 - math.exp(-2))
        v4 = 20 * math.exp(-2)
        check(abs(v3 - 172.9) < 0.05 and abs(v4 - 2.707) < 0.01,
              f"7.{n}: μ(20)=172.9, λ(20)=2.71", (round(v3, 3), round(v4, 3)))
    else:
        target = 1.0 if n == 8 else 119.83
        check(abs(f(20, th, 38) - target) < 0.02, f"7.{n}: value at tau=38", round(f(20, th, 38), 2))

# identities linking the pairs of equations
check(abs((V0 / L0) * math.log(10 / 5) - 6.931) < 0.01, "7.6: Δτ = 6.93 CPU hr")
check(abs((V0 / L0) * (10 - 5) - 50) < 1e-9, "7.5: Δμ = 50 failures")
check(abs((1 / th) * math.log(20 / 1) - 119.83) < 0.01, "7.10: Δμ = 119.8 (book prints 119)")
check(abs((1 / th) * (1 / 1 - 1 / 20) - 38) < 0.01, "7.11: Δτ = 38 CPU hr")
check(abs((1 / th) * math.log(20 / 0.5) - 147.6) < 0.2, "7.10(b): Δμ = 147.6 (book prints 148)")
check(abs((1 / th) * (1 / 0.5 - 1 / 20) - 78) < 0.01, "7.11(b): Δτ = 78 CPU hr")

# derivative consistency: dμ/dτ must equal λ(τ)
h = 1e-6
tau = 10.0
dmu = (V0 * (1 - math.exp(-L0 * (tau + h) / V0)) - V0 * (1 - math.exp(-L0 * tau / V0))) / h
check(abs(dmu - L0 * math.exp(-L0 * tau / V0)) < 1e-4, "7.3 differentiated == 7.4")

print("\n=== 3. worked examples ===")
check(abs(200 * (1 - math.exp(-2)) - 173) < 1, "Ex 7.1: μ(20)=173")
check(abs(20 * math.exp(-2) - 2.71) < 0.01, "Ex 7.1: λ(20)=2.71")
check(abs(20 * math.exp(-10) - 0.000908) < 1e-6, "Ex 7.1: λ(100)=0.000908")
check(abs(20 * (1 - 100 / 200) - 10) < 1e-9, "Ex 7.1: current λ=10")
check(abs(-20 / 200 + 0.1) < 1e-9, "Ex 7.1: dλ/dμ = −0.1")
check(abs((500 / 2) * (2 - 0.05) - 487) < 1, "Ex 7.6: Δμ = 487 (13 faults remain)")
check(abs(0.03 * (100 - 60 + 1) - 1.23) < 1e-9, "Ex 7.7: λ=1.23")
check(abs(0.03 * (100 - 80 + 1) - 0.63) < 1e-9, "Ex 7.7: λ=0.63")
check(abs(5 * 10 + 2 * 25 - 100) < 1e-9, "Ex 7.4: XI = 100 person hr")
check(abs(500 / 505 * 100 - 99.01) < 0.01, "Availability = 99.01%")
check(abs(119 + 2 * 38 - 195) < 1e-9, "Ex 7.5(a): XI = 195")
check(abs(5 * 119 - 595) < 1e-9, "Ex 7.5(a): XF = 595")
check(abs(119 + 1.5 * 38 - 176) < 1e-9, "Ex 7.5(a): XC = 176")
check(abs(148 + 2 * 78 - 304) < 1e-9, "Ex 7.5(b): XI = 304")
check(abs(5 * 148 - 740) < 1e-9, "Ex 7.5(b): XF = 740")
check(abs(148 + 1.5 * 78 - 265) < 1e-9, "Ex 7.5(b): XC = 265")

print("\n=== 3b. Example 7.2 and 7.3 (log Poisson) ===")
th2 = 0.02
l0 = 20.0
check(abs(l0 * math.exp(-th2 * 100) - 2.7) < 0.01, "Ex 7.2(i): λ = 2.7")
check(abs(-th2 * l0 * math.exp(-th2 * 100) + 0.054) < 0.001, "Ex 7.2(ii): dλ/dμ = −0.054")
mu20 = (1 / th2) * math.log(l0 * th2 * 20 + 1)
check(round(mu20) == 110 or round(mu20) == 109, f"Ex 7.2(iii): μ(20) ≈ 109 (got {mu20:.2f})")
check(abs(l0 / (l0 * th2 * 20 + 1) - 2.22) < 0.01, "Ex 7.2(iii): λ(20) = 2.22")
mu100 = (1 / th2) * math.log(l0 * th2 * 100 + 1)
check(round(mu100) == 186, f"Ex 7.2(iii): μ(100) = 186 (got {mu100:.2f})")
check(abs(l0 / (l0 * th2 * 100 + 1) - 0.4878) < 0.001, "Ex 7.2(iii): λ(100) = 0.4878")
dmu72 = (1 / th2) * math.log(2.7 / 2)
dtau72 = (1 / th2) * (1 / 2 - 1 / 2.7)
check(abs(dmu72 - 15.1) < 0.2 and abs(dtau72 - 6.5) < 0.1, "Ex 7.2(iv): 15 failures, 6.5 CPU hr",
      (round(dmu72, 2), round(dtau72, 2)))

th3 = 0.025
check(abs((1 / th3) * math.log(30 / 5) - 71.67) < 0.05, "Ex 7.3(a): log Δμ = 71.67")
check(abs((1 / th3) * (1 / 5 - 1 / 30) - 6.66) < 0.02, "Ex 7.3(a): log Δτ = 6.66")
check(abs((1 / th3) * math.log(30 / 0.5) - 163.8) < 0.2, "Ex 7.3(b): log Δμ = 163.8")
check(abs((1 / th3) * (1 / 0.5 - 1 / 30) - 78.66) < 0.05, "Ex 7.3(b): log Δτ = 78.66")
check(abs((100 / 10) * (10 - 0.5) - 95) < 1e-9, "Ex 7.3(b): basic Δμ = 95")
check(abs((100 / 10) * math.log(10 / 0.5) - 29.96) < 0.05, "Ex 7.3(b): basic Δτ = 30")

print("\n=== 4. Table 7.3 means ===")
blk = MD.split("Table 7.3")[1].split("Mean failures")[0]
rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|$", blk, re.M)
if rows:
    m1 = sum(int(a) * float(b) for a, b, c in rows)
    m2 = sum(int(a) * float(c) for a, b, c in rows)
    check(abs(m1 - 3.04) < 0.02, f"t=1 hr mean = 3.04 (got {m1:.2f})")
    check(abs(m2 - 7.77) < 0.02, f"t=5 hr mean = 7.77 (got {m2:.2f})")

print("\n================ SUMMARY ================")
print(f"FAILURES: {len(fails)}")
for f in fails:
    print("  -", f)
sys.exit(1 if fails else 0)
