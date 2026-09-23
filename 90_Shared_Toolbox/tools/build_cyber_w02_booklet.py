# -*- coding: utf-8 -*-
"""Build the Cyber Security Week 02 "Risk" booklet (English only, HTML -> PDF).

Sources merged:
  1. Sharp, R., "Risk", Introduction to Cybersecurity, Springer, 2023, pp. 37-56
  2. An unidentified second source (physical security / authentication / NIST)

Figures are the book's own, cropped from the typeset PDF into
01_Semester_1/01_Cyber_Security/06_Diagrams_&_Mindmaps/from_sharp_ch3/.

NOTE ON ESCAPING: this builder deliberately contains NO backslash escape
sequences. All symbols are Unicode (x, divide, arrow, phi). That is the lesson
learned from the Soft Computing booklet, where Python ate the LaTeX backslashes.
"""
from pathlib import Path
import base64
import re
import html as _html

OUT = Path(r"G:\My Drive\Master-Studio\01_Semester_1\01_Cyber_Security\03_Study_Notes")
FIGDIR = Path(r"G:\My Drive\Master-Studio\01_Semester_1\01_Cyber_Security\06_Diagrams_&_Mindmaps\from_sharp_ch3")
HTML_OUT = OUT / "Week_02_Risk_Booklet.html"


def fig(name, alt):
    """Inline a figure as base64 so the HTML is fully self-contained.

    `name` may be given with or without the .png extension.
    """
    p = FIGDIR / name
    if not p.is_file():
        p = FIGDIR / (name + ".png")
    if not p.is_file():
        return f'<div class="figmiss">[missing figure: {name}]</div>'
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    return f'<img src="data:image/png;base64,{b64}" alt="{alt}"/>'


CSS = """
@page { size: A4; margin: 17mm 16mm 16mm; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; }
body {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  color:#1d2733; font-size:10.4pt; line-height:1.55; background:#fff;
  -webkit-font-smoothing: antialiased;
}
.page { padding-bottom: 5mm; }
.pbreak { page-break-before: always; }
.nobrk { page-break-inside: avoid; }

/* ---------- cover ---------- */
.cover { padding-top: 42mm; text-align:left; }
.cover .eyebrow { font-size:9pt; letter-spacing:.20em; text-transform:uppercase; color:#7b8794; }
.cover h1 { font-size:31pt; line-height:1.12; margin:6mm 0 0; color:#12293f; font-weight:650; letter-spacing:-0.4pt; }
.cover .rule { width:56mm; height:3px; background:#1f6f8b; margin:7mm 0; }
.cover .sub { font-size:12.5pt; color:#41566b; margin:0 0 3mm; }
.cover .meta { margin-top:16mm; font-size:10pt; color:#41566b; line-height:1.85; }
.cover .meta b { color:#12293f; font-weight:600; }
.cover .foot-note { margin-top:18mm; font-size:8.6pt; color:#8a95a1; line-height:1.6; border-top:1px solid #e3e8ee; padding-top:4mm; }

/* ---------- headings ---------- */
h1.sec {
  font-size:17pt; color:#12293f; font-weight:650; margin:0 0 5mm;
  padding-bottom:2.4mm; border-bottom:2.5px solid #1f6f8b; letter-spacing:-0.2pt;
}
h1.sec .num { color:#1f6f8b; margin-right:3mm; }
h2 { font-size:12.4pt; color:#173a56; margin:6mm 0 2mm; font-weight:640; }
h2:first-of-type { margin-top:1mm; }
h3 { font-size:10.6pt; color:#1f6f8b; margin:4.5mm 0 1.5mm; font-weight:640; }
p { margin:0 0 2.6mm; }
ul, ol { margin:0 0 3mm 5.5mm; padding-left:4mm; }
li { margin-bottom:1.3mm; }
b, strong { font-weight:640; color:#12293f; }
code { font-family: "Consolas","SF Mono",monospace; font-size:9.6pt; background:#f2f5f8; padding:0.3mm 1mm; border-radius:1mm; }

/* ---------- contents ---------- */
.toc { margin-top:2mm; }
.toc-row { display:flex; align-items:baseline; gap:2mm; padding:1.5mm 0; border-bottom:1px dotted #dde3ea; }
.toc-row .n { width:13mm; color:#1f6f8b; font-weight:640; flex:none; }
.toc-row .t { flex:1; }
.toc-row .p { color:#8a95a1; font-size:9.4pt; }
.toc-sub { padding-left:15mm; font-size:9.6pt; color:#41566b; }
.toc-sub .n { width:11mm; }
.toc-group { font-size:9pt; letter-spacing:.10em; text-transform:uppercase; color:#1f6f8b;
             font-weight:640; margin:5mm 0 1.5mm; padding-bottom:1mm; border-bottom:1.5px solid #cfe0e8; }
.toc-group:first-child { margin-top:1mm; }

/* ---------- boxes ---------- */
.def { border-left:3.5px solid #1f6f8b; background:#f4f9fb; padding:3.2mm 4mm; margin:3mm 0 4mm; }
.def .tag { display:block; font-size:8.4pt; letter-spacing:.10em; text-transform:uppercase; color:#1f6f8b; margin-bottom:1.4mm; font-weight:640; }
.key { border:1px solid #cfe0e8; background:#fbfdfe; padding:3.2mm 4mm; margin:3mm 0 4mm; border-radius:1.5mm; }
.key .tag { display:block; font-size:8.4pt; letter-spacing:.10em; text-transform:uppercase; color:#1f6f8b; margin-bottom:1.6mm; font-weight:640; }
.trap { border-left:3.5px solid #b45309; background:#fffaf2; padding:2.8mm 4mm; margin:3mm 0; font-size:9.9pt; }
.trap .tag { display:block; font-size:8.4pt; letter-spacing:.10em; text-transform:uppercase; color:#9a4a06; margin-bottom:1.2mm; font-weight:640; }
.note { border-left:3.5px solid #8a95a1; background:#f7f8fa; padding:2.8mm 4mm; margin:3mm 0; font-size:9.5pt; color:#41566b; }
.note .tag { display:block; font-size:8.4pt; letter-spacing:.10em; text-transform:uppercase; color:#6b7683; margin-bottom:1.2mm; font-weight:640; }
.formula { text-align:center; font-size:15pt; color:#12293f; margin:4mm 0; padding:3.4mm; background:#f4f9fb; border-radius:1.5mm; font-weight:600; letter-spacing:.02em; }

/* ---------- tables ---------- */
table { width:100%; border-collapse:collapse; margin:3mm 0 4mm; font-size:9.5pt; }
th { background:#12293f; color:#fff; padding:2mm 2.4mm; text-align:left; font-weight:600; font-size:9.2pt; }
td { border:0.5pt solid #d5dde5; padding:1.9mm 2.4mm; vertical-align:top; }
tr:nth-child(even) td { background:#f8fafc; }
td.c, th.c { text-align:center; }

/* ---------- figures ---------- */
.figbox { margin:4mm 0 4.5mm; text-align:center; }
.figbox img { max-width:100%; height:auto; border:1px solid #e3e8ee; border-radius:1.5mm; }
.figbox.tall img { max-height:118mm; }
.figcap { font-size:8.8pt; color:#6b7683; margin-top:1.8mm; text-align:center; line-height:1.45; }
.figrow { display:flex; gap:5mm; align-items:flex-start; margin:4mm 0; }
.figrow > div { flex:1; text-align:center; }
.figrow img { max-width:100%; height:auto; border:1px solid #e3e8ee; border-radius:1.5mm; }
.figmiss { color:#b45309; font-size:9pt; padding:6mm; border:1px dashed #b45309; }
.anch { font-size:1pt; color:#ffffff; }

/* ---------- misc ---------- */
.two { display:flex; gap:6mm; }
.two > div { flex:1; }
.foot { display:none; }
.small { font-size:9.2pt; color:#5b6673; }
.tight li { margin-bottom:0.6mm; }
.lead { font-size:11pt; color:#41566b; margin-bottom:4mm; }
hr.soft { border:0; border-top:1px solid #e8edf2; margin:5mm 0; }
"""


# Sections that should start on a fresh printed page: the contents page, the
# opening of each major part, and the three closing reference sections.
PBREAK = {2, 5, 19, 27, 28, 29}


def page(num, title, body):
    """`title` carries the section key inside <span class="num">…</span>.

    An invisible anchor is emitted so the rendered PDF can be searched for the
    exact heading position — plain-text search is unreliable because the same
    words appear in the contents and in cross-references.
    """
    cls = "page pbreak" if num in PBREAK else "page"
    mk = re.search(r'<span class="num">([^<]+)</span>', title)
    key = mk.group(1) if mk else str(num)
    return (f'<section class="{cls}"><h1 class="sec">'
            f'<span class="anch">@@{key}@@</span>{title}</h1>{body}</section>')


# ----------------------------------------------------------------------------
# FRONT MATTER
# ----------------------------------------------------------------------------

COVER = f"""
<section class="page cover">
  <div class="eyebrow">Master Studio · Cyber Security</div>
  <h1>Cybersecurity Risks<br/>and Threats</h1>
  <div class="rule"></div>
  <p class="sub">Week 02 · Booklet 2 · Study Booklet</p>
  <div class="meta">
    <b>Course</b>&nbsp;&nbsp;01_Cyber_Security (CS502)<br/>
    <b>Instructor</b>&nbsp;&nbsp;Asst. Prof. Dr. Huda Lafta Majeed<br/>
    <b>Primary source</b>&nbsp;&nbsp;Robin Sharp, <i>Introduction to Cybersecurity: A Multidisciplinary Challenge</i>,<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Springer, Cham, 2023 — Chapter 3 &ldquo;Risk&rdquo;, pp. 37–56<br/>
    <b>DOI</b>&nbsp;&nbsp;10.1007/978-3-031-41463-3_3
  </div>
  <div class="foot-note">
    Built from the original textbook and from the doctor's own marking of the delivered
    booklet. Every section is tagged with the source it came from. Where the material is
    known to be inaccurate, the correct fact is stated alongside.<br/><br/>
    Figure 3.1 photograph: Terry Goss, Wikimedia Commons, <i>White_shark.jpg</i>, CC-BY 2.5 Generic.
  </div>
</section>
"""

# Contents structure: (group label or None, [(key, label, search text)])
TOC_GROUPS = [
    (None, [
        ("1", "How to use this booklet", "How to use this booklet"),
        ("2", "What the doctor marked as important", "What the doctor marked as important"),
    ]),
    ("3 &nbsp;&middot;&nbsp; Risk, the core idea", [
        ("3.1", "What is risk? Objective and subjective", "What is risk? Objective and subjective"),
        ("3.2", "Threat, vulnerability and damage", "Threat, vulnerability and damage"),
        ("3.3", "Basic risk: S = F &times; K, and the risk matrix", "Basic risk: S = F"),
        ("3.4", "Countermeasures and residual risk: R = S / M", "Countermeasures and residual risk: R = S"),
        ("3.5", "The three-point scale", "The three-point scale"),
        ("3.6", "Threats in IT systems &mdash; the four groups", "Threats in IT systems"),
        ("3.7", "Countermeasures matched to threats", "Countermeasures matched to threats"),
        ("3.8", "The five steps for dealing with damage", "The five steps for dealing with damage"),
        ("3.9", "Risk management and the five strategies", "Risk management and the five strategies"),
        ("3.10", "Systematic security analysis &mdash; five frameworks", "Systematic security analysis"),
        ("3.11", "ISO/IEC 27002 and the ISO 27000 series", "ISO/IEC 27002 and the ISO 27000 series"),
        ("3.12", "OCTAVE", "OCTAVE"),
        ("3.13", "PDCA", "PDCA"),
        ("3.14", "Worked examples", "Worked examples"),
    ]),
    ("4 &nbsp;&middot;&nbsp; Physical security and authentication", [
        ("4.1", "Security policy and access control", "Security policy and access control"),
        ("4.2", "Locks, deadbolts and cipher locks", "Locks, deadbolts and cipher locks"),
        ("4.3", "Gates and control relays", "Gates and control relays"),
        ("4.4", "Authentication systems and the four factors", "Authentication systems and the four factors"),
        ("4.5", "Authentication technologies", "Authentication technologies"),
        ("4.6", "Remote monitoring and automated access control", "Remote monitoring and automated access control"),
        ("4.7", "The NIST material", "The NIST material"),
        ("4.8", "Cyber risk assessment and management", "Cyber risk assessment and management"),
    ]),
    (None, [
        ("5", "Exam traps and formula card", "Exam traps and formula card"),
        ("6", "Glossary", "Glossary"),
        ("7", "Sources and verification notes", "Sources and verification notes"),
    ]),
]

# Flat list used to locate each heading in the rendered PDF.
TOC_LOOKUP = [(k, s) for _g, items in TOC_GROUPS for (k, _l, s) in items]


def toc_html(pm):
    """pm: dict key -> page number (int) or None."""
    out = ['<section class="page pbreak"><h1 class="sec">Contents</h1><div class="toc">']
    for group, items in TOC_GROUPS:
        if group:
            out.append(f'<div class="toc-group">{group}</div>')
        for key, label, _s in items:
            p = pm.get(key)
            num = str(p) if p else "&mdash;"
            sub = " toc-sub" if key.count(".") else ""
            out.append(
                f'<div class="toc-row{sub}"><span class="n">{key}</span>'
                f'<span class="t">{label}</span><span class="p">{num}</span></div>'
            )
    out.append('</div><p class="small" style="margin-top:6mm">Page numbers refer to the printed '
               'page shown at the foot of each page.</p></section>')
    return "\n".join(out)


# ----------------------------------------------------------------------------
# 1 — HOW TO USE
# ----------------------------------------------------------------------------

S1 = page(3, '<span class="num">1</span>How to use this booklet', """
<p class="lead">This booklet merges everything the Week 02 material contains into one ordered document, with the original figures, and it marks what the doctor treated as examinable.</p>

<h2>Two sources, clearly separated</h2>
<p>The booklet the doctor distributed is a <b>compilation of two different books</b>. That was verified by searching the primary source end to end. It matters, because the two parts behave differently in the exam.</p>
<table>
  <tr><th style="width:26%">Part</th><th style="width:37%">Where it comes from</th><th>How to treat it</th></tr>
  <tr>
    <td><b>Sections 3.1–3.14</b><br/><span class="small">Risk theory</span></td>
    <td>Sharp, <i>Introduction to Cybersecurity</i>, Chapter 3 &ldquo;Risk&rdquo;, pp. 37–56</td>
    <td>Complete and verified against the original. Every figure in this booklet is from here.</td>
  </tr>
  <tr>
    <td><b>Sections 4.1–4.8</b><br/><span class="small">Physical security, authentication, NIST</span></td>
    <td>An <b>unidentified second source</b>. None of this text appears in Sharp at all.</td>
    <td>Use the wording as given. One term in it is wrong — see §4.4.</td>
  </tr>
</table>

<h2>The doctor's exam method</h2>
<p>The quiz is <b>written / essay</b>, roughly ten minutes, at the start of the lecture. The stakes are soft — it is a reading check.</p>
<div class="key">
  <span class="tag">Answer shape</span>
  <ul class="tight" style="margin-bottom:0">
    <li><b>If the question gives you numbers</b> — apply the formula. This booklet has two: <b>S = F &times; K</b> and <b>R = S / M</b>.</li>
    <li><b>If it gives you no numbers</b> (an analytical scenario) — answer as <b>step &rarr; CIA pillar &rarr; (techniques in brackets)</b>.</li>
  </ul>
</div>

<h2>How the marking in this booklet works</h2>
<table>
  <tr><th style="width:30%">Marker</th><th>Meaning</th></tr>
  <tr><td><b>Marked YELLOW</b> in the doctor's copy</td><td>A countable list to memorise — the count first, then the items.</td></tr>
  <tr><td><b>Marked RED</b> in the doctor's copy</td><td>Something to be able to explain out loud.</td></tr>
  <tr><td><b>Not marked at all</b></td><td>Still readable material, but not flagged as examinable.</td></tr>
  <tr><td><b>Corrected</b> badge</td><td>The book itself is wrong here. The exam answer and the correct fact are both given.</td></tr>
</table>

<div class="note">
  <span class="tag">One rule for the whole booklet</span>
  Where the material is inaccurate, <b>answer in the doctor's vocabulary — she marks it — but know the correct fact.</b> Writing the correction alongside, in brackets, shows mastery instead of contradicting her.
</div>
""")

# ----------------------------------------------------------------------------
# 2 — EMPHASIS MAP
# ----------------------------------------------------------------------------

S2 = page(4, '<span class="num">2</span>What the doctor marked as important', """
<p class="lead">The delivered Word file carries the doctor's own highlighting. Extracting it mechanically gives an objective map of the exam scope — it is not an interpretation.</p>

<h2>Yellow highlight &mdash; memorise these lists</h2>
<table>
  <tr><th style="width:58%">Marked text</th><th>What it is</th></tr>
  <tr><td>Risk avoidance · Risk reduction · Risk retention · Risk transfer · Risk sharing</td><td>The <b>five mitigation strategies</b> (§3.9)</td></tr>
  <tr><td>COBIT · COSO · FAIR · OCTAVE</td><td>Four of the <b>five analysis frameworks</b> (§3.10)</td></tr>
  <tr><td>&ldquo;&hellip;the latest version of ISO/IEC 27002 from 2022&hellip; within <b>14 categories</b>&rdquo;</td><td>The ISO number <b>14</b> (§3.11) &mdash; <b>corrected</b> in this booklet</td></tr>
  <tr><td>&ldquo;&hellip;threats and vulnerabilities in <b>three phases</b>&rdquo;</td><td>OCTAVE's phase count (§3.12)</td></tr>
</table>

<h2>Red highlight &mdash; be able to explain these</h2>
<table>
  <tr><th style="width:58%">Marked text</th><th>What it is</th></tr>
  <tr><td>Build up asset-based threat profiles · Identify vulnerabilities in the infrastructure · Develop a security strategy and plans</td><td>The <b>three OCTAVE phases</b> (§3.12)</td></tr>
  <tr><td>Plan · Do · Check · Act</td><td>The <b>four PDCA elements</b> (§3.13)</td></tr>
  <tr><td>Locks and Keys · Locking Deadbolts · Cipher Locks · Control Gates · Authentication Systems</td><td>The <b>physical security controls</b> (§4.2–4.4)</td></tr>
  <tr><td>Knowledge · Possession · Inheritance · Location</td><td>The <b>four authentication factors</b> (§4.4)</td></tr>
</table>

<h2>Coloured text &mdash; the taxonomies</h2>
<p>Not highlighted, but set in colour, which marks the classification schemes:</p>
<ul>
  <li>The <b>four threat groups</b> — hardware, software, data, liveware (§3.6)</li>
  <li>The <b>countermeasure-to-threat matching</b> (§3.7)</li>
  <li>The <b>equation letters S, F, K</b> — the only equation symbols she coloured (§3.3)</li>
</ul>

<div class="trap">
  <span class="tag">What she did not mark</span>
  The two NIST blocks — <i>&ldquo;Develop a risk-management program&rdquo;</i> and <i>&ldquo;Use NIST security controls&rdquo;</i> — carry no marking at all. The student's own verdict was that they are <b>not important</b>. Recorded in §4.7 so you can read them once and move on.
</div>
""")

# ----------------------------------------------------------------------------
# 3 — RISK CORE
# ----------------------------------------------------------------------------

S3_1 = page(5, '<span class="num">3.1</span>What is risk? Objective and subjective', """
<div class="def">
  <span class="tag">Definition &mdash; Sharp, p. 38</span>
  Risk, in its <b>technical sense</b>, is <b>the quantitative probability that an error situation occurs and gives rise to damage</b>. In IT security, <b>damage is synonymous with a breach of the security policy</b>.
</div>

<h2>Objective risk</h2>
<p>That definition is <b>objective</b> — it is a property of the system, not of anyone's opinion. It must not be confused with subjective risk.</p>

<h2>Subjective risk</h2>
<p><b>Subjective risk</b> also takes <b>human factors</b> into account — public attitudes, trust, and personality. The same situation can carry a very different perceived risk from its actual risk.</p>

<div class="def">
  <span class="tag">Evidence &mdash; the Danish survey, Sharp p. 56</span>
  In a 2009 Danish investigation, respondents judged whether various events counted as security breaches:
  <ul class="tight" style="margin:2mm 0 0 0">
    <li><b>Almost 100%</b> said it was a breach if other people extracted personal data from their computer over the net.</li>
    <li><b>Only about a quarter</b> thought <b>theft of their computer</b> was a breach — even though theft is <b>more common</b> than hacking and gives the thief easy access to everything on the machine.</li>
  </ul>
</div>
<p class="small">People's perception of risk for those two event types was evidently very different from the actual risk. That gap is exactly what "subjective risk" names.</p>

<div class="key">
  <span class="tag">Exam-ready pair</span>
  <b>Objective risk</b> — the technical, quantitative definition. <b>Subjective risk</b> — the same situation as people perceive it, shaped by attitudes, trust and personality.
</div>
""")

S3_2 = page(6, '<span class="num">3.2</span>Threat, vulnerability and damage', """
<p class="lead">Damage does not appear on its own. It requires a <b>threat</b> acting on a <b>vulnerability</b>.</p>

<div class="def">
  <span class="tag">The causal chain</span>
  <b>Damage</b> occurs when a <b>threat is realised against some weakness in the system</b>. A weakness which can be exploited to damage the system is known as a <b>vulnerability</b>.
</div>

<div class="figbox tall">
""" + fig("fig3_1_shark", "A white shark behind the bars of a cage") + """
  <div class="figcap"><b>Figure 3.1</b> — The threat is the <b>shark</b>; the vulnerability is a <b>welding fault in the cage</b>.<br/>
  Photo: Terry Goss, Wikimedia Commons, CC-BY 2.5 Generic. (Sharp, p. 38)</div>
</div>

<p>The metaphor is worth holding on to, because it separates two things students routinely merge: the <b>shark exists</b> whether or not the cage is faulty, and the <b>welding fault exists</b> whether or not a shark is nearby. <b>Neither one is damage.</b> Damage needs both.</p>

<div class="key">
  <span class="tag">Consequences of the distinction</span>
  <ul class="tight" style="margin-bottom:0">
    <li>A <b>threat</b> is not a vulnerability.</li>
    <li>A <b>vulnerability</b> is not a threat.</li>
    <li>Neither is, by itself, <b>risk</b> — risk is the quantified combination (§3.3).</li>
  </ul>
</div>

<div class="trap">
  <span class="tag">Exam trap</span>
  If a question describes a weakness with no actor, the answer is <b>vulnerability</b>. If it describes an actor with no weakness, the answer is <b>threat</b>. Only when both are present, and quantified, does the question become about <b>risk</b>.
</div>
""")

S3_3 = page(7, '<span class="num">3.3</span>Basic risk: S = F &times; K, and the risk matrix', """
<div class="formula">S = F &times; K</div>

<table>
  <tr><th style="width:16%">Symbol</th><th>Meaning &mdash; Sharp, p. 38</th></tr>
  <tr><td><b>S</b></td><td>The <b>basic risk</b> of a threat</td></tr>
  <tr><td><b>F</b></td><td>The <b>frequency</b> of attempts to exploit the vulnerability</td></tr>
  <tr><td><b>K</b></td><td>The <b>consequences</b> of a successful attempt</td></tr>
</table>

<p class="small">Note: the doctor coloured <b>S</b>, <b>F</b> and <b>K</b> red in her copy. These three letters are hers.</p>

<h2>Why it is a multiplication, not a sum</h2>
<p>This is worth being able to argue, because it is a likely essay question.</p>
<ul>
  <li><b>By multiplication:</b> if either factor is near zero, the product collapses. A nuisance that happens constantly but harms nothing is not a catastrophe; a catastrophe that never happens is not a threat either. <b>Both factors must matter</b> — and multiplication enforces exactly that.</li>
  <li><b>By addition:</b> a very large frequency could <b>compensate</b> for zero consequences and produce a large &ldquo;risk&rdquo;. That is nonsense — an event with no consequence cannot be a risk.</li>
</ul>

<div class="figbox">
""" + fig("fig3_2_risk_matrix", "The risk matrix: frequency against consequences") + """
  <div class="figcap"><b>Figure 3.2</b> — The risk matrix. The individual threats are placed in the square matching their frequency and consequences. (Sharp, p. 38)</div>
</div>

<h2>Reading the matrix</h2>
<table>
  <tr><th class="c">Consequences &darr; / Frequency &rarr;</th><th class="c">low</th><th class="c">medium</th><th class="c">high</th></tr>
  <tr><td><b>low</b></td><td class="c">green</td><td class="c">green</td><td class="c">green</td></tr>
  <tr><td><b>medium</b></td><td class="c">green</td><td class="c">yellow</td><td class="c">yellow</td></tr>
  <tr><td><b>high</b></td><td class="c">green</td><td class="c">yellow</td><td class="c" style="background:#ffe3e3"><b>red</b></td></tr>
</table>
<p>The diagonal arrow labelled <b>Risk</b> shows risk rising from the top-left corner to the bottom-right corner.</p>

<div class="key">
  <span class="tag">The rule to remember</span>
  <b>Red appears in exactly one cell: high frequency AND high consequences.</b> This is what the book states in words — <i>&ldquo;This arises when the consequences of a successful attack are high and the frequency of attempts to exploit the vulnerability is also high.&rdquo;</i>
</div>
""")

S3_4 = page(8, '<span class="num">3.4</span>Countermeasures and residual risk: R = S / M', """
<p class="lead">Risk is reduced by introducing <b>countermeasures</b>, also called <b>controls</b>, which must protect against the relevant threat. What is left is the <b>residual risk</b>.</p>

<div class="formula">R = S / M</div>

<table>
  <tr><th style="width:16%">Symbol</th><th>Meaning &mdash; Sharp, p. 39</th></tr>
  <tr><td><b>R</b></td><td>The <b>residual risk</b> — the reduced risk</td></tr>
  <tr><td><b>S</b></td><td>The risk of the threat, from §3.3</td></tr>
  <tr><td><b>M</b></td><td>The <b>level of countermeasures</b> — and this is the part to be precise about</td></tr>
</table>

<div class="key">
  <span class="tag">What M covers &mdash; quote this in the exam</span>
  <b>M covers both the number of countermeasures &mdash; there can be several things which affect the risk for particular types of attack &mdash; and their effectiveness.</b>
  <p style="margin:2mm 0 0 0" class="small">So M is not simply "how many countermeasures". Ten weak measures are not the same as one strong one. M is a <b>combined protective factor</b>: count <b>and</b> quality.</p>
</div>

<div class="figbox">
""" + fig("fig3_3_residual", "The residual risk matrix: risk against countermeasures") + """
  <div class="figcap"><b>Figure 3.3</b> — The residual risk matrix. Note the countermeasures axis is <b>reversed</b>: high on the left. (Sharp, p. 39)</div>
</div>

<h2>Reading the matrix</h2>
<table>
  <tr><th class="c">Risk &darr; / Countermeasures &rarr;</th><th class="c">high</th><th class="c">medium</th><th class="c">low</th></tr>
  <tr><td><b>low</b></td><td class="c">green</td><td class="c">green</td><td class="c">green</td></tr>
  <tr><td><b>medium</b></td><td class="c">green</td><td class="c">yellow</td><td class="c">yellow</td></tr>
  <tr><td><b>high</b></td><td class="c">green</td><td class="c">yellow</td><td class="c" style="background:#ffe3e3"><b>red</b></td></tr>
</table>
<p>Diagonal arrow labelled <b>Residual risk</b>. <b>Red appears in exactly one cell: high risk AND low countermeasures.</b></p>

<div class="key">
  <span class="tag">The two-stage model &mdash; do not mix the matrices up</span>
  <table style="margin:0">
    <tr><th style="width:34%">Matrix</th><th>Axes</th><th style="width:26%">Red corner</th></tr>
    <tr><td>Risk matrix (Fig. 3.2)</td><td>frequency &times; consequences</td><td>high and high</td></tr>
    <tr><td>Residual risk matrix (Fig. 3.3)</td><td>risk &divide; countermeasures</td><td>high risk, low countermeasures</td></tr>
  </table>
  <p style="margin:2.5mm 0 0 0" class="small">The relationship: the first equation <b>feeds</b> the second. <b>S</b> is computed once from frequency and consequences, then used as the input to <b>R = S / M</b>. They are two stages of one pipeline, not two alternatives.</p>
</div>
""")

S3_5 = page(9, '<span class="num">3.5</span>The three-point scale', """
<div class="def">
  <span class="tag">Sharp, p. 39 &mdash; quoted</span>
  <i>&ldquo;In the two figures, 3.2 and 3.3, we have here used a 3-point scale (low, medium, high) for all quantities (frequency, consequences, risk, countermeasures, residual risk). This is a somewhat arbitrary but often used convention.&rdquo;</i>
</div>

<p>The book gives its reason for staying coarse, and it is a good one:</p>
<blockquote class="note" style="margin:3mm 0">
  <i>&ldquo;Even if one can argue for a finer division of the scale, the uncertainty in estimating these variables is in practice large, and a finer division is therefore (at least in the first instance) more or less meaningless.&rdquo;</i>
</blockquote>

<h2>Why the scale matters for the equations</h2>
<p>The book's own worked examples print the arithmetic like this:</p>
<div class="formula" style="font-size:12.5pt">medium &times; high &nbsp;=&nbsp; medium</div>
<p>That is not arithmetic multiplication — it is a <b>combination on an ordinal scale</b>, read back onto the same three levels. So <b>&times; and &divide; in this material are shorthand for the colour tables</b>, not numbers to calculate.</p>

<div class="trap">
  <span class="tag">Exam trap</span>
  If a question gives you low / medium / high, <b>read the answer off Figure 3.2 or 3.3</b>. Do not try to multiply or divide the words as if they were numbers.
</div>

<h2>Consequences are the hardest quantity to place</h2>
<p>The book notes that consequences can be particularly difficult to put on a scale, because the impact of an attack may involve several kinds of element:</p>
<ul>
  <li>Financial losses due to increased costs or loss of income</li>
  <li>Loss of reputation — for example failure to provide agreed services or meet delivery dates</li>
  <li>Penalties for failing to fulfil regulatory requirements</li>
  <li>Compensation to employees for failing to meet obligations of employment</li>
</ul>
<p>Or combinations of these. And what counts as <b>low, medium or high</b> naturally depends on <b>the size and purpose of the IT system</b> — a consequence that is severe for a small clinic may be minor for a bank.</p>
""")

S3_6 = page(10, '<span class="num">3.6</span>Threats in IT systems &mdash; the four groups', """
<p class="lead">Many IT users believe the only threat is an attacker hacking in. In reality the threat pattern is far more varied. The book separates it into <b>four groups</b>.</p>

<h2>1. Hardware-related threats</h2>
<p>Threats which <b>physically</b> affect the computer itself or the infrastructure it depends on.</p>
<ul>
  <li>Harmful surroundings</li>
  <li>Natural disasters such as storms</li>
  <li>Physical attacks on the computer, such as theft</li>
  <li>Faults in the infrastructure</li>
</ul>

<h2>2. Software-related threats</h2>
<p>Threats affecting the <b>software installed</b> in the computer — applications and the operating system — or arising from poorly designed or wilfully malicious programs from outside.</p>
<ul>
  <li>Unauthorised modification or deletion of software</li>
  <li>Wilfully malicious programs — <b>malware</b>: viruses, worms, trojan horses, logic bombs</li>
  <li>Poorly designed programs which contain vulnerabilities</li>
  <li>Incorrect or out-of-date software versions</li>
  <li>Theft or unauthorised copying of software</li>
</ul>

<h2>3. Data-related threats</h2>
<p>Threats which can lead to <b>unauthorised processing, including storage, of data</b> in any way.</p>
<ul>
  <li>Unwanted storage, modification, disclosure or deletion of data</li>
  <li><b>Inference</b> — collecting accessible data from which it is possible to <b>deduce confidential information that is not directly accessible</b></li>
  <li><b>Masquerading</b> — pretending to be someone else — and unauthorised access</li>
</ul>

<h2>4. Liveware-related threats</h2>
<p>Threats related to <b>human error among the computer's users</b>.</p>
<ul>
  <li>Social engineering, phishing</li>
  <li>IT fraud, forgery and other forms of criminality, now carried out with the help of computers</li>
</ul>

<div class="key">
  <span class="tag">The distinction that earns marks</span>
  <b>Inference is not direct theft of confidential data.</b> It is collecting data that <i>is</i> accessible and deducing from it information that is <i>not</i> directly accessible. If a question describes a chain of reasoning from public or low-privilege data to a secret, the answer is <b>inference</b>, not unauthorised access.
</div>
""")

S3_7 = page(11, '<span class="num">3.7</span>Countermeasures matched to threats', """
<p class="lead">A threat is blocked by controlling a vulnerability with suitable countermeasures — and the countermeasure <b>must be adapted to the type of threat</b>. The book gives six pairings.</p>

<table>
  <tr><th style="width:52%">Threat</th><th>Countermeasure</th></tr>
  <tr><td>Attackers outside the system, attacking through the Internet</td><td><b>Firewalls</b> in the network, to prevent traffic from the attacker reaching the target</td></tr>
  <tr><td>Malware</td><td><b>Antivirus programs</b> and other so-called security programs</td></tr>
  <tr><td>Vandalism, theft and other physical damage to the equipment</td><td>Place the equipment in a <b>secure room</b></td></tr>
  <tr><td>Unauthorised modification or deletion of data or software</td><td>Take <b>regular backup copies</b></td></tr>
  <tr><td>Unauthorised access to data</td><td>Use <b>encryption</b> or <b>access control</b></td></tr>
  <tr><td>Personnel and ordinary authorised users</td><td><b>Check personnel</b> and introduce <b>suitable training</b></td></tr>
</table>

<div class="trap">
  <span class="tag">Exam trap</span>
  The last row is the one that catches people. The threat here is <b>the organisation's own authorised users</b> — not an outsider. And the countermeasure is <b>administrative, not technical</b>: vetting and training. If a question describes an insider threat and the options are all technical controls, the administrative answer is the one you want.
</div>

<h2>The general point</h2>
<p>There is no single countermeasure that covers everything. The matching is the content: <b>each threat has its own appropriate control</b>, and choosing the control is the security work.</p>
""")

S3_8 = page(12, '<span class="num">3.8</span>The five steps for dealing with damage', """
<div class="note">
  <span class="tag">Recovered content</span>
  This list is in the original book (Sharp, p. 42). <b>It was missing from the Word booklet the doctor distributed.</b> If you remembered a five-step list that was not in the file, this is it.
</div>

<p class="lead">More generally, the book says, one can deal with damaging events in five ways:</p>

<table>
  <tr><th class="c" style="width:10%">#</th><th style="width:26%">Step</th><th>What it means</th></tr>
  <tr><td class="c"><b>1</b></td><td><b>Preventing</b> them</td><td>Block attacks, or remove or reduce the vulnerability</td></tr>
  <tr><td class="c"><b>2</b></td><td><b>Complicating</b> them</td><td>Make the attack more difficult to perform</td></tr>
  <tr><td class="c"><b>3</b></td><td><b>Diverting</b> them</td><td>Make other targets more attractive</td></tr>
  <tr><td class="c"><b>4</b></td><td><b>Detecting</b> them</td><td>When they occur, or later</td></tr>
  <tr><td class="c"><b>5</b></td><td><b>Reestablishing</b> status</td><td>After them</td></tr>
</table>

<div class="key">
  <span class="tag">The split worth memorising &mdash; the book's own wording</span>
  <i>&ldquo;Notice that some of them (1, 2 and 3) are <b>proactive</b> steps, which reduce the risk before the damage takes place, while others (4 and 5) are <b>reactive</b> steps which are taken when the damage has in fact occurred.&rdquo;</i>
  <p style="margin:2.5mm 0 0 0"><b>Proactive: 1, 2, 3. &nbsp;&nbsp;Reactive: 4, 5.</b> Ways of dealing with damage can naturally be combined.</p>
</div>

<div class="trap">
  <span class="tag">Do not confuse the two five-item lists</span>
  <ul class="tight" style="margin-bottom:0">
    <li><b>This list</b> (§3.8) — how to <b>deal with damage</b>: preventing, complicating, diverting, detecting, reestablishing.</li>
    <li><b>The next list</b> (§3.9) — the five <b>risk mitigation strategies</b>: avoidance, reduction, retention, transfer, sharing.</li>
  </ul>
  Both have five items. They are different lists, and a question about one will offer items from the other as distractors.
</div>
""")

S3_9 = page(13, '<span class="num">3.9</span>Risk management and the five strategies', """
<div class="def">
  <span class="tag">Definition &mdash; Sharp, p. 42</span>
  <b>Risk management</b> deals with <b>all the activities which are related to evaluating and reducing risks</b>. The part whose aim is to reduce risk to an <b>acceptable level</b> is often called <b>risk mitigation</b>.
</div>
<p class="small">Note the containment: risk mitigation is a <i>part of</i> risk management, not a synonym for it. The umbrella is evaluation <b>and</b> reduction; the subset is reduction to an acceptable level.</p>

<h2>The five strategies &mdash; in this order</h2>
<div class="key">
  <span class="tag">Marked YELLOW by the doctor &mdash; learn the order</span>
  <table style="margin:0">
    <tr><th class="c" style="width:8%">#</th><th style="width:24%">Strategy</th><th style="width:38%">What it means</th><th>The book's example</th></tr>
    <tr><td class="c"><b>1</b></td><td><b>Risk avoidance</b></td><td>Keep the target system away from given risks</td><td>Forbid risky behaviour such as use of WiFi</td></tr>
    <tr><td class="c"><b>2</b></td><td><b>Risk reduction</b></td><td>Take proactive steps to prevent losses occurring, or to reduce the extent of the loss</td><td>Make use of backups, encryption and so on</td></tr>
    <tr><td class="c"><b>3</b></td><td><b>Risk retention</b></td><td>Allow a certain, <b>agreed</b> amount of residual risk</td><td>Use reliable, but not redundant, communication equipment</td></tr>
    <tr><td class="c"><b>4</b></td><td><b>Risk transfer</b></td><td>Transfer the risk to others</td><td>Set up a contract for outsourcing</td></tr>
    <tr><td class="c"><b>5</b></td><td><b>Risk sharing</b></td><td>Agree with other parties to deal with risks jointly</td><td>Agree on common facilities or mutual insurance</td></tr>
  </table>
</div>

<div class="trap">
  <span class="tag">Transfer versus sharing</span>
  <b>Transfer</b> hands the risk to someone else — you are no longer carrying it. <b>Sharing</b> keeps you in the risk but splits it with others. Outsourcing is transfer; mutual insurance or shared facilities is sharing.
</div>

<h2>The balance every choice must strike</h2>
<p>Whichever strategy you choose, the book says risk management must balance <b>three factors</b>:</p>
<table>
  <tr><th style="width:26%">Factor</th><th>The question it answers</th></tr>
  <tr><td><b>Security</b></td><td>How well is the IT system protected against unwanted events?</td></tr>
  <tr><td><b>Functionality</b></td><td>How well does the IT system perform its intended functions?</td></tr>
  <tr><td><b>Usability</b></td><td>How easy is it for users to make use of the system?</td></tr>
</table>
<div class="trap">
  <span class="tag">The book's warning &mdash; worth quoting</span>
  <i>&ldquo;This last factor is unfortunately often forgotten by system designers&hellip; <b>If security measures do not give a usable system, users will find ways to avoid them!</b>&rdquo;</i>
</div>
""")

S3_10 = page(14, '<span class="num">3.10</span>Systematic security analysis &mdash; five frameworks', """
<p class="lead">To develop a secure system it is an advantage to use a systematic method. Over the years a number of procedures have been developed for security analysis of IT systems.</p>

<table>
  <tr><th style="width:20%">Framework</th><th style="width:34%">Full name</th><th>What it offers</th></tr>
  <tr>
    <td><b>COBIT</b><br/><span class="small">marked yellow</span></td>
    <td><b>C</b>ontrol <b>O</b>bjectives for <b>I</b>nformation and related <b>T</b>echnology</td>
    <td>Objectives for measures which can be used to <b>manage risk</b></td>
  </tr>
  <tr>
    <td><b>COSO</b><br/><span class="small">marked yellow</span></td>
    <td><b>C</b>ommittee of <b>S</b>ponsoring <b>O</b>rganizations</td>
    <td>A detailed description of the <b>internal processes</b> a company must follow to reach a suitably low risk</td>
  </tr>
  <tr>
    <td><b>FAIR</b><br/><span class="small">marked yellow</span></td>
    <td><b>F</b>actor <b>A</b>nalysis of <b>I</b>nformation <b>R</b>isk</td>
    <td>A <b>taxonomy</b> of risk factors, a <b>standard for naming</b> risk-related quantities, and a <b>model for calculating</b> risk</td>
  </tr>
  <tr>
    <td><b>ISO/IEC 27002</b></td>
    <td>International standard</td>
    <td>A <b>checklist</b> of what must be considered to achieve a secure system (§3.11)</td>
  </tr>
  <tr>
    <td><b>OCTAVE</b><br/><span class="small">marked yellow</span></td>
    <td><b>O</b>perationally <b>C</b>ritical <b>T</b>hreat, <b>A</b>sset and <b>V</b>ulnerability <b>E</b>valuation</td>
    <td>The <b>process</b> of analysing threats and the corresponding risks, and of finding suitable countermeasures (§3.12)</td>
  </tr>
</table>

<div class="key">
  <span class="tag">How to tell them apart in one line each</span>
  <ul class="tight" style="margin-bottom:0">
    <li><b>COBIT</b> — objectives for managing risk.</li>
    <li><b>COSO</b> — internal processes inside the company.</li>
    <li><b>FAIR</b> — the only one with a <b>calculation model</b>; also a naming standard.</li>
    <li><b>ISO/IEC 27002</b> — a <b>checklist</b>.</li>
    <li><b>OCTAVE</b> — a <b>process</b>.</li>
  </ul>
</div>

<p>The book notes that the last two are not alternatives: <b>they supplement one another</b>, because risk analysis is an important element of the ISO/IEC 27002 checklist.</p>
""")

S3_11 = page(15, '<span class="num">3.11</span>ISO/IEC 27002 and the ISO 27000 series', """
<div class="def">
  <span class="tag">Sharp, p. 43</span>
  ISO/IEC 27002 is part of a series developed <b>jointly by ISO and IEC</b> — the International Organization for Standardization and the International Electrotechnical Commission. The series currently consists of <b>44 complete or planned standards</b>, covering information security in general and in specific areas such as <b>finance, energy supply, collection of digital evidence and cloud computing</b>.
</div>

<h2>The series, as the book tabulates it</h2>
<p>The book carries a table the Word booklet dropped. It is worth having, because the two numbers that get confused are both in it.</p>
<table>
  <tr><th style="width:26%">Standard</th><th>Topic</th></tr>
  <tr><td><b>ISO/IEC 27000</b></td><td>Information security management systems — Overview and vocabulary</td></tr>
  <tr><td><b>ISO/IEC 27001</b></td><td>Information security management systems — <b>Requirements</b></td></tr>
  <tr><td><b>ISO/IEC 27002</b></td><td><b>Code of practice for information security controls</b></td></tr>
  <tr><td>ISO/IEC 27003</td><td>ISMS implementation guidance</td></tr>
  <tr><td>ISO/IEC 27005</td><td>Information security risk management</td></tr>
  <tr><td>ISO/IEC 27017</td><td>Code of practice for information security controls for cloud services</td></tr>
</table>

<div class="key">
  <span class="tag">27001 versus 27002 &mdash; the distinction the booklet lost</span>
  <b>27001 = Requirements.</b> It is the standard an organisation is <b>certified against</b>.<br/>
  <b>27002 = Code of practice.</b> It is the <b>guidance</b> — the checklist of controls.
  <p style="margin:2.5mm 0 0 0" class="small">They are different documents. If a question asks which one you are audited against, it is 27001.</p>
</div>

<h2>The fourteen categories &mdash; and the correction</h2>
<div class="trap">
  <span class="tag">Corrected &mdash; the book is wrong here, and the doctor highlighted this line yellow</span>
  The material says: <i>&ldquo;The latest version of ISO/IEC 27002 from <b>2022</b> describes targets for what has to be done within <b>14 categories</b>&rdquo;</i> — and then lists fourteen items.
  <p style="margin:2.5mm 0 0 0">The list is real, but the <b>label is wrong</b>:</p>
  <table style="margin:2.5mm 0 0 0">
    <tr><th style="width:30%">Edition</th><th>Actual structure</th></tr>
    <tr><td><b>ISO/IEC 27002:2013</b></td><td><b>114 controls in 14 clauses</b> — and these are the fourteen items listed</td></tr>
    <tr><td><b>ISO/IEC 27002:2022</b></td><td><b>93 controls in 4 themes</b>: Organisational · People · Physical · Technological</td></tr>
  </table>
  <p style="margin:2.5mm 0 0 0"><b>In the exam:</b> write <b>14</b>, because that is what she marked. If there is room, add <b>&ldquo;(the 2013 structure; the 2022 revision reorganised into 4 themes and 93 controls)&rdquo;</b>. That shows mastery rather than contradicting her.</p>
</div>

<h2>The fourteen categories, in order</h2>
<table>
  <tr><th class="c" style="width:8%">#</th><th style="width:42%">Category</th><th class="c" style="width:8%">#</th><th>Category</th></tr>
  <tr><td class="c">1</td><td>Information security policies</td><td class="c">8</td><td>Operation security</td></tr>
  <tr><td class="c">2</td><td>Organization of information security</td><td class="c">9</td><td>Communication security</td></tr>
  <tr><td class="c">3</td><td>Human resource security</td><td class="c">10</td><td>System acquisition, development and maintenance</td></tr>
  <tr><td class="c">4</td><td>Asset management</td><td class="c">11</td><td>Supplier relationships</td></tr>
  <tr><td class="c">5</td><td>Access control</td><td class="c">12</td><td>Information security incident management</td></tr>
  <tr><td class="c">6</td><td>Cryptography</td><td class="c">13</td><td>Information security aspects of business continuity management</td></tr>
  <tr><td class="c">7</td><td>Physical and environmental security</td><td class="c">14</td><td>Compliance with legal and contractual requirements</td></tr>
</table>
<p class="small">The list is logically ordered — policies &rarr; organisation &rarr; people &rarr; assets &rarr; access &rarr; cryptography &rarr; physical &rarr; operations &rarr; communications &rarr; development &rarr; suppliers &rarr; incidents &rarr; continuity &rarr; compliance. Learn the logic and the fourteen fall out in sequence.</p>
""")

S3_12 = page(16, '<span class="num">3.12</span>OCTAVE', """
<div class="def">
  <span class="tag">What it is</span>
  <b>OCTAVE</b> — <b>O</b>perationally <b>C</b>ritical <b>T</b>hreat, <b>A</b>sset and <b>V</b>ulnerability <b>E</b>valuation — is a method for <b>risk analysis</b>, developed at <b>Carnegie Mellon University</b> for the <b>US Department of Defense</b>, by the <b>CERT</b> Coordination Center at the university's Software Engineering Institute.
</div>

<h2>The three phases</h2>
<div class="key">
  <span class="tag">Marked RED by the doctor &mdash; be able to state these</span>
  <table style="margin:0">
    <tr><th class="c" style="width:10%">Phase</th><th style="width:38%">Name</th><th>What happens</th></tr>
    <tr><td class="c"><b>1</b></td><td><b>Build asset-based threat profiles</b></td><td>An organisational evaluation. Determine what matters to the organisation, select the critical assets, and identify threats to each — creating a threat profile per asset</td></tr>
    <tr><td class="c"><b>2</b></td><td><b>Identify vulnerabilities in the infrastructure</b></td><td>Examine network access paths and how far each class of component resists attack</td></tr>
    <tr><td class="c"><b>3</b></td><td><b>Develop a security strategy and plans</b></td><td>Identify risks to critical assets, build a protection strategy and mitigation plans</td></tr>
  </table>
</div>

<h2>The variants</h2>
<p>The book lists <b>four</b>:</p>
<ol>
  <li><b>OCTAVE</b> — the original method</li>
  <li><b>OCTAVE-S</b> — a simplified version for <b>small enterprises with limited resources</b></li>
  <li><b>OCTAVE ALLEGRO</b> — an expanded version for enterprises with an <b>advanced IT structure</b></li>
  <li><b>OCTAVE FORTE</b> — <span class="small">listed in the book with no description</span></li>
</ol>

<div class="trap">
  <span class="tag">On the fourth variant &mdash; a note, not a correction</span>
  Public OCTAVE documentation names only <b>three</b> methodologies: OCTAVE, OCTAVE-S and OCTAVE Allegro. <b>No source outside this book names an &ldquo;OCTAVE Forte&rdquo;</b>, and the book itself gives no description — the sentence is garbled in the original. So the fourth variant is the <b>book's</b>, not the doctor's invention, and she is reproducing it faithfully.
  <p style="margin:2.5mm 0 0 0"><b>In the exam:</b> the book says four, so write four. The three that matter for explaining are OCTAVE, OCTAVE-S and Allegro.</p>
</div>

<p class="small">Also worth knowing, though not in this chapter: <b>OCTAVE Allegro</b> runs on <b>eight steps in four phases</b>, not three. The three-phase structure above belongs to the original OCTAVE method.</p>
""")

S3_13 = page(17, '<span class="num">3.13</span>PDCA', """
<div class="def">
  <span class="tag">Why PDCA at all &mdash; Sharp, p. 53</span>
  <b>Risk management should not be a one-time activity.</b> The risk profile changes with time, as new forms of attack are developed or known threats appear more often. The situation must be <b>re-evaluated at regular intervals</b>. Risk management therefore most often takes the form of a <b>PDCA process</b>.
</div>

<div class="figbox tall">
""" + fig("fig3_11_pdca", "The PDCA cycle") + """
  <div class="figcap"><b>Figure 3.11</b> — Schematic view of a PDCA process. (Sharp, p. 54)</div>
</div>

<h2>The four phases</h2>
<div class="key">
  <span class="tag">Marked RED by the doctor &mdash; the acronym and the elements</span>
  <table style="margin:0">
    <tr><th style="width:16%">Phase</th><th>What happens in risk management</th></tr>
    <tr><td><b>Plan</b></td><td>Threats are identified, risks are analysed, and countermeasures are planned</td></tr>
    <tr><td><b>Do</b></td><td>Countermeasures or other forms of risk management are implemented</td></tr>
    <tr><td><b>Check</b></td><td>The implemented solution is monitored, to check that the desired level of security is maintained</td></tr>
    <tr><td><b>Act</b></td><td>The solution is adjusted so that it continues to give the desired security level, <b>or</b> a decision is taken to carry out a completely new Plan phase</td></tr>
  </table>
</div>

<div class="key">
  <span class="tag">The point most students miss</span>
  <b>Act does not close the process — it restarts it.</b> It ends either in an adjustment or in a decision to begin a <b>completely new Plan phase</b>. PDCA is a <b>cycle</b>, not a straight line: the four phases are repeated continually.
</div>

<h2>Where OCTAVE fits</h2>
<p>The book places the two together: when risk analysis is carried out using <b>OCTAVE</b>, that activity fits into the <b>Plan</b> phase of PDCA. The remaining phases deal with the necessary follow-up of the analysis, to see what to do next.</p>
""")

S3_14 = page(18, '<span class="num">3.14</span>Worked examples', """
<p class="lead">The book works three threat scenarios through both matrices. Reading them once shows how the ordinal scale behaves in practice.</p>

<h2>The three scenarios</h2>
<table>
  <tr><th style="width:12%">Threat</th><th style="width:22%">Frequency</th><th style="width:34%">Consequences</th><th>Risk</th></tr>
  <tr>
    <td><b>1</b></td>
    <td>medium<br/><span class="small">about once a month</span></td>
    <td>high<br/><span class="small">data for some employees is missing, giving legal problems and possibly compensation</span></td>
    <td><b>medium &times; high = medium</b></td>
  </tr>
  <tr>
    <td><b>2</b></td>
    <td>low<br/><span class="small">about once a year</span></td>
    <td>high<br/><span class="small">loss of communication with the outside world, causing loss of income</span></td>
    <td><b>low &times; high = low</b></td>
  </tr>
  <tr>
    <td><b>3</b></td>
    <td>medium<br/><span class="small">about once a month</span></td>
    <td>high<br/><span class="small">the design department cannot operate; loss of income and reputation</span></td>
    <td><b>medium &times; high = medium</b></td>
  </tr>
</table>

<div class="figrow">
  <div>""" + fig("fig3_9_risk_example", "Risk matrix with three threats placed") + """
    <div class="figcap"><b>Figure 3.9</b> — the three threats placed in the risk matrix. (Sharp, p. 52)</div>
  </div>
  <div>""" + fig("fig3_10_resid_example", "Residual risk matrix with the three threats placed") + """
    <div class="figcap"><b>Figure 3.10</b> — the same threats after countermeasures. (Sharp, p. 53)</div>
  </div>
</div>

<h2>Then the countermeasures are applied</h2>
<table>
  <tr><th style="width:12%">Threat</th><th style="width:16%">Risk</th><th style="width:30%">Countermeasures</th><th>Residual risk</th></tr>
  <tr><td><b>1</b></td><td>medium</td><td>medium — backup of personnel records taken every night</td><td><b>medium / medium = medium</b></td></tr>
  <tr><td><b>2</b></td><td>low</td><td>medium — spare mail server operational within 12 hours</td><td><b>low / medium = low</b></td></tr>
  <tr><td><b>3</b></td><td>medium</td><td>medium — incremental backup of design files every hour</td><td><b>medium / medium = medium</b></td></tr>
</table>

<div class="trap">
  <span class="tag">What these examples prove about the equations</span>
  <b>medium &times; high is given as medium, not as a number.</b> So the multiplication and division are <b>ordinal combinations read off the colour table</b> — not arithmetic. See §3.5.
</div>

<h2>What happens next, in the book's own words</h2>
<p><i>&ldquo;After this one would typically consider whether the residual risk is too high — that is to say, whether it lies in a yellow or red area in the residual risk matrix. If the residual risk is too high, more or better countermeasures must be introduced, or other forms of risk mitigation must be used.&rdquo;</i></p>
""")

# ----------------------------------------------------------------------------
# 4 — SECOND SOURCE
# ----------------------------------------------------------------------------

S4_1 = page(19, '<span class="num">4.1</span>Security policy and access control', """
<div class="note">
  <span class="tag">Source</span>
  Everything from §4.1 onward comes from the <b>second, unidentified source</b> in the doctor's booklet. None of it appears in Sharp. The wording is reproduced as given, with one correction flagged in §4.4.
</div>

<div class="def">
  <span class="tag">Security policy</span>
  A <b>security policy</b> is documentation stating <b>how security should be implemented at each level</b>. Businesses and organisations develop comprehensive security policies that define <b>who is authorised to access different assets</b> and <b>what they are allowed to do with those assets</b> when they do access them.
</div>

<p>It is described as <b>a key component that brings all three levels of security together</b>.</p>

<h2>Why free movement is a problem</h2>
<p>The material's worked example: allowing employees and visitors <b>free access to all departments</b> creates a variety of security risks. Access control is needed for two distinct reasons:</p>
<ol>
  <li>To reduce <b>the human nature of temptation</b> — if everyone can move freely, it is much harder to stop them accessing or taking physical or cyber assets.</li>
  <li>To <b>prevent accidents</b>.</li>
</ol>

<div class="key">
  <span class="tag">The policy-to-enforcement chain</span>
  <ol class="tight" style="margin-bottom:0">
    <li>Develop a <b>cohesive access-control policy at each level</b> — giving authorised people appropriate levels of access to selected assets, while inhibiting access by people who are not authorised.</li>
    <li><b>Enforce</b> those policies with the correct <b>types and numbers</b> of access-control devices.</li>
  </ol>
  <p style="margin:2.5mm 0 0 0">The devices named: <b>sensors · barriers · logs · ID badges · security guards</b> — as deemed appropriate.</p>
</div>

<h2>Cyber security policy</h2>
<p>The company's <b>cyber security policy</b> explains the <b>overall requirements</b> needed to protect an organisation's network data and computer systems.</p>

<div class="key">
  <span class="tag">Three terms, in increasing scope</span>
  <ul class="tight" style="margin-bottom:0">
    <li><b>Security policy</b> — the document: <i>how</i> security is implemented at each level.</li>
    <li><b>Cyber security policy</b> — the organisation's <i>overall requirements</i> for protecting network data and systems.</li>
    <li><b>Cyber risk assessment and management</b> — the ongoing <i>process</i> (§4.8).</li>
  </ul>
</div>
""")

S4_2 = page(20, '<span class="num">4.2</span>Locks, deadbolts and cipher locks', """
<div class="def">
  <span class="tag">Locks and keys &mdash; the distinction worth quoting</span>
  The primary physical barrier in most security perimeters is the <b>lockable door</b>. The <b>door</b> provides the physical barrier, but in itself <b>it will only keep honest people out</b>. The <b>lock</b> provides the <b>authentication function</b> of the barrier, through its <b>key</b>. Having the key signifies that the person either <b>possesses or knows</b> the information required to gain access.
</div>

<h2>Standard key-locking deadbolts</h2>
<ul>
  <li>Locking mechanism similar to the electronic solenoid-operated deadbolt, but <b>engaged or withdrawn with a key</b>.</li>
  <li>Provide an added level of security for doors that <b>can be operated manually</b>.</li>
  <li>Available with a <b>single or double cylinder</b>.</li>
</ul>

<h2>Solenoid-operated deadbolt locks</h2>
<ul>
  <li><b>Electronically operated</b> deadbolt locks.</li>
  <li>Offer an <b>increased level of security for the perimeter</b>.</li>
  <li>Adaptable to any security system; perform well as <b>auxiliary locks</b> on doors where access control is desired.</li>
</ul>

<h2>Cipher locks</h2>
<ul>
  <li>Require <b>personal access codes known by the user</b>.</li>
  <li>Often used in access-control and management systems.</li>
  <li>They operate by <b>unlocking magnetic door locks when the correct programmed code is entered</b> on the cipher-lock keypad.</li>
  <li>Provide an added level of security for <b>perimeter entry areas</b>.</li>
</ul>

<div class="key">
  <span class="tag">The three compared in one line each</span>
  <table style="margin:0">
    <tr><th style="width:30%">Type</th><th>Distinguishing feature</th></tr>
    <tr><td>Standard key-locking deadbolt</td><td>Operated by a <b>key</b>; for doors operated manually; single or double cylinder</td></tr>
    <tr><td>Solenoid-operated deadbolt</td><td><b>Electronic</b>; higher perimeter security; good as an <b>auxiliary</b> lock</td></tr>
    <tr><td>Cipher lock</td><td>A <b>personal access code</b> entered on a keypad; releases a magnetic lock</td></tr>
  </table>
</div>

<div class="trap">
  <span class="tag">The sentence that carries the marks</span>
  <b>&ldquo;The door provides the physical barrier but in itself will only keep honest people out.&rdquo;</b> It is a memorable line, and it makes the point that a barrier without an authentication function is not access control.
</div>
""")

S4_3 = page(21, '<span class="num">4.3</span>Gates and control relays', """
<h2>Access-control gates</h2>
<p>Like a door, a <b>gate</b> is a type of physical barrier that can be <b>swung, drawn, or lowered</b> to control <b>ingress and egress</b> through a wall or fence. Two main types:</p>

<table>
  <tr><th style="width:24%">Type</th><th>Where it is used</th></tr>
  <tr><td><b>Sliding gates</b></td><td>Used where <b>high levels of operational safety and security</b> are needed</td></tr>
  <tr><td><b>Swinging gates</b></td><td>Equipped with <b>fully adjustable hinges</b> that allow the gate to swing through <b>180 degrees</b></td></tr>
</table>

<h2>Control relays</h2>
<div class="def">
  <span class="tag">Definition</span>
  Relays are <b>electromechanical devices</b> that employ safer, <b>low-voltage / low-current control signals</b> to control <b>higher-voltage / higher-current devices</b>.
</div>
<p>The point of a relay in a security system is <b>safety of separation</b>: the thing the operator touches runs on low voltage and low current, while the thing being driven — a gate motor, a lock solenoid — can draw far more.</p>

<div class="key">
  <span class="tag">Physical security, in the order the material presents it</span>
  <ol class="tight" style="margin-bottom:0">
    <li><b>Locks and keys</b> — the lockable door and the authentication function of the key</li>
    <li><b>Standard key-locking deadbolts</b> — key-operated</li>
    <li><b>Solenoid-operated deadbolt locks</b> — electronic</li>
    <li><b>Cipher locks</b> — code-operated</li>
    <li><b>Access-control gates</b> — sliding and swinging</li>
    <li><b>Control relays</b> — the low-voltage control layer</li>
  </ol>
</div>
""")

S4_4 = page(22, '<span class="num">4.4</span>Authentication systems and the four factors', """
<div class="def">
  <span class="tag">Definition</span>
  <b>Authentication</b> is the process of <b>determining that someone is who they say they are</b>.
</div>

<p>Effective access control involves being able to control the <b>ingress, egress and regress</b> to an asset based on <b>authorisation</b>. In particular, <b>limiting the access of unauthorised personnel to important assets is the most fundamental security step you can take</b>.</p>

<div class="key">
  <span class="tag">The one-line logic to memorise</span>
  <b>Authorisation is based on authentication.</b>
  <p style="margin:2.5mm 0 0 0" class="small">You cannot decide what someone may do until you know who they are. That single sentence makes the whole section answerable.</p>
</div>

<h2>The four factors</h2>
<div class="key">
  <span class="tag">Marked RED by the doctor &mdash; four factors, not three</span>
  <table style="margin:0">
    <tr><th style="width:20%">Factor</th><th>The material's wording</th></tr>
    <tr><td><b>Knowledge</b></td><td>Something you <b>know</b> — or something that only the designated person should know</td></tr>
    <tr><td><b>Possession</b></td><td>Something you <b>have</b> — or something that only the designated person should have</td></tr>
    <tr><td><b>Inheritance</b></td><td>Something you <b>are</b> — or something that only the designated person is</td></tr>
    <tr><td><b>Location</b></td><td>Somewhere you <b>are</b> — or somewhere that only the designated person is</td></tr>
  </table>
</div>

<div class="trap">
  <span class="tag">Corrected &mdash; one word in this list is wrong</span>
  The material prints <b>&ldquo;Inheritance&rdquo;</b>. The correct English term for <i>something you are</i> is <b>INHERENCE</b>. <i>Inheritance</i> means receiving property from a predecessor, which is unrelated. The word appears <b>nowhere in Sharp's book</b>, so this came in with the second source.
  <p style="margin:2.5mm 0 0 0"><b>In the exam:</b> her four words are Knowledge, Possession, Inheritance, Location — and the count of four is what she marked. If there is room, write <b>&ldquo;inherence (something you are)&rdquo;</b>. It shows the correct term without contradicting her.</p>
</div>

<div class="trap">
  <span class="tag">Two more traps in this table</span>
  <ul class="tight" style="margin-bottom:0">
    <li><b>There are four factors, not three.</b> Most students remember knowledge, possession and &ldquo;something you are&rdquo; — and drop <b>Location</b>.</li>
    <li>The standard security literature treats the <b>core</b> set as three (knowledge, possession, inherence) and <b>location</b> as an extension. So the material's four is defensible, but it is not the universal count.</li>
  </ul>
</div>
""")

S4_5 = page(23, '<span class="num">4.5</span>Authentication technologies', """
<p class="lead">Four physical technologies are described, in increasing order of data security.</p>

<h2>Magnetic stripe readers</h2>
<p>A magnetic stripe card is a physical credit-card-like device that contains authentication information in the form of <b>magnetically coded spots on a magnetic stripe</b>.</p>

<h2>Smart cards</h2>
<p>Also credit-card-like and often resembling magnetic stripe cards, but they offer <b>improved data security</b> due to the presence of <b>intelligent circuitry</b> that can be used to <b>hide the user's data until an authentication process has been performed</b>.</p>

<h2>RFID badges</h2>
<p><b>Radio Frequency Identification</b> badges provide <b>hands-free</b> access-control tools that improve on the <b>bar code, magnetic stripe and proximity reader</b> technologies. The RFID system employs <b>radio signals</b> to identify unique items using an <b>RFID reader device</b> and <b>RFID tags</b>.</p>

<h2>Biometric scanners</h2>
<p><b>Biometrics</b> is the term used to describe access-control mechanisms that use <b>human physical characteristics</b> to verify individual identities.</p>

<div class="key">
  <span class="tag">The four compared</span>
  <table style="margin:0">
    <tr><th style="width:26%">Technology</th><th>Its distinguishing feature</th></tr>
    <tr><td><b>Magnetic stripe</b></td><td>Authentication data as <b>magnetically coded spots</b> on a stripe</td></tr>
    <tr><td><b>Smart card</b></td><td><b>Intelligent circuitry</b> hides the user's data <b>until authentication succeeds</b> — the reason it is more secure</td></tr>
    <tr><td><b>RFID badge</b></td><td><b>Hands-free</b>; radio signals; improves on bar code, magnetic stripe and proximity readers</td></tr>
    <tr><td><b>Biometric</b></td><td>Verifies identity from <b>human physical characteristics</b></td></tr>
  </table>
</div>

<div class="trap">
  <span class="tag">Likely question</span>
  <b>Why is a smart card more secure than a magnetic stripe card?</b> Because of the <b>intelligent circuitry</b> that conceals the user's data <b>until the authentication process has been carried out</b>. A stripe simply stores the data and gives it up on read.
</div>
""")

S4_6 = page(24, '<span class="num">4.6</span>Remote monitoring and automated access control', """
<h2>Remote-access monitoring</h2>
<div class="def">
  <span class="tag">Definition</span>
  Monitoring or measuring devices <b>from a remote location or control room</b>. In the security realm, this involves having <b>external access to the security system through a communication system</b>.
</div>

<h2>Automated access-control systems</h2>
<p>These add another dimension to standard security monitoring and reporting. Note the qualification the material makes: automated access control is <b>not an integral part</b> of the typical intrusion-detection and monitoring system — but it <b>adds to the safety and convenience</b> of perimeter-access control.</p>

<p>They come in two flavours:</p>

<table>
  <tr><th style="width:32%">Type</th><th>What it does</th></tr>
  <tr>
    <td><b>Remote-access-control systems</b></td>
    <td>Manages entry to protected areas by <b>authenticating the identity of persons entering a secured area</b> — a security zone or computer system — using an authentication system <b>located in a different location than the access point</b></td>
  </tr>
  <tr>
    <td><b>Remote-control access systems</b></td>
    <td>Works with remote monitoring systems to <b>monitor, control and supervise doors, gates and conveyances from a distance</b></td>
  </tr>
</table>

<div class="key">
  <span class="tag">Three similar names &mdash; keep them apart</span>
  <table style="margin:0">
    <tr><th style="width:34%">Term</th><th>The key idea</th></tr>
    <tr><td>Remote-access <b>monitoring</b></td><td><b>Watching and measuring</b> devices from a remote location or control room</td></tr>
    <tr><td>Remote-<b>access control</b></td><td><b>Managing entry</b> by authenticating from a <b>different location than the access point</b></td></tr>
    <tr><td>Remote-<b>control access</b></td><td><b>Operating</b> doors, gates and conveyances at a distance, together with remote monitoring</td></tr>
  </table>
</div>

<div class="trap">
  <span class="tag">Exam trap</span>
  The three names differ only in word order. Read the question carefully:
  <b>monitoring</b> = observe · <b>remote-access control</b> = authenticate remotely · <b>remote-control access</b> = operate remotely.
</div>
""")

S4_7 = page(25, '<span class="num">4.7</span>The NIST material', """
<div class="trap">
  <span class="tag">Read once and move on &mdash; this section carries no marking</span>
  These two blocks have <b>no highlight and no colour</b> in the doctor's copy, and the student's own assessment was that they are <b>not important</b>. They are recorded here for completeness only.
</div>

<h2>Develop a risk-management program</h2>
<ul>
  <li>Determine the risks of <b>losing control of a host</b>.</li>
  <li>Identify potential adversarial activities that could target your domain — for example, are they targeting <b>intellectual property</b>?</li>
  <li>Present a <b>risk-informed report</b> so the organisation recognises the risks and provides support and buy-in to resolve, reduce or prevent risks of loss.</li>
</ul>

<h2>Use NIST security controls</h2>
<ul>
  <li>Create a <b>matrix of individual concerns and associated attack vectors</b>.</li>
  <li>Provide <b>mitigation method(s) for each</b>.</li>
  <li>Select the appropriate <b>NIST family</b> — <b>Management</b>, <b>Operational</b>, <b>Technical</b> — of security controls to be implemented, referencing <b>NIST SP 800-53</b>.</li>
  <li>Ensure the reasons for selection are <b>commensurate to the risks</b>. The selection of low-, medium- and high-level implementations should be described in the guidance and should help ensure a <b>cost-effective</b> solution.</li>
  <li><b>&ldquo;Don't overprescribe controls!&rdquo;</b></li>
</ul>

<h2>The NIST Framework stakeholders — create a policy for assessments</h2>
<ul>
  <li>Define the environment.</li>
  <li>Determine organisational priorities for protecting company property and materials.</li>
  <li>Ensure senior management is supportive.</li>
  <li>Procedurally define a process and diligence to form an informative assessment outcome.</li>
</ul>

<div class="key">
  <span class="tag">If it does come up, the two facts worth having</span>
  <ul class="tight" style="margin-bottom:0">
    <li>The three <b>NIST control families</b>: <b>Management · Operational · Technical</b>.</li>
    <li>The reference for the controls: <b>NIST SP 800-53</b>.</li>
  </ul>
</div>
""")

S4_8 = page(26, '<span class="num">4.8</span>Cyber risk assessment and management', """
<div class="def">
  <span class="tag">Definition</span>
  <b>Cyber risk assessment and management</b> is the process of <b>identifying, evaluating and mitigating</b> the risks associated with cyber threats to an organisation or system. It involves understanding the <b>potential vulnerabilities in a system</b>, the <b>likelihood of cyberattacks</b>, and the <b>impact</b> such attacks could have on the organisation's <b>operations, reputation and data security</b>.
</div>

<h2>The four key components &mdash; in order</h2>
<div class="key">
  <span class="tag">Learn the sequence</span>
  <table style="margin:0">
    <tr><th class="c" style="width:8%">#</th><th style="width:26%">Component</th><th>What it involves</th></tr>
    <tr><td class="c"><b>1</b></td><td><b>Risk Identification</b></td><td>Pinpointing potential cyber threats — malware, phishing, ransomware, data breaches, and so on</td></tr>
    <tr><td class="c"><b>2</b></td><td><b>Risk Evaluation</b></td><td>Analysing the likelihood of each risk materialising and the severity of its potential impact</td></tr>
    <tr><td class="c"><b>3</b></td><td><b>Risk Mitigation</b></td><td>Developing strategies to reduce or manage the risks — implementing controls such as <b>firewalls, encryption, user education and backup systems</b></td></tr>
    <tr><td class="c"><b>4</b></td><td><b>Monitoring and Review</b></td><td>Continuously observing the cyber landscape, updating defences, and reassessing risks as new threats emerge</td></tr>
  </table>
</div>

<h2>Why it matters</h2>
<ul>
  <li>As technology advances, cyber threats become more complex, making risk management essential for <b>protecting sensitive data</b> and ensuring the <b>continuity of business operations</b>.</li>
  <li>Standards and frameworks such as <b>ISO 27001</b>, the <b>NIST Cybersecurity Framework</b>, and country-specific guidelines — for example from the <b>UK's National Cyber Security Centre</b> — provide structured approaches.</li>
</ul>

<p><b>The outcome:</b> by properly conducting cyber risk assessments and management, organisations can <b>improve their resilience against attacks</b> and better prepare for the inevitable challenges of the digital landscape.</p>

<div class="key">
  <span class="tag">Note the overlap with §3.9</span>
  Component <b>3, Risk Mitigation</b>, is the same idea as the risk mitigation of §3.9 — the part of risk management aiming to reduce risk to an acceptable level. Here it is given the concrete controls: firewalls, encryption, user education, backups.
</div>
""")

# ----------------------------------------------------------------------------
# 5-7
# ----------------------------------------------------------------------------

S5 = page(27, '<span class="num">5</span>Exam traps and formula card', """
<h2>Formula card</h2>
<table>
  <tr><th style="width:22%">Equation</th><th style="width:34%">Meaning</th><th>Symbols</th></tr>
  <tr>
    <td class="c"><b>S = F &times; K</b></td>
    <td>Basic risk of a threat</td>
    <td><b>S</b> basic risk · <b>F</b> frequency of attempts to exploit the vulnerability · <b>K</b> consequences of a successful attempt</td>
  </tr>
  <tr>
    <td class="c"><b>R = S / M</b></td>
    <td>Residual risk after countermeasures</td>
    <td><b>R</b> residual risk · <b>S</b> risk of the threat · <b>M</b> level of countermeasures — <b>number AND effectiveness</b></td>
  </tr>
</table>
<div class="note">
  <span class="tag">How to use them</span>
  The scale is <b>ordinal</b> (low / medium / high), and the book's own examples print <b>&ldquo;medium &times; high = medium&rdquo;</b>. So read the answer off <b>Figure 3.2</b> or <b>Figure 3.3</b> — do not multiply the words as numbers.
</div>

<h2>The numbers to remember</h2>
<table>
  <tr><th style="width:16%">Count</th><th>What</th></tr>
  <tr><td class="c"><b>2</b></td><td>Equations</td></tr>
  <tr><td class="c"><b>4</b></td><td>Threat groups — hardware · software · data · liveware</td></tr>
  <tr><td class="c"><b>5</b></td><td>Risk mitigation strategies — avoidance · reduction · retention · transfer · sharing</td></tr>
  <tr><td class="c"><b>5</b></td><td>Analysis frameworks — COBIT · COSO · FAIR · ISO/IEC 27002 · OCTAVE</td></tr>
  <tr><td class="c"><b>5</b></td><td>Steps for dealing with damage — preventing · complicating · diverting · detecting · reestablishing</td></tr>
  <tr><td class="c"><b>14</b></td><td>ISO/IEC 27002 categories <span class="small">(the 2013 structure; 2022 is 4 themes / 93 controls)</span></td></tr>
  <tr><td class="c"><b>3</b></td><td>OCTAVE phases</td></tr>
  <tr><td class="c"><b>4</b></td><td>OCTAVE variants as listed in the book <span class="small">(3 exist publicly)</span></td></tr>
  <tr><td class="c"><b>4</b></td><td>PDCA elements — plan · do · check · act</td></tr>
  <tr><td class="c"><b>4</b></td><td>Authentication factors — knowledge · possession · inheritance/inherence · location</td></tr>
  <tr><td class="c"><b>4</b></td><td>Cyber risk assessment components — identification · evaluation · mitigation · monitoring</td></tr>
</table>

<h2>Traps, in the order you will meet them</h2>
<ol>
  <li><b>Fuzzification is input, defuzzification is output</b> — carry-over from Week 01.</li>
  <li><b>A threat is not a vulnerability.</b> Weakness alone = vulnerability. Actor alone = threat.</li>
  <li><b>Multiplication, not addition.</b> Both factors must matter.</li>
  <li><b>Red has exactly one cell in each matrix.</b> (high, high) for risk; (high risk, low countermeasures) for residual risk.</li>
  <li><b>Do not mix the two matrices.</b> Risk matrix: frequency &times; consequences. Residual risk matrix: risk &divide; countermeasures.</li>
  <li><b>M is number AND effectiveness</b> — not just a count.</li>
  <li><b>The two five-item lists are different.</b> Dealing with damage (preventing…reestablishing) versus mitigation strategies (avoidance…sharing).</li>
  <li><b>Proactive 1–2–3, reactive 4–5</b> in the damage list.</li>
  <li><b>Act restarts PDCA</b> — it is a cycle, not a line.</li>
  <li><b>OCTAVE phases = 3; OCTAVE variants = 4 in the book.</b></li>
  <li><b>14 categories</b> — and know that they are the 2013 structure.</li>
  <li><b>Authentication factors = 4</b>, and the third is <i>inherence</i>, not <i>inheritance</i>.</li>
  <li><b>Authorisation is based on authentication.</b></li>
  <li><b>Insider threats are met with administrative controls</b> — vetting and training, not technology.</li>
  <li><b>Three remote terms differ by word order</b> — monitoring · remote-access control · remote-control access.</li>
</ol>
""")

S6 = page(28, '<span class="num">6</span>Glossary', """
<table>
  <tr><th style="width:30%">Term</th><th>Meaning</th></tr>
  <tr><td><b>Risk</b> (technical sense)</td><td>The quantitative probability that an error situation occurs and gives rise to damage. Damage = a breach of the security policy</td></tr>
  <tr><td><b>Objective risk</b></td><td>Risk as a property of the system, independent of opinion</td></tr>
  <tr><td><b>Subjective risk</b></td><td>Risk as perceived, shaped by attitudes, trust and personality</td></tr>
  <tr><td><b>Threat</b></td><td>An actor or event that can realise damage against a weakness</td></tr>
  <tr><td><b>Vulnerability</b></td><td>A weakness which can be exploited to damage the system</td></tr>
  <tr><td><b>Damage</b></td><td>A breach of the security policy</td></tr>
  <tr><td><b>Basic risk (S)</b></td><td>Frequency of attempts &times; consequences of a successful attempt</td></tr>
  <tr><td><b>Residual risk (R)</b></td><td>The risk remaining after countermeasures; risk divided by the level of countermeasures</td></tr>
  <tr><td><b>Countermeasure / control (M)</b></td><td>A measure protecting against a threat. Covers number <b>and</b> effectiveness</td></tr>
  <tr><td><b>Risk matrix</b></td><td>Grid placing threats by frequency and consequences</td></tr>
  <tr><td><b>Residual risk matrix</b></td><td>Grid placing threats by risk and level of countermeasures</td></tr>
  <tr><td><b>Inference</b></td><td>Deducing confidential information from data that is accessible</td></tr>
  <tr><td><b>Masquerading</b></td><td>Pretending to be someone else</td></tr>
  <tr><td><b>Liveware-related threat</b></td><td>A threat from human error among the computer's users</td></tr>
  <tr><td><b>Malware</b></td><td>Viruses, worms, trojan horses, logic bombs</td></tr>
  <tr><td><b>Risk management</b></td><td>All activities related to evaluating and reducing risks</td></tr>
  <tr><td><b>Risk mitigation</b></td><td>The part of risk management aiming to reduce risk to an acceptable level</td></tr>
  <tr><td><b>PDCA</b></td><td>Plan · Do · Check · Act — the cyclic form risk management takes</td></tr>
  <tr><td><b>Authentication</b></td><td>Determining that someone is who they say they are</td></tr>
  <tr><td><b>Authorisation</b></td><td>What an authenticated party is permitted to do. Based on authentication</td></tr>
  <tr><td><b>Ingress / egress / regress</b></td><td>Entry / exit / return</td></tr>
  <tr><td><b>Inherence</b></td><td>Something you are. Printed as &ldquo;inheritance&rdquo; in the material</td></tr>
  <tr><td><b>Biometrics</b></td><td>Access control using human physical characteristics</td></tr>
</table>
""")

S7 = page(29, '<span class="num">7</span>Sources and verification notes', """
<h2>Primary source</h2>
<div class="def">
  <span class="tag">Citation</span>
  [Sharp, R., &ldquo;Risk&rdquo;, in <i>Introduction to Cybersecurity: A Multidisciplinary Challenge</i>, Undergraduate Topics in Computer Science, Springer, Cham, 2023, pp. 37–56](https://doi.org/10.1007/978-3-031-41463-3_3)
  <p style="margin:2mm 0 0 0" class="small">Whole book: [Sharp, R., <i>Introduction to Cybersecurity: A Multidisciplinary Challenge</i>, Springer, Cham, 2023, 442 pp.](https://doi.org/10.1007/978-3-031-41463-3) · ISBN 978-3-031-41463-3</p>
</div>

<h2>Second source</h2>
<p><b>Not identified.</b> The physical-security, authentication and NIST material (§4.1–4.8) does not appear anywhere in Sharp's 452 pages. Four targeted searches failed to find it; its text is not publicly indexed. One term in it — <i>inheritance</i> — is not used by any published source for &ldquo;something you are&rdquo;.</p>

<h2>What was verified, and how</h2>
<table>
  <tr><th style="width:38%">Claim</th><th style="width:14%">Verdict</th><th>Basis</th></tr>
  <tr><td>S = F &times; K</td><td class="c"><b>confirmed</b></td><td>Read verbatim from Sharp p. 38</td></tr>
  <tr><td>R = S / M, with M = number + effectiveness</td><td class="c"><b>confirmed</b></td><td>Read verbatim from Sharp p. 39</td></tr>
  <tr><td>The five mitigation strategies, in order</td><td class="c"><b>confirmed</b></td><td>Sharp p. 42, Definition 3.1</td></tr>
  <tr><td>The three OCTAVE phases</td><td class="c"><b>confirmed</b></td><td>Sharp p. 46; matches the published OCTAVE method</td></tr>
  <tr><td>PDCA, four elements</td><td class="c"><b>confirmed</b></td><td>Sharp p. 53</td></tr>
  <tr><td>The four threat groups, including &ldquo;liveware&rdquo;</td><td class="c"><b>confirmed</b></td><td>Sharp p. 40</td></tr>
  <tr><td>&ldquo;ISO/IEC 27002 from <b>2022</b> … 14 categories&rdquo;</td><td class="c" style="background:#ffe3e3"><b>wrong</b></td><td>The 14 categories are the <b>2013</b> structure (114 controls in 14 clauses). 2022 is <b>4 themes / 93 controls</b>. The sentence is Sharp's own, p. 45 — the booklet reproduces it faithfully</td></tr>
  <tr><td>&ldquo;OCTAVE FORTE&rdquo; as a fourth variant</td><td class="c" style="background:#fff5e6"><b>book only</b></td><td>Present in Sharp p. 46 with no description and a garbled sentence. No public OCTAVE source names it — only three methodologies are documented</td></tr>
  <tr><td>Authentication factor &ldquo;<b>Inheritance</b>&rdquo;</td><td class="c" style="background:#ffe3e3"><b>wrong term</b></td><td>The standard term is <b>Inherence</b>. The word appears nowhere in Sharp</td></tr>
  <tr><td>OCTAVE developed &ldquo;for CERT&rdquo;</td><td class="c" style="background:#fff5e6"><b>imprecise</b></td><td>Developed at Carnegie Mellon University in 2001 <b>for the US Department of Defense</b>; CERT/SEI is the CMU body</td></tr>
</table>

<h2>Figures</h2>
<p>All figures are the book's own, extracted from its typeset PDF: <b>3.1</b> (p. 38), <b>3.2</b> (p. 38), <b>3.3</b> (p. 39), <b>3.9</b> (p. 52), <b>3.10</b> (p. 53), <b>3.11</b> (p. 54). The Word booklet the doctor distributed contains <b>no images at all</b>, so none of these were available in it.</p>
<p class="small">Figure 3.1 photograph: Terry Goss, Wikimedia Commons, file <i>White_shark.jpg</i>, licence <b>CC-BY 2.5 Generic</b>. Attribution required on reuse.</p>

<h2>Content recovered from the book that the Word booklet had dropped</h2>
<ul>
  <li>The <b>five-step list for dealing with damaging events</b> (§3.8)</li>
  <li>The <b>security / functionality / usability</b> balance (§3.9)</li>
  <li>The <b>Danish 2009 survey</b> on objective versus subjective risk (§3.1)</li>
  <li>The book's <b>Table 3.1</b>, distinguishing ISO/IEC 27001 from 27002 (§3.11)</li>
  <li>All figures and both worked-example matrices (§3.14)</li>
</ul>

<hr class="soft"/>
<p class="small">Booklet built 2026-09-23. English only, per the student's instruction. Every claim traced to a named source; nothing asserted without one. Where the source is wrong, the error is stated rather than silently corrected.</p>
""")

BODY_SECTIONS = [S1, S2, S3_1, S3_2, S3_3, S3_4, S3_5, S3_6, S3_7, S3_8, S3_9, S3_10,
                 S3_11, S3_12, S3_13, S3_14, S4_1, S4_2, S4_3, S4_4, S4_5, S4_6, S4_7, S4_8,
                 S5, S6, S7]


def build_html(pm):
    parts = [COVER, toc_html(pm)] + BODY_SECTIONS
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n'
        '<title>Cybersecurity Risks and Threats - Week 02 Booklet</title>\n'
        '<style>\n' + CSS + '\n</style>\n</head>\n<body>\n'
        + '\n'.join(parts) + '\n</body>\n</html>\n'
    )


if __name__ == "__main__":
    import json
    import sys

    pagemap = {}
    if len(sys.argv) > 1:
        pagemap = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    doc = build_html(pagemap)
    HTML_OUT.write_text(doc, encoding="utf-8")
    print(f"Wrote {HTML_OUT} ({HTML_OUT.stat().st_size} bytes)")
    print(f"Sections: {len(BODY_SECTIONS)}  pagemap entries: {len(pagemap)}")
