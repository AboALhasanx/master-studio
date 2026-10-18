# Portal Cloud Sync — Dropbox setup (one time, ~2 minutes, free)

The student portal syncs each student's own data (saved questions, history,
best scores) into **their own Dropbox** (app folder `mcq-portal.json`).
No server, no database, no fees. The app uses OAuth2 PKCE (no secret needed).

## What the student (vault owner) must do in Dropbox

1. Open https://www.dropbox.com/developers/apps and sign in.
2. **Create app** → Choose **Scoped access** → Choose **App folder** access
   (the app only ever sees its own folder, never the whole Dropbox).
3. Name it `mcq-portal` → **Create app**.
4. On the app's **Settings** tab:
   - Copy the **App key** (a short string like `abc123xyz`).
   - Under **OAuth 2 > Redirect URIs**, add BOTH lines (exact, with `https/http`):
     - `https://mcq-portal-jade.vercel.app/`
     - `http://127.0.0.1:8080/`  (local testing only)
     - Click **Add** after each.
   - Under **Permissions** tab, check:
     - `account_info.read`
     - `files.content.read`
     - `files.content.write`
     - Click **Submit**.
5. Send the **App key** to the agent (chat is fine — it is a *public*
   identifier, not a secret; it ships inside the web app).

## What the agent does with the key

1. Put it in `js/dropbox-config.js` in the portal repo:
   `window.PORTAL_DROPBOX_KEY = '<KEY>';` (the file is committed —
   the key is a *public* identifier by design, safe to ship).
2. Run the cloud E2E test (`tests` below), then `vercel --prod`.
3. Each student taps **القائمة → الحساب → ربط Dropbox** once; sync is automatic after that.

## How sync works (for agents)

- Code: `mcq-portal/js/cloud.js` (`window.PortalAccount`... actually `window.PortalCloud`).
- Auth: OAuth2 PKCE, tokens in `localStorage.portal_cloud_tokens` (never exported).
- File: app-folder `/mcq-portal.json` = `{saved, history, bests, updatedAt}`.
- First link: if cloud empty (or older than local sync) → upload local;
  else → download cloud and replace local views.
- Every local change (save/answer/best) → debounced upload (2 s) when online.
- Offline: works fully on device cache; auto-pushes on `online` event.
- History cap 200, bests keyed `portal_best_*`, all wrapped in try/catch.

## Tests

- Local (no key): menu account row shows unconfigured hint; no crashes.
- With key (needs the real redirect + login in Thorium):
  `node C:\Windows\Temp\opencode\shot\qa_cloud.js` (created when the key arrives).
