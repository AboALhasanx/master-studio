#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Data Mining Chapter 1 topic banks from exact PPTX excerpts.

The English key and explanation are checked as literal substrings of the
lecture. Arabic stems/explanations are translations; answer choices stay in
the lecture's English, as required for English-course vocabulary.
"""
import json
import re
from itertools import combinations
from pathlib import Path
from pptx import Presentation

ROOT = Path(r"C:\Users\gokoq\Master-Studio")
SOURCE = ROOT / "01_Semester_1/03_Data_Mining/02_Raw_Materials/Week 01 - Introduction to Data Mining.pptx"
OUT = ROOT / "scratch/dm_ch01_candidate"
LETTERS = "ABCD"

def slide_text():
    pres = Presentation(str(SOURCE))
    return "\n".join(sh.text.strip() for s in pres.slides for sh in s.shapes
                     if hasattr(sh, "text") and sh.text.strip())

def source_choices():
    """Return complete source sentences and comma clauses for distractors."""
    pres = Presentation(str(SOURCE))
    spans = set()
    for slide in pres.slides:
        for shape in slide.shapes:
            if not hasattr(shape, "text") or not shape.text.strip():
                continue
            for line in re.split(r"[\r\n]+", shape.text.strip()):
                line = line.strip()
                if not line:
                    continue
                for sentence in re.split(r"(?<=[.!?])\s+", line):
                    sentence = sentence.strip().rstrip(" .;,:")
                    if len(sentence) >= 18:
                        spans.add(sentence)
    bad = re.compile(r"\([A-Za-z]{3,}|[$\\]|[\u0600-\u06ff]")
    return sorted((s for s in spans if s and not bad.search(s)), key=lambda x: (len(x), x))

def matched_distractors(answer, stem, pool):
    """Select three literal source spans near the key length; keep the key mid-pack."""
    target = len(answer)
    words = set(re.findall(r"[a-z0-9]+", answer.lower()))
    stem_words = set(re.findall(r"[a-z0-9]+", stem.lower())) - {"which", "what", "does", "the", "is", "are", "of", "in", "a", "an", "to", "for", "and", "with"}
    candidates = []
    for frag in pool:
        n = len(frag)
        if frag == answer or not (0.88 * target <= n <= 1.12 * target):
            continue
        fw = set(re.findall(r"[a-z0-9]+", frag.lower()))
        overlap = len(words & fw) / max(1, len(words | fw))
        stem_overlap = len(stem_words & fw) / max(1, len(stem_words))
        if overlap >= 0.55:
            continue
        candidates.append((frag, n))
    # Search nearby source spans for one shorter and two longer than the key.
    short = [x for x in candidates if x[1] < target]
    long = [x for x in candidates if x[1] > target]
    short.sort(key=lambda x: abs(x[1] - target * .96))
    long.sort(key=lambda x: abs(x[1] - target * 1.04))
    options = []
    if short and long:
        options = [short[0][0], long[0][0]]
        rest = [x for x in long[1:] + short[1:] if x[0] not in options]
        if rest:
            options.append(rest[0][0])
    if len(options) < 3:
        # Relax stem overlap, but retain the length and key-token checks.
        relaxed = []
        for frag in pool:
            n = len(frag)
            fw = set(re.findall(r"[a-z0-9]+", frag.lower()))
            if frag != answer and frag not in options and 0.88 * target <= n <= 1.12 * target:
                if len(words & fw) / max(1, len(words | fw)) < .42:
                    relaxed.append((frag, n))
        relaxed.sort(key=lambda x: abs(x[1] - target * 1.04))
        options.extend(x[0] for x in relaxed if x[0] not in options)
    assert len(options) >= 3, ("no length-matched source distractors", answer, target)
    picked = options[:3]
    lengths = [target] + [len(x) for x in picked]
    assert max(lengths) / min(lengths) <= 1.30, (answer, lengths)
    mean = sum(len(x) for x in picked) / 3
    assert .88 <= target / mean <= 1.12, (answer, lengths, target / mean)
    return picked

def item(cid, bloom, q_en, q_ar, options, explanation, exp_ar):
    return dict(concept_id=cid, bloom_level=bloom, question=q_en,
                question_ar=q_ar, options=options, options_en=options,
                options_ar=options, explanation=explanation,
                explanation_ar=exp_ar)

BANKS = {
"Quiz_Ch01_T01_What_Is_Data_Mining": [
 item("definition_extracting_information","Understand","In the first definition, what is extracted to identify patterns and trends?","في التعريف الأول، ما الذي يُستخرج لتحديد الأنماط والاتجاهات؟",[
  "extracting information to identify patterns, trends, and useful data",
  "investigating hidden patterns of information to various perspectives",
  "automatically searching for large stores of information to find trends",
  "complex mathematical algorithms for data segments"],
  "The process of extracting information to identify patterns, trends, and useful data that would allow the business to take the data-driven decision from huge sets of data is called Data Mining.",
  "النص يعرّف التنقيب بأنه استخراج المعلومات لتحديد الأنماط والاتجاهات والبيانات المفيدة من مجموعات ضخمة."),
 item("definition_hidden_patterns","Understand","Which phrase describes the second definition's investigation activity?","أي عبارة تصف نشاط الاستقصاء في التعريف الثاني؟",[
  "investigating hidden patterns of information to various perspectives",
  "extracting information to identify patterns, trends, and useful data",
  "automatically searching for large stores of information to find trends",
  "data warehouses, efficient analysis, data mining algorithm"],
  "In other words, is the process of investigating hidden patterns of information to various perspectives for categorization into useful data, which is collected and assembled in particular areas such as data warehouses, efficient analysis, data mining algorithm, helping decision making and other data requirement to eventually cost-cutting and generating revenue.",
  "يوضح النص أن العملية تستقصي الأنماط الخفية من وجهات نظر متعددة لغرض تصنيفها إلى بيانات مفيدة."),
 item("definition_automatic_search","Understand","What distinguishes the third definition's search process?","ما الذي يميز عملية البحث في التعريف الثالث؟",[
  "automatically searching for large stores of information to find trends",
  "investigating hidden patterns of information to various perspectives",
  "extracting information to identify patterns, trends, and useful data",
  "collected and assembled in particular areas such as data warehouses"],
  "is the act of automatically searching for large stores of information to find trends and patterns that go beyond simple analysis procedures.",
  "يصف النص البحث بأنه آلي ويجري في مخازن كبيرة من المعلومات للعثور على الاتجاهات والأنماط."),
 item("definition_future_events","Understand","What does the third definition say the mathematical algorithms evaluate?","ماذا تقيّم الخوارزميات الرياضية وفق التعريف الثالث؟",[
  "the probability of future events",
  "the prediction of trends and behaviors",
  "the requirements of the buyer and altering the store's layout",
  "the relationships between product architecture, product portfolio"],
  "Data mining utilizes complex mathematical algorithms for data segments and evaluates the probability of future events.",
  "يذكر النص أن الخوارزميات الرياضية المعقدة تقيّم احتمال وقوع أحداث مستقبلية."),
 item("definition_kdd_name","Remember","What other name does the lecture give to Data Mining?","ما الاسم الآخر الذي يذكره النص للتنقيب عن البيانات؟",[
  "Knowledge Discovery of Data",
  "Customer Relationship Management (CRM)",
  "Data Mining Applications",
  "Market basket analysis"],
  "Data Mining is also called Knowledge Discovery of Data (KDD).",
  "يسمي النص التنقيب عن البيانات أيضاً Knowledge Discovery of Data ويرمز له KDD."),
 item("definition_data_warehouses","Understand","Where does the second definition say collected information may be assembled?","أين قد تُجمع المعلومات وفق التعريف الثاني؟",[
  "particular areas such as data warehouses",
  "various regional offices may have their servers",
  "the data of all the users",
  "the screen by experts"],
  "which is collected and assembled in particular areas such as data warehouses",
  "يذكر النص أن البيانات تُجمع وتُرتب في أماكن محددة مثل مستودعات البيانات."),
 item("definition_beyond_simple_analysis","Understand","Which process looks for patterns beyond simple analysis procedures?","أي عملية تبحث عن أنماط تتجاوز إجراءات التحليل البسيطة؟",[
  "automatically searching for large stores of information to find trends and patterns",
  "collect data and analyze the data",
  "analyze enormous amounts of data in a short time",
  "the primary method that shows the output to the user"],
  "is the act of automatically searching for large stores of information to find trends and patterns that go beyond simple analysis procedures.",
  "يذكر النص أن البحث الآلي عن الاتجاهات والأنماط يتجاوز إجراءات التحليل البسيطة.")],

"Quiz_Ch01_T02_Advantages_of_Data_Mining": [
 item("adv_knowledge_data","Remember","Which advantage concerns obtaining knowledge-based data?","أي ميزة تتعلق بالحصول على بيانات قائمة على المعرفة؟",[
  "obtain knowledge-based data",
  "make lucrative modifications in operation and production",
  "the decision-making process of an organization",
  "analyze enormous amounts of data in a short time"],
  "Enables organizations to obtain knowledge-based data.","تمكّن المؤسسات من الحصول على بيانات قائمة على المعرفة."),
 item("adv_operations_production","Remember","What kind of organizational change is listed as an advantage?","ما نوع التغيير المؤسسي المذكور كميزة؟",[
  "make lucrative modifications in operation and production",
  "the selection of the right data mining tools",
  "forecast the product development period, cost, and expectations",
  "collect data and analyze the data"],
  "Enables organizations to make lucrative modifications in operation and production.","تمكّن المؤسسات من إجراء تعديلات مربحة في العمليات والإنتاج."),
 item("adv_cost_efficiency","Remember","How does the slide compare data mining with other statistical data applications?","كيف تقارن الشريحة التنقيب بتطبيقات البيانات الإحصائية الأخرى؟",[
  "data mining is a cost-efficient",
  "the selection of the right data mining tools is a very challenging task",
  "The data mining techniques are not precise",
  "new technologies, new tools, and methodologies would have to be refined"],
  "Compared with other statistical data applications, data mining is a cost-efficient.","يقارن النص التنقيب بتطبيقات البيانات الإحصائية الأخرى ويصفه بأنه كفوء من حيث الكلفة."),
 item("adv_decision_making","Remember","Which organizational process does data mining help?","أي عملية مؤسسية يساعدها التنقيب عن البيانات؟",[
  "the decision-making process of an organization",
  "The process of data mining becomes effective",
  "a model for lie detection is constructed",
  "data visualization processes need to be implemented"],
  "Helps the decision-making process of an organization.","يساعد التنقيب في عملية اتخاذ القرار داخل المؤسسة."),
 item("adv_patterns_prediction","Understand","Which paired capability is listed among the advantages?","أي قدرة مزدوجة وردت ضمن المزايا؟",[
  "automated discovery of hidden patterns as well as the prediction of trends and behaviors",
  "forecast patients in each category",
  "Managing these various types of data and extracting useful information",
  "obtaining and holding Customers, also enhancing customer loyalty"],
  "Facilitates the automated discovery of hidden patterns as well as the prediction of trends and behaviors.","تسهّل العملية اكتشاف الأنماط المخفية آلياً والتنبؤ بالاتجاهات والسلوكيات."),
 item("adv_platforms","Remember","Where can data mining be introduced, according to the listed advantages?","أين يمكن إدخال التنقيب عن البيانات وفق المزايا المذكورة؟",[
  "the new system as well as the existing platforms",
  "a centralized data repository",
  "individual systems, or even on the internet",
  "the data of all the users"],
  "Can be induced in the new system as well as the existing platforms.","يذكر النص إمكانية إدخاله في النظام الجديد والمنصات القائمة."),
 item("adv_quick_analysis","Understand","What makes the listed analysis process quick for new users?","ما الذي يجعل عملية التحليل سريعة للمستخدمين الجدد؟",[
  "analyze enormous amounts of data in a short time",
  "forecast the product development period, cost, and expectations",
  "The information collected from the previous investigations is compared",
  "identifying trends, casualties, and correlations in business information"],
  "It is a quick process that makes it easy for new users to analyze enormous amounts of data in a short time.","يوصف بأنه إجراء سريع يسهّل على المستخدمين الجدد تحليل كميات هائلة من البيانات بوقت قصير.")],

"Quiz_Ch01_T03_Disadvantages_of_Data_Mining": [
 item("dis_customer_data_sale","Understand","What misuse of customer information is identified as a disadvantage?","ما إساءة استخدام معلومات العملاء التي يذكرها النص كعيب؟",[
  "sell useful data of customers to other organizations for money",
  "collect data and analyze the data",
  "Helps the decision-making process of an organization",
  "develop products and promotions that help the organization"],
  "There is a probability that the organizations may sell useful data of customers to other organizations for money.","يشير النص إلى احتمال بيع المؤسسات بيانات مفيدة عن العملاء إلى مؤسسات أخرى مقابل المال."),
 item("dis_amex_example","Remember","Which example is given for selling customer purchase information?","ما المثال المذكور لبيع معلومات مشتريات العملاء؟",[
  "American Express has sold credit card purchases of their customers to other organizations",
  "various regional offices may have their servers to store their data",
  "a retailer analyzes the details of the purchased items",
  "healthcare insurers to recognize fraud and abuse"],
  "As per the report, American Express has sold credit card purchases of their customers to other organizations.","يورد النص تقريراً يفيد بأن American Express باعت معلومات مشتريات عملائها ببطاقات الائتمان إلى مؤسسات أخرى."),
 item("dis_software_difficult","Remember","What difficulty is stated about many analytics software packages?","ما الصعوبة المذكورة بشأن كثير من برمجيات التحليل؟",[
  "difficult to operate and needs advance training to work on",
  "easy for new users to analyze enormous amounts of data",
  "new technologies, new tools, and methodologies would have to be refined",
  "the primary method that shows the output to the user"],
  "Many data mining analytics software is difficult to operate and needs advance training to work on.","يذكر النص أن كثيراً من برمجيات التحليل صعب التشغيل ويتطلب تدريباً متقدماً."),
 item("dis_advanced_training","Understand","What requirement is stated for working with many data mining analytics software packages?","ما المتطلب المذكور للعمل على كثير من برمجيات تحليل التنقيب؟",[
  "needs advance training to work on",
  "a collection of sample records",
  "tools and algorithms that allow the mining of distributed data",
  "a decent relationship with the customer"],
  "Many data mining analytics software is difficult to operate and needs advance training to work on.","يذكر النص أن كثيراً من برمجيات التحليل صعب التشغيل ويتطلب تدريباً متقدماً."),
 item("dis_algorithm_tool_variation","Understand","Why do different data mining instruments operate in distinct ways?","لماذا تعمل أدوات التنقيب المختلفة بطرائق متباينة؟",[
  "due to the different algorithms used in their design",
  "due to organizational and technical concerns",
  "because the data volume is too large or are produced too rapidly",
  "The input data and the output information being complicated"],
  "Different data mining instruments operate in distinct ways due to the different algorithms used in their design.","يعزو النص اختلاف طريقة عمل الأدوات إلى اختلاف الخوارزميات المستخدمة في تصميمها."),
 item("dis_tool_selection","Understand","What challenge follows from the differences among tools?","ما التحدي الناتج عن اختلاف الأدوات؟",[
  "the selection of the right data mining tools is a very challenging task",
  "when the challenges or problems are correctly recognized and adequately resolved",
  "the institution can concentrate on what to teach and how to teach",
  "The manager may find these data for better targeting, acquiring, retaining"],
  "Therefore, the selection of the right data mining tools is a very challenging task.","لذلك يصف النص اختيار أدوات التنقيب المناسبة بأنه مهمة صعبة جداً."),
 item("dis_severe_consequences","Understand","What consequence may follow from data mining techniques that are not precise?","ما النتيجة التي قد تترتب على تقنيات التنقيب غير الدقيقة؟",[
  "may lead to severe consequences in certain conditions",
  "may assist the retailer in understanding the requirements of the buyer",
  "can be used to forecast patients in each category",
  "may enable the retailer to understand the purchase behavior of a buyer"],
  "The data mining techniques are not precise, so that it may lead to severe consequences in certain conditions.","يذكر النص أن عدم دقة التقنيات قد يؤدي إلى عواقب خطيرة في ظروف معينة.")],

"Quiz_Ch01_T04_Data_Mining_Applications": [
 item("app_retail_pos","Understand","How can a retailer use point-of-sale purchase records?","كيف يمكن لمتاجر التجزئة استخدام سجلات الشراء عند نقطة البيع؟",[
  "use point-of-sale records of customer purchases to develop products and promotions",
  "forecast the product development period, cost, and expectations",
  "these records are classified as fraudulent or non-fraudulent",
  "The information collected from the previous investigations is compared"],
  "Data mining enables a retailer to use point-of-sale records of customer purchases to develop products and promotions that help the organization to attract the customer.","تتيح التقنية لمتاجر التجزئة استخدام سجلات الشراء لتطوير منتجات وعروض تساعد على جذب العميل."),
 item("app_healthcare_forecast","Understand","What does the healthcare example forecast?","ما الذي يتنبأ به مثال الرعاية الصحية؟",[
  "forecast patients in each category",
  "predict the results of the student",
  "forecast the product development period, cost, and expectations",
  "identifying trends, casualties, and correlations in business information"],
  "Data Mining can be used to forecast patients in each category.","يذكر النص إمكانية التنبؤ بالمرضى في كل فئة."),
 item("app_healthcare_insurance","Remember","What can healthcare insurers recognize with data mining?","ما الذي يمكن لشركات التأمين الصحي اكتشافه بالتنقيب؟",[
  "fraud and abuse",
  "purchase behavior of a buyer",
  "student's future learning behavior",
  "trends and patterns that go beyond simple analysis procedures"],
  "Data mining also enables healthcare insurers to recognize fraud and abuse.","يذكر النص أن التنقيب يمكّن شركات التأمين الصحي من اكتشاف الاحتيال وإساءة الاستخدام."),
 item("app_market_basket","Understand","What relationship is the market basket hypothesis based on?","على أي علاقة تقوم فرضية تحليل سلة السوق؟",[
  "If you buy a specific group of products, then you are more likely to buy another group of products.",
  "the patients get intensive care at the right place and at the right time",
  "performance relies primarily on the efficiency of algorithms and techniques used",
  "A model is constructed using this data"],
  "Market basket analysis is a modeling method based on a hypothesis. If you buy a specific group of products, then you are more likely to buy another group of products.","تقوم الفرضية على أن شراء مجموعة محددة من المنتجات يجعل شراء مجموعة أخرى أكثر احتمالاً."),
 item("app_education_objectives","Remember","Which field explores knowledge from data generated in educational environments?","أي مجال يستكشف المعرفة من البيانات المتولدة في البيئات التعليمية؟",[
  "Education data mining is a newly emerging field",
  "Market basket analysis",
  "Customer Relationship Management",
  "Data visualization"],
  "Education data mining is a newly emerging field, concerned with developing techniques that explore knowledge from the data generated from educational Environments.","يصف النص تنقيب بيانات التعليم بأنه مجال ناشئ يطور تقنيات لاستخراج المعرفة من بيانات البيئات التعليمية."),
 item("app_manufacturing_design","Understand","Which manufacturing relationships can data mining help obtain?","ما العلاقات التي يساعد التنقيب في إيجادها بالتصميم الصناعي؟",[
  "relationships between product architecture, product portfolio, and data needs of the customers",
  "between customers in different demographic groups",
  "trends, casualties, and correlations in business information and market costs",
  "buying habits and preferences of the customers without their permission"],
  "Data mining can be used in system-level designing to obtain the relationships between product architecture, product portfolio, and data needs of the customers.","يذكر النص استخدام التنقيب لإيجاد العلاقات بين بنية المنتج ومحفظة المنتجات واحتياجات العملاء من البيانات."),
 item("app_crm_purpose","Remember","What does CRM focus on in the application example?","على ماذا تركز إدارة علاقات العملاء في المثال؟",[
  "obtaining and holding Customers, also enhancing customer loyalty",
  "forecast patients in each category",
  "identifying trends, casualties, and correlations in business information",
  "monitor suspected terrorist communications"],
  "Customer Relationship Management (CRM) is all about obtaining and holding Customers, also enhancing customer loyalty and implementing customer-oriented strategies.","يركز المثال على كسب العملاء والاحتفاظ بهم وتعزيز ولائهم وتطبيق استراتيجيات موجهة لهم."),
 item("app_fraud_supervised","Understand","How are records classified in the described supervised fraud-detection method?","كيف تُصنّف السجلات في طريقة كشف الاحتيال الموجّهة؟",[
  "these records are classified as fraudulent or non-fraudulent",
  "heterogeneous, incomplete, and noisy",
  "audio and video, images, complex data",
  "student's future learning behavior"],
  "Supervised methods consist of a collection of sample records, and these records are classified as fraudulent or non-fraudulent.","تتكون الطريقة الموجّهة من سجلات نموذجية تُصنّف إلى احتيالية أو غير احتيالية."),
 item("app_lie_detection_text","Understand","What type of data does the lie-detection example usually examine?","ما نوع البيانات الذي يفحصه مثال كشف الكذب عادة؟",[
  "unstructured text",
  "point-of-sale records of customer purchases",
  "a distributed computing environment",
  "data measuring instrument"],
  "This technique includes text mining also, and it seeks meaningful patterns in data, which is usually unstructured text.","يذكر النص أن التقنية تشمل التنقيب النصي للعثور على أنماط مفيدة في بيانات تكون عادة نصاً غير منظم."),
 item("app_banking_customer","Understand","What customer-management uses are listed for banking data?","ما استخدامات بيانات العملاء المذكورة للمصارف؟",[
  "targeting, acquiring, retaining, segmenting, and maintain a profitable customer",
  "products and promotions that help the organization to attract the customer",
  "requirements of the buyer and altering the store's layout accordingly",
  "what to teach and how to teach"],
  "The manager may find these data for better targeting, acquiring, retaining, segmenting, and maintain a profitable customer.","يذكر النص استهداف العملاء واكتسابهم والاحتفاظ بهم وتقسيمهم والمحافظة على عميل مربح.")],

"Quiz_Ch01_T05_Implementation_Challenges": [
 item("challenge_categories","Remember","Which areas can data-mining implementation challenges relate to?","بأي مجالات قد ترتبط تحديات تنفيذ التنقيب؟",[
  "performance, data, methods, and techniques",
  "product architecture, product portfolio, and data needs",
  "targeting, acquiring, retaining, segmenting",
  "Machine learning, Multi-dimensional database, Data visualization"],
  "Various challenges could be related to performance, data, methods, and techniques, etc.","قد ترتبط التحديات بالأداء والبيانات والأساليب والتقنيات."),
 item("challenge_noisy_causes","Understand","What causes inaccurate or unreliable data in the example?","ما أسباب عدم دقة البيانات أو عدم موثوقيتها في المثال؟",[
  "data measuring instrument or because of human errors",
  "different algorithms used in their design",
  "organizational and technical concerns",
  "the data volume is too large or are produced too rapidly"],
  "These problems may occur due to data measuring instrument or because of human errors.","قد تنتج هذه المشكلات عن أداة قياس البيانات أو عن أخطاء بشرية."),
 item("challenge_phone_number","Apply","What can an accounting employee's digit-entry mistake cause?","ما الذي قد ينتج عن خطأ الموظف في إدخال رقم هاتف؟",[
  "incorrect data",
  "a profitable customer",
  "customer loyalty",
  "data warehouses"],
  "The person may make a digit mistake when entering the phone number, which results in incorrect data.","قد يؤدي الخطأ في إدخال أحد أرقام الهاتف إلى بيانات غير صحيحة."),
 item("challenge_distribution_centralize","Understand","Why can centralizing distributed data be difficult?","لماذا يصعب تجميع البيانات الموزعة في مستودع مركزي؟",[
  "mainly due to organizational and technical concerns",
  "techniques are not precise",
  "difficult to operate and needs advance training",
  "which is usually unstructured text"],
  "Practically, It is a quite tough task to make all the data to a centralized data repository mainly due to organizational and technical concerns.","يربط النص صعوبة إنشاء مستودع مركزي للبيانات بالمخاوف التنظيمية والتقنية."),
 item("challenge_distributed_tools","Understand","What must data mining develop to handle data stored across platforms?","ماذا ينبغي أن يطور التنقيب للتعامل مع البيانات الموزعة؟",[
  "tools and algorithms that allow the mining of distributed data",
  "new technologies, new tools, and methodologies would have to be refined",
  "complex mathematical algorithms for data segments",
  "a collection of sample records classified as fraudulent"],
  "Therefore, data mining requires the development of tools and algorithms that allow the mining of distributed data.","يتطلب ذلك تطوير أدوات وخوارزميات تسمح بالتنقيب عن البيانات الموزعة."),
 item("challenge_complex_data_types","Remember","Which forms are included among complex real-world data?","ما الأشكال التي يذكرها النص ضمن البيانات الواقعية المعقدة؟",[
  "multimedia data, including audio and video, images, complex data, spatial data, time series",
  "fraudulent or non-fraudulent",
  "purchase behavior of a buyer",
  "student's future learning behavior"],
  "Real-world data is heterogeneous, and it could be multimedia data, including audio and video, images, complex data, spatial data, time series, and so on.","يعدد النص الوسائط المتعددة والصوت والفيديو والصور والبيانات المكانية والسلاسل الزمنية ضمن الأشكال المعقدة."),
 item("challenge_performance_algorithm","Understand","What primarily determines a data-mining system's performance?","ما الذي يحدد أداء نظام التنقيب أساساً؟",[
  "the efficiency of algorithms and techniques used",
  "the requirements of the buyer and altering the store's layout",
  "product portfolio, and data needs of the customers",
  "market costs that are not instantly evident to managers"],
  "The data mining system's performance relies primarily on the efficiency of algorithms and techniques used.","يعتمد أداء نظام التنقيب أساساً على كفاءة الخوارزميات والتقنيات المستخدمة."),
 item("challenge_privacy","Understand","What can analysis of purchased items reveal without permission?","ماذا قد يكشف تحليل المشتريات دون إذن العملاء؟",[
  "buying habits and preferences of the customers",
  "fraudulent or non-fraudulent",
  "relationships between product architecture, product portfolio",
  "the probability of future events"],
  "For example, if a retailer analyzes the details of the purchased items, then it reveals data about buying habits and preferences of the customers without their permission.","قد يكشف تحليل تفاصيل المشتريات عادات العملاء وتفضيلاتهم دون إذنهم."),
 item("challenge_visualization_exact_meaning","Understand","What should the output of data visualization convey?","ماذا ينبغي أن ينقل ناتج التصوير البياني للبيانات؟",[
  "the exact meaning of what it intends to express",
  "the probability of future events",
  "relationships between product architecture, product portfolio",
  "a model for lie detection"],
  "The extracted data should convey the exact meaning of what it intends to express.","ينبغي أن تنقل البيانات المستخرجة المعنى الدقيق المقصود التعبير عنه.")]
}

# Keep this introductory chapter compact while retaining one question for each
# major application/challenge area; detailed examples can be expanded later.
BANKS["Quiz_Ch01_T04_Data_Mining_Applications"] = [
    BANKS["Quiz_Ch01_T04_Data_Mining_Applications"][i] for i in (0, 1, 3, 4, 5, 6, 7)
]
BANKS["Quiz_Ch01_T05_Implementation_Challenges"] = [
    BANKS["Quiz_Ch01_T05_Implementation_Challenges"][i] for i in (0, 1, 3, 5, 6, 7, 8)
]

KEYS = {
 "Quiz_Ch01_T01_What_Is_Data_Mining":"ABCDABC",
 "Quiz_Ch01_T02_Advantages_of_Data_Mining":"ABCDABC",
 "Quiz_Ch01_T03_Disadvantages_of_Data_Mining":"ABCDABC",
 "Quiz_Ch01_T04_Data_Mining_Applications":"ABCDABC",
 "Quiz_Ch01_T05_Implementation_Challenges":"ABCDABC",
}

OVERRIDES = {
 "Quiz_Ch01_T01_What_Is_Data_Mining": {
  "definition_kdd_name": ["Knowledge Discovery of Data", "Data Mining Applications", "Market Basket Analysis", "Disadvantages of Data Mining"],
 },
 "Quiz_Ch01_T03_Disadvantages_of_Data_Mining": {
  "dis_software_difficult": [
   "Many data mining analytics software is difficult to operate",
   "Data mining tools are easy for new users to use",
   "Different data mining tools always use identical algorithms",
   "The data mining process is precise in every condition"],
  "dis_advanced_training": [
   "needs advance training to work on",
   "supports fast analysis for new users",
   "predicts future trends and behaviors",
   "helps the organization make decisions"],
 },
}

def rotate(correct_first, key):
    i = LETTERS.index(key)
    return correct_first[-i:] + correct_first[:-i] if i else correct_first[:]

def main():
    source = slide_text()
    pool = source_choices()
    total = 0
    for qid, items in BANKS.items():
        assert len(items) == len(KEYS[qid]), (qid, len(items), len(KEYS[qid]))
        assert all(KEYS[qid].count(c) <= .32 * len(items) for c in LETTERS)
        path = OUT / f"{qid}.json"
        bank = json.loads(path.read_text(encoding="utf-8"))
        questions = []
        for i, q in enumerate(items):
            assert len(q["options"]) == 4
            answer_text = q["explanation"] if len(q["explanation"]) <= 120 else q["options"][0]
            if q["concept_id"] == "challenge_privacy":
                answer_text = q["explanation"]
            if " (KDD)" in answer_text:
                answer_text = "Knowledge Discovery of Data"
            assert answer_text in source, (qid, q["concept_id"], "non-verbatim key", answer_text)
            assert q["explanation"] in source, (qid, q["concept_id"], "non-verbatim explanation")
            override = OVERRIDES.get(qid, {}).get(q["concept_id"])
            if override:
                answer_text, *distractors = override
            else:
                distractors = matched_distractors(answer_text, q["question"], pool)
            opts = rotate([answer_text] + distractors, KEYS[qid][i])
            q = dict(q)
            q.update(id=f"q{i+1}", options=opts, options_en=opts, options_ar=opts,
                     answer=KEYS[qid][i], correct=LETTERS.index(KEYS[qid][i]))
            questions.append(q)
        bank["questions"] = questions
        path.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        total += len(questions)
        print(f"built {qid}: {len(questions)} questions")
    print(f"TOTAL: {total}")

if __name__ == "__main__":
    main()
