# Cyber Security Ch4–Ch5 candidate source audit

Date: 2026-10-27  
Status: working candidate only; active quiz banks and portal content are unchanged.

## Source evidence and limits

- `W04_Cryptography.pdf` is an 18-page source titled **Week 3: Cryptography Basics** even though it is used as Chapter 4. The Chapter 4 TriLayer note explicitly says its source is AI-generated and that no instructor-marked copy was found. The rendered pages confirm the title/numbering mismatch and the section sequence; the PDF has no visible instructor marks in the pages reviewed.
- `W05_Network_Security.pdf` is 29 pages and combines four large topics: protocol vulnerabilities; firewalls/proxies/VPNs; IDS/IPS; and segmentation/defense in depth. No marked instructor copy was found. The “Exam Summary” and emphasis tables in the TriLayer note are authored study guidance, not professor annotations.
- Visual spot-checks of the raw PDFs covered W04 page 1 and W05 pages 1, 14, and 25. They confirm the W04 numbering mismatch and show W05’s introduction, formal risk/governance material, and segmentation models. No handwritten professor marks were visible on these sampled pages; this is not evidence that every unseen page is unmarked.
- Consequently, Ch4/Ch5 questions are source-derived study coverage only. They must not be described as confirmed instructor priorities. The cleaner Ch1/2/3/6 banks informed question style (named lists once, a small number of applications, concise recall/understanding questions), not Ch4/5 exam scope.
- The Chapter 4 candidate already corrects the source's AES-128 brute-force time conversion: `2^127 / 10^18` seconds is approximately `5.4e12` years.
- Deeper review found that W04's integrated PKI model labels `P_trust` as a success probability, then multiplies `(1 - P_trust)` into overall security. The candidate's three questions testing this inconsistent model were removed. A symmetric-key revocation item was also rewritten to ask why replacement is difficult, rather than giving the remedy as the answer.
- W05 contains multiple highly specific mathematical extensions. Some repeat the same residual-risk idea across proxy, VPN, IDS/IPS, and segmentation sections, while others assume simplified probability/adoption models. The candidate now keeps the distinct core formulas and drops redundant model restatements, standards-number recall, and the over-asserted BGP adoption example.
- The source's SolarWinds/VPN example conflates the Orion supply-chain compromise with later VPN use. The old candidate question was removed. CISA describes the trojanized Orion update as initial access and documents later VPN activity in follow-on analysis; see [CISA incident analysis](https://www.cisa.gov/sites/default/files/publications/Supply_Chain_Compromise_Detecting_APT_Activity_from_known_TTPs.pdf).

## Candidate cleanup completed

- Chapter 4: 9 topic banks, **118 questions** (down from 180 at the start of this cleanup). Removed repeated TLS handshake details, duplicated hash/signature applications, repeated formulas, duplicate cases, and the inconsistent integrated PKI probability model; retained distinct RSA/ECC, hash, PKI, TLS, email-security, and economic/quantum concepts.
- Chapter 5: 17 topic banks, **221 questions** (down from 346). Removed repeated residual-risk formulations, redundant DNS/RFC recall, unsupported or over-asserted BGP probability examples, repeated proxy/VPN/IDS reliability models, and the multi-question Markov expansion. The five-layer defense-in-depth list remains one question, with two distinct layer examples retained.
- English `options_en` is synchronized with `options` for all candidate items. Question IDs were renumbered after removals. Strict answer-key balancing was rerun where pruning changed the distribution.
- Work remains isolated in `scratch/ch04_ch05_candidate/`; no active bank was replaced, retired, synced, pulled, released, or deployed.

## Gate status after cleanup

- `quiz_balancer.py --check --strict`: passed all 26 candidate banks after the latest balancing run. Candidate-wide concept IDs are unique; answer/correct indexes and `options`/`options_en` are aligned.
- Schema v2/v3 and dry-run gates: passed in candidate preflight for Chapters 4 and 5. Handout-reference scan is zero for both chapters.
- Added read-only `90_Shared_Toolbox/tools/quiz_quality_gate.py` and wired it into the Chapter 4/5 candidate preflight, the general Cyber preflight, the bank protocol, and the authoring skill/runbook. It checks chapter-scoped concept/stem duplication, duplicate choices, answer/index alignment, bilingual field completeness, option-array parity, near-duplicate stems, repeated formulas, explanations, and bilingual answer shape. Functional smoke checks confirmed chapter-scoped concept IDs do not collide, duplicate choices fail, and formula alternatives are not collapsed into false duplicates.
- Chapter 4 candidate preflight passes all current gates (9 banks / 118 questions); the new gate reports zero structural errors and zero shape failures. Its three near-duplicate warnings were reviewed: DES/AES descriptions, the two complementary hybrid roles, and RSA/ECC equivalence items are related but distinct.
- **Chapter 5 is not ready for publication:** current preflight fails English unique-longest answer shape (`109/221`) and the new bilingual shape gate. The new gate reports 0 structural errors, 109/221 English and 91/221 Arabic correct answers uniquely longest, 6 English and 107 Arabic spread violations, plus 1 English and 91 Arabic key-to-distractor-average ratio violations. Psychometric, schema, handout-reference, and dry-run gates pass. Continue question-level editing before proposing any active-bank replacement.
- Calibration against previously cleaned active chapters found zero structural errors in Chapters 1–3 and 6. The shape gate passes Chapters 6, but flags Arabic option spread in Ch1 (7 questions) and Ch2 (8), plus one key-length ratio in Ch3. Those active banks were inspected read-only and left untouched; the findings matter only if those chapters are reopened for editing or release.
- Final decision (2026-10-27): **do not publish Ch4/Ch5 together**. Ch4 passes, but Ch5 fails mandatory option-shape gates (`109/221` EN unique-longest plus bilingual spread/ratio defects). `portal_content.py status` could not read the remote state because the sandbox denied socket access (`WinError 10013`); the local dry-run passed. No active banks or portal state were changed.

## Next actions

1. Continue Chapter 5 English/Arabic option-shape edits while preserving meaning and answer/correct alignment.
2. Review remaining source-derived cases and mathematical claims for accuracy; treat generated models as study coverage, not professor emphasis.
3. Re-run the full candidate preflight. Keep all work isolated until the student explicitly chooses any later replacement/publish scope.
