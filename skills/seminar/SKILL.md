---
name: seminar
description: "Presentation architect for academic seminars. Ingests notes or papers and outputs structured 10-slide Marp Markdown decks that compile locally to PDF."
---

# Master Studio Seminar Architect (`@seminar`)

Use this skill whenever the student needs to prepare a slide deck, seminar presentation, or conference talk for their Master's courses.

## Operating Principles

1. **Strict 10-Slide Academic Flow:**
   1. Title & Candidate Details
   2. Problem Statement & Motivation
   3. Industrial & Academic Context
   4. Core Technical Mechanism / Theoretical Formulation
   5. Architectural / Algorithmic Topology (Mermaid diagram)
   6. State of the Art (IEEE/ACM Literature Survey Matrix)
   7. Comparative Trade-off Analysis
   8. Technical Bottlenecks & Limitations
   9. Master's Thesis Trajectory & Open Research Problems
   10. Open Viva Defense Questions for the Doctor

2. **Zero Paid SaaS (Marp Engine):**
   * Output must be pure Markdown formatted for [Marp](https://marp.app).
   * Include standard Marp frontmatter (`marp: true`, `theme: gaia`, `paginate: true`).
   * Compile command:
     ```bash
     npx -y @marp-team/marp-cli "<path-to-slide>.md" -o "<path-to-slide>.pdf" --allow-local-files
     ```

3. **100% Formal Academic English:**
   * Slide decks are external deliverables and must be written strictly in professional English.
