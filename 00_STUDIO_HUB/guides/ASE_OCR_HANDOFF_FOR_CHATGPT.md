# Technical Review Request — OCR strategy for digitising a scanned software-engineering textbook

> **How to use:** paste this entire file into ChatGPT and ask it to answer the decision questions in §9.
> **Role requested:** critical technical reviewer. Please challenge assumptions, flag anything unverifiable, and give a single recommended path — not a menu.
> **Prepared:** 2026-11-11. All numbers below were checked against primary sources on that date; vendor benchmarks are labelled as such.

---

## 0. What I need from you

We digitised a scanned textbook into a searchable PDF, but the OCR layer is weak. We are about to rebuild it as **clean editable text** (Markdown master → DOCX), chapter by chapter. Before committing to an OCR engine we want an independent opinion on:

1. whether our chosen accuracy target and measurement method are sound;
2. which engine to use given our hardware and budget;
3. whether any of our assumptions are wrong.

Please be blunt. If the plan is bad, say so.

---

## 1. Objective and hard constraints

| | |
|:---|:---|
| **Goal** | A clean, editable, verbatim-faithful **text** version of the book, one chapter at a time. Markdown is the master; DOCX is an export. |
| **Why** | Searchability, quotation accuracy for exam prep, and as a base for the student's own derivative study packs. |
| **Legal** | The book is in copyright (2008). The vault's GitHub repo is **public**. A full-text reproduction must stay in the gitignored `02_Raw_Materials/**` and must never be committed. Only original study packs may be shared publicly. |
| **Privacy / cost** | The student values tools that work offline and cost nothing; cloud APIs are acceptable only if clearly worth it. |
| **Workflow** | Zero-CLI: the student gives natural-language instructions, the agent runs every tool. Chapter-by-chapter review is expected, not one-shot bulk conversion. |
| **Epistemic** | No fabricated citations, quotes, or accuracy figures. Claims that are not sourced must be labelled `[Foundational Knowledge / Standard Concept]`. |

---

## 2. The book

**K. K. Aggarwal & Yogesh Singh, _Software Engineering_, 3rd ed., New Age International (P) Ltd., New Delhi, 2008.**
- ISBN-13 **978-81-224-2360-0**, ISBN-10 8122423604
- **528 printed pages**, 10 chapters, paperback only (no official ebook/Kindle/Google Play edition anywhere)
- The 3rd edition shipped with a **CD of chapter-wise PowerPoint slides** — this is the origin of the 1094-page slide deck that circulates online
- Chapter map (printed pages): Ch1 Introduction 1–20 · Ch2 SDLC Models 21–39 · Ch3 Requirements 40–138 · Ch4 Project Planning 139–202 · Ch5 Design 203–249 · Ch6 Metrics 250–307 · Ch7 Reliability 308–364 · Ch8 Testing 365–458 · Ch9 Maintenance 459–490 · Ch10 Software Certification 493–497 · Answers 498–500

**2nd edition (2005):** 480 printed pages, ISBN 8122416381, 9 chapters, no Certification chapter.

---

## 3. What we already have (full inventory)

| Artefact | Provenance | State |
|:---|:---|:---|
| `02_Raw_Materials/Aggarwal_SE_3rdEd_COMPLETE/Aggarwal_SE_3rdEd_COMPLETE_Ch1-10_OCR.pdf` | merge of the five sources below | **452 PDF pages, 209.6 MB, 910,590 searchable chars, 11 bookmarks** |
| Ch1–Ch6 (PDF pp.1–327, printed 1–307) | Internet Archive item `software-engineering-3rd-ed-yogesh-singh-k-k-aggarwal-1-removed` (open-source collection) | **240 DPI** page images + Tesseract 5.3 OCR text layer |
| Ch7–Ch10 (PDF pp.328–452, printed 308–497) | chapter scans from GitHub `BhaskarAnand-05/DTU_5th_Sem_Books` | **202–231 DPI** images + a locally built **RapidOCR** invisible text layer |
| `AliFahim_Software_Engineering.pdf` | original 2-up photocopy | 256 PDF pages, **~95–108 DPI per printed page**, no text layer. The **only** source containing Answers pp.498–500 |
| `Aggarwal_SE_3rdEd_Answers_printed498-500_OCR.pdf` | 2 pages extracted from AliFahim pp.255–256 | 386 KB, 4,124 OCR chars. **Letters unreliable** — see §5 |
| `02_Raw_Materials/Aggarwal_SE_3rdEd_InternetArchive/Aggarwal_SE_3rdEd_Ch1-6_OCR_fulltext.txt` | IA `_djvu.txt` | 682 KB plain text |
| Internet Archive `softwareengineer0000agga` | full **2nd edition**, 494 pp, 360 DPI, ISBN 8122416381 | lending only (`access-restricted-item: true`); readable PDF/epub/djvu.txt are private, only an encrypted PDF + LCP epub are public |
| Google Books volume `dx2C9Zkez5YC` | full **2nd edition** text index | **snippet view**: TOC + full-text search-inside, but page images return "image not available". No download |
| `mait4us.weebly.com` / `tecse.weebly.com` | publisher's official slide deck, split into 10 born-digital chapter PDFs | 1094 pages total, clean native text, ~7 MB — **slides, not book prose** |
| `repo.darmajaya.ac.id/4672/` | 2nd-edition partial | 18 MB free download but only **103 pages**, no text layer |
| `_digitizer/digitize_chapter.py` | our pilot pipeline | extracts page blocks → strips running heads/folios → de-hyphenates → normalises bullets/quotes → anchors figure crops on `Fig. N.N:` captions → Markdown. Produced a clean 3-page Ch5 sample incl. a 200 DPI Fig. 5.1 crop |

**Page-map rule for Ch1–Ch6:** `PDF page = printed page + 20` (verified at Ch1 p.21←1, Ch4 p.159←139, Ch5 p.223←203, Ch6 p.270←250). Ch7 starts at merged PDF p.328.

---

## 4. Are the 2nd and 3rd editions different? (evidence, not assumption)

**Primary evidence — the publisher's own 3rd-edition blurb (Amazon.in ASIN B0B2MWGTJK), verbatim:**
> "The suggestions of students, teachers, researchers and practitioners have found a place in this edition. Since pedagogy of classroom delivery is fast changing and power point presentations have become a way of life. To help the teachers and students, chapterwise power point presentations have been prepared and a copy of CD is attached to this edition of the book. **A new chapter on software certification** ... has also been added."

**TOC comparison:** identical chapter names and order for Ch1–Ch9; chapter lengths essentially unchanged (Testing = 94 pp in both); cumulative page offset grows from +2 (Ch2) to +20 (Ch9). Total 480 → 528 pp. Only structural addition = Ch10.

**Empirical verbatim test** (Google Books `SearchWithinVolume2` on the 2nd ed vs `search_for` on our 3rd-ed PDF):

| Phrase | 2nd ed | 3rd ed | Offset |
|:---|:---|:---|:---|
| "Software design is more creative process than analysis" | PA193–194 | printed 203 | +10 |
| "Vitruvious recorded the following attributes" | PA197 | printed 206 | +9 |
| "Cohesion is a measure of the degree…" | PA202 | printed 211 | +9 |

Same wording, including the book's own "Vitruvious" misspelling. **Conclusion: Ch1–Ch9 prose is verbatim identical.** Therefore Google Books 2nd-ed snippets are usable as a **spelling/verification reference**, but NOT as a page-number source, NOT for Ch10, and NOT as proof that revised examples match.

---

## 5. The failure that triggered this review

We used **`rapidocr-onnxruntime`** (PP-OCRv4-era ONNX, CPU-first) because it needed no admin-level install. It was a convenience choice, not an accuracy choice.

Observed failures:
- On the Answers page, the answer letter **`(b)` is systematically read as `(6)`** — e.g. `5.1, (6)` instead of `5.1. (b)`.
- Figure-label regions produce junk (`á = , A`, `Cortificatlon`, `Sofware Reliability`).
- Running heads and folios leak into paragraph text.
- Hyphenated words split across text blocks (`specifi-` / `cations`).

**Two distinct root causes — please do not conflate them:**
1. **Engine age/quality** — fixable by choosing a modern engine.
2. **Source resolution** — the Answers pages come from a ~100 DPI, 2-up photocopy. Distinguishing `(b)` from `(6)` there is a signal-resolution problem. We assume no engine reaches 90% character accuracy on that specific page, and we plan to **transcribe it manually from the image** regardless of engine.

---

## 6. Modern OCR landscape — numbers verified from primary sources (2026-11-11)

### 6.1 `allenai/olmocr` README — olmOCR-Bench v0.4.0 (7,000+ test cases over 1,400 documents)

| System | Overall |
|---|---:|
| Chandra OCR 0.1.0* | 83.1±0.9 |
| Infinity-Parser 7B* | 82.5 |
| olmOCR v0.4.0 | 82.4±1.1 |
| PaddleOCR-VL* | 80.0±1.0 |
| Marker 1.10.1 | 76.1±1.1 |
| DeepSeek-OCR | 75.7±1.0 |
| MinerU 2.5.4 | 75.2±1.1 |
| Mistral OCR API | 72.0±1.1 |
| Nanonets-OCR2-3B | 69.5±1.1 |

`*` = reported by the model authors, not reproduced in-house. The "Base" column is 98.5–99.9 for all systems.

> **Critical caveat we want checked:** olmOCR-Bench scores are **pass/fail "facts"** (text presence/absence, reading order, table cell relationships, math rendering), **not CER/WER**. Its "Old scans" category uses historical typewritten Library of Congress letters and tests reading order — it is not a character-accuracy measurement. We have deliberately avoided claiming "no OCR exceeds 50% on old scans". Is our reading correct?

### 6.2 Mistral OCR 2503 announcement (6 Mar 2025) — **vendor internal benchmark**, model now deprecated

| Model | Overall | Scanned | Tables |
|---|---:|---:|---:|
| Mistral OCR 2503 | 94.89 | **98.96** | 96.12 |
| Gemini-1.5-Pro-002 | 89.92 | 96.15 | 89.71 |
| Gemini-2.0-Flash-001 | 88.69 | 95.11 | 91.46 |
| Azure OCR | 89.52 | 94.65 | 89.52 |
| GPT-4o-2024-11-20 | 89.77 | 94.58 | 91.70 |
| Google Document AI | 83.42 | 92.77 | 78.16 |

Fuzzy-match-in-generation: Mistral 99.02, Azure 97.31, Gemini 2.0 Flash 96.53, Google Doc AI 95.88.

### 6.3 Mistral OCR 4 (23 Jun 2026) and OCR 4.1 (16 Jul 2026) — current generation

- OCR 4: **85.20 OlmOCRBench** (top overall among systems tested), **93.07 OmniDocBench**, ~**72% human-preference win rate** over every leading OCR / document-AI system tested (600+ documents, 12+ languages, blind annotators), 170 languages, 2000 pages/min on one node in the earlier generation.
- Returns **bounding boxes, typed block classification, and inline / block-level confidence scores**, plus Markdown-structured text.
- Pricing: **$4 / 1,000 pages**, **$2 / 1,000 with Batch API**; Document AI $5 / 1,000.
- OCR 4.1 is the latest (`mistral-ocr-4-1`), same $4/1,000 pages, $5/1,000 annotated pages, paragraph-level bbox.
- Mistral explicitly warns its own aggregate benchmarks are **directional** and recommends evaluating on one's own documents.

### 6.4 PaddleOCR (open source, CPU-capable)

- **PaddleOCR-VL-1.6 (0.9B)**: **96.3% on OmniDocBench v1.6**; v1.5 = 94.5%; 109–111 languages. CPU is listed as a supported backend at project level, but no VLM-specific CPU-only guarantee is documented.
- **PP-OCRv5** (May 2025): CPU-capable, single model for Chinese/English/Japanese/etc.; internal weighted accuracy rose **53.0% → 80.1%** vs v4 on a hard multi-scene evaluation set (not clean English book prose).
- **olmOCR / Chandra / Infinity-Parser**: 7B-class VLMs; olmOCR requires a recent NVIDIA GPU with **≥12 GB VRAM** and 30 GB disk.

---

## 7. Environment

| | |
|:---|:---|
| OS | Windows (Git Bash shell) |
| GPU | **Intel HD Graphics 520 integrated only — no NVIDIA GPU** (`nvidia-smi` absent) |
| RAM | 12 GB |
| Python | system Python 3.12; isolated venv `C:\Users\gokoq\.workbuddy-ai\binaries\python\envs\ocr` with `rapidocr-onnxruntime`, `pymupdf`, `numpy`, `opencv` |
| Install policy | Prefer pip / venv; **no admin-level system install**, no Tesseract binary currently installed |
| Network | Some search engines and many sites block automated clients; a real Thorium browser driven by Playwright is available when needed |
| Cost estimate | 452 pages × $4/1,000 = **≈ $1.81** for the whole book via Mistral OCR 4.1; ≈ $0.90 with Batch |

---

## 8. Proposed plan (please critique)

1. **Define accuracy as WER/CER**, computed with `jiwer`, against an explicit ground truth — not a vendor score.
2. **Ground truth sources:**
   - (a) Google Books 2nd-ed `SearchWithinVolume2` snippets, valid because Ch1–Ch9 prose is verbatim identical (§4);
   - (b) a manually transcribed **10-page sample** from the 240 DPI renders, covering clean prose, a figure page, a table page, and the Answers page.
3. **Benchmark three engines on the same 10 pages:** current RapidOCR (baseline), PP-OCRv5 local CPU, Mistral OCR 4.1 cloud.
4. **Acceptance gate:** WER ≤ 10% on clean-prose pages → adopt the engine. Report figure/table/Answers pages separately; never auto-accept them.
5. **Use confidence scores** (Mistral OCR 4.1) to flag low-confidence regions for human review instead of proofreading all 452 pages.
6. **Pipeline per chapter:** OCR → silent de-hyphenation, running-head/folio removal, bullet/quote normalisation → figure crops anchored on `Fig. N.N:` captions → tables and formulas rebuilt manually → Markdown → DOCX.
7. **Answer key (pp.498–500): manual transcription from the page image only.** Non-negotiable.
8. **All outputs stay local / gitignored.** No full-text reproduction is committed to the public repo.

---

## 9. Decision questions for the reviewer

1. Is **WER ≤ 10% on clean prose, measured with `jiwer`**, the right acceptance gate for "90%+ accuracy"? If not, what metric and threshold would you set, and how should we handle the fact that our ground truth (Google Books snippets) is itself truncated and fuzzy-matched?
2. Is our conclusion that **Ch1–Ch9 prose is verbatim identical between the 2nd and 3rd editions** adequately supported by the three phrase checks, or do we need a larger sample before using 2nd-ed snippets as ground truth?
3. Given **no GPU, 12 GB RAM, no admin install, and a strong preference for free/offline tools**, which single engine should we adopt: PP-OCRv5 (local CPU), PaddleOCR-VL 0.9B (CPU, probably very slow), or Mistral OCR 4.1 (~$2)? Please give one recommendation with the reasoning and the trade-off you would accept.
4. Are we wrong to treat the **Answers page** as unfixable by OCR? Is there a modern engine or a prompting/VLM technique that reliably distinguishes `(b)` from `(6)` on a ~100 DPI 2-up photocopy — or is manual transcription genuinely the only defensible option?
5. For the **Markdown → DOCX** rebuild of a textbook, what is the most reliable way to preserve figures (we have clean 200–240 DPI crops), tables, and in-line formulas without hand-editing 452 pages? Any toolchain we have missed (Marker, MinerU, Docling, Surya, Chandra, GOT-OCR2.0, olmOCR via a remote endpoint)?
6. Are there **legal or practical risks** in uploading a complete in-copyright textbook to a third-party OCR API that we should weigh more heavily than the ~$2 cost and accuracy gain?
7. What is the **most likely way this plan fails** that we have not considered?

---

## 10. Non-negotiables

- The answer key is human-transcribed, never OCR-trusted.
- No accuracy claim is published without a measurement on our own pages.
- No invented citations, page numbers, or quotes.
- The full reconstructed text never enters the public GitHub repo.
- Chapter-by-chapter: quality over speed.

---

## Appendix A — reproducible checks / endpoints

```
# Google Books full-text search inside the 2nd edition
https://books.google.com/books?jscmd=SearchWithinVolume2&q=<URL-encoded phrase>&vid=dx2C9Zkez5YC
# Returns JSON-ish HTML containing "number_of_results", "page_id", "snippet_text", word boxes.
# Rate-limits to ~1 request before HTTP 429; pace >=12 s or rotate books.google.iq / .com / .co.uk.

# Internet Archive metadata
https://archive.org/metadata/softwareengineer0000agga            # full 2nd ed, lending
https://archive.org/metadata/software-engineering-3rd-ed-yogesh-singh-k-k-aggarwal-1-removed

# Slide deck (born-digital, 10 chapters, 1094 pp)
https://mait4us.weebly.com/software-engineering.html

# 2nd-ed partial (103 pp, free)
http://repo.darmajaya.ac.id/4672/
```

**Verified dead ends (do not re-hunt):** no official ebook on Amazon (.com/.in/.sg/.ca/.au/.uk), AbeBooks, Sapna, Mybooksfactory, Google Play Books, Perlego; Google Books 3rd-ed record `ISh5PwAACAAJ` is metadata-only; Anna's Archive `.is` returns zero results even for control queries; pdfcoffee is Cloudflare-gated; `vaccination.gov.ng`, `sanandres.uep.edu.py`, `dad.norgate.lv`, `jacksonms.gov`, `topperlearning.motion.ac.in` are SEO-spam PDF shells; `UNIT 2.pdf` and `Unit-3 ( Software Design ).pdf` in the DTU repo are handwritten student notes; the only fork of that repo has an identical file list.
