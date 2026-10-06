# Design Spec: Master Studio Silent Motion-Graphics Video Tutorial Engine

- **Author:** Master Studio Engineering & Architecture
- **Date:** 2026-10-06
- **Status:** Approved by Student / In Design Review
- **Target Deliverable:** Advanced Software Engineering — Chapter 4: Software Project Planning (30-Minute Silent Master Motion Tutorial)

---

## 1. Problem Statement & Motivation

Master Studio provides high-yield academic study notes, Word documents, and publication-grade vector PDFs. However, complex procedural and quantitative engineering topics—such as Albrecht's Function Point Analysis (FPA), Value Adjustment Factor (VAF) calculations, and COCOMO Rayleigh curves—benefit significantly from continuous, step-by-step visual motion graphics.

Standard generative AI video tools suffer from severe mathematical hallucinations, unreadable formula renders, and proprietary cloud lock-in. 

This subsystem introduces a **code-driven, deterministic, 100% local motion-graphics video engine** using HyperFrames (HTML5/CSS/GSAP rendered via Headless Chromium and FFmpeg). To support focused study, the output format is **pure silent motion graphics** (no human voiceover in background), using kinetic typography, structured visual hierarchy, animated boundary diagrams, and bilingual English-Arabic explanatory callouts.

---

## 2. Core Constraints & Governance Invariants

1. **Zero Human Voiceover:** The video is 100% silent motion. Visual choreography and dynamic subtitles provide complete pedagogical direction.
2. **Deterministic & Local (Zero-SaaS):** Rendered entirely on local CPU/GPU using Playwright/Headless Chromium and local FFmpeg 9.0.2. No third-party video APIs or subscriptions.
3. **WCAG AA Contrast & Layout Verification:** Every scene must pass `npx hyperframes check` with 0 lint errors, 0 runtime exceptions, 0 layout faults, and 100% WCAG AA contrast compliance.
4. **Autonomous Single-Command Execution:** The student never manages render flags. The Python orchestrator handles individual scene builds, validation gates, caching, and stream stitching.

---

## 3. Subsystem Architecture

### 3.1. Modular Segmented Pipeline with Lossless Stitching
A 30-minute video ($54,000$ frames at 30 fps) cannot be reliably rendered as a single monolithic browser timeline without risk of memory exhaustion. The pipeline decomposes the 30-minute curriculum into **9 discrete scenes** ($2.5\text{--}4.0$ minutes each).

```
01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/
└── Ch04_Project_Planning_Video/
    ├── scenes/
    │   ├── 01_planning_and_loc/         (index.html · ~3.0 min)
    │   ├── 02_fpa_foundations/          (index.html · ~3.0 min)
    │   ├── 03_data_functions_ilf_eif/   (index.html · ~3.5 min)
    │   ├── 04_tx_functions_ei_eo_eq/    (index.html · ~3.5 min)
    │   ├── 05_complexity_and_ufp/       (index.html · ~3.5 min)
    │   ├── 06_gsc_and_vaf/              (index.html · ~3.5 min)
    │   ├── 07_worked_numerical_exam/    (index.html · ~4.0 min)
    │   ├── 08_cocomo_and_putnam/        (index.html · ~3.0 min)
    │   └── 09_exam_traps_summary/       (index.html · ~2.5 min)
    ├── rendered_parts/                  (cached per-scene MP4s)
    │   ├── scene_01.mp4
    │   └── ...
    └── ASE_Ch04_Planning_Master_Tutorial.mp4  (final 30-min stitched MP4)
```

### 3.2. Lossless Concat Engine (`video_builder.py`)
The tool `90_Shared_Toolbox/tools/video_builder.py` automates the render cycle:
1. Scans `scenes/` directory in numerical order.
2. Checks hash/timestamp cache: if a scene's source HTML has not changed and its rendered MP4 exists, re-rendering is skipped.
3. Validates un-rendered scenes via `npx hyperframes check`.
4. Renders the scene to standard $1920 \times 1080$, 30 fps H.264 MP4.
5. Emits an FFmpeg concat manifest (`concat.txt`) and joins all segments via:
   ```bash
   ffmpeg -y -f concat -safe 0 -i concat.txt -c copy ASE_Ch04_Planning_Master_Tutorial.mp4
   ```
   *Execution time for stitching: $< 5$ seconds.*

---

## 4. Visual Language & Cognitive Pacing (Silent Mode)

### 4.1. Screen Layout ($1920 \times 1080$)
- **Top Header Bar (84px height):**
  - Left: Master Studio Badge + Subject Title (`Advanced Software Engineering — CS502`).
  - Center/Right: Current Scene Badge (`Scene X of 9: Title`) + Continuous gradient progress bar.
- **Main Stage Canvas (896px height):**
  - Kinetic chalkboards for step-by-step mathematical proofs.
  - Dashed and glowing system boundary diagrams with animated particle data packets for transaction flows.
  - Interactive incrementing metric counters ($0 \rightarrow \text{Value}$) for formula evaluations.
- **Director's Bilingual Bottom Strip (100px height):**
  - Synchronized bilingual text anchors: top line English technical explanation; bottom line RTL Arabic conceptual rationale.

### 4.2. Semantic Color Palette
- **Background:** Slate Dark (`#090d16` with `#151e33` radial gradient).
- **Inputs (`EI`):** Sky Blue (`#38bdf8`).
- **Outputs (`EO`):** Emerald Green (`#34d399`).
- **Inquiries (`EQ`):** Amber / Gold (`#f59e0b`).
- **Internal Logical Files (`ILF`):** Indigo / Violet (`#818cf8`).
- **External Interfaces (`EIF`):** Pink / Rose (`#f472b6`).
- **Text:** Crisp White (`#f8fafc`) and Muted Slate (`#94a3b8`).

### 4.3. Reading Pacing Rules
- Prose slides must hold for at least 1 second per 2.5 words (equivalent to 150 words per minute reading pace).
- Equations must anchor on screen for at least 6.0 seconds to allow cognitive processing.
- All entrance animations use smooth GSAP tweens (`power2.out`, stagger $0.1\text{--}0.2\text{s}$) with clean opacity transitions between stages.

---

## 5. Pedagogical Scene Syllabus (Chapter 4: Planning)

1. **Scene 01: The Planning Crisis & LOC Dilemma (~180s):**
   - Project planning triple constraint (Scope, Cost, Schedule).
   - Lines of Code (LOC) flaws: implementation dependent, late-stage only, ambiguous counts (18 vs 17 vs 13 lines).
   - Conte's rigorous academic definition of LOC.
2. **Scene 02: Albrecht’s Function Point Foundations (~180s):**
   - 1979 Allan Albrecht (IBM) breakthrough.
   - Core principle: sizing software based on user-visible functions rather than programming language syntax.
   - Estimation directly from Software Requirements Specifications (SRS).
3. **Scene 03: Data Function Types (ILF & EIF) (~210s):**
   - System boundary definition.
   - Internal Logical Files (ILF): user-identifiable data maintained inside the system.
   - External Interface Files (EIF): files maintained by another system but referenced by ours.
4. **Scene 04: Transactional Function Types (EI, EO, EQ) (~210s):**
   - External Inputs (EI): data crossing boundary to update internal logic.
   - External Outputs (EO): derived calculations and reports crossing boundary outward.
   - External Inquiries (EQ): input-output query retrieval pairs without file state mutation.
5. **Scene 05: Complexity Multipliers & UFP Computation (~210s):**
   - Matrix of Low, Average, and High complexity weights ($3$ to $15$).
   - Mathematical formulation:
     $$UFP = \sum_{i=1}^5 \sum_{j=1}^3 W_{ij} \times Z_{ij}$$
6. **Scene 06: Value Adjustment Factor & The 14 GSCs (~210s):**
   - The 14 General System Characteristics ($F_1$ to $F_{14}$) with degrees of influence ($0$ to $5$).
   - Calculation of Technical Complexity Factor (TCF / VAF):
     $$VAF = 0.65 + 0.01 \times \sum_{i=1}^{14} F_i$$
7. **Scene 07: Comprehensive Exam Numerical Problem (~240s):**
   - Step-by-step exam problem walkthrough: given concrete counts of transactions and files with complexity ratings, calculating $UFP$, computing $VAF$ from GSC scores, and finding final adjusted $FP = UFP \times VAF$.
8. **Scene 08: Cost Estimation Models (COCOMO & Putnam) (~180s):**
   - Boehm’s Constructive Cost Model (COCOMO) modes: Organic, Semidetached, Embedded.
   - Putnam's Software Equation and Rayleigh manpower distribution curves over project schedule phases.
9. **Scene 09: Master Summary & Dr. Ali Fahim Exam Traps (~150s):**
   - Rapid-fire comparison matrix.
   - Professor's key exam traps: language independence, early estimation, conversion from FP to LOC backfiring across languages.

---

## 6. Verification & Quality Gates

Each scene and the final master video must satisfy:
1. `npx hyperframes check` on all 9 scenes: Exit Code 0.
2. `video_builder.py` render run: all 9 `.mp4` chunks generated.
3. Lossless stitch: `ASE_Ch04_Planning_Master_Tutorial.mp4` verified with `ffprobe`:
   - Duration: $\approx 1,800\text{ seconds}$ ($30\text{ minutes} \pm 10\text{s}$).
   - Resolution: $1920 \times 1080$, 30 fps, H.264.
   - 0 missing frames or decode errors.
4. Snapshot extraction: 1 verification frame extracted per scene into `snapshots/`.
