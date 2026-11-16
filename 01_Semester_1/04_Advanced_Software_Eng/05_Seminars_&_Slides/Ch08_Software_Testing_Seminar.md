---
marp: true
theme: gaia
paginate: true
header: Advanced Software Engineering · Software Testing
footer: CS603 · Chapter 8
style: |
  section { font-family: Arial, sans-serif; color: #111; background: #fff; }
  h1, h2, h3 { color: #111; }
  header, footer { color: #555; font-size: 12px; }
  table { font-size: 0.78em; }
  blockquote { border-color: #777; color: #222; }
  a { color: #222; }
---

<!-- INTERNAL SCOPE: built from V8_Predictive_Vocabulary.md. This is provisional, not Dr. Fahim's confirmed vocabulary list. -->

# Software Testing

## Selecting Evidence Through Test Design

Advanced Software Engineering · Chapter 8

---

## Testing produces evidence, not proof

- A test executes a program to expose errors through observed behavior.
- A finite test set samples inputs and execution paths.
- Exhaustive testing is impractical for non-trivial programs because input combinations and paths grow rapidly.
- A passing test supports confidence in the tested conditions; it does not establish that every defect is absent.

| Term | Role in the chain |
|:--|:--|
| **Mistake / error** | A human action or judgment introduces a problem. |
| **Fault / defect** | The problem is represented in a software artifact. |
| **Failure** | Executing the fault produces externally observable behavior that violates expectations. |

A fault may remain dormant on one run and produce a failure on another. Follow the course source's terminology; these labels are not used identically in every taxonomy.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 2–9.  
**Related reading:** Myers, Badgett, and Sandler, “Test-Case Design.”

---

## Verification and validation

| Verification | Validation |
|:--|:--|
| Does a work product satisfy the conditions set for its development phase? | Does the resulting system satisfy its specified requirements and intended use? |
| Checks conformance to a stated basis. | Checks whether the product is acceptable for its intended users or customer. |

Acceptance testing involves the customer or end users. In the course deck, **alpha testing** takes place at the developer's site in a controlled setting; **beta testing** takes place at users' sites in a real setting.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 11–12 and 170–179.

---

## Two complementary test-design views

| Functional / black-box | Structural / white-box |
|:--|:--|
| Select tests from specified input-output behavior. | Select tests from internal control or data structure. |
| Equivalence classes, boundary values, decision tables, cause-effect graphs. | Flow graphs, independent paths, cyclomatic complexity, data-flow criteria. |
| Asks which behaviors the specification requires. | Asks which internal structures the tests exercise. |

The views answer different questions. A test set can exercise required examples while leaving important internal paths or data uses untouched.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 13–103 and 104–169.

---

## Partition inputs before choosing cases

**Equivalence-class partitioning** groups inputs expected to be handled similarly. Select representative values from valid and invalid classes rather than testing every value.

**Boundary Value Analysis (BVA)** focuses on class edges, where implementation mistakes often change behavior.

For the course's single-fault convention, with *n* input variables:

| Method | Test-count convention |
|:--|:--:|
| BVA | $4n + 1$ |
| Robustness testing | $6n + 1$ |
| Worst-case testing | $5^n$ |

Robustness adds values just outside valid limits; worst-case testing combines boundary values across variables.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 20–46.  
**Related reading:** Myers, Badgett, and Sandler, “Test-Case Design,” DOI: [10.1002/9781119202486.ch4](https://doi.org/10.1002/9781119202486.ch4).

---

## Convert rules into test cases

When outcomes depend on combinations of conditions:

1. List the relevant **conditions** and **effects**.
2. Represent their relationships in a cause-effect graph.
3. Convert the graph into decision rules in a decision table.
4. Choose tests that exercise the distinct rules.

This makes combinations visible and helps identify missing, contradictory, or redundant cases. It does not replace checking the source specification.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 47–103.  
**Related reading:** Myers, Badgett, and Sandler, “Test-Case Design,” DOI: [10.1002/9781119202486.ch4](https://doi.org/10.1002/9781119202486.ch4).

---

## Control-flow testing

- A **flow graph** represents possible control transfers through a program.
- A **DD-path** compresses a sequence between decision points.
- An **independent path** contributes at least one new edge to the basis of paths already selected.
- Path counts can grow rapidly, especially when loops are present; covering a basis is not the same as executing every possible path.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 104–131.

---

## Cyclomatic complexity

For a flow graph $G$:

$$V(G) = E - N + 2P$$

- $E$: edges; $N$: nodes; $P$: connected components.
- For a single connected program graph, $P = 1$.
- The course also presents region count and predicate-node count plus one as equivalent calculations under its graph assumptions.
- $V(G)$ gives the size of an independent-path basis; it is a structural test-design aid, not a defect count or a guarantee of correctness.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 132–146.  
**Primary reference:** T. J. McCabe, “A Complexity Measure,” *IEEE Transactions on Software Engineering*, vol. SE-2, no. 4, pp. 308–320, 1976. DOI: [10.1109/TSE.1976.233837](https://doi.org/10.1109/TSE.1976.233837).

---

## Follow definitions to their uses

**Data-flow testing** selects paths that connect a variable's definition to a use without an intervening redefinition.

- A **definition** assigns a value.
- A **use** reads that value in a computation or decision.
- A **definition-clear path** preserves the value between those points.

This view can expose uninitialized, overwritten, or unused values that a control-flow-only view may miss.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 155–161.

---

## Mutation testing asks whether tests detect change

1. Create a small program variant (**mutant**) by changing an operator or statement.
2. Run the test suite against the original and the mutant.
3. A test that distinguishes their behavior **kills** the mutant.
4. A surviving mutant may indicate a test gap, or it may be equivalent to the original for all relevant inputs.

The number of surviving mutants does not directly equal the number of additional tests required; one test may distinguish multiple mutants.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 162–169.  
**Related reading:** Y. Jia and M. Harman, “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering*, vol. 37, no. 5, pp. 649–678, 2011. DOI: [10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62).

---

## Levels, integration, and debugging

| Area | Question it answers |
|:--|:--|
| **Unit testing** | Does an individual module behave as expected? |
| **Integration testing** | Do connected modules exchange data and control correctly? |
| **System testing** | Does the assembled system meet its system-level requirements? |
| **Validation / acceptance** | Is the product suitable for its intended users and customer? |

Top-down, bottom-up, and sandwich integration use different orders; **stubs** and **drivers** support components that are not yet available. Debugging then traces an observed failure to its cause rather than treating the symptom as the fault.

**Course source:** Aggarwal & Singh, Chapter 8 deck, slides 170–188.

---

## Summary and references

No single technique covers every source of failure. Choose tests from the specification, the control structure, and the movement of data; interpret coverage as evidence about the selected test basis.

**Course source**  
K. K. Aggarwal and Y. Singh, *Software Engineering*, 3rd ed., Chapter 8 course deck, slides 2–188, New Age International Publishers, 2007.

**Supplementary sources**

- G. J. Myers, T. Badgett, and C. Sandler, “Test-Case Design,” in *The Art of Software Testing*, 3rd ed., 2012. DOI: [10.1002/9781119202486.ch4](https://doi.org/10.1002/9781119202486.ch4).
- T. J. McCabe, “A Complexity Measure,” *IEEE Transactions on Software Engineering*, vol. SE-2, no. 4, pp. 308–320, 1976. DOI: [10.1109/TSE.1976.233837](https://doi.org/10.1109/TSE.1976.233837).
- Y. Jia and M. Harman, “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering*, vol. 37, no. 5, pp. 649–678, 2011. DOI: [10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62).

<!-- Scope note: This seminar follows the Chapter 8 predictive vocabulary map and must be reconciled with Dr. Fahim's official list if supplied. -->
