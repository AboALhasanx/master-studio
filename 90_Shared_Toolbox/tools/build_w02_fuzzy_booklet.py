# -*- coding: utf-8 -*-
"""Build English-only Soft Computing W02 Fuzzy Logic Systems booklet (HTML → PDF).

Strategy (student request): draft by topic parts, then merge into one booklet.
Math source of truth: W02_Fuzzy_Math_Vision_Verified.md (never OCR).
Source extraction MD files are left untouched.
"""
from pathlib import Path
import re

OUT = Path(r"G:\My Drive\Master-Studio\01_Semester_1\05_Soft_Computing\03_Study_Notes")
HTML = OUT / "w02-fuzzy-logic-systems-booklet.html"
PDF = OUT / "w02-fuzzy-logic-systems-booklet.pdf"

CSS = """
@page { size: A4; margin: 15mm 13mm 14mm; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; }
body {
  font-family: "Segoe UI", Tahoma, Arial, sans-serif;
  color:#1c2430; font-size:10.2pt; line-height:1.48; background:#fff;
}
.page {
  page-break-after: always;
  position: relative;
  min-height: 255mm;
  padding-bottom: 10mm;
}
.page:last-child { page-break-after: auto; }
.cover { text-align:center; padding-top: 38mm; min-height: 255mm; }
.cover .school { letter-spacing:.14em; font-size:9.5pt; color:#5a6a7a; text-transform:uppercase; }
.cover h1 { font-size:26pt; margin:8mm 0 2mm; color:#0b3d5c; font-weight:650; letter-spacing:-0.3pt; }
.cover .sub { font-size:13.5pt; color:#0f6b6b; margin-bottom:3mm; font-weight:600; }
.cover .tag { display:inline-block; background:#0b3d5c; color:#fff; padding:2mm 5mm; border-radius:999px; font-size:9pt; letter-spacing:.06em; margin-bottom:6mm; }
.cover .rule { width:48mm; height:2px; background:#0b3d5c; margin:5mm auto; }
.cover .meta { font-size:10.5pt; color:#2a3540; margin-top:10mm; line-height:1.7; text-align:left; display:inline-block; }
.cover .note { margin-top:14mm; font-size:9pt; color:#667; }
h1.sec {
  font-size:15pt; color:#0b3d5c; border-bottom:2px solid #0b3d5c;
  padding-bottom:1.8mm; margin:0 0 4mm; font-weight:650;
}
h1.sec .pn { float:right; font-size:9.5pt; color:#6b7c8c; font-weight:500; padding-top:3pt; }
h2 { font-size:11.5pt; color:#0f4c75; margin:4mm 0 1.5mm; font-weight:650; }
h3 { font-size:10.5pt; color:#1b6b6b; margin:3mm 0 1mm; font-weight:650; }
p { margin:0 0 2.2mm; text-align:justify; }
ul, ol { margin:0 0 2.5mm 5mm; padding-left:4mm; }
li { margin-bottom:1mm; }
table { width:100%; border-collapse:collapse; margin:2.5mm 0 3.5mm; font-size:9.2pt; }
th { background:#0b3d5c; color:#fff; padding:1.8mm 2mm; text-align:left; font-weight:600; }
td { border:0.4pt solid #c2ced8; padding:1.7mm 2mm; vertical-align:top; }
tr:nth-child(even) td { background:#f5f8fb; }
.formula {
  text-align:center; margin:3mm 0; padding:2.5mm 3mm;
  background:#f7fafc; border-left:3px solid #0f4c75;
  font-size:11.5pt;
}
.formula-row { display:flex; gap:4mm; margin:2.5mm 0; }
.formula-row .formula { flex:1; }
.def {
  border:0.6pt solid #0f4c75; background:#eef6fb; padding:2.5mm 3.5mm;
  margin:2.5mm 0 3.5mm; border-radius:2mm;
}
.def b.tag { color:#0b3d5c; }
.trap {
  border-left:3px solid #b35c00; background:#fff8ee;
  padding:2.2mm 3mm; margin:2.5mm 0; font-size:9.6pt;
}
.trap b { color:#8a4b00; }
.ex {
  border-left:3px solid #0f6b6b; background:#f2fbfa;
  padding:2.2mm 3mm; margin:2.5mm 0; font-size:9.6pt;
}
.ex b { color:#0f5c5c; }
.figbox {
  border:0.5pt solid #c5d0d8; background:#fafcfd; padding:3mm;
  margin:2.5mm 0; text-align:center;
}
.foot {
  position:absolute; bottom:0; left:0; right:0;
  font-size:7.8pt; color:#8a96a3; text-align:center;
  border-top:0.4pt solid #e2e8ee; padding-top:1.2mm;
}
.toc td { border:none; padding:1.1mm 0; font-size:9.8pt; }
.toc td:first-child { width:14mm; color:#0b3d5c; font-weight:650; }
.small { font-size:8.8pt; color:#5a6570; }
.pipeline {
  display:flex; align-items:center; justify-content:center; gap:0;
  margin:6mm 0 4mm; flex-wrap:nowrap;
}
.pipe-node {
  border:1.5pt solid #0b3d5c; background:#eef6fb; color:#0b3d5c;
  padding:3mm 2.5mm; border-radius:2mm; min-width:28mm;
  font-size:8.8pt; font-weight:650; text-align:center; line-height:1.25;
}
.pipe-node.dark { background:#0b3d5c; color:#fff; }
.pipe-arrow { color:#0f6b6b; font-size:14pt; padding:0 1.2mm; font-weight:700; }
.pipe-label {
  text-align:center; font-size:8.5pt; color:#5a6570;
  margin:1mm 0 4mm; letter-spacing:.02em;
}
.two-col { display:flex; gap:4mm; }
.two-col > div { flex:1; }
.kv { width:100%; border-collapse:collapse; font-size:9.2pt; }
.kv td { border:0.4pt solid #c2ced8; padding:1.6mm 2mm; }
.kv td:first-child { width:32%; background:#f0f5f9; font-weight:600; color:#0b3d5c; }
.center { text-align:center; }
.tight p, .tight li { margin-bottom:1mm; }
.laws-grid { display:grid; grid-template-columns:1fr 1fr; gap:2.5mm; margin:2mm 0 3mm; }
.law-card {
  border:0.5pt solid #c2ced8; border-radius:2mm; padding:2.2mm 2.5mm;
  background:#fbfcfe;
}
.law-card .t { font-weight:650; color:#0b3d5c; font-size:9.2pt; margin-bottom:1.2mm; }
.law-card .f { font-size:10.5pt; text-align:center; margin-top:1mm; }
.chip {
  display:inline-block; background:#eef6fb; color:#0b3d5c; border:0.4pt solid #b7c9d8;
  border-radius:999px; padding:0.4mm 2.2mm; font-size:8.2pt; margin:0.3mm;
}
"""


def page(n, title, body, extra_class=""):
    foot = f'<div class="foot">W02 · Fuzzy Logic Systems · Soft Computing &nbsp;·&nbsp; {n}</div>'
    return (
        f'<section class="page {extra_class}">'
        f'<h1 class="sec">{title}<span class="pn">{n}</span></h1>'
        f"{body}{foot}</section>"
    )


def cover():
    return """
<section class="cover page">
  <div class="school">University of Wasit · College of Computer Science &amp; Information Technology</div>
  <h1>Fuzzy Logic Systems</h1>
  <div class="sub">Soft Computing — Week 02 Study Booklet</div>
  <div class="tag">ENGLISH EDITION · VISION-VERIFIED MATH</div>
  <div class="rule"></div>
  <div class="meta">
    <div><b>Instructor:</b> Prof. Dr. Abdul Hadi Mohammed Alaidi / Adkhil</div>
    <div><b>Course:</b> Soft Computing · Fall 2026</div>
    <div><b>Scope:</b> Fuzzy Logic motivation &amp; architecture · Crisp/Classical Set Theory · Fuzzy Sets &amp; Membership Functions</div>
    <div><b>Math source:</b> Vision-verified booklet pages (W02_Fuzzy_Math_Vision_Verified.md)</div>
    <div><b>Notation:</b> &phi; = empty set · X / U = universe · &mu;:&nbsp;X&nbsp;&rarr;&nbsp;[0,&nbsp;1] · membership is <b>not</b> probability</div>
    <div><b>Language:</b> English only · equations typeset in LaTeX (MathJax)</div>
  </div>
  <div class="note">Source booklet: W02_Fuzzy_Logic_Systems.pdf (pp. 1–66) · extraction Markdown preserved as-is<br/>
  Condensed study booklet (~28 pages) · Koko · 2026-09-22</div>
  <div class="foot">W02 · Fuzzy Logic Systems · Soft Computing · Booklet</div>
</section>
"""


def part_toc():
    body = """
<p>This booklet reconstructs Week&nbsp;02 as one coherent argument: exact sets first, then gradual membership. Source pages are marked beside formulas. Math symbols follow the booklet’s own notation (vision-verified).</p>
<table class="toc">
  <tr><td>1</td><td>Scope, learning outcomes, terminology map</td></tr>
  <tr><td>2</td><td>Why Fuzzy Logic exists — imprecision, noise, acceptable reasoning</td></tr>
  <tr><td>3</td><td>Fuzzy Logic System architecture (pipeline)</td></tr>
  <tr><td>4</td><td>Rule Base and linguistic IF–THEN rules</td></tr>
  <tr><td>5</td><td>Fuzzification · Inference Engine · Defuzzification</td></tr>
  <tr><td>6</td><td>Crisp versus fuzzy — intuitive comparison</td></tr>
  <tr><td>7</td><td>Membership: binary versus graded</td></tr>
  <tr><td>8–11</td><td>Classical set theory — definition, notation, types</td></tr>
  <tr><td>12–14</td><td>Set operations — union, intersection, difference, complement, Cartesian product</td></tr>
  <tr><td>15–17</td><td>Classical-set laws and De Morgan’s Law</td></tr>
  <tr><td>18</td><td>Home tasks (active recall)</td></tr>
  <tr><td>19–20</td><td>Why crisp sets fail · classical vs fuzzy matrix</td></tr>
  <tr><td>21–23</td><td>Fuzzy-set definition · membership function · not probability</td></tr>
  <tr><td>24–25</td><td>Alternative notation (discrete &amp; continuous)</td></tr>
  <tr><td>26–27</td><td>Representation of a fuzzy set — discrete &amp; continuous cases</td></tr>
  <tr><td>28</td><td>Exam traps, formula sheet, glossary</td></tr>
</table>
<h2>Learning outcomes</h2>
<ul>
  <li>Explain why fuzzy logic targets <b>acceptable</b> reasoning under imprecision.</li>
  <li>Draw and label the four-stage Fuzzy Logic System pipeline.</li>
  <li>Distinguish fuzzification (input) from defuzzification (output).</li>
  <li>Compute classical set operations and state the standard laws.</li>
  <li>Define a fuzzy set by membership function and ordered pairs.</li>
  <li>Write discrete and continuous fuzzy-set notation without treating <code>/</code> as division.</li>
</ul>
"""
    return page(1, "Scope &amp; Learning Outcomes", body)


def part_motivation():
    body = """
<div class="def">
  <b class="tag">Core idea (source pp. 2–3)</b>
  <p style="margin-top:1.5mm">Fuzzy Logic is designed to produce <b>acceptable reasoning</b> under imprecision and uncertainty — not necessarily perfectly exact reasoning. It embodies human-like thinking into a control system and can emulate human deductive thinking (inferring conclusions from what people know).</p>
</div>
<h2>Why fuzzy systems are built</h2>
<ul>
  <li><b>Any input quality:</b> works with imprecise, distorted, or noisy input information.</li>
  <li><b>Simple construction:</b> easy to build and understand; algorithms can be described with little data (low memory).</li>
  <li><b>Mathematical base:</b> grounded in set theory; the reasoning itself is simple.</li>
  <li><b>Human-like decisions:</b> resembles human reasoning and decision making in complex situations.</li>
  <li><b>Uncertainty:</b> uncertainties can be handled with the help of fuzzy logic.</li>
</ul>
<h2>Central progression of Week 02</h2>
<div class="figbox">
  Real-world imprecision / noise
  &nbsp;&rarr;&nbsp; Human-like linguistic reasoning
  &nbsp;&rarr;&nbsp; Fuzzy Logic System
  &nbsp;&rarr;&nbsp; Fuzzification &rarr; Rule Base + Inference &rarr; Defuzzification
  &nbsp;&rarr;&nbsp; Crisp control / output value
</div>
<p class="small">Mathematical bridge: classical sets define exact membership; fuzzy sets relax membership from {0,&nbsp;1} to the continuous interval [0,&nbsp;1].</p>
"""
    return page(2, "Why Fuzzy Logic Exists", body)


def part_architecture():
    body = """
<p>A Fuzzy Logic System converts crisp sensor readings into linguistic grades, reasons with expert rules, then converts the result back into a usable crisp control value <span class="small">(source p. 4 architecture; components pp. 5–6)</span>.</p>
<div class="pipeline">
  <div class="pipe-node">INPUT<br/>crisp values</div>
  <div class="pipe-arrow">&rarr;</div>
  <div class="pipe-node dark">FUZZIFIER</div>
  <div class="pipe-arrow">&rarr;</div>
  <div class="pipe-node">RULE BASE</div>
  <div class="pipe-arrow">+</div>
  <div class="pipe-node dark">INFERENCE<br/>ENGINE</div>
  <div class="pipe-arrow">&rarr;</div>
  <div class="pipe-node">DEFUZZIFIER</div>
  <div class="pipe-arrow">&rarr;</div>
  <div class="pipe-node">OUTPUT<br/>crisp value</div>
</div>
<div class="pipe-label">Crisp input → membership grades → fired linguistic rules → combined action → crisp control</div>
<table>
  <tr><th>Component</th><th>Role</th><th>Direction</th></tr>
  <tr><td><b>Rule Base</b></td><td>Expert IF–THEN linguistic rules that govern decision making.</td><td>knowledge store</td></tr>
  <tr><td><b>Fuzzifier</b> (Fuzzification)</td><td>Converts crisp numbers into fuzzy sets / membership degrees.</td><td>input conversion</td></tr>
  <tr><td><b>Inference Engine</b></td><td>Matches current fuzzy input to each rule; fires rules; combines control actions.</td><td>reasoning</td></tr>
  <tr><td><b>Defuzzifier</b> (Defuzzification)</td><td>Converts the inferred fuzzy set into a crisp output value.</td><td>output conversion</td></tr>
</table>
<div class="trap"><b>Exam trap — do not swap directions.</b> Fuzzification is <b>input</b> conversion (crisp → fuzzy). Defuzzification is <b>output</b> conversion (fuzzy → crisp).</div>
"""
    return page(3, "Fuzzy Logic Architecture", body)


def part_rule_base():
    body = """
<div class="def">
  <b class="tag">Rule Base (source p. 5)</b>
  <p style="margin-top:1.5mm">Contains the set of rules and the IF–THEN conditions provided by <b>experts</b> to govern the decision-making system, on the basis of <b>linguistic information</b>. Recent fuzzy theory offers methods for design and tuning of fuzzy controllers; most reduce the number of fuzzy rules.</p>
</div>
<h2>Linguistic IF–THEN form</h2>
<div class="formula">IF &nbsp;<i>antecedent</i>&nbsp; THEN &nbsp;<i>consequent</i></div>
<div class="ex">
  <b>Worked linguistic rule</b><br/>
  IF temperature is <b>high</b> THEN fan speed is <b>fast</b>.<br/>
  IF pressure is <b>low</b> THEN valve is <b>slightly open</b>.
</div>
<table>
  <tr><th>Part</th><th>Meaning</th><th>Typical content</th></tr>
  <tr><td>Antecedent</td><td>Condition on input linguistic terms</td><td>“temperature is high”</td></tr>
  <tr><td>Consequent</td><td>Action / output linguistic term</td><td>“fan speed is fast”</td></tr>
  <tr><td>Linguistic variable</td><td>Variable taking words as values</td><td>temperature, speed, age</td></tr>
  <tr><td>Linguistic value</td><td>Word / term (fuzzy set label)</td><td>high, fast, young, tall</td></tr>
</table>
<p>Rules are not Boolean switches. Each rule fires to a <b>degree</b> when the input matches its antecedent; several rules can fire together and are combined by the inference engine.</p>
<div class="trap"><b>Exam trap.</b> The Rule Base stores <b>linguistic</b> expert knowledge (IF–THEN), not raw sensor numbers. Sensors enter through fuzzification.</div>
"""
    return page(4, "Rule Base &amp; Linguistic Rules", body)


def part_components():
    body = """
<h2>Fuzzification (source p. 5)</h2>
<div class="def">
  <p style="margin:0">Converts <b>inputs</b> — crisp numbers — into <b>fuzzy sets</b>. Crisp inputs are the exact values measured by sensors and passed into the control system, such as temperature, pressure, rpm, etc.</p>
</div>
<div class="formula">\\(x \\mapsto \\mu_{\\tilde{A}}(x)\\) &nbsp;&nbsp;&nbsp; <span class="small">(the map from element to membership grade is called fuzzification)</span></div>
<h2>Inference Engine (source p. 6)</h2>
<div class="def">
  <p style="margin:0">Determines the <b>matching degree</b> of the current fuzzy input with respect to each rule, decides which rules are to be <b>fired</b>, then <b>combines</b> the fired rules to form the control actions.</p>
</div>
<h2>Defuzzification (source p. 6)</h2>
<div class="def">
  <p style="margin:0">Converts the fuzzy sets obtained by the inference engine into a <b>crisp value</b>. Several defuzzification methods exist; the best-suited one is used with a specific expert system to reduce error.</p>
</div>
<table>
  <tr><th>Stage</th><th>Converts</th><th>Example</th></tr>
  <tr><td>Fuzzification</td><td>crisp → fuzzy</td><td>32.5 °C → μ<sub>high</sub>(32.5) = 0.7</td></tr>
  <tr><td>Inference</td><td>fuzzy + rules → fired rules</td><td>combine “fan fast” degrees</td></tr>
  <tr><td>Defuzzification</td><td>fuzzy → crisp</td><td>output fan PWM = 180</td></tr>
</table>
<div class="trap"><b>Exam trap.</b> Fuzzification = <b>input</b> path. Defuzzification = <b>output</b> path. Never reverse them.</div>
"""
    return page(5, "Fuzzification · Inference · Defuzzification", body)


def part_crisp_vs_fuzzy():
    body = """
<div class="two-col">
<div>
<h2>Crisp / classical</h2>
<ul>
  <li>Employs <b>bi-valued</b> logic.</li>
  <li>Membership μ<sub>A</sub>(x) ∈ {0, 1}.</li>
  <li>Strict boundary: member or non-member.</li>
  <li>Historically tied to Boolean expert systems.</li>
</ul>
</div>
<div>
<h2>Fuzzy</h2>
<ul>
  <li>Implements <b>infinite-valued</b> logic.</li>
  <li>Membership grades in [0, 1].</li>
  <li>Vague boundary; partial belonging.</li>
  <li>Imitates human qualitative thinking.</li>
</ul>
</div>
</div>
<p>Scientists argued that human thinking does not always follow crisp “yes/no” logic; it can be vague, qualitative, uncertain, imprecise, or fuzzy. Fuzzy set theory was developed to imitate that style of thinking <span class="small">(source p. 7)</span>.</p>
<h2>Membership shape (source pp. 8–10, 52)</h2>
<div class="figbox">
<table style="max-width:95mm;margin:0 auto;font-family:Segoe UI,sans-serif">
<tr><th></th><th>Crisp step</th><th>Fuzzy curve</th></tr>
<tr><td>“Tall” at height h</td><td>μ = 0 below cut (e.g. 5′10″), μ = 1 above</td><td>μ rises gradually (e.g. 0.5 … 0.9 … 1.0)</td></tr>
<tr><td>Boundary</td><td>vertical jump</td><td>smooth / gradual</td></tr>
<tr><td>Age words</td><td>hard bins</td><td>young / middle-aged / old overlap</td></tr>
</table>
</div>
<div class="ex">
  <b>Tall-people comparison (source p. 52)</b><br/>
  Crisp set A: person is tall iff height ≥ 5′10″ (hard cut).<br/>
  Fuzzy set Ã: height 5′10″ → μ ≈ 0.5; 6′2″ → μ ≈ 0.9; higher → μ = 1.0 (graded curve).
</div>
"""
    return page(6, "Crisp vs Fuzzy — Intuition", body)


def part_membership_binary_graded():
    body = """
<div class="formula-row">
  <div class="formula">\\(\\mu_A(x) \\in \\{0, 1\\}\\) &nbsp;&nbsp;<span class="small">crisp / classical</span></div>
  <div class="formula">\\(\\mu_{\\tilde{A}}(x) \\in [0, 1]\\) &nbsp;&nbsp;<span class="small">fuzzy (0 and 1 inclusive)</span></div>
</div>
<table>
  <tr><th>Grade μ(x)</th><th>Meaning</th></tr>
  <tr><td>0</td><td>no membership — x is not in the set</td></tr>
  <tr><td>1</td><td>full membership — x is totally in the set</td></tr>
  <tr><td>0 &lt; μ(x) &lt; 1</td><td>partial membership / degree of belonging</td></tr>
</table>
<p>Larger number in [0, 1] ⇒ stronger belonging. A fuzzy set is therefore a <b>vague boundary set</b> compared with a crisp set <span class="small">(source pp. 55–58)</span>.</p>
<div class="def">
  <b class="tag">Definition 1 — Membership function (source p. 55, vision-locked)</b>
  <p>If \\(X\\) is a universe of discourse and \\(x \\in X\\), then a fuzzy set \\(A\\) in \\(X\\) is a set of ordered pairs:</p>
  <div class="formula">\\tilde{A} = \\{(x,\\, \\mu_{\\tilde{A}}(x)) \\mid x \\in X\\}</div>
  <p style="margin-bottom:0">where \\(\\mu_{\\tilde{A}}(x)\\) maps each element of \\(X\\) onto a membership grade in \\([0, 1]\\) <b>both inclusive</b>.</p>
</div>
<div class="trap"><b>Exam trap (source p. 48).</b> The degree of membership / truth is <b>not the same as probability</b>. Fuzzy truth represents membership in vaguely defined sets — not the chance of an event.</div>
"""
    return page(7, "Membership: Binary vs Graded", body)


def part_classical_def():
    body = """
<div class="def">
  <b class="tag">Definition — Crisp / classical set (source p. 11)</b>
  <p style="margin-top:1.5mm">A set is an <b>unordered collection of different elements</b>. Changing the order of elements or repeating an element does <b>not</b> change the set.</p>
</div>
<div class="ex"><b>Examples from the booklet</b><br/>set of all positive integers · set of planets in the solar system · set of states in India · set of lowercase letters of the alphabet</div>
<h2>Roster / list notation (source p. 12)</h2>
<p>List all elements in braces, separated by commas.</p>
<div class="formula-row">
  <div class="formula">A = \\{a, e, i, o, u\\}</div>
  <div class="formula">B = \\{1, 3, 5, 7, 9\\}</div>
</div>
<p class="small">A = vowels in the English alphabet · B = odd numbers less than 10.</p>
<h2>Set-builder notation (source p. 13)</h2>
<p>Define the set by a common property \\(p(x)\\):</p>
<div class="formula">A = \\{x : p(x)\\}</div>
<div class="formula-row">
  <div class="formula">A = \\{x : x \\text{ is a vowel in English}\\}</div>
  <div class="formula">B = \\{x : 1 \\le x &lt; 10 \\text{ and } (x \\bmod 2) \\ne 0\\}</div>
</div>
"""
    return page(8, "Classical Set — Definition &amp; Notation", body)


def part_membership_card():
    body = """
<h2>Member and non-member (source p. 14)</h2>
<div class="formula-row">
  <div class="formula">\\(x \\in S\\) &nbsp;&nbsp;<span class="small">x is a member of S</span></div>
  <div class="formula">\\(y \\notin S\\) &nbsp;&nbsp;<span class="small">y is not a member of S</span></div>
</div>
<div class="ex"><b>Example</b> &nbsp; If \\(S = \\{1, 1.2, 1.7, 2\\}\\), then \\(1 \\in S\\) but \\(1.5 \\notin S\\).</div>
<h2>Cardinality (source pp. 15–17)</h2>
<p>Cardinality of a set \\(S\\), written \\(|S|\\), is the number of elements of the set (the cardinal number). An infinite set has infinite cardinality.</p>
<div class="formula-row">
  <div class="formula">|\\{1, 4, 3, 5\\}| = 4</div>
  <div class="formula">|\\{1, 2, 3, 4, 5, \\ldots\\}| = \\infty</div>
</div>
<table>
  <tr><th>Relation</th><th>Meaning</th><th>Mapping</th></tr>
  <tr><td>\\(|X| = |Y|\\)</td><td>same cardinality</td><td>there exists a <b>bijective</b> \\(f : X \\to Y\\)</td></tr>
  <tr><td>\\(|X| \\le |Y|\\)</td><td>X not larger than Y</td><td>there exists an <b>injective</b> \\(f : X \\to Y\\)</td></tr>
  <tr><td>\\(|X| &lt; |Y|\\)</td><td>strictly smaller</td><td>injective but <b>not</b> bijective</td></tr>
</table>
<div class="trap"><b>Exam trap.</b> Cardinality counts <b>distinct</b> elements. Duplicates and order never change a classical set.</div>
"""
    return page(9, "Membership · Cardinality", body)


def part_types_a():
    body = """
<table>
  <tr><th>Type</th><th>Definition</th><th>Booklet example</th></tr>
  <tr><td><b>Universal set</b></td><td>All elements in a particular context / application; every set in that context is a subset of it. Written \\(U\\).</td><td>\\(U\\) = all animals on earth; mammals, fishes, insects ⊆ U</td></tr>
  <tr><td><b>Finite set</b></td><td>Contains a definite number of elements.</td><td>\\(S = \\{x \\mid x \\in \\mathbb{N},\\ 50 &lt; x &lt; 70\\}\\)</td></tr>
  <tr><td><b>Infinite set</b></td><td>Contains infinitely many elements.</td><td>\\(S = \\{x \\mid x \\in \\mathbb{N},\\ x &gt; 10\\}\\)</td></tr>
  <tr><td><b>Subset</b></td><td>\\(Y \\subseteq X\\) if every element of \\(Y\\) is in \\(X\\).</td><td>\\(Y=\\{1,2\\}\\), \\(X=\\{1,2,3,4,5,6\\}\\) ⇒ \\(Y \\subseteq X\\)</td></tr>
  <tr><td><b>Proper subset</b></td><td>Subset of but not equal to: \\(Y \\subset X\\) and \\(|Y| &lt; |X|\\).</td><td>same \\(Y \\subset X\\); \\(X\\) has extra elements</td></tr>
</table>
<p class="small">Note: the booklet writes subset with a “less-than-or-equal / contains” style glyph in places; read as \\(Y \\subseteq X\\) (every element of Y is in X).</p>
<div class="ex"><b>Equal vs subset</b> &nbsp; If \\(X = Y = \\{1,2,3\\}\\), then \\(Y \\subseteq X\\) but \\(Y\\) is <b>not</b> a proper subset of \\(X\\).</div>
"""
    return page(10, "Types of Sets I", body)


def part_types_b():
    body = """
<table>
  <tr><th>Type</th><th>Definition</th><th>Booklet example</th></tr>
  <tr><td><b>Empty / null set</b></td><td>Contains no elements. Written \\(\\varphi\\) in this booklet. Finite; \\(|\\varphi| = 0\\).</td><td>\\(S = \\{x \\mid x \\in \\mathbb{N},\\ 7 &lt; x &lt; 8\\} = \\varphi\\)</td></tr>
  <tr><td><b>Singleton / unit set</b></td><td>Contains exactly one element. Written \\(\{s\}\\).</td><td>\\(S = \\{x \\mid x \\in \\mathbb{N},\\ 7 &lt; x &lt; 9\\} = \\{8\\}\\)</td></tr>
  <tr><td><b>Equal sets</b></td><td>Contain the same elements (order irrelevant).</td><td>\\(A=\\{1,2,6\\}\\), \\(B=\\{6,1,2\\}\\) ⇒ \\(A = B\\)</td></tr>
  <tr><td><b>Equivalent sets</b></td><td>Same cardinality, not necessarily same elements.</td><td>\\(A=\\{1,2,6\\}\\), \\(B=\\{16,17,22\\}\\), \\(|A|=|B|=3\\)</td></tr>
  <tr><td><b>Overlapping sets</b></td><td>Share at least one common element.</td><td>\\(A=\\{1,2,6\\}\\), \\(B=\\{6,12,42\\}\\) share 6</td></tr>
  <tr><td><b>Disjoint sets</b></td><td>No common element: \\(A \\cap B = \\varphi\\).</td><td>\\(A=\\{1,2,6\\}\\), \\(B=\\{7,9,14\\}\\)</td></tr>
</table>
<div class="formula">\\[A \\cap B = \\varphi \\quad \\text{(disjoint)}\\]</div>
<div class="trap"><b>Exam trap.</b> <b>Equal</b> ⇒ same elements. <b>Equivalent</b> ⇒ same size only. Overlapping needs ≥ 1 shared element; disjoint needs 0.</div>
"""
    return page(11, "Types of Sets II", body)


def part_ops_union_int():
    body = """
<p>Set operations: union, intersection, difference, complement, Cartesian product <span class="small">(source p. 25)</span>.</p>
<h2>Union (pp. 25–26)</h2>
<div class="formula">A \\cup B = \\{x \\mid x \\in A \\ \\text{OR}\\  x \\in B\\}</div>
<div class="ex"><b>Example</b> &nbsp; \\(A = \\{10, 11, 12, 13\\}\\), \\(B = \\{13, 14, 15\\}\\)<br/>\\(A \\cup B = \\{10, 11, 12, 13, 14, 15\\}\\) &nbsp;— the common element occurs <b>only once</b>.</div>
<h2>Intersection (pp. 27–28)</h2>
<div class="formula">A \\cap B = \\{x \\mid x \\in A \\ \\text{AND}\\  x \\in B\\}</div>
<div class="ex"><b>Same sets</b> &nbsp; \\(A \\cap B = \\{13\\}\\) &nbsp;— only the common element is kept.</div>
<div class="figbox">A = {10,11,12,<b>13</b>} &nbsp;&nbsp; B = {<b>13</b>,14,15}<br/>
A ∪ B = {10,11,12,13,14,15} &nbsp;&nbsp;|&nbsp;&nbsp; A ∩ B = {13}</div>
"""
    return page(12, "Union &amp; Intersection", body)


def part_ops_diff_comp():
    body = """
<h2>Difference / relative complement (pp. 29–30)</h2>
<div class="formula">A - B = \\{x \\mid x \\in A \\ \\text{AND}\\  x \\notin B\\}</div>
<div class="ex">
  <b>Example (booklet)</b> &nbsp; \\(A = \\{10,11,12,13\\}\\), \\(B = \\{13,14,15\\}\\)<br/>
  \\((A - B) = \\{10, 11, 12\\}\\) &nbsp;&nbsp; \\((B - A) = \\{14, 15\\}\\)<br/>
  Hence \\((A - B) \\ne (B - A)\\) — difference is <b>not commutative</b>.
</div>
<h2>Complement of a set (pp. 31–32)</h2>
<div class="formula">A' = \\{x \\mid x \\notin A\\} = U - A</div>
<p>More specifically \\(A' = U - A\\), where \\(U\\) is the universal set. The booklet also writes complement with an overline: \\(\\bar{A}\\) or \\(\\overline{A}\\).</p>
<div class="ex"><b>Example</b> &nbsp; If \\(A = \\{x : x \\text{ is an odd integer}\\}\\), then \\(A' = \\{y : y \\text{ is not an odd integer}\\}\\).</div>
<div class="trap"><b>Exam trap.</b> \\(A - B\\) keeps what is only in A. It is directional: \\(A - B \\ne B - A\\) in general.</div>
"""
    return page(13, "Difference &amp; Complement", body)


def part_cartesian():
    body = """
<div class="def">
  <b class="tag">Cartesian product / cross product (source p. 33)</b>
  <p style="margin-top:1.5mm">For sets \\(A_1, A_2, \\ldots, A_n\\), the Cartesian product \\(A_1 \\times A_2 \\times \\cdots \\times A_n\\) is all possible <b>ordered</b> \\(n\\)-tuples \\((x_1, x_2, \\ldots, x_n)\\) with \\(x_i \\in A_i\\).</p>
</div>
<div class="formula">A \\times B = \\{(a, b) \\mid a \\in A,\\ b \\in B\\}</div>
<div class="ex">
  <b>Booklet example</b> &nbsp; \\(A = \\{a, b\\}\\), \\(B = \\{1, 2\\}\\)<br/>
  \\(A \\times B = \\{(a,1), (a,2), (b,1), (b,2)\\}\\)<br/>
  \\(B \\times A = \\{(1,a), (1,b), (2,a), (2,b)\\}\\)
</div>
<div class="trap"><b>Exam trap.</b> Pairs are <b>ordered</b>: \\(A \\times B \\ne B \\times A\\) in general. \\((a,1) \\ne (1,a)\\).</div>
<h2>Why ordered pairs matter for fuzzy sets</h2>
<p>Later, a fuzzy set is represented as a set of ordered pairs \\((x, \\mu(x))\\) — element and its grade. The Cartesian-product idea (pairs, not bare elements) is the structural bridge into fuzzy representation.</p>
"""
    return page(14, "Cartesian Product", body)


def part_laws_1():
    body = """
<p class="small">Vision-verified from booklet pages 34–36. Symbols: \\(\\varphi\\) = empty set · \\(X\\) = universal set (Identity slide).</p>
<div class="laws-grid">
  <div class="law-card">
    <div class="t">Commutative (p. 34)</div>
    <div class="f">\\[A \\cup B = B \\cup A\\]</div>
    <div class="f">\\[A \\cap B = B \\cap A\\]</div>
  </div>
  <div class="law-card">
    <div class="t">Associative (p. 35)</div>
    <div class="f">\\[A \\cup (B \\cup C) = (A \\cup B) \\cup C\\]</div>
    <div class="f">\\[A \\cap (B \\cap C) = (A \\cap B) \\cap C\\]</div>
  </div>
  <div class="law-card" style="grid-column:1 / -1">
    <div class="t">Distributive (p. 36)</div>
    <div class="f">\\[A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)\\]</div>
    <div class="f">\\[A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)\\]</div>
  </div>
</div>
<div class="ex"><b>Reading note</b> — Commutative: order of two sets does not matter. Associative: grouping of three does not matter. Distributive: ∪ and ∩ distribute over each other (both directions).</div>
<div class="trap"><b>Exam trap.</b> There is <b>no</b> “cancellation law” for ∪ / ∩ like in ordinary algebra. Do not invent \\(A \\cup B = A \\cup C \\Rightarrow B = C\\).</div>
"""
    return page(15, "Classical-Set Laws I", body)


def part_laws_2():
    body = """
<p class="small">Vision-verified from booklet pages 37–39.</p>
<div class="laws-grid">
  <div class="law-card">
    <div class="t">Idempotency (p. 37)</div>
    <div class="f">\\[A \\cup A = A\\]</div>
    <div class="f">\\[A \\cap A = A\\]</div>
  </div>
  <div class="law-card">
    <div class="t">Identity — four laws (p. 38)</div>
    <div class="f">\\[A \\cup \\varphi = A\\]</div>
    <div class="f">\\[A \\cap X = A\\]</div>
    <div class="f">\\[A \\cap \\varphi = \\varphi\\]</div>
    <div class="f">\\[A \\cup X = X\\]</div>
  </div>
  <div class="law-card">
    <div class="t">Transitive (p. 39)</div>
    <div class="f">\\[A \\subseteq B \\subseteq C \\ \\Rightarrow\\  A \\subseteq C\\]</div>
  </div>
  <div class="law-card">
    <div class="t">Involution (p. 39)</div>
    <div class="f">\\[\\overline{\\overline{A}} = A\\]</div>
  </div>
</div>
<div class="ex"><b>Identity slide text.</b> “For set \\(A\\) and universal set \\(X\\), this property states” the four laws above. Booklet empty set is written \\(\\varphi\\).</div>
<div class="trap"><b>Exam trap.</b> Identity has <b>four</b> laws (not two). Empty = \\(\\varphi\\); universal on this slide = \\(X\\) (elsewhere \\(U\\) also appears).</div>
"""
    return page(16, "Classical-Set Laws II", body)


def part_demorgan():
    body = """
<div class="def">
  <b class="tag">De Morgan’s Law (source p. 40, vision-verified)</b>
  <p style="margin-top:1.5mm">“It is a very important law and supports in proving tautologies and contradiction.”</p>
</div>
<div class="formula">\\overline{A \\cap B} = \\bar{A} \\cup \\bar{B}</div>
<div class="formula">\\overline{A \\cup B} = \\bar{A} \\cap \\bar{B}</div>
<p class="small">The complement bar on the left covers the <b>whole</b> expression. Involution form: \\(\\overline{\\overline{A}} = A\\).</p>
<div class="ex">
  <b>Verification sketch</b><br/>
  An element is outside \\(A \\cap B\\) iff it is outside A <b>or</b> outside B ⇒ \\(\\overline{A \\cap B} = \\bar{A} \\cup \\bar{B}\\).<br/>
  An element is outside \\(A \\cup B\\) iff it is outside A <b>and</b> outside B ⇒ \\(\\overline{A \\cup B} = \\bar{A} \\cap \\bar{B}\\).
</div>
<table>
  <tr><th>Law</th><th>Formula (booklet style)</th></tr>
  <tr><td>De Morgan (intersection)</td><td>complement\\((A \\cap B) = \\bar{A} \\cup \\bar{B}\\)</td></tr>
  <tr><td>De Morgan (union)</td><td>complement\\((A \\cup B) = \\bar{A} \\cap \\bar{B}\\)</td></tr>
  <tr><td>Involution</td><td>\\(\\overline{\\overline{A}} = A\\)</td></tr>
</table>
"""
    return page(17, "De Morgan’s Law", body)


def part_home_tasks():
    body = """
<p>Active recall from source pp. 41–44. Attempt before looking at the checklist at the end.</p>
<div class="def">
  <b class="tag">Home Task 1</b>
  <p>Let \\(U = \\{1,2,\\ldots,20\\}\\).</p>
  <p>\\(A = \\{2,5,7,8,10,13,15,16,18,19,20\\}\\)</p>
  <p>\\(B = \\{1,2,3,4,5,6,9,10,11,12,14,16,17,19\\}\\)</p>
  <p style="margin-bottom:0">Find: (1) \\(A \\cup B\\) &nbsp; (2) \\(A \\cap B\\) &nbsp; (3) \\(A - B\\) &nbsp; (4) \\(B - A\\) &nbsp; (5) \\(A'\\) &nbsp; (6) \\(B'\\)</p>
</div>
<div class="def">
  <b class="tag">Home Task 2</b>
  <p style="margin-bottom:0">Let \\(A = \\{R, S\\}\\), \\(B = \\{7, 10, 18\\}\\). Find (1) \\(A \\times B\\) &nbsp; (2) \\(B \\times A\\).</p>
</div>
<div class="def">
  <b class="tag">Home Task 3</b>
  <p style="margin-bottom:0">Give one example each of: Empty Set · Unit Set · Equal Set · Equivalent Set · Overlapping Set · Disjoint Set.</p>
</div>
<div class="trap"><b>Self-check (Task 1).</b> \\(A \\cup B = U\\). \\(A \\cap B = \\{2,5,10,16,19\\}\\). \\(A-B = \\{7,8,13,15,18,20\\}\\). \\(B-A = \\{1,3,4,6,9,11,12,14,17\\}\\). \\(A' = U-A\\), \\(B' = U-B\\). Verify \\(A - B \\ne B - A\\).</div>
"""
    return page(18, "Home Tasks — Active Recall", body)


def part_why_crisp_fails():
    body = """
<h2>Concept of a fuzzy system (source p. 45)</h2>
<div class="figbox">
  Fuzzy element(s) → Fuzzy set(s) → Fuzzy rule(s) → Fuzzy implication (inference) → Fuzzy system → OUTPUT
</div>
<p>Fuzzy sets extend classical sets to handle <b>partial membership</b>: elements may belong with varying degrees <span class="small">(source p. 46)</span>.</p>
<h2>Where crisp boundaries break</h2>
<table>
  <tr><th>Linguistic concept</th><th>Crisp cut problem</th><th>Fuzzy response</th></tr>
  <tr><td>“Tall person”</td><td>5′10″ tall = tall, 5′09.9″ = not tall</td><td>gradual μ(h) curve</td></tr>
  <tr><td>“Young / old”</td><td>hard age bins, sharp walls</td><td>overlapping age terms</td></tr>
  <tr><td>“Comfortable city”</td><td>city is or is not comfortable</td><td>grades like 0.7, 0.9, 0.3</td></tr>
  <tr><td>Noisy sensor</td><td>single threshold thrashing</td><td>stable degrees of belonging</td></tr>
</table>
<div class="ex"><b>Booklet comfort example (p. 59)</b><br/>\\(X\\) = all cities in India; \\(A\\) = “city of comfort”<br/>\\(A = \\{(\\text{New Delhi}, 0.7), (\\text{Bangalore}, 0.9), (\\text{Chennai}, 0.8), (\\text{Hyderabad}, 0.6), (\\text{Kolkata}, 0.3), (\\text{Kharagpur}, 0)\\}\\)</div>
<div class="trap"><b>Exam trap.</b> Human vague/qualitative thinking is the motivation; the mathematical tool is graded membership in [0, 1].</div>
"""
    return page(19, "Why Crisp Sets Fail", body)


def part_comparison():
    body = """
<table>
  <tr><th>Basis</th><th>Crisp set</th><th>Fuzzy set</th></tr>
  <tr><td>Form</td><td>\\(S = \\{s \\mid s \\in X\\}\\) — collection of elements</td><td>\\(F = \\{(s, \\mu) \\mid s \\in X\\}\\) — ordered pairs; \\(\\mu(s)\\) is the degree of \\(s\\)</td></tr>
  <tr><td>Inclusion of \\(s \\in X\\)</td><td>crisp: strict boundary, yes or no</td><td>fuzzy: if present, with a degree of membership</td></tr>
  <tr><td>Basic property</td><td>precise and certain characteristics</td><td>vague or ambiguous properties</td></tr>
  <tr><td>Partial membership</td><td>not allowed</td><td>allowed; element may be partly in the set</td></tr>
  <tr><td>Logic</td><td>bi-valued</td><td>infinite-valued</td></tr>
  <tr><td>Typical application</td><td>digital design</td><td>fuzzy controllers</td></tr>
  <tr><td>Truth values</td><td>True / False ∈ {0, 1}</td><td>membership values on [0, 1]</td></tr>
  <tr><td>Boundary</td><td>strict boundary T or F</td><td>fuzzy boundary with degree of membership</td></tr>
  <tr><td>Crisp / fuzzy relation</td><td>can be viewed as a special fuzzy case</td><td>a fuzzy set need not be crisp</td></tr>
  <tr><td>Excluded middle &amp; non-contradiction</td><td>classical discussion — may or may not hold in the booklet’s slide wording</td><td>booklet slide states they hold (read with care for exam wording)</td></tr>
</table>
<div class="trap"><b>Exam trap (source p. 48).</b> Degree of membership / truth ≠ probability. Fuzzy truth = membership in a vaguely defined set.</div>
"""
    return page(20, "Classical vs Fuzzy Matrix", body)


def part_fuzzy_def():
    body = """
<div class="def">
  <b class="tag">Formal definition (source pp. 55–56, 60)</b>
  <p>A fuzzy set \\(\\tilde{A}\\) in universe of discourse \\(X\\) is a set of ordered pairs:</p>
  <div class="formula">\\tilde{A} = \\{(x,\\, \\mu_{\\tilde{A}}(x)) \\mid x \\in X\\}</div>
  <p style="margin-bottom:0">where \\(\\mu_{\\tilde{A}}(x)\\) is the <b>membership function</b> of \\(\\tilde{A}\\), and \\(X\\) is the <b>universe of discourse</b>. A fuzzy set is totally characterized by its membership function (MF).</p>
</div>
<table class="kv">
  <tr><td>Membership function</td><td>\\(\mu_{\\tilde{A}}\\) — assigns a grade to each \\(x\\)</td></tr>
  <tr><td>Universe of discourse</td><td>\\(X\\) (also written \\(U\\) on some slides)</td></tr>
  <tr><td>Fuzzy set</td><td>\\(\\tilde{A}\\) — collection of graded memberships</td></tr>
</table>
<p>The membership function associates each element \\(x \\in X\\) with a value in \\([0, 1]\\). Compared with a crisp set, a fuzzy set has a <b>vague boundary</b>.</p>
"""
    return page(21, "Fuzzy Set — Formal Definition", body)


def part_mf():
    body = """
<div class="formula">\\mu_{\\tilde{A}} : X \\to [0, 1]</div>
<p class="small">\\([0, 1]\\) means all real numbers between 0 and 1 <b>including</b> 0 and 1 (vision-locked p. 55).</p>
<table>
  <tr><th>Case</th><th>Value</th><th>Meaning (source p. 58)</th></tr>
  <tr><td>total membership</td><td>\\(\\mu_{\\tilde{A}}(x) = 1\\)</td><td>\\(x\\) is totally in \\(\\tilde{A}\\)</td></tr>
  <tr><td>no membership</td><td>\\(\\mu_{\\tilde{A}}(x) = 0\\)</td><td>\\(x\\) is not in \\(\\tilde{A}\\)</td></tr>
  <tr><td>partial membership</td><td>\\(0 &lt; \\mu_{\\tilde{A}}(x) &lt; 1\\)</td><td>\\(x\\) is partly in \\(\\tilde{A}\\)</td></tr>
</table>
<h2>Universe of discourse</h2>
<p>\\(X\\) is the set of all possible values for the variable of interest (height, age, temperature, city names). The membership function “cuts” this universe into graded belonging rather than two boxes.</p>
<div class="def">
  <b class="tag">Fuzzification (source p. 57)</b>
  <p style="margin:0">The translation \\(x \\mapsto \\mu_{\\tilde{A}}(x)\\) is known as <b>Fuzzification</b>.</p>
</div>
"""
    return page(22, "Membership Function &amp; Universe", body)


def part_not_prob():
    body = """
<h2>Meaning of the membership grade (source p. 57)</h2>
<ul>
  <li>Value of \\(\\mu(x)\\) lies between 0 and 1.</li>
  <li>It is the <b>degree of membership</b> (membership value) of element \\(x\\) in set \\(A\\).</li>
  <li>Members of a fuzzy set are members <b>to some degree</b> — membership grade / degree of membership.</li>
  <li>The grade is the degree of <b>belonging</b>. The larger the number in [0, 1], the stronger the belonging.</li>
</ul>
<div class="trap"><b>N.B. This is not a probability.</b> (explicit booklet warning, p. 57; reconfirmed p. 48: fuzzy truth represents membership in vaguely defined sets.)</div>
<table>
  <tr><th></th><th>Membership μ(x)</th><th>Probability P(E)</th></tr>
  <tr><td>Question</td><td>How much is x in the vague set?</td><td>How likely is event E?</td></tr>
  <tr><td>Sum rule</td><td>Σ/∫ = union of grades (not a total of 1)</td><td>Σ P = 1 over exhaustive events</td></tr>
  <tr><td>Interpretation</td><td>compatibility / belonging</td><td>chance / frequency</td></tr>
</table>
<div class="ex"><b>City of comfort (p. 59)</b> Bangalore at 0.9 means Bangalore is highly compatible with the vague concept “comfortable city” — not that Bangalore is comfortable with probability 0.9.</div>
"""
    return page(23, "Membership Is Not Probability", body)


def part_notation_discrete():
    body = """
<div class="def">
  <b class="tag">Alternative notation (source pp. 61–62, vision-verified)</b>
  <p>If universe \\(X\\) is <b>discrete</b>:</p>
</div>
<div class="formula">\\tilde{A} = \\sum_{x_i \\in X} \\mu_{\\tilde{A}}(x_i) \\,/\\, x_i</div>
<p>Equivalently, for members \\(x_1, \\ldots, x_n\\) with grades \\(\mu_1, \\ldots, \mu_n\\):</p>
<div class="formula">\\tilde{A} = \\mu_1/x_1 + \\mu_2/x_2 + \\cdots + \\mu_n/x_n \\quad = \\sum_{i=1..n} \\mu_i / x_i</div>
<p>Notation \\(\\mu / x\\) means: \\(x\\) is a member of the set <b>to degree</b> \\(\\mu\\).</p>
<div class="trap"><b>Critical reading note (blue text on slide p. 61).</b> “Σ and integral signs stand for the <b>union of membership grades</b>; ‘/’ stands for a <b>marker</b> and <b>does not imply division</b>.”</div>
<div class="ex"><b>Micro-example.</b> \\(X = \\{a,b,c\\}\\), grades 0.2, 1.0, 0.7 ⇒ \\(\\tilde{A} = 0.2/a + 1.0/b + 0.7/c\\) (markers, not quotients).</div>
"""
    return page(24, "Notation — Discrete Universe", body)


def part_notation_continuous():
    body = """
<div class="def">
  <b class="tag">Continuous universe (source pp. 61–62)</b>
  <p>If universe \\(X\\) is <b>continuous</b>:</p>
</div>
<div class="formula">\\tilde{A} = \\int_{X} \\mu_{\\tilde{A}}(x) \\,/\\, x</div>
<p class="small">Again: \\(\\int\\) collects / unions membership grades over \\(X\\); \\(/\\) is a marker, not division.</p>
<table>
  <tr><th>Universe</th><th>Notation</th><th>Symbol meaning</th></tr>
  <tr><td>Discrete \\(X\\)</td><td>\\(\\sum_{x_i \\in X} \\mu(x_i)/x_i\\)</td><td rowspan="2">\\(\\sum\\) or \\(\\int\\) = <b>union of membership grades</b><br/>\\(/\\) = <b>marker</b>, not division</td></tr>
  <tr><td>Continuous \\(X\\)</td><td>\\(\\int_X \\mu(x)/x\\)</td></tr>
</table>
<div class="trap"><b>Exam trap.</b> Do not “compute” \\(\\mu/x\\) as a quotient. Do not interpret \\(\\int \\mu/x\\) as an ordinary probability integral.</div>
<div class="ex"><b>Compact discrete form (p. 63).</b> \\(\\tilde{A} = \\sum_{i=1..n} \\mu_i/x_i\\) with \\(x_1,\\ldots,x_n\\) members of \\(\\tilde{A}\\) and \\(\mu_1,\\ldots,\mu_n\\) their degrees of membership.</div>
"""
    return page(25, "Notation — Continuous Universe", body)


def part_rep_discrete():
    body = """
<div class="def">
  <b class="tag">Representation — mathematical concept (source p. 64, vision-locked)</b>
  <p>A fuzzy set \\(\\tilde{A}\\) in the universe of information \\(U\\) is a set of ordered pairs:</p>
  <div class="formula">\\tilde{A} = \\{(y,\\, \\mu_{\\tilde{A}}(y)) \\mid y \\in U\\}</div>
  <p style="margin-bottom:0">\\(\\mu_{\\tilde{A}}(y)\\) = degree of membership of \\(y\\) in \\(\\tilde{A}\\), with \\(\\mu_{\\tilde{A}}(y) \\in [0, 1]\\).</p>
</div>
<h2>Case 1 — discrete and finite universe (p. 65)</h2>
<div class="formula">\\tilde{A} = \\mu_{\\tilde{A}}(y_1)/y_1 + \\mu_{\\tilde{A}}(y_2)/y_2 + \\mu_{\\tilde{A}}(y_3)/y_3 + \\cdots = \\sum_i \\mu_{\\tilde{A}}(y_i)/y_i</div>
<p class="small">Slash notation \\(\mu_i / y_i\\) means “\\(y_i\\) at grade \\(\mu_i\\)”. The slash is a <b>marker</b>, not division (slide p. 61).</p>
<div class="ex"><b>Consistent example.</b> \\(U = \\{\\text{New Delhi}, \\text{Bangalore}, \\text{Chennai}\\}\\) with grades 0.7, 0.9, 0.8 can be written \\(0.7/\\text{New Delhi} + 0.9/\\text{Bangalore} + 0.8/\\text{Chennai}\\).</div>
"""
    return page(26, "Representation — Discrete Case", body)


def part_rep_continuous():
    body = """
<h2>Case 2 — continuous and infinite universe (p. 66)</h2>
<p>When the universe of information \\(U\\) is continuous and infinite, membership is given by a curve \\(\mu_{\\tilde{A}}(y)\\) and the set is written:</p>
<div class="formula">\\tilde{A} = \\int_{U} \\mu_{\\tilde{A}}(y) \\,/\\, y</div>
<div class="figbox">
<table style="max-width:110mm;margin:0 auto">
<tr><th>Case</th><th>Universe</th><th>Representation</th></tr>
<tr><td>1</td><td>discrete &amp; finite</td><td>\\(\sum_i \\mu_i / y_i\\) or list of pairs \\((y_i, \\mu_i)\\)</td></tr>
<tr><td>2</td><td>continuous &amp; infinite</td><td>\\(\int_U \\mu(y)/y\\) or MF curve over U</td></tr>
</table>
</div>
<div class="ex"><b>Reading the diagram idea.</b> Discrete: a finite column of (element, grade). Continuous: a smooth membership curve over a real interval (height, temperature, age).</div>
<div class="trap"><b>Exam trap.</b> Both cases use the same semantics — graded membership. Only the bookkeeping symbol changes: \\(\\sum\\) vs \\(\\int\\). Universe letter may be \\(X\\) or \\(U\\) in this booklet.</div>
"""
    return page(27, "Representation — Continuous Case", body)


def part_exam():
    body = """
<h2>Formula sheet (booklet style, vision-safe)</h2>
<div class="def" style="font-size:9.3pt">
<b>Classical laws</b><br/>
Commutative: \\(A \\cup B = B \\cup A\\) · \\(A \\cap B = B \\cap A\\)<br/>
Associative: \\(A \\cup (B \\cup C) = (A \\cup B) \\cup C\\) · \\(A \\cap (B \\cap C) = (A \\cap B) \\cap C\\)<br/>
Distributive: \\(A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)\\) · \\(A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)\\)<br/>
Idempotent: \\(A \\cup A = A\\) · \\(A \\cap A = A\\)<br/>
Identity: \\(A \\cup \\varphi = A\\) · \\(A \\cap X = A\\) · \\(A \\cap \\varphi = \\varphi\\) · \\(A \\cup X = X\\)<br/>
Transitive: \\(A \\subseteq B \\subseteq C \\Rightarrow A \\subseteq C\\) &nbsp; Involution: \\(\\overline{\\overline{A}} = A\\)<br/>
De Morgan: \\(\\overline{A \\cap B} = \\bar{A} \\cup \\bar{B}\\) · \\(\\overline{A \\cup B} = \\bar{A} \\cap \\bar{B}\\)<br/>
<b>Fuzzy</b><br/>
\\(\mu_{\\tilde{A}} : X \\to [0,1]\\) · \\(\\tilde{A} = \\{(x,\\mu(x)) \\mid x \\in X\\}\\) · Fuzzification: \\(x \\mapsto \\mu(x)\\)<br/>
Discrete: \\(\\tilde{A} = \\sum_{x_i \\in X} \\mu(x_i)/x_i\\) · Continuous: \\(\\tilde{A} = \\int_X \\mu(x)/x\\)<br/>
<span class="small">/ = marker, not division · Σ/∫ = union of membership grades · membership ≠ probability</span>
</div>
<h2>Top exam traps</h2>
<ol class="tight">
  <li>Fuzzification = input · Defuzzification = output.</li>
  <li>Membership grade is <b>not</b> probability.</li>
  <li>Identity laws = <b>four</b>; empty = \\(\\varphi\\); universal on Identity slide = \\(X\\).</li>
  <li>\\(/\\) in fuzzy notation is a <b>marker</b>, never division.</li>
  <li>De Morgan bars cover the whole left-hand expression.</li>
  <li>\\(A - B\\) is not commutative; Cartesian pairs are ordered.</li>
</ol>
<h2>Glossary</h2>
<p class="small"><b>Universe of discourse</b> X/U · <b>Membership function</b> μ · <b>Fuzzy set</b> Ã · <b>Grade</b> μ(x) ∈ [0,1] · <b>Rule Base</b> IF–THEN expert rules · <b>Fuzzifier</b> crisp→fuzzy · <b>Inference Engine</b> match &amp; fire · <b>Defuzzifier</b> fuzzy→crisp · <b>Cardinality</b> |A| · <b>φ</b> empty set · <b>X</b> universal (Identity slide)</p>
"""
    return page(28, "Exam Traps · Formula Sheet · Glossary", body)


# ---- merge by topic parts ----
TOPIC_PARTS = [
    ("cover", cover),
    ("toc", part_toc),
    ("motivation", part_motivation),
    ("architecture", part_architecture),
    ("rule_base", part_rule_base),
    ("components", part_components),
    ("crisp_fuzzy", part_crisp_vs_fuzzy),
    ("membership", part_membership_binary_graded),
    ("classical_def", part_classical_def),
    ("cardinality", part_membership_card),
    ("types_1", part_types_a),
    ("types_2", part_types_b),
    ("ops_ui", part_ops_union_int),
    ("ops_dc", part_ops_diff_comp),
    ("cartesian", part_cartesian),
    ("laws_1", part_laws_1),
    ("laws_2", part_laws_2),
    ("demorgan", part_demorgan),
    ("home_tasks", part_home_tasks),
    ("crisp_fails", part_why_crisp_fails),
    ("comparison", part_comparison),
    ("fuzzy_def", part_fuzzy_def),
    ("mf", part_mf),
    ("not_prob", part_not_prob),
    ("notation_d", part_notation_discrete),
    ("notation_c", part_notation_continuous),
    ("rep_d", part_rep_discrete),
    ("rep_c", part_rep_continuous),
    ("exam", part_exam),
]


def wrap_display_math(html: str) -> str:
    """Wrap pure-TeX .formula / .f bodies in \\[...\\] for MathJax."""

    def repl(m):
        open_tag, content, close = m.group(1), m.group(2), m.group(3)
        if "\\(" in content or "\\[" in content or "$" in content:
            return m.group(0)
        if "<" in content:
            return m.group(0)
        return f"{open_tag}\\[{content.strip()}\\]{close}"

    html = re.sub(
        r'(<div class="(?:formula|f)">)(.*?)(</div>)',
        repl,
        html,
        flags=re.S,
    )
    return html


def build():
    parts_html = []
    for name, fn in TOPIC_PARTS:
        parts_html.append(f"<!-- part:{name} -->\n{fn()}")
    body = wrap_display_math("\n".join(parts_html))
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>W02 Fuzzy Logic Systems — Soft Computing Booklet</title>
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['\\\\(', '\\\\)']],
    displayMath: [['\\\\[', '\\\\]']],
    processEscapes: true,
    packages: {{'[+]': ['ams']}}
  }},
  options: {{
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    enableMenu: false
  }},
  chtml: {{ scale: 1.0 }},
  startup: {{
    ready: () => {{
      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(() => {{
        document.body.setAttribute('data-mathjax-done', '1');
      }});
    }}
  }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script"></script>
<style>
{CSS}
</style>
</head>
<body>
{body}
</body>
</html>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {HTML} ({HTML.stat().st_size} bytes)")
    print(f"Parts merged: {len(TOPIC_PARTS)}")
    return HTML


if __name__ == "__main__":
    build()
