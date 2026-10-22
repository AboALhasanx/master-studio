// Offline button sweep on the tablet: Wi-Fi is off, so every screen must come
// from the device cache and still behave. Same setup -> act -> assert shape.
const { chromium } = require('playwright-core');
const results = [];
let consoleErrors = [];
const wait = (p, ms) => p.waitForTimeout(ms);
const vis = (p, sel) => p.locator(sel).first().isVisible().catch(() => false);
const count = (p, sel) => p.locator(sel).count().catch(() => 0);
const need = (c, m) => { if (!c) throw new Error(m); };
const clearToasts = (p) => p.evaluate(() => { document.querySelectorAll('.portal-toast').forEach((t) => t.remove()); });

async function home(p) {
  await p.evaluate(() => { location.hash = '#/'; });
  await wait(p, 600);
  await p.evaluate(() => {
    const lv = document.querySelector('#leave-modal');
    if (lv && !lv.classList.contains('hidden')) { const g = document.querySelector('#leave-go'); if (g) g.click(); }
  });
  await wait(p, 700);
  await p.evaluate(() => {
    document.querySelectorAll('.modal-overlay:not(.hidden)').forEach((m) => { const c = m.querySelector('.icon-btn'); if (c) c.click(); });
    document.querySelectorAll('.drawer.open').forEach((d) => { const c = d.querySelector('.icon-btn'); if (c) c.click(); });
    const po = document.querySelector('#pause-overlay'); if (po) po.classList.add('hidden');
    document.querySelectorAll('.portal-toast').forEach((t) => t.remove());
    location.hash = '#/';
  });
  await wait(p, 1000);
  await clearToasts(p);
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

(async () => {
  const b = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = b.contexts()[0];
  let p = ctx.pages().find((x) => x.url().indexOf('mcq-portal') >= 0);
  if (!p) {
    p = await ctx.newPage();
    await p.goto('https://mcq-portal-jade.vercel.app/', { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  }
  await p.bringToFront();
  p.on('pageerror', (e) => consoleErrors.push('pageerror: ' + e.message.split('\n')[0]));
  p.on('console', (m) => { if (m.type() === 'error') consoleErrors.push('console: ' + m.text().slice(0, 120)); });

  // offline: a "?v=" URL bypasses the cache, so open the plain URL (SW-served)
  await p.goto('https://mcq-portal-jade.vercel.app/', { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  await p.waitForTimeout(2500);
  await p.waitForFunction(() => window.PortalApp && window.PortalApp.bankCount() >= 30, null, { timeout: 40000 });
  await home(p);
  console.log('offline?', await p.evaluate(() => !navigator.onLine),
              '| source:', await p.evaluate(() => window.PortalApp.contentSource()),
              '| banks:', await p.evaluate(() => window.PortalApp.bankCount()));

  await step(p, 'offline/the shell opens from cache', async () => {
    const st = await p.evaluate(() => ({ online: navigator.onLine, src: window.PortalApp.contentSource(), banks: window.PortalApp.bankCount() }));
    need(st.online === false, 'the device is still online');
    need(st.src === 'cache', 'content source is ' + st.src);
    need(st.banks >= 30, 'only ' + st.banks + ' banks cached');
    return JSON.stringify(st);
  });

  await step(p, 'offline/all six subjects and their chapters render', async () => {
    const subjects = await count(p, '#subject-filter-bar .filter-chip');
    need(subjects === 6, subjects + ' subjects');
    const seen = [];
    for (let i = 0; i < subjects; i++) {
      await clearToasts(p);
      await p.locator('#subject-filter-bar .filter-chip').nth(i).click();
      await wait(p, 450);
      const cards = await count(p, '#catalog-cards-container .sketch-row');
      need(cards >= 1, 'no cards in subject ' + i);
      seen.push(cards);
    }
    return 'cards per subject: ' + seen.join(',');
  });

  await step(p, 'offline/theme + sound buttons work', async () => {
    await home(p);
    const t0 = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
    await p.click('#btn-theme-header'); await wait(p, 500);
    const t1 = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
    need(t0 !== t1, 'theme did not change');
    await p.click('#btn-theme-header'); await wait(p, 400);
    await clearToasts(p);
    const s0 = await p.evaluate(() => (document.querySelector('#sound-header-icon') || {}).getAttribute('data-lucide'));
    await p.click('#btn-sound-header'); await wait(p, 400);
    const s1 = await p.evaluate(() => (document.querySelector('#sound-header-icon') || {}).getAttribute('data-lucide'));
    need(s0 !== s1, 'sound did not change');
    await p.click('#btn-sound-header'); await wait(p, 300);
    return t0 + '->' + t1 + ' | ' + s0 + '->' + s1;
  });

  await step(p, 'offline/notifications sheet opens', async () => {
    await clearToasts(p);
    await p.click('#btn-bell'); await wait(p, 800);
    need(await vis(p, '#notif-modal'), 'sheet missing');
    await p.click('#notif-close'); await wait(p, 500);
    return 'opened and closed';
  });

  await step(p, 'offline/drawer rows open every screen', async () => {
    const rows = [['#menu-saved', '#/saved'], ['#menu-stats', '#/stats'], ['#menu-league', '#/league'], ['#menu-account', '#/account']];
    const out = [];
    for (const [sel, hash] of rows) {
      await home(p);
      await clearToasts(p);
      await p.click('#btn-menu-catalog'); await wait(p, 700);
      await p.click(sel); await wait(p, 1200);
      const h = await p.evaluate(() => location.hash);
      need(h.indexOf(hash) === 0, sel + ' -> ' + h);
      out.push(hash);
    }
    return out.join(' ');
  });

  await step(p, 'offline/quiz opens, answers and explains', async () => {
    await home(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).waitFor({ timeout: 15000 });
    await clearToasts(p);
    await p.locator('#subject-filter-bar .filter-chip').nth(5).click(); await wait(p, 600);
    await clearToasts(p);
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click(); await wait(p, 1200);
    await p.click('#btn-start-quiz'); await wait(p, 1200);
    const opts = await count(p, '#options-container .option-tile');
    need(opts === 4, 'options: ' + opts);
    await p.locator('#options-container .option-tile').nth(0).click(); await wait(p, 700);
    const fb = await vis(p, '#live-feedback-box');
    need(fb, 'no explanation after answering');
    return '4 options + explanation';
  });

  await step(p, 'offline/language switch works', async () => {
    await clearToasts(p);
    await p.click('#lang-switch-session .lang-opt[data-lang="en"]'); await wait(p, 700);
    const letters = (await p.locator('.option-letter').first().innerText()).trim();
    need(letters === 'A', 'letters=' + letters);
    await p.click('#lang-switch-session .lang-opt[data-lang="ar"]'); await wait(p, 500);
    return 'EN ok';
  });

  await step(p, 'offline/matrix drawer works', async () => {
    await clearToasts(p);
    await p.click('#btn-open-matrix'); await wait(p, 900);
    const cells = await count(p, '#matrix-grid button, #matrix-grid .matrix-cell');
    need(cells > 0, 'no matrix cells');
    await p.click('#btn-close-matrix'); await wait(p, 500);
    return cells + ' cells';
  });

  await step(p, 'offline/leave guard still warns', async () => {
    await clearToasts(p);
    await p.click('#btn-exit'); await wait(p, 800);
    need(await vis(p, '#leave-modal'), 'no warning offline');
    await p.click('#leave-stay'); await wait(p, 500);
    await clearToasts(p);
    await p.click('#btn-exit'); await wait(p, 700);
    await p.click('#leave-go'); await wait(p, 900);
    need((await p.evaluate(() => location.hash)).indexOf('#/quiz/') !== 0, 'still in the quiz');
    return 'warned, then left';
  });

  await step(p, 'offline/stats and saved render from local data', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/stats'; }); await wait(p, 1500);
    const pills = await count(p, '.range-opt');
    need(pills === 3, 'range pills: ' + pills);
    await p.evaluate(() => { location.hash = '#/saved'; }); await wait(p, 1300);
    const groups = await count(p, '#saved-groups > *');
    return 'stats pills: ' + pills + ', saved groups: ' + groups;
  });

  await step(p, 'offline/account sync reports honestly (no crash)', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/account'; }); await wait(p, 1500);
    await clearToasts(p);
    await p.click('#account-sync-now'); await wait(p, 2500);
    const toast = await p.evaluate(() => {
      const t = document.querySelector('.portal-toast');
      return t ? t.textContent.trim() : '';
    });
    need(/\S/.test(toast), 'offline sync stayed silent');
    return 'toast: ' + toast;
  });

  await step(p, 'offline/league shows cached board or the offline note', async () => {
    await home(p);
    await p.evaluate(() => { location.hash = '#/league'; }); await wait(p, 2500);
    const st = await p.evaluate(() => ({
      rows: document.querySelectorAll('#league-board .league-row').length,
      empty: !document.querySelector('#league-empty-state').classList.contains('hidden'),
      note: !!document.querySelector('#league-offline-note') && !!document.querySelector('#league-offline-note').offsetParent,
      text: (document.querySelector('#league-offline-note') || {}).textContent || '',
    }));
    need(st.rows > 0 || st.empty || st.note, 'no rows, no empty state and no offline note: ' + JSON.stringify(st));
    return JSON.stringify(st).slice(0, 120);
  });

  await step(p, 'offline/league share fails gracefully', async () => {
    const shareVisible = await vis(p, '#btn-league-share');
    if (!shareVisible) return 'share button hidden with no board';
    await clearToasts(p);
    await p.click('#btn-league-share'); await wait(p, 2500);
    const st = await p.evaluate(() => ({
      modal: !document.querySelector('#share-modal').classList.contains('hidden'),
      toast: (document.querySelector('.portal-toast') || {}).textContent || '',
    }));
    need(st.modal || /\S/.test(st.toast), 'offline share stayed silent');
    return 'modal: ' + st.modal + ', toast: ' + (st.toast.trim() || '(none)');
  });

  await home(p);
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/offline-sweep.png' });
  await b.close();

  const failed = results.filter((r) => !r.ok);
  console.log('\n=== offline sweep ===');
  console.log(results.length + ' steps, ' + failed.length + ' failed');
  failed.forEach((f) => console.log('  FAIL ' + f.name + ' :: ' + f.note));
  console.log('console errors:', consoleErrors.length, consoleErrors.slice(0, 4).join(' | '));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
