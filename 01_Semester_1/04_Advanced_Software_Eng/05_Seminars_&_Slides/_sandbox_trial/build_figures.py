#!/usr/bin/env python3
"""
Sandbox trial -- Chapter 5 Software Design figure set, authored as CODE.
Outputs 2x-scale PNGs (300 dpi effective) into ./figures/.
Engines: matplotlib (curves/ladders), Graphviz (hierarchy), PlantUML (UML seq/class).
English only, clean academic black/white line-art. No copyright images.
"""
import subprocess
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle, Circle

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

GRAPHVIZ_BIN = r"C:\Program Files\Graphviz\bin"
PLANTUML_JAR = Path(r"C:\Windows\Temp\opencode\office_diag\plantuml.jar")

INK = "#111111"
GREY = "#666666"
ACCENT = "#1E3A8A"


def style(ax):
    ax.set_facecolor("white")
    for s in ax.spines.values():
        s.set_color(INK)
    ax.tick_params(colors=INK)
    ax.grid(False)


# ---------------------------------------------------------------- Fig 1: U-curve
def fig01_modularity_cost():
    import numpy as np
    fig, ax = plt.subplots(figsize=(6.4, 5.0), dpi=300)
    style(ax)
    x = np.linspace(1, 20, 400)
    total = 0.35 * x + 40.0 / x          # integration cost + development cost
    integ = 0.35 * x + 2
    dev = 40.0 / x + 1
    ax.plot(x, dev, color=INK, lw=1.6)
    ax.plot(x, integ, color=INK, lw=1.6)
    ax.plot(x, total, color=ACCENT, lw=2.0, ls=(0, (2, 2)))
    i = int(np.argmin(total))
    ax.axvspan(x[i - 25], x[i + 25], color="#E5E7EB", alpha=0.7, zorder=0)
    ax.annotate("Cost to\ndevelop", xy=(3.2, dev[40]), xytext=(3.0, 26),
                fontsize=9, color=INK, ha="center")
    ax.annotate("Cost to\nintegrate", xy=(16, integ[300]), xytext=(16.5, 16),
                fontsize=9, color=INK, ha="center")
    ax.annotate("Total software cost", xy=(x[i] + 2, total[i + 30]), xytext=(12.5, 22),
                fontsize=9, color=ACCENT, ha="center",
                arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.text(x[i], 12.5, "Region of\nMinimum Cost", ha="center", fontsize=9, color=INK)
    ax.set_xlabel("Number of Modules  (M)", fontsize=10, color=INK)
    ax.set_ylabel("Cost of Effort", fontsize=10, color=INK)
    ax.set_xlim(0, 20); ax.set_ylim(0, 30)
    ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    out = FIG / "fig01_modularity_cost.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


# ------------------------------------------------- Fig 2: Conceptual vs Technical
def _box(ax, x, y, w, h, text, fc="white", ec=INK, fs=9, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                linewidth=1.2, edgecolor=ec, facecolor=fc))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=INK, fontweight="bold" if bold else "normal", wrap=True)


def fig02_conceptual_technical():
    fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=300)
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5.4)
    _box(ax, 3.6, 2.2, 2.8, 1.1, "DESIGN\n(problem solving)", fc="#F1F5F9", bold=True)
    _box(ax, 0.3, 0.4, 3.6, 1.1, "CONCEPTUAL design\n\"WHAT the user sees\"\n(screens, reports, data use)")
    _box(ax, 6.1, 0.4, 3.6, 1.1, "TECHNICAL design\n\"HOW it is built\"\n(HW, SW, comm, architecture)")
    _box(ax, 0.5, 3.9, 3.2, 0.9, "Customer\n(requirements)")
    _box(ax, 6.3, 3.9, 3.2, 0.9, "System builders\n(implementation)")
    ax.annotate("", xy=(4.4, 3.3), xytext=(2.1, 3.9),
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate("", xy=(5.6, 3.3), xytext=(7.9, 3.9),
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate("", xy=(2.6, 1.5), xytext=(4.2, 2.2),
                arrowprops=dict(arrowstyle="->", color=INK))
    ax.annotate("", xy=(7.4, 1.5), xytext=(5.8, 2.2),
                arrowprops=dict(arrowstyle="->", color=INK))
    fig.tight_layout()
    out = FIG / "fig02_conceptual_technical.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


# ---------------------------------------------------- Fig 3: Coupling spectrum
def _ladder(ax, items, colors, title=None, worst_label="WORST", best_label="BEST"):
    n = len(items)
    for i, (label, col) in enumerate(zip(items, colors)):
        y = n - i
        ax.add_patch(FancyBboxPatch((0.5, y - 0.32), 6.0, 0.64,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    linewidth=1.1, edgecolor=INK, facecolor=col))
        ax.text(3.5, y, label, ha="center", va="center", fontsize=9.5, color=INK)
    ax.text(6.9, n, worst_label, ha="right", va="center", fontsize=9,
            color="#991B1B", fontweight="bold")
    ax.text(6.9, 1, best_label, ha="right", va="center", fontsize=9,
            color="#15803D", fontweight="bold")
    ax.annotate("", xy=(6.9, n - 0.1), xytext=(6.9, 1.1),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.2))
    ax.set_xlim(0, 7.4); ax.set_ylim(0.4, n + 0.8); ax.axis("off")


def fig03_coupling_spectrum():
    fig, ax = plt.subplots(figsize=(7.4, 5.0), dpi=300)
    _ladder(ax,
            ["Content coupling", "Common coupling", "External coupling",
             "Control coupling", "Stamp coupling", "Data coupling"],
            ["#FCA5A5", "#FDBA74", "#FDE68A", "#BBF7D0", "#86EFAC", "#4ADE80"],
            "Figure 3  |  Coupling Spectrum: Worst to Best",
            "WORST (avoid)", "BEST (target)")
    fig.tight_layout()
    out = FIG / "fig03_coupling_spectrum.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


# ---------------------------------------------------- Fig 4: Cohesion ladder
def fig04_cohesion_ladder():
    fig, ax = plt.subplots(figsize=(7.4, 5.6), dpi=300)
    _ladder(ax,
            ["Coincidental", "Logical", "Temporal", "Procedural",
             "Communicational", "Sequential", "Functional"],
            ["#FCA5A5", "#FDBA74", "#FDE68A", "#FEF08A", "#BBF7D0", "#86EFAC", "#4ADE80"],
            "Figure 4  |  Cohesion Ladder: Weakest to Strongest",
            "WEAKEST", "STRONGEST")
    fig.tight_layout()
    out = FIG / "fig04_cohesion_ladder.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


# ---------------------------------------------------- Fig 5: High vs Low coupling
def fig05_high_low_coupling():
    fig, ax = plt.subplots(figsize=(7.8, 3.8), dpi=300)
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4.4)

    def node(x, y, w=1.7, h=0.8):
        ax.add_patch(Rectangle((x, y), w, h, fill=False, ec=INK, lw=1.2))
        return x + w / 2, y + h / 2

    # High coupling (left)
    a = node(1.0, 2.9); b = node(0.3, 0.6); c = node(2.4, 0.6)
    for p, q, off in [(a, b, 0), (a, b, 5), (a, c, 0), (a, c, 5), (b, c, 0), (b, c, 5)]:
        ax.plot([p[0] + off * 0.04, q[0] + off * 0.04], [p[1], q[1]], color=INK, lw=1.0)
    ax.text(1.7, 3.95, "High Coupling", ha="center", fontsize=10, color="#991B1B",
            fontweight="bold")

    # Low coupling (right)
    d = node(6.6, 2.9); e = node(5.9, 0.6); f = node(8.0, 0.6)
    ax.plot([d[0], e[0]], [d[1], e[1]], color=INK, lw=1.0)
    ax.plot([d[0], f[0]], [d[1], f[1]], color=INK, lw=1.0)
    ax.text(7.3, 3.95, "Low Coupling", ha="center", fontsize=10, color="#15803D",
            fontweight="bold")
    ax.plot([9.85, 9.85], [0.4, 3.9], color="#E5E7EB", lw=1.0)
    fig.tight_layout()
    out = FIG / "fig05_high_low_coupling.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


# ---------------------------------------------------- Fig 6: Common coupling (globals)
def fig06_common_coupling():
    fig, ax = plt.subplots(figsize=(7.4, 4.6), dpi=300)
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5.6)
    _box(ax, 3.4, 4.3, 3.2, 1.0, "GLOBAL DATA AREA\nA1, A2, A3, V1, V2", fc="#FEE2E2")
    for i, (name, msg) in enumerate([("Module X", "Change V1 to Zero"),
                                     ("Module Y", "Increment V1"),
                                     ("Module Z", "V1 = V2 + A1")]):
        x = 0.4 + i * 3.2
        _box(ax, x, 1.0, 2.6, 1.2, f"{name}\n{msg}")
        ax.annotate("", xy=(x + 1.3, 2.2), xytext=(5.0, 4.3),
                    arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(5.0, 0.35, "All modules read/write the same global variables  ->  changes ripple everywhere",
            ha="center", fontsize=8.5, color=GREY)
    fig.tight_layout()
    out = FIG / "fig06_common_coupling.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


# ---------------------------------------------------- Fig 7: Structure chart (Graphviz)
def fig07_structure_chart():
    dot = """
digraph UpdateFile {
  rankdir=TB; nodesep=0.45; ranksep=0.55; bgcolor="white";
  node [shape=box style=filled fillcolor="white" fontname="Helvetica" fontsize=11 height=0.5];
  edge [fontname="Helvetica" fontsize=9 color="#111111"];
  UpdateFile [label="Update File"];
  getValidTrans [label="getValidTrans"];
  getMaster [label="getMaster"];
  updateMaster [label="updateMaster"];
  putNewMaster [label="putNewMaster" peripheries=2];
  getTrans [label="getTrans"];
  validateTrans [label="validate Trans"];
  formatMaster [label="format Master"];
  writeMaster [label="write Master"];
  askContinue [label="ask if User\\nwants to\\ncontinue"];
  UpdateFile -> getValidTrans [label="trans"];
  UpdateFile -> getMaster [label="master"];
  UpdateFile -> updateMaster [label="valid-trans"];
  UpdateFile -> putNewMaster [label="new-master"];
  getValidTrans -> getTrans [label="trans"];
  getValidTrans -> validateTrans [label="valid-trans"];
  putNewMaster -> formatMaster [label="new-master"];
  putNewMaster -> writeMaster [label="format"];
  putNewMaster -> askContinue [label="continue"];
  { rank=same; getValidTrans; getMaster; updateMaster; putNewMaster; }
  { rank=same; getTrans; validateTrans; formatMaster; writeMaster; askContinue; }
}
"""
    src = HERE / "fig07_structure_chart.gv"
    src.write_text(dot, encoding="utf-8")
    out = FIG / "fig07_structure_chart.png"
    subprocess.run([f"{GRAPHVIZ_BIN}\\dot.exe", "-Tpng", "-Gdpi=200", str(src), "-o", str(out)],
                   check=True, capture_output=True, text=True)
    return out


# ---------------------------------------------------- Fig 8: Sequence (PlantUML)
def fig08_sequence():
    puml = r"""
@startuml
skinparam style strictuml
skinparam shadowing false
skinparam defaultFontName Helvetica
skinparam sequenceMessageAlign center
actor Operator
participant "Bar-code Reader" as R
participant "Student Info\nController" as C
participant "Book Info\nController" as B
database "Student DB" as SDB
database "Book DB" as BDB
Operator -> R : 1. Read barcode
R -> C : 2. Submit barcode
C -> SDB : 3. Get student details
SDB --> C : 4. Student details
C -> C : 5. Validate student details
C --> R : 6. Valid / invalid
Operator -> R : 7. Read book code
R -> B : 8. Submit book code
B -> BDB : 9. Check book can be issued
BDB --> B : 10. Issue status
B -> BDB : 11. Update details
BDB --> B : 12. Record added
B --> Operator : 13. Issue successful
@enduml
"""
    puml_path = HERE / "fig08_sequence.puml"
    puml_path.write_text(puml, encoding="utf-8")
    subprocess.run(["java", "-jar", str(PLANTUML_JAR), "-tpng", str(puml_path)],
                   check=True, capture_output=True, text=True)
    gen = puml_path.with_suffix(".png")
    out = FIG / "fig08_sequence.png"
    if gen.exists():
        gen.replace(out)
    return out


# ---------------------------------------------------- Fig 9: Class inheritance (PlantUML)
def fig09_class_inheritance():
    puml = r"""
@startuml
skinparam style strictuml
skinparam shadowing false
skinparam defaultFontName Helvetica
skinparam classAttributeIconSize 0
class Shape {
  - Colour
  + SetColour()
  + Draw()
}
class Square {
  - Point[4]
  + Draw()
}
class Triangle {
  - Point[3]
  + Draw()
}
Shape <|-- Square
Shape <|-- Triangle
note right of Shape : Base class (super class)
note bottom of Square : Desired class (subclass)
@enduml
"""
    puml_path = HERE / "fig09_class_inheritance.puml"
    puml_path.write_text(puml, encoding="utf-8")
    subprocess.run(["java", "-jar", str(PLANTUML_JAR), "-tpng", str(puml_path)],
                   check=True, capture_output=True, text=True)
    gen = puml_path.with_suffix(".png")
    out = FIG / "fig09_class_inheritance.png"
    if gen.exists():
        gen.replace(out)
    return out


# ---------------------------------------------------- Fig 10: OO pipeline (Graphviz)
def fig10_oo_pipeline():
    dot = """
digraph OO {
  rankdir=TB; nodesep=0.3; ranksep=0.4; bgcolor="white";
  node [shape=box style="filled,rounded" fillcolor="#F1F5F9" fontname="Helvetica"
        fontsize=11 color="#1E3A8A" penwidth=1.2];
  edge [color="#1E3A8A" penwidth=1.2];
  P [label="Problem statement", fillcolor="#FEF08A"];
  U [label="1. Create use-case model"];
  A [label="2. Draw activity diagram (if reqd.)"];
  I [label="3. Draw interaction diagrams\\n(sequence + collaboration)"];
  C [label="4. Draw the class diagram"];
  S [label="5. Draw state chart / object\\ndiagram (if reqd.)"];
  D [label="6. Draw component &\\ndeployment diagram"];
  Doc [label="Design documents", fillcolor="#FEF08A"];
  P -> U -> A -> I -> C -> S -> D -> Doc;
}
"""
    src = HERE / "fig10_oo_pipeline.gv"
    src.write_text(dot, encoding="utf-8")
    out = FIG / "fig10_oo_pipeline.png"
    subprocess.run([f"{GRAPHVIZ_BIN}\\dot.exe", "-Tpng", "-Gdpi=200", str(src), "-o", str(out)],
                   check=True, capture_output=True, text=True)
    return out


# ---------------------------------------------------- Fig 0: Design framework
def fig00_design_framework():
    dot = """
digraph Framework {
  rankdir=LR; nodesep=0.22; ranksep=0.35; bgcolor="white";
  node [shape=box style="filled,rounded" fillcolor="#F1F5F9" fontname="Helvetica"
        fontsize=10 color="#1E3A8A" penwidth=1.0 height=0.45 margin="0.08,0.05"];
  edge [color="#1E3A8A" penwidth=1.0 arrowsize=0.7];
  A [label="Initial\\nrequirements", fillcolor="#FEF08A"];
  B [label="Gather\\nrequirements\\ndata"];
  C [label="Analyse\\nrequirements\\ndata"];
  D [label="Conceive\\nhigh-level\\ndesign"];
  E [label="Refine &\\ndocument\\nthe design"];
  F [label="Validate vs\\nrequirements"];
  G [label="Completed\\ndesign", fillcolor="#FEF08A"];
  Q [label="Answer\\nrequirement\\nquestions", fillcolor="#FFFFFF", style="filled,dashed"];
  A -> B -> C -> D -> E -> F -> G;
  F -> Q [style=dashed, constraint=false];
  Q -> D [style=dashed, constraint=false];
}
"""
    src = HERE / "fig00_design_framework.gv"
    src.write_text(dot, encoding="utf-8")
    out = FIG / "fig00_design_framework.png"
    subprocess.run([f"{GRAPHVIZ_BIN}\\dot.exe", "-Tpng", "-Gdpi=200", str(src), "-o", str(out)],
                   check=True, capture_output=True, text=True)
    return out


# ---------------------------------------------------- Fig 12: informal -> detailed
def fig12_informal_to_detailed():
    dot = """
digraph Informal {
  rankdir=LR; nodesep=0.4; ranksep=0.75; bgcolor="white";
  node [shape=box style="filled" fillcolor="#F1F5F9" fontname="Helvetica"
        fontsize=11 color="#1E3A8A" penwidth=1.2 height=0.8 width=1.6];
  edge [color="#1E3A8A" penwidth=1.2];
  A [label="Informal design\\noutline"];
  B [label="Informal\\ndesign"];
  C [label="More formal\\ndesign"];
  D [label="Finished\\ndesign"];
  A -> B -> C -> D;
  B -> A [style=dashed, constraint=false];
  C -> B [style=dashed, constraint=false];
  D -> C [style=dashed, constraint=false];
}
"""
    src = HERE / "fig12_informal_to_detailed.gv"
    src.write_text(dot, encoding="utf-8")
    out = FIG / "fig12_informal_to_detailed.png"
    subprocess.run([f"{GRAPHVIZ_BIN}\\dot.exe", "-Tpng", "-Gdpi=200", str(src), "-o", str(out)],
                   check=True, capture_output=True, text=True)
    return out


def fig13_coupling_degrees():
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 3.0), dpi=300)
    for ax in axes:
        ax.axis("off"); ax.set_xlim(0, 4); ax.set_ylim(0, 4)

    def c(ax, x, y, r=0.32):
        ax.add_patch(Circle((x, y), r, fill=False, ec=INK, lw=1.3))
        return x, y

    # (a) uncoupled
    pts = [(1.0, 2.6), (3.0, 2.6), (1.0, 1.0), (3.0, 1.0)]
    for x, y in pts: c(axes[0], x, y)
    axes[0].set_title("(a) Uncoupled: no dependencies", fontsize=8.5, color=INK)

    # (b) loosely coupled
    b = [(1.0, 2.6), (3.0, 2.6), (1.0, 1.0), (3.0, 1.0)]
    for x, y in b: c(axes[1], x, y)
    for a, z in [(b[0], b[1]), (b[2], b[3]), (b[1], b[3])]:
        axes[1].annotate("", xy=z, xytext=a, arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.0))
    axes[1].set_title("(b) Loosely coupled: some", fontsize=8.5, color=INK)

    # (c) highly coupled
    cc = [(1.0, 2.7), (2.6, 2.7), (1.8, 1.4), (0.8, 0.5), (3.0, 1.2)]
    for x, y in cc: c(axes[2], x, y)
    import itertools
    for a, z in itertools.combinations(cc, 2):
        axes[2].annotate("", xy=z, xytext=a,
                         arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.7))
    axes[2].set_title("(c) Highly coupled: many", fontsize=8.5, color=INK)

    fig.tight_layout()
    out = FIG / "fig13_coupling_degrees.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


def fig14_coupling_example():
    fig, ax = plt.subplots(figsize=(8.2, 3.6), dpi=300)
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4.6)

    def pair(x0, title, label, color):
        _box(ax, x0 + 0.7, 3.3, 2.6, 0.8, "Edit student record")
        _box(ax, x0 + 0.7, 0.6, 2.6, 0.8, "Retrieve student record")
        ax.annotate("", xy=(x0 + 2.0, 3.3), xytext=(x0 + 2.0, 1.4),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
        ax.annotate("", xy=(x0 + 3.4, 1.4), xytext=(x0 + 3.4, 3.3),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
        ax.text(x0 + 1.55, 2.35, label, ha="right", va="center", fontsize=8.0, color=color)
        ax.text(x0 + 3.6, 2.35, "Student record,\nEOF", ha="left", va="center", fontsize=8.0, color=INK)
        ax.text(x0 + 2.0, 4.25, title, ha="center", fontsize=9.5, color=color, fontweight="bold")

    pair(0.0, "Poor design: Tight Coupling", "Student name,\nStudent ID,\naddress, course", "#991B1B")
    pair(5.0, "Good design: Loose Coupling", "Student ID", "#15803D")
    ax.plot([4.9, 4.9], [0.2, 4.5], color="#E5E7EB", lw=1.0)
    fig.tight_layout()
    out = FIG / "fig14_coupling_example.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


def fig15_bottom_up_tree():
    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=300)
    ax.axis("off"); ax.set_xlim(-0.5, 5.5); ax.set_ylim(-0.6, 2.6)
    top = (2.5, 2.2)
    mids = [(1.0, 1.3), (2.5, 1.3), (4.0, 1.3)]
    bots = [(0.3, 0.3), (1.1, 0.3), (1.9, 0.3), (2.9, 0.3), (3.6, 0.3), (4.6, 0.3)]
    for (x, y) in mids + bots:
        ax.add_patch(Circle((x, y), 0.2, fill=True, fc="#DBEAFE", ec=INK, lw=1.0))
    ax.add_patch(FancyBboxPatch((top[0] - 0.5, top[1] - 0.18), 1.0, 0.36,
                                boxstyle="round,pad=0.02", fc="#FEF08A", ec=INK, lw=1.1))
    ax.text(top[0], top[1], "whole\nprogram", ha="center", va="center", fontsize=8)
    cross = {0: [1, 2], 1: [0, 1], 2: [1], 3: [1, 2], 4: [2], 5: [1, 2]}
    for bi, ms in cross.items():
        for mi in ms:
            ax.plot([bots[bi][0], mids[mi][0]], [bots[bi][1] + 0.2, mids[mi][1] - 0.2],
                    color=GREY, lw=0.8)
    for m in mids:
        ax.plot([m[0], top[0]], [m[1] + 0.2, top[1] - 0.2], color=INK, lw=1.0)
    ax.text(2.5, -0.4, "library modules combine upward into larger ones (cross-linked tree)",
            ha="center", fontsize=8, color=GREY)
    fig.tight_layout()
    out = FIG / "fig15_bottom_up_tree.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


def fig16_topdown_vs_reusable():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6), dpi=300)
    for ax, title in zip(axes, ["Top-down structure", "Design reusable structure"]):
        ax.axis("off"); ax.set_xlim(0, 6); ax.set_ylim(0, 4.4)
        ax.set_title(title, fontsize=10, color=ACCENT, fontweight="bold")
    import numpy as np
    def box(ax, x, y, w=1.1, h=0.6, t=""):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="#F1F5F9", ec=INK, lw=1.0))
        if t:
            ax.text(x, y, t, ha="center", va="center", fontsize=7.5)
    # left: top-down
    a = axes[0]
    box(a, 3, 3.6, 1.4, 0.6, "root")
    box(a, 1.6, 2.2); box(a, 4.4, 2.2)
    for x in (0.8, 2.4):
        box(a, x, 0.8)
        a.plot([1.6, x], [1.9, 1.1], color=INK, lw=1.0)
    for x in (3.6, 5.2):
        box(a, x, 0.8)
        a.plot([4.4, x], [1.9, 1.1], color=INK, lw=1.0)
    a.plot([3, 1.6], [3.3, 2.5], color=INK, lw=1.0)
    a.plot([3, 4.4], [3.3, 2.5], color=INK, lw=1.0)
    # right: reusable
    b = axes[1]
    box(b, 3, 3.6, 1.4, 0.6, "root")
    box(b, 1.6, 2.2); box(b, 4.4, 2.2)
    box(b, 3, 0.9, 1.5, 0.6, "shared module")
    b.plot([3, 1.6], [3.3, 2.5], color=INK, lw=1.0)
    b.plot([3, 4.4], [3.3, 2.5], color=INK, lw=1.0)
    b.plot([1.6, 3], [1.9, 1.2], color=INK, lw=1.0)
    b.plot([4.4, 3], [1.9, 1.2], color=INK, lw=1.0)
    fig.tight_layout()
    out = FIG / "fig16_topdown_vs_reusable.png"
    fig.savefig(out, facecolor="white"); plt.close(fig)
    return out


def main():
    builders = [
        ("Fig 0  design framework", fig00_design_framework),
        ("Fig 1  modularity cost", fig01_modularity_cost),
        ("Fig 13 coupling degrees", fig13_coupling_degrees),
        ("Fig 14 coupling example", fig14_coupling_example),
        ("Fig 15 bottom-up tree", fig15_bottom_up_tree),
        ("Fig 16 topdown vs reusable", fig16_topdown_vs_reusable),
        ("Fig 2  conceptual/technical", fig02_conceptual_technical),
        ("Fig 3  coupling spectrum", fig03_coupling_spectrum),
        ("Fig 4  cohesion ladder", fig04_cohesion_ladder),
        ("Fig 5  high/low coupling", fig05_high_low_coupling),
        ("Fig 6  common coupling", fig06_common_coupling),
        ("Fig 7  structure chart", fig07_structure_chart),
        ("Fig 8  sequence diagram", fig08_sequence),
        ("Fig 9  class inheritance", fig09_class_inheritance),
        ("Fig 10 OO pipeline", fig10_oo_pipeline),
        ("Fig 12 informal->detailed", fig12_informal_to_detailed),
    ]
    ok, fail = 0, 0
    for name, fn in builders:
        try:
            out = fn()
            size = out.stat().st_size if out.exists() else 0
            print(f"[OK]   {name:32s} -> {out.name} ({size//1024} KB)")
            ok += 1
        except Exception as e:
            print(f"[FAIL] {name:32s} :: {e}")
            fail += 1
    print(f"\nFigures built: {ok} ok, {fail} failed")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
