# Tool Radar — Candidates

Last reviewed: 2026-10-27

These are leads for evaluation, not endorsements. Feature and performance descriptions below are project-reported unless explicitly marked as locally tested.

| Project | Status / added | Why it may help Master Studio | Main checks before adoption |
|---|---|---|---|
| [Baidu Unlimited-OCR 2](https://github.com/baidu/Unlimited-OCR) | **First candidate · evaluate later · added 2026-10-27** | Parses all pages in one request with cross-page context; targets very long documents, page structure, tables, and figures. Could help with long scanned or layout-heavy course sources. | Released 2026-10-27, so treat project claims as unverified. README's tested setup uses an NVIDIA A800 80 GB; SGLang requires a customized wheel. Check Arabic and formula accuracy, setup cost, and model-weight terms. Compare with the existing local reader before considering any integration. |
| [MinerU](https://github.com/opendatalab/MinerU) | **Candidate · high relevance · added 2026-10-27** | Converts PDFs, images, and Office documents to Markdown/JSON; advertises OCR for 109 languages, layout recovery, formulas, and cross-page table merging. The documented pipeline backend supports CPU use, making it a practical comparison candidate. | Check Arabic and math on our sources, Windows setup, model downloads/offline mode, CPU time, and the project's custom license. Keep its online services out of the test path. |
| [Docling](https://github.com/docling-project/docling) | **Candidate · high relevance · added 2026-10-27** | Local document conversion with selectable OCR engines, layout/table extraction, Markdown/JSON output, and page-range controls. Could complement the current PDF reader for difficult pages and office files. | Test OCR engine and language configuration for Arabic; compare complex two-column reading order, formula handling, tables, CPU requirements, and offline model setup. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) / PaddleOCR-VL | **Candidate · OCR-focused · added 2026-10-27** | Offers OCR and document parsing for PDFs/images, structured Markdown/JSON, and a multilingual model family; the project describes Arabic support. Could be useful when scanned pages or multilingual OCR are the main failure. | Verify the exact model's Arabic quality and license, local installation/runtime on this Windows host, model size, and whether it adds value over bundled RapidOCR. Do not rely on project benchmark claims without a local comparison. |

## First comparison set

Use the current [`pdf_reader.py`](../../90_Shared_Toolbox/tools/pdf_reader.py) as the baseline. Choose a small set of already-authorized, non-sensitive source pages that includes:

1. a clean digital PDF page (control case);
2. a scanned page with English body text and a formula;
3. an Arabic or bilingual page;
4. a two-column page with a figure or table;
5. a long document containing a table or section that continues across pages.

Score text fidelity, reading order, table structure, formulas, Arabic, figure references, page alignment, runtime, setup effort, and offline operation. Verify critical text visually against the source. Do not upload course or student files to hosted demos.
