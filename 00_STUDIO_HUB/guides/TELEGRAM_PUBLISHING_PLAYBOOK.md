# Telegram Publishing Playbook — catalog cards + chapters + booklets

> **Status:** ACTIVE — **model re-cut 2026-10-02**: files are published by the
> **spare human account** (so the student can edit them from his phone), while
> the **bot** keeps only the pinned card, the quiz buttons and conversation.
> **Group:** `Master-Studio FINAL` → `chat_id -1003710711332` (forum).
> **Authority:** conventions here are binding for `telegram/catalog.py`,
> `telegram/human.py`, `tools/tg.py`, `tools/tg_catalog.py`.
> Full session evidence: `00_STUDIO_HUB/sessions/2026-10-02.md`.

**TL;DR (عربي):** الاحتياطي ينشر الكارت (placeholder) → الجابترات (بالأسماء
العربية عبر `--filename`) → يعدّل الكارت (`edit_message`) → البوت يثبّت الكارت
(`pin`) → المعرّفات تُكتب في `catalog/*.json` → رسائل البوت القديمة تُحذف →
تحقق حيّ → pytest + bandit → commit + push.

## 0. Who publishes what (2026-10-02)

| Content | Publisher | Why |
|---|---|---|
| Booklets, chapters, memos, files | **spare account** (`human --verb sendfile`) | the student can edit/delete them from his own phone; a message can only be edited by its own sender |
| Pinned catalog card | **spare account** (posted), **bot** (pins it) | content is the student's; the pin is an admin action the bot holds |
| Quiz links | **bot** | inline URL buttons are bot-only in Telegram |
| Chat, replies | bot | — |

Both accounts are admins of the group (the spare is **anonymous**) and **both
can pin** (`can_pin_messages`): prefer `tg.py pin` (bot, Bot API), fall back to
the spare via MTProto when the Bot API socket is dropping — proven live when
`10054` refused `pinChatMessage` for card `190` and the spare's
`UpdatePinnedMessageRequest` pinned it instantly.

## 1. The Layout (live)

| Subject | Topic | Card (spare) | Chapters (spare) | Sources (spare) | Booklet |
|---|---|---|---|---|---|
| 01 أمن المعلومات | 84 | `181` | `182–185, 244, 246, 248–255` (14) | — | 61 pp / 1.01 MB |
| 02 إنجليزي | 85 | `187` | `188, 284` (2) | `285, 286` (2) | 72 pp / 29.07 MB |
| 03 تنقيب البيانات | 86 | `190` | `191–195, 283` (6) | `214–215` (2) | 122 pp / 1.49 MB |
| 04 هندسة برمجيات | 87 | `196` | `197–199, 272` (4 في الكارت؛ `273–278` منشورة بلا دمج) | `210–213` (4) | 459 pp / 2.26 MB |
| 05 حوسبة ناعمة | 88 | `201` | `202–203, 281` (3) | `216–220` (5) | 144 pp / 5.10 MB |
| 06 ذكاء اصطناعي | 89 | `205` | `206, 240, 282` (3) | `221–222` (2) | 76 pp / 1.42 MB |

Topic names: **`◆ <subject>` — no numeric prefix, no emoji**. The three
utility topics (`◇ الامتحانات والأسئلة` 90, `◇ التقدم والتحليلات` 91,
`◇ الأدوات` 92) were **closed then deleted 2026-10-02** and removed from
`structure.STRUCTURE` so a future `structure` run cannot recreate them. Their
registry keys stay seeded — but **unbound**: `registry.RETIRED_SUBJECTS` clears
any stale coordinates on every seeded load *and* `resolve()` refuses them, so
an old command fails with a clear *unbound* rather than posting into a topic
that no longer exists (the file still pointed at threads 90/91/92 until
2026-10-03 — the promise was documented four times and enforced nowhere).
Source of truth for ids: `00_STUDIO_HUB/telegram/catalog/*.json`.

The **Sources** column is the canonical course books, one post each, caption
`مصدر مادة : <source>` / `الطبعة: <edition>`: the 13 textbooks published into
topics 86–89 on 2026-10-02, plus the two English course books into topic 85 on
2026-10-09 (`285` New Headway Upper-Intermediate SB, `286` Q Skills 4 R&W SB) —
15 posts. Each catalog records its own under `references`
(`message_id` + source + edition), so the JSON is the inventory rather than a
chat scroll; the editions were read out of each PDF, never assumed.

## 2. The Ordering Recipe (spare-account model)

```
1. spare publishes the CARD as a placeholder (booklet file, chapters not yet
   listed) into the topic  -> card gets an id
2. spare publishes each CHAPTER with its final caption; the caption's
   "الفهرس : كتالوج المادة" carries the card link -> chapters get ids
3. spare edits the card (edit_message) with the full render (real chapter ids)
4. bot pins the card:  tg.py pin --subject <key> --message-id <card>
5. write the REAL ids into catalog/*.json (chapters + catalog_message_id)
6. delete the old bot messages (card + chapters)
7. verify live
```

**Why the placeholder pass:** the card's `【الأول】…` links need the chapter
ids, and the chapters' `الفهرس` link needs the card id — a cycle. Publishing
the card first breaks it, and one `edit_message` completes it (the same
two-pass idea the old `tg_catalog --push` used, now in the spare's hands).

**Caption rule:** the docs usually arrive already final; on a plain edit
Telethon drops text-url entities, so prefer **HTML** captions (`parse_mode="html"`)
where the source text is available, and re-assert the caption after any media
swap (an `editMessageMedia` wipes the caption).

## 3. File-Naming Budget: 62 bytes

Telegram slugifies attachment names past ~64 **bytes** (not chars). Safe
budget = **≤ 62 UTF-8 bytes**, enforced by
`test_every_attachment_filename_fits_telegrams_safe_byte_budget`:

* pattern: `<Arabic> - <English>.pdf`, **no numeric prefixes**
  (`test_no_attachment_filename_carries_a_numeric_prefix`);
* use the short head when the full name overflows: `هندسة برمجيات` (04),
  `حوسبة ناعمة` (05, full `الحوسبة الناعمة` = 65 B), `ذكاء اصطناعي` (06);
* chapter files: `<head> - الجابتر الاول.pdf` (note: filenames use `الاول`
  without hamza; the card table generated by `arabic_ordinal` uses `الأول`).

Office sources convert via `90_Shared_Toolbox/tools/office_to_pdf.py`.
**Engine order (2026-10-02):**

1. **Office COM (primary on Windows with Word/PowerPoint)** — Word:
   `doc.ExportAsFixedFormat(out, 17)`; PowerPoint: `pres.SaveAs(out, 32)`
   (`ppSaveAsPDF`; `ExportAsFixedFormat` breaks under late binding). This is the
   same engine as *File ▸ Export as PDF*, so the output matches Office exactly.
2. **Chromium (fallback)** — mammoth/python-pptx → HTML → print-to-PDF.

**Never `x2t`/LibreOffice.** The ONLYOFFICE `x2t` converter renders whole
documents in a single math font (Asana Math) — every chapter built with it is
visually wrecked *and* unextractable (proven 2026-10-02: DM chapters 155–159,
SC 161). Both engines carry a QA gate (`qa_pdf`) that fails any PDF whose pages
use only math/symbol fonts, have no spaces, or have no text — the exact failure
signature, pinned by `tests/test_office_to_pdf.py`.

**Office COM gotcha — `RPC_E_CALL_REJECTED` (0x80010001).** A hidden *modal*
dialog (classically "Word isn't your default program" after another converter
hijacked the `.docx` associations) makes every COM call after `Open` fail and
leaves zombie `WINWORD.EXE` processes. `BM_CLICK` does **not** reach Word's
custom buttons; **`WM_COMMAND` with the real control id does**
(`PostMessage(dlg, WM_COMMAND, (BN_CLICKED << 16) | cid, button_hwnd)`). The
converter wraps every COM call in `_com_busy_retry`, which dismisses any Office
dialog (tick "Don't show again" first, then No/OK) and retries. If a future
round sees mass `WINWORD.EXE` processes, that is the signature.

Merge with fitz. Booklet outputs live in the gitignored
`00_STUDIO_HUB/telegram/catalog/files/` (never commit publisher PDFs —
public repo).

## 4. Swapping the Attachment (`editMessageMedia`)

The gateway's edit path writes **text only** (`editMessageText`), so a card
whose booklet arrives after the card keeps its placeholder forever. Swap it
with `editMessageMedia` — same message id, pin and position preserved
(card 123: 830 B placeholder → 5.98 MB real; same for 125).

## 5. Edit vs. Delete: the 48-Hour Rule

* `editMessageText` has **no time limit** — proven live: message `26` edited
  3 days after creation. The 48 h window is `deleteMessage` only (+ business
  messages). So **in-place edit is the only replacement path** for old cards.
* A card goes silent only if: not sent by its own author, author demoted, lost
  `catalog_message_id`, or a poll. **Rule (2026-10-02 model): cards and
  chapters are published by the spare account — the bot never publishes
  content.** In-place edit therefore goes through
  `tg.py --live human --verb edit --chat <chat> --message-id <id> --text <html>`
  (2026-10-03), not the bot's `edit`: a message can only be edited by its own
  sender. The verb is gated, allowlisted and audited like every other human
  verb, and it deliberately does **not** spend the send budget — a card refresh
  must never be able to silence a real send. Before it existed the playbook
  promised `human --verb edit` while no such verb was in `HUMAN_VERBS`, so the
  migration had to reach for a raw Telethon script that bypassed the kill
  switch, the allowlist and the ledger.

## 6. Card Format (binding)

* Arabic subject name, no `01` prefix; doctor's title + name;
  `الجابتر` = chapter count; verbatim `● كل جابتر بملف :` then `【Ordinal】`,
  3 per row; chapter links carry the ordinals.
* Forbidden in card: `<blockquote expandable>`, `📂 المسار`, gateway footer,
  per-link icons, notes sections, any emoji, any URL outside its `<a>`.
* Chapter captions (house style): `● <subject>` /
  `● الجابتر <Ordinal>   ①` / `● <note>` / blank /
  `ملخص الجابتر : <a href=…>اضغط هنا</a>` (only when the subject has a
  summary file — links its message id; added 2026-10-05 for SC) / blank /
  `الفهرس : <a href=…>كتالوج المادة</a>`. No `DOWNLOAD` promo line.
  Summary posts themselves carry `● ملخص الجابتر <Ordinal>   ①` + the
  card link only — **never a slide range** (the student dropped ranges:
  "ما تحتاج").

## 7. Verification Gate (before any commit)

1. Live topic check — the **permanent tool**, not a temp script:
   `python 90_Shared_Toolbox/tools/tg_verify.py --live` → **`ALL CHECKS PASSED`**.
   Per subject it asserts: the card is the first content message and is pinned,
   names the subject + doctor, carries the verbatim chapter line and every
   ordinal, attaches the merged booklet, its links point at the published
   chapter files, shows no bare URL, every chapter and source post exists, and
   no display filename exceeds 62 bytes. It prints one line per check (a
   variable count — one per invariant plus one per chapter file), exits `1`
   with the failing labels, and refuses with exit `5` when `--live` is absent.
   Read-only by construction.
2. `pytest -q` green, `bandit -r 90_Shared_Toolbox/telegram`
   High 0, CI + CodeQL green after push.
3. **Audit-row vocabulary.** Bulk publishing goes through `tg.py human …` (one
   verb per invocation) so each row keeps the CLI's convention: `result="sent"`
   for a message that left the process and `detail="message_id=X file=Y"`. A
   one-off script calling `human.run()` directly must copy that rule
   (`cli._human_detail` + `SEND_VERBS`), or it writes rows the ledger cannot be
   filtered by — found 2026-10-03, where rows `210`–`222` read `ok` /
   `message_id=X <name>`; they were **left as written**, because an audit
   ledger is not rewritten.
4. Stale idempotency rows in `gateway.db` block re-sends of identical payloads
   (`status=duplicate`, no message) — drop rows whose `message_id` was deleted.
5. Push path: `git -c credential.helper= -c "credential.helper=!gh auth
   git-credential" push` after clearing `GITHUB_TOKEN`/`GH_TOKEN`; commit
   message via `-F` temp file (PowerShell here-strings break); never stage
   `.workbuddy-ai/memory/*`; PowerShell `>` writes UTF-16 — Arabic/HTML
   payloads go through temp `.py` files.

## 8. Tooling Map

| Task | Command |
|---|---|
| render / push / edit card | `tools/tg_catalog.py --push` (`--live` for network; dry-run flags `file_missing` and continues, live refuses without the booklet) |
| publish / pin card | `tools/tg.py <verb> --json --live --actor 5664798395 …` |
| **live verification gate** | `tools/tg_verify.py --live` — reads topics 84–89 as the spare and prints `ALL CHECKS PASSED` (see §7) |
| inbound Pull poll (proposals only) | `tools/tg.py bridge --live --limit 20` (see `telegram/bridge.py`) |
| urgent vs. restricted | `telegram/permissions.py` — `classify()`; restricted waits for private-chat `نعم`/`لا` |
| one-shot mention replies | `tools/tg.py interactive --live` (bounded; admin verbs become pending approvals) |
| spare human account (files, edits) | `tools/tg.py human --verb sendfile …` — the **only** publish path for content (`--file`, `--filename`, `--text`, `--thread`); `--verb edit --message-id … --text …` refreshes a message the spare owns (gated, allowlisted, audited; not send-budgeted). `whoami`/`chats`/`read`/`say`/`sendfile`/`edit`/`login` — there is **no** `delete`/`sendtext` verb |
| group layout + index | `structure` verb; registry `90_Shared_Toolbox/telegram/registry.json` (gitignored) |
