# Chapter 6 — Candidate Diagram and Visual Atlas

This is a source-navigation and reconstruction checklist, not a collection of newly authored diagrams. Retain only visuals that support a supplied vocabulary item or a source exercise.

| Visual family | Candidate source | What to inspect and preserve | Study/use potential |
|---|---|---|---|
| Measurement / metric question map | Aggarwal slides 2–6 | Question wording, grouping, and relationship between measurement, management information and improvement. | Explain why metrics answer distinct project/product questions. |
| Metric-category examples | Slides 9–10 | Product/process/project grouping and listed examples. | Classification practice; avoid extending categories without a source. |
| Halstead tables and code examples | Slides 11–38 | Operator/operand token sets, table columns, formula notation, worked-example sequence. | Recreate a counting table and a formula workflow; numbers and symbols need independent verification. |
| Input/internal/output data view | Slide 39 | Data boundaries, inputs/outputs and internal data nodes/links. | Distinguish data categories before applying data-structure metrics. |
| Program and cross-reference list | Slides 41–44, 56–62 | Source-code labels, variable names, statement references, ordering and any excluded tokens. | Build/read a cross-reference list; avoid claiming an OCR table preserves spatial alignment. |
| Live-variable and span traces | Slides 45–53, 63–68 | Statement order, live-variable sets, counts, span endpoints and averaging denominator. | Hand trace with a table; compare displayed source result to an independent check. |
| Shared data / information-flow graph | Slides 69–77; Pressman 5e §19.4.2, printed p.524 for Henry–Kafura | Components, call/data connections, fan-in/out direction, hierarchy levels, parameters and model-specific weights. Slide 74 sets top-level fan-in and leaf fan-out to 1 for its basic procedure; it warns that this fan-in model can penalize reuse. Pressman's HKM uses module statement length × [fin+fout]² and includes control and data connections. | Calculate each named variant separately; preserve slide boundary conventions when reproducing that procedure; do not label the slide's simple model Henry–Kafura without evidence. Arrows must match the source's direction. |
| OO metric tables / class structures | Slides 78–88 | Definitions, class/method/attribute membership, inheritance direction, coupling and cohesion pair rules. | Derive metrics from a small class diagram only after the exact measure definition is verified. |
| UCP actor and use-case weight tables | Slides 89–90 | Actor interface classes and use-case transaction categories with their weights. | Calculation table; do not infer the missing adjustment factors from these two slides alone. |
| Statistical displays | Slide 92 (listed histograms, pie charts, box plots); supporting source only if a visual is present | Axis/scale, plotted metric, outliers, group comparison and caveats. | Read/interpret a chart, not merely name it. |
| Control-flow graph for McCabe measures | Aggarwal & Singh Ch.8 scan pp.422–425 (PDF spreads 217–218), slides 132–134 | Fig. 8.21 / Fig. 21 has nodes a–f, a unique entry/exit, 9 edges, one connected component and five independent paths. The source states V(G)=E−N+2P, predicate nodes + 1, and number of regions; preserve each directed edge and loop. | Draw from code or identify errors in a supplied graph; compute all three values and compare. Source figures visually checked at the spread/slide level. |
| GQM / metrics-program model | Course-source prose and targeted support pages to verify | Goal, questions, metrics, organizational context, baseline and feedback loop. | Construct a compact mapping and detect a metric that does not answer its stated question. |

## Rendering/review rule

Use a source-image view to capture layout/labels, and a source-anchored semantic contract before redrawing. For each generated vector, verify all nodes, connections, labels, order, weights and direction against the source. OCR and vector search can locate a figure but cannot validate its layout. Do not redraw a candidate whose exact source or vocabulary relevance is unconfirmed.
