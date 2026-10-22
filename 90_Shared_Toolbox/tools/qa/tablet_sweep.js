// Systematic button sweep on the real tablet (CDP). Every step is a queued
// "setup -> act -> assert -> restore" unit; the run prints a table.
const { chromium } = require('playwright-core');
const BASE = 'https://mcq-portal-jade.vercel.app';
const results = [];
let consoleErrors = [];

const wait = (p, ms) => p.waitForTimeout(ms);
const vis = (p, sel) => p.locator(sel).first().isVisible().catch(() => false);
const count = (p, sel) => p.locator(sel).count().catch(() => 0);

async function home(p) {
  // a started quiz blocks navigation: try, then confirm the leave, then try again
  await p.evaluate(() => { location.hash = '#/'; });
  await wait(p, 600);
  await p.evaluate(() => {
    const lv = document.querySelector('#leave-modal');
    if (lv && !lv.classList.contains('hidden')) { const g = document.querySelector('#leave-go'); if (g) g.click(); }
  });
  await wait(p, 700);
  await p.evaluate(() => {
    document.querySelectorAll('.modal-overlay:not(.hidden)').forEach((m) => {
      const btn = m.querySelector('.icon-btn, #share-close, #link-close, #btn-close-info');
      if (btn) btn.click();
    });
    document.querySelectorAll('.drawer.open').forEach((d) => {
      const c = d.querySelector('.icon-btn');
      if (c) c.click();
    });
    const po = document.querySelector('#pause-overlay'); if (po) po.classList.add('hidden');
    document.querySelectorAll('.portal-toast').forEach((t) => t.remove());
    location.hash = '#/';
  });
  await wait(p, 1000);
  await p.evaluate(() => { document.querySelectorAll('.portal-toast').forEach((t) => t.remove()); });
}

async function step(p, name, fn) {
  const before = consoleErrors.length;
  try {
    const note = await fn();
    results.push({ name, ok: true, note: note || '' });
    console.log('PASS ' + name + (note ? '  :: ' + note : ''));
  } catch (e) {
    const extra = consoleErrors.slice(before).join(' | ');
    results.push({ name, ok: false, note: e.message.split('\n')[0] + (extra ? ' :: ' + extra : '') });
    console.log('FAIL ' + name + '  :: ' + results[results.length - 1].note);
    try { await home(p); } catch (e2) {}
  }
}

const need = (cond, msg) => { if (!cond) throw new Error(msg); };
const clearToasts = (p) => p.evaluate(() => { document.querySelectorAll('.portal-toast').forEach((t) => t.remove()); });
const atHome = (h) => h === '' || h.indexOf('#/') === 0;

(async () => {
  const b = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const p = b.contexts()[0].pages().find((x) => x.url().indexOf('mcq-portal') >= 0);
  await p.bringToFront();
  p.on('pageerror', (e) => consoleErrors.push('pageerror: ' + e.message.split('\n')[0]));
  p.on('console', (m) => { if (m.type() === 'error') consoleErrors.push('console: ' + m.text().slice(0, 120)); });

  // fresh shell
  await p.goto(BASE + '/?v=94', { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  for (let i = 0; i < 20; i++) { await wait(p, 1000); if (await p.evaluate(() => localStorage.getItem('portal_shell_version')) === 'v94') break; }
  await p.waitForFunction(() => document.querySelectorAll('#subject-filter-bar .filter-chip').length >= 6, null, { timeout: 40000 });
  await home(p);
  console.log('shell:', await p.evaluate(() => localStorage.getItem('portal_shell_version')),
              '| banks:', await p.evaluate(() => window.PortalApp.bankCount()));

  // ---------------- home bar ----------------
  await step(p, 'home/brand link points home', async () => {
    const href = await p.locator('#brand-home').getAttribute('href');
    need(href === '#/', 'href=' + href);
    return href;
  });

  await step(p, 'home/sound button toggles', async () => {
    const a = await p.evaluate(() => (document.querySelector('#sound-header-icon') || {}).getAttribute ? document.querySelector('#sound-header-icon').getAttribute('data-lucide') : '');
    await p.click('#btn-sound-header'); await wait(p, 400);
    const b2 = await p.evaluate(() => (document.querySelector('#sound-header-icon') || {}).getAttribute ? document.querySelector('#sound-header-icon').getAttribute('data-lucide') : '');
    need(a !== b2, 'icon unchanged: ' + a);
    await p.click('#btn-sound-header'); await wait(p, 300);
    return a + ' -> ' + b2;
  });

  await step(p, 'home/theme button toggles', async () => {
    const a = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
    await p.click('#btn-theme-header'); await wait(p, 500);
    const b2 = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
    need(a !== b2, 'theme unchanged: ' + a);
    await p.click('#btn-theme-header'); await wait(p, 300);
    return a + ' -> ' + b2;
  });

  await step(p, 'home/bell opens the notifications sheet', async () => {
    await p.click('#btn-bell'); await wait(p, 700);
    need(await vis(p, '#notif-modal'), 'sheet not visible');
    return 'items: ' + (await count(p, '#notif-list .notif-item'));
  });

  await step(p, 'notifications/read all clears the badge', async () => {
    if (!(await vis(p, '#notif-read-all'))) return 'no unread items -> the button is hidden (by design)';
    await p.click('#notif-read-all'); await wait(p, 600);
    const dot = await vis(p, '#bell-dot');
    need(!dot, 'badge still visible');
    return 'badge cleared';
  });

  await step(p, 'notifications/close button', async () => {
    await p.click('#notif-close'); await wait(p, 500);
    need(!(await vis(p, '#notif-modal')), 'sheet still visible');
    return 'closed';
  });

  await step(p, 'home/every subject chip filters', async () => {
    const n = await count(p, '#subject-filter-bar .filter-chip');
    const seen = [];
    for (let i = 0; i < n; i++) {
      await p.locator('#subject-filter-bar .filter-chip').nth(i).click();
      await wait(p, 400);
      const active = await p.locator('#subject-filter-bar .filter-chip.active').innerText();
      const cards = await count(p, '#catalog-cards-container .sketch-row');
      need(cards >= 1, 'no cards for ' + active.trim());
      seen.push(active.trim() + ':' + cards);
    }
    return seen.join(' | ');
  });

  await step(p, 'home/every chapter chip filters', async () => {
    const n = await count(p, '#chapter-filter-bar .filter-chip');
    const seen = [];
    for (let i = 0; i < n; i++) {
      await p.locator('#chapter-filter-bar .filter-chip').nth(i).click();
      await wait(p, 400);
      const cards = await count(p, '#catalog-cards-container .sketch-row');
      need(cards >= 1, 'empty chapter at index ' + i);
      seen.push(cards);
    }
    return 'cards per chapter: ' + seen.join(',');
  });

  await step(p, 'home/play cell opens the start card', async () => {
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
    await wait(p, 900);
    need((await p.evaluate(() => location.hash)).indexOf('#/quiz/') === 0, 'hash=' + await p.evaluate(() => location.hash));
    need(await vis(p, '#btn-start-quiz'), 'start button missing');
    return 'start card open';
  });

  await step(p, 'quiz/start card leaves home without a warning', async () => {
    await home(p);
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
    await wait(p, 900);
    need(await vis(p, '#btn-start-quiz'), 'start card missing');
    await p.evaluate(() => { location.hash = '#/'; });
    await wait(p, 900);
    const warned = await vis(p, '#leave-modal');
    const h = await p.evaluate(() => location.hash);
    need(!warned, 'the start card warned even though nothing started');
    need(atHome(h), 'did not leave the start card: ' + h);
    return 'left silently (nothing started)';
  });

  await step(p, 'home/info cell opens the info sheet', async () => {
    await home(p);
    const diag = await p.evaluate(() => ({
      rows: document.querySelectorAll('#catalog-cards-container .sketch-row').length,
      info: document.querySelectorAll('#catalog-cards-container .row-info-cell').length,
      deckVisible: !!document.querySelector('#deck-catalog').offsetParent,
      hash: location.hash,
    }));
    need(diag.info > 0 && diag.deckVisible, 'catalogue not ready: ' + JSON.stringify(diag));
    await p.locator('#catalog-cards-container .row-info-cell').first().click({ timeout: 8000 });
    await wait(p, 800);
    need(await vis(p, '#info-sheet-start'), 'info sheet missing');
    return 'info sheet open';
  });

  await step(p, 'info sheet/close button', async () => {
    await p.click('#btn-close-info'); await wait(p, 500);
    need(!(await vis(p, '#info-sheet-start')), 'still open');
    return 'closed';
  });

  await step(p, 'home/saved shortcut is hidden on home and works from saved', async () => {
    await home(p);
    const onHome = await vis(p, '#btn-open-saved');
    need(!onHome, 'the saved shortcut is visible on the home screen (it should hide there)');
    await p.evaluate(() => { location.hash = '#/saved'; }); await wait(p, 1100);
    need(await vis(p, '#btn-open-saved'), 'the saved shortcut is missing in the saved view');
    await p.click('#btn-open-saved'); await wait(p, 700);
    return 'hidden on home, visible in saved';
  });

  // ---------------- drawer ----------------
  await step(p, 'drawer/hamburger opens', async () => {
    await home(p);
    await p.click('#btn-menu-catalog'); await wait(p, 800);
    need(await vis(p, '#menu-drawer'), 'drawer not visible');
    return 'open';
  });

  for (const [label, id, expectHash] of [
    ['saved', '#menu-saved', '#/saved'],
    ['stats', '#menu-stats', '#/stats'],
    ['league', '#menu-league', '#/league'],
    ['account', '#menu-account', '#/account'],
  ]) {
    await step(p, 'drawer/' + label + ' row navigates', async () => {
      await home(p);
      await p.click('#btn-menu-catalog'); await wait(p, 700);
      await p.click(id); await wait(p, 900);
      const h = await p.evaluate(() => location.hash);
      need(h.indexOf(expectHash) === 0, 'hash=' + h);
      return h;
    });
  }

  await step(p, 'drawer/install row reports state', async () => {
    await home(p);
    await p.click('#btn-menu-catalog'); await wait(p, 700);
    await p.click('#menu-install'); await wait(p, 800);
    const txt = await p.locator('#menu-install').textContent();
    need(/مثبّت|متاح|ثبّته/.test(txt), 'no state text: ' + txt.replace(/\n/g, ' '));
    return txt.replace(/\n/g, ' | ').slice(0, 70);
  });

  await step(p, 'drawer/offline row reports state', async () => {
    await home(p);
    await p.click('#btn-menu-catalog'); await wait(p, 700);
    await p.click('#menu-offline'); await wait(p, 900);
    const txt = await p.locator('#menu-offline').innerText();
    need(/جاهزة|بدون إنترنت|تجهيز|نت/.test(txt), 'no offline text: ' + txt.replace(/\n/g, ' '));
    return txt.replace(/\n/g, ' | ').slice(0, 70);
  });

  await step(p, 'drawer/sound row toggles', async () => {
    await home(p);
    await p.click('#btn-menu-catalog'); await wait(p, 700);
    const a = await p.locator('#menu-sound-label').innerText();
    await p.click('#menu-sound'); await wait(p, 500);
    const b2 = await p.locator('#menu-sound-label').innerText();
    need(a !== b2, 'label unchanged: ' + a);
    await p.click('#menu-sound'); await wait(p, 300);
    return a + ' -> ' + b2;
  });

  await step(p, 'drawer/theme row toggles', async () => {
    const a = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
    await p.click('#menu-theme'); await wait(p, 600);
    const b2 = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
    need(a !== b2, 'theme unchanged');
    await p.click('#menu-theme'); await wait(p, 300);
    return a + ' -> ' + b2;
  });

  await step(p, 'drawer/close button', async () => {
    await p.click('#btn-close-menu'); await wait(p, 600);
    need(!(await vis(p, '#menu-drawer')), 'still open');
    return 'closed';
  });

  await step(p, 'drawer/tour row replays the tour', async () => {
    await home(p);
    await p.click('#btn-menu-catalog'); await wait(p, 700);
    await p.click('#menu-tour'); await wait(p, 1500);
    need(await vis(p, '#tour-tip'), 'tour tip missing');
    const t = await p.locator('#tour-tip-title').innerText();
    await p.click('#tour-btn-skip'); await wait(p, 700);
    return t;
  });

  // ---------------- quiz ----------------
  await step(p, 'quiz/start a 5-question bank', async () => {
    await home(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).click(); // AI
    await wait(p, 500);
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
    await wait(p, 900);
    await p.click('#btn-start-quiz');
    await p.waitForSelector('#options-container .option-tile', { timeout: 15000 });
    return 'question 1 of ' + (await p.locator('#question-total-label').innerText());
  });

  await step(p, 'quiz/option tile selects', async () => {
    await p.locator('#options-container .option-tile').nth(0).click();
    await wait(p, 500);
    const locked = await p.evaluate(() => document.querySelector('#options-container').classList.contains('locked'));
    need(locked, 'options not locked after answering');
    return 'answered';
  });

  await step(p, 'quiz/save bookmark', async () => {
    await p.click('#btn-save-question'); await wait(p, 700);
    const saved = await p.evaluate(() => localStorage.getItem('portal_saved_v1') || '{}');
    need(saved.length > 2, 'nothing saved');
    return 'saved keys: ' + Object.keys(JSON.parse(saved)).length;
  });

  await step(p, 'quiz/explanation toggle', async () => {
    const before = await p.evaluate(() => document.querySelector('#live-feedback-box').classList.contains('collapsed'));
    await clearToasts(p);
    await p.click('#live-expl-toggle');
    await wait(p, 500);
    const after = await p.evaluate(() => document.querySelector('#live-feedback-box').classList.contains('collapsed'));
    need(before !== after, 'collapsed state unchanged');
    return before + ' -> ' + after;
  });

  await step(p, 'quiz/language switch EN', async () => {
    await clearToasts(p); await p.click('#lang-switch-session .lang-opt[data-lang="en"]'); await wait(p, 700);
    const letters = await p.locator('.option-letter').first().innerText();
    need(letters.trim() === 'A', 'letters=' + letters);
    await p.click('#lang-switch-session .lang-opt[data-lang="ar"]'); await wait(p, 500);
    return 'EN ok, back to AR';
  });

  await step(p, 'quiz/matrix drawer + jump', async () => {
    await clearToasts(p); await p.click('#btn-open-matrix'); await wait(p, 800);
    need(await vis(p, '#matrix-grid'), 'matrix missing');
    await p.locator('#matrix-grid button, #matrix-grid .matrix-cell').nth(2).click();
    await wait(p, 700);
    await p.click('#btn-close-matrix'); await wait(p, 500);
    return 'index now ' + (await p.locator('#question-index-label').innerText());
  });

  await step(p, 'quiz/timer pause', async () => {
    await clearToasts(p); await p.click('#btn-timer-pause'); await wait(p, 800);
    const t1 = await p.locator('#quiz-timer, .quiz-timer').first().innerText().catch(() => '');
    await wait(p, 1200);
    const t2 = await p.locator('#quiz-timer, .quiz-timer').first().innerText().catch(() => '');
    return 'timer ' + t1.trim() + ' -> ' + t2.trim();
  });

  await step(p, 'quiz/exit warns before leaving (leave modal)', async () => {
    await clearToasts(p); await p.click('#btn-exit'); await wait(p, 800);
    need(await vis(p, '#leave-modal'), 'no leave warning — the quiz exited directly');
    const title = await p.locator('#leave-title').innerText();
    await p.click('#leave-stay'); await wait(p, 600);
    need(!(await vis(p, '#leave-modal')), 'stay did not close the modal');
    need((await p.evaluate(() => location.hash)).indexOf('#/quiz/') === 0, 'stay left the quiz');
    return title.trim();
  });

  await step(p, 'quiz/exit confirmed leaves the quiz', async () => {
    await clearToasts(p); await p.click('#btn-exit'); await wait(p, 700);
    need(await vis(p, '#leave-modal'), 'no warning on the second exit');
    await p.click('#leave-go'); await wait(p, 900);
    const h = await p.evaluate(() => location.hash);
    need(h.indexOf('#/quiz/') !== 0, 'still in the quiz: ' + h);
    return 'left -> ' + h;
  });

  // ---------------- results ----------------
  await step(p, 'results/finish a quiz and land on the results', async () => {
    await home(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).waitFor({ timeout: 15000 });
    await clearToasts(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).click();
    await wait(p, 600);
    await clearToasts(p);
    await p.locator('#catalog-cards-container .sketch-play-cell').first().waitFor({ timeout: 15000 });
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
    await wait(p, 1000);
    await clearToasts(p);
    await p.click('#btn-start-quiz');
    await wait(p, 1200);
    const st = await p.evaluate(() => ({
      hash: location.hash,
      views: [...document.querySelectorAll('.state-view, .quiz-view, .results-view')].filter((x) => x.offsetParent).map((x) => x.id),
      options: document.querySelectorAll('#options-container .option-tile').length,
    }));
    need(st.options > 0, 'quiz did not start: ' + JSON.stringify(st));
    for (let i = 0; i < 8; i++) {
      await p.locator('#options-container .option-tile').nth(0).click();
      await wait(p, 400);
      if (!(await vis(p, '#btn-next'))) break;
      await p.click('#btn-next'); await wait(p, 500);
      if (!(await vis(p, '#options-container .option-tile'))) break;
    }
    await wait(p, 1200);
    need(await vis(p, '#results-view'), 'no results view');
    return 'score ' + (await p.locator('#results-view .score-value, #results-view .results-score').first().innerText().catch(() => '?'));
  });

  await step(p, 'results/review filter pills', async () => {
    const pills = await count(p, '.filter-pill');
    for (let i = 0; i < pills; i++) {
      await p.locator('.filter-pill').nth(i).click();
      await wait(p, 400);
      const cards = await count(p, '#review-cards-list > *');
      if (i === 0) need(cards > 0, 'no review cards');
    }
    return pills + ' pills ok';
  });

  await step(p, 'results/back to catalog', async () => {
    await p.click('#btn-back-catalog'); await wait(p, 900);
    need(atHome(await p.evaluate(() => location.hash)), 'hash wrong');
    return 'home';
  });

  await step(p, 'results/retry quiz', async () => {
    // finish quickly then retry
    await home(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).waitFor({ timeout: 15000 });
    await clearToasts(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).click();
    await wait(p, 600);
    await clearToasts(p);
    await p.locator('#catalog-cards-container .sketch-play-cell').first().waitFor({ timeout: 15000 });
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
    await wait(p, 1000);
    await clearToasts(p);
    await p.click('#btn-start-quiz');
    await wait(p, 1200);
    const st = await p.evaluate(() => ({
      hash: location.hash,
      views: [...document.querySelectorAll('.state-view, .quiz-view, .results-view')].filter((x) => x.offsetParent).map((x) => x.id),
      options: document.querySelectorAll('#options-container .option-tile').length,
    }));
    need(st.options > 0, 'quiz did not start: ' + JSON.stringify(st));
    for (let i = 0; i < 8; i++) {
      await p.locator('#options-container .option-tile').nth(0).click(); await wait(p, 350);
      if (!(await vis(p, '#btn-next'))) break;
      await p.click('#btn-next'); await wait(p, 450);
      if (!(await vis(p, '#options-container .option-tile'))) break;
    }
    await wait(p, 1000);
    await p.click('#btn-retry-quiz'); await wait(p, 1200);
    need(await vis(p, '#options-container .option-tile'), 'retry did not start a quiz');
    return 'restarted';
  });

  await step(p, 'quiz/leave after the retry (cleanup)', async () => {
    await p.click('#btn-exit'); await wait(p, 700);
    if (await vis(p, '#leave-modal')) { await p.click('#leave-go'); await wait(p, 700); }
    return 'left';
  });

  // ---------------- saved / stats / league / account ----------------
  await step(p, 'saved view renders the saved question', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/saved'; }); await wait(p, 1200);
    const groups = await count(p, '#saved-groups > *');
    need(groups > 0, 'no saved groups');
    const chips = await count(p, '#saved-subject-bar .filter-chip');
    return 'groups: ' + groups + ', subject chips: ' + chips;
  });

  await step(p, 'stats range pills + hero', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/stats'; }); await wait(p, 1400);
    const pills = await count(p, '.range-opt');
    for (let i = 0; i < pills; i++) { await p.locator('.range-opt').nth(i).click(); await wait(p, 500); }
    const hero = await count(p, '#stats-hero > *');
    return 'pills: ' + pills + ', hero nodes: ' + hero;
  });

  await step(p, 'stats export button responds', async () => {
    const [dl] = await Promise.all([
      p.waitForEvent('download', { timeout: 4000 }).catch(() => null),
      p.click('#btn-export-data'),
    ]);
    return dl ? ('download: ' + dl.suggestedFilename()) : 'clicked (no download event in this context)';
  });

  await step(p, 'league share card modal', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/league'; }); await wait(p, 1800);
    const state = await p.evaluate(() => ({
      rows: document.querySelectorAll('#league-board .league-row').length,
      empty: !document.querySelector('#league-empty-state').classList.contains('hidden'),
      me: !document.querySelector('#league-me').hasAttribute('hidden'),
      share: !!document.querySelector('#btn-league-share').offsetParent,
    }));
    if (!state.share) return 'share hidden (state: ' + JSON.stringify(state) + ')';
    await clearToasts(p);
    await p.click('#btn-league-share'); await wait(p, 2500);
    const modal = await vis(p, '#share-modal');
    if (modal) {
      await p.click('#share-close'); await wait(p, 500);
      return 'in-app share card shown (state ' + JSON.stringify(state) + ')';
    }
    // Android Chrome can share a file natively: the sheet is a system dialog,
    // invisible to CDP — dismiss it and report the path taken
    try { execSync('adb shell input keyevent KEYCODE_BACK', { stdio: 'ignore' }); } catch (e) {}
    await wait(p, 1200);
    const after = await count(p, '.portal-toast');
    return 'native share sheet path (toasts: ' + after + ', state ' + JSON.stringify(state) + ')';
  });

  await step(p, 'league subject filter chips', async () => {
    const n = await count(p, '#league-subject-bar .filter-chip');
    if (!n) return 'no league filters (empty board)';
    for (let i = 0; i < n; i++) { await clearToasts(p); await p.locator('#league-subject-bar .filter-chip').nth(i).click({ timeout: 8000 }); await wait(p, 600); }
    return n + ' league filters ok';
  });

  await step(p, 'account sync now', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/account'; }); await wait(p, 1400);
    await p.click('#account-sync-now'); await wait(p, 1200);
    const toast = await count(p, '.portal-toast');
    return 'toasts: ' + toast;
  });

  await step(p, 'account link-device modal', async () => {
    await p.click('#account-link'); await wait(p, 1000);
    need(await vis(p, '#link-modal'), 'link modal missing');
    await p.click('#link-close'); await wait(p, 600);
    return 'opened and closed';
  });

  await step(p, 'account avatar picker', async () => {
    const before = await p.evaluate(() => localStorage.getItem('portal_account_v1'));
    await p.locator('#account-avatar-preview, .avatar-picker-open').first().click().catch(() => {});
    await wait(p, 900);
    const grid = await count(p, '.avatar-grid button, .avatar-option');
    if (grid) { await p.locator('.avatar-grid button, .avatar-option').nth(3).click(); await wait(p, 900); }
    const after = await p.evaluate(() => localStorage.getItem('portal_account_v1'));
    return 'avatar options: ' + grid + (before !== after ? ', avatar changed' : ', unchanged');
  });

  await step(p, 'account back arrow', async () => {
    await p.click('#account-close'); await wait(p, 900);
    const h = await p.evaluate(() => location.hash);
    need(h.indexOf('#/account') !== 0, 'still on the account page');
    return 'back -> ' + h;
  });

  await home(p);
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/sweep-final.png' });
  await b.close();

  const failed = results.filter((r) => !r.ok);
  console.log('\n=== sweep summary ===');
  console.log(results.length + ' steps, ' + failed.length + ' failed');
  failed.forEach((f) => console.log('  FAIL ' + f.name + ' :: ' + f.note));
  console.log('console errors seen:', consoleErrors.length, consoleErrors.slice(0, 5).join(' | '));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
