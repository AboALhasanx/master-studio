# -*- coding: utf-8 -*-
"""
visio_uml_render.py
-------------------
Drop REAL Microsoft Visio UML master shapes onto a page and export to PNG.

Unlike the earlier hand-drawn structure chart, this uses Visio's own
shipped UML stencils (the proper notation: stick-figure actors, ellipses,
system boundary, class boxes with compartments, sequence lifelines).

Hard-won facts
--------------
* Visio REFUSES to open stencils that live under `C:\Program Files\...`
  (`File not found`). Copy the .vssx/.vstx into a WRITABLE folder first;
  then `Documents.OpenEx(path, 2|8)` works and `doc.Masters` enumerates.
* Available stencils (copied into ./stencils):
    UUSEME_M.VSSX               -> Actor, Use Case, Subsystem, Association,
                                   Dependency, Generalization, Include, Extend
    USEQME_M.VSSX               -> Actor/Object lifeline, Activation, Message,
                                   Return Message, Self Message, Loop/Opt/Alt
                                   fragments, Interaction operand
    ASSOCIATIONS_UML_CLASS_M.VSTX -> Class, Member, Separator, Aggregation,
                                   Association, Composition
    INTERFACE_UML_CLASS_M.VSTX  -> Interface, Enumeration, Directed
                                   Association, Dependency, Interface Realization
    UML_CLASS_M.VSTX            -> Class, Inheritance, Directed Association
    DBUML_M.VSSX                -> Entity, Attribute, Key, Relationship
    SDL_M.VSSX                  -> Decision, Process, Terminator, ...
* Drop a master:  shp = page.Drop(master, x, y)   (x,y = centre, inches)
* Set text:       shp.Text = "..."
* Resize:         shp.CellsU("Width").ResultIU / shp.CellsU("Height").ResultIU
* Connect two shapes: use page.Drop(app.ConnectorToolDataObject, x, y) then
  conn.CellsU("BeginX").GlueTo(from.CellsU("PinX")) ; EndX.GlueTo(to PinX).
  Simpler + robust: draw a DrawLine with an arrowhead, OR glue a dynamic
  connector. For clarity here we use glued dynamic connectors when the
  stencil provides "Dynamic connector", else DrawLine.
* RTL/BiDi in Visio text: AVOID a Latin word immediately followed by a digit,
  and avoid commas before words. Same rule as the structure chart.
"""

from __future__ import annotations

import argparse
import os
import time

import win32com.client as win32

LAB = os.path.dirname(os.path.abspath(__file__))
STENCIL_DIR = os.path.join(LAB, "stencils")


class UML:
    def __init__(self, visible=False):
        self.app = win32.Dispatch("Visio.InvisibleApp")
        self.app.Visible = 1 if visible else 0
        self.app.AlertResponse = 7
        self.app.ScreenUpdating = 0
        self.doc = self.app.Documents.Add("")
        self.page = self.doc.Pages.Item(1)
        self._masters = {}   # cached stencil docs

    # ---------------------------------------------------------------- stencil
    def load(self, stencil_file):
        """Open a stencil read-only+hidden and return {Name: Master}."""
        if stencil_file in self._masters:
            return self._masters[stencil_file]
        path = os.path.join(STENCIL_DIR, stencil_file)
        d = self.app.Documents.OpenEx(path, 2 | 8)   # visOpenRO|visOpenHidden
        table = {m.Name: m for m in d.Masters}
        self._masters[stencil_file] = table
        return table

    def page_size(self, w, h):
        ps = self.page.PageSheet
        ps.CellsU("PageWidth").ResultIU = w
        ps.CellsU("PageHeight").ResultIU = h

    def drop(self, master, x, y, text=None, w=None, h=None):
        shp = self.page.Drop(master, x, y)
        if w is not None:
            shp.CellsU("Width").ResultIU = w
        if h is not None:
            shp.CellsU("Height").ResultIU = h
        if text is not None:
            shp.Text = text
        return shp

    def label(self, cx, cy, w, h, text, size=10.0, bold=0, align=1,
              color="RGB(20,20,20)"):
        t = self.page.DrawRectangle(cx - w / 2.0, cy - h / 2.0,
                                    cx + w / 2.0, cy + h / 2.0)
        t.Text = text
        t.CellsU("LinePattern").FormulaU = "0"
        t.CellsU("FillPattern").FormulaU = "0"
        t.CellsU("Char.Size").FormulaU = f"{size} pt"
        t.CellsU("Char.Color").FormulaU = color
        t.CellsU("Char.Style").FormulaU = "1" if bold else "0"
        t.CellsU("Para.HorzAlign").FormulaU = str(align)
        t.CellsU("VerticalAlign").FormulaU = "1"
        return t

    def box(self, x1, y1, x2, y2, line="RGB(60,90,140)", fill=None,
            width_pt=1.0, dashed=False, rounding=None):
        s = self.page.DrawRectangle(x1, y1, x2, y2)
        s.CellsU("LineColor").FormulaU = line
        s.CellsU("LineWeight").FormulaU = f"{width_pt} pt"
        if fill:
            s.CellsU("FillForegnd").FormulaU = fill
        if dashed:
            s.CellsU("LinePattern").FormulaU = "2"
        if rounding is not None:
            s.CellsU("Rounding").FormulaU = f"{rounding} in"
        return s

    def line(self, x1, y1, x2, y2, arrow=4, color="RGB(60,90,140)",
             width_pt=1.1, dashed=False, begin_arrow=0):
        c = self.page.DrawLine(x1, y1, x2, y2)
        c.CellsU("LineColor").FormulaU = color
        c.CellsU("LineWeight").FormulaU = f"{width_pt} pt"
        c.CellsU("EndArrow").FormulaU = str(arrow)
        c.CellsU("BeginArrow").FormulaU = str(begin_arrow)
        if dashed:
            c.CellsU("LinePattern").FormulaU = "2"
        return c

    def glue(self, from_shp, to_shp, begin_arrow=0, end_arrow=4,
             color="RGB(60,90,140)", dashed=False):
        """Glue a dynamic connector between two shapes (auto-routes)."""
        conn = self.page.Drop(self.app.ConnectorToolDataObject, 0, 0)
        conn.CellsU("BeginX").GlueTo(from_shp.CellsU("PinX"))
        conn.CellsU("EndX").GlueTo(to_shp.CellsU("PinX"))
        conn.CellsU("LineColor").FormulaU = color
        conn.CellsU("BeginArrow").FormulaU = str(begin_arrow)
        conn.CellsU("EndArrow").FormulaU = str(end_arrow)
        if dashed:
            conn.CellsU("LinePattern").FormulaU = "2"
        return conn

    # ------------------------------------------------------------------ output
    def class_box(self, x, y, w, name, attrs, ops, name_h=0.32,
                  row_h=0.20, line="RGB(40,60,100)", fill="RGB(248,250,255)"):
        """Draw a UML class box with three compartments: name | attributes |
        operations. Returns a dict with the anchor points used by connectors.

        We draw this manually rather than using the stencil's Class master
        because that master's compartment composition is unpredictable; a
        hand-drawn box gives exact, deterministic layout.
        """
        n_attr = len(attrs)
        n_ops = len(ops)
        attr_h = max(1, n_attr) * row_h
        ops_h = max(1, n_ops) * row_h
        total_h = name_h + attr_h + ops_h
        top = y + total_h / 2.0
        bot = y - total_h / 2.0
        left = x - w / 2.0
        right = x + w / 2.0

        # outer rectangle
        outer = self.page.DrawRectangle(left, bot, right, top)
        outer.CellsU("LineColor").FormulaU = line
        outer.CellsU("LineWeight").FormulaU = "1.25 pt"
        outer.CellsU("FillForegnd").FormulaU = fill
        outer.CellsU("Rounding").FormulaU = "0"

        # name compartment band (fill) + text
        name_band = self.page.DrawRectangle(left, top - name_h, right, top)
        name_band.CellsU("LinePattern").FormulaU = "0"
        name_band.CellsU("FillForegnd").FormulaU = "RGB(219,234,254)"

        t = self.page.DrawRectangle(left + 0.04, top - name_h, right - 0.04, top)
        t.Text = name
        t.CellsU("LinePattern").FormulaU = "0"
        t.CellsU("FillPattern").FormulaU = "0"
        t.CellsU("Char.Size").FormulaU = "9.5 pt"
        t.CellsU("Char.Style").FormulaU = "1"
        t.CellsU("Para.HorzAlign").FormulaU = "1"
        t.CellsU("VerticalAlign").FormulaU = "1"

        # separator under name
        sep1 = self.page.DrawLine(left, top - name_h, right, top - name_h)
        sep1.CellsU("LineColor").FormulaU = line
        sep1.CellsU("LineWeight").FormulaU = "1.0 pt"
        # separator between attributes and operations
        ymid = top - name_h - attr_h
        sep2 = self.page.DrawLine(left, ymid, right, ymid)
        sep2.CellsU("LineColor").FormulaU = line
        sep2.CellsU("LineWeight").FormulaU = "1.0 pt"

        # attribute text (left aligned)
        if attrs:
            at = self.page.DrawRectangle(left + 0.07, ymid, right - 0.07,
                                         top - name_h - 0.03)
            at.Text = "\n".join(attrs)
            at.CellsU("LinePattern").FormulaU = "0"
            at.CellsU("FillPattern").FormulaU = "0"
            at.CellsU("Char.Size").FormulaU = "8 pt"
            at.CellsU("Para.HorzAlign").FormulaU = "0"
            at.CellsU("VerticalAlign").FormulaU = "0"

        # operations text (left aligned)
        if ops:
            ot = self.page.DrawRectangle(left + 0.07, bot + 0.03, right - 0.07,
                                         ymid - 0.03)
            ot.Text = "\n".join(ops)
            ot.CellsU("LinePattern").FormulaU = "0"
            ot.CellsU("FillPattern").FormulaU = "0"
            ot.CellsU("Char.Size").FormulaU = "8 pt"
            ot.CellsU("Para.HorzAlign").FormulaU = "0"
            ot.CellsU("VerticalAlign").FormulaU = "0"

        return {"cx": x, "cy": y, "top": top, "bot": bot,
                "left": left, "right": right, "h": total_h, "w": w}

    def save(self, path):
        full = os.path.abspath(path)
        if os.path.exists(full):
            os.remove(full)
        self.doc.SaveAs(full)

    def export(self, png):
        full = os.path.abspath(png)
        if os.path.exists(full):
            os.remove(full)
        self.page.Export(full)

    def close(self):
        for fn in (self.doc.Close, self.app.Quit):
            try:
                fn()
            except Exception:
                pass


# ============================================================================
# USE CASE DIAGRAM
# ============================================================================
def use_case_diagram(out_vsdx, out_png):
    """Library Management System use-case diagram (chapter case study).

    Mirrors the structure on slides 84-92: actors around a system boundary,
    use cases inside, include/extend dependencies.
    """
    u = UML()
    u.page_size(12.0, 8.6)
    S = u.load("UUSEME_M.VSSX")
    actor, uc = S["Actor"], S["Use Case"]

    # system boundary
    u.box(3.75, 0.85, 9.35, 7.25, line="RGB(30,64,175)", width_pt=1.4,
          rounding=0.15)
    u.label(6.55, 6.95, 5.2, 0.35, "Library Management System",
            size=12, bold=1, color="RGB(30,64,175)")

    # actors (left + right), spaced to avoid crossing
    a_student  = u.drop(actor, 1.60, 5.55, "Student",       w=0.55, h=1.35)
    a_operator = u.drop(actor, 1.60, 2.85, "Operator",      w=0.55, h=1.35)
    a_barcode  = u.drop(actor, 11.45, 4.20, "Bar-code\nReader", w=0.60, h=1.45)

    # use cases (inside the boundary)
    e1 = u.drop(uc, 5.35, 5.55, "Issue Book",              w=1.90, h=0.85)
    e2 = u.drop(uc, 5.35, 3.55, "Return Book",             w=1.90, h=0.85)
    e3 = u.drop(uc, 8.35, 6.05, "Query Book",              w=1.90, h=0.85)
    e4 = u.drop(uc, 8.35, 4.05, "Maintain Student\nDetail", w=2.05, h=0.98)
    e5 = u.drop(uc, 5.35, 1.75, "Login",                   w=1.55, h=0.80)
    e6 = u.drop(uc, 8.35, 1.85, "Print Receipt",           w=1.80, h=0.82)

    # actor -> use case associations (straight, non-crossing where possible)
    for e in (e1, e2, e3):
        u.glue(a_student, e, color="RGB(70,70,70)")
    u.glue(a_operator, e1, color="RGB(70,70,70)")
    u.glue(a_operator, e2, color="RGB(70,70,70)")
    u.glue(a_operator, e4, color="RGB(70,70,70)")
    u.glue(a_operator, e5, color="RGB(70,70,70)")
    u.glue(a_barcode, e1, color="RGB(70,70,70)")
    u.glue(a_barcode, e2, color="RGB(70,70,70)")

    # include: Issue Book and Return Book both include Login
    u.line(5.10, 5.12, 5.10, 2.16, arrow=4, dashed=True, width_pt=1.0)
    u.label(6.35, 3.55, 1.30, 0.24, "include", size=8.5)
    # extend: Print Receipt extends Issue Book
    u.line(8.35, 1.44, 8.35, 1.44, arrow=0)
    u.line(8.35, 2.26, 6.30, 2.26, arrow=0, dashed=True, width_pt=1.0)
    u.line(6.30, 2.26, 6.30, 2.26, arrow=0)
    u.label(7.35, 2.42, 1.25, 0.24, "extend", size=8.5)
    # dependency: Maintain Student Detail is used by Operator-maintained flows
    u.line(8.35, 3.56, 8.35, 2.30, arrow=4, dashed=True, width_pt=1.0)

    u.label(6.0, 8.15, 11.0, 0.5,
            "Use Case Diagram  /  Library Management System  /  chapter slides",
            size=13, bold=1)

    u.save(out_vsdx)
    u.export(out_png)
    u.close()


def class_diagram(out_vsdx, out_png):
    """Entity class diagram for the Library System (matches slide 93) plus the
    OOD relationship kinds from slides 77-78 (association / dependency /
    generalisation)."""
    u = UML()
    u.page_size(13.0, 9.2)

    def cb(x, y, w, name, attrs, ops, name_h=0.34, row_h=0.20):
        return u.class_box(x, y, w, name, attrs, ops,
                           name_h=name_h, row_h=row_h)

    # --- entity classes (slide 93) -------------------------------------
    book = cb(4.35, 7.10, 2.95, "Book Details",
              ["Book Id", "Book Name", "Author Name", "Publisher",
               "Copies in Book Bank", "Copies in General"],
              ["Add Book()", "Update No Of Copies()"])
    student = cb(9.10, 7.10, 3.15, "Student Details",
                 ["Student Barcode Id", "Student Roll no", "Name", "Course",
                  "No of Book Bank Issued", "No of General Issued"],
                 ["Get Student Details()", "Add Student()", "Delete Student()"])
    issued = cb(4.35, 3.95, 2.95, "Issued Book Details",
                ["Book Id", "Barcode Id", "Issued"],
                ["Add()", "Delete()", "Issue()", "Return()"])
    sib = cb(9.10, 3.95, 3.15, "Student Issued Book Details",
             ["Student Barcode Id", "Book Barcode Id"],
             ["Add()", "Delete()"])
    login = cb(0.95, 3.95, 2.55, "Login Details",
               ["User Id", "User Name", "Password", "User Role"],
               ["Add()", "Delete()", "Update()"])
    # generalisation children
    bbb = cb(3.55, 1.30, 2.15, "Book Bank Book", ["IssueLimit"], [])
    gbk = cb(6.15, 1.30, 2.15, "General Book", ["IssueLimit"], [])

    # --- relationships --------------------------------------------------
    # dependency (unidirectional, dashed) : Issued Book Details -> Book Details
    u.line(issued["cx"] - 0.75, issued["top"], issued["cx"] - 0.75, book["bot"],
           arrow=4, dashed=True, width_pt=1.0)
    u.label(issued["cx"] - 0.05, 5.75, 1.6, 0.24, "dependency", size=8.0)
    # dependency : Student Issued Book Details -> Student Details
    u.line(sib["cx"], sib["top"], sib["cx"], student["bot"],
           arrow=4, dashed=True, width_pt=1.0)
    u.label(sib["cx"] + 1.15, 5.55, 1.6, 0.24, "dependency", size=8.0)
    # association : Issued Book Details <-> Student Issued Book Details
    u.line(issued["right"], issued["cy"], sib["left"], sib["cy"],
           arrow=0, width_pt=1.1)
    u.label((issued["right"] + sib["left"]) / 2.0, issued["cy"] + 0.28,
            1.5, 0.24, "association", size=8.0)
    # Login Details association to Issued records
    u.line(login["right"], login["cy"], issued["left"], issued["cy"],
           arrow=0, width_pt=1.1)
    u.label((login["right"] + issued["left"]) / 2.0, login["cy"] + 0.28,
            1.2, 0.24, "used by", size=8.0)

    # generalisation : Book Bank Book & General Book -> Book Details
    # children sit BELOW; the shared bar is above them; a single stem rises
    # from the bar to Book Details' bottom edge, arrowhead pointing UP (parent).
    bar_y = 2.55
    u.line(bbb["cx"], bbb["top"], bbb["cx"], bar_y, width_pt=1.0)
    u.line(gbk["cx"], gbk["top"], gbk["cx"], bar_y, width_pt=1.0)
    u.line(bbb["cx"], bar_y, gbk["cx"], bar_y, width_pt=1.0)
    stem_x = (bbb["cx"] + gbk["cx"]) / 2.0
    u.line(stem_x, bar_y, stem_x, book["bot"], arrow=4, width_pt=1.0)
    u.label(stem_x + 1.00, 2.85, 1.6, 0.24, "generalisation", size=8.0)

    u.label(6.5, 8.85, 12.0, 0.5,
            "Entity Class Diagram  /  Library System  /  chapter slide",
            size=13, bold=1)

    u.save(out_vsdx)
    u.export(out_png)
    u.close()


def sequence_diagram(out_vsdx, out_png):
    """UML sequence diagram for 'Issue Book' in the Library System.

    Objects typed per slide 75: boundary (interface) / control / entity.
    Messages mirror the sequence described in the chapter's case study.
    """
    u = UML()
    u.page_size(12.4, 8.6)

    # lifeline x positions
    xs = {"user": 1.45, "ui": 4.15, "ctrl": 6.95, "ent": 9.75}
    top = 7.85
    bottom = 0.85
    head_h = 0.62

    def lifeline(x, title, stereotype):
        # header box
        h = u.box(x - 0.95, top - head_h, x + 0.95, top,
                  line="RGB(40,60,100)", fill="RGB(219,234,254)")
        u.label(x, top - head_h + 0.20, 1.80, 0.26, title,
                size=9.0, bold=1)
        u.label(x, top - head_h + 0.52, 1.80, 0.22, stereotype,
                size=7.5, color="RGB(90,90,90)")
        # dashed lifeline
        u.line(x, top - head_h, x, bottom, arrow=0, dashed=True,
               width_pt=0.9, color="RGB(120,120,120)")

    lifeline(xs["user"], "User", "actor")
    lifeline(xs["ui"],   "Query book interface", "boundary")
    lifeline(xs["ctrl"], "Query operator", "control")
    lifeline(xs["ent"],  "Book details", "entity")

    def msg(x_from, x_to, y, text, dashed=False, arrow=4):
        # activation bar (small) at the receiver
        u.line(x_from, y, x_to, y, arrow=arrow, dashed=dashed, width_pt=1.0)
        u.label((x_from + x_to) / 2.0, y + 0.155, abs(x_to - x_from) - 0.1,
                0.22, text, size=7.8)

    def self_msg(x, y, text):
        u.line(x, y, x + 0.75, y, arrow=0, width_pt=1.0)
        u.line(x + 0.75, y, x + 0.75, y - 0.30, width_pt=1.0)
        u.line(x + 0.75, y - 0.30, x, y - 0.30, arrow=4, width_pt=1.0)
        u.label(x + 0.95, y - 0.40, 1.5, 0.22, text, size=7.8, align=0)

    y = 6.95
    msg(xs["user"], xs["ui"], y, "1  enter name or author")
    y -= 0.75
    msg(xs["ui"], xs["ctrl"], y, "2  get details")
    y -= 0.75
    msg(xs["ctrl"], xs["ent"], y, "3  search details")
    y -= 0.75
    msg(xs["ent"], xs["ctrl"], y, "4  result", dashed=True, arrow=4)
    y -= 0.75
    msg(xs["ctrl"], xs["ui"], y, "5  show result", dashed=True, arrow=4)

    # activation bars on the control lifeline
    for yy in (6.95, 6.20, 5.45, 4.70, 3.95):
        pass
    u.box(xs["ctrl"] - 0.05, 3.70, xs["ctrl"] + 0.05, 7.20,
          line="RGB(40,60,100)", fill="RGB(230,235,245)")
    u.box(xs["ent"] - 0.05, 4.70, xs["ent"] + 0.05, 5.70,
          line="RGB(40,60,100)", fill="RGB(230,235,245)")

    u.label(6.2, 8.25, 11.5, 0.5,
            "Sequence Diagram  /  Issue Book and Query Book  /  Library System",
            size=13, bold=1)

    u.save(out_vsdx)
    u.export(out_png)
    u.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--png", required=True)
    a = ap.parse_args()
    if a.kind == "usecase":
        use_case_diagram(a.out, a.png)
    elif a.kind == "class":
        class_diagram(a.out, a.png)
    elif a.kind == "sequence":
        sequence_diagram(a.out, a.png)
    else:
        raise SystemExit(f"unknown kind {a.kind}")
    print("OK", a.out, os.path.getsize(a.out), "|", a.png,
          os.path.getsize(a.png) if os.path.exists(a.png) else "NO-PNG")
