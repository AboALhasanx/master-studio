# Tasks 3-5 Brief: Complete WebUI Frontend Suite (HTML, CSS, JS)

**Files:**
- Modify/Create: `91_Dashboard/templates/quiz.html`
- Create: `91_Dashboard/static/quiz.css`
- Create: `91_Dashboard/static/quiz.js`

**Global Constraints:**
- **Zero Emoji Icons**: Use Lucide SVG icons exclusively (`data-lucide="..."` and `lucide.createIcons()`). Strict prohibition of emoji characters for UI controls.
- **Theming**: Dark mode default (`#0B1C2E`), Light mode (`#F8FAFC`), System theme via CSS variables.
- **Mobile First Touch Targets**: Buttons $\ge 48\text{px}$ touch target height, smooth drawer transitions.
- **Metacognitive Reflection**: 4 quick-select chips (`Misread Question`, `Calculation Slip`, `Terminology Mix-up`, `Concept Gap`) + 1-line note field for wrong answers.
- **Lucky Guess / WOW Toggle**: Checkbox on correct answers to flag flukes.
- **Dwell Timer**: Tracks per-question dwell time (seconds) and session total duration.
- **Idempotent Sync**: `crypto.randomUUID()` attached to telemetry payload sent to `POST /api/quiz/submit`.

**Detailed Requirements:**
1. `91_Dashboard/templates/quiz.html`:
   - Top Bar: Back button, Quiz title/subtitle, Bookmarks toggle (`bookmark`), Analytics toggle (`bar-chart-2`), Theme toggle (`sun`/`moon`).
   - Progress Bar + Timer Row: Progress fill %, Question X of Y, Dwell timer (`clock` icon + `00:15`), Total timer (`04:30`).
   - Active Question View:
     - Question text (with BiDi support).
     - Option buttons (A, B, C, D) with selected state.
     - Bookmark question toggle (`bookmark` icon).
   - Bottom Sticky Nav: Previous button, Next/Finish button.
   - Result & Review View:
     - Score percentage, PASS/FAIL badge, Correct/Wrong/Avg Dwell stats.
     - Action buttons: "Try Again" (`refresh-cw`), "Send to Master Studio" (`send`).
     - Review list: Wrong answers show reflection chips; Correct answers show "Lucky Guess / WOW" toggle.
   - Drawers:
     - Bookmarks drawer (slide-over / bottom-sheet).
     - Analytics drawer (shows active review queue, passing thresholds).
     - Drawer overlay for closing on tap outside.

2. `91_Dashboard/static/quiz.css`:
   - Theme variables for `[data-theme="dark"]` and `[data-theme="light"]`.
   - Card elevations, rounded borders (`10px`-`16px`), high-contrast typography.
   - Drawer slide animation from right (or bottom on mobile).

3. `91_Dashboard/static/quiz.js`:
   - State management: `questions`, `currentIndex`, `answers`, `dwellTimes`, `reflections`, `luckyGuesses`, `bookmarks`.
   - Auto-fetch `/api/quiz/<subject_id>/<quiz_id>` when `subject_id` and `quiz_id` are provided in `body[data-subject]` and `body[data-quiz]`.
   - Timer loop running at 1s interval.
   - "Send to Master Studio" sends full telemetry payload to `/api/quiz/submit`. On success, reveals green checkmark banner.
   - Bookmarks sync with `/api/quiz/bookmarks`.

**Deliverable:**
Complete and verify `quiz.html`, `quiz.css`, and `quiz.js`. Write report to `.superpowers/sdd/2026-09-19-interactive-web-quiz-system/tasks-3-5-report.md`.
