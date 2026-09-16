---
marp: true
theme: gaia
_class: lead
paginate: true
header: "University of Wasit | College of Computer Science & IT | Master of Computer Science"
footer: "Candidate: Master Candidate | Subject: CS-MCS-504: Advanced Software Eng | Date: 2026-09-16"
backgroundColor: #ffffff
style: |
  section {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    font-size: 21px;
    padding: 34px 44px;
    color: #1a202c;
  }
  section.lead {
    text-align: center;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: #ffffff;
  }
  section.lead h1 {
    color: #ffffff;
    font-size: 36px;
    margin-bottom: 12px;
  }
  section.lead h2 {
    color: #93c5fd;
    font-size: 22px;
    font-weight: 400;
  }
  section.lead p {
    color: #e2e8f0;
    font-size: 17px;
  }
  h1 {
    color: #0f172a;
    font-size: 28px;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-bottom: 14px;
  }
  h2 {
    color: #1e40af;
    font-size: 21px;
    margin-top: 8px;
    margin-bottom: 6px;
  }
  table {
    font-size: 15px;
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
  }
  th {
    background-color: #1e3a8a;
    color: #ffffff;
    padding: 7px 9px;
  }
  td {
    padding: 5px 9px;
    border-bottom: 1px solid #e2e8f0;
  }
  ul, ol {
    margin-top: 4px;
    margin-bottom: 4px;
  }
  li {
    margin-bottom: 4px;
    line-height: 1.35;
  }
  code {
    background-color: #f1f5f9;
    color: #0f172a;
    font-size: 16px;
    padding: 2px 5px;
    border-radius: 4px;
  }
  blockquote {
    background: #f8fafc;
    border-left: 4px solid #2563eb;
    padding: 6px 12px;
    font-size: 16px;
    color: #334155;
    margin: 8px 0;
  }
  footer {
    font-size: 11px;
    color: #64748b;
  }
  header {
    font-size: 11px;
    color: #64748b;
  }
---

<!-- Slide 1: Title & Academic Affiliation (Lead Slide) -->
# Architectural Tactics & Quality Attribute Resilience
## Advanced Software Engineering & Systems Modeling Seminar

**Master of Computer Science Program (Preparatory Stage)**  
College of Computer Science & Information Technology — University of Wasit

**Candidate:** Master Candidate  
**Course & Subject:** CS-MCS-504: Advanced Software Engineering  
**Supervising Professor:** Asst. Prof. Dr. Ali Fahim Ni'ma  
**Academic Term:** Semester 1 (Fall 2026) | **Date:** 2026-09-16

---

<!-- Slide 2: Problem Statement & Research Motivation -->
# 1. Problem Statement & Research Motivation

* **The Core Architectural Challenge:**
  * High-concurrency distributed systems frequently fail non-functional requirements (QAs) despite functionally correct algorithms.
  * Macro-patterns (e.g., Microservices, Event-Driven) lack atomic mechanisms to guarantee deterministic quality attribute bounds.
* **Research & Engineering Question:**
  * *How can fine-grained Architectural Tactics (SEI & ISO/IEC 25010) be systematically synthesized to guarantee strict availability ($99.999\%$) and latency ($p99 \le 50\text{ms}$) under volatile workloads?*
* **Academic & Practical Significance:**
  * Bridges high-level architectural design with concrete source-code level quality enforcement.
  * Prevents catastrophic cascade failures in mission-critical and cloud-native systems.

---

<!-- Slide 3: Academic & Industrial Context -->
# 2. Academic & Industrial Context

* **Evolution of Software Architecture:**
  * *1990s (Foundational):* Structural topologies, Module-Interconnection Languages (Perry & Wolf, Garlan & Shaw).
  * *2000s (Quality Attributes):* SEI Formalization of Quality Attribute Scenarios and Architecture Trade-off Analysis Method (ATAM).
  * *2010s–Present:* Cloud-native resilience, Chaos Engineering, and automated tactic traceability (ISO/IEC 25010 / IEEE 42010).
* **Industrial & Curricular Pressures:**
  * Microservice sprawl introduces exponential communication failure surfaces.
  * SWEBOK v4 and University of Wasit curriculum mandate rigorous trade-off modeling over intuitive guesswork.

---

<!-- Slide 4: Core Theoretical Mechanism & Formulation -->
# 3. Core Theoretical Mechanism & Formulation

* **SEI 6-Part Quality Attribute Scenario:**
  $$\mathcal{S}_{\text{QA}} = \langle \text{Stimulus}, \text{Source}, \text{Environment}, \text{Artifact}, \text{Response}, \text{Response Measure} \rangle$$

* **Mathematical Model of System Availability ($\mathcal{A}$):**
  $$\mathcal{A} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} = \frac{\text{MTBF}}{\text{MTBF} + (\tau_{\text{detect}} + \tau_{\text{recover}} + \tau_{\text{verify}})}$$

* **Invariants of Tactic Selection:**
  1. *Availability Tactic Goal:* $\lim_{\text{MTTR} \to 0} \mathcal{A} = 1.0$ (via Active Redundancy & Heartbeats).
  2. *Performance Tactic Goal:* Minimize contention queue delay $\mathcal{W}_q \le \frac{\rho}{\mu (1-\rho)}$ (via Caching & Throttling).

---

<!-- Slide 5: System Architecture & Tactic Workflow Model -->
# 4. System Architecture & Tactic Workflow Model

```
[ Incoming Client Requests ]
            │
            ▼
┌──────────────────────────────────────────────────────────┐
│  Ingress DMZ: Web App Firewall & Token Authenticator    │
│  [Tactics: Resist Attacks, Authenticate/Authorize]       │
└───────────────────────────┬──────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│  Resilience Gateway: Circuit Breaker & Rate Throttler    │
│  [Tactics: Manage Event Arrival, Prevent Fault Spread]   │
└─────────────┬──────────────────────────────┬─────────────┘
              ▼                              ▼
┌───────────────────────────┐  ┌───────────────────────────┐
│ Primary Worker Node       │  │ Standby Replica Node      │
│ [Tactic: Concurrency]     │  │ [Tactic: Active Redundancy│
└─────────────┬─────────────┘  └─────────────┬─────────────┘
              ▼                              ▼
┌──────────────────────────────────────────────────────────┐
│ Distributed Persistence Tier (Redis Cache + Raft Shards) │
│ [Tactics: Maintain Multiple Copies, Quorum Replication]  │
└──────────────────────────────────────────────────────────┘
```

---

<!-- Slide 6: State-of-the-Art Literature Survey -->
# 5. State-of-the-Art Literature Survey

| Paper Title & Authors | Venue & Year | Core Focus / Methodology | Key Architectural Finding | Verified DOI |
|:---|:---:|:---|:---|:---:|
| **Detecting Tactics in Code**<br>Mirakhorli & Cleland-Huang | IEEE TSE<br>2016 | Information retrieval & ML classifiers for tactic footprints | Proves architectural degradation stems from eroded code tactics | [10.1109/TSE.2015.2479234](https://doi.org/10.1109/TSE.2015.2479234) |
| **Pattern-Tactic Interaction**<br>Harrison & Avgeriou | Elsevier JSS<br>2010 | Taxonomic analysis of pattern-tactic semantic coupling | Tactics form atomic building blocks of architectural patterns | [10.1016/j.jss.2010.04.067](https://doi.org/10.1016/j.jss.2010.04.067) |
| **Software Architecture: Roadmap**<br>David Garlan | ACM/IEEE ICSE<br>2000 | Foundational landscape of formal architectural models | Establishes explicit architectural rationale as first-class asset | [10.1145/336512.336537](https://doi.org/10.1145/336512.336537) |

---

<!-- Slide 7: Architectural Trade-off Matrix -->
# 6. Architectural Trade-off Matrix

| Tactic & Quality Focus | Primary Benefit (+) | Critical Trade-off / Penalty (-) | Complexity | Optimal Use Case |
|:---|:---|:---|:---:|:---|
| **Active Redundancy**<br>*(Availability)* | Near-zero failover ($\text{MTTR} \approx 0$); instantaneous session survival | $N \times$ infrastructure cost; consensus latency overhead | $\mathcal{O}(N)$ nodes<br>$\mathcal{O}(\log N)$ sync | Financial ledgers, aerospace, healthcare |
| **Multi-Tier Caching**<br>*(Performance)* | Sub-millisecond reads ($p99 < 5\text{ms}$); offloads database I/O | Cache invalidation complexity; eventual consistency / stale reads | $\mathcal{O}(1)$ lookup<br>$\mathcal{O}(M)$ RAM | E-commerce catalogs, streaming metadata |
| **End-to-End Encryption**<br>*(Security)* | Total confidentiality; zero-trust network perimeter defense | High CPU cryptographic tax; increased per-request latency | $\mathcal{O}(k)$ cipher<br>Key lifecycle | Banking APIs, HIPAA medical data |
| **Introduce Intermediary**<br>*(Modifiability)* | Loose coupling; centralized telemetry & security policy injection | Single point of failure risk; $+3\text{ms}$ network hop penalty | $\mathcal{O}(1)$ routing<br>$\mathcal{O}(R)$ table | Polyglot enterprise microservices |

---

<!-- Slide 8: Technical Bottlenecks & Known Limitations -->
# 7. Technical Bottlenecks & Critical Limitations

* **Tactic Interference & Negative Side-Effects:**
  * Injecting *Security Tactics* (e.g., deep TLS payload inspection) severely degrades *Performance Efficiency* (reduces throughput by up to $35\%$).
  * Over-applying *Availability Tactics* (e.g., heavy heartbeats & synchronous checkpoints) induces network saturation and jitter.
* **Failure Modes under Extreme Conditions:**
  * *Thundering Herd / Cache Stampede:* Simultaneous key expiry causes database connection pool exhaustion.
  * *Split-Brain under Asymmetric Partitions:* Redundant nodes with inadequate quorum isolation accept conflicting writes.
* **Traceability Decay:**
  * Source code evolutions often violate initial tactic constraints due to developer ignorance.

---

<!-- Slide 9: Future Research & Master's Thesis Trajectory -->
# 8. Future Research & Thesis Trajectory

* **Emerging Research Frontiers:**
  * AI-driven self-adaptive tactic switching (e.g., reinforcement learning to dynamically tune circuit breaker thresholds).
  * Automated formal verification of quality attribute trade-offs using TLA+ and SMT solvers.
* **Proposed Master's Thesis Direction:**
  * *"Automated Architectural Tactic Synthesis and Conflict Resolution in Cloud-Native Microservice Ecosystems."*
  * *Contribution:* An automated framework detecting QA tactic conflicts at pull-request time and recommending Pareto-optimal configurations.
* **Departmental Alignment:**
  * Directly supports the Advanced Software Engineering and Distributed Intelligent Systems research group at University of Wasit.

---

<!-- Slide 10: Open Defense & Viva Examination Prompts -->
# 9. Open Defense & Committee Viva Prompts

> **Simulated Master's Examination & Committee Cross-Examination:**

1. **Trade-off Defense Prompt:**  
   *"Candidate, how do you resolve the fundamental contradiction between the 'Active Redundancy' tactic (demanding immediate consistency) and the 'Asynchronous Event Sourcing' tactic (introducing eventual consistency) under the PACELC theorem?"*
2. **Standardization & Verification Prompt:**  
   *"Demonstrate how your proposed architectural model satisfies ISO/IEC 25010 maintainability and fault-tolerance sub-characteristics during a zero-downtime rolling upgrade."*
3. **Traceability & Code Conformance:**  
   *"If developer commits degrade your caching tactic into an un-synchronized shared state, what automated metric detects this architectural drift?"*

**Thank you! Questions and academic discussion are welcomed.**
