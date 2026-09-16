# 🗺️ 16-Week Syllabus & Progress Roadmap: Advanced Software Engineering

> **Course Code:** CS603  
> **Course Title:** Advanced Software Engineering & Architecture / *هندسة البرمجيات المتقدمة والمعمارية*  
> **Instructor:** Asst. Prof. Dr. Ali Fahim Ni'ma (*أ.م.د. علي فاهم نعمة*)  
> **Credit Hours:** 3 Units | Weekly Time: Monday 10:30 AM – 01:30 PM (3 Contact Hours)  
> **Repository Directory:** `01_Semester_1/04_Advanced_Software_Eng/`

---

## 1. Course Overview & Master Competency Matrix

This flagship 3-credit course prepares master candidates for high-level software system architecture design, trade-off evaluation, and empirical software engineering research. Operating without static slides, students engage directly with primary IEEE/ACM literature, SWEBOK v3/v4 knowledge areas, ISO/IEC 25010 standards, and the Software Engineering Institute (SEI) architecture tactics framework.

```
+=======================================================================================================+
|                                    16-WEEK PROGRESS TRACKER OVERVIEW                                  |
+=======================================================================================================+
| Completed Weeks: [ 0 / 16 ] | Progress: 0.0% | Status: Initializing Semester 1                        |
+=======================================================================================================+
```

---

## 2. Detailed 16-Week Chronological Roadmap

### 🏛️ Phase 1: Architecture Foundations & Quality Scenarios (Weeks 1–4)

- [ ] **Week 01: Foundations of Software Architecture & SWEBOK Knowledge Areas**
  - **Topics:** What is Software Architecture? Architecture as the bridge between requirements and implementation. IEEE 42010 Architecture Description standard (Architectural Views, Viewpoints, Stakeholders, Concerns). SWEBOK v3/v4 Knowledge Areas overview. Why software architecture matters (communication, early design decisions, transferable abstraction).
  - **Literature & Standards:** SWEBOK v3 (Chapter 2: Software Design, Chapter 10: Software Quality) + IEEE Std 42010-2011 (`https://doi.org/10.1109/IEEESTD.2011.6129467`).
  - **Deliverables:** Architectural Foundations Note in `03_Study_Notes/Week_01_Architecture_Foundations.md`.
  - **Self-Assessment:** Contrast an Architectural Pattern vs. an Architectural Tactic vs. a Design Pattern with concrete examples.

- [ ] **Week 02: Quality Attributes Taxonomy & The ISO/IEC 25010 Quality Model**
  - **Topics:** Functional vs. Non-Functional Requirements, The ISO/IEC 25010 Product Quality Model (Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability). Quality attribute sub-characteristics and operational definitions.
  - **Literature & Standards:** ISO/IEC 25010:2011 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE).
  - **Deliverables:** Complete ISO 25010 Quality Mapping Table in `03_Study_Notes/Week_02_ISO25010_Quality_Model.md`.
  - **Self-Assessment:** Map 10 ambiguous stakeholder statements into precise ISO 25010 sub-characteristics.

- [ ] **Week 03: Specifying Quality Attribute Scenarios (The 6-Part SEI Template)**
  - **Topics:** The limitation of vague quality statements, SEI formal 6-part scenario architecture: (1) Source of Stimulus, (2) Stimulus, (3) Artifact, (4) Environment, (5) Response, (6) Response Measure. General scenarios vs. Concrete scenarios.
  - **Literature:** Bass, Clements, Kazman — *Software Architecture in Practice* (3rd/4th Edition), Chapter 4.
  - **Deliverables:** Collection of 8 formal concrete scenarios for diverse quality attributes in `03_Study_Notes/Week_03_Quality_Scenarios.md`.
  - **Self-Assessment:** Write a 6-part scenario for a cloud storage service experiencing 99.999% availability under regional data center failure.

- [ ] **Week 04: Architectural Tactics — Availability & Fault Tolerance Engineering**
  - **Topics:** Understanding Availability: Faults, Errors, Failures. SEI Availability Tactics: Fault Detection (Ping/Echo, Heartbeat, Exception detection), Fault Recovery (Active Redundancy / Hot Standby, Passive Redundancy / Warm Standby, State Resynchronization, Rollback/Checkpoint), Fault Prevention (Removal from service, Transactions). Availability calculation: MTBF / (MTBF + MTTR).
  - **Literature:** Bass et al., Chapter 5 + Avizienis et al., "Basic Concepts and Taxonomy of Dependable and Secure Computing" (`https://doi.org/10.1109/TDSC.2004.24`).
  - **Deliverables:** Availability Tactics Deep Dive & Mermaid Failover Diagram in `03_Study_Notes/Week_04_Availability_Tactics.md`.
  - **Self-Assessment:** Compare Active Redundancy vs. Passive Redundancy regarding synchronization latency, hardware cost, and failover time.

---

### ⚡ Phase 2: Performance, Modifiability & Security Tactics (Weeks 5–8)

- [ ] **Week 05: Architectural Tactics — Performance, Latency & Concurrency Management**
  - **Topics:** Performance drivers: Latency, Throughput, Jitter, Bandwidth. SEI Performance Tactics: Control Resource Demand (Manage event arrival rate, Sample inputs, Limit queue sizes), Manage Resources (Increase concurrency, Thread pooling, Introduce caching, Maintain multiple copies of data / read replicas, Partition state), Resource Arbitration (Priority scheduling, Earliest Deadline First).
  - **Literature:** Bass et al., Chapter 6 + Dean & Barroso, "The Tail at Scale", *Communications of the ACM* (`https://doi.org/10.1145/2408776.2408794`).
  - **Deliverables:** Performance Tactics & Caching Strategies Synthesis in `03_Study_Notes/Week_05_Performance_Tactics.md`.
  - **Self-Assessment:** Construct a trade-off matrix evaluating the latency vs. memory consumption of L1/L2 in-memory cache vs. distributed Redis cache.

- [ ] **Week 06: Architectural Tactics — Modifiability, Decoupling & Binding Time**
  - **Topics:** Cost and impact of change, Cohesion and Coupling definitions. SEI Modifiability Tactics: Reduce Coupling (Encapsulation, Use an Intermediary / Broker / Adapter, Restrict communication paths, Publish-Subscribe event bus), Increase Cohesion (Semantic coherence, Abstract common interfaces), Defer Binding Time (Compile-time vs. Load-time vs. Runtime configuration / Plugins / Dynamic service discovery).
  - **Literature:** Bass et al., Chapter 7 + Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", *CACM* (`https://doi.org/10.1145/361598.361623`).
  - **Deliverables:** Modifiability & Decoupling Guide in `03_Study_Notes/Week_06_Modifiability_Tactics.md`.
  - **Self-Assessment:** Analyze how deferring binding time to runtime via configuration files affects Modifiability, Performance, and Testability.

- [ ] **Week 07: Architectural Tactics — Security, Testability & Usability Tactics**
  - **Topics:** Security Tactics (Resist attacks: Authenticate, Authorize, Encrypt, Maintain integrity; Detect attacks: Intrusion detection, Audit trails; Recover: Graceful degradation). Testability Tactics (Control and observe system state: Specialized test interfaces, Record/playback, Abstract data sources). Usability Tactics (Support user initiative: Cancel, Undo, Progress indicator; Support system initiative: User models).
  - **Literature:** Bass et al., Chapters 8, 9, 10.
  - **Deliverables:** Security, Testability & Usability Tactics Matrix in `03_Study_Notes/Week_07_Security_Testability_Tactics.md`.
  - **Self-Assessment:** Design a testability harness tactic allowing deterministic unit testing of an asynchronous event-driven workflow.

- [ ] **Week 08: Midterm Assessment & Architectural Trade-off Synthesis**
  - **Exam Focus:** Comprehensive written evaluation on Weeks 1–7: Specifying formal 6-part scenarios, applying availability/performance/modifiability tactics, and constructing formal trade-off matrices.
  - **Weight:** 30% of coursework grade.
  - **Deliverables:** Midterm exam debrief and error log updates in `LEARNER_MODEL.md`.

---

### 🔍 Phase 3: Architecture Evaluation Methods (ATAM / CBAM) & Patterns (Weeks 9–12)

- [ ] **Week 09: Architecture Trade-off Analysis Method (ATAM) Execution**
  - **Topics:** Purpose of architectural evaluation, The 4 phases and 9 steps of ATAM: (1) Present ATAM, (2) Present Business Drivers, (3) Present Architecture, (4) Identify Architectural Approaches, (5) Generate Quality Attribute Utility Tree, (6) Analyze Architectural Approaches, (7) Brainstorm and Prioritize Scenarios, (8) Analyze Architectural Approaches, (9) Present Results. Identifying Sensitivity Points, Trade-off Points, Risks, and Non-risks.
  - **Literature:** Kazman, Klein, Clements — "ATAM: Method for Architecture Evaluation", SEI Technical Report (`https://doi.org/10.1184/R1/6584288.v1`).
  - **Deliverables:** Complete ATAM Utility Tree and Evaluation Walkthrough in `03_Study_Notes/Week_09_ATAM_Methodology.md`.
  - **Self-Assessment:** Construct an ATAM Utility Tree for an autonomous ride-sharing backend prioritizing Performance and Security.

- [ ] **Week 10: Cost Benefit Analysis Method (CBAM) & Economic Architecture Decisions**
  - **Topics:** Architecture economics: Why technical superiority is insufficient without ROI. The CBAM process: Assigning utility to scenarios, Calculating expected architectural strategy costs, Estimating quality attribute gains, Ranking strategies by Benefit-to-Cost Ratio ($ROI = \frac{\Delta \text{Utility}}{\text{Cost}}$).
  - **Literature:** Kazman, Asundi, Klein — "Making Architecture Design Decisions: An Economic Approach", SEI CMU/SEI-2002-TR-035 (`https://doi.org/10.1184/R1/6584444.v1`).
  - **Deliverables:** CBAM Economic Decision Matrix in `03_Study_Notes/Week_10_CBAM_Economic_Modeling.md`.
  - **Self-Assessment:** Calculate the ROI ranking for 3 competing architectural upgrade strategies given budget constraints.

- [ ] **Week 11: Modern Architectural Styles — Microservices, Event-Driven & Domain-Driven Design**
  - **Topics:** Monolith vs. Service-Oriented vs. Microservices architecture, Microservice design trade-offs (Network partitioning, distributed transactions, 2PC vs. Sagas, Eventual consistency), Domain-Driven Design (DDD) concepts (Bounded Contexts, Ubiquitous Language, Aggregates, Event Storming).
  - **Literature:** Newman — *Building Microservices* + Evans — *Domain-Driven Design* + Fowler, "Microservices" (`https://martinfowler.com/articles/microservices.html`).
  - **Deliverables:** Microservices vs. Monolith Architectural Comparison in `03_Study_Notes/Week_11_Modern_Architectures.md`.
  - **Self-Assessment:** Analyze how the Saga pattern manages distributed consistency during multi-service checkout workflows.

- [ ] **Week 12: Software Product Lines (SPL) & Component-Based Engineering**
  - **Topics:** Software Product Line Engineering (SPLE): Domain Engineering vs. Application Engineering, Commonality and Variability analysis, Feature Models / Feature Trees, Software variability mechanisms (compile-time, load-time, runtime). Component-Based Software Engineering (CBSE): Component interfaces, contracts, composition anomalies.
  - **Literature:** Clements & Northrop — *Software Product Lines: Practices and Patterns* + Kang et al., "Feature-Oriented Domain Analysis (FODA)".
  - **Deliverables:** Feature Tree Diagram (Mermaid) in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Draw a Feature Diagram for a configurable Smart Home IoT system with mandatory, optional, and mutually exclusive features.

---

### 🔬 Phase 4: Empirical SE, Metrics & Legacy Modernization (Weeks 13–16)

- [ ] **Week 13: Empirical Software Engineering, Research Methods & Threats to Validity**
  - **Topics:** Empirical SE research paradigms (Surveys, Case Studies, Controlled Experiments, Repository Mining / MSR), Formulating research questions (GQM: Goal-Question-Metric), Statistical hypothesis testing in SE, Threats to Validity: Construct Validity, Internal Validity, External Validity, Conclusion Validity.
  - **Literature:** Wohlin et al. — *Experimentation in Software Engineering* (`https://doi.org/10.1007/978-3-642-29044-2`) + Kitchenham et al., "Guidelines for performing Systematic Literature Reviews in SE".
  - **Deliverables:** Empirical Research Methodology Guide in `03_Study_Notes/Week_13_Empirical_Software_Engineering.md`.
  - **Self-Assessment:** Analyze an empirical software engineering paper and identify 3 critical threats to external validity.

- [ ] **Week 14: CI/CD, DevOps Engineering & Automated Quality Governance**
  - **Topics:** Continuous Integration / Continuous Deployment (CI/CD) pipelines, Automated quality gates, Shift-Left security (DevSecOps), Static analysis tools (SonarQube), Infrastructure as Code (IaC), Canary deployments and Blue-Green zero-downtime releases.
  - **Literature:** Humble & Farley — *Continuous Delivery* + Bass, Weber, Zhu — *DevOps: A Software Architect's Perspective*.
  - **Deliverables:** CI/CD Quality Pipeline architecture diagram in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Design a multi-stage automated deployment pipeline with automated rollback on health probe failure.

- [ ] **Week 15: Technical Debt, Architecture Smells & Legacy System Modernization**
  - **Topics:** Technical Debt taxonomy (Code debt, Architecture debt, Test debt), Detecting architectural smells (Cyclic dependencies, Hub-like dependency, God components), Refactoring strategies (Strangler Fig Pattern, Branch by Abstraction), Software measurement metrics: McCabe Cyclomatic Complexity ($V(G) = E - N + 2P$), Chidamber & Kemerer (CK) Metric Suite (WMC, DIT, NOC, CBO, RFC, LCOM).
  - **Literature:** Kruchten et al., "Technical Debt: From Metaphor to Theory and Practice", *IEEE Software* (`https://doi.org/10.1109/MS.2012.167`) + Chidamber & Kemerer, "A Metrics Suite for Object Oriented Design" (`https://doi.org/10.1109/32.295895`).
  - **Deliverables:** Software Metrics & Technical Debt calculation notes in `03_Study_Notes/Week_15_Metrics_and_Technical_Debt.md`.
  - **Self-Assessment:** Compute Cyclomatic Complexity and CK metrics (CBO, LCOM) for a sample Java/C++ object-oriented class hierarchy.

- [ ] **Week 16: Comprehensive Architecture Defense, Final Exam & Literature Synthesis**
  - **Activities:** Comprehensive final written examination covering architectural tactics, formal scenario derivations, ATAM execution, empirical validity analysis, and software metrics.
  - **Deliverables:** 100-Question Advanced SE Anki deck export in `07_Quizzes_&_Anki/`.
  - **Final Target:** Score $\ge 90\%$ (Distinction / *امتياز*).

---

## 3. Assessment & Grading Criteria

| Component | Weight | Target Score | Description |
|:---|:---:|:---:|:---|
| **Classroom Participation & Literature Seminars** | 10% | 10% | Weekly oral discussion of IEEE/ACM papers and standards |
| **Architectural Case Study & ATAM Report** | 15% | 14% | Complete formal architecture evaluation report for a mission-critical system |
| **Oral Research Seminar Presentation (Marp)** | 15% | 14% | 12-slide research seminar on modern architectural paradigms |
| **Midterm Examination (Week 08)** | 20% | 18% | Written examination on Tactics, Scenarios, and ISO 25010 |
| **Final Semester Examination (Week 16)** | 40% | 36% | Comprehensive written examination |
| **Total Course Grade** | **100%** | **$\ge 92\%$** | **Grade Target: High Distinction (امتياز مرتفع)** |
