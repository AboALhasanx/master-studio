# Chapter 8 — Software Testing

**Skeleton**

- **State the purpose.** Testing executes the product to find defects and to build justified confidence that behaviour matches requirements; it cannot prove absence of defects.
- **Explain why exhaustive testing fails.** The input domain is effectively infinite, and path count explodes combinatorially with loops and branches.
- **Fix the vocabulary.** Mistake (human action), fault/defect (latent in the artifact), error (incorrect internal state), failure (observable deviation). A fault can produce zero, one, or many failures.
- **Separate verification from validation.** Verification asks "did we build the product right?" against the specification; validation asks "did we build the right product?" against user need.
- **Design black-box tests from the specification.** Boundary value analysis, robustness, worst-case, equivalence partitioning, decision tables, cause-effect graphing.
- **Design white-box tests from the code.** Flow graph, DD-paths, independent paths, cyclomatic complexity, graph and connection matrices, data-flow testing, mutation testing.
- **Apply the right level.** Unit (drivers and stubs), integration (top-down, bottom-up, sandwich), system (operational attributes), acceptance (alpha and beta), regression after every change.
- **Debug after failure.** Inductive debugging builds a hypothesis from observations; deductive debugging eliminates candidate causes until one survives.

**Keywords**

- **Verification / validation** — Spec compliance vs user need — <span dir="rtl">التحقق / الإثبات</span>
- **Fault / error / failure** — Defect, bad state, observable symptom — <span dir="rtl">خطأ كامن / حالة خاطئة / فشل</span>
- **Test case / suite / data** — Input, expected output, oracle — <span dir="rtl">حالة اختبار / مجموعة / بيانات</span>
- **Oracle** — Mechanism deciding pass or fail — <span dir="rtl">معيار الحكم</span>
- **Black-box testing** — Specification-driven, no internals — <span dir="rtl">الاختبار الصندوقي الأسود</span>
- **BVA** — min, min+, nominal, max−, max — <span dir="rtl">تحليل القيم الحدية</span>
- **Robustness testing** — Adds min− and max+ — <span dir="rtl">اختبار المتانة</span>
- **Worst-case testing** — Full cross-product of extremes — <span dir="rtl">اختبار أسوأ الحالات</span>
- **Equivalence partitioning** — One representative per class — <span dir="rtl">تقسيم فئات التكافؤ</span>
- **Decision table** — Conditions × actions × rules — <span dir="rtl">جدول القرار</span>
- **Cause-effect graphing** — Boolean causes to effects, then table — <span dir="rtl">مخطط السبب والأثر</span>
- **White-box testing** — Structure-driven — <span dir="rtl">الاختبار الصندوقي الأبيض</span>
- **Flow graph** — Nodes and edges of control flow — <span dir="rtl">مخطط التدفق</span>
- **DD-path** — Decision-to-decision path — <span dir="rtl">مسار قرار إلى قرار</span>
- **Cyclomatic complexity** — V(G) independent paths — <span dir="rtl">التعقيد الدوري</span>
- **Data-flow testing** — DEF and USE nodes, du paths — <span dir="rtl">اختبار تدفق البيانات</span>
- **Mutation testing** — Mutants killed by the suite — <span dir="rtl">اختبار الطفرات</span>
- **Driver / stub** — Test harness above and below the unit — <span dir="rtl">محرك / بديل</span>
- **Regression testing** — Re-run to detect reintroduced defects — <span dir="rtl">اختبار الانحدار</span>

**Facts, numbers, formulas**

- **Boundary value analysis.** For $n$ independent variables: $T_{\text{BVA}}=4n+1$ (min, min+, nominal, max−, max for each, plus the all-nominal case).
- **Robustness testing.** $T_{\text{robust}}=6n+1$, adding min− and max+ per variable.
- **Worst-case testing.** $T_{\text{worst}}=5^{n}$ (full cross-product of the five boundary points).
- **Robust worst-case.** $T_{\text{robust worst}}=7^{n}$, adding both invalid bounds to every combination. For two variables the four counts are $9, 13, 25, 49$; for three variables $13, 19, 125, 343$.
- **Cyclomatic complexity.** V(G) = E - N + 2P; also predicate nodes + 1; also the number of bounded regions. V(G) gives an upper bound on the number of independent paths in a basis set, and therefore a minimum target for branch coverage.
- **Independent paths.** A basis set contains V(G) linearly independent paths; adding more paths adds combinations, not new basis vectors.
- **Data-flow testing.** A definition (DEF) node assigns a value; a use (USE) node reads it, either as a predicate use (p-use) in a branch or a computation use (c-use). A definition-use path (du-path) runs from a definition to a use with no intervening redefinition; a definition-clear path (dc-path) contains no redefinition of that variable. Anomalies: defined-but-never-used, used-before-defined, double definition.
- **Mutation testing.** Each mutant contains one syntactic change; the suite *kills* a mutant if some test fails on it. Equivalent mutants cannot be killed and must be excluded from the score.
- **Levels.** Unit testing isolates one module with drivers (callers) and stubs (callees). Integration combines modules and tests interfaces: top-down needs stubs, bottom-up needs drivers, sandwich mixes both. System testing covers usability, security, compatibility, dependability, documentation. Acceptance testing is user-facing: alpha on the developer site, beta at the customer site.
- **Regression.** Re-run the existing suite after a change; selection strategies range from retest-all to safe, coverage-based, and minimization-based subsets.

**Technique at a glance — basis, strength, blind spot**

| Technique | Basis | Finds | Cannot find |
|:--|:--|:--|:--|
| BVA | Boundaries of each variable | Off-by-one and threshold defects | Interaction between variables |
| Robustness | Boundary plus invalid extremes | Input validation gaps | Cross-variable combinations |
| Worst-case | Cross-product of extremes | Combination defects | Path or state defects |
| Equivalence partitioning | Input classes | Representative class defects | Defects inside a class |
| Decision table | Condition and action combinations | Missing and contradictory rules | Timing or sequence behaviour |
| Cause-effect graphing | Boolean causes to effects | Logical dependency errors | Performance behaviour |
| DD-path / independent paths | Control-flow graph | Unreachable or untested branches | Data dependencies |
| Data-flow testing | DEF and USE sets | Definition-use anomalies | Control-flow-only defects |
| Mutation testing | One syntactic change per mutant | Weak assertions in the suite | Equivalent mutants |
| System testing | Operational attributes | Usability, security, compatibility gaps | Internal code defects |

**Traps**

- **"Testing proves correctness."** It cannot. It finds defects and provides evidence; correctness needs formal verification or exhaustive testing, both usually infeasible.
- **Confusing error and failure.** An error is an internal state; a failure is the external deviation. A fault may produce neither.
- **BVA world-count errors.** $4n+1$ is standard, $6n+1$ is robustness, $5^{n}$ is worst-case, $7^{n}$ is robust worst-case. The exponent is the giveaway.
- **"Cyclomatic complexity equals the number of paths."** It equals the size of a *basis*, an upper bound on independent paths, not the total path count.
- **Data-flow testing is not DFD testing.** One works on DEF/USE sets in code; the other is a requirements modelling notation.
- **Mutation score without equivalent mutants.** Reporting a score that counts unfixable equivalents as live mutants understates quality.
- **Top-down versus bottom-up.** Top-down needs stubs, bottom-up needs drivers; naming them backwards is the classic loss.
- **Thread testing.** It appears in the question bank but is not developed in the lecture body; keep it question-level, not a core concept.

**Three lines**
Testing is sampling, so name the adequacy criterion before claiming coverage.
Black-box techniques choose *inputs*, white-box techniques choose *paths*, and neither subsumes the other.
Every level has a harness: drivers above, stubs below, and regression after every change.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Verification | Conformance to the specification as written | مطابقة المواصفة |
| Validation | Conformance to the intended user need | مطابقة الحاجة |
| BVA | Testing at and around boundaries: min, min+, nominal, max-, max | القيم الحدية |
| Cyclomatic complexity | Basis size of independent paths in a flow graph | حجم الأساس |
| DD-path | A decision-to-decision path between branch points | مسار بين قرارين |
| Mutation testing | Altering code to check whether the suite detects the change | قياس قوة الاختبار |

**Question patterns**

- **"Design tests for a numeric range"** → BVA with $4n+1$, robustness $6n+1$, worst-case $5^n$, robust worst-case $7^n$. Give the count before the cases.
- **"Design tests for business rules"** → decision table: conditions, actions, rules, then one test per feasible rule and one per contradiction.
- **"Compute $V(G)$"** → edges minus nodes plus twice the components; then state that it bounds the size of a basis set, not the total path count.
- **"Which technique catches this defect?"** → boundary defects by BVA, rule defects by decision tables, path defects by structural testing, data defects by du-paths, weak assertions by mutation.
- **"Unit, integration or system?"** → unit isolates logic with drivers and stubs, integration tests interfaces, system tests operational attributes, acceptance tests user need.
- **"Top-down or bottom-up integration?"** → top-down needs stubs and validates the architecture early; bottom-up needs drivers and validates components early. Sandwich trades both.
- **"Compute the mutation score"** → killed over non-equivalent mutants. Exclude equivalents explicitly or the score is meaningless.
- **"Verification or validation?"** → specification versus need. One can pass while the other fails, and that gap is the classic exam answer.
- **"What should regression select?"** → a subset that is safe, precise, efficient and general; retest-all is safe but rarely affordable.

## الاسترجاع
AR:الاختبار أخذ عينات من فضاء مدخلات ومسارات غير منتهٍ، وكل تقنية تحدّد ما تستطيع رؤيته وما هي مضمونة ألا تراه، ولهذا لا يثبت الاختبار الصحة بل يكشف العيوب ويبني ثقة مبررة. والمصطلحات تتدرج من الخطأ البشري إلى العيب الكامن إلى الحالة الخاطئة إلى الفشل المرصود، والتحقق يطابق المواصفة بينما الإثبات يطابق حاجة المستخدم. وتُصمّم الحالات من الخارج بتحليل القيم الحدية، أربع نقاط لكل متغير زائد حالة اسمية، ثم اختبار المتانة الذي يضيف الحدين غير الصالحين، ثم أسوأ الحالات الذي يأخذ الجداء الديكارتي، ثم تقسيم فئات التكافؤ وجداول القرار ومخططات السبب والأثر. ومن الداخل تُصمّم من مخطط التدفق: مسارات قرار إلى قرار، ومسارات مستقلة بعدد التعقيد الدوري، ومصفوفات الاتصال، واختبار تدفق البيانات الذي يتابع مسارات التعريف والاستخدام ويكشف الشذوذات، واختبار الطفرات الذي يقيس قوة مجموعة الاختبار. ثم تُطبّق المستويات: وحدة بمحركات وبدائل، وتكامل من الأعلى أو الأسفل أو مختلط، ونظام، وقبول ألفا وبيتا، وانحدار بعد كل تغيير.
