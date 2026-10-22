const { chromium } = require('playwright-core');
const out = [];
const T = (n, c, x = '') => { out.push(`${c ? 'PASS' : 'FAIL'} ${n}${!c && x ? ' :: ' + x : ''}`); console.log(out[out.length - 1]); };
(async () => {
  const b = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const p = b.contexts()[0].pages().find((x) => x.url().indexOf('mcq-portal') >= 0);
  await p.bringToFront();
  p.on('pageerror', (e) => console.log('PAGEERROR:', e.message.split('\n')[0]));

  // fresh shell
  await p.goto('https://mcq-portal-jade.vercel.app/?v=95', { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  for (let i = 0; i < 20; i++) { await p.waitForTimeout(1000); if (await p.evaluate(() => localStorage.getItem('portal_shell_version')) === 'v95') break; }
  await p.waitForFunction(() => window.PortalApp && window.PortalApp.bankCount() >= 38, null, { timeout: 40000 });

  // pretend one chapter is brand new: drop its seen version
  const target = 'Quiz_Ch02_ModelA_Search_and_Learning';
  await p.evaluate((qid) => {
    const seen = JSON.parse(localStorage.getItem('portal_seen_v1') || '{}');
    seen[qid] = 0;
    localStorage.setItem('portal_seen_v1', JSON.stringify(seen));
  }, target);
  await p.reload({ waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(4000);
  await p.evaluate(() => { document.querySelectorAll('.portal-toast').forEach((t) => t.remove()); });

  // the AI chapter 2 card must carry the "جديد" badge
  await p.locator('#subject-filter-bar .filter-chip').nth(5).click();
  await p.waitForTimeout(900);
  await p.locator('#chapter-filter-bar .filter-chip').nth(1).click();
  await p.waitForTimeout(900);
  const badgeBefore = await p.evaluate(() => document.querySelectorAll('#catalog-cards-container .sketch-chip-new').length);
  const bellBefore = await p.evaluate(() => (document.querySelector('#bell-dot') || {}).textContent || '');
  T('a new chapter shows the «جديد» badge', badgeBefore >= 1, 'badges: ' + badgeBefore);
  T('the bell shows an unread count', /\\d/.test(bellBefore) || bellBefore === '+1', 'badge: ' + JSON.stringify(bellBefore));

  const itemsBefore = await p.evaluate(() => {
    const btn = document.querySelector('#btn-bell'); if (btn) btn.click();
    return new Promise((r) => setTimeout(() => {
      const n = document.querySelectorAll('#notif-list .notif-row').length;
      const close = document.querySelector('#notif-close'); if (close) close.click();
      r(n);
    }, 700));
  });
  T('the sheet lists the new chapter', itemsBefore >= 1, 'rows: ' + itemsBefore);

  // open the quiz (visit it), then come back home
  await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
  await p.waitForTimeout(1200);
  await p.locator('#btn-start-quiz').click();
  await p.waitForSelector('#options-container .option-tile', { timeout: 20000 });
  await p.evaluate(() => { const x = document.querySelector('#btn-exit'); if (x) x.click(); });
  await p.waitForTimeout(800);
  await p.evaluate(() => { const g = document.querySelector('#leave-go'); if (g) g.click(); });
  await p.waitForTimeout(1500);

  const badgeAfter = await p.evaluate(() => document.querySelectorAll('#catalog-cards-container .sketch-chip-new').length);
  const bellAfter = await p.evaluate(() => {
    const d = document.querySelector('#bell-dot');
    return d ? (d.classList.contains('hidden') ? '' : d.textContent) : 'no-dot';
  });
  T('the «جديد» badge is gone after visiting', badgeAfter === 0, 'badges: ' + badgeAfter);
  T('the bell count dropped', bellAfter === '' || bellAfter === 'no-dot', 'badge: ' + JSON.stringify(bellAfter));

  const itemsAfter = await p.evaluate(() => {
    const btn = document.querySelector('#btn-bell'); if (btn) btn.click();
    return new Promise((r) => setTimeout(() => {
      const n = document.querySelectorAll('#notif-list .notif-row').length;
      const empty = !document.querySelector('#notif-empty').classList.contains('hidden');
      const close = document.querySelector('#notif-close'); if (close) close.click();
      r({ n, empty });
    }, 700));
  });
  T('the notification left the sheet', itemsAfter.n === 0, JSON.stringify(itemsAfter));

  // and it stays gone after a reload
  await p.reload({ waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(4000);
  const persisted = await p.evaluate((qid) => {
    const seen = JSON.parse(localStorage.getItem('portal_seen_v1') || '{}');
    return Number(seen[qid] || 0);
  }, target);
  T('the visit is remembered', persisted > 0, 'seen version: ' + persisted);

  await b.close();
  console.log('\n' + (out.filter((l) => l.startsWith('FAIL')).join('\n') || 'all green'));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
