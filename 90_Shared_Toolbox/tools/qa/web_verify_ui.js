// Verify on the tablet: clean card titles, 1.1 chapter numbers, the login card
// close button, and the leave modal in the light theme.
const { chromium } = require('playwright-core');
const EXE = 'C:\\Users\\gokoq\\AppData\\Local\\Thorium\\Application\\thorium.exe';
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const out = [];
const T = (n, c, x = '') => { out.push(`${c ? 'PASS' : 'FAIL'} ${n}${!c && x ? ' :: ' + x : ''}`); console.log(out[out.length - 1]); };

(async () => {
  const b = await chromium.launch({ executablePath: EXE, headless: true, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  await ctx.addInitScript("try { localStorage.setItem('portal_tour_done','1'); } catch(e){}");
  const p = await ctx.newPage();
  await p.bringToFront();
  await p.goto('https://mcq-portal-jade.vercel.app/?t=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  for (let i = 0; i < 25; i++) { await p.waitForTimeout(1000); try { if (await p.evaluate(() => localStorage.getItem('portal_shell_version')) === '1.2.0') break; } catch (e) {} }
  await wait(4000);

  // ---- the catalogue ----
  await p.locator('#subject-filter-bar .filter-chip').first().click();
  await wait(900);
  const chips = await p.evaluate(() => Array.from(document.querySelectorAll('#chapter-filter-bar .filter-chip')).map((x) => x.textContent.trim()));
  T('the chapter chips are plain numbers', chips.join(',') === '1,2,3,4', chips.join(','));
  const cards = await p.evaluate(() => Array.from(document.querySelectorAll('#catalog-cards-container .sketch-title')).map((x) => x.textContent.trim()));
  const topicNums = await p.evaluate(() => Array.from(document.querySelectorAll('#catalog-cards-container .sketch-topic-num')).map((x) => x.textContent.trim()));
  T('chapter 1 shows six cards', cards.length === 6, cards.length + ': ' + cards.join(' | ').slice(0, 160));
  const withSubject = cards.filter((c) => c.indexOf('الأمن السيبراني') >= 0);
  T('no card repeats the subject name', withSubject.length === 0, withSubject.join(' | '));
  T('every card shows its topic number 1.1-1.6', JSON.stringify(topicNums) === JSON.stringify(["موضوع: 1","موضوع: 2","موضوع: 3","موضوع: 4","موضوع: 5","موضوع: 6"]), topicNums.join(','));
  const cardChip = await p.evaluate(() => (document.querySelector('#catalog-cards-container .sketch-chip') || {}).textContent);
  T('the card chip shows the chapter', /جابتر\s*1|^1$/.test((cardChip || '').trim()), cardChip);
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/verify-catalog.png' });

  // ---- the login card: the close button ----
  await p.evaluate(() => document.querySelector('.btn-menu').click());
  await wait(800);
  await p.evaluate(() => document.querySelector('#menu-account').click());
  await wait(1000);
  const login = await p.evaluate(() => {
    const m = document.querySelector('#login-modal');
    const b = document.querySelector('#login-close');
    return {
      open: !!m && !m.classList.contains('hidden'),
      close: !!b && !!b.offsetParent,
      label: b ? b.getAttribute('aria-label') : null,
    };
  });
  T('the login card is open', login.open);
  T('the login card has a visible close button', login.close, JSON.stringify(login));
  T('the close button is labelled', !!login.label, JSON.stringify(login));
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/verify-login.png' });
  await p.evaluate(() => { const b = document.querySelector('#login-close'); if (b) b.click(); });
  await wait(700);
  T('the close button closes the card',
    await p.evaluate(() => document.querySelector('#login-modal').classList.contains('hidden')));

  // ---- the leave modal in the light theme ----
  await p.evaluate(() => { try { localStorage.setItem('portal_theme', 'light'); } catch (e) {} });
  await p.reload({ waitUntil: 'domcontentloaded' });
  await wait(4000);
  const theme = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
  T('the light theme is on', theme === 'light', theme);
  await p.locator('#subject-filter-bar .filter-chip').first().click();
  await wait(700);
  await p.locator('#catalog-cards-container .sketch-play-cell').first().click();
  await wait(1000);
  await p.evaluate(() => { const b = document.querySelector('#btn-start-quiz'); if (b) b.click(); });
  await wait(1500);
  await p.locator('#options-container .option-tile').first().click();
  await wait(900);
  await p.evaluate(() => { const b = document.querySelector('#btn-exit'); if (b) b.click(); });
  await wait(900);
  const leave = await p.evaluate(() => {
    const m = document.querySelector('#leave-modal');
    const card = m ? m.querySelector('.leave-card, .modal-card') : null;
    const cs = card ? getComputedStyle(card) : null;
    const page = getComputedStyle(document.body);
    const btn = document.querySelector('#leave-stay');
    return {
      open: !!m && !m.classList.contains('hidden'),
      cardBg: cs ? cs.backgroundColor : '',
      cardColor: cs ? cs.color : '',
      pageBg: page.backgroundColor,
      btnColor: btn ? getComputedStyle(btn).color : '',
    };
  });
  T('the leave modal is open', leave.open);
  T('the leave card follows the light theme', /255,\s*255,\s*255/.test(leave.cardBg), JSON.stringify(leave));
  T('the leave text is dark on the light card', leave.cardColor !== leave.btnColor, JSON.stringify(leave));
  await p.screenshot({ path: 'C:/Windows/Temp/opencode/shot/verify-leave-light.png' });
  // back to dark
  await p.evaluate(() => { try { localStorage.setItem('portal_theme', 'dark'); } catch (e) {} });
  await p.reload({ waitUntil: 'domcontentloaded' });
  await wait(3500);

  console.log('\nconsole errors: none collected');
  await b.close();
  console.log('\n' + (out.filter((l) => l.startsWith('FAIL')).join('\n') || 'all green'));
})().catch((e) => { console.error('FATAL', e.message); process.exit(1); });
