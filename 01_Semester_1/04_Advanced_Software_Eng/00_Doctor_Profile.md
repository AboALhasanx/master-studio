# 👨‍🏫 Instructor Dossier: Asst. Prof. Dr. Ali Fahim Ni'ma

> **Subject:** 🏗️ Advanced Software Engineering (CS603)  
> **Academic Rank:** Assistant Professor (*أستاذ مساعد دكتور*)  
> **Faculty:** College of Computer Science & Information Technology, University of Wasit  
> **Lecture Slot:** Monday, 10:30 AM – 01:30 PM (3 Credit Hours / 3 Contact Hours)  
> **Status:** Active Coursework Instructor (Semester 1, 2026–2027)

---

## 1. Professional Background & Academic Persona

Asst. Prof. Dr. Ali Fahim Ni'ma is a senior faculty member and software engineering authority specializing in software architecture, quality attribute engineering, systems modeling, and empirical software engineering methodologies.

- **Canonical Textbooks (Distributed 2026-09-16):**
  1. Ian Sommerville — *Software Engineering* (9th Edition)
  2. Roger Pressman — *Software Engineering: A Practitioner's Approach*
  3. Rajib Mall — *Fundamentals of Software Engineering* (4th Edition)
  4. B.B. Agarwal, S.P. Tayal, M. Gupta — *Software Engineering and Testing: An Introduction* (2010)
- **Policy on Proposing External Sources:** Dr. Ali explicitly stated: *"و ممكن ان يعتمد مصدر اخر بعد ان تعرضوه عليه اشوفه"* (Students are permitted to adopt external literature or books after presenting them to him for review and approval).
- **Primary Source Immersion:** In addition to the four canonical textbooks, students are required to read, synthesize, and critique primary academic literature (IEEE TSE, ACM TOSEM, ICSE), SEI technical reports, and international standards (ISO/IEC 25010, SWEBOK, IEEE 42010).
- **Architectural Trade-offs as Core Philosophy:** Software architecture is fundamentally the *science of trade-offs*.

## 2. Core Theoretical Foundations & High-Yield Domains

```
+-----------------------------------------------------------------------------------------------+
|                              DR. ALI FAHIM'S INTELLECTUAL PILLARS                             |
+===============================================================================================+
| 1. SEI Architecture Tactics       | Bass, Clements, Kazman: "Software Architecture in Practice"|
| 2. Quality Attributes Taxonomy    | ISO/IEC 25010 Quality Model (Availability, Modifiability) |
| 3. Formal Scenario Engineering    | 6-Part SEI Quality Attribute Scenario Template            |
| 4. Architecture Evaluation        | ATAM (Trade-offs/Sensitivity) & CBAM (Economic ROI)       |
| 5. Empirical Software Engineering | Research paradigms, experimental design, validity threats |
| 6. SWEBOK Knowledge Areas         | Design, Requirements, Quality, Maintenance, Metrics       |
+-----------------------------------------------------------------------------------------------+
```

### Key Architectural Tactics Catalogs
Dr. Ali Fahim expects master candidates to master the specific tactical mechanisms categorized by the Software Engineering Institute (SEI):

1. **Availability Tactics:**
   - *Fault Detection:* Ping/Echo, Heartbeat, Timestamp, Sanity Checking, Condition Monitoring, Voting.
   - *Fault Recovery:* Active Redundancy (hot standby), Passive Redundancy (warm/cold standby), State Resynchronization, Rollback / Checkpoint, Shadowing.
   - *Fault Prevention:* Removal from Service, Transactions, Process Monitor.
2. **Performance Tactics:**
   - *Demand Control:* Manage request rate, Sample input, Limit queue sizes.
   - *Resource Management:* Increase concurrency, Thread pooling, Introduce caching, Maintain multiple copies of data (replication), Asynchronous processing.
   - *Resource Arbitration:* Priority scheduling, Round-robin, Earliest Deadline First.
3. **Modifiability Tactics:**
   - *Reduce Coupling:* Encapsulation, Use an intermediary (Broker, Adapter, Facade), Restrict communication paths, Publish-Subscribe event buses.
   - *Increase Cohesion:* Semantic coherence, Abstract common interfaces.
   - *Defer Binding Time:* Runtime configuration files, Dynamic component loading / Plugins, Polymorphism.
4. **Security Tactics:**
   - *Resist Attacks:* Authenticate actors, Authorize actors, Encrypt data in transit/at rest, Validate input.
   - *Detect Attacks:* Intrusion Detection Systems (IDS), Audit trails.
   - *Recover from Attacks:* Graceful degradation, State restoration.

---

## 3. The 6-Part Quality Attribute Scenario Framework

In all assignments and exams, Dr. Ali Fahim rejects vague quality claims (*"the system must be fast and secure"*). Every quality requirement must be formulated using the **formal SEI 6-part specification**:

```
+=======================================================================================================+
|                                    FORMAL SEI 6-PART SCENARIO TEMPLATE                                |
+====================+==================================================================================+
| Element            | Definition & Master Standard                                                     |
+====================+==================================================================================+
| 1. Source          | The entity generating the stimulus (e.g., Internal user, External attacker)     |
| 2. Stimulus        | The condition arriving at the system (e.g., 50,000 req/sec spike, DB failure)    |
| 3. Artifact        | The specific subsystem/component affected (e.g., Payment Gateway, Auth Service)  |
| 4. Environment     | System state during arrival (e.g., Normal operation, Degraded mode, Peak load)   |
| 5. Response        | The observable activity undertaken (e.g., Shed load, Failover to standby node)   |
| 6. Response Measure| Quantifiable metric (e.g., Latency < 200ms at 99th percentile, Downtime < 5 sec)|
+====================+==================================================================================+
```

---

## 4. Examination Philosophy & Question Formats

Dr. Ali Fahim’s examinations are **highly challenging, scenario-driven, and design-oriented**.

### Typical Exam Question Types

| Question Type | Cognitive Demand | Example Prototype |
|:---|:---|:---|
| **Architectural Trade-off Analysis** | Synthesizing competing architectural styles across quality dimensions. | *"A financial brokerage requires sub-millisecond execution latency while guaranteeing zero transaction loss during cloud node failures. Construct a comprehensive Trade-off Matrix comparing Event-Driven Microservices vs. Shared-Memory Monolith across Availability, Performance, and Modifiability. Justify your architectural selection using SEI tactics."* |
| **Formal Scenario Construction** | Writing rigorous 6-part ISO 25010 scenarios. | *"Formulate two formal 6-part Quality Attribute Scenarios for an Autonomous Medical Infusion Pump: one for Safety/Availability and one for Security/Integrity."* |
| **ATAM Evaluation Walkthrough** | Tracing the steps of the Architecture Trade-off Analysis Method. | *"Explain how ATAM identifies Sensitivity Points and Trade-off Points. Provide a concrete scenario where Modifiability conflicts with Performance."* |
| **Empirical Validity Defense** | Evaluating research methodology in empirical software engineering. | *"Define Construct Validity, Internal Validity, and External Validity. Analyze how a controlled experiment evaluating a new refactoring tool might suffer from threats to External Validity."* |
| **Software Metrics Calculation** | Formal software measurement arithmetic. | *"Given the following control flow graph, calculate McCabe's Cyclomatic Complexity $V(G) = E - N + 2P$. Explain how this metric guides unit test suite design."* |

---

## 5. Master-Level Answering Protocol

To achieve a top grade ($\ge 85\%$) under Dr. Ali Fahim:

```mermaid
flowchart TD
    A[Architectural Problem Prompt] --> B[1. State System Context & Quality Priorities]
    B --> C[2. Formulate Formal 6-Part Scenarios]
    C --> D[3. Select Specific SEI Architectural Tactics]
    D --> E[4. Construct Explicit Trade-off Matrix]
    E --> F[5. Anchor in ISO/SWEBOK Standards]
```

### The 3 Inviolable Rules:
1. **Rule 1: Always Articulate Trade-offs:** Never claim a solution is purely beneficial. Always state what is sacrificed (*"Applying the Publish-Subscribe tactic improves Modifiability by decoupling publishers from subscribers, but introduces non-deterministic latency and increases debugging complexity, penalizing Testability."*).
2. **Rule 2: Never Use Vague Terminology:** Replace *"the system is scalable"* with *"the system applies horizontal replication tactics to maintain sub-200ms latency under 10,000 concurrent transactions (ISO/IEC 25010 Performance Efficiency)."*
3. **Rule 3: Use Mermaid Architectural C4 Diagrams:** Illustrate subsystem relationships with clear container/component boundary diagrams.

---

## 6. Doctor-Specific Agent Tuning Prompt (`@examiner` & `@tutor`)

```yaml
doctor_profile:
  name: "Asst. Prof. Dr. Ali Fahim Ni'ma"
  subject: "Advanced Software Engineering"
  course_weight: "3 Credit Hours (Flagship Core)"
  pedagogy: "Syllabus & Primary Literature-driven, SEI Architecture Tactics, ISO/IEC 25010, ATAM/CBAM"
  mandatory_structures:
    - "6-part formal Quality Attribute Scenarios"
    - "Explicit Trade-off Analysis Matrices (Benefit vs Penalty)"
    - "SEI named tactics (e.g., Active Redundancy, Encapsulation, Heartbeat)"
  forbidden_patterns:
    - "Generic answers without trade-off analysis"
    - "Unquantified quality claims ('fast', 'reliable')"
  scoring_rubric:
    architectural_tactics_and_tradeoffs: 45%
    formal_scenario_precision: 30%
    standards_and_literature_grounding: 25%
```

---

## 7. Observed Chapter Pattern, Vocabulary Maps & Source Expectations

> **Why this section exists:** recorded from the Chapter 5 (Design) seminar review and the Chapter 6 (Metrics) vocabulary drop. It captures *how Dr. Ali Fahim builds a chapter and expects it to be presented* — for exam preparation and for any future chapter artefact. It is a record, not a task.

### 7.1 The pattern (observed)

1. For each chapter he hands a **detailed vocabulary list** that is effectively **the exam scope** — and it is **noticeably broader than the Aggarwal chapter** it is based on.
2. He expects the material to **follow the book's topic order**, but to be **synthesised from multiple sources**. Reproducing the book alone is rejected.
3. He **requires sources explicitly**: *"ما يقبل من غير المصادر"* — content presented without a cited source is not accepted. Cite the book (author, chapter, page).
4. He **reviews semantically**: his feedback names **missing concepts**, not wording. Two teams that copied the textbook verbatim were caught by exactly this.

### 7.2 Chapter 5 (Software Design) — the feedback that confirms the pattern

A submitted seminar reproduced **Aggarwal Ch. 5 verbatim** (including the book's own figures). His review flagged, as missing:

| Flagged as missing | Where it actually lives (PDF pages) |
|:--|:--|
| **abstraction** (procedural · data · control) | **Pressman §13.4.1** PDF 370–371 |
| **stepwise refinement** | **Pressman §13.4.2** PDF 371 |
| **information hiding** | **Pressman §13.4.9** PDF 379–380 |
| **fan-in / fan-out** | **Mall §5.4** PDF 300–301 · **Pressman §13.4.5** PDF 375 |
| **depth / width** | same pages |
| **design review** | **Mall §6.6** PDF 349–352 |
| **DFD → structure chart methodology** (transform / transaction analysis) | **Mall §6.4.1** PDF 344–348 |
| *"الخصائص"* (properties) | Most likely **Meyer's five modularity criteria** (Pressman PDF 373); note the modular-system properties were **already present** in the submission |

**Lesson:** Aggarwal Ch. 5 does **not** contain these; the doctor expects the standard SE sources (**Pressman / Mall**) to fill them in.

### 7.3 Chapter 6 (Software Metrics) — future vocabulary map (recorded)

The Ch. 6 vocabulary list (12 sections, ~60 items) is roughly **twice** the Aggarwal Ch. 6 scope. Source map:

| Vocabulary block | In Aggarwal Ch.6? | Where else (PDF pages) |
|:--|:--:|:--|
| 1. Fundamentals of Measurement (scales, representation condition, GQM) | ❌ (definition only) | **No source in the vault** → *Fenton & Pfleeger*; GQM → Sommerville PDF 691 |
| 2. Categories of Metrics (product/process/project; internal/external; predictor/control) | ✅ partial | external for internal/external + predictor/control |
| 3. Size Metrics (LOC, Function Points, Feature/Mark II/Object Points, backfiring) | ❌ | **Pressman 107–162 · Mall 142–166 · Leach 153–180 · CS-Agarwal 167–170** |
| 4. Halstead's Software Science | ✅ **full** | (reinforce: Mall 167–169 · Pressman 559–565) |
| 5. Data Structure Metrics (live variables, span, program weakness) | ✅ **exclusive to Aggarwal** | — |
| 6. Information Flow Metrics (Henry & Kafura, IF4, Shepperd) | ✅ | Henry/Kafura: Pressman ~8 · Leach |
| 7. Control Flow / Cyclomatic (McCabe), essential complexity, knot | ❌ | **Mall 568–576 · Pressman 465–477 · Sommerville 685–690** |
| 8. Object-Oriented Metrics (CK, MOOD, Lorenz & Kidd) | ✅ partial | **Pressman 681–696** (MOOD, Lorenz) |
| 9. Use-Case Oriented Metrics (Use Case Points) | ✅ (slides 89–91) | — |
| 10. Quality & Defect Metrics (defect density, DRE, phase containment, MTBF) | ❌ | **Mall 84–127** (phase containment) · **Pressman 123–133** (DRE) · **MTBF: Mall 616–642** |
| 11. Productivity & Process Metrics | ❌ | **Pressman / Mall / Sommerville** |
| 12. Metrics Analysis & Program (validation, baselines, ethics) | ✅ partial | **Pressman 127–139 · Sommerville 688–697** (ethics in Sommerville) |

**Note:** "Fundamentals of Measurement" (scales, representation condition) has **no source inside the vault** — it is the classic **Fenton & Pfleeger, *Software Metrics***. The doctor is following the classic metrics literature, not only Aggarwal.

### 7.4 Exam-relevant, calculable topics (Chapter 6)

Halstead metrics · Function Points · Cyclomatic complexity $V(G)$ · Information-flow (fan-in / fan-out) · the CK suite (WMC, DIT, NOC, CBO, RFC, LCOM) · Use Case Points · Defect Density / Defect Removal Efficiency. These are the numeric, examinable cores.

### 7.5 Working method that this profile implies

For any chapter the doctor assigns: (1) take his vocabulary list as the exam scope; (2) follow the book's topic order; (3) fill every block from the **richest** source (Aggarwal where it is richest, otherwise Pressman / Mall / Sommerville / Leach / Fenton); (4) cite the source and page for anything not in the lecture source; (5) expect concept-level review, not word-level.
