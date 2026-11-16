import sys, re, os

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"C:\Users\gokoq\Master-Studio"
CH08_DIR = os.path.join(ROOT, r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch08_Software_Testing")

# Official publisher answer key from printed p. 499 of Aggarwal & Singh (3rd ed.)
OFFICIAL_KEYS = {
    1: 'd', 2: 'c', 3: 'b', 4: 'b', 5: 'b', 6: 'c', 7: 'd', 8: 'a', 9: 'c', 10: 'a',
    11: 'a', 12: 'b', 13: 'c', 14: 'd', 15: 'b', 16: 'a', 17: 'a', 18: 'a', 19: 'b', 20: 'b',
    21: 'd', 22: 'a', 23: 'b', 24: 'd', 25: 'c', 26: 'b', 27: 'b', 28: 'a', 29: 'd', 30: 'a',
    31: 'b', 32: 'd', 33: 'a', 34: 'b', 35: 'a', 36: 'a', 37: 'd', 38: 'c', 39: 'a', 40: 'c',
    41: 'd', 42: 'b', 43: 'c', 44: 'd', 45: 'c', 46: 'd', 47: 'b', 48: 'b', 49: 'd', 50: 'b'
}

# Load raw MCQs
with open(os.path.join(CH08_DIR, 'raw_mcqs.txt'), 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Filter headers
lines = raw_text.split('\n')
clean_lines = []
for l in lines:
    if 'Software Engineering (3rd ed.)' in l or 'Multiple Choice Questions' in l or 'Note: Choose' in l or re.match(r'^\s*\d+\s*$', l) or '=== Page' in l:
        continue
    clean_lines.append(l)

cleaned = '\n'.join(clean_lines)

# Match items
raw_items = re.findall(r'(?:^|\n)(8\.\d+)\s+([\s\S]*?)(?=(?:\n8\.\d+\s+)|$)', cleaned)
raw_dict = {}
for q_id, q_body in raw_items:
    num = int(q_id.split('.')[1])
    raw_dict[num] = q_body.strip()

print(f"Loaded {len(raw_dict)} raw MCQ items.")

# Item explanations, source locators, and Arabic notes
DATA = {
    1: {
        "text": "the process of executing a program with the intent of finding errors",
        "ans": "**Software testing is defined classically by Myers (1979) as the process of executing a program with the intent of finding errors.** Testing demonstrates the presence of defects rather than their absolute absence.",
        "note": "تعريف مايرز الكلاسيكي (Glenford Myers, 1979): الاختبار هو عملية تنفيذ البرنامج بقصد اكتشاف الأخطاء والعيوب الكامنة، وليس إثبات خلوه التام من الأخطاء لأن الاختبار الشامل مستحيل حسابياً.",
        "src": "Aggarwal & Singh (3rd ed.), §8.1.1, p. 365; companion slide 4, 189."
    },
    2: {
        "text": "bugs",
        "ans": "**Mistakes made during the coding phase are generally referred to as bugs or errors.** A mistake made by a human developer introduces a bug/fault into the source code, which may subsequently cause a dynamic runtime failure.",
        "note": "الهفوة أو الخطأ الذهني البشري أثناء كتابة الكود البرمجي يُطلق عليه اصطلاحاً «Bug» أو «Fault»، وهو العيب الثابت المتروك في الشيفرة المصدرية.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.1, pp. 368–369; companion slide 189."
    },
    3: {
        "text": "Behavior testing",
        "ans": "**Functional testing is known as behavioral testing or black-box testing.** It treats the software component as a black box, deriving test inputs purely from requirements specifications without examining internal structural control flow.",
        "note": "الفحص الوظيفي (Functional Testing) يُعرف أيضاً بالفحص السلوكي (Behavioral Testing) أو فحص الصندوق الأسود (Black-box)؛ حيث تُبنى حالات الاختبار استناداً إلى المدخلات والمخرجات المطلوبة بالمواصفات دون النظر للكود الداخلي.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3, p. 371; companion slide 189."
    },
    4: {
        "text": "4n+1 test cases",
        "ans": "**For a function of $n$ variables, boundary value analysis (BVA) yields $4n + 1$ test cases.** Under the single-fault assumption, each variable is tested at four boundary extremes ($min, min+, max-, max$) while holding other variables at nominal, plus one common baseline test case with all variables at nominal values: $4(n) + 1 = 4n + 1$.",
        "note": "تحليل القيم الحدية القياسي (BVA) يولد $4n+1$ حالة اختبار لعدد $n$ من المتغيرات اعتماداً على فرضية العيب المنفرد (Single-fault assumption)، حيث يُختبر كل متغير عند 4 قيم حدية وتبقى بقية المتغيرات عند قيمتها الطبيعية (Nominal)، بالإضافة لحالة اختبار مركزية واحدة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.1, p. 372; companion slide 189."
    },
    5: {
        "text": "13",
        "ans": "**For a function of two variables ($n = 2$), robustness testing generates $6n + 1 = 6(2) + 1 = 13$ test cases.** Robustness testing adds values just outside the valid boundaries ($min-$ and $max+$), testing 6 extreme points per variable plus the nominal center.",
        "note": "فحص المتانة (Robustness Testing) يختبر القيم الواقعة خارج الحدود مباشرة ($min-$ و $max+$) بالإضافة للحدود الأربعة، فيكون لكل متغير 6 قيم حدية بالإضافة للحالة الطبيعية ($6n+1$). لمتغيرين اثنين: $6(2)+1 = 13$ حالة اختبار.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.1, pp. 373, 384; companion slide 190."
    },
    6: {
        "text": "6n+1 test cases",
        "ans": "**For a function of $n$ variables, robustness testing of boundary value analysis yields $6n + 1$ test cases.** Each variable takes values $\{min-, min, min+, nom, max-, max, max+\}$, producing $6$ tests per variable held against nominal values of all other inputs, plus $1$ all-nominal test case.",
        "note": "قاعدة عدد حالات اختبار المتانة العامة لـ $n$ متغير هي $6n+1$، وهي امتداد لقاعدة BVA القياسية ($4n+1$) بإضافة نقطتين غير صالحتين لكل متغير لاختبار مناعة النظام ضد المدخلات غير المقبولة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.1, p. 384; companion slide 190."
    },
    7: {
        "text": "maintenance testing",
        "ans": "**Regression testing is primarily related to maintenance testing.** It involves re-running previously executed test suites on a modified program to confirm that recent bug fixes or enhancements have not degraded existing functional capabilities.",
        "note": "اختبار الانحدار (Regression Testing) يرتبط عضوياً بمرحلة الصيانة (Maintenance)؛ هدفه التأكد من أن التعديلات أو معالجة الأخطاء السابقة لم تُدخل أعطالاً جانبية جديدة على وظائف النظام المستقرة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3, p. 371 & §9.5, p. 482; companion slide 190."
    },
    8: {
        "text": "Source node",
        "ans": "**In a control flow graph, a node with indegree $= 0$ and outdegree $\\ne 0$ is called a source node.** It represents the entry point of the program or module.",
        "note": "في مخطط تدفق التحكم (Control Flow Graph)، العقدة التي لا يدخل إليها أي سهم ($indegree=0$) ويخرج منها مسار واحد أو أكثر ($outdegree \\ne 0$) تُسمى عقدة المصدر أو البداية (Source Node).",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.1, p. 407; companion slide 190."
    },
    9: {
        "text": "Destination node",
        "ans": "**In a control flow graph, a node with indegree $\\ne 0$ and outdegree $= 0$ is called a destination node (or sink node).** It represents the exit point or termination of the control flow.",
        "note": "العقدة التي تدخل إليها مسارات ($indegree \\ne 0$) ولا يخرج منها أي مسار ($outdegree=0$) هي عقدة المقصد أو النهاية (Destination / Sink Node).",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.1, p. 407; companion slide 191."
    },
    10: {
        "text": "four portions",
        "ans": "**A decision table has four distinct portions:** (1) Condition Stub in the upper left, (2) Condition Entry in the upper right, (3) Action Stub in the lower left, and (4) Action Entry in the lower right.",
        "note": "جدول القرار (Decision Table) يتكون بنيوياً من 4 أرباع محددة: جذع الشروط (أعلى اليسار)، بنود الشروط (أعلى اليمين)، جذع الإجراءات (أسفل اليسار)، وبنود الإجراءات (أسفل اليمين).",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.3, p. 395; companion slide 191."
    },
    11: {
        "text": "users",
        "ans": "**Beta testing is carried out by real end users or customers at external customer sites.** It represents live operational evaluation in unconstrained, real-world user environments without active intervention from the development team.",
        "note": "اختبار بيتا (Beta testing) ينفذه المستخدمون الفعليون (Users/Customers) في مواقعهم وبيئات عملهم الواقعية دون رقابة مباشرة من فريق التطوير.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 191."
    },
    12: {
        "text": "input domain",
        "ans": "**Equivalence class partitioning is primarily related to partitioning the input domain of a program into valid and invalid classes of data.** Test cases are derived under the assumption that all data values within a single partition exhibit equivalent behavioral results.",
        "note": "تجزئة فئات التكافؤ (Equivalence Class Partitioning) تركز أساساً على تقسيم فضاء المدخلات (Input Domain) إلى مجموعات بيانات صالحة وغير صالحة، لاختيار ممثل واحد عن كل فئة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.2, p. 390; companion slide 191."
    },
    13: {
        "text": "functional testing",
        "ans": "**Cause-effect graphing is one form of functional (black-box) testing technique.** It translates complex natural-language specifications into Boolean logical graphs relating input conditions (causes) to output responses (effects) to systematically generate decision tables.",
        "note": "مخطط السبب والنتيجة (Cause-Effect Graphing) هو تقنية متقدمة تابعة لفحوصات الصندوق الأسود الوظيفية (Functional Testing)، تهدف لتحويل العلاقات المنطقية بين المدخلات والمخرجات إلى جداول قرار دقيقة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.4, p. 402; companion slide 191."
    },
    14: {
        "text": "all of the above",
        "ans": "**During validation, software is evaluated to ensure it satisfies: (a) customer requirements, (b) stated specifications, and (c) intended operational user needs.** Validation addresses the holistic question: 'Are we building the right product?'",
        "note": "عملية التحقق من الصلاحية (Validation) تشمل التحقق من مطابقة المنتج لكل من: متطلبات الزبون، المواصفات المكتوبة، والاحتياج التشغيلي الواقعي للمستخدمين.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.3, p. 370; companion slide 191."
    },
    15: {
        "text": "checking that we are building the product right",
        "ans": "**Verification is checking that we are building the product right (Boehm, 1981).** It encompasses static reviews, inspections, and consistency analyses ensuring that intermediate software artifacts strictly conform to preceding specifications.",
        "note": "التحقق الهيكلي (Verification) هو التأكد من أننا «نبني المنتج بطريقة صحيحة» (Building the product right) عبر مطابقة المخرجات مع المواصفات المكتوبة لكل مرحلة تطويرية.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.3, p. 370; companion slide 192."
    },
    16: {
        "text": "checking that we are building the right product",
        "ans": "**Validation is checking that we are building the right product (Boehm, 1981).** It establishes that the executable software fulfills its intended business purpose and satisfies actual user expectations in its operational environment.",
        "note": "التحقق الوظيفي (Validation) هو التأكد من أننا «نبني المنتج الصحيح المطلوب» (Building the right product) الذي يلبي حاجات المستخدمين والزبائن الحقيقية.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.3, p. 370; companion slide 192."
    },
    17: {
        "text": "developer",
        "ans": "**Alpha testing is done by developers or in-house testing personnel (or by representative customers in developer presence).** It is conducted under controlled laboratory conditions to identify remaining defects prior to broader external release.",
        "note": "اختبار ألفا (Alpha testing) يجريه المطورون أو فريق الاختبار الداخلي للشركة (أو زبائن بحضور وتوجيه المطور) في بيئة الشركة الخاضعة للمراقبة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 192."
    },
    18: {
        "text": "developer's site",
        "ans": "**The site for Alpha testing is the developer's site.** It takes place in a controlled development setting where developers can directly monitor runtime behavior and immediately record diagnostic anomaly traces.",
        "note": "الموقع الحصري لاختبار ألفا هو موقع المطور (Developer's site) وبيئته الداخلية المتحكم بها.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 192."
    },
    19: {
        "text": "user's site",
        "ans": "**The site for Beta testing is the user's site.** Software is distributed to real end users who execute it within their diverse, unmonitored production hardware and operating configurations.",
        "note": "موقع اختبار بيتا هو موقع المستخدم الفعلي (User's site) لضمان العمل على البيئات والأجهزة المتنوعة للعملاء.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 193."
    },
    20: {
        "text": "customer",
        "ans": "**Acceptance testing is done by the customer (or designated user representatives).** It provides formal verification that contract requirements and business deliverables have been fully satisfied before financial sign-off and deployment.",
        "note": "اختبار القبول (Acceptance testing) تجريه جهة الزبون الرسمية (Customer) كإجراء تعاقدي نهائي للموافقة على استلام المنظومة وتشغيلها.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 193."
    },
    21: {
        "text": "all of the above",
        "ans": "**One fault in software may lead to: (a) no failure (if unexecuted or masked), (b) a single failure, or (c) multiple failures across different operational runs.** The manifestation of a fault depends dynamically on input data combinations and execution environment state.",
        "note": "العيب البرمجي الواحد (Fault) قد لا يسبب أي فشل إن لم يُنفذ المسار أو تم تمويه النتيجة، أو قد يسبب فشلاً واحداً، أو يسبب انهيارات متعددة متكررة في بيئات مختلفة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.1, p. 369; companion slide 193."
    },
    22: {
        "text": "set of test cases",
        "ans": "**A test suite is a collection or set of test cases designed to test a program or module.** It bundles inputs, execution conditions, and expected outcomes to verify compliance with a defined scope of requirements.",
        "note": "حزمة الاختبار (Test Suite) هي مجموعة منظمة من حالات الاختبار (Set of test cases) تُجمع وتُنفذ سوياً للتحقق من وحدة أو نظام كامل.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.2, p. 369; companion slide 193."
    },
    23: {
        "text": "validation",
        "ans": "**Behavioral specifications are required for validation.** Because validation evaluates external compliance with required user operations without regard to internal algorithms, clear behavioral specifications serve as the benchmark for acceptable functional outcomes.",
        "note": "المواصفات السلوكية (Behavioral specifications) تصف الاستجابات الخارجية للنظام، وهي المرجع الأساسي لإجراء التحقق الوظيفي (Validation).",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.3, p. 370; companion slide 193."
    },
    24: {
        "text": "regression testing",
        "ans": "**During the development phase, the following approach is generally not adopted as a primary testing level: regression testing.** Development testing progresses systematically through unit testing, integration testing, and system testing; regression testing is a re-testing activity triggered by code modifications and maintenance.",
        "note": "أثناء دورة مراحل التطوير المتسلسلة (Unit $\\rightarrow$ Integration $\\rightarrow$ System)، لا يُصنف اختبار الانحدار (Regression) كمرحلة تطوير أساسية قائمة بذاتها، بل هو إجراء صيانة وإعادة اختبار عند تعديل الكود.",
        "src": "Aggarwal & Singh (3rd ed.), §8.5, pp. 435–436; companion slide 194."
    },
    25: {
        "text": "regression testing",
        "ans": "**Regression testing is not a functional test design technique.** Boundary value analysis, equivalence class partitioning, and cause-effect graphing are black-box test derivation methods, whereas regression testing is a strategy for repeating existing tests after changes.",
        "note": "تقنيات تصميم الفحص الوظيفي هي BVA و Equivalence Partitioning و Cause-effect graphing؛ أما Regression testing فهو استراتيجية إعادة تشغيل الفحوصات وليس أسلوباً لاشتقاق الحالات من المواصفات.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3, p. 371; companion slide 194."
    },
    26: {
        "text": "complex combinations of conditions",
        "ans": "**Decision tables are useful for describing situations involving complex combinations of conditions and multiple interrelated actions.** They systematically prevent omitted logic paths when input variables interact in multi-rule business logic.",
        "note": "جداول القرار (Decision Tables) هي الأداة المثلى لمعالجة وحصر الحالات التي تحتوي على تركيبات شروط منطقية معقدة (Complex combinations of conditions) تتطلب استجابات مختلفة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.3, p. 395; companion slide 194."
    },
    27: {
        "text": "they do not explore combinations of input conditions",
        "ans": "**One major weakness of boundary value analysis and equivalence class partitioning is that they do not explore combinations of input conditions.** Both methods test variables largely in isolation under the single-fault assumption, missing defects caused by variable interactions.",
        "note": "نقطة الضعف الجوهرية في تحليل القيم الحدية وتجزئة التكافؤ هي إهمال التفاعل بين الشروط المركبة، حيث تفترض كل طريقة فحص المتغير بمعزل عن بقية المتغيرات.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.3, p. 395; companion slide 194."
    },
    28: {
        "text": "input & output",
        "ans": "**In cause-effect graphing, cause and effect represent input condition and output action (or state change) respectively.** A cause is a distinct input condition or equivalence class; an effect is an observable output or internal transformation.",
        "note": "في تقنية مخطط السبب والنتيجة (Cause-Effect Graphing)، يمثل «السبب» شرط الإدخال (Input)، ويمثل «الأثر» الإجراء أو المخرج الناتج (Output).",
        "src": "Aggarwal & Singh (3rd ed.), §8.3.4, p. 402; companion slide 195."
    },
    29: {
        "text": "all of the above",
        "ans": "**A DD-path graph is also called a condensed flow graph, decision-to-decision path graph, or reduced control flow graph.** It compresses sequences of single-entry, single-exit nodes into individual vertices to simplify path and basis-set analysis.",
        "note": "مخطط مسارات القرار (DD-path graph) يُطلق عليه أيضاً المخطط المكثف (Condensed graph) أو مسار القرار إلى القرار، لأنه يدمج سلاسل التعليمات المتتالية في عقدة واحدة لتسهيل حساب التعقيد.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.1, p. 410; companion slide 195."
    },
    30: {
        "text": "any path through the program that introduces at least one new edge",
        "ans": "**An independent path is any path through a program that introduces at least one edge that has not been traversed before the path is defined.** The set of all independent paths forms a basis set for the control flow graph.",
        "note": "المسار المستقل (Independent path) في الرسم البياني للبرنامج هو أي مسار يتضمن على الأقل ضلعاً (Edge) جديداً لم يسبق مروره في المسارات المحددة قبله.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.1, p. 407; companion slide 195."
    },
    31: {
        "text": "Thomas McCabe",
        "ans": "**Cyclomatic complexity metric was developed by Thomas J. McCabe in 1976.** It provides a quantitative measure of the logical complexity of a program based on graph theory.",
        "note": "مقياس التعقيد الدوري (Cyclomatic Complexity) ابتكره العالم توماس مكيب (Thomas McCabe) عام 1976 لحساب عدد المسارات المستقلة خطياً في الكود.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.2, p. 422; companion slide 195."
    },
    32: {
        "text": "all of the above",
        "ans": "**Cyclomatic complexity $V(G)$ is denoted by all of the following equivalent formulations:** (a) $V(G) = E - N + 2P$, (b) $V(G) = \\text{Number of bounded regions in a planar flow graph} + 1$, and (c) $V(G) = P + 1$ (where $P$ is the number of predicate nodes with 2 outgoing edges).",
        "note": "التعقيد الدوري $V(G)$ يُحسب بثلاث طرق رياضية متطابقة: $E-N+2P$ (حيث $P$ عدد المكونات المتصلة)، أو عدد المناطق المحصورة $+1$، أو عدد عقد القرار الثنائية $+1$.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.2, pp. 422–424; companion slide 196."
    },
    33: {
        "text": "two outgoing edges",
        "ans": "**The equation $V(G) = \\Pi + 1$ of cyclomatic complexity is applicable only if every predicate node has exactly two outgoing edges.** If a decision node has multi-way branching (such as a switch statement with $k > 2$ branches), the simple $+1$ rule fails and each multi-way branch must be converted into binary decision points.",
        "note": "صيغة التعقيد الدوري السريعة $V(G) = \\text{Predicate} + 1$ تصح فقط وبشرط حتمي أن يكون لكل عقدة قرار مخرجان اثنان فقط (Binary decision: True/False). في حال وجود تفرع متعدد (Switch) يجب تفكيكها.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.2, p. 424; companion slide 196."
    },
    34: {
        "text": "number of nodes in the flow graph",
        "ans": "**The size of a graph matrix is an $N \\times N$ square matrix, where $N$ is the number of nodes in the flow graph.** Each row and column corresponds directly to a node.",
        "note": "مصفوفة الرسم البياني (Graph Matrix) هي مصفوفة مربعة بأبعاد $N \\times N$، حيث يمثل $N$ عدد العقد الإجمالي في مخطط تدفق البرنامج.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.3, p. 426; companion slide 196."
    },
    35: {
        "text": "one row and one column in graph matrix",
        "ans": "**In a graph matrix, every node is represented by exactly one row and one column.** The entry at $(i, j)$ indicates whether a directed edge connects node $i$ to node $j$.",
        "note": "في مصفوفة الرسم، تُمثل كل عقدة بصف واحد وعمود واحد حصراً؛ وتُسجل التوصيلات بين العقدة $i$ والعقدة $j$ في الخلية المتقاطعة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.3, p. 426; companion slide 197."
    },
    36: {
        "text": "number of independent paths",
        "ans": "**Cyclomatic complexity $V(G)$ is equal to the number of linearly independent paths through the program flow graph.** It establishes the upper bound for the number of test cases required to achieve complete branch coverage.",
        "note": "التعقيد الدوري $V(G)$ يساوي رياضياً عدد المسارات المستقلة خطياً (Number of independent paths) في فضاء المسارات الأساسي للبرنامج.",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.2, p. 422; companion slide 197."
    },
    37: {
        "text": "none of the above",
        "ans": "**Data flow testing is not related to data flow diagrams, E-R diagrams, or data dictionaries.** Data flow testing is a structural (white-box) technique focusing on the lifecycle of program variables (definitions, uses, and kills) along paths in control flow graphs.",
        "note": "فحص تدفق البيانات (Data Flow Testing) هو فحص صندوق أبيض لمسارات المتغيرات (DEF/USE) في كود البرنامج، ولا علاقة له بمخططات تدفق البيانات (DFD) أو مخططات الكيانات (ERD).",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.4, p. 430; companion slide 197."
    },
    38: {
        "text": "all du-paths that are not dc-paths",
        "ans": "**In data flow testing, a key objective is to uncover data anomalies, which requires examining all du-paths that are not definition-clear (dc) paths.** If a variable is re-defined along a path before being used, an anomaly or redundant definition exists.",
        "note": "الهدف في فحص تدفق البيانات هو كشف التشوهات (Data anomalies) باختبار المسارات التي يعاد فيها تعريف المتغير دون استخدامه (المسارات التي ليست dc-paths نظيفة).",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.4, pp. 430–432; companion slide 197."
    },
    39: {
        "text": "fault seeding",
        "ans": "**Mutation testing is closely related to fault seeding.** In mutation testing, artificial syntactic faults (mutants) are deliberately inserted into programs to assess the adequacy and effectiveness of a test suite in 'killing' the mutated programs.",
        "note": "فحص التحوير (Mutation testing) يعتمد على غرس الأخطاء البرمجية عمداً (Fault seeding) لتقييم كفاءة مجموعة الاختبار في اكتشاف وقتل النسخ المشوهة (Mutants).",
        "src": "Aggarwal & Singh (3rd ed.), §8.4.5, p. 430; companion slide 198."
    },
    40: {
        "text": "scaffolding",
        "ans": "**The overhead code required to be written for unit testing (consisting of drivers and stubs) is called scaffolding.** Drivers simulate calling modules, while stubs simulate subordinate called modules.",
        "note": "الكود الإضافي المساند المكتوب لتنفيذ فحص الوحدة (Unit testing)، والذي يتضمن برامج القيادة (Drivers) والمحاكيات البديلة (Stubs)، يُسمى السقالات البرمجية (Scaffolding).",
        "src": "Aggarwal & Singh (3rd ed.), §8.5.1, p. 436; companion slide 198."
    },
    41: {
        "text": "regression testing",
        "ans": "**Regression testing is a testing strategy, not a debugging technique.** Debugging techniques for locating errors include core dumps, execution traces, print statements, backtracking, and induction/deduction methods.",
        "note": "اختبار الانحدار (Regression testing) هو مرحلة فحص، وليس أسلوباً لتنقيح الأخطاء (Debugging technique). أساليب التنقيح تشمل تفريغ الذاكرة (Core dumps) وتتبع التنفيذ (Traces).",
        "src": "Aggarwal & Singh (3rd ed.), §8.7.1, p. 442; companion slide 198."
    },
    42: {
        "text": "failure",
        "ans": "**A break or observable departure in the normal working/operation of a system is called a failure.** A fault is the internal static defect in code; an error is a human misaction; a failure is the dynamic breakdown observed during execution.",
        "note": "التوقف أو العطل الظاهر في عمل المنظومة أثناء التشغيل يُسمى فشلاً (Failure). الفشل هو العرض الخارجي الملاحظ، والخلل (Fault) هو السبب الداخلي في الكود.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.1, p. 369; companion slide 198."
    },
    43: {
        "text": "acceptance testing",
        "ans": "**Alpha and Beta testing techniques are specialized forms of acceptance testing.** They assess software readiness from user perspectives before formal commercial distribution.",
        "note": "اختبارات ألفا وبيتا هي أشكال وتطبيقات مباشرة تابعة لاختبار القبول (Acceptance testing) لتقييم رضا المستخدمين عن المنظومة.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 198."
    },
    44: {
        "text": "acceptance testing",
        "ans": "**Acceptance testing is not a verification activity; it is a dynamic validation activity.** Reviews, walkthroughs, inspections, and path tracing are verification activities examining artifacts for specification conformance.",
        "note": "اختبار القبول (Acceptance testing) هو نشاط فحص تشغيلي تابع للـ Validation وليس نشاط تدقيق مكتبي تابع للـ Verification مثل المراجعات (Reviews) والتدقيق (Walkthrough).",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.3, p. 370; companion slide 199."
    },
    45: {
        "text": "verification and validation",
        "ans": "**Testing software is basically an integrated discipline encompassing both verification and validation (V&V).** Verification confirms structural compliance with design specifications, while validation confirms behavioral satisfaction of customer requirements.",
        "note": "فحص البرمجيات يشمل كلاً من التحقق الهيكلي والتحقق الوظيفي (Verification and Validation) معاً لضمان الجودة الشاملة للمنتج.",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.3, p. 370; companion slide 199."
    },
    46: {
        "text": "all of the above",
        "ans": "**Integration testing techniques include: (a) top-down integration, (b) bottom-up integration, and (c) sandwich (hybrid) integration.** All of the above are standard structural strategies for combining and testing interacting modules.",
        "note": "استراتيجيات فحص التكامل تشمل الفحص التنازلي (Top-down)، الفحص التصاعدي (Bottom-up)، والفحص الهجين/الشطيرة (Sandwich).",
        "src": "Aggarwal & Singh (3rd ed.), §8.5.2, pp. 437–438; companion slide 199."
    },
    47: {
        "text": "black box testing",
        "ans": "**The functionality of software is tested by black-box (functional) testing.** Black-box testing evaluates system responses strictly against functional requirements without requiring knowledge of internal code constructs.",
        "note": "فحص وظائف النظام وسلوكه الخارجي يتم حصراً عبر فحص الصندوق الأسود (Black box testing) بالاعتماد على متطلبات النظام.",
        "src": "Aggarwal & Singh (3rd ed.), §8.3, p. 371; companion slide 199."
    },
    48: {
        "text": "identification of faults",
        "ans": "**In top-down integration testing, the approach is used primarily for the early identification of major architectural and control faults.** Testing begins with the main control module using stubs, ensuring that top-level decision and interface logic is validated before lower-level components are built.",
        "note": "في الفحص التنازلي (Top-down)، تُختبر موديولات التحكم العليا أولاً، مما يتيح الاكتشاف المبكر للعيوب الهيكلية الحرجة وعيوب الربط بين الواجهات (Identification of faults).",
        "src": "Aggarwal & Singh (3rd ed.), §8.5.2, p. 437; companion slide 199."
    },
    49: {
        "text": "all of the above",
        "ans": "**Thread testing is an integration technique used for testing real-time systems, object-oriented systems, and event-driven systems.** It tracks execution threads triggered by specific external events through the interacting components of the architecture.",
        "note": "اختبار الخيوط (Thread testing) يُستخدم في فحص تكامل الأنظمة اللحظية (Real-time)، الموجهة للكائنات (OO)، والأنظمة المقادة بالأحداث (Event-driven).",
        "src": "Aggarwal & Singh (3rd ed.), §8.5.2, p. 438; companion slide 200."
    },
    50: {
        "text": "beta testing",
        "ans": "**Testing of software with actual data and in the actual live operational environment is called beta testing.** It exposes the product to realistic operational stress in customer environments without developer intervention.",
        "note": "فحص البرمجيات بالبيانات الفعلية الحقيقية وفي بيئة العمل الواقعية بواسطة المستخدمين يُسمى اختبار بيتا (Beta testing).",
        "src": "Aggarwal & Singh (3rd ed.), §8.2.4, p. 370; companion slide 200."
    }
}

# ---------------------------------------------------------------------------
# Review fix (2026-10-23): the bold key line is now taken literally from the
# scanned option text, and every explanation below is checked against the
# companion deck (slide numbers) and the textbook table of contents (section
# start pages). Items without an explanatory sentence in the deck say so.
# ---------------------------------------------------------------------------
OVR = {
    2: {
        "ans": "**When developers make mistakes while coding, these mistakes are called bugs.** People make errors (a good synonym is mistake); a failure occurs only when a fault executes.",
        "note": "الخطأ البشري أثناء كتابة الكود يسمى «bug». لا تخلط بين الخيارين: errors هو الفعل البشري العام، أما bugs فهو الاسم الذي يطلقه المصدر على أخطاء الترميز.",
    },
    7: {
        "ans": "**Publisher key: regression testing is primarily related to maintenance testing,** meaning re-testing after software has been changed.",
        "note": "اختبار الانحدار (Regression) يرتبط بمرحلة الصيانة: إعادة الفحص بعد أي تعديل. السلايدات لا تشرح هذا البند بجملة صريحة، فاحفظه كمفتاح الناشر.",
    },
    12: {
        "ans": "**Equivalence class partitioning is a black-box (functional) technique:** the input domain is divided into classes from the specification, and test cases are chosen from each class without looking at the code.",
        "note": "تجزئة فئات التكافؤ تقنية صندوق أسود (Black-box) لأنها تُشتق من المواصفات فقط. الفخ: الخياران Structural وMutation يخصان عائلات أخرى، وليسا صحيحين.",
    },
    14: {
        "ans": "**During validation the customer checks the product.** Alpha, beta and acceptance testing are the ways of involving the customer during testing, and the product is judged against the customer's expectations.",
        "note": "في Validation الزبون هو من يفحص المنتج (Alpha وBeta وAcceptance كلها طرق لإشراك الزبون). الفخ: الخيار (b) Product is checked صحيح لغوياً لكنه لا يميّز Validation، ومفتاح الناشر هو (d).",
    },
    15: {
        "ans": "**Verification is checking the product with respect to its specifications:** evaluating whether the products of a development phase satisfy the conditions imposed at the start of that phase.",
        "note": "Verification: مطابقة ناتج كل مرحلة مع المواصفات والشروط التي وُضعت في بدايتها. أما مطابقة توقعات الزبون فهي Validation.",
    },
    16: {
        "ans": "**Validation is checking the product with respect to the customer's expectation.** The deck words it as evaluating the system during or at the end of development against the specified requirements; the key chooses the customer-expectation option.",
        "note": "Validation: مطابقة المنتج لتوقعات الزبون. تنبيه: صياغة السلايد 11 هي «specified requirements»، لكن مفتاح الناشر لهذا السؤال هو (a) فاعتمده.",
    },
    17: {
        "ans": "**Alpha tests are conducted at the developer's site by some potential customers, in a controlled environment.** The customer is therefore the keyed answer.",
        "note": "اختبار ألفا ينفذه زبائن محتملون في موقع المطور وبيئة متحكَّم بها. الفخ: لا تختر Developer لأن المفتاح (a) Customer.",
    },
    20: {
        "ans": "**Acceptance testing is conducted by the end user or customer.** It is used when the software is developed for a specific customer, who runs a series of tests to validate all requirements; these may range from ad hoc tests to a well-planned systematic series.",
        "note": "اختبار القبول ينفذه الزبون أو المستخدم النهائي عندما يُطوَّر النظام لزبون محدد، وقد يكون عشوائياً أو منظماً.",
    },
    23: {
        "ans": "**Publisher key: behavioral specifications are required for verification.** The deck gives no sentence explaining this item, so it is a keyed fact; a behavioral specification is the reference the product's observable behavior is checked against.",
        "note": "المفتاح الرسمي هو (b) Verification. السلايدات لا تشرح السبب بجملة صريحة، لذا لا تجادل المفتاح في الامتحان؛ تذكّر أن الخيار الذي يطابق حرفه هو Verification وليس Validation.",
    },
    24: {
        "ans": "**Acceptance testing is not adopted during the development phase.** Unit, bottom-up and integration testing are development-time approaches; acceptance testing involves the customer and is done after unit and integration testing.",
        "note": "أثناء التطوير تُستخدم Unit وBottom-up وIntegration. اختبار القبول (Acceptance) يخص الزبون ويأتي بعدها، لذلك هو الخيار غير المعتمد (d).",
    },
    25: {
        "ans": "**Regression testing is not a functional testing technique.** Boundary value analysis and decision tables are functional (black-box) techniques; regression testing is re-testing after changes.",
        "note": "BVA وDecision table تقنيات وظيفية، أما Regression فهو إعادة اختبار بعد التعديل وليس تقنية لاشتقاق الحالات من المواصفات.",
    },
    26: {
        "ans": "**Decision tables are useful where a number of combinations of actions are taken under varying sets of conditions.** They list conditions and actions as rules, so each combination of conditions is tied to its actions.",
        "note": "جداول القرار تناسب الحالات التي تتغير فيها مجموعة الشروط وتُنفَّذ تركيبات مختلفة من الإجراءات. الفخ: الخيار (a) يتحدث عن إجراء واحد فقط.",
    },
    29: {
        "ans": "**A DD path graph is a decision-to-decision path graph.** It reduces the flow graph by combining runs of sequential nodes into single nodes, keeping the decision nodes.",
        "note": "DD = Decision to Decision. الرسم يدمج العقد المتتابعة ويُبقي عقد القرار. الفخ: لا تفكّ الاختصار إلى Design أو Defect أو Destination.",
    },
    30: {
        "ans": "**An independent path is any path through the DD path graph that introduces at least one new set of processing statements or new conditions.**",
        "note": "المسار المستقل يضيف على الأقل مجموعة جديدة من تعليمات المعالجة أو شروطاً جديدة. الفخ: at most وone and only one خياران خاطئان.",
    },
    31: {
        "ans": "**Cyclomatic complexity was developed by T. J. McCabe.** The deck introduces it as McCabe's cyclomatic metric, V(G) = e - n + 2P.",
        "note": "مقياس التعقيد الدوري من وضع مكيب (T. J. McCabe).",
    },
    32: {
        "ans": "**All three formulations are valid:** (a) V(G) = e - n + 2P, (b) V(G) = π + 1, where π is the number of predicate nodes, and (c) V(G) = the number of regions of the flow graph.",
        "note": "الطرق الثلاث صحيحة: e-n+2P (حيث P عدد المكونات المتصلة)، وπ+1 (حيث π عدد عقد القرار)، وعدد المناطق. لذلك الإجابة (d).",
    },
    33: {
        "ans": "**The equation V(G) = π + 1 applies only if every predicate node has two outgoing edges.** A node with three or more outgoing edges breaks the simple +1 rule.",
        "note": "صيغة π+1 تصح فقط إذا كان لكل عقدة قرار مخرجان اثنان بالضبط.",
    },
    41: {
        "ans": "**Regression testing is a testing activity, not a debugging technique.** Core dumps, traces and print statements are debugging aids; debugging begins after a failure symptom is found and locates the place and cause of the error.",
        "note": "Regression فحص وليس أسلوب تنقيح. التنقيح يبدأ بعد ظهور العَرَض ويحدد مكان الخطأ وسببه.",
    },
    48: {
        "ans": "**Publisher key: (b) identification of faults.** The deck shows top-down as one of the three integration approaches (Fig. 30) but gives no sentence tying it to this option, so treat it as a keyed fact.",
        "note": "مفتاح الناشر (b). السلايد 175 يعرض الفحص التنازلي (Top-down) كأحد أساليب التكامل دون جملة تفسّر هذا الخيار، فاحفظ المفتاح.",
    },
    49: {
        "ans": "**Publisher key: (d) all of the above.** The chapter text does not define thread testing; the term appears only in this question, so treat it as a keyed fact.",
        "note": "المفتاح الرسمي (d). مصطلح Thread testing يرد في هذا السؤال فقط ولا يُشرح في نص الفصل، فاحفظه كمفتاح.",
    },
}
for _n, _o in OVR.items():
    DATA[_n].update(_o)

# Section start pages come from the printed table of contents (p. xvii); slide
# numbers are the companion-deck pages that state or illustrate the point.
SECTION = {
    1: "§8.1.1 (p. 365); slide 3", 2: "§8.2.1 (p. 369); slide 9", 3: "§8.3 (p. 371); slide 13",
    4: "§8.3.1 (p. 372); slides 15, 20", 5: "§8.3.1 (p. 372); slides 24–25", 6: "§8.3.1 (p. 372); slide 24",
    7: "no explanatory slide; publisher key", 8: "§8.4 (p. 406); flow-graph background, slide 105",
    9: "§8.4 (p. 406); flow-graph background, slide 105", 10: "§8.3.3 (p. 395); slide 77",
    11: "§8.2.4 (p. 370); slide 12", 12: "§8.3.2 (p. 390); slides 61–62", 13: "§8.3.4 (p. 402); slide 92",
    14: "§8.2.3 (p. 370); slides 11, 178", 15: "§8.2.3 (p. 370); slide 11", 16: "§8.2.3 (p. 370); slides 11, 176",
    17: "§8.2.4 (p. 370); slide 12", 18: "§8.2.4 (p. 370); slide 12", 19: "§8.2.4 (p. 370); slide 12",
    20: "§8.2.4 (p. 370); slides 12, 178", 21: "§8.2.1 (p. 369); slide 9", 22: "§8.2.2 (p. 369); slide 10",
    23: "no explanatory slide; publisher key", 24: "§8.2.4 (p. 370) and §8.5 (p. 435); slides 12, 170, 178",
    25: "§8.3 (p. 371); slide 13", 26: "§8.3.3 (p. 395); slide 77", 27: "§8.3.4 (p. 402); slide 92",
    28: "§8.3.4 (p. 402); slide 92", 29: "§8.4.1 (p. 407); slides 112, 116", 30: "§8.4.1 (p. 407); slides 117–118",
    31: "§8.4.2 (p. 422); slide 132", 32: "§8.4.2 (p. 422); slides 132, 138", 33: "§8.4.2 (p. 422); slide 138",
    34: "§8.4.3 (p. 426); slide 147", 35: "§8.4.3 (p. 426); slide 147", 36: "§8.4.2 (p. 422); slide 134",
    37: "§8.4.4 (p. 430); slide 155", 38: "§8.4.4 (p. 430); slides 157–158", 39: "§8.4.5 (p. 430); slide 167",
    40: "§8.5.1 (p. 436); slide 172", 41: "§8.7 (p. 441); slides 180–185", 42: "§8.2.1 (p. 369); slide 9",
    43: "§8.2.4 (p. 370); slides 12, 178", 44: "§8.2.3 (p. 370); slides 11, 178", 45: "§8.2.3 (p. 370); slide 11",
    46: "§8.5.2 (p. 437); slide 175", 47: "§8.3 (p. 371); slide 13", 48: "§8.5.2 (p. 437); slide 175",
    49: "no explanatory slide; publisher key", 50: "§8.2.4 (p. 370); slide 12",
}
MCQ_SLIDE = {}
for _page, _ids in {189: (1, 2, 3, 4), 190: (5, 6, 7, 8, 9), 191: (10, 11, 12, 13, 14), 192: (15, 16, 17, 18),
                    193: (19, 20, 21, 22, 23), 194: (24, 25, 26, 27), 195: (28, 29, 30, 31), 196: (32, 33, 34),
                    197: (35, 36, 37, 38), 198: (39, 40, 41, 42, 43), 199: (44, 45, 46, 47, 48), 200: (49, 50)}.items():
    for _i in _ids:
        MCQ_SLIDE[_i] = _page
for _n in range(1, 51):
    DATA[_n]["src"] = (f"Aggarwal & Singh (3rd ed.), question printed pp. 451–455, publisher key p. 499; "
                       f"{SECTION[_n]}; question on slide {MCQ_SLIDE[_n]}.")

# Now let's build the full Markdown document
md_out = []
md_out.append("---")
md_out.append('title: "ASE Chapter 8 — T1 Multiple-Choice Questions Pack"')
md_out.append('course: "Advanced Software Engineering (CS603)"')
md_out.append('instructor: "Asst. Prof. Dr. Ali Fahim Ni\'ma"')
md_out.append('author: "Master Studio Engine"')
md_out.append('date: "2026-10-22"')
md_out.append('lang: "en"')
md_out.append("---")
md_out.append("")
md_out.append("# ASE Chapter 8 — T1 Multiple-Choice Questions Pack")
md_out.append("")
md_out.append("<!-- Print-hidden metadata: All 50 textbook/slide MCQs keyed against the official publisher answer key in Aggarwal & Singh (3rd ed., p. 499). -->")
md_out.append("")
md_out.append("---")
md_out.append("")

for num in range(1, 51):
    q_key = f"8.{num}"
    body = raw_dict.get(num, "")
    
    # Split stem and options
    # Find options (a), (b), (c), (d)
    opt_matches = list(re.finditer(r'\(([a-d])\)\s*([\s\S]*?)(?=(?:\([a-d]\))|$)', body))
    if opt_matches:
        stem = body[:opt_matches[0].start()].strip()
        # Clean stem
        stem = re.sub(r'\s+', ' ', stem)
        opts = {}
        for om in opt_matches:
            letter = om.group(1).lower()
            val = om.group(2).strip()
            val = re.sub(r'\s+', ' ', val)
            opts[letter] = val
        opts_line = f"(a) {opts.get('a','')} · (b) {opts.get('b','')} · (c) {opts.get('c','')} · (d) {opts.get('d','')}"
    else:
        stem = body
        opts_line = "(a) · (b) · (c) · (d)"
    
    key_letter = OFFICIAL_KEYS[num]
    d = DATA[num]
    # The bold key line repeats the scanned option text for the keyed letter, so
    # the letter and its wording can never disagree.
    key_text = opts[key_letter] if opt_matches else d['text']
    if opt_matches:
        # Normalise glyphs extracted from the scan: the predicate symbol is pi.
        opts_line = opts_line.replace('∏', 'π')
        stem = stem.replace('∏', 'π')
        key_text = key_text.replace('∏', 'π').rstrip('.')
    
    md_out.append('<div class="no-break">')
    md_out.append("")
    md_out.append(f"### Q{q_key}. {stem}")
    md_out.append(f"{opts_line}")
    md_out.append("{: .keep-next }")
    md_out.append(f"> **({key_letter}) {key_text}**")
    md_out.append(">")
    md_out.append(f"> {d['ans']}")
    md_out.append(">")
    md_out.append(f"> *Source: {d['src']}*")
    md_out.append("")
    md_out.append("> [!NOTE]")
    md_out.append("> **ملاحظة الطالب والفخ الامتحاني:**")
    md_out.append(">")
    md_out.append(f"> {d['note']}")
    md_out.append("")
    md_out.append("</div>")
    md_out.append("")
    md_out.append("---")
    md_out.append("")

md_out.append("<!-- Print-hidden study guidance retained for screen use.")
md_out.append("## Retrieval Set & Active Recall Self-Test")
md_out.append("")
md_out.append("Use the questions in this pack for active recall:")
md_out.append("- Cover the model answer and notes for each question.")
md_out.append("- Articulate the correct option and the technical justification before revealing the key.")
md_out.append("- Verify distinguishing criteria between functional testing (black-box) and structural testing (white-box).")
md_out.append("-->")
md_out.append("")

out_path = os.path.join(CH08_DIR, "T1_MCQ.md")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_out))

print(f"Generated {out_path} successfully. Total lines: {len(md_out)}")
