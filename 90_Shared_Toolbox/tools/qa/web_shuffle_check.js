// Verify runtime shuffling: same quiz, three launches -> question order and
// option order must vary, while the correct-answer TEXT stays identical.
const { chromium } = require('playwright-core');
const EXE = 'C:\\Users\\gokoq\\AppData\\Local\\Thorium\\Application\\thorium.exe';
const BASE = process.env.PORTAL_URL || 'http://127.0.0.1:8081';
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const b = await chromium.launch({ executablePath: EXE, headless: true, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  await ctx.addInitScript("try { localStorage.setItem('portal_tour_done','1'); } catch(e){}");
  const runs = [];
  for (let r = 0; r < 3; r++) {
    const p = await ctx.newPage();
    await p.goto(BASE + '/?debug=1&v=' + Date.now() + r, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await p.waitForFunction(() => window.__portal && window.__portal.S && window.__portal.S.index, null, { timeout: 40000 });
    // start the first AI quiz directly
    await p.evaluate(() => { location.hash = '#/quiz/06_Artificial_Intelligence/Quiz_Ch01_ModelA_AI_Foundations'; });
    await p.waitForFunction(() => window.__portal && window.__portal.S && window.__portal.S.session, null, { timeout: 20000 });
    await wait(800);
    if (await p.locator("#btn-start-quiz").isVisible().catch(() => false)) { await p.click("#btn-start-quiz"); }
    await p.waitForFunction(() => window.__portal.S.session.started, null, { timeout: 20000 });
    const snap = await p.evaluate(() => window.__portal.S.session.questions.map((q) => ({
      id: q.id,
      opts: q.options.map((o) => (o && o.en) || o),
      correctText: (() => { const o = q.options[q.correct]; return (o && o.en) || o; })(),
    })));
    runs.push(snap);
    await p.close();
  }
  const byId = (id) => runs.map((s) => s.find((q) => q.id === id));
  const qOrder = runs.map((s) => s.map((q) => q.id).join(','));
  const oOrder = byId('q1').map((q) => q.opts.join('|'));
  const keyText = byId('q1').map((q) => q.correctText);
  console.log('question orders:', JSON.stringify(qOrder, null, 1));
  console.log('q1 option orders differ:', new Set(oOrder).size > 1, JSON.stringify(oOrder));
  console.log('q1 correct text stable:', new Set(keyText).size === 1, JSON.stringify(keyText));
  const okOrder = new Set(qOrder).size > 1 || new Set(oOrder).size > 1;
  console.log(okOrder && new Set(keyText).size === 1 ? 'SHUFFLE-OK' : 'SHUFFLE-FAIL');
  await b.close();
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
