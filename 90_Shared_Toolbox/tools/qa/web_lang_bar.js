const { chromium } = require('playwright-core');
const EXE = 'C:\\Users\\gokoq\\AppData\\Local\\Thorium\\Application\\thorium.exe';
const BASE = process.env.PORTAL_URL || 'http://127.0.0.1:8081';
const out = [];
const T = (n, c, x = '') => { out.push(`${c ? 'PASS' : 'FAIL'} ${n}${!c && x ? ' :: ' + x : ''}`); console.log(out[out.length - 1]); };
(async () => {
  const b = await chromium.launch({ executablePath: EXE, headless: true, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width: 400, height: 860 } });
  await ctx.addInitScript("try { localStorage.setItem('portal_tour_done','1'); } catch(e){}");
  await ctx.setExtraHTTPHeaders({ 'Cache-Control': 'no-cache' });
  await ctx.route('**/sw.js', (r) => r.abort());
  const p = await ctx.newPage();
  p.on('pageerror', (e) => console.log('PAGEERROR:', e.message.split('\n')[0]));
  await p.goto(BASE + '/?v=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForSelector('#catalog-cards-container .sketch-row', { timeout: 30000 });
  await p.waitForTimeout(1200);

  T('home: no language switch in the bar', !(await p.locator('#lang-switch-catalog').isVisible()));
  T('home: the bell is in the bar', await p.locator('#btn-bell').isVisible());

  await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
  await p.waitForTimeout(1000);
  if (await p.locator('#btn-start-quiz').isVisible()) await p.locator('#btn-start-quiz').click();
  await p.waitForSelector('#options-container .option-tile', { timeout: 20000 });
  T('quiz: the language switch is in the bar', await p.locator('#lang-switch-session').isVisible());
  T('quiz: the bell is still there', await p.locator('#btn-bell-session').isVisible());
  const arStem = (await p.locator('#question-text').innerText()).slice(0, 40);
  await p.locator('#lang-switch-session .lang-opt[data-lang="en"]').click();
  await p.waitForTimeout(700);
  const enStem = await p.locator('#question-text').innerText();
  T('quiz: EN translates the question', /[A-Za-z]{4,}/.test(enStem) && enStem !== arStem, enStem.slice(0, 50));
  T('quiz: the EN button is the active one', (await p.locator('#lang-switch-session .lang-opt[data-lang="en"]').getAttribute('aria-pressed')) === 'true');
  await p.locator('#lang-switch-session .lang-opt[data-lang="ar"]').click();
  await p.waitForTimeout(500);

  // finish the quiz to reach the results/review bar
  for (let i = 0; i < 12; i++) {
    if (!(await p.locator('#options-container .option-tile').first().isVisible().catch(() => false))) break;
    await p.locator('#options-container .option-tile').first().click();
    await p.waitForTimeout(350);
    if (await p.locator('#btn-next').isVisible().catch(() => false)) { await p.locator('#btn-next').click().catch(() => {}); await p.waitForTimeout(500); }
  }
  await p.waitForTimeout(1000);
  T('results: the language switch stays in the bar', await p.locator('#lang-switch-session').isVisible());
  T('results: the bell stays too', await p.locator('#btn-bell-session').isVisible());

  await p.evaluate(() => { location.hash = '#/saved'; });
  await p.waitForTimeout(1000);
  T('saved: the language switch is in the bar', await p.locator('#lang-switch-catalog').isVisible());
  T('saved: the bell is there', await p.locator('#btn-bell').isVisible());
  await p.evaluate(() => { location.hash = '#/'; });
  await p.waitForTimeout(800);
  T('home again: the switch disappears', !(await p.locator('#lang-switch-catalog').isVisible()));

  await p.locator('.btn-menu').first().click();
  await p.waitForSelector('#menu-drawer.open', { timeout: 8000 });
  await p.waitForTimeout(500);
  T('drawer: no language row any more', (await p.locator('#menu-drawer .lang-switch, #menu-drawer [data-lang]').count()) === 0);
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/lang-bar.png' });
  await b.close();
  console.log('\n' + (out.filter((l) => l.startsWith('FAIL')).join('\n') || 'all green'));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
