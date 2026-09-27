# -*- coding: utf-8 -*-
"""SVG diagrams for the Cyber Security Week 02 (Risk) note. English-only, DM style."""
import os
OUT = r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\06_Diagrams_&_Mindmaps"
os.makedirs(OUT, exist_ok=True)
INK="#1a202c"; EDGE="#4a5568"; BLUE="#2b6cb0"; GREEN="#2f855a"; RED="#c53030"
ORANGE="#dd6b20"; PURPLE="#6b46c1"; GREY="#718096"; LBLUE="#ebf8ff"; CARD="#f7fafc"

def esc(s): return s.replace("&","&amp;")
def svg(h, body, title=None):
    t=f'<text x="24" y="30" font-family="Segoe UI, Arial" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>' if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {h}" font-family="Segoe UI, Arial">'
            f'<rect x="0" y="0" width="680" height="{h}" fill="#ffffff"/>{t}{body}</svg>')
def rrect(x,y,w,h,fill,stroke=INK,sw=1.6,rx=8,txt="",ts=13,tc=INK,tw="700"):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if txt: s+=f'<text x="{x+w/2}" y="{y+h/2+ts/3}" text-anchor="middle" font-size="{ts}" font-weight="{tw}" fill="{tc}">{esc(txt)}</text>'
    return s
def txt(x,y,s,size=12,fill=INK,anchor="start",weight="normal"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(s)}</text>'
def arrow(x1,y1,x2,y2,stroke=EDGE,sw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" marker-end="url(#ah)"/>'
HEAD='<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#4a5568"/></marker></defs>'
diagrams={}

# 1) Risk chain + equations
body=(rrect(40,64,180,58,LBLUE,txt="Threat (F)")
      +arrow(222,93,250,93)
      +rrect(252,64,176,58,LBLUE,txt="Vulnerability")
      +arrow(430,93,458,93)
      +rrect(460,64,180,58,CARD,stroke=RED,txt="Damage",tc=RED)
      +txt(340,158,"Basic risk   S = F × K",15,INK,"middle","700")
      +txt(340,182,"(F = frequency of attempts, K = consequences)",11,GREY,"middle")
      +txt(340,214,"Residual risk   R = S / M",15,INK,"middle","700")
      +txt(340,238,"(M = number of countermeasures × effectiveness)",11,GREY,"middle"))
diagrams["cy_w2_risk_flow.svg"]=svg(262,body,title="Risk chain + the two equations")

# 2) Four threat groups
def gbox(x,y,name,desc,color):
    return (rrect(x,y,296,62,CARD,stroke=color,sw=1.8)
            +txt(x+16,y+27,name,12.5,color,"start","700")
            +txt(x+16,y+47,desc,10.5,GREY,"start"))
body=(gbox(30,60,"Hardware","storms · theft · infra faults",RED)
      +gbox(354,60,"Software","malware · bugs · outdated versions",BLUE)
      +gbox(30,134,"Data","unwanted disclosure · inference",ORANGE)
      +gbox(354,134,"Liveware","social engineering · phishing",PURPLE))
diagrams["cy_w2_threat_groups.svg"]=svg(212,body,title="Four threat groups in IT systems")

# 3) PDCA
def pbox(x,label,desc,color):
    return (rrect(x,64,148,92,CARD,stroke=color,sw=1.8)
            +txt(x+74,92,label,14,color,"middle","700")
            +txt(x+74,116,desc,10,INK,"middle")
            +txt(x+74,134,"",10))
body=(pbox(30,"Plan","identify threats,\nanalyse risks","") if False else
      rrect(30,64,148,92,CARD,stroke=BLUE,sw=1.8)+txt(104,92,"Plan",14,BLUE,"middle","700")+txt(104,116,"identify threats",10,INK,"middle")+txt(104,132,"analyse risks",10,INK,"middle")
      +arrow(180,110,206,110)
      +rrect(208,64,148,92,CARD,stroke=GREEN,sw=1.8)+txt(282,92,"Do",14,GREEN,"middle","700")+txt(282,116,"implement",10,INK,"middle")+txt(282,132,"countermeasures",10,INK,"middle")
      +arrow(358,110,384,110)
      +rrect(386,64,148,92,CARD,stroke=ORANGE,sw=1.8)+txt(460,92,"Check",14,ORANGE,"middle","700")+txt(460,116,"monitor the",10,INK,"middle")+txt(460,132,"solution",10,INK,"middle")
      +arrow(460,158,460,184)
      +rrect(386,186,148,86,CARD,stroke=PURPLE,sw=1.8)+txt(460,212,"Act",14,PURPLE,"middle","700")+txt(460,236,"adjust or restart",10,INK,"middle")+txt(460,252,"a new Plan",10,INK,"middle")
      +arrow(384,229,206,229)+arrow(206,229,104,229)+arrow(104,229,104,158))
diagrams["cy_w2_pdca.svg"]=svg(292,body,title="Risk management as a PDCA process")

# 4) Authentication factors
body=(rrect(40,64,290,58,LBLUE,txt="Knowledge — something you know")
      +rrect(350,64,290,58,LBLUE,txt="Possession — something you have")
      +rrect(40,140,290,58,LBLUE,txt="Inherence — something you are")
      +rrect(350,140,290,58,LBLUE,txt="Location — somewhere you are")
      +txt(340,224,"authorization is based on authentication",11.5,GREY,"middle"))
diagrams["cy_w2_auth_factors.svg"]=svg(244,body,title="Four authentication factors")

for name,c in diagrams.items():
    open(os.path.join(OUT,name),"w",encoding="utf-8").write(c)
    print("wrote",name)
print("TOTAL:",len(diagrams))
