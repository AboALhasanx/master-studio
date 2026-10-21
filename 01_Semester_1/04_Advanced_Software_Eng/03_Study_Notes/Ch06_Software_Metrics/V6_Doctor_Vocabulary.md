# Chapter 6 — Software Metrics: Supplied Vocabulary

> Scope record prepared from the student's supplied Chapter 6 vocabulary on 2026-10-19. The original instructor post is not attached here; preserve the wording as supplied and treat it as the chapter scope, not as an exam-weight prediction.

## 1. Fundamentals of Measurement

- Why measure software — the questions metrics answer
- Measure, measurement, metric, and indicator
- Direct versus indirect measures
- Measurement theory: entities, attributes, scales
- Scales of measurement: nominal, ordinal, interval, ratio, absolute
- Representation condition and meaningfulness of a metric
- Goal–Question–Metric (GQM) paradigm
- Areas of application and problems during implementation

## 2. Categories of Metrics

- Product metrics
- Process metrics
- Project metrics
- Internal versus external attributes
- Predictor metrics versus control metrics

## 3. Size Metrics

- Lines of Code (LOC, KLOC): definitions and counting rules
- Strengths and criticisms of LOC
- Function Points: components, complexity weights, value adjustment factor
- Feature Points and Mark II Function Points
- Object Points
- Converting between size measures (backfiring)

## 4. Halstead's Software Science

- Token count: operators and operands
- Vocabulary (η) and program length (N)
- Program volume (V) and potential volume (V*)
- Program level (L) and difficulty (D)
- Effort (E) and estimated time (T)
- Estimated program length and error percentage
- Language level (λ) and the language-level table
- Counting rules for C
- Criticisms and empirical validity of software science

## 5. Data Structure Metrics

- Input, internal and output data
- Amount of data: VARS, η₂, cross-reference lists
- Live variables: three definitions
- Average live variables (L̄V)
- Variable span (SP) and average span size
- Module weakness (WM) and program weakness (WP)
- Deriving program-wide metrics from module metrics

## 6. Information Flow Metrics

- Fan-in and fan-out
- Henry and Kafura's information flow metric
- Length and complexity weighting
- IF4 and its variants
- Shepperd's refinements
- Interpreting high fan-out and high fan-in

## 7. Control Flow and Complexity Metrics

- Cyclomatic complexity (McCabe): three computation methods
- Essential complexity and design complexity
- Knot count and nesting depth
- Relationship between complexity and testability

## 8. Object-Oriented Metrics

- Why traditional metrics fall short for OO systems
- The CK (Chidamber & Kemerer) suite:
  - Weighted Methods per Class (WMC)
  - Depth of Inheritance Tree (DIT)
  - Number of Children (NOC)
  - Coupling Between Objects (CBO)
  - Response For a Class (RFC)
  - Lack of Cohesion in Methods (LCOM)
- MOOD metrics suite
- Lorenz and Kidd metrics
- Class size, method size and inheritance metrics

## 9. Use-Case Oriented Metrics

- Use Case Points (UCP)
- Unadjusted actor weights and use case weights
- Technical and environmental complexity factors
- Estimating effort from use case points
- Comparison with function points

## 10. Quality and Defect Metrics

- Defect density and defect removal efficiency
- Defects per function point / per KLOC
- Phase containment effectiveness
- Mean time between failures as a product metric
- Customer-reported problem metrics

## 11. Productivity and Process Metrics

- Productivity measures: LOC/PM, FP/PM
- Effort distribution across phases
- Rework and cost of quality
- Process maturity metrics

## 12. Metrics Analysis and Program

- Statistical analysis of metric data
- Correlation, regression and outliers
- Validation of metrics: theoretical and empirical
- Establishing a metrics program in an organisation
- Baselines, data collection and tooling
- Common pitfalls: measurement dysfunction, gaming, misuse against individuals
- Ethics of software measurement

## Provenance boundary

This ledger preserves the student's supplied wording. It does not claim that every bullet appears in the course slides or in the primary textbook. The chapter source map records where a term is supported, partly supported, or still requires verification. The seminar PDF is only a navigation aid and is not answer authority.
