# -*- coding: utf-8 -*-
"""Generate SVG diagrams for the Cyber Security Week 01 note (English-only, DM style)."""
import os
OUT = r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\06_Diagrams_&_Mindmaps"
os.makedirs(OUT, exist_ok=True)

INK="#1a202c"; GRID="#cbd5e0"; EDGE="#4a5568"
BLUE="#2b6cb0"; GREEN="#2f855a"; RED="#c53030"
ORANGE="#dd6b20"; PURPLE="#6b46c1"; NODE="#bee3f8"
GREY="#718096"; LBLUE="#ebf8ff"; CARD="#f7fafc"

def esc(s): return s.replace("&","&amp;")
def svg(h, body, title=None):
    t = f'<text x="24" y="30" font-family="Segoe UI, Arial" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>' if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {h}" font-family="Segoe UI, Arial">'
            f'<rect x="0" y="0" width="680" height="{h}" fill="#ffffff"/>{t}{body}</svg>')
def rrect(x,y,w,h,fill,stroke=INK,sw=1.5,rx=8,txt="",ts=14,tc=INK,tw="600"):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if txt: s+=f'<text x="{x+w/2}" y="{y+h/2+ts/3}" text-anchor="middle" font-size="{ts}" font-weight="{tw}" fill="{tc}">{esc(txt)}</text>'
    return s
def txt(x,y,s,size=12,fill=INK,anchor="start",weight="normal"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(s)}</text>'
HEAD='<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#4a5568"/></marker></defs>'

diagrams={}

# 1) CIA triad
def pillar(x,color,name,techs):
    s=rrect(x,60,196,166,CARD,stroke=color,sw=2,rx=10)
    s+=txt(x+98,90,name,14,color,"middle","700")
    y=126
    for t in techs:
        s+=txt(x+16,y,"• "+t,11.5,INK,"start")
        y+=24
    return s
body=(pillar(30,BLUE,"Confidentiality",["encryption","access controls","VPNs"])
      +pillar(242,GREEN,"Integrity",["hashing (SHA-256)","digital signatures","version control"])
      +pillar(454,ORANGE,"Availability",["redundancy","load balancing","DDoS mitigation"]))
diagrams["cy_w1_cia_triad.svg"]=svg(248,body,title="The CIA Triad — three pillars + techniques")

# 2) Attack surface
body=(rrect(40,64,180,66,LBLUE,txt="E — exposed points",ts=12)
      +txt(130,118,"open ports, APIs",11,GREY,"middle")
      +txt(232,102,"×",22,INK,"middle","700")
      +rrect(252,64,180,66,LBLUE,txt="V — severity",ts=12)
      +txt(342,118,"CVSS 0–10",11,GREY,"middle")
      +txt(444,102,"×",22,INK,"middle","700")
      +rrect(464,64,176,66,LBLUE,txt="A — asset value",ts=12)
      +txt(552,118,"how important",11,GREY,"middle")
      +txt(340,172,"AS = Σ ( E × V × A )",16,INK,"middle","700")
      +txt(340,204,"any factor = 0  →  AS = 0",12.5,RED,"middle","700")
      +txt(340,228,"fewer entry points is the cheapest fix",11.5,GREY,"middle"))
diagrams["cy_w1_attack_surface.svg"]=svg(252,body,title="Attack Surface — why multiply, not add")

# 3) Threat landscape
def tbox(x,y,w,name,desc,color):
    return (rrect(x,y,w,64,CARD,stroke=color,sw=1.8)
            +txt(x+w/2,y+26,name,12.5,color,"middle","700")
            +txt(x+w/2,y+46,desc,10.5,GREY,"middle"))
body=(tbox(30,64,196,"Malware","viruses · worms · trojans",RED)
      +tbox(242,64,196,"Phishing","social engineering",ORANGE)
      +tbox(454,64,196,"Insider","misuse of access",PURPLE)
      +tbox(136,150,196,"APT","state-sponsored, stealthy",BLUE)
      +tbox(348,150,196,"IoT attacks","botnets — e.g. Mirai",GREEN))
diagrams["cy_w1_threat_landscape.svg"]=svg(238,body,title="Threat Landscape — five vectors")

for name,content in diagrams.items():
    with open(os.path.join(OUT,name),"w",encoding="utf-8") as f: f.write(content)
    print("wrote", name, len(content), "bytes")
print("TOTAL:", len(diagrams))
