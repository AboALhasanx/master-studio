# QA harnesses (agent-side)

Browser/tablet checks that need a running app. They are **not** part of the
deployed site; run them from a shell.

| file | what it does | how to run |
|---|---|---|
| `tablet_sweep.js` | the full button sweep on the **real tablet** over CDP: 47 queued steps (home bar, drawer, notifications, quiz, results, saved, stats, league, account), each `setup → act → assert → restore`, printing PASS/FAIL per step and the console errors seen | `adb forward tcp:9222 localabstract:chrome_devtools_remote` then `node tablet_sweep.js` |
| `tablet_results_flow.js` | the quiz → results → review → retry-wrong → retry-quiz → home flow, on the tablet | same |
| `web_lang_bar.js` | the ع/EN switch is in the bar for quiz/results/saved, hidden on home, and gone from the drawer (desktop/headless is fine) | `PORTAL_URL=https://mcq-portal-jade.vercel.app node web_lang_bar.js` |
| `web_content_structure.js` | subject/chapter/card structure: six subjects, one chip per chapter, exactly two cards per chapter, KaTeX renders | same |
| `tablet_offline_sweep.js` | the same sweep with Wi-Fi **off**: the shell must come from the cache, every screen must open, a quiz must answer and explain, and the league/account actions must say they need the network instead of going silent | `adb shell svc wifi disable` then `node tablet_offline_sweep.js` |
| `tablet_new_badge.js` | the «جديد» badge is stateful: a fresh chapter shows it, opening the quiz clears it at once, the notification leaves the sheet and the visit is remembered after a reload | `node tablet_new_badge.js` |
| `portal_db_clean.py` | sweeps the QA guests out of the content portal (keeps the student's account and the real league row) | `python portal_db_clean.py` (dry run), `APPLY=1 python portal_db_clean.py` |

Notes
- The tablet harnesses drive Chrome over CDP (`tcp:9222`); wake the screen first
  and re-run `adb forward` after the device sleeps.
- A step that clicks a header button right after an action may hit a toast that
  covers the bar: the harness clears `.portal-toast` before those clicks.
- Android Chrome can answer the league share button with the **native share
  sheet** (a system dialog CDP cannot see); the harness dismisses it with
  `adb shell input keyevent KEYCODE_BACK`.
- `portal_db_clean.py` needs the Supabase service key, which is fetched with the
  MCP OAuth token in `%USERPROFILE%\.local\share\opencode\mcp-auth.json`. If the
  Management API answers **401 Invalid access token**, the token expired —
  refresh it with `https://api.supabase.com/v1/oauth/token`
  (`grant_type=refresh_token` + the `clientInfo` credentials in that file) and
  write the new `accessToken` / `refreshToken` / `expiresAt` back.
- Any browser run creates a guest account in the portal; run the cleaner after.
