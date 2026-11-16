# -*- coding: utf-8 -*-
"""
Clean answer diagrams for ASE Chapter 8 T4 (Exercises 8.19, 8.27, 8.34).
Figures contain only the graph itself; all explanation stays in the Markdown.
Layout rule: every arrow is drawn between box edges, and every T/F label sits
on its own branch, never on a node.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

INK = "#1f2937"
BLUE_FC, BLUE_EC = "#e8f1fb", "#2b6cb0"
ORANGE_FC, ORANGE_EC = "#fdebd0", "#c05621"
GREEN_FC, GREEN_EC = "#e6f6ea", "#2f855a"
GRAY_FC, GRAY_EC = "#eceff3", "#6b7280"


def box(ax, cx, cy, w, h, text, fc, ec, fs=11, weight="bold"):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=ec, lw=1.8, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, fontweight=weight, color=INK, zorder=4)


def arrow(ax, p, q, rad=0.0, color=INK, lw=1.6):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, lw=lw, color=color,
                                 connectionstyle=f"arc3,rad={rad}", zorder=2, shrinkA=0, shrinkB=0))


def label_on(ax, p, q, text, t=0.5, color=INK, fs=10.5):
    x = p[0] + (q[0] - p[0]) * t
    y = p[1] + (q[1] - p[1]) * t
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, fontweight="bold", color=color, zorder=5,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none"))


def flow_graph():
    fig, ax = plt.subplots(figsize=(7.2, 6.6), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(2.2, 11.0)
    ax.axis("off")

    W, H = 2.3, 0.72
    n1, n2 = (5.0, 10.2), (5.0, 8.7)
    n3, n6 = (2.6, 7.0), (7.4, 7.0)
    n4, n5, n7, n8 = (1.4, 5.1), (3.9, 5.1), (6.1, 5.1), (8.6, 5.1)
    n9 = (5.0, 3.0)

    box(ax, *n1, W, H, "1   read A, B, C", ORANGE_FC, ORANGE_EC)
    box(ax, *n2, W, H, "2   if (A > B)", BLUE_FC, BLUE_EC)
    box(ax, *n3, W, H, "3   if (A > C)", BLUE_FC, BLUE_EC)
    box(ax, *n6, W, H, "6   if (C > B)", BLUE_FC, BLUE_EC)
    for c, t in ((n4, "4   print A"), (n5, "5   print C"), (n7, "7   print C"), (n8, "8   print B")):
        box(ax, *c, 1.9, H, t, GREEN_FC, GREEN_EC)
    box(ax, *n9, 3.0, H, "9   exit", ORANGE_FC, ORANGE_EC)

    def bot(c, dx=0.0, w_h=H):
        return (c[0] + dx, c[1] - w_h / 2)

    def top(c, dx=0.0):
        return (c[0] + dx, c[1] + H / 2)

    edges = [
        (bot(n1), top(n2), None),
        (bot(n2), top(n3), "T"), (bot(n2), top(n6), "F"),
        (bot(n3), top(n4), "T"), (bot(n3), top(n5), "F"),
        (bot(n6), top(n7), "T"), (bot(n6), top(n8), "F"),
        (bot(n4), (4.0, n9[1] + H / 2), None), (bot(n5), (4.6, n9[1] + H / 2), None),
        (bot(n7), (5.4, n9[1] + H / 2), None), (bot(n8), (6.0, n9[1] + H / 2), None),
    ]
    for p, q, lab in edges:
        arrow(ax, p, q)
        if lab:
            label_on(ax, p, q, lab, t=0.5, color="#276749" if lab == "T" else "#b91c1c")

    fig.savefig(os.path.join(OUT_DIR, "CH08_EX27_Largest_Flow_Graph.png"), dpi=300, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def cause_effect_graph():
    fig, ax = plt.subplots(figsize=(8.0, 6.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0.6, 9.6)
    ax.axis("off")

    def circ(cx, cy, r, text, fc, ec, fs=11):
        ax.add_patch(Circle((cx, cy), r, fc=fc, ec=ec, lw=1.8, zorder=3))
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, fontweight="bold", color=INK, zorder=4)

    R = 0.46
    causes = {"c2": (1.0, 8.4), "c1": (1.0, 5.4), "c3": (1.0, 2.2)}
    gates = {"g1": (5.2, 8.4, "∧"), "g2": (5.2, 6.4, "∧"), "g3": (5.2, 3.9, "∧"), "g4": (5.2, 1.9, "∧"),
             "g5": (8.0, 5.1, "∨")}
    effects = {"e1": (11.0, 8.4), "e3": (11.0, 5.1), "e2": (11.0, 1.9)}

    for k, (x, y) in causes.items():
        circ(x, y, R, k.replace("c", "c"), BLUE_FC, BLUE_EC)
    for k, (x, y, s) in gates.items():
        circ(x, y, 0.4, s, ORANGE_FC, ORANGE_EC, fs=14)
    for k, (x, y) in effects.items():
        circ(x, y, R, k, GREEN_FC, GREEN_EC)

    def pt(name, side):
        d = {**{k: (v[0], v[1]) for k, v in causes.items()}, **{k: (v[0], v[1]) for k, v in gates.items()},
             **{k: (v[0], v[1]) for k, v in effects.items()}}
        x, y = d[name]
        r = R if name[0] in "ce" else 0.4
        return (x + (r if side == "r" else -r), y)

    def link(a, b, neg=False):
        p, q = pt(a, "r"), pt(b, "l")
        arrow(ax, p, q, lw=1.4)
        if neg:
            label_on(ax, p, q, "~", t=0.78, color="#b91c1c", fs=14)

    link("c2", "g1"); link("c1", "g1")
    link("c1", "g2"); link("c2", "g2", neg=True)
    link("c1", "g3", neg=True); link("c3", "g3")
    link("c1", "g4", neg=True); link("c3", "g4", neg=True)
    link("g2", "g5"); link("g3", "g5")
    link("g1", "e1"); link("g5", "e3"); link("g4", "e2")

    fig.savefig(os.path.join(OUT_DIR, "CH08_EX19_Largest_Cause_Effect_Graph.png"), dpi=300, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def data_flow_graph():
    fig, ax = plt.subplots(figsize=(7.0, 5.4), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(1.6, 9.0)
    ax.axis("off")

    H = 0.8
    pos = {1: (1.6, 7.6), 2: (5.0, 7.6), 3: (5.0, 5.2), 4: (5.0, 2.9), 5: (8.6, 7.6)}
    box(ax, *pos[1], 1.9, H, "1   x = 0", ORANGE_FC, ORANGE_EC)
    box(ax, *pos[2], 2.6, H, "2   while (x < N)", BLUE_FC, BLUE_EC)
    box(ax, *pos[3], 2.6, H, "3   print(x)", BLUE_FC, BLUE_EC)
    box(ax, *pos[4], 2.6, H, "4   x = x + 1", ORANGE_FC, ORANGE_EC)
    box(ax, *pos[5], 1.9, H, "5   exit", GRAY_FC, GRAY_EC)

    arrow(ax, (pos[1][0] + 0.95, 7.6), (pos[2][0] - 1.3, 7.6))
    arrow(ax, (5.0, 7.6 - H / 2), (5.0, 5.2 + H / 2)); label_on(ax, (5.0, 7.2), (5.0, 5.6), "T", color="#276749")
    arrow(ax, (5.0, 5.2 - H / 2), (5.0, 2.9 + H / 2))
    arrow(ax, (pos[2][0] + 1.3, 7.6), (pos[5][0] - 0.95, 7.6)); label_on(ax, (6.3, 7.6), (7.65, 7.6), "F", color="#b91c1c")
    arrow(ax, (pos[4][0] - 1.3, 2.9), (pos[2][0] - 1.3, 7.45), rad=-0.55)

    # tags beside the boxes (short, outside the boxes)
    ax.text(1.6, 6.85, "DEF x", ha="center", fontsize=10, color=ORANGE_EC, fontweight="bold")
    ax.text(5.0, 8.3, "p-use x", ha="center", fontsize=10, color=BLUE_EC, fontweight="bold")
    ax.text(6.6, 5.2, "c-use x", ha="left", va="center", fontsize=10, color=BLUE_EC, fontweight="bold")
    ax.text(6.6, 2.9, "c-use x, then DEF x", ha="left", va="center", fontsize=10, color=ORANGE_EC, fontweight="bold")

    fig.savefig(os.path.join(OUT_DIR, "CH08_EX34_Data_Flow_Graph.png"), dpi=300, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


if __name__ == "__main__":
    flow_graph()
    cause_effect_graph()
    data_flow_graph()
    print("diagrams written to", OUT_DIR)
