# -*- coding: utf-8 -*-
"""Generate Week-1 / Week-2 Cyber shortcut table images (PNG) + PDFs.

Reusable: edit the W1/W2 lists (or point them at the glossary) and re-run to
regenerate the images in 06_Diagrams_&_Mindmaps. Uses Playwright Chromium.
"""
import os, html, glob
from playwright.sync_api import sync_playwright

W1 = [
 ("CIA","Confidentiality, Integrity, Availability","الثالوث الأساسي لأمن المعلومات: السرية + السلامة + التوافر"),
 ("ISO","International Organization for Standardization","المنظمة الدولية للمعايير — تصدر ISO 27001 للأمن"),
 ("NIST","National Institute of Standards and Technology","معهد أمريكي يصدر أطر الأمن (NIST CSF, RMF)"),
 ("OCTAVE","Operationally Critical Threat, Asset, and Vulnerability Evaluation","إطار تقييم المخاطر على مستوى المؤسسة"),
 ("FAIR","Factor Analysis of Information Risk","منهج كمّي لتقدير مخاطر المعلومات بالمال"),
 ("IEC","International Electrotechnical Commission","الهيئة الدولية للتقانة الكهربائية (تشارك ISO)"),
 ("CSF","Cybersecurity Framework (NIST)","إطار NIST: تحديد/حماية/كشف/استجابة/تعافي"),
 ("ISMS","Information Security Management System","نظام إدارة أمن المعلومات (ISO 27001)"),
 ("IDS","Intrusion Detection System","نظام كشف التسلل — يراقب وينبّه"),
 ("IPS","Intrusion Prevention System","نظام منع التسلل — يكشف ويمنع"),
 ("DDoS","Distributed Denial of Service","هجوم إغراق موزّع يوقف الخدمة"),
 ("APT","Advanced Persistent Threat","تهديد متقدّم مستمر — هجوم منظّم طويل الأمد"),
 ("XSS","Cross-Site Scripting","حقن سكربتات ضارة بصفحات الويب"),
 ("CVE","Common Vulnerabilities and Exposures","قاعدة معرّفات الثغرات المعروفة"),
 ("CVSS","Common Vulnerability Scoring System","تقييم خطورة الثغرات (0–10)"),
 ("OWASP","Open Worldwide Application Security Project","مرجع أمن تطبيقات الويب (Top 10)"),
 ("IAM","Identity and Access Management","إدارة الهويات والصلاحيات"),
 ("RMF","Risk Management Framework","إطار إدارة المخاطر (NIST)"),
 ("SHA","Secure Hash Algorithm","خوارزمية تجزئة آمنة (SHA-256)"),
 ("GDPR","General Data Protection Regulation","لائحة حماية البيانات الأوروبية"),
 ("HIPAA","Health Insurance Portability and Accountability Act","قانون حماية بيانات المرضى (أمريكا)"),
 ("PCI (DSS)","Payment Card Industry Data Security Standard","معيار أمن بيانات بطاقات الدفع"),
 ("ENISA","European Union Agency for Cybersecurity","وكالة الأمن السيبراني الأوروبية"),
 ("ICS","Industrial Control Systems","أنظمة التحكم الصناعي"),
 ("IoT","Internet of Things","إنترنت الأشياء — أجهزة متصلة"),
]

W2 = [
 ("CIA","Confidentiality, Integrity, Availability","الثالوث الأساسي: السرية + السلامة + التوافر"),
 ("OCTAVE","Operationally Critical Threat, Asset, and Vulnerability Evaluation","إطار تقييم مخاطر على مستوى المؤسسة"),
 ("FAIR","Factor Analysis of Information Risk","منهج كمّي لتقدير مخاطر المعلومات"),
 ("ISO","International Organization for Standardization","المنظمة الدولية للمعايير (ISO 27001)"),
 ("IEC","International Electrotechnical Commission","الهيئة الدولية للتقانة الكهربائية"),
 ("NIST","National Institute of Standards and Technology","معهد أمريكي لأطر الأمن"),
 ("CSF","Cybersecurity Framework (NIST)","إطار NIST للأمن السيبراني"),
 ("ISMS","Information Security Management System","نظام إدارة أمن المعلومات"),
 ("PDCA","Plan–Do–Check–Act","دورة التحسين المستمر: خطّط/نفّذ/تحقّق/صحّح"),
 ("COBIT","Control Objectives for Information and Related Technologies","إطار حوكمة وإدارة تقنية المعلومات"),
 ("COSO","Committee of Sponsoring Organizations","إطار الرقابة الداخلية وإدارة المخاطر"),
 ("CERT","Computer Emergency Response Team","فريق الاستجابة لطوارئ الحاسوب"),
 ("MFA","Multi-Factor Authentication","مصادقة متعددة العوامل"),
 ("RFID","Radio Frequency Identification","تعريف بالترددات الراديوية"),
]

OUT = r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\06_Diagrams_&_Mindmaps"

def build(title, sub, rows):
    trs = "".join(
        f'<tr><td class="sc">{html.escape(a)}</td><td class="nm">{html.escape(b)}</td><td class="mn">{html.escape(c)}</td></tr>'
        for a, b, c in rows)
    return f"""<!doctype html><html dir="rtl" lang="ar"><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}} body{{font-family:"Segoe UI",Tahoma,Arial,sans-serif;margin:0;padding:26px;background:#fff;color:#1c2b28}}
.wrap{{max-width:880px;margin:0 auto}}
.hdr{{background:#0F6E56;color:#fff;border-radius:16px;padding:18px 24px;margin-bottom:16px}}
.hdr .badge{{display:inline-block;background:rgba(255,255,255,.18);border-radius:999px;padding:2px 12px;font-size:12px;margin-bottom:8px}}
.hdr h1{{margin:0;font-size:23px;font-weight:700}}
.hdr p{{margin:6px 0 0;font-size:12.5px;opacity:.92}}
table{{width:100%;border-collapse:collapse;font-size:13.5px;border-radius:14px;overflow:hidden;box-shadow:0 2px 8px rgba(15,110,86,.12)}}
thead th{{background:#0F6E56;color:#fff;text-align:right;padding:11px 14px;font-weight:600;font-size:13px}}
tbody td{{padding:10px 14px;border-bottom:1px solid #eaeaea;vertical-align:top;line-height:1.5}}
tbody tr:nth-child(even){{background:#f3f8f6}}
td.sc{{font-family:Consolas,"Courier New",monospace;font-weight:700;color:#0F6E56;white-space:nowrap;direction:ltr;text-align:left}}
td.nm{{direction:ltr;text-align:left;color:#33413d}}
td.mn{{color:#222}}
.foot{{margin-top:14px;font-size:11.5px;color:#8a8a8a;text-align:center}}
</style></head><body><div class="wrap">
<div class="hdr"><span class="badge">{html.escape(sub)}</span><h1>{html.escape(title)}</h1><p>Master Studio · Cyber Security (CS502) · Dr. Huda Lafta Majeed</p></div>
<table><thead><tr><th>Shortcut</th><th>الاسم الكامل</th><th>شنو يعني</th></tr></thead><tbody>{trs}</tbody></table>
<div class="foot">Source: Cyber_Shortcuts_Glossary.md · {len(rows)} shortcuts</div>
</div></body></html>"""

def chrome_exe():
    for pat in [r"C:\Users\gokoq\AppData\Local\ms-playwright\chromium-*\chrome-win64\chrome.exe"]:
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None

def main():
    os.makedirs(OUT, exist_ok=True)
    exe = chrome_exe()
    jobs = [("W01_Shortcuts", "Cyber Security — Week 1 · Shortcuts", "Week 01", W1),
            ("W02_Shortcuts", "Cyber Security — Week 2 · Shortcuts", "Week 02", W2)]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 940, "height": 300}, device_scale_factor=2)
        for name, title, sub, rows in jobs:
            pg.set_content(build(title, sub, rows))
            pg.screenshot(path=os.path.join(OUT, name + ".png"), full_page=True)
            pg.pdf(path=os.path.join(OUT, name + ".pdf"), format="A4", print_background=True,
                   margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"})
            print("done:", name)
        b.close()

if __name__ == "__main__":
    main()
