#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Second sweep: the indirect references the first pass missed.

Not the word "handout" this time — "this chapter", "her rule", "she said",
"answer in her vocabulary", "the mentioned six". Same defect, softer wording.
"""
import glob

PAIRS = [
    ("She said the number of domains can grow, so treat the six as the current set of examples, not a closed list.",
     "The number of domains can grow, so the six are the current set of examples, not a closed list."),
    ("قالت إن عدد المجالات قابل للزيادة، فالستة هي المجموعة الحالية من الأمثلة وليست قائمة مغلقة.",
     "عدد المجالات قابل للزيادة، فالستة هي المجموعة الحالية من الأمثلة وليست قائمة مغلقة."),
    ("لا توجد إلا المجالات الستة المذكورة ولن يُضاف غيرها.",
     "لا توجد إلا المجالات الستة نفسها ولن يُضاف غيرها."),
    ("The CIA triad is the backbone of cybersecurity: every control in this chapter serves one of its three pillars.",
     "The CIA triad is the backbone of cybersecurity: every control serves one of its three pillars."),
    ("ثالوث CIA هو العمود الفقري للأمن السيبراني: كل ضابط في هذا الجابتر يخدم أحد أركانه الثلاثة.",
     "ثالوث CIA هو العمود الفقري للأمن السيبراني: كل ضابط يخدم أحد أركانه الثلاثة."),
    ("والتجزئة هي المذكورة مع خوارزميتها SHA-256.",
     "والتجزئة هي المقترنة بخوارزميتها SHA-256."),
    ("Mirai هو المثال المذكور:",
     "Mirai هو المثال القياسي:"),
    ("Her rule: above 100 means there is investment, below 100 means there is none. It is stated as given and taken as given.",
     "The rule: above 100 means there is investment, below 100 means there is none."),
    ("قاعدتها: فوق 100 يعني هناك استثمار، وتحت 100 يعني لا يوجد. تُؤخذ كما وردت.",
     "القاعدة: فوق 100 يعني هناك استثمار، وتحت 100 يعني لا يوجد."),
    ("and it is one of only two places in this chapter where the order matters.",
     "and it is one of only two lists where the order matters."),
    ("وهو أحد موضعين فقط في هذا الجابتر يكون فيهما الترتيب مهماً.",
     "وهو أحد موضعين فقط يكون فيهما الترتيب مهماً."),
    ("Answer in her vocabulary, but know the fact.",
     "Use the familiar wording, but know the fact."),
    ("أجب بمفرداتها، لكن اعرف الحقيقة.",
     "استخدم الصياغة المتداولة، لكن اعرف الحقيقة."),
]

files = sorted(glob.glob(r"C:\Users\gokoq\Master-Studio\scratch\ch0[12]_t0*.py"))
applied = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    before = s
    for old, new in PAIRS:
        if old in s:
            s = s.replace(old, new)
            applied += 1
    if s != before:
        open(f, "w", encoding="utf-8").write(s)
print("replacements applied:", applied)
for old, new in PAIRS:
    if any(old in open(f, encoding="utf-8").read() for f in files):
        print("  STILL PRESENT:", old[:60])
