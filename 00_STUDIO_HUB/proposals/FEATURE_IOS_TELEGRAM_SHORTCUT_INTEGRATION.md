# Feature Proposal: iOS Telegram File Ingestion via Apple Shortcuts Deep-Link

> **Status:** ON HOLD (Deferred per student instruction; to be activated if requested by colleagues or supervisor).  
> **Platform:** iOS 16+ (Safari PWA + Apple Shortcuts App).  
> **Target App:** MSCQuiz (Master Studio).  

---

## 1. Problem Statement
Due to Apple WebKit sandbox restrictions on iOS, PWAs cannot register file handlers directly in the OS to open `.json` files when tapped inside Telegram or WhatsApp.

## 2. Proposed Technical Solution (Off-Tracks)
1. **Apple Shortcut Action ("Open in MSCQuiz"):**
   - Receives any shared file from iOS Share Sheet.
   - Base64-encodes the file content.
   - Opens URL: `https://<domain>/quiz#data=<base64_encoded_quiz>`.
2. **PWA Ingestion Engine (Already Implemented in `quiz.js`):**
   - `quiz.js` listens to `window.location.hash`.
   - On `#data=...`, it decodes the payload, normalizes to Canonical Schema v2, persists into `QuizVault` (IndexedDB), and opens the quiz immediately.
3. **Distribution:**
   - A single iCloud Shortcut link shared in Telegram. Students tap once to install the shortcut, then use "Share -> Open in MSCQuiz" forever.
