// Verify one published chapter in the real app (defaults: Cyber chapter 5):
//  - 17 cards in chapter 5, each with a "Ù…ÙˆØ¶ÙˆØ¹: N" badge, no subject name in titles
//  - the retired bank (Quiz_02_Risk_Assessment) is gone from the catalogue
//  - two launches reshuffle questions AND options while the correct text is stable
//  - the translation toggle switches the stem to English
function loadChromium() {
  const path = require('path');
  const roots = [
    process.env.PLAYWRIGHT_CORE,
    path.join(process.env.TEMP || 'C:\\Windows\\Temp', 'opencode', 'shot', 'node_modules', 'playwright-core'),
  ].filter(Boolean);
  try { return require('playwright-core').chromium; } catch (e) {}
  for (const r of roots) { try { return require(r).chromium; } catch (e) {} }
  console.error('playwright-core not found: npm i playwright-core   (or set PLAYWRIGHT_CORE=<path to the package>)');
  process.exit(2);
}
const chromium = loadChromium();
const EXE = 'C:\\Users\\gokoq\\AppData\\Local\\Thorium\\Application\\thorium.exe';
const BASE = process.env.PORTAL_URL || 'http://127.0.0.1:8081';
const SUBJ = process.env.SUBJECT || '01_Cyber_Security';
const CHAPTER = Number(process.env.CHAPTER || 5);
const QUIZ = process.env.QUIZ || 'Quiz_Ch05_T01_Protocol_Surface_And_Transport';
const EXPECT = Number(process.env.EXPECT || 17);
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
let fails = 0;
const check = (name, ok, detail) => {
  console.log((ok ? 'PASS ' : 'FAIL ') + name + (detail === undefined ? '' : ' -> ' + detail));
  if (!ok) fails++;
};

(async () => {
  const b = await chromium.launch({ executablePath: EXE, headless: true, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  await ctx.addInitScript(`
    try {
      localStorage.setItem('portal_tour_done', '1');
      localStorage.setItem('portal_ui_v1', JSON.stringify({ subject: '${SUBJ}', chapter: ${CHAPTER}, lang: 'ar' }));
    } catch (e) {}
  `);
  const p = await ctx.newPage();
  await p.goto(BASE + '/?debug=1&v=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForFunction(() => window.__portal && window.__portal.S && window.__portal.S.index, null, { timeout: 45000 });

  const info = await p.evaluate((CHAPTER) => {
    const S = window.__portal.S;
    const sub = S.index.subjects.find((s) => s.subject_id === '01_Cyber_Security');
    const chs = sub ? sub.chapters : [];
    return {
      version: S.contentVersion,
      source: S.contentSource,
      chapters: [...new Set(chs.map((c) => c.chapter_no))].sort((a, b) => a - b),
      ch5: chs.filter((c) => c.chapter_no === CHAPTER).map((c) => ({ quiz: c.quiz_id, topic: (c.topic && c.topic.ar) || '', n: c.count, label: c.topicLabel })),
      risk: chs.some((c) => c.quiz_id === 'Quiz_02_Risk_Assessment'),
      subjectTitle: sub ? sub.subject_title : '',
    };
  }, CHAPTER);
  console.log('content version:', info.version, '| source:', info.source, '| chapters:', info.chapters.join(','));
  check('chapter ' + CHAPTER + ' has ' + EXPECT + ' banks', info.ch5.length === EXPECT, info.ch5.length);
  check('retired Risk_Assessment not listed', info.risk === false);
  const nums = info.ch5.map((c) => (c.label.match(/\d+/) || [''])[0]);
  check('topic badges are 1..N', nums.join(',') === Array.from({ length: EXPECT }, (_, i) => String(i + 1)).join(','), nums.join(' '));
  const dupSubject = info.ch5.filter((c) => c.topic && info.subjectTitle && c.topic.includes(info.subjectTitle));
  check('no card title repeats the subject name', dupSubject.length === 0, dupSubject.map((c) => c.topic).join(' | '));

  await p.waitForSelector('.sketch-row', { timeout: 30000 });
  const dom = await p.evaluate(() => ({
    rows: document.querySelectorAll('.sketch-row').length,
    badges: [...document.querySelectorAll('.sketch-topic-num')].map((e) => e.textContent.trim()),
    titles: [...document.querySelectorAll('.sketch-title')].map((e) => e.textContent.trim()),
    subjectTags: [...document.querySelectorAll('.sketch-subject-tag')].map((e) => e.textContent.trim()),
  }));
  check('DOM shows ' + EXPECT + ' cards', dom.rows === EXPECT, dom.rows);
  check('DOM badges match', dom.badges.join('|') === info.ch5.map((c) => c.label).join('|'), dom.badges.slice(0, 3).join(' '));
  check('every card carries the subject chip', dom.subjectTags.length === EXPECT && dom.subjectTags.every((t) => t === info.subjectTitle), dom.subjectTags[0]);
  console.log('first three cards:', JSON.stringify(dom.titles.slice(0, 3), null, 0));

  // ---- two launches, shuffle + language toggle -----------------------------
  const runs = [];
  for (let r = 0; r < 2; r++) {
    const page = r === 0 ? p : await ctx.newPage();
    await page.goto(BASE + '/?debug=1&v=' + Date.now() + r + '#/quiz/' + SUBJ + '/' + QUIZ, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForFunction(() => window.__portal && window.__portal.S && window.__portal.S.session, null, { timeout: 45000 });
    const started = await page.evaluate(() => !!(window.__portal.S.session && window.__portal.S.session.started));
    if (!started) {
      if (await page.locator('#btn-start-quiz').isVisible().catch(() => false)) await page.click('#btn-start-quiz');
      await page.waitForFunction(() => window.__portal.S.session && window.__portal.S.session.started, null, { timeout: 30000 });
    }
    await wait(400);
    const snap = await page.evaluate(() => {
      const S = window.__portal.S;
      const ses = S.session;
      return {
        lang: S.lang,
        order: ses.questions.map((q) => q.id),
        items: ses.questions.map((q) => ({
          id: q.id,
          opts: q.options.map((o) => (o && o.en) || o),
          correctText: (() => { const o = q.options[q.correct]; return (o && o.en) || o; })(),
        })),
        stem: document.getElementById('question-text').textContent.trim(),
        stemDir: document.getElementById('question-text').getAttribute('dir'),
      };
    });
    runs.push(snap);
    if (r === 0) {
      // toggle to English on the live session
      await page.click('#lang-toggle-session');
      await wait(500);
      const after = await page.evaluate(() => ({
        lang: window.__portal.S.lang,
        stem: document.getElementById('question-text').textContent.trim(),
        firstOption: document.querySelector('.option-tile .option-content').textContent.trim(),
      }));
      check('translation toggle switches to English', after.lang === 'en', after.lang);
      check('stem changes with the toggle', after.stem !== snap.stem, JSON.stringify([snap.stem.slice(0, 40), after.stem.slice(0, 40)]));
      check('English stem is Latin text', /[A-Za-z]{4,}/.test(after.stem) && !/[\u0600-\u06FF]/.test(after.stem), after.stem.slice(0, 60));
      await page.click('#lang-toggle-session');
      await wait(300);
    }
  }
  const byId = (id) => runs.map((s) => s.items.find((q) => q.id === id));
  const q1 = runs[0].order[0];
  check('question order differs between launches', runs[0].order.join(',') !== runs[1].order.join(','), runs.map((r) => r.order.join(',')).join(' | '));
  check('option order differs for the same question', byId(q1)[0].opts.join('|') !== byId(q1)[1].opts.join('|'));
  check('correct answer text is stable', byId(q1)[0].correctText === byId(q1)[1].correctText, byId(q1).map((q) => q.correctText.slice(0, 40)).join(' | '));

  console.log(fails === 0 ? '\nALL-CHECKS-PASSED' : '\n' + fails + ' CHECK(S) FAILED');
  await b.close();
  process.exit(fails === 0 ? 0 : 1);
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });

