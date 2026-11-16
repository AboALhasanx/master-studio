import os

out_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance"
md_path = os.path.join(out_dir, "T4_Diagrams.md")

content = r"""# Advanced Software Engineering — Chapter 9: Software Maintenance
## T4: Structural Diagrams & Process Workflows

### Q9.F1 (Exercise 9.7): Software Maintenance Process Workflow
**Prompt:** Explain the steps of software maintenance with the help of a diagram (Exercise 9.7).

![Software Maintenance Process](diagrams/CH09_FIG02_Maintenance_Process.png)

**Diagram Structure & Key Elements:**
- **Maintenance Objectives (Inputs):** Correct program error, Add new capabilities, Delete obsolete features, Optimization.
- **Phase 1: Program Understanding** (Quality attributes: Complexity, Documentation, Self-descriptiveness).
- **Phase 2: Generate Particular Maintenance Proposal** (Quality attribute: Extensibility).
- **Phase 3: Account for Ripple Effect** (Quality attribute: Stability — resistance to change amplification).
- **Phase 4: Testing** (Quality attribute: Testability).
- **Decision Gate (Pass Testing?):** If No, takes the feedback loop returning to earlier phases for rework; if Yes, the modified baseline is approved for release.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 463–465; Slide 10 (Fig. 9.2).

---

### Q9.F2 (Exercise 9.13): Boehm's Decision-Driven Maintenance Model
**Prompt:** Explain Boehm's maintenance model with the help of a diagram (Exercise 9.13).

![Boehm's Maintenance Model](diagrams/CH09_FIG06_Boehms_Model.png)

**Diagram Structure & Key Elements:**
- **Change Input & Evaluation:** Maintenance request initiates assessment of system baseline.
- **Triage Tracks:** Differentiates emergency fixes (rapid code patching with deferred documentation) from routine modifications and major feature enhancements.
- **Sequential Stages:**
  1. Understand Existing Software
  2. Generate Maintenance Strategy
  3. Validate Maintenance Strategy (assessing impact before coding)
  4. Verify & Implement Changes
  5. System Retesting (regression verification)

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, p. 468; Slide 19 (Fig. 9.6).

---

### Q9.F3 (Exercise 9.15): Taute Maintenance Model Workflow
**Prompt:** Describe the Taute maintenance model. What are the various phases of this model? (Exercise 9.15).

![Taute Maintenance Model](diagrams/CH09_FIG07_Taute_Model.png)

**Diagram Structure & Key Elements:**
The Taute model organizes maintenance into eight cyclical phases:
1. **Change request:** Initial logging of maintenance defect or enhancement.
2. **Estimate:** Quantitative effort and cost projection.
3. **Schedule:** Release calendar integration and resource planning.
4. **Program:** Code modification.
5. **Test:** Verification and regression testing.
6. **Documentation:** Updating requirements, designs, and user manuals.
7. **Release:** Formal deployment of updated baseline.
8. **Operation:** Operational monitoring (cycling back to Change request).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, p. 469; Slide 20 (Fig. 9.7).

---

### Q9.F4 (Exercise 9.32): Configuration Management Change Request Form
**Prompt:** What are configuration management activities? Draw the performa of change request form (Exercise 9.32).

![Change Request Form](diagrams/CH09_FIG14_Change_Request_Form.png)

**Form Performa & Required Fields:**
The change control process is governed by the **Configuration Control Authority (CCA)** using the standard 18-field Change Request Form:
1. Project ID:
2. Change Requester with date:
3. Requested change with date:
4. Change analyzer:
5. Components affected:
6. Associated components:
7. Estimated change costs:
8. Change priority:
9. Change assessment:
10. Change implementation:
11. Date submitted to CCA:
12. Date of CCA decision:
13. CCA decision:
14. Change implementer:
15. Date submitted to QA:
16. Date of implementation:
17. Date submitted to CM:
18. QA decision:

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 484–485; Slide 58 (Fig. 9.14).

---

### Q9.F5 (Exercise 9.25): Reverse Engineering Abstraction Levels & Domain Mapping
**Prompt:** What is reverse engineering? Discuss levels of reverse engineering (Exercise 9.25).

![Reverse Engineering Levels of Abstraction](diagrams/CH09_FIG11_Reverse_Eng_Levels.png)

![Domain Mapping](diagrams/CH09_FIG10_Domain_Mapping.png)

**Diagram Structure & Key Elements:**
- **Abstraction Levels & Lifecycle Mapping (Fig. 9.11):**
  - **Implementation Phase (Low):** Source code listings and binary artifacts.
  - **Design Phase (Intermediary):** Architecture models, call graphs, and data structures.
  - **Specification Phase (High):** Requirements specifications and domain concepts.
- **Operations Taxonomy:**
  - **Redocumentation:** Horizontal recreation of equivalent representations within the same abstraction level.
  - **Design Recovery:** Vertical upward abstraction from Implementation to Design.
  - **Specification Recovery:** Vertical upward abstraction from Design to Specification.
- **Domain Mapping (Fig. 9.10):** Establishes cognitive mappings between the Problem/Application Domain and the Programming/Implementation Domain.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, pp. 476–478; Slides 42 & 45 (Figs. 9.10 & 9.11).

---

## Retrieval Set & Active Recall Self-Test

1. In Fig. 9.2 (Maintenance Process), list the four core phases and state the specific software quality attribute associated with each phase.
2. What role does the "Pass testing?" decision diamond play in Fig. 9.2, and what action occurs when testing fails?
3. In Boehm's maintenance model (Fig. 9.6), how are emergency fixes handled compared to routine maintenance?
4. Enumerate the eight sequential phases of the Taute maintenance model (Fig. 9.7).
5. State the name of the change approval authority in Fig. 9.14 and list at least six core fields of the Change Request Form.
6. Based on Fig. 9.11, distinguish between Redocumentation and Design Recovery in terms of abstraction levels.
"""

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Generated {md_path} successfully.")
