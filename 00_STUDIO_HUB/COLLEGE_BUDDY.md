---
title: "College Buddy: Academic Events & Interactive Deadlines Ledger"
type: "interactive-buddy-ledger"
last_updated: "2026-09-17"
version: "1.0.0"
---

# College Buddy: Academic Event & Deadline Ledger

> **Role:** The student's interactive college companion ledger.
> **Behavioral Rule for All Agents:**
> 1. At session start, check upcoming dates in this ledger. If $\le 3$ days remain, proactively alert the student and offer targeted study drills.
> 2. If an event date has passed and the status is still `UPCOMING`, **immediately ask the student during check-in**:
>    *"Hey! [Event] with [Professor] was scheduled for [Date]. How did it go? Did it end well, did the doctor postpone it, or was it canceled?"*
> 3. Based on the student's answer, update the status to `COMPLETED`, `POSTPONED`, or `CANCELED`, record their reflection, and update `LEARNER_MODEL.md` (mastered concepts or review queue).

---

## 1. Active Events & Upcoming Deadlines

| ID | Target Date | Subject | Event / Topic | Professor | Status | Urgency | Buddy Notes / Action |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **EVT-01** | 2026-09-21 | 04_Advanced_Software_Eng | Lecture 01 Oral Defense Drill (Patriot Kinematics) | Dr. Ali Fahim | UPCOMING | HIGH | Drill 24-bit fixed-point clock drift math ($0.3433\text{s} \rightarrow 687\text{m}$) |
| **EVT-02** | 2026-09-20 | 02_English_Language | Unit 01 Grammar & Tenses Submission | Dr. Haidar Akab | UPCOMING | MEDIUM | Verify Headway SB pp.6–15 tense matrix and avoid contractions |

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
| *Archive initialized* | - | - | - | - | Initial system baseline | System tracking active |

---

## 4. Status Definitions
- `UPCOMING`: Event is scheduled in the future.
- `DUE_TODAY`: Event is today! High alert.
- `NEEDS_CHECKIN`: Target date has passed, awaiting student debrief on outcome.
- `COMPLETED`: Done! Student reflection logged.
- `POSTPONED`: Doctor moved the date; target date updated.
- `CANCELED`: Class or deadline called off.
