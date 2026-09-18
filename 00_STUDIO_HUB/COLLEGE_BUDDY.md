---
title: "College Buddy: Academic Events & Interactive Deadlines Ledger"
type: "interactive-buddy-ledger"
last_updated: "2026-09-18"
version: "1.1.0"
---

# College Buddy: Academic Event & Deadline Ledger

> **Role:** The student's interactive college companion ledger.
> **Behavioral Rule for All Agents:**
> 1. At session start, check upcoming dates in this ledger. If $\le 3$ days remain, proactively alert the student and offer targeted study drills.
> 2. If an event date has passed and the status is still `UPCOMING`, **immediately ask the student during check-in**:
>    *"Hey! [Event] with [Professor] was scheduled for [Date]. How did it go? Did it end well, did the doctor postpone it, or was it canceled?"*
> 3. Based on the student's answer, update the status to `COMPLETED`, `POSTPONED`, or `CANCELED`, record their reflection, and update `LEARNER_MODEL.md` (mastered concepts or review queue).
> 4. **Only record events the student actually reports.** Never invent a date, and never infer a deadline from a syllabus or from "what usually happens". Agent-inferred events presented as real deadlines caused a false alarm on 2026-09-18 — see §3.

---

## 1. Active Events & Upcoming Deadlines

| ID | Target Date | Subject | Event / Topic | Professor | Status | Urgency | Buddy Notes / Action |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **EVT-04** | 2026-09-20 (Sun) | 01_Cyber_Security | **Daily quiz (امتحان يومي)** — Week 01 material | Dr. Huda Lafta Majeed | UPCOMING | **HIGH** | Sunday lecture, 08:30–10:30. Revise Week 01 Cyber Security content. |
| **EVT-05** | 2026-09-27 (Sun) | 02_English_Language | **Presentation (~5 min)** — write a short research-style paper on any computer/software field in English, using field terminology; present it on the Data Show and explain the terms | Dr. Haidar Akab Alwan | UPCOMING | LOW | Purpose: the professor wants to show the class how research papers are written. Student says it is *not* high-stakes. |
| **EVT-06** | open | 03_Data_Mining | **Standing question** from Dr. Ahmed Shakir: Week 02 *data representation & preparation* (preprocessing before data mining), specifically **"what is the data type of a URL?"** | Dr. Ahmed Shakir Abd Al-Rida | OPEN | MEDIUM | Raised in the previous lecture. Needs an answer. |

> **Correction — 2026-09-18, confirmed by the student.** The earlier entries `EVT-01` ("Lecture 01 Oral Defense Drill", 2026-09-21) and `EVT-02` ("Unit 01 Grammar & Tenses Submission", 2026-09-20) were **inferred by an agent and are NOT real scheduled events**. The student confirmed no such dated events exist. Both have been moved to §3 Event History as `INVALID`. **Do not present agent-inferred events to the student as deadlines.**

### Weekly Rhythm (student-confirmed)

There are usually **no formal dated deadlines**. The real pattern is:

> **The lecture taken this week → the next lecture carries a light follow-up task on it** — a small assignment, or a question he is expected to be able to answer in class.

So reminders should be kept as **soft prep notes**, never as hard deadlines, unless the student himself states a date.

---

## 2. Interaction & Lifecycle Protocol

```
         [Professor Announces Date in Lecture]
                          │
                          ▼
            [Student mentions in Chat]
                          │
                          ▼
             [Agent adds to Table above]
                          │
      ┌───────────────────┴───────────────────┐
      ▼                                       ▼
[Approaching: <= 3 Days]              [Date Reached / Passed]
  Agent alerts in boot:                 Agent debriefs:
  "Alert: Dr. Ali's viva                "How did Dr. Ali's quiz go?
   drill is in 3 days!"                  Did it end well or moved?"
      │                                       │
      │                               ┌───────┴───────┐
      │                               ▼               ▼
      │                         [Completed]     [Postponed]
      ▼                               │               │
[Study Rehearsal]                     ▼               ▼
                              Update Learner     Shift Date
                              Model Mastery      Forward
```

---

## 3. Event History & Learning Archive

| ID | Date | Subject | Event | Status | Student Feedback & Outcome | Impact on Learning Model |
| **EVT-03** | 2026-09-16 | 04_Advanced_Software_Eng | Surprise Pop Quiz | COMPLETED | Aced the Brooks complexity distinctions | Added Brooks essential complexity to mastered concepts |
| **EVT-01** | *never scheduled* | 04_Advanced_Software_Eng | "Lecture 01 Oral Defense Drill" | **INVALID** | Student confirmed 2026-09-18: no such event exists — agent-inferred | None. No viva was scheduled. |
| **EVT-02** | *never scheduled* | 02_English_Language | "Unit 01 Grammar & Tenses Submission" | **INVALID** | Student confirmed 2026-09-18: no such event exists — agent-inferred | None. No submission was scheduled. |
| *Archive initialized* | - | - | - | - | Initial system baseline | System tracking active |

---

## 4. Status Definitions
- `UPCOMING`: Event is scheduled in the future.
- `DUE_TODAY`: Event is today! High alert.
- `NEEDS_CHECKIN`: Target date has passed, awaiting student debrief on outcome.
- `COMPLETED`: Done! Student reflection logged.
- `POSTPONED`: Doctor moved the date; target date updated.
- `CANCELED`: Class or deadline called off.
