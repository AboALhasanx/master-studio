#!/usr/bin/env python3
"""
_bench_agent_android.py — Benchmark competing Android *agent observation* and
*action* primitives on a real USB-attached device.

Research question (System 1 vs System 2 framing)
------------------------------------------------
What should an LLM agent be handed at each step of the loop, and which action
primitive should it use?

  OBSERVATION
    A  raw UIAutomator XML dump   adb exec-out uiautomator dump /dev/tty
    B  compact action table       hs ui
    C  focused-window state       adb shell dumpsys window
    D  full-res PNG screenshot    adb exec-out screencap -p
    E  768px JPEG screenshot      hs see --size 768
  ACTION
    1  adb shell input tap X Y    fresh adb process per call
    2  hs tap X Y                 warm daemon socket, coordinates
    3  hs tap "Label"             warm daemon socket, text lookup + tap

Mutual exclusion (measured, not assumed)
----------------------------------------
`uiautomator dump` and the `hs` daemon both require the device's single
UiAutomation session. With the daemon up, `uiautomator dump` is SIGKILLed
(rc 137). The benchmark therefore runs in two explicit phases:

  phase 1  daemon DOWN  -> A, C, D, action 1
  phase 2  daemon UP    -> B, C, D, action 2, action 3

Action tests run on the launcher only: tapping there opens an app, which HOME
escapes deterministically. Tapping inside Settings could mutate a preference.

Usage:
    python 90_Shared_Toolbox/tools/_bench_agent_android.py [--runs 7]
"""

import argparse
import io
import json
import math
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ADB = "adb"
HS = str(
    Path(__file__).resolve().parents[1]
    / "bin" / "handsets" / "handsets" / "hs.exe"
)

SCREENS = [
    ("launcher", ["adb", "shell", "input", "keyevent", "KEYCODE_HOME"]),
    ("settings", ["adb", "shell", "am", "start", "-n",
                  "com.android.settings/.Settings"]),
]

# Blank spot on the 800x1340 launcher (below the icon grid, above the dock).
SAFE_XY = (400, 900)


# --------------------------------------------------------------------------- #
# primitives
# --------------------------------------------------------------------------- #
def _run(cmd, timeout=60):
    """Run a command -> (elapsed_ms, stdout_bytes)."""
    t0 = time.perf_counter()
    p = subprocess.run(cmd, capture_output=True, timeout=timeout)
    return (time.perf_counter() - t0) * 1000.0, p.stdout


def _txt(b):
    return b.decode("utf-8", errors="replace")


def daemon_up() -> bool:
    _, out = _run([HS], timeout=20)
    for line in _txt(out).splitlines():
        if "running" in line and line.split()[:1] == ["serial"]:
            continue
        parts = line.split()
        if len(parts) >= 4 and parts[0].startswith("AJ"):
            return parts[3] == "yes"
    return False


def set_daemon(up: bool):
    if up:
        _run([HS, "ui"], timeout=30)
    else:
        _run([HS, "drop"], timeout=30)
        time.sleep(1.5)


def focus():
    _, out = _run(["adb", "shell", "dumpsys", "window"], timeout=30)
    for line in _txt(out).splitlines():
        if "mCurrentFocus" in line and "Window{" in line:
            return line.split("Window{", 1)[1].split("}", 1)[0]
    return ""


def settle(setup_cmd, expect=""):
    """Return the screen to a known state; verify it landed there."""
    for _ in range(3):
        subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_BACK"],
                       capture_output=True, timeout=30)
        time.sleep(0.4)
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_HOME"],
                   capture_output=True, timeout=30)
    time.sleep(0.6)
    subprocess.run(setup_cmd, capture_output=True, timeout=60)
    time.sleep(1.5)
    if expect:
        got = focus()
        if expect not in got:
            # dialogs / recents may still be on top; one more clean attempt
            subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_HOME"],
                           capture_output=True, timeout=30)
            time.sleep(0.6)
            subprocess.run(setup_cmd, capture_output=True, timeout=60)
            time.sleep(1.5)
            got = focus()
        return got
    return focus()


def show_dialogs():
    _, out = _run(["adb", "shell", "dumpsys", "window"], timeout=30)
    txt = _txt(out)
    i = txt.find("Window #")
    return txt[i:i + 700] if i != -1 else ""


# --------------------------------------------------------------------------- #
# token accounting
# --------------------------------------------------------------------------- #
_enc = None


def text_tokens(s: str) -> int:
    global _enc
    if _enc is None:
        try:
            import tiktoken
            _enc = tiktoken.get_encoding("cl100k_base")
        except Exception:
            return math.ceil(len(s) / 4)
    return len(_enc.encode(s))


def image_tokens_wh(w, h) -> int:
    """OpenAI-style image pricing: 512px tiles @170 tok + 85 base."""
    return 85 + 170 * math.ceil(w / 512) * math.ceil(h / 512)


def image_tokens(png_bytes: bytes) -> int:
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(png_bytes))
        return image_tokens_wh(*im.size)
    except Exception:
        return 0


def pct(vals, p):
    if not vals:
        return 0.0
    s = sorted(vals)
    k = min(len(s) - 1, max(0, int(round((p / 100.0) * (len(s) - 1)))))
    return s[k]


# --------------------------------------------------------------------------- #
# observation methods
# --------------------------------------------------------------------------- #
def obs_raw_xml():
    """Raw UIAutomator XML. Requires the daemon DOWN (mutually exclusive)."""
    t0 = time.perf_counter()
    p = subprocess.run(["adb", "exec-out", "uiautomator", "dump", "/dev/tty"],
                       capture_output=True, timeout=60)
    raw = _txt(p.stdout) + _txt(p.stderr)
    if p.returncode != 0 or "</hierarchy>" not in raw:
        subprocess.run(["adb", "shell", "uiautomator", "dump",
                        "/sdcard/_bench_ui.xml"], capture_output=True, timeout=60)
        p2 = subprocess.run(["adb", "exec-out", "cat", "/sdcard/_bench_ui.xml"],
                            capture_output=True, timeout=60)
        raw = _txt(p2.stdout)
        subprocess.run(["adb", "shell", "rm", "-f", "/sdcard/_bench_ui.xml"],
                       capture_output=True, timeout=30)
    ms = (time.perf_counter() - t0) * 1000.0
    end = raw.rfind("</hierarchy>")
    xml = raw[: end + len("</hierarchy>")] if end != -1 else raw
    if "</hierarchy>" not in xml:
        raise RuntimeError(f"raw dump failed rc={p.returncode} "
                           f"head={raw[:60]!r}")
    return ms, len(xml.encode()), text_tokens(xml), xml


def obs_hs_ui():
    ms, out = _run([HS, "ui"], timeout=30)
    s = _txt(out)
    if not s.strip():
        raise RuntimeError("hs ui returned empty")
    return ms, len(s.encode()), text_tokens(s), s


def obs_dumpsys():
    ms, out = _run(["adb", "shell", "dumpsys", "window"], timeout=30)
    full = _txt(out)
    keep = "\n".join(l for l in full.splitlines()
                     if "mCurrentFocus" in l or "mFocusedApp" in l)
    return ms, len(keep.encode()), text_tokens(keep), keep


def obs_screencap_png():
    ms, out = _run(["adb", "exec-out", "screencap", "-p"], timeout=60)
    if len(out) < 1000:
        raise RuntimeError(f"screencap too small: {len(out)} bytes")
    return ms, len(out), image_tokens(out), ""


def obs_hs_see():
    fd, path = tempfile.mkstemp(suffix=".jpg")
    os.close(fd)
    Path(path).unlink(missing_ok=True)
    ms, _ = _run([HS, "see", path, "--size", "768"], timeout=60)
    p = Path(path)
    if not p.exists():
        raise RuntimeError("hs see produced no file")
    b = p.read_bytes()
    p.unlink(missing_ok=True)
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(b))
        tok = image_tokens_wh(*im.size)
    except Exception:
        tok = 0
    return ms, len(b), tok, ""


# --------------------------------------------------------------------------- #
# action methods (launcher only)
# --------------------------------------------------------------------------- #
def tap_adb_xy(x, y, runs, expect):
    lat = []
    for _ in range(runs):
        ms, _ = _run(["adb", "shell", "input", "tap", str(x), str(y)])
        lat.append(ms)
        if focus().split("/", 1)[0] not in (expect, ""):
            settle_home()
    settle_home()
    return lat


def tap_hs_xy(x, y, runs, expect):
    lat = []
    for _ in range(runs):
        ms, _ = _run([HS, "tap", str(x), str(y)], timeout=30)
        lat.append(ms)
        if focus().split("/", 1)[0] not in (expect, ""):
            settle_home()
    settle_home()
    return lat


def tap_hs_text(label, runs, expect):
    """Text lookup + tap. Restored before EVERY timed call so the node exists
    (otherwise `hs tap` burns its NOT_FOUND timeout and poisons p95)."""
    lat = []
    for _ in range(runs):
        settle_home()
        ms, _ = _run([HS, "tap", label, "--timeout", "4000"], timeout=30)
        lat.append(ms)
        if focus().split("/", 1)[0] not in (expect, ""):
            settle_home()
    settle_home()
    return lat


def settle_home():
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_HOME"],
                   capture_output=True, timeout=30)
    time.sleep(0.7)


def pick_label():
    """First quoted label on the launcher, so the text-tap test is real."""
    _, out = _run([HS, "ui"], timeout=30)
    for line in _txt(out).splitlines():
        if line.startswith("tap") and '"' in line:
            a = line.find('"')
            b = line.find('"', a + 1)
            if b > a:
                return line[a + 1 : b]
    return ""


# --------------------------------------------------------------------------- #
def measure_obs(methods, runs):
    """Return {name: stats} averaged over `runs` samples on the current screen."""
    out = {}
    for name, fn in methods:
        lat, sizes, toks, sample = [], [], [], ""
        err = None
        for _ in range(runs):
            try:
                ms, sz, tok, s = fn()
            except Exception as e:
                err = str(e)
                continue
            lat.append(ms)
            sizes.append(sz)
            toks.append(tok)
            if s and not sample:
                sample = s
        if not lat:
            out[name] = {"error": err or "no samples"}
            continue
        out[name] = {
            "p50_ms": round(pct(lat, 50), 1),
            "p95_ms": round(pct(lat, 95), 1),
            "min_ms": round(min(lat), 1),
            "bytes_p50": int(pct(sizes, 50)),
            "tokens_p50": int(pct(toks, 50)),
            "n": len(lat),
            "error": err,
            "sample": sample[:600],
        }
    return out


PHASE1_OBS = [
    ("A_raw_xml_dump", obs_raw_xml),
    ("C_dumpsys_focus", obs_dumpsys),
    ("D_screencap_png", obs_screencap_png),
]
PHASE2_OBS = [
    ("B_hs_ui_action_table", obs_hs_ui),
    ("C_dumpsys_focus", obs_dumpsys),
    ("D_screencap_png", obs_screencap_png),
    ("E_hs_screenshot_768jpg", obs_hs_see),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=7)
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args()

    model = _txt(_run(["adb", "shell", "getprop", "ro.product.model"])[1]).strip()
    res = {"meta": {
        "device": model,
        "serial": _txt(_run(["adb", "get-serialno"])[1]).strip(),
        "screen": _txt(_run(["adb", "shell", "wm", "size"])[1]).strip(),
        "runs": args.runs,
        "hs_exists": Path(HS).exists(),
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
    }}
    print(json.dumps(res["meta"], indent=2))

    # ---------------- phase 1: daemon DOWN (raw XML is available) ----------
    print("\n### PHASE 1 — hs daemon DOWN (raw UIAutomator available)")
    set_daemon(False)
    res["phase1"] = {"daemon": daemon_up()}
    for label, cmd in SCREENS:
        subprocess.run(cmd, capture_output=True, timeout=60)
        time.sleep(1.5)
        print(f"\n  [{label}]")
        got = measure_obs(PHASE1_OBS, args.runs)
        res["phase1"][label] = got
        for k, v in got.items():
            if "error" in v and v["error"]:
                print(f"    {k:26s} ERROR {v['error']}")
            else:
                print(f"    {k:26s} p50={v['p50_ms']:8.1f}ms  "
                      f"p95={v['p95_ms']:8.1f}ms  "
                      f"bytes={v['bytes_p50']:>9,d}  tok={v['tokens_p50']:>6,d}")

    # action 1 needs daemon down; launcher only
    print("\n  [action — launcher]")
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_HOME"],
                   capture_output=True, timeout=30)
    time.sleep(1.2)
    expect = "com.android.launcher3"
    x, y = SAFE_XY
    res["phase1"]["action"] = {}
    try:
        lat = tap_adb_xy(x, y, args.runs, expect)
        res["phase1"]["action"]["1_adb_input_tap"] = {
            "p50_ms": round(pct(lat, 50), 1), "p95_ms": round(pct(lat, 95), 1),
            "n": len(lat)}
        print(f"    {'1_adb_input_tap':26s} p50={pct(lat,50):8.1f}ms  "
              f"p95={pct(lat,95):8.1f}ms")
    except Exception as e:
        print(f"    ! 1_adb_input_tap: {e}")

    # ---------------- phase 2: daemon UP ------------------------------------
    print("\n### PHASE 2 — hs daemon UP (hs verbs available)")
    set_daemon(True)
    res["phase2"] = {"daemon": daemon_up()}
    for label, cmd in SCREENS:
        subprocess.run(cmd, capture_output=True, timeout=60)
        time.sleep(1.5)
        print(f"\n  [{label}]")
        got = measure_obs(PHASE2_OBS, args.runs)
        res["phase2"][label] = got
        for k, v in got.items():
            if "error" in v and v["error"]:
                print(f"    {k:26s} ERROR {v['error']}")
            else:
                print(f"    {k:26s} p50={v['p50_ms']:8.1f}ms  "
                      f"p95={v['p95_ms']:8.1f}ms  "
                      f"bytes={v['bytes_p50']:>9,d}  tok={v['tokens_p50']:>6,d}")

    print("\n  [action — launcher]")
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_HOME"],
                   capture_output=True, timeout=30)
    time.sleep(1.2)
    res["phase2"]["action"] = {}
    for name, fn in [
        ("2_hs_tap_xy", lambda: tap_hs_xy(x, y, args.runs, expect)),
        ("3_hs_tap_by_text", lambda: tap_hs_text(pick_label(), args.runs, expect)),
    ]:
        try:
            lat = fn()
            res["phase2"]["action"][name] = {
                "p50_ms": round(pct(lat, 50), 1),
                "p95_ms": round(pct(lat, 95), 1), "n": len(lat)}
            print(f"    {name:26s} p50={pct(lat,50):8.1f}ms  "
                  f"p95={pct(lat,95):8.1f}ms")
        except Exception as e:
            print(f"    ! {name}: {e}")

    out = Path(args.out) if args.out else (
        Path(__file__).resolve().parents[2] / "00_STUDIO_HUB"
        / "_bench_agent_android.json")
    out.write_text(json.dumps(res, indent=2, ensure_ascii=False),
                   encoding="utf-8")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
