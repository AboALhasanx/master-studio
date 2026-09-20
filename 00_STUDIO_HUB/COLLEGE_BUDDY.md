---
title: "College Buddy: Academic Events & Interactive Deadlines Ledger"
type: "interactive-buddy-ledger"
last_updated: "2026-09-20"
version: "1.2.0"
---

# College Buddy: Academic Event & Deadline Ledger

> **Behavioral Rule for All Agents:**
> 1. At session start, check upcoming dates. If $\le 3$ days remain, proactively alert and offer targeted drills.
> 2. If an event date has passed and status is still `UPCOMING`, ask the student how it went.
> 3. Update status to `COMPLETED`, `POSTPONED`, or `CANCELED` based on **student report only**.
> 4. **Only record events the student actually reports.** Never invent a date from a syllabus.

---

## 1. Active Events & Upcoming Deadlines

| ID | Target Date | Subject | Event / Topic | Professor | Status | Urgency | Buddy Notes / Action |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **EVT-04** | **next week** (weekly Cyber slot = Sunday 08:30; **no new exact date given**) | 01_Cyber_Security | **Daily quiz POSTPONED** by Dr. Huda (student report 2026-09-20) | Dr. Huda Lafta Majeed | **POSTPONED** | HIGH (prep still needed) | **Covers TWO booklets (ملزمتين):** (1) material we already have / Week 01 notes — OK; (2) **a second booklet she has NOT given them yet** — not Week 02 as previously assumed. She taught ~40 min from it today via Data Show; mostly memorization; student took paper notes + **voice recording**. He will hand the booklet over when he has it. Possible **external reading passage** in the exam (doctor mentioned). |
| **EVT-05** | after Unit 1 from **both** sources (no date stated); **research-paper talk = next week** | 02_English_Language | **Exam after Unit 1** (Q Skills + Headway) + **research-paper talk on Data Show** | Dr. Haidar Akab Alwan | UPCOMING | MEDIUM | **Clarifications 2026-09-20 (student):** Paper topic = **any Computer Science field**; want **strong academic terminology**. English lecture today = **nothing new substantial**; Q Skills already at **vocab p.17**. **Headway = important for grammar**; student flags **Language Focus** section (e.g. near p.8+) as likely important — treat Headway grammar/Language Focus as exam-core, not optional. Possible **external passage**. Exam after Unit 1 both sources. |
| **EVT-04b** | when delivered | 01_Cyber_Security | **Huda booklet 2** | Dr. Huda | **WAITING** | — | Student: still **not given**; only **random notes** until booklet drops. Then **we read/understand it together**. No notes build until materials arrive. |
| **EVT-06** | answered 2026-09-19 | 03_Data_Mining | Standing question: data type of a **URL** | Dr. Ahmed Shakir | **ANSWERED** | — | **Nominal.** Still may be asked in class Monday. |

> **Correction — 2026-09-18:** EVT-01 and EVT-02 were agent-inferred and are INVALID. Do not invent deadlines.

### Weekly Rhythm (student-confirmed)

Usually **no hard dated deadlines**. Pattern: this week’s lecture → light follow-up next lecture. Reminders stay soft unless the student states a date.

---

## 2. Student Lecture Log — 2026-09-20 (Sunday)

### 01_Cyber_Security — Dr. Huda
- Daily quiz **postponed to next week**.
- Quiz will cover **two booklets**.
- Booklet 1 = the one they already have (our Week 01 PDF/notes still valid).
- Booklet 2 = **not yet given to students**; **not** the “Week 02” people assumed. Today she taught **~40 minutes** from it on the Data Show; student describes it as **mostly memorization (تافهة/حفظ)**.
- Student followed on Data Show only (she didn’t have the booklet with her).
- He wrote **paper notes** and **recorded her voice** — will provide booklet/details later when available.
- Doctor mentioned a possible **external passage** on the exam.
- Exam timing tied to finishing relevant material — exact new quiz date **not stated** beyond “next week”.

### 02_English_Language — Dr. Haidar
- **Q Skills:** reached **Vocabulary Skill — page 17**.
- **Headway:** reached **page 8**; last work = upper **tenses/sentences table** + **Practice 1** exercise.
- Possible **external passage** in the exam.
- Exam **after Unit 1** from **both** sources (Q Skills + Headway).
- **Next week:** research-paper presentation/talk on Data Show — formal paper reading + speaking + **academic vocabulary questions**.

---

## 3. Event History & Learning Archive

| ID | Date | Subject | Event | Status | Student Feedback & Outcome | Impact on Learning Model |
|:---|:---|:---|:---|:---|:---|:---|
| **EVT-03** | 2026-09-16 | 04_Advanced_SE | Surprise pop quiz | COMPLETED | Aced Brooks distinctions | Brooks mastered |
| **EVT-01** | never | 04_Advanced_SE | Agent-inferred viva | INVALID | Student confirmed fake | None |
| **EVT-02** | never | 02_English | Agent-inferred submission | INVALID | Student confirmed fake | None |
| **EVT-04** | 2026-09-20 | 01_Cyber_Security | Daily quiz (original date) | **POSTPONED** | Student: postponed to next week; two booklets; booklet 2 not delivered yet; ~40 min taught; paper notes + audio | Keep Week 01 notes; **wait for booklet 2** before building new notes; no invented exam date |

---

## 4. Status Definitions
- `UPCOMING`: scheduled in the future (student-reported).
- `POSTPONED`: moved by the professor; original date void.
- `COMPLETED`: event happened.
- `CANCELED`: not happening.
- `ANSWERED`: standing question resolved.
- `INVALID`: was never real (agent error).

---

*Updated 2026-09-20 by Koko from Abu Al-Hasan's post-lecture report.*
