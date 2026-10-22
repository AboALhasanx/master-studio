const { chromium } = require('playwright-core');
const EXE = 'C:\\Users\\gokoq\\AppData\\Local\\Thorium\\Application\\thorium.exe';
(async () => {
  const b = await chromium.launch({ executablePath: EXE, headless: true, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  await ctx.addInitScript("try { localStorage.setItem('portal_tour_done','1'); } catch(e){}");
  await ctx.setExtraHTTPHeaders({ 'Cache-Control': 'no-cache' });
  const p = await ctx.newPage();
  p.on('pageerror', (e) => console.log('PAGEERROR:', e.message.split('\n')[0]));
  await p.goto('https://mcq-portal-jade.vercel.app/?v=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForFunction(() => document.querySelectorAll('#subject-filter-bar .filter-chip').length >= 6, null, { timeout: 40000 });
  await p.waitForTimeout(1500);
  console.log('banks:', await p.evaluate(() => window.PortalApp.bankCount()), '| version:', await p.evaluate(() => window.PortalApp.contentVersion()));
  await p.locator('#subject-filter-bar .filter-chip', { hasText: 'الأمن السيبراني' }).click();
  await p.waitForTimeout(900);
  const ch1 = await p.evaluate(() => ({
    chapters: Array.from(document.querySelectorAll('#chapter-filter-bar .filter-chip')).map((x) => x.textContent.trim()),
    cards: Array.from(document.querySelectorAll('#catalog-cards-container .sketch-title')).map((x) => x.textContent.trim()),
  }));
  console.log('chapters:', JSON.stringify(ch1.chapters), '| ch1 cards:', ch1.cards.length);
  ch1.cards.forEach((t, i) => console.log('  ', i + 1, t));
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/cyber-ch1-cards.png' });
  // open the math bank (T02) and check KaTeX
  await p.locator('#catalog-cards-container .sketch-play-cell').nth(1).click();
  await p.waitForTimeout(1200);
  if (await p.locator('#btn-start-quiz').isVisible().catch(() => false)) await p.locator('#btn-start-quiz').click();
  await p.waitForSelector('#options-container .option-tile', { timeout: 20000 });
  await p.waitForTimeout(600);
  const q = await p.evaluate(() => ({
    stem: document.querySelector('#question-text').textContent.slice(0, 90),
    katex: document.querySelectorAll('#question-text .katex, #question-text-2 .katex, #options-container .katex').length,
    opts: document.querySelectorAll('#options-container .option-tile').length,
  }));
  console.log('quiz:', JSON.stringify(q, null, 1));
  await p.locator('#options-container .option-tile').first().click();
  await p.waitForTimeout(900);
  console.log('feedback visible:', await p.evaluate(() => !document.querySelector('#live-feedback-box').classList.contains('hidden')));
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/cyber-t02-quiz.png' });
  await b.close();
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
