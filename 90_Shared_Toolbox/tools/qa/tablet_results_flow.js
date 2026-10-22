const { chromium } = require('playwright-core');
const out = [];
const T = (n, c, x = '') => { out.push(`${c ? 'PASS' : 'FAIL'} ${n}${!c && x ? ' :: ' + x : ''}`); console.log(out[out.length - 1]); };
(async () => {
  const b = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const p = b.contexts()[0].pages().find((x) => x.url().indexOf('mcq-portal') >= 0);
  await p.bringToFront();
  p.on('pageerror', (e) => console.log('PAGEERROR:', e.message.split('\n')[0]));

  const clean = async () => {
    // a started quiz blocks navigation: ask to leave, then navigate again
    await p.evaluate(() => { location.hash = '#/'; });
    await p.waitForTimeout(700);
    await p.evaluate(() => {
      const lv = document.querySelector('#leave-modal');
      if (lv && !lv.classList.contains('hidden')) { const g = document.querySelector('#leave-go'); if (g) g.click(); }
    });
    await p.waitForTimeout(800);
    await p.evaluate(() => {
      document.querySelectorAll('.modal-overlay:not(.hidden)').forEach((m) => { const c = m.querySelector('.icon-btn'); if (c) c.click(); });
      document.querySelectorAll('.drawer.open').forEach((d) => { const c = d.querySelector('.icon-btn'); if (c) c.click(); });
      const po = document.querySelector('#pause-overlay'); if (po) po.classList.add('hidden');
      document.querySelectorAll('.portal-toast').forEach((t) => t.remove());
      location.hash = '#/';
    });
    await p.waitForTimeout(1100);
    await p.evaluate(() => { document.querySelectorAll('.portal-toast').forEach((t) => t.remove()); });
  };

  const startQuiz = async () => {
    await clean();
    await p.locator('#subject-filter-bar .filter-chip').nth(5).waitFor({ timeout: 15000 });
    await p.locator('#subject-filter-bar .filter-chip').nth(5).click();
    await p.waitForTimeout(600);
    await p.evaluate(() => { document.querySelectorAll('.portal-toast').forEach((t) => t.remove()); });
    await p.locator('#catalog-cards-container .sketch-play-cell').first().waitFor({ timeout: 15000 });
    await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
    await p.waitForTimeout(1100);
    await p.click('#btn-start-quiz');
    await p.waitForSelector('#options-container .option-tile', { timeout: 20000 });
  };

  // 1) finish a quiz
  await startQuiz();
  T('quiz started', await p.locator('#options-container .option-tile').count() === 4);
  for (let i = 0; i < 8; i++) {
    await p.locator('#options-container .option-tile').nth(i % 4).click();
    await p.waitForTimeout(400);
    if (!(await p.locator('#btn-next').isVisible().catch(() => false))) break;
    await p.click('#btn-next'); await p.waitForTimeout(500);
    if (!(await p.locator('#options-container .option-tile').first().isVisible().catch(() => false))) break;
  }
  await p.waitForTimeout(1500);
  T('results view reached', await p.locator('#results-view').isVisible());
  const score = await p.locator('#results-view').innerText();
  console.log('   results text:', score.replace(/\n/g, ' | ').slice(0, 110));
  T('review cards rendered', (await p.locator('#review-cards-list > *').count()) > 0,
    String(await p.locator('#review-cards-list > *').count()));

  // 2) review filter pills
  const pills = await p.locator('.filter-pill').count();
  let pillsOk = true;
  for (let i = 0; i < pills; i++) {
    await p.locator('.filter-pill').nth(i).click();
    await p.waitForTimeout(500);
    const n = await p.locator('#review-cards-list > *').count();
    if (i === 0 && n === 0) pillsOk = false;
  }
  T('review filter pills switch', pillsOk, pills + ' pills');

  // 3) retry wrong only
  await p.click('#btn-retry-wrong'); await p.waitForTimeout(1500);
  T('retry-wrong starts a quiz', (await p.locator('#options-container .option-tile').count()) > 0);
  if ((await p.locator('#options-container .option-tile').count()) > 0) {
    await p.evaluate(() => { const x = document.querySelector('#btn-exit'); if (x) x.click(); });
    await p.waitForTimeout(700);
    if (await p.locator('#leave-modal').isVisible().catch(() => false)) { await p.click('#leave-go'); await p.waitForTimeout(900); }
  }

  // 4) retry the whole quiz, then back to catalog
  await startQuiz();
  for (let i = 0; i < 8; i++) {
    await p.locator('#options-container .option-tile').nth(0).click();
    await p.waitForTimeout(380);
    if (!(await p.locator('#btn-next').isVisible().catch(() => false))) break;
    await p.click('#btn-next'); await p.waitForTimeout(480);
    if (!(await p.locator('#options-container .option-tile').first().isVisible().catch(() => false))) break;
  }
  await p.waitForTimeout(1400);
  await p.click('#btn-retry-quiz'); await p.waitForTimeout(1600);
  T('retry-quiz restarts', (await p.locator('#options-container .option-tile').count()) > 0);
  await p.evaluate(() => { const x = document.querySelector('#btn-exit'); if (x) x.click(); });
  await p.waitForTimeout(700);
  if (await p.locator('#leave-modal').isVisible().catch(() => false)) { await p.click('#leave-go'); await p.waitForTimeout(900); }
  await p.waitForTimeout(900);
  T('back home after leaving', (await p.evaluate(() => location.hash)) === '' || (await p.evaluate(() => location.hash)).indexOf('#/') === 0,
    await p.evaluate(() => location.hash));

  await b.close();
  console.log('\n' + (out.filter((l) => l.startsWith('FAIL')).join('\n') || 'all green'));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
