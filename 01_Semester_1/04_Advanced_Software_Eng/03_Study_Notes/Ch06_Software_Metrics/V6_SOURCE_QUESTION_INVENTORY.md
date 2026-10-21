# Chapter 6 — Source Question Inventory

Inventory of the K.K. Aggarwal & Yogesh Singh Chapter 6 slide deck only. Chapter 4 size-estimation and Chapter 8 cyclomatic-complexity prompts/material are separate cross-chapter course sources and are not included in these 20+28 counts. This is a locator and tagging aid, not an answer key. The deck gives no identified publisher key; verify each answer from the relevant source pages. Counts do not imply marks or exam likelihood.

## MCQs: 20 items, slides 96–100

| ID | Main topic | Primary action / skill | Review flag |
|---|---|---|---|
| 6.1 | Metric categories | Identify the category that does not belong | — |
| 6.2 | Halstead | Recall attribution of software science measures | Verify spelling/name against source |
| 6.3 | Halstead | Select the vocabulary formula | Visually verified on slide 96 and scan p.304: η = η₁ + η₂; option (a) |
| 6.4 | Halstead | Interpret the unit/meaning of volume | Distinguish storage size from the model's definition |
| 6.5 | Halstead | Identify the unit used for effort | — |
| 6.6 | Halstead | Select the language-level relationship | Visually verified on slide 97: λ = L × V* = L²V; option (d) |
| 6.7 | Data-structure metrics | Select program weakness | Source defect: stem asks for program weakness, but every formula choice is for module weakness; slide 97 also repeats label (a). Book scan p.305 confirms WP is the mean of module weaknesses. Preserve and flag the original; author a separate corrected practice item if needed. |
| 6.8 | Information flow | Define fan-in | — |
| 6.9 | Information flow | Define fan-out | — |
| 6.10 | Size/complexity | Identify which option is not a size metric | — |
| 6.11 | Halstead | Identify which item is not a software-science measure | — |
| 6.12 | Halstead | Recall the Stroud-number range | Verify exact range and unit before keying |
| 6.13 | Halstead | Name the minimal-algorithm implementation measure | — |
| 6.14 | Halstead | Select the program-volume formula | Visually verified on slide 99 and scan p.305: V = N log₂η; option (a) |
| 6.15 | Size metrics | Identify the claimed standard size measure | Source wording is underspecified (“international standard”); choices omit function points. Preserve as ambiguous unless the course source defines its intended standard. |
| 6.16 | OO metrics | Identify a non-member of the listed metric set | — |
| 6.17 | OO cohesion | Distinguish direct versus indirect method connection | Verified: slide 85 defines LCC as TCC plus indirect connections; slide 100 key is (b) LCC. |
| 6.18 | OO inheritance | Interpret DIT | — |
| 6.19 | Web metrics | Distinguish a dynamic page | Adjacent course topic, not a named leaf in the supplied vocabulary |
| 6.20 | Size/complexity | Identify which option is not a size metric | Near-duplicate concept of 6.10; preserve source ID, but do not author another redundant copy |

## Written exercises: 28 items, slides 101–106

| ID | Main topic | Primary action / skill | Source-use note |
|---|---|---|---|
| 6.1 | Fundamentals | Define metrics and explain why measurement is needed | Short conceptual answer |
| 6.2 | Fundamentals | Explain application areas and implementation problems | Keep source examples distinct from later synthesis |
| 6.3 | Categories | Describe metric categories with examples | Core source coverage |
| 6.4 | Halstead | Explain software science and evaluate relevance to component-based development | Separate definition from the student's evidence-based evaluation |
| 6.5 | Halstead | Explain language level's role | — |
| 6.6 | Halstead | List the named measures/formulas | Use a verified formula ledger; not a substitute for calculation practice |
| 6.7 | Halstead | Calculate metrics from supplied unique-token counts | Values appear as η₁=20 and η₂=40 in extracted text; verify placement visually before solving |
| 6.8 | Halstead | Design/implement a source-code analysis tool | Stretch/application prompt; do not turn into a programming project in the print pack |
| 6.9 | Halstead | Compare C and Pascal implementations using software-science metrics | Adapt only with short, fully specified code fragments; otherwise the prompt is underdetermined and too large |
| 6.10 | Halstead | Apply token-counting rules to procedure identifiers | State the language/counting convention |
| 6.11 | Function points | Recalculate payroll FP after adding file/interface requirements | A direct applied calculation; identify changed inputs/outputs/files/queries and assumptions |
| 6.12 | Data-structure metrics | Define the family and explain amount-of-data counting | — |
| 6.13 | Data-structure metrics | Explain module weakness and program-level aggregation | — |
| 6.14 | Data-structure metrics | Create a cross-reference list and calculate requested measures from code | Original prompt lacks its own code listing; provide a self-contained, short code stem if adapted |
| 6.15 | Data-structure metrics | Demonstrate the relationship between SP and LV at a statement | Show definitions and endpoint/counting convention |
| 6.16 | Data-structure metrics | Explain relevance to testing | Conceptual application |
| 6.17 | Information flow | Explain the model | Distinguish the basic model from weighted variants |
| 6.18 | Analysis | Discuss metric-data problems and analysis methods | Include interpretation limits; correlation is not causation |
| 6.19 | Productivity/process | Explain process improvement and productivity effects | Avoid unsupported claims of guaranteed improvement |
| 6.20 | Size metrics | Explain LOC's limits for nesting/control structure | Connect the prompt to a verified control-flow metric only where sourced |
| 6.21 | Data structure / quality | Evaluate whether data metrics relate to complexity, quality, or both | Requires a bounded rationale, not an unsupported universal answer |
| 6.22 | Size/reuse context | Compare library reuse with writing code | Adjacent application prompt; keep if it helps the supplied size/productivity terms |
| 6.23 | Halstead and FP | Compare complexity measures and justify cost-prediction choice | State context and assumptions; no single universal winner |
| 6.24 | LOC estimates | Analyze how different initial estimates could affect a project | Scenario reasoning, not numeric estimation |
| 6.25 | Size metrics | Choose a suitable estimation technique | Must be conditional on project context and supported criteria |
| 6.26 | OO metrics | Describe OO metrics and their role | Use only the supplied CK/MOOD/Lorenz–Kidd scope |
| 6.27 | OO metrics | Define RFC, CBO, DAC, TCC, LCC and DIT | Check acronym expansions and metric versions |
| 6.28 | UCP | Explain the purpose/importance of use-case metrics | Source asks significance; the supplied list also requires calculation, so add one distinct calculation item if a verified formula source is found |

## Coverage gaps revealed by this source set

## Visual/source checks completed during preparation

- Slide 96 and the scanned book p.304 visually confirm MCQ 6.3: vocabulary η = η₁ + η₂ (choice a).
- Slide 97 visually confirms MCQ 6.6: λ = L × V* = L²V (choice d). Its MCQ 6.7 says “Program weakness” while all formula options name WM (module weakness); option labels also duplicate “(a)”. The scanned book p.305 distinguishes the concepts: WMᵢ is module weakness and WP is the arithmetic mean of the module weaknesses. Do not silently repair or miskey the source item.
- Slide 99 and scanned book p.305 visually confirm MCQ 6.14: V = N log₂η (choice a). MCQ 6.15's “international standard” wording is not resolved by its options and needs a source-grounded decision before inclusion as keyed practice.
- Slide 100 visually confirms MCQ 6.17 wording/options. Slide 85 defines LCC as TCC plus indirect method connections; the key is (b) LCC.
- Exercise 6.7's slide image confirms the given unique-token counts η₁=20 and η₂=40. These alone do not determine actual program length/volume/effort/time; check whether the source gives additional counts or explicitly asks for estimated variants before constructing a worked answer. Never invent token totals.
- Pressman 5e §19.4.2, PDF p.552 / printed p.524, explicitly gives the Henry–Kafura formula HKM = length(i) × [fin(i)+fout(i)]² and the relevant fan-in/out extension. This is a verified gap-only source. IF4 and Shepperd refinements remain unverified in the available source checks.

- The source exercises are concentrated in Halstead and data-structure metrics. They do **not** provide a direct worked problem for UCP calculation, cyclomatic-complexity calculation, quality/defect formulas, predictor/control classification, or statistical regression.
- Mark II function points, IF4/Shepperd variants, essential/design complexity, knot count, metric-validation methods, and measurement ethics beyond the cited professional duties remain bounded or partial; see the leaf statuses in `V6_Vocabulary_Coverage.md`. Measurement scales have Stevens and Fenton anchors; internal-versus-external attributes have a Sommerville anchor; Henry–Kafura has a Pressman anchor. MOOD/Lorenz–Kidd, Object Points, DRE and GQM have bounded support-book anchors in the source map/catalog.
- Add original questions only for genuinely uncovered supplied terms and nonredundant practice. Keep source IDs and authored-question IDs distinct. Never infer exam weight from this inventory.

## Initial nonduplicative practice emphasis

The later pack should be calculation-heavy enough to train each formula family once with a complete solution and then a small number of variants: Halstead; FP/size; data structure; information flow; cyclomatic complexity; OO metrics where computable; UCP if supported; and quality/productivity metrics where supported. Concept questions should close vocabulary gaps without repeating the source MCQs. Visual exercises should be limited to meaningful graphs, tables and traces, not decorative redraws.
