import os

out_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance"
md_path = os.path.join(out_dir, "T1_MCQ.md")

content = r"""# Advanced Software Engineering — Chapter 9: Software Maintenance
## T1: Multiple Choice Questions (Publisher Q9.1–Q9.25)

### Q9.1
**Process of generating analysis and design documents is called:**
- (a) Inverse Engineering
- (b) Software Engineering
- **(c) Reverse Engineering**
- (d) Re-engineering

**Reverse engineering** analyzes existing implementation artifacts (source code) to extract high-level architectural designs, data models, and requirement specifications without altering operational behavior.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 476, 488; Slide 64; Answer Key p. 499.

---

### Q9.2
**Regression testing is primarily related to:**
- (a) Functional testing
- (b) Data flow testing
- (c) Development testing
- **(d) Maintenance testing**

**Maintenance testing** ensures that modifications introduced to correct defects, adapt to environment shifts, or add features do not introduce regression defects or corrupt previously validated system baselines.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 473, 488; Slide 64; Answer Key p. 499.

---

### Q9.3
**Which one is not a category of maintenance?**
- (a) Corrective maintenance
- **(b) Effective maintenance**
- (c) Adaptive maintenance
- (d) Perfective maintenance

The four canonical categories of software maintenance are Corrective, Adaptive, Perfective, and Preventive. **Effective maintenance** is a distractor and does not exist in standard software engineering taxonomies.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 460, 488; Slide 64; Answer Key p. 499.

---

### Q9.4
**The maintenance initiated by defects in the software is called:**
- **(a) Corrective maintenance**
- (b) Adaptive maintenance
- (c) Perfective maintenance
- (d) Preventive maintenance

**Corrective maintenance** specifically handles reactive modifications performed to diagnose and rectify residual faults and errors identified in operational production baselines.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 460, 488; Slide 65; Answer Key p. 499.

---

### Q9.5
**Patch is known as:**
- **(a) Emergency fixes**
- (b) Routine fixes
- (c) Critical fixes
- (d) None of the above

A **patch** represents an emergency fix deployed directly to source code to restore system operations during unplanned outages or critical security incidents, bypassing full upfront design reviews.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 466, 488; Slide 65; Answer Key p. 499.

---

### Q9.6
**Adaptive maintenance is related to:**
- (a) Modification in software due to failure
- (b) Modification in software due to demand of new functionalities
- (c) Modification in software due to increase in complexity
- **(d) Modification in software to match changes in the ever-changing environment.**

**Adaptive maintenance** modifies an existing software system to maintain compatibility with changes in its external operating environment, such as new operating systems, hardware platforms, or database upgrades.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 460, 488; Slide 65; Answer Key p. 499.

---

### Q9.7
**Perfective maintenance refers to enhancements:**
- (a) Making the product better
- (b) Making the product faster and smaller
- (c) Making the product with new functionalities
- **(d) All of the above**

**Perfective maintenance** encompasses user-requested enhancements, performance tuning (speed and memory optimizations), and structural modifications that improve maintainability and reliability.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 460, 488; Slide 65; Answer Key p. 499.

---

### Q9.8
**As per distribution of maintenance effort, which type of maintenance has consumed maximum share?**
- (a) Adaptive
- (b) Corrective
- **(c) Perfective**
- (d) Preventive

**Perfective maintenance** accounts for the largest share of maintenance expenditures (**50%**), driven by ongoing organizational growth and evolving user functional demands throughout the operational life cycle.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 461, 488; Slide 65; Answer Key p. 499.

---

### Q9.9
**As per distribution of maintenance effort, which type of maintenance has consumed minimum share?**
- (a) Adaptive
- (b) Corrective
- (c) Perfective
- **(d) Preventive**

**Preventive maintenance** accounts for the smallest proportion of maintenance effort (**4%**), representing proactive code restructuring and defect prevention prior to operational failure.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 461, 488; Slide 66; Answer Key p. 499.

---

### Q9.10
**Which one is not a maintenance model?**
- **(a) CMM**
- (b) Iterative Enhancement model
- (c) Quick-fix model
- (d) Reuse-Oriented model

**CMM (Capability Maturity Model)** is an organizational process improvement framework, whereas Quick-fix, Iterative Enhancement, Reuse-Oriented, Boehm, and Taute are software maintenance process models.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 466–469, 489; Slide 66; Answer Key p. 499.

---

### Q9.11
**In which model, fixes are done without detailed analysis of the long-term effects?**
- (a) Reuse oriented model
- **(b) Quick-fix model**
- (c) Taute maintenance model
- (d) None of the above

The **Quick-fix model** patches source code directly without detailed analysis or documentation updates, accelerating architectural decay and code entropy.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 466, 489; Slide 66; Answer Key p. 499.

---

### Q9.12
**Iterative enhancement model is a:**
- **(a) three stage model**
- (b) two stage model
- (c) four stage model
- (d) seven stage model

The **Iterative Enhancement model** operates in an ongoing three-stage cycle: **Analysis**, **Redesign**, and **Implementation**, ensuring architecture and documentation remain synchronized.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 466–467, 489; Slide 66; Answer Key p. 499.

---

### Q9.13
**Taute maintenance model has:**
- (a) Two phases
- (b) six phases
- **(c) eight phases**
- (d) ten phases

The **Taute maintenance model** partitions the maintenance lifecycle into eight cyclical phases: **Change request**, **Estimate**, **Schedule**, **Program**, **Test**, **Documentation**, **Release**, and **Operation**.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 469, 489; Slide 66; Answer Key p. 499.

---

### Q9.14
**In Boehm model, ACT stands for:**
- (a) Actual change time
- (b) Actual change traffic
- **(c) Annual change traffic**
- (d) Annual change time

**ACT (Annual Change Traffic)** represents the fraction of software lines of code modified or added in a typical year relative to total system size: $\frac{\text{KLOC}_{\text{added}} + \text{KLOC}_{\text{modified}}}{\text{KLOC}_{\text{total}}}$.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 472, 489; Slide 66; Answer Key p. 499.

---

### Q9.15
**Regression testing is known as:**
- **(a) the process of retesting the modified parts of the software**
- (b) the process of testing the design documents
- (c) the process of reviewing the SRS
- (d) None of the above

**Regression testing** validates modified components and dependent routines to ensure changes preserve previously established behavioral and reliability baselines.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 473, 489; Slide 67; Answer Key p. 499.

---

### Q9.16
**The purpose of regression testing is to:**
- (a) increase confidence in the correctness of the modified program
- (b) locate errors in the modified program
- (c) preserve the quantity and reliability of software
- **(d) All of the above**

Regression testing detects side-effect defects, verifies correct delta implementation, and maintains baseline software reliability across evolutionary releases.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 473, 489; Slide 67; Answer Key p. 499.

---

### Q9.17
**Regression testing is related to:**
- (a) maintenance of software
- (b) development of software
- **(c) both (a) and (b)**
- (d) none of the above.

Regression testing is essential during initial development (as new modules are integrated into growing builds) and throughout operational maintenance (as patches are deployed).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 473, 489; Slide 67; Answer Key p. 499.

---

### Q9.18
**Which one is not a selective retest technique:**
- (a) coverage technique
- (b) minimization technique
- (c) safe technique
- **(d) maximization technique**

Selective retest methods comprise coverage techniques, minimization techniques, and safe techniques. **Maximization technique** is non-existent.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 475, 490; Slide 67; Answer Key p. 499.

---

### Q9.19
**Purpose of reverse engineering is to:**
- (a) recover information from the existing code or any other intermediate document
- (b) redocumentation and/or document generation
- (c) understand the source code and associated documents
- **(d) All of the above**

Reverse engineering supports information recovery from legacy implementations, automated redocumentation, and system comprehension.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 476, 490; Slide 68; Answer Key p. 499.

---

### Q9.20
**Legacy systems are:**
- **(a) old systems**
- (b) new systems
- (c) undeveloped systems
- (d) None of the above

**Legacy systems** are mature, established operational software products that remain critical to enterprise operations but present maintenance challenges due to aging technology stacks.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 479, 490; Slide 68; Answer Key p. 499.

---

### Q9.21
**User documentation consists of:**
- (a) System overview
- (b) Installation guide
- (c) Reference guide
- **(d) All of the above**

User documentation packages user-facing guidance into introductory overviews, step-by-step installation guides, and complete operational reference manuals.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 486, 490; Slide 68; Answer Key p. 499.

---

### Q9.22
**Which one is not a user documentations ?**
- (a) Beginner's Guide
- (b) Installation guide
- **(c) SRS**
- (d) System administration

The **Software Requirements Specification (SRS)** is a technical development and system document establishing functional requirements, not an end-user guide.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 486, 490; Slide 68; Answer Key p. 499.

---

### Q9.23
**System documentation may not have:**
- (a) SRS
- (b) Design document
- (c) Acceptance Test Plan
- **(d) System administration**

System documentation records architectural and development specifications (SRS, SDD, Test Plans, Data Dictionaries). **System administration** is an operational user manual rather than an internal system design artifact.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 486, 490; Slide 69; Answer Key p. 499.

---

### Q9.24
**The process by which existing processes and methods are replaced by new techniques is:**
- (a) Reverse engineering
- **(b) Business process re-engineering**
- (c) Software configuration management
- (d) Technical feasibility

**Business Process Re-engineering (BPR)** restructures fundamental operational workflows to achieve major gains in cost, quality, and speed.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 481, 490; Slide 69; Answer Key p. 499.

---

### Q9.25
**The process of transforming a model into source code is:**
- (a) Reverse Engineering
- **(b) Forward engineering**
- (c) Re-engineering
- (d) Restructuring

**Forward engineering** is the conventional development process that moves from abstract models and requirement specifications down to physical source code implementation.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 480, 490; Slide 69; Answer Key p. 499.

---

## Retrieval Set & Active Recall Self-Test

1. In Q9.1, state the verified definition of Reverse Engineering.
2. In Q9.8 and Q9.9, state the maximum and minimum effort shares among the four maintenance categories.
3. List the eight cyclical phases of the Taute maintenance model in Q9.13.
4. What formula defines Annual Change Traffic (ACT) in Q9.14?
5. State the distinction between user documentation and system documentation based on Q9.21, Q9.22, and Q9.23.
"""

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Generated {md_path} successfully.")
