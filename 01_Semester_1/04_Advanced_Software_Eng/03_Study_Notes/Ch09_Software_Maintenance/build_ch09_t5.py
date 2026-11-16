import os

out_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance"
md_path = os.path.join(out_dir, "T5_Apply_Select.md")

content = r"""# Advanced Software Engineering — Chapter 9: Software Maintenance
## T5: Applied Decisions & Scenario Matrices

### Scenario 1: Maintenance Process Model Selection Across Industrial Profiles

**Context & Problem:**
An engineering director must select the most appropriate software maintenance process model for four distinct organizational scenarios based on system criticality, architectural health, and regulatory constraints.

**Engineering Evaluation & Model Allocation:**

1. **System A — Production Security Emergency (Critical Zero-Day Vulnerability):**
   - **Recommended Model:** **Quick-Fix Model**
   - **Technical Rationale:** The overriding operational objective is instantaneous fault containment and service restoration. Quick-Fix permits immediate source patching at the code level.
   - **Mandatory Compensating Action:** Post-incident reconciliation is strictly enforced to update the SRS, architecture descriptions, and test suites, preventing documentation desynchronization and software entropy.

2. **System B — Well-Architected Core Banking Platform (Major Regulatory Feature Enhancement):**
   - **Recommended Model:** **Iterative Enhancement Model**
   - **Technical Rationale:** The system has high-quality design artifacts and documentation. The 3-stage cycle (**Analysis $\to$ Redesign $\to$ Implementation**) ensures that new functional capabilities are redesigned cleanly into the existing architecture, modifying design documents prior to code implementation.

3. **System C — Mission-Critical Avionics Control (Stringent Audit & Verification Regulations):**
   - **Recommended Model:** **Taute Maintenance Model**
   - **Technical Rationale:** Avionics safety standards require an unbroken audit trail. Taute's **eight sequential phases** (Request $\to$ Assign $\to$ Estimate $\to$ Schedule $\to$ Change $\to$ Retest $\to$ Audit $\to$ Release) enforce formal sign-offs and verification gates at each step.

4. **System D — Component-Based Enterprise Resource Planning (ERP):**
   - **Recommended Model:** **Reuse-Oriented Model**
   - **Technical Rationale:** When maintaining an object-oriented or modular component-based architecture, maintenance objectives are achieved by identifying existing reusable software assets, analyzing their interfaces, modifying them, and integrating them back into the architecture.

> [!NOTE]
> **معيار الاختيار الهندسي:** يُحظر استخدام نموذج (Quick-Fix) للتطويرات الروتينية لأنه يدمر المعمارية، ويُقتصر استخدامه على الطوارئ بشرط التحديث اللاحق للوثائق. بينما يُعد (Iterative Enhancement) الأنسب للأنظمة الموثقة، و(Taute) للأنظمة الخاضعة لرقابة تدقيقية صارمة.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 466–469; Slides 13–21.

---

### Scenario 2: Legacy Code Modification Strategy & Textbook Guidelines (Exercise 9.29)

**Context & Problem:**
A maintenance team inherits an undocumented 15-year-old operational software system. Management tasks the team with modifying several core modules without destabilizing the system. The team must apply the canonical suggestions provided in the reference textbook for modifying legacy code (Exercise 9.29).

**Authoritative Textbook Recommendations (Aggarwal & Singh, p. 480; Slide 49):**

1. **Study code well before attempting changes:**
   - Engineers must perform comprehensive static and dynamic program understanding prior to making any edits. Comprehending existing execution semantics prevents erroneous assumptions.
2. **Concentrate on overall control flow and not coding:**
   - Focus on module interconnections, calling hierarchies, and global execution paths rather than micro-level line-by-line syntax optimizations.
3. **Heavily comment internal code:**
   - Annotate legacy functions with detailed descriptive headers, parameter explanations, side-effect warnings, and modification histories to rebuild lost tacit knowledge.
4. **Create Cross References:**
   - Map variable and function occurrences across all source files to identify shared globals and hidden interdependencies.
5. **Build Symbol tables:**
   - Reconstruct explicit inventories of data structures, types, identifiers, and scope rules to clarify data definitions.
6. **Use own variables, constants, and declarations to localize the effect:**
   - Avoid mutating shared legacy variables or global accumulators directly. Define localized variables and explicit parameters to insulate existing code blocks from unexpected state corruption.
7. **Keep detailed maintenance document:**
   - Maintain a dedicated maintenance journal recording every change, rationale, affected lines, and verification outcomes to establish an audit trail.
8. **Use modern design techniques:**
   - When adding new modules or refactoring existing ones, employ structured programming and modern architectural patterns to raise the system's maintainability baseline.

> [!NOTE]
> **التطابق مع المصدر المعتمد:** هذه التوصيات الثماني مستخرجة حرفياً من كتاب أجاروال وسينغ ص 480 وشريحة المحاضرة 49، وهي تمثل الإجابة المباشرة المعتمدة امتحانياً للتمرين 9.29 حول تعديل الكود الموروث (Legacy Code).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, p. 480; Slide 49.

---

### Scenario 3: Selective Regression Test Execution Analysis on Code Deltas

**Context & Problem:**
Following a corrective maintenance patch to a shared utility module, a test manager must decide between executing the entire test suite (**Retest-All**) versus executing a **Selective Retest Suite** using safe, coverage-based, or minimization techniques.

**Evaluation Framework (Rothermel & Harrold Criteria; Aggarwal & Singh, pp. 474–475):**

1. **Retest-All Strategy:**
   - **Mechanism:** Executes every test case in the baseline test suite $T$.
   - **Trade-off Analysis:** Offers $100\%$ fault coverage safety but incurs maximum computational cost and execution time. Unviable for large commercial systems undergoing continuous patches.

2. **Selective Retest Strategy:**
   - **Mechanism:** Identifies a subset $T' \subseteq T$ that traverses code blocks affected by modification $\Delta P$.
   - **Evaluation Across the Four Standard Criteria (Slide 39 / p. 475):**
     - **Inclusiveness:** Measures the extent to which the technique selects test cases that reveal modification-induced faults. A *safe* technique achieves $100\%$ inclusiveness by selecting all tests whose execution paths are modified.
     - **Precision:** Measures the ability to exclude test cases that do not traverse modified code paths. Higher precision eliminates redundant executions.
     - **Efficiency:** The computational effort required to run the selection algorithm versus the execution time saved.
     - **Generality:** The applicability of the selection technique across diverse programming languages and control paradigms.

3. **Minimization Danger:**
   - **Cautionary Rule:** Test suite minimization seeks the smallest subset covering modified blocks. However, minimization is non-safe because dropping tests with identical structural coverage can miss subtle semantic defects triggered by different data values.

> [!NOTE]
> **القاعدة الامتحانية:** تُعد التقنيات الآمنة (Safe Techniques) هي المعيار الأضمن في فحص الانحدار الانتقائي لأنها تضمن نسبة شمولية (Inclusiveness = 100%)، في حين أن تقنيات التقليص (Minimization) قد توفر وقتاً لكنها تخاطر بإسقاط اختبارات حيوية تكشف أخطاء دلالية مستترة.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 473–475; Slides 32–39.

---

### Scenario 4: SCM Change Control Lifecycle & CCA Governance

**Context & Problem:**
An urgent customer request requires modifying the billing calculation algorithm in an operational enterprise system. The modification must progress through the four canonical SCM activities and pass Configuration Control Authority (CCA) governance.

**End-to-End Governance Lifecycle (Aggarwal & Singh, pp. 484–486; Slides 54–58):**

1. **SCM Activity 1: Component & Change Identification:**
   - The requester submits a formal **Change Request Form** (Fig. 9.14) recording: Project ID, Requester name, Date, and Description of the proposed billing logic update.
   - Configuration items are identified: billing module source files, SRS Section 4.2, and billing test suites.

2. **SCM Activity 2: Change Control & CCA Decision:**
   - The change analyzer evaluates the request, estimating costs, priority, affected components, and associated ripple effects.
   - The form is submitted to the **Configuration Control Authority (CCA)**.
   - The CCA reviews technical feasibility and business impact, issuing an official verdict (**Approved**).

3. **SCM Activity 3: Change Implementation & Quality Audit:**
   - The designated change implementer modifies source code, updates SRS specifications, and modifies test procedures.
   - The modified components are submitted to Quality Assurance (QA) along with regression test results. QA verifies that the modification meets requirements without side effects and signs the QA decision.

4. **SCM Activity 4: Status Accounting & Baseline Update:**
   - The change is delivered to Configuration Management (CM).
   - Version control tools record a new **revision** (replacement baseline), documenting the author, timestamp, compiler versions, and modified artifacts.
   - Status accounting records the complete history in the project audit ledger.

> [!NOTE]
> **التسلسل الإداري الصارم:** تنتقل الاستمارة رسمياً بين أربع جهات: المحلل (Analyzer) $\to$ سلطة التحكم بالتوصيف (CCA) لاتخاذ القرار $\to$ المنفذ (Implementer) $\to$ توكيد الجودة (QA) للفحص والاعتماد $\to$ إدارة التوصيف (CM) لتوثيق الإصدار الجديد (Revision).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 484–486; Slides 54–58.

---

### Scenario 5: Legacy Software Modernization Strategy — Re-engineer vs New Development

**Context & Problem:**
An enterprise relies on a legacy transaction processor written in an obsolete language running on aging hardware. Senior management must decide whether to continue standard maintenance, re-engineer the software, or commission entirely new software development.

**Comparative Modernization Evaluation (Aggarwal & Singh, p. 481; Slide 48):**

1. **Re-engineering Paradigm (Understanding & Transformation):**
   - **Process:** Existing Software System $\to$ Reverse Engineering (understanding) $\to$ Transformation / Restructuring $\to$ Re-engineered System.
   - **Advantages:**
     - **Lower Risk:** Preserves core business rules embedded in legacy code.
     - **Lower Cost:** Leverages existing intellectual assets rather than rebuilding from zero.
     - **Faster Delivery:** Incremental restructuring delivers usable updates sooner than greenfield development.

2. **New Software Development Paradigm:**
   - **Process:** System Specification $\to$ Design & Implementation $\to$ New System.
   - **Trade-offs:**
     - High architectural freedom allowing modern tech stacks.
     - Severe risk of omitting undocumented, tacit business logic accumulated over years of maintenance.
     - Significantly higher initial capital expenditure and schedule risk.

3. **Economic Decision Framework (Sneed's Rule of Re-engineering):**
   - Software re-engineering is economically justified only when the estimated cost of re-engineering ($C_{\text{reeng}}$) satisfies:
     $$C_{\text{reeng}} \le 0.5 \times C_{\text{new}}$$
   - If re-engineering costs exceed $50\%$ of complete new development, commissioning new development or purchasing a modern package becomes the superior economic decision.

> [!NOTE]
> **المعادلة الاقتصادية الحاسمة:** تعتمد المفاضلة على تقليل المخاطر واحتواء التكاليف. إعادة الهندسة تحافظ على القواعد التجارية المجربة (Business Rules) بتكلفة أقل، وتكون مجدية اقتصادياً عندما لا تتجاوز تكلفتها 50% من تكلفة بناء نظام جديد من الصفر.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 480–482; Slide 48 (Fig. 9.12).

---

<!-- The following retrieval set provides active recall verification for applied decision scenarios -->
## Retrieval Set & Active Recall Self-Test

1. In Scenario 1, justify why the Quick-Fix model is acceptable for emergency vulnerability patching but prohibited for routine banking system enhancements.
2. State the eight canonical recommendations provided in the textbook for modifying legacy code (Exercise 9.29).
3. In Scenario 3, why is a safe regression test selection technique preferred over test suite minimization in mission-critical deployments?
4. What are the four core configuration management activities, and what authority grants formal change approval in Scenario 4?
5. Under Sneed's economic rule, what is the maximum cost threshold for justifying software re-engineering over new development?
"""

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Generated {md_path} successfully.")
