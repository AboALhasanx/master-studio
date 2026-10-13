# -*- coding: utf-8 -*-
"""
visio_structure_chart.py  (v2)
------------------------------
Render a real SE **structure chart** (Aggarwal & Singh, Ch.5, slides 41-45)
using Microsoft Visio via COM (win32com), then export to PNG.

Hard-won facts baked in
-----------------------
* Visio.InvisibleApp dispatches (Version 16.0 confirmed).
* DrawLine(x1,y1,x2,y2) draws a *static* line you can arrow + label; dynamic
  connectors are fussier and not needed here.
* Visio text boxes DO reorder mixed punctuation on RTL hosts (the same BiDi
  family of bugs as the study PDFs). => every string we hand to Visio must be
  punctuation-clean: avoid stray `)` `(` `.` `·` `—` inside a line that also
  holds words, and never put ASCII punctuation adjacent to digits inside text
  meant to read left-to-right. We keep Visio text to plain words + `/` + `:`.
* Connector label rotation is governed by the shape's text angle; leaving it
  unset lets Visio auto-rotate along the line. We instead place a *separate*
  small text box next to the arrow so the label always stays horizontal.

Layout model
------------
Top-down tree. For each parent, a horizontal "bus" runs BELOW the parent box
(its y = parent_bottom - stub). Children hang from that bus by drop-stubs into
their top edge. A short stub connects the parent's bottom to the bus. All
arrows point DOWNWARD.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import win32com.client as win32


class VisioChart:
    def __init__(self, visible: bool = False):
        self.app = win32.Dispatch("Visio.InvisibleApp")
        self.app.Visible = 1 if visible else 0
        self.app.AlertResponse = 7
        self.app.ScreenUpdating = 0
        self.doc = self.app.Documents.Add("")
        self.page = self.doc.Pages.Item(1)

    # ------------------------------------------------------------------ utils
    def clear_page(self):
        while self.page.Shapes.Count > 0:
            self.page.Shapes.Item(1).Delete()

    def set_page_size(self, w, h):
        ps = self.page.PageSheet
        ps.CellsU("PageWidth").ResultIU = w
        ps.CellsU("PageHeight").ResultIU = h

    def add_box(self, cx, cy, w, h, text,
                fill="RGB(240,246,255)", line="RGB(60,90,140)",
                fontsize=10.0, bold=1, size_out=None):
        shp = self.page.DrawRectangle(cx - w / 2.0, cy - h / 2.0,
                                      cx + w / 2.0, cy + h / 2.0)
        shp.Text = text
        shp.CellsU("FillForegnd").FormulaU = fill
        shp.CellsU("LineColor").FormulaU = line
        shp.CellsU("LineWeight").FormulaU = "1.25 pt"
        if size_out is not None:
            shp.CellsU("Char.Size").FormulaU = f"{size_out} pt"
        else:
            shp.CellsU("Char.Size").FormulaU = f"{fontsize} pt"
        shp.CellsU("Char.Style").FormulaU = "1" if bold else "0"
        shp.CellsU("Para.HorzAlign").FormulaU = "1"
        shp.CellsU("VerticalAlign").FormulaU = "1"
        shp.CellsU("Rounding").FormulaU = "0.08 in"
        return shp

    def add_line(self, x1, y1, x2, y2, color="RGB(60,90,140)",
                 width_pt=1.25, end_arrow=4, dashed=False):
        c = self.page.DrawLine(x1, y1, x2, y2)
        c.CellsU("LineColor").FormulaU = color
        c.CellsU("LineWeight").FormulaU = f"{width_pt} pt"
        c.CellsU("EndArrow").FormulaU = str(end_arrow)
        c.CellsU("BeginArrow").FormulaU = "0"
        if dashed:
            c.CellsU("LinePattern").FormulaU = "2"
        return c

    def add_text(self, cx, cy, w, h, text, fontsize=9.0, align=1,
                 color="RGB(30,30,30)", bold=0):
        t = self.page.DrawRectangle(cx - w / 2.0, cy - h / 2.0,
                                    cx + w / 2.0, cy + h / 2.0)
        t.Text = text
        t.CellsU("LinePattern").FormulaU = "0"
        t.CellsU("FillPattern").FormulaU = "0"
        t.CellsU("Char.Size").FormulaU = f"{fontsize} pt"
        t.CellsU("Char.Color").FormulaU = color
        t.CellsU("Char.Style").FormulaU = "1" if bold else "0"
        t.CellsU("Para.HorzAlign").FormulaU = str(align)
        t.CellsU("VerticalAlign").FormulaU = "1"
        return t

    def save(self, path):
        full = os.path.abspath(path)
        if os.path.exists(full):
            os.remove(full)
        self.doc.SaveAs(full)

    def export_png(self, path):
        full = os.path.abspath(path)
        if os.path.exists(full):
            os.remove(full)
        self.page.Export(full)

    def close(self):
        for fn in (self.doc.Close, self.app.Quit):
            try:
                fn()
            except Exception:
                pass


def render_spec(chart: VisioChart, spec: dict):
    chart.clear_page()
    pg = spec.get("page", {})
    page_w = pg.get("w", 11.0)
    page_h = pg.get("h", 8.5)
    chart.set_page_size(page_w, page_h)

    # ---- lay out node centres -------------------------------------------
    levels: dict[int, list] = {}
    for n in spec["nodes"]:
        levels.setdefault(int(n["level"]), []).append(n)

    # vertical bands
    top_pad = 1.05          # reserved for the title
    bot_pad = 0.75
    max_level = max(levels) if levels else 0
    band = (page_h - top_pad - bot_pad) / (max_level + 1) if (max_level + 1) else 1.0

    pos = {}
    for lvl, nodes in levels.items():
        nodes = sorted(nodes, key=lambda d: d.get("order", 0))
        k = len(nodes)
        y = page_h - top_pad - lvl * band - band / 2.0
        for i, n in enumerate(nodes):
            # explicit x_frac (fraction of page width) wins over even spacing
            if "x_frac" in n:
                x = page_w * float(n["x_frac"])
            else:
                x = page_w * (i + 1) / (k + 1)
            pos[n["id"]] = (x, y, n.get("w", 1.7), n.get("h", 0.66))

    # ---- edges: parent bottom -> bus -> child top, arrows downward -------
    for e in spec.get("edges", []):
        a, b = e["from"], e["to"]
        if a not in pos or b not in pos:
            continue
        ax, ay, aw, ah = pos[a]
        bx, by, bw, bh = pos[b]
        a_bot = ay - ah / 2.0
        b_top = by + bh / 2.0
        if b_top >= a_bot:      # safety: skip non-descending edges
            continue
        midy = (a_bot + b_top) / 2.0
        col = e.get("color", "RGB(60,90,140)")

        # parent stub down to the bus
        chart.add_line(ax, a_bot, ax, midy, color=col)
        # horizontal bus
        chart.add_line(ax, midy, bx, midy, color=col)
        # drop stub into the child (arrowhead)
        chart.add_line(bx, midy, bx, b_top, color=col)

        lbl = e.get("label", "")
        if lbl:
            # place the label to the RIGHT of the drop stub, horizontal
            chart.add_text(bx + 0.62, (midy + b_top) / 2.0, 1.15, 0.22,
                           lbl, fontsize=8.5, align=0,
                           color=e.get("label_color", "RGB(20,20,20)"))

    # ---- boxes on top ----------------------------------------------------
    for n in spec["nodes"]:
        x, y, w, h = pos[n["id"]]
        chart.add_box(x, y, w, h, n["text"],
                      fill=n.get("fill", "RGB(240,246,255)"),
                      line=n.get("line", "RGB(60,90,140)"),
                      fontsize=n.get("fontsize", 10.0))

    # ---- title -----------------------------------------------------------
    if spec.get("title"):
        chart.add_text(page_w / 2.0, page_h - 0.45, page_w - 1.0, 0.5,
                       spec["title"], fontsize=13.0, align=1, bold=1)

    # ---- side notes (horizontal, wrapped by our own newlines) ------------
    for s in spec.get("side_notes", []):
        chart.add_text(s["x"], s["y"], s.get("w", 3.2), s.get("h", 0.9),
                       s["text"], fontsize=s.get("fontsize", 8.5), align=0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--png", required=True)
    args = ap.parse_args()

    with open(args.spec, "r", encoding="utf-8") as fh:
        spec = json.load(fh)

    chart = VisioChart(visible=False)
    try:
        render_spec(chart, spec)
        chart.save(args.out)
        chart.export_png(args.png)
        time.sleep(0.4)
        print("VSDX:", os.path.abspath(args.out), os.path.getsize(os.path.abspath(args.out)))
        if os.path.exists(os.path.abspath(args.png)):
            print("PNG :", os.path.abspath(args.png), os.path.getsize(os.path.abspath(args.png)))
        else:
            print("PNG : NOT WRITTEN", file=sys.stderr)
    finally:
        chart.close()


if __name__ == "__main__":
    main()
