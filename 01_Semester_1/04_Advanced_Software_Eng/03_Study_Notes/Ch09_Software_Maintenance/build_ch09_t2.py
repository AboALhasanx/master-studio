import os

out_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance"
md_path = os.path.join(out_dir, "T2_Descriptive.md")

content = r"""# Advanced Software Engineering — Chapter 9: Software Maintenance
## T2: Descriptive & Conceptual Exercises

### Q9.D1 (Exercise 9.1): Definition, Categories & Dominant Effort in Software Maintenance
**Question:**
What is software maintenance? Describe various categories of maintenance. Which category consumes maximum effort and why?

Software maintenance is defined (IEEE 610.12) as the modification of a software product after delivery to correct faults, improve performance or other attributes, or adapt the product to a modified environment.

The chapter establishes four categories of software maintenance:

1. **Corrective Maintenance:** Reactive modifications performed to correct latent residual faults discovered during operation.
2. **Adaptive Maintenance:** Modifications performed to keep software usable in a changing external operating environment (operating systems, hardware platforms, or database upgrades).
3. **Perfective Maintenance:** Enhancements implemented to satisfy new or modified user requirements, optimize execution speed and resource consumption, or refine software maintainability.
4. **Preventive Maintenance:** Proactive modifications performed to detect and correct latent faults or improve internal structure before failures manifest in operational execution.

**Effort Distribution:**
- **Perfective Maintenance:** **50%**
- **Adaptive Maintenance:** **25%**
- **Corrective Maintenance:** **21%**
- **Preventive Maintenance:** **4%**

**Why Perfective Consumes Maximum Effort:**
Perfective maintenance consumes half of all maintenance expenditures because software systems evolve with organizational business needs. As end-users gain operational experience with software, they identify new workflow efficiencies and demand functional extensions, continually expanding the feature backlog far beyond error rectification.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 459–461; Slides 2–5.

---

### Q9.D2 (Exercise 9.2): Maintenance Implications for a One-Person Organization
**Question:**
What are the implications of maintenance for a one-person software production organization?

In a single-developer software production enterprise, maintenance creates severe operational constraints:

1. **Resource Exhaustion:** Because one individual must balance ongoing development, customer support, and defect rectification, maintenance requests consume available engineering hours, halting new development.
2. **Absence of Independent Review:** The developer acts as their own tester and reviewer, increasing susceptibility to cognitive confirmation bias during patch verification.
3. **Severe Tacit Knowledge Vulnerability:** Architectural rationale, code quirks, and operational assumptions remain in the sole developer's memory rather than in synchronized documents, creating a critical single point of failure (bus factor = 1).
4. **Code Entropy:** Under pressure to restore operational service, the lone programmer frequently applies code patches without updating requirements or design artifacts, accelerating architectural decay.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 461–463; Slides 6–7.

---

### Q9.D3 (Exercise 9.4): Major Maintenance Problems & Practical Solutions
**Question:**
Discuss various problems during maintenance. Describe some solutions to these problems.

**Major Maintenance Problems:**
1. **Unstructured & Undocumented Legacy Code:** Software developed without adherence to structured programming principles or lacking design documentation requires heavy cognitive effort to comprehend.
2. **Personnel Turnover:** When maintenance is conducted by engineers who did not build the system, comprehension time increases significantly.
3. **Ripple Effect:** Modifications in one module unintentionally break dependent variables or control flows elsewhere in the system.
4. **Outdated Test Suites:** Missing or outdated test suites prevent maintainers from verifying whether baseline functionality was preserved.
5. **Organizational Neglect:** Viewing maintenance as low-prestige custodial work results in assigning novice staff and underfunding documentation efforts.

**Practical Engineering Solutions:**
1. **Maintainability Standards:** Enforce coding guidelines, low module coupling, and Single-Entry Single-Exit (SESE) modularity during development.
2. **Mandatory Documentation Synchronization:** Require updating design specifications, data dictionaries, and user manuals before approving code changes.
3. **Configuration Control Authority (CCA):** Route all modification requests through a standard Change Request Form evaluated by a formal CCA.
4. **Automated Regression Test Harnesses:** Maintain automated test suites to verify that modifications do not introduce defect regressions.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 461–463; Slides 6–8.

---

### Q9.D4 (Exercise 9.6): Importance of Maintenance & Category Effort Share
**Question:**
Explain the importance of maintenance. Which category consumes maximum effort and why?

Software maintenance preserves large capital investments and ensures organizational operational continuity:

1. **Investment Protection:** Prolongs the operational lifespan of mission-critical systems and maximizes return on investment.
2. **Business Continuity:** Prevents operational degradation and obsolescence as business processes evolve.
3. **Environment Adaptation:** Adapts software to evolving external hardware, OS platforms, and communication protocols.

**Effort Share:**
Perfective maintenance consumes the maximum effort (**50%**), followed by Adaptive (25%), Corrective (21%), and Preventive (4%). It dominates because business evolution naturally demands new capabilities, performance tuning, and usability enhancements that outweigh simple error fixing.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 459–461; Slides 3–5.

---

### Q9.D5 (Exercise 9.7): Steps of Software Maintenance Process
**Question:**
Explain the steps of software maintenance with help of a diagram.

The software maintenance process progresses through four sequential phases driven by specific maintenance objectives and closed with a test gate:

1. **Maintenance Objective Formulation:** Initiated by one of four operational triggers: correcting program errors, adding new capabilities, deleting obsolete features, or optimizing execution/maintainability.
2. **Phase 1: Program Understanding:** Engineers analyze source code and design documentation. Governed by software quality attributes: **Complexity**, **Documentation**, and **Self-descriptiveness**.
3. **Phase 2: Generate Particular Maintenance Proposal:** A concrete modification plan is formulated. Governed by the attribute **Extensibility**.
4. **Phase 3: Account for Ripple Effect:** Engineers trace how changes affect dependent modules and data structures. Governed by the attribute **Stability** (resistance to change amplification).
5. **Phase 4: Modified Program Testing & Verification:** The modified system undergoes targeted regression testing. Governed by **Testability**.
   - If tests fail, the feedback loop returns control to Phase 1 or 2 for correction; if tests pass, the release is certified.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 463–465; Slide 10.

---

### Q9.D6 (Exercise 9.8): Self-Descriptiveness of Code & Maintenance Impact
**Question:**
What is self descriptiveness of a program? Explain the effect of this parameter on maintenance activities.

**Self-descriptiveness** refers to the degree to which source code explicitly conveys its intent, algorithmic purpose, and operational logic directly to an inspecting engineer without requiring external manuals.

**Key Indicators:**
- Meaningful, domain-aligned identifier and variable names.
- Clean modular structures reflecting problem domain concepts.
- Focused internal comments describing the rationale for non-obvious logic.

**Impact on Maintenance Activities:**
In Phase 1 of the maintenance process (Program Understanding), comprehending undocumented code accounts for over half of total maintenance labor. High self-descriptiveness accelerates mental model construction, shortens comprehension time, and lowers the probability of introducing unintended ripple bugs.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 464–465; Slide 11.

---

### Q9.D7 (Exercise 9.10): Maintainability Definition & Role During Maintenance
**Question:**
What is maintainability? What is its role during maintenance?

**Maintainability** is defined (IEEE 610.12) as the ease with which a software system or component can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment.

**Role in the Maintenance Lifecycle:**
Maintainability represents the combination of quality attributes supporting all four maintenance phases:
1. **Supports Program Understanding:** Driven by low structural complexity, clear documentation, and high self-descriptiveness.
2. **Facilitates Proposal Generation:** Supported by high architectural extensibility.
3. **Restrains Ripple Effects:** Enabled by high program stability and low modular coupling.
4. **Streamlines Validation:** Enabled by high testability and modular Single-Entry Single-Exit (SESE) designs.

High maintainability reduces the effort required per change unit, lowering life-cycle total cost of ownership.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 465–466; Slide 12.

---

### Q9.D8 (Exercise 9.11): Quick-Fix Model — Advantages & Disadvantages
**Question:**
Describe Quick-fix model. What are the advantages and disadvantages of this model?

The **Quick-Fix Model** modifies software directly at the source code level in response to a change request, releasing the patched code without updating requirements specifications, architectural designs, or documentation.

**Advantages:**
- **Instantaneous Turnaround:** Rapid execution; suitable for emergency operational fixes or critical zero-day vulnerabilities.
- **Minimal Initial Overhead:** Requires no upfront design restructuring or documentation sign-offs.

**Disadvantages:**
- **Architectural Degradation:** Code entropy increases with each patch, turning modular architectures into tangled logic.
- **Documentation Desynchronization:** Requirements and design documents become obsolete, complicating future maintenance.
- **High Ripple Risk:** Bypassing impact analysis frequently introduces severe regression defects.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 466–467; Slide 13.

---

### Q9.D9 (Exercise 9.12): Iterative Enhancement Model & Its 3-Stage Cycle
**Question:**
How is iterative enhancement model helpful during maintenance? Explain the various stage cycles of this model.

The **Iterative Enhancement Model** assumes that maintenance modifications must follow a disciplined, cyclic engineering process rather than ad-hoc code patching.

**The Three-Stage Cycle:**
1. **Analysis Stage:** Engineers analyze the proposed change against current system baselines, requirements, and design documentation to establish technical feasibility and scope.
2. **Redesign Stage:** Architecture and detailed designs are systematically modified to accommodate the change *before* code is touched, preserving structural integrity.
3. **Implementation Stage:** Code is modified according to the redesigned specifications, unit tested, and integrated back into the system baseline.

**Why It Is Helpful:**
It prevents code entropy by ensuring that documentation and architecture remain synchronized with code modifications across the entire operational lifespan.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 466–467; Slides 14–15.

---

### Q9.D10 (Exercise 9.14): Reuse-Oriented Maintenance Model in OO Design
**Question:**
State the various steps of reuse oriented model. Is it a recommended model in object oriented design?

The **Reuse-Oriented Maintenance Model** achieves modifications by identifying and integrating pre-existing, verified components.

**The Four Steps:**
1. **Identify Components for Reuse:** Search repository assets for modules meeting modification objectives.
2. **Analyze Components:** Evaluate components to ensure interface compatibility and functional fit.
3. **Modify Components:** Adapt selected components to satisfy exact operational requirements.
4. **Integrate into System:** Integrate modified components into the system architecture and conduct regression testing.

**Recommendation in Object-Oriented Design:**
**Yes**, it is recommended for Object-Oriented (OO) systems. OO paradigms (encapsulation, inheritance, polymorphism, and modular interfaces) provide well-defined class boundaries that facilitate component substitution and reuse without destabilizing unrelated subsystems.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 467–468; Slides 16–17.

---

### Q9.D11 (Exercise 9.15): Taute Maintenance Model & Sequential Phases
**Question:**
Describe the Taute maintenance model. What are various phases of this model?

The **Taute Maintenance Model** is an eight-phase cyclical maintenance governance model designed for structured software evolution:

1. **Change request:** Formal logging and initiation of a modification request.
2. **Estimate:** Technical estimation of effort, cost, and duration.
3. **Schedule:** Incorporating the change task into the release roadmap.
4. **Program:** Engineering modification of source code.
5. **Test:** Verification and regression testing of modified components.
6. **Documentation:** Synchronizing specifications, user guides, and system manuals.
7. **Release:** Deploying the approved release baseline to operational environments.
8. **Operation:** Monitoring software performance in production and logging future change requests (cycling back to phase 1).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), p. 469; Slide 20 (Fig. 9.7).

---

### Q9.D12 (Exercise 9.16): Belady & Lehman Maintenance Effort Estimation Model
**Question:**
Write a short note on Belady and Lehman model for the calculation of maintenance effort.

Belady and Lehman formulated an empirical macro-model capturing the non-linear dynamics of software maintenance effort:

$$M = P + K \cdot e^{c - d}$$

**Parameter Definitions:**
- $M$: Total maintenance effort expended.
- $P$: Productive baseline development effort involving original analysis, design, coding, testing, and evaluation.
- $K$: Empirically determined calibration constant.
- $c$: Measure of complexity resulting from poor design and inadequate documentation.
- $d$: Degree to which the maintenance engineering team is familiar with the software system.

The exponential term $e^{c - d}$ demonstrates that maintenance costs grow exponentially when system complexity ($c$) exceeds team familiarity and documentation clarity ($d$).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 470–471; Slides 23–25.

---

### Q9.D13 (Exercise 9.17): Maintenance Cost Estimation Models
**Question:**
Describe various maintenance cost estimation models.

1. **Defect Repair Cost Ratio Model (Table 3, Slide 22):**
   - Relative cost multiplier of fixing errors across lifecycle phases:
     $$\text{Analysis} : \text{Design} : \text{Implementation} = 1 : 10 : 100$$
2. **Belady-Lehman Empirical Model:**
   - Calculates total effort considering complexity and team familiarity:
     $$M = P + K \cdot e^{c - d}$$
3. **Boehm's COCOMO Annual Maintenance Effort (AME) Model:**
   - Based on Annual Change Traffic ($ACT$) scaling development effort ($SDE$) and environmental cost drivers ($EAF$):
     $$AME = ACT \times SDE \times EAF$$
     where $ACT = \frac{\text{KLOC}_{\text{added}} + \text{KLOC}_{\text{modified}}}{\text{KLOC}_{\text{total}}}$.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 470–473; Slides 22–31.

---

### Q9.D14 (Exercise 9.25): Reverse Engineering Definition & Levels of Abstraction
**Question:**
What is reverse engineering? Discuss levels of reverse engineering.

**Reverse engineering** is the process of analyzing an existing software system to identify its components and their interrelationships, and to create representations of the system at higher levels of abstraction.

**Levels of Abstraction (Fig. 9.11, Slide 45; Book p. 477):**
1. **Implementation Phase (Low Abstraction):** Source code, data files, compiler outputs, and low-level physical representations.
2. **Design Phase (Intermediary Abstraction):** Data flow diagrams, call graphs, module hierarchy charts, and software architecture descriptions.
3. **Specification Phase (High Abstraction):** System requirements specifications, functional models, and business rule definitions.

**Transformation Operations:**
- **Redocumentation:** Horizontal recreation of equivalent representations within the same abstraction level.
- **Design Recovery:** Vertical upward abstraction from Implementation to Design level.
- **Specification Recovery:** Vertical upward abstraction from Design to Specification level.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 476–478; Slides 41–46.

---

### Q9.D15 (Exercise 9.26): Reverse Engineering Tools & Detailed Discussion of Two
**Question:**
What are the appropriate reverse engineering tools? Discuss any two tools in detail.

Reverse engineering tools automate the extraction of syntactic and architectural abstractions from legacy code bases:

1. **Parsers (Syntactic Analysis Tools):**
   - Ingests raw source code, applies language grammar rules, and produces an Abstract Syntax Tree (AST) and symbol table.
   - Forms the front-end of reverse engineering pipelines, converting unstructured code into structured, traversable syntax nodes.
2. **Call-Graph Extractors (Control Flow Analyzers):**
   - Analyzes function invocations and inter-procedural control transfers to generate directed call graphs.
   - Enables maintainers to visualize calling hierarchies, identify root entry points, evaluate module coupling, and calculate ripple effect propagation paths before applying modifications.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 478–479; Slide 47.

---

### Q9.D16 (Exercise 9.29): Suggestions for Modifying Legacy Code
**Question:**
Discuss the suggestions that may be useful for the modification of the legacy code.

The course textbook specifies eight engineering guidelines when modifying legacy software:

1. **Study code well before attempting changes:** Perform static and dynamic analysis to comprehend operational behavior prior to making edits.
2. **Concentrate on overall control flow and not coding:** Understand calling hierarchies and global execution paths rather than line-by-line syntax details.
3. **Heavily comment internal code:** Add descriptive comments and rationale to clarify obscure routines for future maintainers.
4. **Create Cross References:** Build explicit maps of variable usages, function calls, and shared constants across all modules.
5. **Build Symbol tables:** Reconstruct data dictionary definitions and data structure scopes.
6. **Use own variables, constants and declarations to localize the effect:** Avoid modifying shared legacy variables directly; declare localized variables to isolate changes and prevent ripple regressions.
7. **Keep detailed maintenance document:** Maintain a modification history logging what was changed, why, and verification results.
8. **Use modern design techniques:** Apply structured programming and modern design abstractions to refactored sections.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), p. 480; Slide 49.

---

### Q9.D17 (Exercise 9.30): Types of Program Restructuring Techniques
**Question:**
Explain various types of restructuring techniques. How does restructuring help in maintaining a program?

**Program restructuring** modifies internal program structure without changing external observable behavior:

1. **Control Flow Driven Restructuring:**
   - Imposes structured programming constructs within source code, eliminating arbitrary jumps (`goto`), simplifying nested branches, and organizing code into Single-Entry Single-Exit (SESE) blocks.
2. **Efficiency Driven Restructuring:**
   - Restructures algorithms or routines to optimize runtime performance or memory utilization (e.g., replacing deeply nested `IF-THEN-ELSE-IF` ladders with a structured `CASE` construct).
3. **Adaption Driven Restructuring:**
   - Alters programming style to adapt the system to a new language paradigm or runtime environment (e.g., transforming imperative Pascal code into functional Lisp, or procedural code into object-oriented classes).

**How Restructuring Helps Maintenance:**
Restructuring eliminates spaghetti control flow, reduces cognitive comprehension overhead, localizes ripple effects, and establishes clean modular boundaries that make selective regression testing straightforward.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 482–483; Slides 51–53.

---

### Q9.D18 (Exercise 9.32): Configuration Management Activities & Change Control
**Question:**
What are configuration management activities? Draw the performa of change request form.

Software Configuration Management (SCM) controls the evolution of software products throughout development and maintenance through four activities:

1. **Identification of Components & Changes:** Uniquely labeling all baseline configuration items (specifications, designs, source files, test cases).
2. **Control of Changes:** Governing how modifications are proposed, analyzed, approved, and executed, managed formally by the **Configuration Control Authority (CCA)**.
3. **Auditing Changes:** Verifying that approved changes have been implemented accurately and that accompanying documentation is fully synchronized.
4. **Status Accounting:** Recording and reporting the complete historical ledger of baseline versions and change activity.

*(The complete 18-field performa of the Change Request Form is detailed in T4: Q9.F4).*

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 484–486; Slides 54–58.

---

### Q9.D19 (Exercise 9.33): Impact of Documentation Quantity/Quality on System Success
**Question:**
Explain why the success of a system depends heavily on the quantity of the documentation generated during system development.

Software maintenance accounts for **40% to 70%** of total lifecycle effort (Aggarwal & Singh, p. 459). Because maintenance engineers are rarely the original system developers, system survivability depends on documentation:

1. **Elimination of the Reverse-Engineering Tax:** Without comprehensive requirements (SRS) and architecture documents (SDD), maintainers must expend substantial effort reverse-engineering code simply to comprehend basic design intent.
2. **Containment of Ripple Effects:** Accurate data dictionaries and module interface specifications enable maintainers to trace data-flow linkages, preventing side-effects.
3. **Preservation of Verification Baselines:** Detailed test plans and test case suites allow engineers to conduct selective regression testing with confidence.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 459, 485–487; Slides 3, 59–63.

---

### Q9.D20 (Exercise 9.34): Tools and Documents Required to Maintain Large Software
**Question:**
What is an appropriate set of tools and documents required to maintain a large software product?

**Essential Document Suite:**
1. **Software Requirements Specification (SRS):** Validates original functional scope and behavioral boundaries.
2. **Software Design Description (SDD):** Documents high-level architecture, module decomposition, and data structures.
3. **Source Code Listings with Internal Comments:** Fully documented code.
4. **Test Plans, Test Cases & Test Scripts:** Baseline test assets for regression verification.
5. **User & System Manuals:** Installation, configuration, and operational reference guides.

**Essential Maintenance Toolset:**
1. **Version Control & SCM Systems:** Manages revisions, variations, and change audit trails.
2. **Cross-Reference & Symbol Table Generators:** Maps global data structures and calling relationships.
3. **Call Graph & Static Flow Analyzers:** Visualizes inter-modular control flow and ripple propagation.
4. **Automated Test Runners & Coverage Profilers:** Measures regression coverage and ensures baseline reliability.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 484–487; Slides 55, 63.

---

### Q9.D21 (Exercise 9.36): Feasibility of Specifying Maintainability in the SRS
**Question:**
Is it feasible to specify maintainability in the SRS? If yes, how would we specify it?

**Yes**, it is feasible to specify maintainability in the Software Requirements Specification (SRS), provided requirements are stated as **measurable, verifiable quantitative metrics** rather than vague qualitative statements.

**Illustrative Examples of Quantitative Specification:**
1. **Mean Time to Repair (MTTR):** Specify maximum repair durations for defect classes (e.g., $MTTR \le 2\text{ hours}$ for critical faults).
2. **Maximum Modular Complexity:** Set explicit upper bounds on structural metrics (e.g., McCabe cyclomatic complexity $V(G) \le 10$).
3. **Coupling & Modularity Constraints:** Require modules to exhibit high functional cohesion and data/stamp coupling only, prohibiting common or content coupling.
4. **Comment Density:** Define minimum ratios of explanatory comments in source code (e.g., meaningful comments $\ge 20\%$ of source lines).
5. **Standard Change Turnaround:** Define maximum turnaround effort for standard enhancements (e.g., routine report modifications $\le 5\text{ person-days}$).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 465–466; Slide 12.

---

### Q9.D22 (Exercise 9.37): Software Maintenance Tools and Techniques
**Question:**
What tools and techniques are available for software maintenance? Discuss any two of them.

1. **Program Slicing Technique:**
   - Computes the subset of all program statements that directly or indirectly affect the value of a designated variable at a specific execution point.
   - Confines ripple-effect analysis by allowing maintainers to inspect only statements relevant to a variable of interest without analyzing entire uncoupled code blocks.
2. **Automated Restructuring Tools:**
   - Ingests source code, identifies convoluted or deeply nested control structures, and transforms them into standardized structured programming constructs (e.g., SESE modules, case statements) without altering operational semantics.
   - Modernizes legacy code, improving readability and maintainability.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 478–479, 482–483; Slides 47, 51.

---

### Q9.D23 (Exercise 9.38): Why Maintenance Programming is More Challenging & Programmer Profile
**Question:**
Why is maintenance programming becoming more challenging than new development? What are desirable characteristics of a maintenance programmer?

**Why Maintenance is More Challenging:**
1. **Cognitive Constraint:** In new development, engineers start from a clean slate. Maintainers must decipher complex existing logic written by departed authors within rigid architectural constraints.
2. **Regression Danger:** Every patch carries the risk of triggering unintended ripple failures in operational business baselines.
3. **Heterogeneous Tech Stacks:** Maintainers must master obsolete languages, outdated frameworks, and legacy hardware interfaces simultaneously.

**Desirable Characteristics of a Maintenance Programmer:**
1. **Reverse-Engineering Aptitude:** Ability to read, trace, and extract mental models from undocumented foreign code.
2. **Diagnostic & Debugging Rigor:** Deep analytical patience to isolate subtle latent defects and trace data flows.
3. **Broad System-Level Perspective:** Ability to visualize whole-system implications of localized code changes.
4. **Professional Discipline:** Adheres strictly to existing coding styles, updates documentation diligently, and avoids unapproved code rewrites.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 461–463, 487–488; Slides 6–7.

---

### Q9.D24 (Exercise 9.39): Why Little Attention is Paid to Maintainability During Design
**Question:**
Why little attention is paid to maintainability during design phase?

1. **Schedule Pressure (Time-to-Market Urgency):** Project managers prioritize hitting initial deployment milestones. Adding modular decoupling, clean interfaces, and extensive documentation lengthens initial schedules.
2. **Misaligned Cost Centers:** Initial development and post-delivery maintenance are frequently funded from separate organizational budgets. Development teams have no financial incentive to spend initial development funds to save future maintenance dollars.
3. **Lack of Immediate Visibility:** Code maintainability is an internal non-functional attribute invisible to customers at delivery time, whereas user features are visible.
4. **Absence of Quantitative Enforcement:** While functional features can be verified immediately via acceptance tests, maintainability is rarely audited or enforced during design reviews.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 459–463; Slides 3–6.

---

### Q9.D25 (Exercise 9.40): System Documentation Categories & Purpose
**Question:**
List out system documentation and also explain their purpose.

According to the canonical classification of system documentation (Aggarwal & Singh, p. 486, Table 9.6; Slides 62–63, Table 6), system documentation comprises seven categories:

1. **System Rationale:** Describes the objectives of the entire system.
2. **Software Requirements Specification (SRS):** Provides information on exact requirements of the system as agreed between user and developers.
3. **Specification / Design:** Provides description of:
   - How system requirements are implemented.
   - How the system is decomposed into a set of interacting program units.
   - The function of each program unit.
4. **Implementation:** Provides description of:
   - How the detailed system design is expressed in some formal programming language.
   - Program actions in the form of intra-program comments.
5. **System Test Plan:** Provides description of how program units are tested individually and how the whole system is tested after integration.
6. **Acceptance Test Plan:** Describes the tests that the system must pass before users accept it.
7. **Data Dictionaries:** Contains description of all terms that relate to the software system in question.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), p. 486 (Table 9.6); Slides 62–63 (Table 6).

---

## Retrieval Set & Active Recall Self-Test

1. Enumerate the four canonical maintenance categories (Exercise 9.1) and state their respective effort percentages based on Figure 9.1.
2. What are the four core phases of the software maintenance process (Exercise 9.7) and which decision terminates the cycle?
3. State the three stages of the Iterative Enhancement model (Exercise 9.12) and explain why it prevents code entropy.
4. List the eight phases of the Taute maintenance model in sequential order (Exercise 9.15).
5. State the eight textbook recommendations for modifying legacy code (Exercise 9.29).
6. Enumerate the seven categories of system documentation and their functions based on Table 9.6 (Exercise 9.40).
"""

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Generated {md_path} successfully. Total descriptive exercises: 25")
