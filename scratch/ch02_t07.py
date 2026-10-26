#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T07 — OCTAVE: what it analyses, its three phases, and its variants."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T07_OCTAVE"
TOPIC_EN = "OCTAVE: The Three-Phase Method"
TOPIC_AR = "OCTAVE: الطريقة ذات المراحل الثلاث"

I = [
    # 1 -------------------------------------------------------------------
    ("octave_analyses_three", "Remember",
     "Which three things does OCTAVE analyse systematically?",
     "أي ثلاثة أشياء يحلّلها OCTAVE بشكل منهجي؟",
     ["Assets, threats, and vulnerabilities.",
      "Risks, costs, and existing controls.",
      "Policies, people, and the processes.",
      "Assets, budgets, and project timelines."],
     ["الأصول والتهديدات والثغرات.",
      "المخاطر والكلف والضوابط.",
      "السياسات والأفراد والعمليات.",
      "الأصول والميزانيات والجداول."],
     "OCTAVE is a systematic analysis of assets, threats, and vulnerabilities, and its name is built from exactly those three ideas.",
     "OCTAVE تحليل منهجي للأصول والتهديدات والثغرات، واسمه مبني من هذه الأفكار الثلاث."),

    # 2 -------------------------------------------------------------------
    ("phase_one", "Remember",
     "What happens in the first OCTAVE phase?",
     "ماذا يحدث في المرحلة الأولى من OCTAVE؟",
     ["Build up asset-based threat profiles.",
      "Identify vulnerabilities in infrastructure.",
      "Develop the security strategy and plans.",
      "Screen the personnel before access."],
     ["بناء ملفات تهديد مبنية على الأصول.",
      "تحديد الثغرات في البنية التحتية.",
      "تطوير الاستراتيجية والخطط الأمنية.",
      "فحص الموظفين قبل منحهم الوصول."],
     "Phase one builds asset-based threat profiles: you start from the assets and work out what threatens each one.",
     "المرحلة الأولى تبني ملفات تهديد مبنية على الأصول: تبدأ من الأصول وتستنتج ما يهدد كل واحد منها."),

    # 3 -------------------------------------------------------------------
    ("phase_two", "Remember",
     "What happens in the second OCTAVE phase?",
     "ماذا يحدث في المرحلة الثانية من OCTAVE؟",
     ["Identify vulnerabilities in the infrastructure.",
      "Build up the asset-based threat profiles.",
      "Develop the security strategy and plans.",
      "Appoint a security manager before anything else."],
     ["تحديد الثغرات في البنية التحتية.",
      "بناء ملفات تهديد مبنية على الأصول.",
      "تطوير الاستراتيجية والخطط الأمنية.",
      "تعيين مدير أمن قبل أي شيء."],
     "Phase two looks for the vulnerabilities in the infrastructure that could lead to unauthorized action.",
     "المرحلة الثانية تبحث عن الثغرات في البنية التحتية التي قد تؤدي إلى فعل غير مصرّح به."),

    # 4 -------------------------------------------------------------------
    ("phase_three", "Remember",
     "What happens in the third OCTAVE phase?",
     "ماذا يحدث في المرحلة الثالثة من OCTAVE؟",
     ["Develop the security strategy and plans.",
      "Build up the asset-based threat profiles.",
      "Identify vulnerabilities in infrastructure.",
      "Certify the staff on the standard."],
     ["تطوير الاستراتيجية والخطط الأمنية.",
      "بناء ملفات تهديد مبنية على الأصول.",
      "تحديد الثغرات في البنية التحتية.",
      "منح الموظفين شهادة في المعيار."],
     "Phase three turns the findings into a security strategy and plans to address the risks and vulnerabilities found.",
     "المرحلة الثالثة تحوّل النتائج إلى استراتيجية وخطط أمنية تعالج المخاطر والثغرات المكتشفة."),

    # 5 -------------------------------------------------------------------
    ("phase_count", "Remember",
     "How many phases does OCTAVE have?",
     "كم مرحلة لدى OCTAVE؟",
     ["Three phases.", "Four phases.", "Five phases.", "Six phases too."],
     ["ثلاث مراحل.", "أربع مراحل.", "خمس مراحل.", "ست مراحل."],
     "OCTAVE runs in three phases: profiles, vulnerabilities, then strategy and plans.",
     "OCTAVE يعمل بثلاث مراحل: الملفات، ثم الثغرات، ثم الاستراتيجية والخطط."),

    # 6 -------------------------------------------------------------------
    ("scenario_phase_one", "Apply",
     "A team begins by cataloguing what it owns and what threatens each item. Which phase is this?",
     "فريق يبدأ بجرد ما يملكه وما يهدد كل عنصر. أي مرحلة هذه؟",
     ["Phase one, building the threat profiles.",
      "Phase two, finding the vulnerabilities.",
      "Phase three, writing the strategy.",
      "None of the phases, because it is outside."],
     ["المرحلة الأولى، بناء ملفات التهديد.",
      "المرحلة الثانية، إيجاد الثغرات.",
      "المرحلة الثالثة، كتابة الاستراتيجية.",
      "لا شيء منها، لأن هذا خارج العملية."],
     "Starting from the assets and asking what threatens each one is exactly the asset-based threat profile of phase one.",
     "البدء من الأصول والسؤال عما يهدد كل واحد هو بالضبط ملف التهديد المبني على الأصول في المرحلة الأولى."),

    # 7 -------------------------------------------------------------------
    ("scenario_phase_three", "Apply",
     "A team has finished identifying vulnerabilities and now writes the security strategy. Which phase is it entering?",
     "فريق أنهى تحديد الثغرات وبدأ يكتب الاستراتيجية الأمنية. أي مرحلة يدخل؟",
     ["Phase three, writing the strategy and plans.",
      "Phase one, building the threat profiles.",
      "Phase two, finding the vulnerabilities.",
      "None of the phases, because the work is done."],
     ["المرحلة الثالثة، كتابة الاستراتيجية والخطط.",
      "المرحلة الأولى، بناء ملفات التهديد كلها.",
      "المرحلة الثانية، إيجاد الثغرات في البنية.",
      "لا شيء منها، لأن العمل انتهى فعلاً في هذه الحالة."],
     "Vulnerabilities belong to phase two, so the strategy that follows them is phase three.",
     "الثغرات تخص المرحلة الثانية، فالاستراتيجية التي تأتي بعدها هي المرحلة الثالثة."),

    # 8 -------------------------------------------------------------------
    ("octave_developer", "Remember",
     "Who developed OCTAVE?",
     "من طوّر OCTAVE؟",
     ["CERT at Carnegie Mellon University.",
      "ISO and IEC, working jointly.",
      "The US National Institute of Standards.",
      "A European Union agency in Athens."],
     ["منظمة CERT في جامعة Carnegie Mellon.",
      "منظمتا ISO و IEC بالاشتراك بينهما.",
      "المعهد الأمريكي للمعايير والتقنية NIST.",
      "وكالة تابعة للاتحاد الأوروبي في أثينا."],
     "OCTAVE was developed for CERT, the Computer Emergency Response Team, at Carnegie Mellon University in the USA.",
     "طُوّرت OCTAVE لمنظمة CERT، فريق الاستجابة لحوادث الحاسوب، في جامعة Carnegie Mellon بالولايات المتحدة."),

    # 9 -------------------------------------------------------------------
    ("variant_count", "Remember",
     "How many variants of OCTAVE exist?",
     "كم نوعاً من OCTAVE موجود؟",
     ["Four variants.", "Three variants.", "Five variants.", "Two variants."],
     ["أربعة أنواع.", "ثلاثة أنواع.", "خمسة أنواع.", "نوعان فقط."],
     "Four: the original, OCTAVE-S, OCTAVE ALLEGRO, and OCTAVE FORTE.",
     "أربعة: الأصلي، وOCTAVE-S، وOCTAVE ALLEGRO، وOCTAVE FORTE."),

    # 10 ------------------------------------------------------------------
    ("variant_octave_s", "Remember",
     "Which variant is the simplified one for small enterprises?",
     "أي نوع هو المبسّط للمؤسسات الصغيرة؟",
     ["The simplified one for small enterprises.",
      "The expanded version for advanced IT.",
      "The original method, kept unchanged.",
      "A version that drops all of the three phases."],
     ["النسخة المبسّطة للمؤسسات الصغيرة.",
      "النسخة الموسّعة للمؤسسات المتقدمة.",
      "الطريقة الأصلية دون أي تغيير يذكر.",
      "نسخة تلغي المراحل الثلاث كلها."],
     "OCTAVE-S is the simplified variant for small enterprises with limited resources. ALLEGRO is the expanded one.",
     "OCTAVE-S هو النوع المبسّط للمؤسسات الصغيرة ذات الموارد المحدودة. أما ALLEGRO فهو الموسّع."),
]

KEY = "ABCDABCDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
