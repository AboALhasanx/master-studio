import os

out_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance"
md_path = os.path.join(out_dir, "T3_Compare_Analyze.md")

content = r"""# Advanced Software Engineering — Chapter 9: Software Maintenance
## T3: Comparative & Analytical Evaluations

### Q9.A1 (Exercise 9.3): Analytical Evaluation of "Maintenance is Manageable"
**Prompt:**
Some people feel that "maintenance is manageable". What is your opinion about this issue?

Software maintenance is manageable when governed by rigorous engineering discipline, but becomes unmanageable under typical ad-hoc legacy practices:

1. **Conditions Under Which Maintenance is Manageable:**
   - **Modular Architecture:** Low inter-module coupling and high functional cohesion contain the blast radius of changes.
   - **Synchronized Documentation:** Up-to-date requirements (SRS), design descriptions (SDD), and data dictionaries allow engineers to comprehend system intent quickly.
   - **Configuration Management:** A formal Configuration Control Authority (CCA) processes modifications through structured change-request evaluations.
   - **Automated Regression Harnesses:** Comprehensive regression suites provide rapid feedback on delta impacts.

2. **Conditions Under Which Maintenance Becomes Unmanageable:**
   - **Quick-Fix Patching:** Applying code patches without updating design specifications rapidly degrades system architecture (software entropy).
   - **Tacit Knowledge Loss:** High turnover among original authors leaves unrecorded architectural assumptions.
   - **Ripple Effect Amplification:** In highly coupled architectures, localized edits trigger unforeseen failures across distant modules.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 461–463; Slides 6–9.

---

### Q9.A2 (Exercise 9.5): Perception of Maintenance as Inferior to Development
**Prompt:**
Why do you think that the mistake is frequently made of considering software maintenance inferior to software development?

The perception of software maintenance as subordinate to initial development stems from organizational, cultural, and cognitive misconceptions:

1. **The "Clean Slate" Fallacy:**
   - Initial software development is viewed as creative greenfield innovation where developers design architectures without legacy constraints.
   - Maintenance is mischaracterized as custodial or janitorial work focused merely on cleaning up residual defects.
2. **Cognitive Asymmetry & Intellectual Difficulty:**
   - Maintenance is intellectually more demanding than new development. Maintainers must decipher complex logic written by departed authors under obsolete technologies, deduce undocumented assumptions, and implement modifications within rigid architectural boundaries.
3. **Economic Invisibility vs Capital Investment:**
   - Initial development produces a tangible, visible product celebrated with launches and milestone bonuses.
   - Maintenance primarily prevents operational failure and absorbs **40% to 70%** of total lifecycle expenditures, often viewed by management as a recurring operational liability rather than asset preservation.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 459–463; Slides 3–7.

---

### Q9.A3 (Exercise 9.9): Ripple Effect Dynamics & Impact on Program Stability
**Prompt:**
What is ripple effect? Discuss the various aspects of ripple effect and how does it affect the stability of a program?

In the software maintenance process (Section 9.2.3, p. 465), the **ripple effect** refers to the phenomenon where a modification implemented in one component unintentionally affects or destabilizes other components across the system.

1. **Definition of Program Stability:**
   - Program stability is formally defined as:
     $$\text{Program Stability} = \text{The resistance to the amplification of changes in a program.}$$
2. **Propagation Mechanisms:**
   - **Data Ripple Effect:** Occurs when a variable, global data structure, or database field is modified, altering state assumptions in downstream consumers.
   - **Control Ripple Effect:** Occurs when modified logic branches alter the execution sequence, preconditions, or postconditions expected by calling routines.
3. **Impact on Program Stability:**
   - In a system with low stability, small changes are amplified: modifying one variable can cause faults across numerous dependent modules.
   - Accounting for ripple effects (Phase 3 of the maintenance process) is critical to maintaining program stability and preventing regression defects.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 464–465; Slide 11.

---

### Q9.A4 (Exercise 9.20): Development Testing versus Regression Testing
**Prompt:**
What is regression testing? Differentiate between regression and development testing.

**Regression testing** retests modified software to ensure that changes have corrected faults or added features without introducing defects or breaking existing capabilities.

1. **Primary Objective:**
   - **Development Testing:** Uncovers defects and verifies that newly developed code conforms to functional specifications.
   - **Regression Testing:** Verifies that unmodified portions of the system continue to function correctly and that no side-effects were introduced by code deltas.
2. **Test Suite Dynamics:**
   - **Development Testing:** Test cases are created incrementally from scratch alongside code construction.
   - **Regression Testing:** Reuses, adapts, and executes existing baseline test suites accumulated across previous development cycles.
3. **Execution Frequency & Automation:**
   - **Development Testing:** Executed primarily during initial development phases.
   - **Regression Testing:** Executed repeatedly throughout post-delivery maintenance, requiring automated execution harnesses.
4. **Failure Interpretation:**
   - **Development Testing:** A failure indicates a fault in newly developed logic.
   - **Regression Testing:** A failure indicates a regression or broken dependency in previously working features.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 473–474; Slides 32–34.

---

### Q9.A5 (Exercise 9.21): Importance of Regression Test Selection (RTS) with Examples
**Prompt:**
What is the importance of regression test selection? Discuss with help of examples.

As software evolves, accumulated test suites grow to encompass thousands of test cases. Executing every test case (**Retest-All**) for every minor patch is computationally and economically prohibitive.

1. **Resource Optimization:** RTS reduces testing time and execution costs while preserving fault detection effectiveness.
2. **Rapid Release Turnaround:** Enables rapid deployment of critical fixes and continuous integration workflows.

**Example (Code Delta Selection Logic; Slides 35–36):**
- Consider a program $P$ with modules $M_1, M_2, M_3$ and baseline test suite $T = \{t_1, t_2, t_3, t_4, t_5\}$.
  - $t_1, t_2$ execute paths exclusively inside $M_1$.
  - $t_3, t_4$ execute paths crossing $M_1$ and $M_2$.
  - $t_5$ executes paths exclusively inside $M_3$.
- Suppose a maintenance modification changes module $M_2$ to create version $P'$.
- **Selection Decision:**
  - Tests $t_1, t_2,$ and $t_5$ do not traverse modified module $M_2$.
  - Tests $t_3$ and $t_4$ traverse modified statements in $M_2$.
  - The RTS algorithm selects subset $T' = \{t_3, t_4\}$, executing only $40\%$ of the suite while ensuring modified paths are verified.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 474–475; Slides 34–36.

---

### Q9.A6 (Exercise 9.22): Selective Retest Techniques versus Retest-All
**Prompt:**
What are selective retest techniques? How are they different from "retest-all" techniques?

1. **Retest-All Paradigm:**
   - Executes every test case in the existing baseline test suite $T$ on the modified program $P'$.
   - **Advantage:** Maximum safety; ensures all baseline features are re-verified.
   - **Disadvantage:** Inefficient; executes tests whose execution paths are completely decoupled from the modification.
2. **Selective Retest Paradigm:**
   - Uses algorithmic analysis (control flow graphs, modification deltas) to select a proper subset $T' \subset T$ relevant to verifying $P'$.
   - **Advantage:** Substantially reduces testing execution time and computational expense.
   - **Challenge:** Requires selection algorithms that ensure no test capable of revealing a modification fault is omitted.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 474–475; Slides 36–37.

---

### Q9.A7 (Exercise 9.23): Categories of Retest Techniques & Why Minimization is Non-Useful
**Prompt:**
Explain the various categories of retest techniques. Which one is not useful and why?

Selective retest techniques fall into three categories:

1. **Coverage-Based Techniques:** Selects test cases that satisfy structural coverage criteria across modified code entities (e.g., executing all modified statements or branches).
2. **Minimization-Based Techniques:** Identifies a minimal subset of test cases that satisfies structural coverage of modified components.
3. **Safe Techniques:** Guarantees that every test case in $T$ executing at least one modified path in $P'$ is selected, achieving $100\%$ inclusiveness.

**Why Minimization is Non-Useful in Practice:**
Minimization techniques discard tests that cover identical code statements. However, two test cases executing the same statement may carry different input data values. One test may pass while another exposes an arithmetic overflow or boundary defect. By pruning tests based solely on structural redundancy, minimization sacrifices safety and introduces defect leakage risk.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 474–475; Slide 38.

---

### Q9.A8 (Exercise 9.24): Rothermel & Harrold Evaluation Criteria for RTS Techniques
**Prompt:**
What are the categories to evaluate regression test selection techniques? Why do we use such categorisation?

Rothermel and Harrold established four evaluation criteria for RTS algorithms:

1. **Inclusiveness:** Measures the extent to which an RTS technique selects test cases that reveal modification-induced defects:
   $$\text{Inclusiveness} = \frac{\text{Selected Fault-Revealing Tests}}{\text{Total Available Fault-Revealing Tests}} \times 100\%$$
   A safe technique achieves $100\%$ inclusiveness.
2. **Precision:** Measures the ability to exclude test cases that do not traverse modified code paths and cannot reveal faults.
3. **Efficiency:** The computational time and space required to execute the selection algorithm compared to the testing time saved.
4. **Generality:** The applicability of the technique across diverse language constructs, control structures, and system architectures.

**Purpose of Categorization:**
This framework formalizes the trade-off between **safety** (inclusiveness) and **cost reduction** (precision and efficiency).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), p. 475; Slide 39.

---

### Q9.A9 (Exercise 9.27): Comparison of Reverse Engineering and Re-engineering
**Prompt:**
Discuss reverse engineering and re-engineering.

1. **Core Distinction:**
   - **Reverse Engineering:** An analysis and comprehension process. It analyzes an existing system to extract its components, recover architecture, and understand behavior without altering the code or changing system functionality. It is fundamentally non-mutating.
   - **Re-engineering:** A comprehensive transformation lifecycle. It encompasses reverse engineering to understand the system, restructuring to improve internal quality, and forward engineering to rebuild the software in a modernized form. It is fundamentally mutating.
2. **Process Composition:**
   $$\text{Re-engineering} = \text{Reverse Engineering} + \text{Restructuring} + \text{Forward Engineering}$$
3. **Lifecycle Direction:**
   - Reverse engineering moves upward in abstraction (Implementation $\to$ Design $\to$ Specification).
   - Re-engineering moves upward via reverse engineering, horizontally via restructuring, and downward via forward engineering to produce an updated operational baseline.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 476–481; Slides 41–48.

---

### Q9.A10 (Exercise 9.28): Re-engineering versus New Software Development
**Prompt:**
What is re-engineering? Differentiate between re-engineering and new development.

**Re-engineering** is the examination and alteration of an existing software system to reconstitute it in a new form and the subsequent implementation of that new form.

**Structural Comparison (Fig. 9.12, Slide 48):**

1. **Lifecycle Trajectory:**
   - **New Development:** Starts from abstract System Specifications $\to$ Design & Implementation $\to$ New System.
   - **Re-engineering:** Starts from an Existing Operational Software System $\to$ Understanding & Transformation (Reverse Engineering & Restructuring) $\to$ Re-engineered System.
2. **Business Rule Preservation:**
   - **New Development:** Carries risk of omitting undocumented tacit business rules accumulated over years of maintenance.
   - **Re-engineering:** Recovers and preserves existing business logic directly from working source code.
3. **Risk Profile & Economics:**
   - **New Development:** Higher technical and schedule risk.
   - **Re-engineering:** Lower risk because existing software serves as a proven functional baseline. Re-engineering is economically justified when cost satisfies $C_{\text{reeng}} \le 0.5 \times C_{\text{new}}$ (Sneed's rule).

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 480–481; Slide 48.

---

### Q9.A11 (Exercise 9.31): Single-Entry Single-Exit (SESE) Modularity & Testing Integrity
**Prompt:**
Explain why single entry, single exit modules make testing easier during maintenance.

A Single-Entry Single-Exit (SESE) module possesses exactly one designated entry point and exactly one normal exit point.

**Why SESE Simplifies Testing During Maintenance:**

1. **Deterministic State Preconditions & Postconditions:**
   - Execution cannot enter through arbitrary midpoint jumps (`goto` statements or secondary entry labels). Test harnesses can establish guaranteed input preconditions at the single entry and inspect guaranteed postconditions at the single exit.
2. **Elimination of Hidden Execution Bypasses:**
   - In modules with multiple arbitrary exits (such as premature returns scattered across nested conditionals), execution paths frequently bypass resource cleanup, variable resets, or logging. SESE guarantees that all paths converge at a unified exit, ensuring cleanup code executes consistently.
3. **Composable Unit Test Scaffolding:**
   - SESE modules function as clean, encapsulated blocks. Path analysis is straightforward because all valid execution paths originate at node $N_{\text{entry}}$ and terminate at node $N_{\text{exit}}$.

*(Note: SESE enforces structured control-flow predictability; it does not inherently alter McCabe's cyclomatic complexity, which is determined by decision predicate counts).*

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 482–483, 491; Slide 51.

---

### Q9.A12 (Exercise 9.35): High Module Coupling as a Maintenance Bottleneck
**Prompt:**
Explain why a high degree of coupling among modules can make maintenance very difficult.

**Coupling** measures the degree of interdependence and interconnectedness between software modules. High coupling (such as shared global data or direct access to internal module structures) creates severe maintenance bottlenecks:

1. **Amplification of Ripple Effects:**
   - Modifying a variable or interface in module $A$ triggers unintended side-effect failures in coupled modules $B, C,$ and $D$.
2. **Cognitive Overhead:**
   - Maintainers cannot understand or modify a coupled module in isolation. To modify module $A$, the engineer must read and comprehend all other modules linked to it.
3. **Regression Test Explosion:**
   - Under loose coupling, modifying module $A$ requires retesting only $A$ and its direct interfaces. Under high coupling, changes invalidate system-wide baselines, forcing expensive Retest-All sweeps.

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), pp. 464–465, 491; Slide 11.

---

## Retrieval Set & Active Recall Self-Test

1. In Exercise 9.3, state the specific engineering conditions under which software maintenance is manageable.
2. State the formal definition of program stability in Section 9.2.3 and explain how the ripple effect impacts it (Exercise 9.9).
3. Distinguish between development testing and regression testing across primary objective and test suite dynamics (Exercise 9.20).
4. In Exercise 9.23, why is test suite minimization considered hazardous in mission-critical maintenance?
5. State the four Rothermel & Harrold evaluation criteria for regression test selection techniques (Exercise 9.24).
6. Explain why Single-Entry Single-Exit (SESE) modules simplify unit and regression testing during maintenance (Exercise 9.31).
"""

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Generated {md_path} successfully. Total comparative/analytical exercises: 12")
