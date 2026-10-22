# -*- coding: utf-8 -*-
"""Cross-device sync check (merge semantics): the same account on the computer
and the tablet, two devices editing while apart, a second account for isolation.

Run from a shell:
    adb forward tcp:9222 localabstract:chrome_devtools_remote
    python 90_Shared_Toolbox/tools/qa/sync_cross_device.py
"""
import json
import os
import sys
import time

TESTS = r'C:\Users\gokoq\mcq-portal\tests'
sys.path.insert(0, TESTS)

os.environ.setdefault('PORTAL_BASE_URL', 'https://mcq-portal-jade.vercel.app')

import common  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

TABLET_HANDLE = 'tab023740'
TABLET_PIN = '4271'
TABLET_NAME = 'طالب التابلت'
NEW_HANDLE = 'syncqa%d' % (int(time.time()) % 100000)
NEW_PIN = '1111'
BASE = 'https://mcq-portal-jade.vercel.app'

out = []


def T(name, ok, note=''):
    out.append((name, bool(ok), str(note)))
    print(('PASS ' if ok else 'FAIL ') + name + (('  :: ' + str(note)[:150]) if (note and not ok) else ''), flush=True)


def state(page):
    return page.evaluate("""() => {
      const j = (k, d) => { try { return JSON.parse(localStorage.getItem(k) || d); } catch (e) { return d; } };
      const acc = j('portal_account_v1', null);
      const bests = {};
      for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k && k.indexOf('portal_best_') === 0) bests[k.replace('portal_best_', '')] = j(k, {}); }
      return {
        handle: acc ? acc.handle : null,
        id: acc ? acc.id : null,
        history: (j('portal_history_v1', []) || []).length,
        saved: Object.keys(j('portal_saved_v1', {}) || {}),
        bests: bests,
        touched: Number(localStorage.getItem('portal_data_touched_v1') || 0),
      };
    }""")


def pull(page):
    return page.evaluate("() => window.PortalCloud.pullOrPush()")


def remote(page):
    return page.evaluate("() => window.PortalCloud.download()")


def settle(page, seconds=6):
    for _ in range(seconds):
        page.wait_for_timeout(1000)
        try:
            page.evaluate("() => 1")
        except Exception:
            pass


def wait_app(page):
    page.wait_for_function("() => window.PortalApp && window.PortalApp.bankCount() > 0", timeout=60000)
    page.wait_for_timeout(1200)


def login(page, handle, pin, name):
    page.evaluate("() => document.querySelector('.btn-menu').click()")
    page.wait_for_timeout(500)
    page.evaluate("() => document.querySelector('#menu-account').click()")
    page.wait_for_timeout(800)
    page.wait_for_selector('#login-modal:not(.hidden)', timeout=15000)
    page.fill('#login-name', name)
    page.fill('#login-handle', handle)
    page.fill('#login-pin', pin)
    page.evaluate("() => document.querySelector('#login-submit').click()")
    page.wait_for_timeout(5200)
    return page.evaluate("() => window.PortalCloud.account()")


def logout(page):
    page.evaluate("() => document.querySelector('.btn-menu').click()")
    page.wait_for_timeout(500)
    page.evaluate("() => document.querySelector('#menu-account').click()")
    page.wait_for_timeout(900)
    page.evaluate("() => document.querySelector('#account-logout').click()")
    page.wait_for_timeout(900)


def go_home(page):
    page.evaluate("() => { location.hash = '#/'; }")
    page.wait_for_timeout(700)
    if page.locator('#leave-modal').is_visible():
        page.click('#leave-go')
        page.wait_for_timeout(800)
    page.evaluate("""() => {
      document.querySelectorAll('.modal-overlay:not(.hidden)').forEach((m) => { const c = m.querySelector('.icon-btn'); if (c) c.click(); });
      document.querySelectorAll('.drawer.open').forEach((d) => { const c = d.querySelector('.icon-btn'); if (c) c.click(); });
      document.querySelectorAll('.portal-toast').forEach((t) => t.remove());
      location.hash = '#/';
    }""")
    page.wait_for_timeout(1000)


def save_question(page, which=0):
    """Open the AI subject, start the `which`-th quiz, bookmark one question."""
    for attempt in range(3):
        go_home(page)
        page.locator('#subject-filter-bar .filter-chip').nth(5).wait_for(state='visible', timeout=15000)
        page.locator('#subject-filter-bar .filter-chip').nth(5).click()
        page.wait_for_timeout(600)
        page.evaluate("() => document.querySelectorAll('.portal-toast').forEach((t) => t.remove())")
        page.locator('#catalog-cards-container .sketch-play-cell').nth(which).wait_for(state='visible', timeout=15000)
        page.locator('#catalog-cards-container .sketch-play-cell').nth(which).click()
        page.wait_for_timeout(1100)
        page.wait_for_selector('#btn-start-quiz', state='visible', timeout=15000)
        page.click('#btn-start-quiz')
        page.wait_for_selector('#options-container .option-tile', timeout=20000)
        page.evaluate("() => document.querySelectorAll('.portal-toast').forEach((t) => t.remove())")
        page.click('#btn-save-question')
        page.wait_for_timeout(900)
        keys = page.evaluate("() => Object.keys(JSON.parse(localStorage.getItem('portal_saved_v1') || '{}'))")
        if keys:
            page.evaluate("() => { const x = document.querySelector('#btn-exit'); if (x) x.click(); }")
            page.wait_for_timeout(700)
            if page.locator('#leave-modal').is_visible():
                page.click('#leave-go')
                page.wait_for_timeout(900)
            return keys[-1]
        page.evaluate("() => { const x = document.querySelector('#btn-exit'); if (x) x.click(); }")
        page.wait_for_timeout(700)
        if page.locator('#leave-modal').is_visible():
            page.click('#leave-go')
            page.wait_for_timeout(900)
    return None


def reset_data(page):
    """Empty this device and make the empty state win on the next merge."""
    page.evaluate("""() => {
      const saved = JSON.parse(localStorage.getItem('portal_saved_v1') || '{}');
      const removed = {};
      Object.keys(saved).forEach((k) => { removed[k] = Date.now(); });
      localStorage.setItem('portal_saved_removed_v1', JSON.stringify(removed));
      localStorage.setItem('portal_history_cleared_v1', String(Date.now()));
      localStorage.removeItem('portal_history_v1');
      localStorage.removeItem('portal_saved_v1');
      for (let i = localStorage.length - 1; i >= 0; i--) {
        const k = localStorage.key(i);
        if (k && k.indexOf('portal_best_') === 0) localStorage.removeItem(k);
      }
      localStorage.setItem('portal_data_touched_v1', String(Date.now() + 1000));
    }""")


def main():
    pw = sync_playwright().start()
    try:
        # ---- the tablet ----
        tb = pw.chromium.connect_over_cdp('http://127.0.0.1:9222')
        tctx = tb.contexts[0]
        tpage = next((x for x in tctx.pages if 'mcq-portal' in x.url), None)
        if tpage is None:
            tpage = tctx.new_page()
            tpage.goto(BASE + '/', wait_until='domcontentloaded', timeout=45000)
        tpage.bring_to_front()
        wait_app(tpage)
        settle(tpage, 6)   # a worker update may reload once; let it finish
        tst = state(tpage)
        T('the tablet is signed in', tst['handle'] == TABLET_HANDLE, tst)

        # clean slate
        reset_data(tpage)
        pull(tpage)
        T('the tablet starts empty', len(state(tpage)['saved']) == 0 and state(tpage)['history'] == 0, state(tpage))

        # ---- the computer, same account ----
        browser, cpage, errors = common.new_page(pw, tour_done=True, telegram=None)
        cpage.goto(common.APP, wait_until='domcontentloaded', timeout=60000)
        wait_app(cpage)
        acc = login(cpage, TABLET_HANDLE, TABLET_PIN, TABLET_NAME)
        T('the computer signs in with the tablet handle + PIN', bool(acc and acc['id'] == tst['id']), acc)
        reset_data(cpage)
        pull(cpage)
        cst = state(cpage)
        T('the computer starts empty too', len(cst['saved']) == 0 and cst['history'] == 0, cst)

        # ---- each device edits while apart ----
        key_a = save_question(tpage, 0)
        pull(tpage)
        T('the tablet saves its own bookmark', bool(key_a), key_a)

        key_b1 = save_question(cpage, 0)
        key_b2 = save_question(cpage, 1)
        T('the computer saves two different bookmarks', bool(key_b1 and key_b2 and key_b1 != key_b2), [key_b1, key_b2])

        # the computer has not seen the tablet's save yet: its merge must keep both
        pull(cpage)
        cst = state(cpage)
        T('the merge keeps the tablet bookmark and adds the computer ones',
          key_a in cst['saved'] and key_b1 in cst['saved'] and key_b2 in cst['saved'],
          'tablet=%s b1=%s b2=%s have=%s' % (key_a, key_b1, key_b2, cst['saved']))

        pull(tpage)
        tst = state(tpage)
        T('the tablet receives both computer bookmarks without losing its own',
          all(k in tst['saved'] for k in (key_a, key_b1, key_b2)), tst['saved'])

        # ---- best score merges to the higher value ----
        cpage.evaluate("() => localStorage.setItem('portal_best_merge_probe', JSON.stringify({ pct: 55, frac: '11 / 20' }))")
        tpage.evaluate("() => localStorage.setItem('portal_best_merge_probe', JSON.stringify({ pct: 80, frac: '16 / 20' }))")
        pull(cpage)
        pull(tpage)
        pull(cpage)
        cst = state(cpage)
        T('the best score keeps the higher value', (cst['bests'].get('merge_probe') or {}).get('pct') == 80, cst['bests'].get('merge_probe'))
        cpage.evaluate("() => localStorage.removeItem('portal_best_merge_probe')")
        tpage.evaluate("() => localStorage.removeItem('portal_best_merge_probe')")

        # ---- unsave propagates as a removal ----
        cpage.evaluate("""(key) => {
          const s = JSON.parse(localStorage.getItem('portal_saved_v1') || '{}');
          delete s[key];
          const m = JSON.parse(localStorage.getItem('portal_saved_removed_v1') || '{}');
          m[key] = Date.now();
          localStorage.setItem('portal_saved_v1', JSON.stringify(s));
          localStorage.setItem('portal_saved_removed_v1', JSON.stringify(m));
          localStorage.setItem('portal_data_touched_v1', String(Date.now() + 1000));
        }""", key_b2)
        pull(cpage)
        pull(tpage)
        tst = state(tpage)
        T('an unsave on one device removes it on the other', key_b2 not in tst['saved'] and key_a in tst['saved'], tst['saved'])

        # ---- clear history propagates ----
        cpage.evaluate("""() => {
          localStorage.removeItem('portal_history_v1');
          localStorage.setItem('portal_history_cleared_v1', String(Date.now()));
          localStorage.setItem('portal_data_touched_v1', String(Date.now() + 1000));
        }""")
        pull(cpage)
        pull(tpage)
        T('clearing the history on one device clears it on the other', state(tpage)['history'] == 0, state(tpage))

        # ---- a second account is isolated ----
        logout(cpage)
        cpage.wait_for_timeout(800)
        acc2 = login(cpage, NEW_HANDLE, NEW_PIN, 'حساب ثاني')
        T('the second account signs in', bool(acc2 and acc2['id'] != (acc or {}).get('id')), acc2)
        cst2 = state(cpage)
        T('the second account starts empty', len(cst2['saved']) == 0 and cst2['history'] == 0, cst2)
        key_new = save_question(cpage, 0)
        pull(cpage)
        srv_new = remote(cpage) or {}
        T('the second account keeps its own bookmark row', len(srv_new.get('saved') or {}) >= 1, len(srv_new.get('saved') or {}))

        logout(cpage)
        cpage.wait_for_timeout(800)
        login(cpage, TABLET_HANDLE, TABLET_PIN, TABLET_NAME)
        pull(cpage)
        cst = state(cpage)
        T('switching back restores the first account', key_a in cst['saved'] and key_new not in cst['saved'], cst['saved'])
        T('no runtime errors on the computer', not errors, errors[:2])

        # ---- cleanup: leave the account empty on both sides ----
        reset_data(cpage)
        pull(cpage)
        reset_data(tpage)
        pull(tpage)
        T('the account is cleared again', len(state(tpage)['saved']) == 0 and state(tpage)['history'] == 0, state(tpage))
        browser.close()
    except Exception as exc:
        print('FATAL', exc, flush=True)
        return 1
    finally:
        try:
            pw.stop()
        except Exception:
            pass

    failed = [o for o in out if not o[1]]
    print('\n=== cross-device sync (merge) ===')
    print('%d checks, %d failed' % (len(out), len(failed)))
    for name, ok, note in failed:
        print('  FAIL', name, '::', note)
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
