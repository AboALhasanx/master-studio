# -*- coding: utf-8 -*-
"""Generate SVG diagrams for the Data Mining W02/W03 deep-dive reading.
Outputs into 06_Diagrams_&_Mindmaps/03_Data_Mining/."""
import os

OUT = r"C:\Users\gokoq\Master-Studio\01_Semester_1\03_Data_Mining\06_Diagrams_&_Mindmaps\03_Data_Mining"
os.makedirs(OUT, exist_ok=True)

INK = "#1a202c"; GRID = "#cbd5e0"; EDGE = "#4a5568"
BLUE = "#2b6cb0"; GREEN = "#2f855a"; RED = "#c53030"
ORANGE = "#dd6b20"; PURPLE = "#6b46c1"; NODE = "#bee3f8"
GREY = "#718096"; YEL = "#ecc94b"; LBLUE = "#ebf8ff"

def esc(s):
    return s.replace("&", "&amp;")

def svg(w, h, body, title=None):
    t = ""
    if title:
        t = f'<text x="24" y="30" font-family="Segoe UI, Arial" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {h}" '
            f'font-family="Segoe UI, Arial">'
            f'<rect x="0" y="0" width="680" height="{h}" fill="#ffffff"/>{t}{body}</svg>')

def rrect(x, y, w, h, fill, stroke=INK, sw=1.5, rx=8, txt="", ts=14, tc=INK, tw="600"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if txt:
        s += f'<text x="{x+w/2}" y="{y+h/2+ts/3}" text-anchor="middle" font-size="{ts}" font-weight="{tw}" fill="{tc}">{esc(txt)}</text>'
    return s

def txt(x, y, s, size=13, fill=INK, anchor="start", weight="normal"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(s)}</text>'

def vtext(x, y, lines, ts=12, tc=INK, tw="600"):
    """Centered multi-line text block; lines is a list of strings."""
    s = ""
    n = len(lines)
    if n == 1:
        return txt(x, y + ts*0.35, lines[0], ts, tc, "middle", tw)
    gap = ts * 1.2
    top = y - gap*(n-1)/2
    for i, ln in enumerate(lines):
        s += txt(x, top + i*gap + ts*0.35, ln, ts, tc, "middle", tw)
    return s

def line(x1, y1, x2, y2, stroke=EDGE, sw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'

def poly(pts, stroke=EDGE, sw=2, fill="none"):
    d = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def circ(cx, cy, r, fill=NODE, stroke=EDGE, sw=2, label="", ts=13):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if label:
        s += f'<text x="{cx}" y="{cy+ts/3}" text-anchor="middle" font-size="{ts}" font-weight="700" fill="{INK}">{label}</text>'
    return s

def arrow(x1, y1, x2, y2, stroke=EDGE, sw=2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" '
            f'marker-end="url(#ah)"/>')

HEAD = '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{c}"/></marker></defs>'.replace("{c}", EDGE)

diagrams = {}

# 1. Quantitative Multidimensional
pts = [(120,200),(180,150),(150,120),(240,180),(300,100),(360,160),(280,210),(420,130),(200,90),(470,190)]
sc = "".join(circ(x,y,6,fill=BLUE,stroke=BLUE,sw=1.5) for x,y in pts)
diagrams["dt_quantitative.svg"] = svg(680,300,
    HEAD +
    line(70,250,620,250,GRID,1.5) + line(70,250,70,60,GRID,1.5) +
    txt(560,245,"features →",11,GREY,"start") + txt(40,70,"value ↑",11,GREY) +
    sc +
    arrow(70,250,300,120,BLUE,2.5) +
    txt(150,110,"feature vector",12,BLUE,"middle",700) +
    txt(120,285,"Example: Age=25, BP=80, Chol=190, BMI=22  →  [25,80,190,22]",12,INK,"middle",600),
    title="Quantitative Multidimensional — numeric vector")

# 2. Categorical & Mixed
chips = (rrect(40,70,110,40,RED,txt="Red",tc="#fff") + rrect(165,70,110,40,GREEN,txt="Green",tc="#fff")
         + rrect(290,70,110,40,BLUE,txt="Blue",tc="#fff"))
card = (rrect(150,150,380,110,LBLUE,sw=2) +
        txt(170,185,"Mixed record:",13,INK,"start",700) +
        txt(170,212,"Age = 21   (numeric)",12,INK) +
        txt(170,234,"Gender = Male   (category)",12,INK) +
        txt(360,212,"GPA = 3.4   (numeric)",12,INK) +
        txt(360,234,"Major = CS   (category)",12,INK))
diagrams["dt_categorical.svg"] = svg(680,300, chips + card,
    title="Categorical & Mixed — labels + numbers")

# 3. Binary & Set
grid = ""
hdr = ["Smoker","Loan","Fraud"]
data = [["1","0","0"],["0","1","1"],["1","0","1"],["0","0","0"]]
gx, gy = 60, 110
for c,htxt in enumerate(hdr):
    grid += txt(gx+c*70+25, gy-8, htxt, 11, GREY, "middle")
for r,row in enumerate(data):
    for c,val in enumerate(row):
        fillc = GREEN if val=="1" else "#f7fafc"
        grid += rrect(gx+c*70, gy+r*42, 60, 34, fillc, sw=1.5, txt=val, ts=14)
basket = (rrect(430,120,180,150,"#fff",stroke=ORANGE,sw=2) +
          txt(520,145,"Market Basket",12,ORANGE,"middle",700) +
          txt(455,180,"• Milk",13,INK) + txt(455,210,"• Bread",13,INK) + txt(455,240,"• Eggs",13,INK))
diagrams["dt_binary_set.svg"] = svg(680,300, grid + basket,
    title="Binary & Set — 0/1 matrix + item set")

# 4. Text
doc = (rrect(60,70,150,170,"#fff",stroke=EDGE,sw=2) +
       txt(80,100,"Email:",12,INK,700) +
       line(80,118,190,118,GRID,1) + line(80,134,190,134,GRID,1) +
       line(80,150,170,150,GRID,1) + line(80,166,190,166,GRID,1) +
       line(80,182,160,182,GRID,1) + line(80,198,185,198,GRID,1))
bag = (rrect(330,110,300,140,"#fff",stroke=PURPLE,sw=2) +
       txt(480,140,"Convert to numbers:",13,PURPLE,"middle",700) +
       rrect(350,160,90,30,LBLUE,txt="BoW",ts=12) +
       rrect(450,160,90,30,LBLUE,txt="TF-IDF",ts=12) +
       rrect(350,205,150,30,LBLUE,txt="word embeddings",ts=12))
diagrams["dt_text.svg"] = svg(680,300, doc + bag + arrow(210,150,330,170,PURPLE,2.5),
    title="Text — unstructured → numeric vector")

# 5. Time-Series
ts = [(90,210),(150,150),(210,180),(270,110),(330,160),(390,90),(450,200),(510,130),(570,170)]
diagrams["dt_timeseries.svg"] = svg(680,300,
    HEAD + line(70,250,620,250,GRID,1.5) + line(70,250,70,60,GRID,1.5) +
    txt(560,245,"time →",11,GREY) + txt(40,70,"value ↑",11,GREY) +
    poly(ts, BLUE, 2.5) +
    "".join(circ(x,y,4,fill=BLUE,stroke=BLUE,sw=1) for x,y in ts) +
    txt(120,285,"Example: stock price / ECG signal / temperature",12,INK,"middle",600),
    title="Time-Series — values across time")

# 6. Discrete Sequences
tiles = ""
seq = ["A","T","C","G","A","C","G"]
for i,s in enumerate(seq):
    tiles += rrect(40+i*70,90,60,46, NODE if i%2 else LBLUE, txt=s, ts=18)
flow = (rrect(60,200,90,40,"#fff",txt="Home") + arrow(150,220,180,220,EDGE,2) +
        rrect(180,200,100,40,"#fff",txt="Search") + arrow(280,220,310,220,EDGE,2) +
        rrect(310,200,110,40,"#fff",txt="Product") + arrow(420,220,450,220,EDGE,2) +
        rrect(450,200,100,40,"#fff",txt="Cart"))
diagrams["dt_sequence.svg"] = svg(680,300, tiles + flow,
    title="Discrete Sequence — ordered symbols")

# 7. Spatial
gridlines = ""
for i in range(6):
    gridlines += line(120+i*70,80,120+i*70,260,GRID,1) + line(120,80+i*36,470,80+i*36,GRID,1)
pts2 = [(200,120),(340,100),(420,200),(260,230)]
sc2 = "".join(circ(x,y,7,fill=ORANGE,stroke=ORANGE,sw=1.5) for x,y in pts2)
pin = (txt(560,120,"lat/long",12,GREY,"middle",600) + txt(560,140,"32.50, 45.82",12,INK,"middle",700))
diagrams["dt_spatial.svg"] = svg(680,300, gridlines + sc2 + pin,
    title="Spatial — coordinates on a grid")

# 8. Graph
n = {"A":(250,110),"B":(430,110),"C":(250,230),"D":(430,230)}
e = line(250,110,430,110)+line(250,230,430,230)+line(250,110,250,230)+line(430,110,430,230)+line(250,110,430,230)
nd = "".join(circ(v[0],v[1],28,label=k,ts=15) for k,v in n.items())
diagrams["dt_graph.svg"] = svg(680,300, e+nd + txt(120,170,"nodes =",13,INK,"start",700)+txt(120,195,"objects",12,GREY)+txt(120,225,"edges =",13,INK,"start",700)+txt(120,250,"links",12,GREY),
    title="Network & Graph — nodes + edges")

# 9. Pipeline
steps = [("Collect",""),("Clean",""),("Integrate",""),("Transform",""),
         ("Feature","Extract"),("Reduce",""),("Split","")]
bw, bh, x0, pitch, y = 82, 56, 14, 94, 100
pb = ""
for i,(a,b) in enumerate(steps):
    pb += rrect(x0+i*pitch, y, bw, bh, LBLUE, sw=2)
    pb += vtext(x0+i*pitch+bw/2, y+bh/2, [a] if b=="" else [a,b], ts=11)
    if i < len(steps)-1:
        pb += arrow(x0+i*pitch+bw, y+bh/2, x0+(i+1)*pitch, y+bh/2, EDGE, 2)
diagrams["op_pipeline.svg"] = svg(680,210, pb + txt(18,200,"Data Preparation pipeline (6–7 steps before modeling)",12,INK,"start",600),
    title="Data Preparation")

# 10. Discretization
ax = 60; bw4 = 120; axis_end = ax + 4*bw4   # 60..540, four EQUAL bands
bandrects = (rrect(ax+0*bw4,150,bw4,34,RED) + rrect(ax+1*bw4,150,bw4,34,ORANGE)
             + rrect(ax+2*bw4,150,bw4,34,GREEN) + rrect(ax+3*bw4,150,bw4,34,BLUE))
labels = (txt(ax+0*bw4+bw4/2,200,"Teen",12,RED,"middle",700)
          + txt(ax+1*bw4+bw4/2,200,"Young",12,ORANGE,"middle",700)
          + txt(ax+2*bw4+bw4/2,200,"Middle",12,GREEN,"middle",700)
          + txt(ax+3*bw4+bw4/2,200,"Senior",12,BLUE,"middle",700))
rangelbl = (txt(ax+0*bw4+bw4/2,130,"0–20",11,GREY,"middle")+txt(ax+1*bw4+bw4/2,130,"21–40",11,GREY,"middle")
            +txt(ax+2*bw4+bw4/2,130,"41–60",11,GREY,"middle")+txt(ax+3*bw4+bw4/2,130,"61–80",11,GREY,"middle"))
ar = (arrow(250,108,250,148,INK,2) + txt(250,100,"25 → Young",12,INK,"middle",700)
      + arrow(490,84,490,148,INK,2) + txt(490,76,"67 → Senior",12,INK,"middle",700))
diagrams["op_discretization.svg"] = svg(680,240,
    txt(60,50,"Numeric → Categorical (Discretization)",13,INK,"start",700) + bandrects + labels + rangelbl + ar,
    title="Discretization")

# 11. One-Hot
colc = [RED, BLUE, GREEN]
oh = (txt(40,70,"Categories:",13,INK,"start",700)
      + txt(40,112,"Red",13,RED,"start",700) + txt(40,152,"Blue",13,BLUE,"start",700) + txt(40,192,"Green",13,GREEN,"start",700))
mx, my, mw, mh = 320, 80, 300, 140           # matrix outer border (x 320..620, y 80..220)
m = rrect(mx, my, mw, mh, "#fff", stroke=EDGE, sw=2)
ch = "".join(txt(mx+60+c*80+40, my+14, nm, 12, colc[c], "middle", 700) for c, nm in enumerate(["Red","Blue","Green"]))
rl = "".join(txt(mx+30, my+44+r*32+16, nm, 12, INK, "middle", 700) for r, nm in enumerate(["Red","Blue","Green"]))
cells = ""
for r in range(3):
    for c in range(3):
        val = "1" if r==c else "0"
        cx = mx+60+c*80+40
        cy = my+44+r*32+16
        if val=="1":
            cells += rrect(mx+60+c*80, my+44+r*32, 80, 32, LBLUE, sw=1)
        cells += txt(cx, cy, val, 13, INK if val=="1" else GREY, "middle", "700" if val=="1" else "normal")
diagrams["op_onehot.svg"] = svg(680,260, oh + arrow(180,150,mx,150,EDGE,2.5) + m + ch + rl + cells,
    title="One-Hot Encoding (Categorical → Numeric)")

# 12. TF-IDF
# term-doc matrix: rows the, cat, dog ; cols Doc1, Doc2
mtx = rrect(250,80,260,150,"#fff",stroke=EDGE,sw=2)
cells = (txt(330,105,"Doc1",12,INK,"middle",700)+txt(440,105,"Doc2",12,INK,"middle",700)
         + txt(265,140,"the",12,INK)+txt(330,140,"0.10",13,GREY,"middle")+txt(440,140,"0.08",13,GREY,"middle")
         + txt(265,175,"cat",12,INK)+rrect(305,160,55,28,GREEN,txt="0.91",ts=13,tc="#fff")+rrect(415,160,55,28,GREEN,txt="0.05",ts=13,tc="#fff")
         + txt(265,210,"dog",12,INK)+rrect(305,195,55,28,ORANGE,txt="0.04",ts=13,tc="#fff")+rrect(415,195,55,28,ORANGE,txt="0.88",ts=13,tc="#fff"))
note = txt(530,130,"rare word",12,GREEN,"middle",700)+txt(530,150,"→ HIGH",12,GREEN,"middle",700)+txt(530,185,"common word",12,GREY,"middle")+txt(530,205,"→ LOW",12,GREY,"middle")
diagrams["op_tfidf.svg"] = svg(680,260, mtx+cells+note+txt(30,120,"TF-IDF",14,PURPLE,"start",700)+txt(30,145,"weights",13,GREY),
    title="TF-IDF (Text → Numeric)")

# 13. Time-Series -> Sequence
# 3 bands + symbols
bands2 = rrect(80,170,180,30,RED)+rrect(260,170,180,30,ORANGE)+rrect(440,170,140,30,GREEN)
bl = txt(170,200,"Low",12,RED,"middle",700)+txt(350,200,"Med",12,ORANGE,"middle",700)+txt(510,200,"High",12,GREEN,"middle",700)
ts2 = [(90,150),(160,140),(230,145),(300,130),(370,120),(440,115),(510,108)]
ln = poly(ts2,BLUE,2.5)
sym = txt(170,90,"A",16,INK,"middle",700)+txt(280,90,"A",16,INK,"middle",700)+txt(360,70,"B",16,INK,"middle",700)+txt(470,55,"C",16,INK,"middle",700)
diagrams["op_ts_sequence.svg"] = svg(680,260, bands2+bl+ln+sym+txt(30,40,"Time-Series → Symbolic Sequence (SAX)",13,INK,"start",700),
    title="Time-Series → Sequence")

# 14. Similarity Graph (5 patients)
pos = {"P1":(200,110),"P2":(320,90),"P3":(230,220),"P4":(350,210),"P5":(520,160)}
edges = [("P1","P2"),("P2","P4"),("P4","P3"),("P3","P1")]
ge = "".join(line(pos[a][0],pos[a][1],pos[b][0],pos[b][1],EDGE,2.5) for a,b in edges)
gn = "".join(circ(v[0],v[1],30,label=k,ts=15) for k,v in pos.items())
isol = circ(520,160,30,fill="#fff",stroke=RED,sw=2.5,label="P5",ts=15)
out = txt(520,215,"P5 = outlier",12,RED,"middle",700)
diagrams["op_similarity_graph.svg"] = svg(680,300, ge+gn+isol+out+txt(30,40,"Converting Data INTO a Graph — Similarity Graph",13,INK,"start",700),
    title="Similarity Graph")

# 15. Graph Embedding
g = line(250,110,330,110)+line(250,200,330,200)+line(250,110,250,200)+line(330,110,330,200)+circ(250,110,26,label="A",ts=13)+circ(330,110,26,label="B",ts=13)+circ(250,200,26,label="C",ts=13)+circ(330,200,26,label="D",ts=13)
vec = rrect(470,120,170,90,LBLUE,sw=2,txt="[0.21, 0.75,",ts=13)+txt(555,200," 0.43]",13,INK,"middle",700)
diagrams["op_graph_embedding.svg"] = svg(680,260, g+arrow(360,155,470,165,EDGE,2.5)+vec+txt(30,40,"Graph → Numeric (Graph Embedding)",13,INK,"start",700),
    title="Graph Embedding")

# 16. Scaling
raw = [(120,220),(180,120),(240,200),(300,90)]
mm = [(120,200),(180,120),(240,170),(300,90)]
zs = [(150,150),(210,120),(270,180),(330,130)]
def plot(ox,oy,pts,c,lab):
    s=line(ox,oy,ox+200,oy,GRID,1.5)+line(ox,oy,ox,oy-150,GRID,1.5)
    s+="".join(circ(ox+px,oy-py,5,fill=c,stroke=c,sw=1) for px,py in pts)
    s+=txt(ox+60,oy+20,lab,11,GREY,"middle")
    return s
diagrams["op_scaling.svg"] = svg(680,260,
    plot(60,210,raw,BLUE,"raw (wide)") + plot(280,210,mm,GREEN,"min-max [0,1]") + plot(500,210,zs,ORANGE,"z-score μ=0"),
    title="Scaling — Min-Max vs Z-Score")

for name, content in diagrams.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
print("wrote", len(diagrams), "diagrams to", OUT)
for n in diagrams:
    print(" -", n)
