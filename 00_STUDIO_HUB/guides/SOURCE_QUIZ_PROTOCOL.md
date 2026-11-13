# Source-faithful MCQs — explicitly approved alternate track

## Authority and scope

The student approved this separate track on 2026-11-13, after reviewing the ASE
source-versus-practice audit. It preserves original source questions for recognition
practice; it does **not** replace or relax the existing conceptual/practice banks.
The student approved the original-source sections of the ASE chapter packs, excluding
the authored additions, in chapter-specific batches of 10–15 questions.

This is a narrow exception to `QUIZ_BANK_PROTOCOL.md`,
`AGENT_HANDOFF_QUIZ_BANKS.md` and the pipeline skill's ordinary authoring rules.
It applies only to banks explicitly marked `bank_kind: "source"` that pass the
source-specific gate and original-text manifest checks. Missing kind means ordinary
practice; an unknown kind is invalid. Do not bypass checks by simply adding a flag.

## What may differ from practice banks

- Preserve the original English stem and four options; do not pad distractors,
  remove negative wording, replace “all/none of the above”, or turn a formula into
  prose to satisfy a shape metric.
- Preserve option **and question** order. Positional references such as “both A
  and C” must retain their meaning. Saved questions, retries and review sessions
  retain the source marker and must never permute these options.
- Original key distribution, length spread, formula choices and source-level
  repeated concepts are reported, not “repaired” by rewriting original items.
  Source IDs must still be unique and source concept IDs use a separate namespace.
- Keep the existing practice banks and their strict shape, padding and authoring
  gates unchanged. The exception does not authorize their retirement or rewriting.

## What remains mandatory

- Canonical v2 in the vault, generated v3 in the app; no hand-written live payload.
- Exactly four nonempty bilingual options, consistent `options`/`options_en`,
  valid answer/index mapping, unique item IDs, parseable math, and nonempty
  explanations. Every translated option must correspond to the same original.
- Provenance for each source item: stable original ID, actual reference, and
  original English text/options in a separate source manifest with file anchors.
  The source gate must detect changes against that manifest.
- `source.key_status` is `confirmed`, `derived` or `disputed`. “Confirmed” requires
  an actually checked key; a reasoned solution is “derived”, not a publisher key.
  A disputed/unresolved item must have null `answer` and `correct`, with a
  nonempty bilingual ambiguity note. It remains visible for study but is excluded
  from scores, wrong-only retry and review telemetry; it never receives a guessed
  key. A disputed item carrying a graded key blocks publication. Source banks
  are excluded from competitive VS pools.
- Keep corrections in the separate bilingual `source.note` and explanation.
  Never silently “fix” original wording or pass unreviewed OCR off as verified.
  A literal interpretation, intended interpretation and publisher key can differ;
  document that distinction before resolving an item.
- Arabic UI remains MSA, RTL, with clean English technical terms. Source mode
  starts in English; the translation control remains available.
- Bank IDs follow `Quiz_ChNN_SNN_Source_MCQs`; batch numbering is independent of
  existing topic numbering. Book chapter numbers do not change.

## Validation and release boundary

Run structural v2/v3 validation and `quiz_source_gate.py`, including manifest
fidelity and answer-status checks. Source exceptions never waive these gates.
For publication readiness, use `quiz_source_gate.py <bank-or-directory> --check-publish`;
without that flag a structural-only check is not a publication approval.
The bank's relative `source_manifest` path points inside its own bank directory.
The separate manifest locks every original stem/choice, reviewed key/status,
reference and original-file anchor/hash. A missing manifest item or changed
original file fails the publication gate.
Ordinary banks continue through `quiz_balancer.py --check --strict` and the
shape/padding gates. A source bank must never be passed through an option balancer
that rewrites or permutes the original choices.

Capture an independently reviewed staging ledger with `review_source_manifest.py
--items <prepared.json> --publisher-keys <verified-keys.json> --output
<bank-directory>/source_manifests/ASE_Source_MCQs.json --reviewed`, then import via
`build_source_banks.py --items <prepared.json> --manifest <reviewed-manifest.json>
--output-dir <bank-directory> --dry-run` before the write pass. The importer
validates every batch first, preserves chapter-wide identities, refuses unknown
keys and different existing banks, and never derives a manifest from the banks
it is supposed to check. Transcript answer annotations may be removed only as
an explicit, recorded normalization; never show answer-marking diamonds as choices.

Metadata must survive conversion, loading, cached/offline banks, saved snapshots,
retry and review. The catalogue distinguishes **أسئلة المصدر** from **تدريب الفهم**.
The app can derive the track from the loaded bank payload when an older live
manifest does not carry the optional kind metadata; no remote migration is implied.

Run local source-flow checks and the portal's full CI before declaring readiness.
The student approved local implementation only: no sync, pull, hide, retire,
database migration, remote publication or deployment without separate approval.
Update the generated `QUIZ_BANK_STATE.md` through its tool when content state is
ready; never hand-copy bank-state totals into this protocol.
