# Portal Cloud Sync — Telegram account (WebApp + CloudStorage)

Students already live on Telegram: when they open the portal **from the
course bot**, Telegram itself identifies them (name + @username, no password,
no extra tap) and their data syncs into **their own per-user Telegram cloud**.
No server, no database, no OAuth round-trips, no keys in the bundle.
Outside Telegram the portal keeps working as a device-local guest app.

## What the owner does (bot already exists: `@cs_mscbot`, ~2 minutes)

The course bot already exists — the same `@cs_mscbot` used by the study
gateway (its token stays in the vault `.env`; the portal never needs it).
Only two BotFather steps remain, done once from your Telegram account
(you own the bot):

1. Open **@BotFather** → send `/mybots` → choose `@cs_mscbot` →
   **Menu Button** (may appear as "Bot Settings → Menu Button"):
   - Choose **"Configure menu button"**, send the portal URL:
     `https://mcq-portal-jade.vercel.app/`
     and a short button label, e.g. `افتح الكوزات`.
2. (Recommended) Still in @BotFather, send `/setdomain` → choose
   `@cs_mscbot` → send `mcq-portal-jade.vercel.app` (links the domain).
3. Done — no keys to copy anywhere: the portal reads the public bot
   username from its own `js/tg-config.js` (already set to `cs_mscbot`).

Announce the bot link to the students. Opening the portal **from the
bot's menu button inside Telegram** is what signs them in — nothing else
to do.

## How it works (for agents)

- Code: `mcq-portal/js/cloud.js` (`window.PortalCloud`,
  `js/tg-config.js` holds only the public bot username).
- Identity: `window.Telegram.WebApp.initDataUnsafe.user` (present only when
  opened inside Telegram). `linked()` = a Telegram user is present.
- Storage: `WebApp.CloudStorage`, keys `mcq_idx` + `mcq_p0..mcq_pN`
  (~3800-char chunks; CloudStorage values cap at 4096 chars).
- Bundle shape = the local backup shape
  (`{saved, history, bests, updatedAt}`), so local JSON export/import
  stays 100% compatible.
- First link: cloud missing/older → upload local; cloud newer → download
  and re-render. Every local change debounces a 2 s auto-upload when online.
- Offline: everything keeps working on the device cache; push retries on
  the `online` event.
- Menu account row: guest outside Telegram (with a hint to open from the
  bot) vs Telegram name + sync time when linked.
- Fingerprint note: phones already gate Telegram + saved logins behind
  biometrics, so daily entry is effectively one tap + fingerprint with no
  extra code on our side.

## Tests (agent-run, no real bot needed)

`node C:\Windows\Temp\opencode\shot\qa_cloud.js` injects a **fake**
`window.Telegram.WebApp` (user + in-memory CloudStorage) *before* page
scripts and asserts the full loop: linked identity shown in menu,
local→cloud upload on quiz finish, wipe-local → reload → data restored
from cloud, out-of-quota/offline paths degrade silently.
When the real bot exists, repeat once from inside Telegram on a phone
(open from the bot menu, answer a quiz, reopen on a second device).
