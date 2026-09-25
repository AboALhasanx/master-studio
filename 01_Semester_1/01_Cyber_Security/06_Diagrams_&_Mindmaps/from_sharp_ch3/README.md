# Figures extracted from the original textbook

> **Source:** Sharp, R., *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Undergraduate Topics in Computer Science, Springer, Cham, 2023, **Chapter 3 "Risk", pp. 37–56**. DOI: [10.1007/978-3-031-41463-3_3](https://doi.org/10.1007/978-3-031-41463-3_3)
> **Why these are here:** the Cyber Week 02 Risk booklet delivered by the doctor is a Word conversion with **zero embedded images** — every figure is referenced in the text but absent from the file. These are the actual figures, cropped from the book's own typeset PDF.

## The six figures — these are the ones in use

All are **tightly cropped to the figure itself**, at 320 DPI, with axis labels and diagonal arrows intact. **None is a whole-page render.**

| File | Printed page | Figure | Contents |
|:---|:---:|:---:|:---|
| `fig3_1_shark.png` | 38 | 3.1 | The white shark (the *threat*) behind the cage whose welding fault is the *vulnerability* |
| `fig3_2_risk_matrix.png` | 38 | 3.2 | The **risk matrix** — Frequency × Consequences, colour-coded, diagonal arrow labelled Risk |
| `fig3_3_residual.png` | 39 | 3.3 | The **residual risk matrix** — Countermeasures (axis reversed) × Risk, diagonal arrow labelled Residual risk |
| `fig3_9_risk_example.png` | 52 | 3.9 | The three worked threats placed in the risk matrix |
| `fig3_10_resid_example.png` | 53 | 3.10 | The same threats after countermeasures, in the residual risk matrix |
| `fig3_11_pdca.png` | 54 | 3.11 | The PDCA cycle |

These six are embedded directly in `../../03_Study_Notes/W02_Risks_Basic.pdf`.

## `_page_renders_superseded/` — local only, not published

Seven **whole-page renders** from the first extraction pass — the complete printed pages, not crops. They are **not used anywhere** and are kept **on this machine only**, as a fallback in case a figure ever needs re-cropping at different bounds.

**They are deliberately excluded from the repository** (see `.gitignore`): they are entire pages of a copyrighted book, and this repository is public. Only the six **cropped figures** above are tracked, and each carries the citation and — for the shark photograph — the required CC-BY attribution.

## Attribution and licence

- **The white shark photograph (Fig. 3.1)** is credited in the book itself as: *"Photo of white shark by Terry Goss, Wikimedia Commons file `White_shark.jpg` under license **CC-BY 2.5 Generic** [21]"*. **Attribution is required** wherever this image is reused — keep the credit line with the file.
- **The matrices and diagrams (Figs. 3.2, 3.3, 3.9, 3.10, 3.11)** are simple vector graphics from the chapter. Reproduce them only with the citation above attached.
- **The book itself is not stored in this repository.** Only the specific figures needed to fill the booklet's gap are kept here, for study use, with the full citation.

## How to cite these

> [Sharp, R., "Risk", in *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Undergraduate Topics in Computer Science, Springer, Cham, 2023, pp. 37–56](https://doi.org/10.1007/978-3-031-41463-3_3)

## Re-cropping, if ever needed

The crop rectangles used are recorded in `90_Shared_Toolbox/tools/build_cyber_w02_booklet.py` (PDF-point boxes per page index). The page renders in `_page_renders_superseded/` can be re-cropped directly without needing the book again.

*Extracted 2026-09-23 for the Cyber Security Week 02 study pack.*
