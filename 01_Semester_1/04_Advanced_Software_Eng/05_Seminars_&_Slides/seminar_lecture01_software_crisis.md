# Foundations of Software Engineering & The Software Crisis
Lecture 01: Systems Evolution, Catastrophic Failures, and Academic Taxonomy

Candidate: Master of Computer Science Student
Instructor: Asst. Prof. Dr. Ali Fahim Ni'ma
Institution: College of Computer Science & IT — University of Wasit
Date: September 2026

---

# The Dual Role & Socio-Technical Nature of Software

- Dual Essence of Modern Software:
  1. Software as a Product: Transforms data, executes business logic, and powers cyber-physical devices.
  2. Software as a Vehicle: Acts as the operational platform controlling hardware, operating systems, and communications infrastructure.
- The Socio-Technical Reality (Sommerville):
  - Software does not operate in an abstract mathematical bubble.
  - A complete system includes code, operational processes, and human psychology.
  - Organizational misalignments cause catastrophic system collapses just as easily as runtime exceptions.

---

# Case Study: Dhahran Patriot Missile Failure (1991)

- The Disaster: On Feb 25, 1991, an Iraqi Scud missile struck US barracks in Dhahran, killing 28 soldiers after the Patriot battery failed to engage.
- The Mathematical Root Cause:
  - System clock incremented in integer tenths of a second (0.1 s).
  - Converted to seconds by multiplying by a 24-bit fixed-point register truncation of 1/10.
  - Truncation error: Delta t = 0.000000095 seconds per tick.
- Cumulative Drift over 100 Hours:
  - Total Drift = 3,600,000 * 0.000000095367 s = 0.3433 seconds.
- Tracking Consequence:
  - Scud traveling at Mach 5 (1,676 m/s) -> Radar Range Gate shifted by ~687 meters.
  - The radar looked where the missile was half a kilometer earlier and dismissed the track.

---

# Brooks' Thesis: "No Silver Bullet" (1986)

> "There is no single development, in either technology or management technique, which by itself promises even one order of magnitude (10x) improvement in productivity, in reliability, in simplicity, within a decade."

- Essential Complexity (Inherent to the problem domain):
  - Complexity: Software entities are composed of vast non-identical interacting parts; scaling is non-linear.
  - Conformity: Software must conform to arbitrary human institutions and legacy interfaces.
  - Changeability: Continuous pressure to change due to perceived malleability of code.
  - Invisibility: Software has no geometric spatial representation; topological webs cannot be drawn in 3D.
- Accidental Complexity (Associated with current realization):
  - Language syntax, manual compilation, memory management, and primitive editors.
  - Past advances (High-level languages, IDEs, garbage collection) solved accidental complexity.

---

# What Software Truly Is: The Tripartite Asset

Software is not merely executable code written by a programmer:
Software = Programs + Data Structures + Complete Documentation

- 1. Programs (Code):
  - Modular, maintainable, and covered by automated test suites.
- 2. Data Structures:
  - Schemas, state representations, relational and in-memory data models.
- 3. Comprehensive Documentation:
  - Architectural specifications: Requirements (SRS, ISO 29148), Architectural Views (IEEE 42010), ADRs.
  - Operational documentation: Deployment pipelines, monitoring playbooks, disaster recovery runbooks.
  - User documentation: Operational manuals, training guides, and API contracts.

---

# Defining Software Engineering & The Software Process

- IEEE Standard 610.12 Definition:
  - "The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software."

- The Four Universal Process Activities (Sommerville & Pressman):
  1. Specification: Defining system capabilities and operational boundaries.
  2. Development: Architectural design, component decomposition, and coding.
  3. Validation: Verification (Building the product right?) and Validation (Building the right product?).
  4. Evolution: Adapting software to changing operational, security, and market requirements.

---

# The Software Crisis: Genesis & The IBM OS/360 Lessons

- Coined at NATO Conference (Garmisch, 1968):
  - Projects chronically over budget (200% to 500%), years behind schedule, and untrustworthy.
  - Maintenance costs escalating to consume 70% to 80% of total IT budgets.
- The IBM System/360 Experience (Fred Brooks):
  - Consumed 5,000+ man-years and over $50,000,000.
  - Suffered years of schedule delays and thousands of latent defect releases.
- Brooks' Law:
  - "Adding human resources to a late software project makes it later."
  - New developers require training from existing experts.
  - Inter-team communication channels grow quadratically: C = N(N - 1) / 2.

---

# Debunking Software Myths

| Category | Persistent Industry Myth | Empirical Software Engineering Reality |
|---|---|---|
| Management | "If we fall behind schedule, we can just hire more programmers." | Brooks' Law: Increases communication overhead and training drag, causing further delay. |
| Customer | "A vague general objective is enough; we can work out details later." | Ambiguous requirements are the #1 cause of software failure and architectural rework. |
| Developer | "Once the code compiles and runs, our job as engineers is complete." | Post-delivery maintenance accounts for 60% to 80% of the entire system lifecycle cost. |
| Developer | "The working program is the only deliverable that matters." | Code without documentation is a maintenance disaster that guarantees technical bankruptcy. |

---

# Core Terminology Taxonomy: Dependability Chain

Under formal IEEE 610.12 and Laprie / Avizienis standards:

- Error (Human Mistake):
  - Mental slip, cognitive misunderstanding of requirements, or algorithmic oversight by a human.
- Fault / Defect (Static Flaw):
  - An incorrect step, process, or data definition residing silently in code or documentation.
  - A fault remains dormant until an execution path triggers it.
- Failure (Dynamic Breakdown):
  - An observable deviation of the software service from its specified expected behavior at runtime.
  - Causal Chain: Human Error -> Static Fault/Defect -> Internal Error State -> Observable Failure.

---

# Professional Ethics & Open Defense Viva Questions

- ACM/IEEE Code of Ethics (8 Core Principles):
  - 1. Public | 2. Client and Employer | 3. Product | 4. Judgment | 5. Management | 6. Profession | 7. Colleagues | 8. Self.

- Open Viva Defense Questions (Dr. Ali Fahim):
  1. How does the Patriot missile failure demonstrate that software maintenance is often more hazardous than initial greenfield development?
  2. Why does Brooks argue that solving accidental complexity (e.g. AI code generation, higher-level frameworks) will never eliminate the software crisis?
  3. Under the ACM/IEEE code of ethics, what is an engineer's professional duty when pressured by management to ship software with known latent faults?
