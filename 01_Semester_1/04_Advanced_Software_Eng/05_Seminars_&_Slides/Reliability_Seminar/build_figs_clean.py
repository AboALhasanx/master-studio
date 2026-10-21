#!/usr/bin/env python3
"""Clean, code-drawn figures for Chapter 7 (no scanned images)."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge, FancyBboxPatch, Polygon

from pathlib import Path
FIG = Path(__file__).resolve().parent / "figures"
FIG.mkdir(exist_ok=True)

INK = "#000000"
GREY = "#4A4A4A"
NAVY = "#000000"
BLUE = "#E8E8E8"
GREEN = "#DCDCDC"
AMBER = "#F0F0F0"
RED = "#CFCFCF"


def _fig(w=6.2, h=3.6):
    fig, ax = plt.subplots(figsize=(w, h), dpi=300)
    ax.set_facecolor("white")
    return fig, ax


def _box(ax, x, y, w, h, text, fc="white", fs=8, bold=False, ec=INK):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.01,rounding_size=0.05",
                                linewidth=1.0, edgecolor=ec, facecolor=fc))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", color=INK)


# ------------------------------------------------------------------ 7.1
def bathtub():
    fig, ax = _fig(6.2, 3.4)
    x = np.linspace(0, 9.6, 800)
    y = 5.0 * np.exp(-1.3 * x) + 0.7 + 0.05 * np.exp(1.9 * np.maximum(0, x - 7.0))
    ax.plot(x, y, color=INK, lw=2)
    ax.axvspan(0, 3, color=RED, alpha=0.45, zorder=0)
    ax.axvspan(3, 7, color=GREEN, alpha=0.45, zorder=0)
    ax.axvspan(7, 9.6, color=AMBER, alpha=0.45, zorder=0)
    ax.text(1.5, 0.25, "Burn-in", ha="center", fontsize=9)
    ax.text(5.0, 0.25, "Useful life", ha="center", fontsize=9)
    ax.text(8.3, 0.25, "Wear-out", ha="center", fontsize=9)
    ax.set_xlabel("Time"); ax.set_ylabel("Failure rate")
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0, 9.6); ax.set_ylim(0, 8.2)
    for s in ax.spines.values(): s.set_color(INK)
    fig.tight_layout(); out = FIG / "fig7_1_bathtub.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def sw_curve():
    fig, ax = _fig(6.2, 3.2)
    x = np.linspace(0, 10, 600)
    y = 0.18 + 3.4 * np.exp(-0.55 * x)
    ax.plot(x, y, color=INK, lw=2)
    ax.axvline(3.0, color=GREY, lw=0.9, ls="--")
    ax.axvline(7.6, color=GREY, lw=0.9, ls="--")
    ax.text(1.5, 3.85, "Testing phase", ha="center", fontsize=8)
    ax.text(5.3, 3.85, "Useful life", ha="center", fontsize=8)
    ax.text(8.8, 3.85, "Obsolescence", ha="center", fontsize=8)
    ax.annotate("", xy=(9.7, 0.05), xytext=(0.2, 0.05),
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.annotate("", xy=(0.2, 3.95), xytext=(0.2, 0.02),
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.text(5.0, -0.18, "Time", fontsize=8.5, ha="center")
    ax.text(-0.35, 2.0, "Failure rate", fontsize=8.5, rotation=90, va="center", ha="center")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.05)
    for s in ax.spines.values():
        s.set_visible(False)
    fig.tight_layout(); out = FIG / "fig7_2_sw_reliability.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def mean_fi():
    fig, ax = _fig(6.2, 3.4)
    x = np.linspace(0.2, 9.5, 400)
    mean = 8.4 * (1 - np.exp(-0.28 * x)); fi = 2.4 * np.exp(-0.28 * x)
    ax.plot(x, mean, color=NAVY, lw=2, label="Mean failures")
    ax.plot(x, fi, color=INK, lw=1.8, ls=(0, (4, 2)), label="Failure intensity")
    for t, lab in [(1.2, r"$t_A$"), (5.0, r"$t_B$")]:
        ax.axvline(t, color=GREY, lw=0.8, ls=":"); ax.text(t, 0.3, lab, ha="center", fontsize=9)
    ax.text(7.0, 6.4, "mean failures\nincreases", fontsize=8, color=NAVY)
    ax.text(6.6, 1.0, "failure intensity\ndecreases", fontsize=8, color=INK)
    ax.set_xlabel("Execution time"); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(0, 8.6)
    for s in ax.spines.values(): s.set_color(INK)
    fig.tight_layout(); out = FIG / "fig7_3_mean_fi.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def input_space():
    fig, ax = _fig(4.6, 3.8)
    t = np.linspace(0, 2 * np.pi, 400)
    r = 1 + 0.12 * np.sin(5 * t) + 0.06 * np.cos(9 * t)
    x = 4 + 2.6 * r * np.cos(t); y = 2.8 + 2.1 * r * np.sin(t)
    ax.fill(x, y, facecolor="#EDEDED", edgecolor=INK, lw=1.4)
    ax.plot(3.0, 2.4, "o", color=NAVY, ms=7); ax.plot(5.3, 3.3, "s", color="#6E6E6E", ms=7)
    ax.text(2.9, 1.85, "Input state A\n(P = 0.12)", ha="center", fontsize=8)
    ax.text(5.6, 3.75, "Input state B\n(P = 0.08)", ha="center", fontsize=8)
    ax.set_xlim(0.6, 7.4); ax.set_ylim(0.4, 5.4); ax.axis("off")
    fig.tight_layout(); out = FIG / "fig7_4_input_space.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def profile_part():
    fig, ax = _fig(4.6, 3.2)
    ax.bar(["A", "B"], [0.12, 0.08], color=[BLUE, RED], edgecolor=INK, width=0.5)
    ax.set_ylabel("Probability"); ax.set_ylim(0, 0.2); ax.set_yticks([0, 0.05, 0.1, 0.15, 0.2])
    for s in ax.spines.values(): s.set_color(INK)
    fig.tight_layout(); out = FIG / "fig7_5_profile_part.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def profile():
    fig, ax = _fig(6.0, 3.2)
    x = np.linspace(0.1, 9.9, 500)
    y = 0.03 + 0.34 / (1 + np.exp((x - 3.6) / 0.6))
    ax.plot(x, y, color=INK, lw=2)
    ax.annotate("", xy=(9.8, 0.02), xytext=(0.05, 0.02),
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.annotate("", xy=(0.05, 0.42), xytext=(0.05, 0.01),
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.text(4.9, -0.075, "Input state", fontsize=8.5, ha="center")
    ax.text(-0.55, 0.22, "Probability of occurrence", fontsize=8.5, rotation=90,
            va="center", ha="center")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 10); ax.set_ylim(0, 0.44)
    for s in ax.spines.values():
        s.set_visible(False)
    fig.tight_layout(); out = FIG / "fig7_6_profile.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def rel_fi():
    fig, ax = _fig(6.0, 3.4)
    x = np.linspace(0.2, 9.5, 400)
    fi = 2.2 * np.exp(-0.30 * x) + 0.25
    rel = 0.55 + 0.42 * (1 - np.exp(-0.30 * x))
    ax.plot(x, fi, color=INK, lw=1.8, ls=(0, (4, 2)))
    ax.set_ylabel("Failure intensity", fontsize=9)
    ax.set_xlabel("Time (hr)", fontsize=9)
    ax.set_ylim(0, 2.6); ax.set_xlim(0, 9.6)
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax2 = ax.twinx()
    ax2.plot(x, rel, color=INK, lw=2)
    ax2.set_ylim(0, 1.0); ax2.set_yticks([])
    ax2.set_ylabel("Reliability", fontsize=9)
    ax2.spines["top"].set_visible(False)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([], [], color=INK, lw=1.8, ls=(0, (4, 2)), label="Failure intensity"),
                       Line2D([], [], color=INK, lw=2, label="Reliability")],
              loc="lower left", frameon=False, fontsize=7.6)
    fig.tight_layout(); out = FIG / "fig7_7_rel_fi.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def quality_attributes():
    cols = [
        ("Reliability", ["Correctness", "Consistency and\nprecision", "Robustness", "Simplicity", "Traceability"]),
        ("Usability", ["Accuracy", "Clarity and accuracy\nof documentation", "Conformity of\noperational\nenvironment", "Completeness", "Efficiency"]),
        ("Maintainability", ["Testability", "Maintainability", "Modularity", "Readability"]),
        ("Adaptability", ["Adaptability", "Modifiability", "Expandability", "Portability"]),
    ]
    fig, ax = _fig(7.6, 4.4)
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(1.2, 7.6)
    ax.text(5, 7.25, "Software quality attributes", ha="center", fontsize=11, fontweight="bold")
    ax.text(0.45, 6.55, "Attribute\ndomain", ha="center", fontsize=8.5, fontweight="bold")
    for i, (domain, attrs) in enumerate(cols):
        x = 2.1 + i * 2.15
        _box(ax, x, 6.5, 1.9, 0.55, domain, fc=BLUE, fs=8.5, bold=True)
        ax.plot([x, x], [6.2, 5.9], color=INK, lw=0.9)
        y = 5.5
        for a in attrs:
            h = 0.7 if "\n" in a else 0.45
            _box(ax, x, y, 1.9, h, a, fs=6.8)
            y -= h + 0.35
    fig.tight_layout(); out = FIG / "fig7_8_quality_attributes.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


# ------------------------------------------------------------------ 7.9
def mccall_rings():
    """Concentric rings: 3 product sectors inside, 11 factors on the outer ring."""
    fig, ax = _fig(5.6, 5.6)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-2.55, 2.55); ax.set_ylim(-2.55, 2.55)

    cats = [("Product operation", 270), ("Product revision", 30), ("Product transition", 150)]
    for name, mid in cats:
        ax.add_patch(Wedge((0, 0), 1.55, mid - 60, mid + 60, width=1.55,
                           facecolor="#F2F2F2", edgecolor=INK, lw=1.0))
        am = math.radians(mid)
        ax.text(0.78 * math.cos(am), 0.78 * math.sin(am), name,
                ha="center", va="center", fontsize=7.4, fontweight="bold")

    factors = ["Correctness", "Reliability", "Efficiency", "Integrity", "Usability",
               "Maintainability", "Flexibility", "Testability",
               "Portability", "Reusability", "Interoperability"]
    start = 270 - 60
    step = 120 / 5
    angles = []
    for i in range(5):
        angles.append((start + i * step, start + (i + 1) * step))
    start2 = 30 - 60 + 0
    angles.append((start2 - 120, start2 - 80))
    angles = []
    # operation: 210..330 in five cells
    a0 = 210
    for i in range(5):
        angles.append((a0 + i * 24, a0 + (i + 1) * 24))
    # revision: 330..450(90) in three cells
    a0 = 330
    for i in range(3):
        angles.append((a0 + i * 40, a0 + (i + 1) * 40))
    # transition: 90..210 in three cells
    a0 = 90
    for i in range(3):
        angles.append((a0 + i * 40, a0 + (i + 1) * 40))

    for (s, e), f in zip(angles, factors):
        ax.add_patch(Wedge((0, 0), 2.35, s, e, width=0.8,
                           facecolor="#E6E6E6", edgecolor=INK, lw=0.8))
        mid = (s + e) / 2
        am = math.radians(mid)
        rot = mid + 90
        while rot > 90:
            rot -= 180
        while rot < -90:
            rot += 180
        ax.text(1.95 * math.cos(am), 1.95 * math.sin(am), f, ha="center", va="center",
                fontsize=6.4, rotation=rot, rotation_mode="anchor")

    ax.add_patch(Circle((0, 0), 1.55, fill=False, ec=INK, lw=1.0))
    ax.add_patch(Circle((0, 0), 2.35, fill=False, ec=INK, lw=1.0))
    for a in (90, 210, 330):
        ax.plot([0, 1.55 * math.cos(math.radians(a))],
                [0, 1.55 * math.sin(math.radians(a))], color=INK, lw=1.0)
    fig.tight_layout(); out = FIG / "fig7_9_quality_factors.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def mccall_model():
    """Factor-to-criterion diagram (form of the source figure)."""
    factors = ["Usability", "Integrity", "Efficiency", "Correctness", "Reliability",
               "Maintainability", "Testability", "Flexibility", "Reusability",
               "Portability", "Interoperability"]
    rows = [
        ("Operability", ["Usability"]), ("Training", ["Usability"]),
        ("Communicativeness", ["Usability"]), ("I/O volume", ["Usability"]),
        ("I/O rate", ["Usability"]), ("Access control", ["Integrity"]),
        ("Access audit", ["Integrity"]), ("Storage efficiency", ["Efficiency"]),
        ("Execution efficiency", ["Efficiency"]), ("Traceability", ["Correctness"]),
        ("Completeness", ["Correctness"]), ("Accuracy", ["Reliability"]),
        ("Error tolerance", ["Reliability"]),
        ("Consistency", ["Correctness", "Reliability", "Maintainability"]),
        ("Simplicity", ["Reliability", "Maintainability", "Testability"]),
        ("Conciseness", ["Maintainability"]), ("Instrumentation", ["Testability"]),
        ("Expandability", ["Flexibility"]), ("Generality", ["Flexibility", "Reusability"]),
        ("Self-descriptiveness", ["Maintainability", "Testability", "Flexibility", "Reusability"]),
        ("Modularity", ["Maintainability", "Testability", "Flexibility", "Reusability", "Portability"]),
        ("Machine independence", ["Reusability", "Portability"]),
        ("Software system independence", ["Reusability", "Portability"]),
        ("Communication commonality", ["Portability", "Interoperability"]),
        ("Data commonality", ["Interoperability"]),
    ]
    fig, ax = _fig(7.2, 6.6)
    ax.axis("off"); ax.set_xlim(0, 11.4); ax.set_ylim(0, 11.6)

    fy = {f: 10.7 - i * 0.86 for i, f in enumerate(factors)}
    cy = {c: 11.1 - j * 0.415 for j, (c, _) in enumerate(rows)}

    ax.text(1.55, 11.45, "Factors", ha="center", fontsize=7.8, fontweight="bold")
    ax.text(9.35, 11.45, "Criteria", ha="center", fontsize=7.8, fontweight="bold")

    for f, y in fy.items():
        _box(ax, 1.55, y, 2.3, 0.52, f, fc="#EDEDED", fs=6.6)
    for c, marks in rows:
        _box(ax, 9.35, cy[c], 3.5, 0.32, c, fs=5.9)
        for m in marks:
            ax.plot([2.72, 7.58], [fy[m], cy[c]], color="#8C8C8C", lw=0.45, zorder=0)

    fig.tight_layout(); out = FIG / "fig7_10_mccall_model.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def boehm_model():
    fig, ax = _fig(8.0, 5.2)
    ax.axis("off"); ax.set_xlim(0, 13.2); ax.set_ylim(0, 8.2)
    ax.text(3.9, 7.75, "Primary uses", ha="center", fontsize=8.4, fontweight="bold")
    ax.text(7.0, 7.75, "Intermediate constructs", ha="center", fontsize=8.4, fontweight="bold")
    ax.text(11.2, 7.75, "Primitive constructs", ha="center", fontsize=8.4, fontweight="bold")

    _box(ax, 1.55, 4.0, 1.75, 0.62, "General\nutility", fc=BLUE, fs=7.4, bold=True)
    _box(ax, 3.95, 5.65, 2.0, 0.55, "As is utility", fc=BLUE, fs=7.4, bold=True)
    _box(ax, 3.95, 2.55, 2.0, 0.55, "Maintainability", fc=BLUE, fs=7.4, bold=True)
    for y in (5.65, 2.55):
        ax.annotate("", xy=(2.95, y), xytext=(2.45, 4.0),
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))

    mids = [("Portability", 6.55), ("Reliability", 5.85), ("Efficiency", 5.15),
            ("Human engineering", 4.45), ("Testability", 3.65),
            ("Understandability", 2.95), ("Modifiability", 2.25)]
    for t, y in mids:
        _box(ax, 7.0, y, 2.5, 0.5, t, fs=7.0)
    for y in (6.55, 5.85, 5.15, 4.45):
        ax.annotate("", xy=(5.72, y), xytext=(4.95, 5.65),
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    for y in (3.65, 2.95, 2.25):
        ax.annotate("", xy=(5.72, y), xytext=(4.95, 2.55),
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))

    prims = ["Device independence", "Completeness", "Accuracy", "Consistency",
             "Device efficiency", "Accessibility", "Communicativeness", "Structuredness",
             "Self-descriptiveness", "Conciseness", "Legibility", "Augmentability"]
    for i, t in enumerate(prims):
        _box(ax, 11.2, 6.65 - i * 0.5, 2.85, 0.42, t, fs=6.6)

    ax.plot([9.35, 9.35], [1.15, 6.85], color="#A6A6A6", lw=0.9)
    ax.plot([9.35, 9.55], [1.15, 1.15], color="#A6A6A6", lw=0.9)
    ax.plot([9.35, 9.55], [6.85, 6.85], color="#A6A6A6", lw=0.9)
    ax.annotate("", xy=(9.62, 4.0), xytext=(9.35, 4.0),
                arrowprops=dict(arrowstyle="->", color="#666666", lw=0.9))
    ax.text(6.9, 0.55, "Each intermediate construct is measured by one or more primitive constructs.",
            ha="center", fontsize=6.4, color="#4A4A4A")
    fig.tight_layout(); out = FIG / "fig7_11_boehm_model.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


# ------------------------------------------------------------------ 7.12
def iso9126():
    fig, ax = _fig(5.8, 5.8)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-2.78, 2.78); ax.set_ylim(-2.78, 2.78)
    chars = [
        ("Functionality", "Suitability\nAccuracy\nInteroperability\nSecurity"),
        ("Reliability", "Maturity\nFault tolerance\nRecoverability"),
        ("Usability", "Understandability\nLearnability\nOperability"),
        ("Efficiency", "Time behaviour\nResource behaviour"),
        ("Maintainability", "Analyzability\nChangeability\nStability\nTestability"),
        ("Portability", "Adaptability\nInstallability\nConformance\nReplaceability"),
    ]
    n = len(chars); step = 360 / n
    fills = ["#F7F7F7", "#EFEFEF", "#E7E7E7", "#DFDFDF", "#D7D7D7", "#CFCFCF"]
    for i, (name, subs) in enumerate(chars):
        a0 = 90 - (i + 1) * step; a1 = 90 - i * step
        ax.add_patch(Wedge((0, 0), 2.65, a0, a1, width=2.65, facecolor=fills[i], edgecolor=INK, lw=1.0))
        am = math.radians((a0 + a1) / 2)
        ax.text(1.30 * math.cos(am), 1.30 * math.sin(am), name, ha="center", va="center",
                fontsize=7.2, fontweight="bold")
        ax.text(2.22 * math.cos(am), 2.18 * math.sin(am), subs, ha="center", va="center",
                fontsize=5.3, linespacing=1.45)
    ax.add_patch(Circle((0, 0), 0.72, facecolor="white", edgecolor=INK, lw=1.0))
    ax.text(0, 0, "ISO 9126\nquality\nmodel", ha="center", va="center",
            fontsize=6.4, fontweight="bold")
    fig.tight_layout(); out = FIG / "fig7_12_iso9126.png"; fig.savefig(out, facecolor="white"); plt.close(fig)



def fig_7_23():
    fig, ax = _fig(5.8, 3.2)
    ax.axis("off"); ax.set_xlim(0, 11.0); ax.set_ylim(0, 7.0)
    levels = [("Initial", 1), ("Repeatable", 2), ("Defined", 3), ("Managed", 4), ("Optimizing", 5)]
    for i, (name, n) in enumerate(levels):
        x = 1.9 + i * 1.75
        y = 0.7 + i * 1.15
        ax.add_patch(Rectangle((x, 0.0), 1.45, y, facecolor="#E8E8E8",
                               edgecolor=INK, lw=1.0, zorder=2))
        ax.text(x + 0.725, y - 0.42, str(n), ha="center", va="center",
                fontsize=13, fontweight="bold", zorder=3)
        ax.text(1.65, y - 0.18, name, ha="right", va="center", fontsize=7.6)
        if i < 4:
            ax.annotate("", xy=(x + 1.72, y - 0.1), xytext=(x + 1.48, y - 0.1),
                        arrowprops=dict(arrowstyle="->", color=GREY, lw=0.9))
    fig.tight_layout(); out = FIG / "fig7_23_cmm_levels.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def _axes(xl, yl, xlab, ylab, w=5.4, h=3.2):
    fig, ax = _fig(w, h)
    ax.set_xlim(0, xl); ax.set_ylim(0, yl)
    ax.set_xlabel(xlab, fontsize=9); ax.set_ylabel(ylab, fontsize=9)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(INK)
    return fig, ax


def fig_7_13():
    fig, ax = _axes(V0 * 1.04, L0 * 1.18, "Failures experienced (μ)", "Failure intensity λ(μ)")
    ax.plot([0, V0], [L0, 0], color=INK, lw=2)
    ax.plot([0, V0], [0, 0], color=GREY, lw=0.8, ls=":")
    ax.plot([0, 0], [0, L0], color=GREY, lw=0.8, ls=":")
    ax.text(V0 - 6, 0.55, "V$_0$", fontsize=8)
    ax.text(2, L0 + 0.35, "λ$_0$", fontsize=8)
    ax.text(46, 8.2, r"slope = $-\lambda_0/V_0$", fontsize=8.2, color=GREY)
    fig.tight_layout(); out = FIG / "fig7_13_lambda_mu.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_14():
    import numpy as np
    fig, ax = _axes(60, V0 * 1.12, "Execution time τ", "Mean failures μ(τ)")
    x = np.linspace(0, 60, 400)
    ax.plot(x, V0 * (1 - np.exp(-L0 * x / V0)), color=INK, lw=2)
    ax.axhline(V0, color=GREY, lw=0.8, ls=":")
    ax.text(2, V0 + 4, "V$_0$", fontsize=8)
    fig.tight_layout(); out = FIG / "fig7_14_mu_tau.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_15():
    import numpy as np
    fig, ax = _axes(60, L0 * 1.12, "Execution time τ", "Failure intensity λ(τ)")
    x = np.linspace(0, 60, 400)
    ax.plot(x, L0 * np.exp(-L0 * x / V0), color=INK, lw=2)
    ax.text(2, L0 + 0.3, "λ$_0$", fontsize=8)
    fig.tight_layout(); out = FIG / "fig7_15_lambda_tau.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_16():
    fig, ax = _axes(L0 * 1.05, V0 * 1.1, "Failure intensity objective λ$_F$", "Additional failures Δμ")
    ax.plot([0, L0], [V0, 0], color=INK, lw=2)
    ax.text(L0 * 0.42, V0 * 0.55, "Δμ = (V$_0$/λ$_0$)(λ$_P$ − λ$_F$)", fontsize=7.2)
    fig.tight_layout(); out = FIG / "fig7_16_dmu.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_17():
    import numpy as np
    fig, ax = _axes(L0 * 1.05, V0 * 2.2, "Failure intensity objective λ$_F$", "Additional time Δτ")
    x = np.linspace(0.02, L0, 400)
    ax.plot(x, (V0 / L0) * np.log(L0 / x), color=INK, lw=2)
    ax.text(1.2, 150, "Δτ = (V$_0$/λ$_0$) ln(λ$_P$/λ$_F$)", fontsize=7.2)
    fig.tight_layout(); out = FIG / "fig7_17_dtau.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_18():
    import numpy as np
    fig, ax = _axes(V0 * 1.04, L0 * 1.15, "Mean failures experienced (μ)", "Failure intensity λ(μ)")
    x = np.linspace(0, V0, 400)
    ax.plot(x, L0 * np.exp(-0.025 * x), color=INK, lw=2)
    ax.text(26, 6.5, "λ(μ) = λ₀ exp(−θμ)", fontsize=7.8)
    fig.tight_layout(); out = FIG / "fig7_18_lambda_mu_log.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_19():
    import numpy as np
    fig, ax = _axes(60, 125, "Execution time τ", "Mean failures μ(τ)")
    x = np.linspace(0, 60, 500)
    basic = 100 * (1 - np.exp(-10 * x / 100))
    logm = (1 / 0.025) * np.log(10 * 0.025 * x + 1)
    ax.plot(x, basic, color=INK, lw=1.8, ls=(0, (5, 2)))
    ax.plot(x, logm, color=INK, lw=2)
    ax.axhline(100, color=GREY, lw=0.8, ls=":")
    ax.text(52.5, 91, "V₀", fontsize=8)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([], [], color=INK, lw=2, label="Logarithmic Poisson model"),
                       Line2D([], [], color=INK, lw=1.8, ls=(0, (5, 2)), label="Basic model")],
              loc="lower right", frameon=False, fontsize=7.0)
    fig.tight_layout(); out = FIG / "fig7_19_mu_log.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def fig_7_20():
    import numpy as np
    fig, ax = _axes(60, 2.2, "Execution time τ", "Instantaneous ratio dτ/dt")
    x = np.linspace(0.2, 60, 400)
    ax.plot(x, 1.9 * np.exp(-x / 12) + 0.55, color=INK, lw=2)
    ax.axhline(0.55, color=GREY, lw=0.9, ls=":")
    ax.text(38, 0.72, "θ$_r$ / (ρ$_r$P$_r$)", fontsize=7.6)
    fig.tight_layout(); out = FIG / "fig7_20_ratio.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_21():
    import numpy as np
    fig, ax = _axes(60, 2.6, "Execution time τ", "Ratio dτ/dt")
    x = np.linspace(0.3, 60, 500)
    c1 = 0.45 + 2.4 * np.exp(-x / 5.0)
    c2 = 0.62 + 1.5 * np.exp(-x / 12.0)
    c3 = 0.80 + 0.9 * np.exp(-x / 30.0)
    ax.plot(x, c1, color=INK, lw=1.8)
    ax.plot(x, c2, color="#5A5A5A", lw=1.8)
    ax.plot(x, c3, color="#9A9A9A", lw=1.8, ls=(0, (5, 2)))
    ax.axvline(18, color=GREY, lw=0.8, ls=":")
    ax.axvline(38, color=GREY, lw=0.8, ls=":")
    ax.text(18.6, 2.30, "FI", fontsize=8)
    ax.text(36.4, 2.30, "FC", fontsize=8)
    ax.text(38.8, 2.30, "IC", fontsize=8)
    ax.text(5.0, 1.85, "1", fontsize=9)
    ax.text(27.0, 1.85, "2", fontsize=9)
    ax.text(50.0, 1.85, "3", fontsize=9)
    ax.text(6.0, 0.35, "correction limited", fontsize=6.4, color=GREY)
    ax.text(22.0, 0.35, "identification limited", fontsize=6.4, color=GREY)
    ax.text(44.0, 0.35, "computer time limited", fontsize=6.4, color=GREY)
    fig.tight_layout(); out = FIG / "fig7_21_calendar.png"; fig.savefig(out, facecolor="white"); plt.close(fig)


def fig_7_22():
    fig, ax = _fig(5.6, 3.4)
    ax.set_xlim(0, 9.6); ax.set_ylim(1.2, 7.9)
    N = 6
    for i in range(N):
        x0 = 0.9 + i * 1.35
        y = N + 1 - i
        ax.plot([x0, x0 + 1.35], [y, y], color=INK, lw=2)
        if i < N - 1:
            ax.plot([x0 + 1.35, x0 + 1.35], [y, y - 1], color=INK, lw=1.1, ls=":")
    ax.set_yticks([N + 1 - i for i in range(N)])
    ax.set_yticklabels(["Nφ"] + [f"(N−{i})φ" for i in range(1, N)], fontsize=7.5)
    ax.set_xticks([0.9 + i * 1.35 + 0.675 for i in range(N)])
    ax.set_xticklabels([f"t$_{i+1}$" for i in range(N)], fontsize=7.5)
    ax.set_xlabel("Time t", fontsize=9); ax.set_ylabel("Failure intensity λ(t)", fontsize=9)
    for s in ax.spines.values():
        s.set_color(INK)
    fig.tight_layout(); out = FIG / "fig7_22_jm.png"; fig.savefig(out, facecolor="white"); plt.close(fig)

def fig_7_24():
    steps = ["Application", "Pre-assessment", "Document review and\nadequacy of audit",
             "Compliance audit", "Registration", "Continued surveillance"]
    fig, ax = _fig(4.6, 5.4)
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 12.2)
    y = 11.0
    for i, s in enumerate(steps):
        h = 0.95 if "\n" in s else 0.75
        _box(ax, 5.0, y, 7.6, h, f"{i+1}.  {s}", fc="#EDEDED", fs=8.0)
        if i < len(steps) - 1:
            ax.annotate("", xy=(5.0, y - h/2 - 0.55), xytext=(5.0, y - h/2 - 0.08),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
        y -= (h + 0.62)
    ax.set_ylim(y + 0.45, 11.75)
    fig.tight_layout(); out = FIG / "fig7_24_iso_path.png"; fig.savefig(out, facecolor="white"); plt.close(fig)



