# Chapter 7 — Source Figure Atlas

All locations below refer to pages in the official 126-slide companion deck. The source figure itself—not extracted OCR text—is the semantic reference. Compare it with the matching scan figure and use the clearest complete original image for print. Figures are not answer paragraphs; keep explanations in the separate answer text.

**Initial source-preparation pass (2026-10-21):** a contact sheet of all 24 figure slides was inspected. That initial pass confirmed navigation and broad figure type only. The source-location table below preserves that extraction reference; it is not a current to-do list claiming that no figures were extracted.

**Current local status (2026-11-11):** T4_Diagrams.md contains 10 visual questions using 13 PNG assets in `diagrams/`, and T4_Diagrams.pdf exists. Its current embedded figures are 7.1, 7.2, 7.4, 7.5, 7.10, 7.11, 7.12, 7.13, 7.18, 7.21, 7.22, 7.23 and 7.24. Not every source figure was selected for print. Codex's 2026-10-21 journal records prior figure/content corrections and bounded visual review; no new complete source-image or print-legibility audit is claimed by this inventory refresh. Student final visual approval remains pending. See [00_INDEX.md](00_INDEX.md) for print links.

| Figure | Source slide | Source caption/topic | Source handling reference |
|---|---:|---|---|
| 7.1 | 3 | Hardware bath-tub reliability curve | Extract the original curve; preserve burn-in, useful-life, wear-out labels and axes. |
| 7.2 | 4 | Software reliability curve | Extract original; retain its failure-rate/time meaning and distinguish it from hardware wear-out. |
| 7.3 | 15 | Mean-value and failure-intensity functions | Extract original plot; inspect axes/legend visually. |
| 7.4 | 18 | Input space | Extract original; preserve the input-space shape/regions. |
| 7.5 | 19 | Portion of operational profile | Extract original; preserve probability/run-type labels. |
| 7.6 | 20 | Operational profile | Extract original; read the branch probabilities and paths directly from pixels. |
| 7.7 | 21 | Reliability and failure intensity | Extract original paired trend; inspect scale and direction. |
| 7.8 | 26 | Software quality attributes | Extract original hierarchy/attribute diagram. |
| 7.9 | 30 | Software quality factors | Extract original quality-factor grouping. |
| 7.10 | 35 | McCall quality model | Extract original three-area/factor/criteria model; preserve every label. |
| 7.11 | 40 | Boehm software quality model | Extract original hierarchy; do not substitute a modern quality model. |
| 7.12 | 46 | ISO 9126 quality model | Extract original characteristics/subcharacteristics; check every small label at print scale. |
| 7.13 | 47 | Failure-intensity function for the basic model | Extract the source equation/graphic only after visual formula transcription. |
| 7.14 | 48 | Relationship between failure intensity and mean failures for the basic model | Extract original; verify notation against the scan. |
| 7.15 | 50 | Failure intensity versus execution time, basic model | Extract curve and axes. |
| 7.16 | 51 | Additional failures needed to reach an objective | Extract original objective/curve labels. |
| 7.17 | 52 | Basic-model derived quantities | Inspect slide image; caption is incomplete in the text layer. |
| 7.18 | 59 | Logarithmic Poisson model relationship | Inspect image for full caption, axes, and formula. |
| 7.19 | 60 | Logarithmic Poisson model relationship | Inspect image; text layer omits the plotted variables. |
| 7.20 | 76 | Instantaneous calendar-time/execution-time ratio | Extract original; preserve resource assumptions and axes. |
| 7.21 | 77 | Calendar-time/execution-time ratio under different resources | Extract original; check legend and curve labels. |
| 7.22 | 90 | Jelinski–Moranda relation between time and failure intensity | Extract original; verify variables and interval notation. |
| 7.23 | 94 | CMM maturity levels | Extract original model graphic. |
| 7.24 | 96 | Five CMM levels | Extract original; keep level names and ordering exact. |

## Diagram handling rules for this chapter

- Fixed quality-model hierarchies, CMM level diagrams, and source curves should be extracted from the source rather than recreated from memory.
- A new clean vector is allowed only if the source image cannot print legibly or the question requires a marked-up variant. Keep the unmodified source image beside any reconstruction.
- Any reconstructed graph needs an equation/data/axis checklist and a pixel-size visual review. Do not treat a successful render or OCR as semantic verification.
- Several equations and captions are malformed by the slide PDF text layer. The slide image and scanned-book page image control their transcription.
- Extraction and printable embedding have been performed for the 13 selected assets listed above. Q7.V02 uses Fig. 7.4 as input-state probabilities, Q7.V03 uses Fig. 7.5 as a probability portion rather than a tree, and Q7.V07 uses Figs. 7.13/7.18 with λ-versus-μ axes. Do not reintroduce the superseded figure interpretations from an early coverage snapshot.
