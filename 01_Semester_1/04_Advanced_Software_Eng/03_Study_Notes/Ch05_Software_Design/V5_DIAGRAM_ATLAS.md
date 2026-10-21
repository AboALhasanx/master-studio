# Chapter 5 — Diagram Atlas and Semantic Contracts

> This atlas is a source-navigation and reconstruction specification. A diagram must preserve its concept, notation, node/edge meaning, and direction—not merely resemble a slide. Rendered references are to be linked here once captured. The existing `08_DeepStudy_Ch05/99_SOURCE_MAP.md` is historical navigation and must be checked against the live 99-slide source before final use.

The current visual register is [source_figures/README.md](source_figures/README.md). It contains image renders of 74 selected original slides, including all slides with detected figure/table captions, the full central diagram sequences, and the source MCQ/exercise slides. Open the image before specifying or reconstructing any figure; extracted text and OCR are only navigation aids.

## Source figures and the correct model to preserve

| Source | Type / notation | What the image means | Reconstruction invariant / tool candidate |
|---|---|---|---|
| Slides 2–4 | Design-process conceptual model | Requirements/data move through analysis to a high-level design, with customer/developer roles and a transition from “what” toward “how” | Preserve actor roles, inputs/outputs, and distinction of analysis/design; use a typed process/concept model, not an unlabeled flowchart. |
| Slide 5 | Two-part design process | Conceptual design and technical design are separate but connected views | Keep the two views and their relation explicit; do not collapse them into a single phase label. |
| Slide 9 | Progressive refinement | Informal design outline is refined toward a detailed/finished design | Preserve ordering and increasing detail; a process/activity representation is suitable. |
| Slide 14 | Modularity versus software cost | Cost changes with number of modules and has a region of minimum cost around M; over-modularizing can increase integration/total cost | Replot from source curve shape and labels; do not invent numeric scale or coordinates. Use vector plotting/SVG. |
| Slides 15–16 | Coupling topology examples | Uncoupled, loosely coupled, and highly coupled module relationships | Show module nodes and actual dependency links; increasing link/dependency density communicates coupling. Not a UML class diagram unless the source says so. |
| Slides 18, 22, 24 | Coupling examples | Student-record edit, shared-global/common coupling, and content coupling | Keep which module reads/writes/branches into what explicit; label shared data or internal access precisely. |
| Slides 19–21 | Coupling taxonomy | Data, stamp, control, external, common, content coupling, ranked best to worst | Preserve exactly six categories and order; use a table/scale with direction key, not an unordered node cloud. |
| Slides 25–30 | Cohesion concepts/examples | Functional, sequential, communicational, procedural, temporal, logical, coincidental cohesion | Preserve exactly seven categories and their defining relation; use a table/scale and small semantic examples. |
| Slide 31 | Cohesion/coupling relationship | High-coupling and low-coupling module layouts; design target is high cohesion and low coupling | Preserve the two separate dimensions and their target direction; don't imply that high cohesion itself is a dependency edge. |
| Slide 33 | Bottom-up strategy | Low-level reusable modules are assembled toward higher-level systems | Module hierarchy; arrows/parent-child relation must match the source convention. Graphviz tree/structure chart. |
| Slides 34–35 | Top-down and hybrid strategy | Top-down decomposition and hybrid use of top-down plus existing/bottom-up modules | Contrast hierarchy-building direction and reuse; don't represent these as runtime execution order. |
| Slides 36–39 | Function-oriented decomposition/refinement | Functions are decomposed into interacting modules and refined toward implementation-level detail | Decomposition tree, not data-flow diagram; preserve module hierarchy and refinement levels. |
| Slides 41–43 | Structure-chart notation and update-file example | Modules, calls, data/control couples, and a concrete update-file structure | Use structure-chart notation: module hierarchy and invocation/control relations; label data/control couples according to source. Never substitute a flowchart. |
| Slides 44–45 | Transaction-centred structure chart | A transaction-processing system branches from a transaction discriminator into transaction paths | Preserve transaction center, branches, and module-call hierarchy; Graphviz/DOT or custom SVG. |
| Slide 46 | Pseudocode notation | Structured English used to describe processing/control at different levels of detail | Preserve pseudocode as a textual design notation; do not redraw it as a UML activity diagram unless explicitly asked to translate it. |
| Slides 47–49 | Functional procedure layers | Layered presentation of procedures/design notation | Preserve level boundaries and what detail each level specifies; distinguish these levels from a deployment architecture. |
| Slides 50–57 | IEEE SDD purpose, definitions, information content, organization, and design views | IEEE Std 1016-1998 course treatment; tables and document organization (book pp.221–225) | Reproduce as tables/document structure. Preserve the source's distinction among scope, definitions, purpose, content, and organization; this is not a UML diagram. |
| Slide 63 | Class and instances | Indica/Santro/Maruti/Indigo are instances of class Car | UML object/class distinction: instances are not subclasses. PlantUML class/object notation. |
| Slides 64–68 | Classes, attributes, abstraction, inheritance | Square/Triangle examples share common features abstracted into Shape; inheritance carries state/behavior | Preserve common superclass and subclass generalization, with only evidenced attributes/operations. UML class diagram. |
| Slide 70 | Class hierarchy | Generalization/specialization hierarchy | Use UML generalization semantics and arrow direction verified against OMG UML; do not use a generic arrow without a legend. |
| Slides 72–73, 75–81 | OOD analysis/design steps and outputs | Slide 72 lists the six steps; slides 73–81 explain or illustrate use-case, activity, interaction, object roles, class, state, component/deployment, and use-case/library views | Keep the six-step sequence and its conditional “if required” items exactly as shown. Consult each slide individually: 74 is the activity figure; 75 introduces interaction diagrams; 76 defines entity/boundary/control roles; 77–78 cover class diagrams and relationships; 79 state-chart; 80 component/deployment; 81 starts the library use-case case. Do not merge distinct diagram kinds. |
| Slide 81 and later library case slides | Use-case diagram and library case | Actors, system boundary, use cases, and library-management interactions | Keep actor-goal associations and system boundary; sequence/use-case/class views are different diagrams. PlantUML use-case for the formal view. |

## Out-of-slide professor-feedback diagrams

### DFD → structure chart

The professor explicitly asked for the methodology omitted from the seminar. Treat this as a distinct modeling transformation: a DFD models data transformations and flows; a structure chart models modules, calls, and passed data/control couples. Use Mall §6.4.1 (PDF pp.344–349) as the candidate support. Its transform-analysis path separates the DFD into input, central-processing, and output regions (afferent branch, central transform, efferent branch), then maps them below a root module. Transaction analysis instead identifies distinct transaction paths and a transaction discriminator, then forms corresponding module branches. These are design guidelines, not automatic graph conversion rules; inspect the exact source examples before choosing. Before drawing, make a typed inventory of external entities, processes, data stores, flows, input/central-transform/output regions or transaction branches; then state the mapping to modules and control structure. Preserve the chosen DFD symbol convention (Yourdon/DeMarco or Gane–Sarson) in a legend. A visually tidy chart with the wrong information-flow/control-flow semantics fails.

### UML figure contract

For every UML redraw, record the UML diagram kind, source slide/page, model elements, relationship types, multiplicities, arrow directions, stereotypes, guards/events, and any conditional/not-required elements. Validate element relationships against the course source and UML 2.5.1 semantics. PlantUML is the first code-generation candidate; keep `.puml` plus rendered SVG/PNG.

### Diagram source-of-truth and verification

Each figure will have: (1) a source screenshot/render with page/slide anchor; (2) a concise semantic spec (YAML/JSON or a fully structured Markdown block); (3) editable text code (`.puml`, `.dot`, `.mmd`, or plotting script); (4) generated SVG/PNG; and (5) a review record. Check that all required nodes/relations/labels exist, the renderer succeeds, and the final image is legible beside the source at print scale. A pixel diff may find layout changes but cannot establish semantic correctness. Keep OCR as a search aid only.

The reusable machine-readable contract template is `V5_DIAGRAM_CONTRACT_TEMPLATE.json`. The vault already contains `90_Shared_Toolbox/tools/diagram_forge.py`, which renders local HTML/SVG diagram source to a high-resolution PNG for inspection and print use. It is a renderer, not a semantics checker: the contract and source comparison remain mandatory. For formal UML, add a UML-aware parser/conformance check before treating a rendered shape as a correct UML diagram.

**Pilot completed:** Chapter slide 68, Fig. 23 (Shape/Square/Triangle class generalization) now has editable SVG-in-HTML source, a 2× rendered PNG, and a checked semantic record in `V5_DIAGRAM_CONTRACTS.json`. The arrowheads target the superclass `Shape`; seven member strings are retained from the slide. The custom SVG was checked against the source image but was not run through a UML conformance parser. The DFD-transformation and transaction-centered structure-chart pilots were completed in the 2026-10-19 follow-up below; no UML conformance parser was used.

## Official diagram-as-code references

- OMG, [UML 2.5.1 specification](https://www.omg.org/spec/UML/2.5.1/PDF): normative model semantics and notation.
- PlantUML, [language specification index](https://plantuml.com/sitemap-language-specification), [class](https://plantuml.com/class-diagram), [use-case](https://plantuml.com/en-dark/use-case-diagram), [activity](https://plantuml.com/en/activity-diagram-beta), [sequence](https://plantuml.com/en/sequence-diagram), [state](https://plantuml.com/en/state-diagram), [component](https://plantuml.com/en/component-diagram), and [deployment](https://plantuml.com/deployment-diagram) syntax.
- Mermaid, [official guide](https://mermaid.js.org/landing/) and [class-diagram syntax](https://mermaid.js.org/syntax/classDiagram): useful text-defined diagrams, with supported syntax/version boundaries checked before use.
- Graphviz, [DOT language](https://www.graphviz.org/content/dot-language/) and [hierarchical `dot` layout](https://graphviz.org/docs/layouts/dot/): suitable for directed module hierarchies; custom notation still requires explicit node/edge rules.
- IEEE, [1016-2009 overview](https://standards.ieee.org/ieee/1016/4502/): confirms SDD purpose/content and records that 1016-2009 revised the 1998 practice; course scope continues to cite 1998.

## Source-image navigation

Use the [complete selected-slide image register](source_figures/README.md) for direct visual inspection. Filenames preserve source slide numbers. These are source captures only; any redraw needs its own editable code and semantic contract, and must not overwrite the original image.


## Reconstruction pilots (2026-10-19)

Three editable prototypes test three different diagram semantics. They are study/preparation assets, not final question-pack figures:

- **UML class/generalization:** [Fig. 23 editable HTML/SVG](diagrams/CH05-FIG23_Shape-Inheritance.html) · [PNG](diagrams/CH05-FIG23_Shape-Inheritance.png) · source [slide 68](source_figures/slide-068.png).
- **Transaction-centered structure chart:** [Fig. 19 editable HTML/SVG](diagrams/CH05-FIG19_Transaction-Centered-Structure-Chart.html) · [PNG](diagrams/CH05-FIG19_Transaction-Centered-Structure-Chart.png) · source [slide 44](source_figures/slide-044.png) plus [symbol key, slide 42](source_figures/slide-042.png).
- **DFD → structure chart:** [RMS transform-analysis walkthrough HTML/SVG](diagrams/CH05-GAP_RMS_DFD-to-Structure-Chart.html) · [PNG](diagrams/CH05-GAP_RMS_DFD-to-Structure-Chart.png) · DFD source [Mall Fig. 6.8(b), PDF p.329](source_figures/mall-pdf-329.png) · chart source [Mall Fig. 6.19, zoom](source_figures/mall-fig619-zoom.png). This deliberately pairs Example 6.1's Level-1 DFD with Example 6.6's chart; Mall p.345 explicitly says Example 6.6 derives its chart from the DFD of Example 6.1.

Machine-readable requirements, edge directions, validation, and known limitations are in [V5_DIAGRAM_CONTRACTS.json](../V5_DIAGRAM_CONTRACTS.json). A renderer/parser pass alone is not semantic validation; use the source images and contracts together.
