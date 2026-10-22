// Walk the guided tour on the real tablet, step by step, and report what
// breaks: a missing target, a hidden tip, a wrong view, a console error.
const { chromium } = require('playwright-core');
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const out = [];
const T = (n, c, x = '') => { out.push(`${c ? 'PASS' : 'FAIL'} ${n}${!c && x ? ' :: ' + x : ''}`); console.log(out[out.length - 1]); };

(async () => {
  const b = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = b.contexts()[0];
  const p = ctx.pages().find((x) => x.url().indexOf('mcq-portal') >= 0) || await ctx.newPage();
  const errs = [];
  p.on('pageerror', (e) => errs.push('pageerror: ' + e.message.split('\n')[0]));
  p.on('console', (m) => { if (m.type() === 'error') errs.push('console: ' + m.text().slice(0, 120)); });
  await p.bringToFront();

  // a first-time visitor
  await p.evaluate(() => { try { localStorage.removeItem('portal_tour_done'); } catch (e) {} });
  await p.goto('https://mcq-portal-jade.vercel.app/?t=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  await p.waitForTimeout(5000);

  const shown = await p.evaluate(() => !document.querySelector('#tour-overlay').classList.contains('hidden'));
  T('the tour opens for a first-time visitor', shown);

  let step = 0;
  const seen = [];
  while (step < 40) {
    for (let w = 0; w < 20; w++) {
      const vis = await p.evaluate(() => {
        const t = document.querySelector('#tour-tip');
        return !!t && getComputedStyle(t).visibility === 'visible';
      });
      if (vis) break;
      await wait(200);
    }
    const st = await p.evaluate(() => {
      const ov = document.querySelector('#tour-overlay');
      const tip = document.querySelector('#tour-tip');
      const title = (document.querySelector('#tour-tip-title') || {}).textContent || '';
      const body = (document.querySelector('#tour-tip-body') || {}).textContent || '';
      const prog = (document.querySelector('#tour-tip-progress') || {}).textContent || '';
      const frame = document.querySelector('#tour-frame');
      let target = '';
      if (frame) {
        const r = frame.getBoundingClientRect();
        const el = document.elementFromPoint(Math.round(r.left + r.width / 2), Math.round(r.top + r.height / 2));
        target = el ? (el.id || el.className || el.tagName) : 'none';
      }
      return {
        visible: !!ov && !ov.classList.contains('hidden'),
        title: title.trim(), body: body.trim().slice(0, 70), prog: prog.trim(),
        frame: !!frame && frame.getBoundingClientRect().width > 4,
        target,
        views: [...document.querySelectorAll('.state-view, .quiz-view, .results-view')].filter((x) => x.offsetParent).map((x) => x.id).join(','),
      };
    });
    if (!st.visible) break;
    seen.push(st);
    console.log('  step ' + (step + 1) + ' [' + st.prog + '] ' + st.title + '  | view: ' + st.views);
    const next = p.locator('#tour-btn-next');
    if (!(await next.isVisible().catch(() => false))) { await wait(500); if (!(await next.isVisible().catch(() => false))) { T('the next button is visible on every step', false, st.title); break; } }
    if (await next.isDisabled().catch(() => false)) {
      // the step waits for the student to do the thing it points at
      const acted = await p.evaluate(() => {
        if (document.querySelector('#options-container .option-tile')) { document.querySelector('#options-container .option-tile').click(); return 'answer'; }
        if (document.querySelector('#btn-start-quiz') && document.querySelector('#btn-start-quiz').offsetParent) { document.querySelector('#btn-start-quiz').click(); return 'start'; }
        return 'none';
      });
      console.log('      (action step: ' + acted + ')');
      await wait(1200);
      step++;
      continue;
    }
    await next.click();
    await wait(900);
    step++;
  }

  T('the tour walks to the end', seen.length >= 15, seen.length + ' steps');
  const titles = seen.map((s) => s.title);
  T('every step shows a title', titles.every((t) => t.length > 2), titles.filter((t) => t.length <= 2).join('|'));
  T('every step has a body', seen.every((s) => s.body.length > 5));
  T('the step counter moves', seen.length > 2 && seen[0].prog !== seen[seen.length - 1].prog, seen[0].prog + ' -> ' + seen[seen.length - 1].prog);
  const withFrame = seen.filter((s) => s.frame);
  T('the spotlight finds a target on the steps that have one', withFrame.length >= 5, withFrame.length + ' frames');
  const badFrame = withFrame.filter((s) => s.target === 'none' || s.target === 'body' || s.target === 'html');
  T('the spotlight never lands on nothing', badFrame.length === 0, badFrame.map((s) => s.title).join(' | '));

  // the copy must match the current interface
  const allTitles = titles.join(' | ');
  T('the tour mentions the language switch', /الترجمة|اللغة/.test(allTitles), allTitles.slice(0, 200));
  T('the tour mentions the bell', /جرس|تنبيه/i.test(allTitles) || /جرس|تنبيه/i.test(seen.map(s => s.body).join(' ')));

  // previous + skip (walk a fresh tour, then step back)
  await p.evaluate(() => { try { localStorage.removeItem('portal_tour_done'); } catch (e) {} });
  await p.goto('https://mcq-portal-jade.vercel.app/?t=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  await wait(5000);
  for (let i = 0; i < 3; i++) { await p.locator('#tour-btn-next').click({ timeout: 8000 }).catch(() => {}); await wait(900); }
  const beforePrev = await p.evaluate(() => (document.querySelector('#tour-tip-progress') || {}).textContent);
  await p.locator('#tour-btn-prev').click({ timeout: 8000 }).catch(() => {});
  await wait(900);
  const afterPrev = await p.evaluate(() => (document.querySelector('#tour-tip-progress') || {}).textContent);
  T('the previous button steps back', beforePrev !== afterPrev, beforePrev + ' -> ' + afterPrev);
  await p.evaluate(() => { const b = document.querySelector('#tour-btn-skip'); if (b) b.click(); });
  await wait(700);
  const closed = await p.evaluate(() => document.querySelector('#tour-overlay').classList.contains('hidden'));
  T('the skip button closes the tour', closed);

  // and it can be replayed from the drawer
  await p.evaluate(() => document.querySelector('.btn-menu').click());
  await wait(800);
  await p.evaluate(() => { const m = document.querySelector('#menu-tour'); if (m) m.click(); });
  await wait(1500);
  const replayed = await p.evaluate(() => !document.querySelector('#tour-overlay').classList.contains('hidden'));
  T('the tour can be replayed from the drawer', replayed);
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/tour-replay.png' });

  console.log('\nconsole errors:', errs.length, errs.slice(0, 6).join(' | '));
  await b.close();
  console.log('\n' + (out.filter((l) => l.startsWith('FAIL')).join('\n') || 'all green'));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
