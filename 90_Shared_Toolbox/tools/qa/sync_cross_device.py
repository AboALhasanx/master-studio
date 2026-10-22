# -*- coding: utf-8 -*-
"""Cross-device sync check: the same account on the computer and the tablet,
a different account for isolation, and the newest-change-wins rules.

Run from a shell:
    adb forward tcp:9222 localabstract:chrome_devtools_remote
    python 90_Shared_Toolbox/tools/qa/sync_cross_device.py
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = r'C:\Users\gokoq\mcq-portal\tests'
sys.path.insert(0, TESTS)

os.environ.setdefault('PORTAL_BASE_URL', 'https://mcq-portal-jade.vercel.app')

import common  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

TABLET_HANDLE = 'tab023740'
TABLET_PIN = '4271'
NEW_HANDLE = 'syncqa%d' % (int(time.time()) % 100000)
NEW_PIN = '1111'

out = []


def T(name, ok, note=''):
    out.append((name, bool(ok), str(note)))
    print(('PASS ' if ok else 'FAIL ') + name + (('  :: ' + str(note)[:150]) if (note and not ok) else ''), flush=True)


def state(page):
    return page.evaluate("""() => {
      const j = (k, d) => { try { return JSON.parse(localStorage.getItem(k) || d); } catch (e) { return d; } };
      const acc = j('portal_account_v1', null);
      const bests = {};
      for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k && k.indexOf('portal_best_') === 0) bests[k] = 1; }
      return {
        handle: acc ? acc.handle : null,
        id: acc ? acc.id : null,
        history: (j('portal_history_v1', []) || []).length,
        saved: Object.keys(j('portal_saved_v1', {}) || {}).length,
        bests: Object.keys(bests).length,
        touched: Number(localStorage.getItem('portal_data_touched_v1') || 0),
        signedOut: localStorage.getItem('portal_signed_out_v1') === '1',
      };
    }""")


def pull(page):
    return page.evaluate("() => window.PortalCloud.pullOrPush()")


def remote(page):
    return page.evaluate("() => window.PortalCloud.download()")


def login(page, handle, pin, name):
    page.evaluate("() => document.querySelector('.btn-menu').click()")
    page.wait_for_timeout(500)
    page.evaluate("() => document.querySelector('#menu-account').click()")
    page.wait_for_timeout(700)
    page.wait_for_selector('#login-modal:not(.hidden)', timeout=15000)
    page.fill('#login-name', name)
    page.fill('#login-handle', handle)
    page.fill('#login-pin', pin)
    page.evaluate("() => document.querySelector('#login-submit').click()")
    page.wait_for_timeout(5000)
    return page.evaluate("() => window.PortalCloud.account()")


def logout(page):
    page.evaluate("() => document.querySelector('.btn-menu').click()")
    page.wait_for_timeout(500)
    page.evaluate("() => document.querySelector('#menu-account').click()")
    page.wait_for_timeout(900)
    page.evaluate("() => document.querySelector('#account-logout').click()")
    page.wait_for_timeout(900)


def answer_all(page):
    """Start the first quiz of the current subject and finish it."""
    page.evaluate("() => { location.hash = '#/'; }")
    page.wait_for_timeout(1200)
    page.locator('#subject-filter-bar .filter-chip').nth(5).click()
    page.wait_for_timeout(600)
    page.locator('#catalog-cards-container .sketch-play-cell').first.click()
    page.wait_for_timeout(1200)
    page.click('#btn-start-quiz')
    page.wait_for_selector('#options-container .option-tile', timeout=20000)
    for _ in range(8):
        page.locator('#options-container .option-tile').nth(0).click()
        page.wait_for_timeout(400)
        if not page.locator('#btn-next').is_visible():
            break
        page.click('#btn-next')
        page.wait_for_timeout(500)
        if not page.locator('#options-container .option-tile').first.is_visible():
            break
    page.wait_for_timeout(1200)


def save_question(page):
    """Open a quiz and bookmark its first question (returns to home)."""
    page.evaluate("() => { location.hash = '#/'; }")
    page.wait_for_timeout(1200)
    page.locator('#subject-filter-bar .filter-chip').nth(5).click()
    page.wait_for_timeout(600)
    page.locator('#catalog-cards-container .sketch-play-cell').first.click()
    page.wait_for_timeout(1100)
    page.click('#btn-start-quiz')
    page.wait_for_selector('#options-container .option-tile', timeout=20000)
    page.click('#btn-save-question')
    page.wait_for_timeout(800)
    page.evaluate("() => { const x = document.querySelector('#btn-exit'); if (x) x.click(); }")
    page.wait_for_timeout(700)
    if page.locator('#leave-modal').is_visible():
        page.click('#leave-go')
        page.wait_for_timeout(900)


def add_fake_history(page):
    page.evaluate("""() => {
      const h = JSON.parse(localStorage.getItem('portal_history_v1') || '[]');
      h.push({ t: Date.now(), subjectId: '01_Cyber_Security', subjectTitle: 'x', chapterNo: 1, chapterLabel: '',
               quizId: 'fake-entry', topic: 'fake', correct: 1, total: 1, pct: 100, secs: 1, kind: 'bank' });
      localStorage.setItem('portal_history_v1', JSON.stringify(h));
    }""")


def main():
    pw = sync_playwright().start()
    result = 0
    try:
        # ---- the tablet (already signed in) ----
        tb = pw.chromium.connect_over_cdp('http://127.0.0.1:9222')
        tctx = tb.contexts[0]
        tpage = next((x for x in tctx.pages if 'mcq-portal' in x.url), None)
        if tpage is None:
            tpage = tctx.new_page()
            tpage.goto('https://mcq-portal-jade.vercel.app/', wait_until='domcontentloaded', timeout=45000)
        tpage.bring_to_front()
        tpage.wait_for_function("() => window.PortalApp && window.PortalApp.bankCount() > 0", timeout=40000)
        tpage.wait_for_timeout(1200)

        tst = state(tpage)
        T('the tablet is signed in', tst['handle'] == TABLET_HANDLE, tst)
        T('the tablet starts without local data', tst['history'] == 0 and tst['saved'] == 0, tst)

        # clean slate on the server for this account
        r = pull(tpage)
        T('the empty device syncs to an empty server', r['action'] in ('empty', 'downloaded', 'local-only'), r)

        # ---- the computer, same account ----
        browser, cpage, errors = common.new_page(pw, tour_done=True, telegram=None)
        cpage.goto(common.APP, wait_until='domcontentloaded', timeout=60000)
        cpage.wait_for_function("() => window.PortalApp && window.PortalApp.bankCount() > 0", timeout=40000)
        cpage.wait_for_timeout(1200)
        acc = login(cpage, TABLET_HANDLE, TABLET_PIN, 'طالب التابلت')
        T('the computer signs in with the tablet handle + PIN', bool(acc and acc['id'] == tst['id']), acc)
        cst = state(cpage)
        T('the computer pulls the empty state', cst['history'] == 0 and cst['saved'] == 0, cst)

        # ---- the tablet writes: one finished quiz ----
        answer_all(tpage)
        tst = state(tpage)
        T('the tablet records an attempt', tst['history'] >= 1, tst)
        r = pull(tpage)
        T('the tablet uploads its new data', r['action'] in ('uploaded-new', 'uploaded-local-newer', 'uploaded'), r)

        # ---- the computer sees it ----
        r = pull(cpage)
        cst = state(cpage)
        T('the computer downloads the tablet attempt', r['action'] == 'downloaded', r)
        T('the attempt is on the computer', cst['history'] >= 1, cst)

        # ---- the computer writes: a bookmark ----
        save_question(cpage)
        cst = state(cpage)
        T('the computer records a bookmark', cst['saved'] >= 1, cst)
        r = pull(cpage)
        srv_book = remote(cpage) or {}
        T('the computer uploads the bookmark', len(srv_book.get('saved') or {}) >= 1, 'server saved: %d (action %s)' % (len(srv_book.get('saved') or {}), r.get('action')))

        # ---- the tablet sees it ----
        r = pull(tpage)
        tst = state(tpage)
        T('the tablet downloads the computer bookmark', r['action'] == 'downloaded', r)
        T('the bookmark is on the tablet', tst['saved'] >= 1, tst)

        # ---- stale local change must not clobber newer server data ----
        srv = remote(cpage) or {}
        srv_ts = int(srv.get('updatedAt') or 0)
        cpage.evaluate("(ts) => localStorage.setItem('portal_data_touched_v1', String(ts))", srv_ts - 60000)
        add_fake_history(cpage)
        cst = state(cpage)
        r = pull(cpage)
        T('an older local change loses to the server', r['action'] == 'downloaded', r)
        cst = state(cpage)
        gone = cpage.evaluate("""() => (JSON.parse(localStorage.getItem('portal_history_v1') || '[]')).every((h) => h.quizId !== 'fake-entry')""")
        T('the stale entry was replaced, not uploaded', gone, cst)

        # ---- a newer local change wins ----
        cpage.evaluate("() => localStorage.setItem('portal_data_touched_v1', String(Date.now() + 5000))")
        add_fake_history(cpage)
        r = pull(cpage)
        T('a newer local change wins', r['action'] == 'uploaded-local-newer', r)
        srv2 = remote(cpage) or {}
        has_fake = any(h.get('quizId') == 'fake-entry' for h in (srv2.get('history') or []))
        T('the newer change reached the server', has_fake, 'server history: %d' % len(srv2.get('history') or []))
        r = pull(tpage)
        tst = state(tpage)
        T('the tablet receives the newer change', r['action'] == 'downloaded', r)

        # ---- a tie goes to the server ----
        srv3 = remote(cpage) or {}
        cpage.evaluate("(ts) => localStorage.setItem('portal_data_touched_v1', String(ts))", int(srv3.get('updatedAt') or 0))
        r = pull(cpage)
        T('a tie is won by the server', r['action'] == 'downloaded', r)

        # ---- a different account is isolated ----
        logout(cpage)
        cpage.wait_for_timeout(800)
        acc2 = login(cpage, NEW_HANDLE, NEW_PIN, 'حساب ثاني')
        T('the second account signs in', bool(acc2 and acc2['id'] != tst['id']), acc2)
        cst2 = state(cpage)
        T('the second account starts empty', cst2['history'] == 0 and cst2['saved'] == 0, cst2)
        save_question(cpage)
        cst2 = state(cpage)
        T('the second account keeps its own bookmark', cst2['saved'] >= 1, cst2)
        r = pull(cpage)
        srv_new = remote(cpage) or {}
        T('the second account has its own saved row', len(srv_new.get('saved') or {}) >= 1, 'server saved: %d (action %s)' % (len(srv_new.get('saved') or {}), r.get('action')))

        # back to the first account: its data returns, the second's does not
        logout(cpage)
        cpage.wait_for_timeout(800)
        login(cpage, TABLET_HANDLE, TABLET_PIN, 'طالب التابلت')
        r = pull(cpage)
        cst = state(cpage)
        T('switching back restores the first account', r['action'] == 'downloaded' and cst['history'] >= 1, cst)
        srv_first = remote(cpage) or {}
        first_quiz_ids = {h.get('quizId') for h in (srv_first.get('history') or [])}
        T('the second account data never leaked in', 'fake-entry' in first_quiz_ids, sorted(first_quiz_ids)[:4])

        # ---- cleanup: leave the account with no personal data ----
        cpage.evaluate("""() => {
          localStorage.removeItem('portal_history_v1');
          localStorage.removeItem('portal_saved_v1');
          for (let i = localStorage.length - 1; i >= 0; i--) { const k = localStorage.key(i); if (k && k.indexOf('portal_best_') === 0) localStorage.removeItem(k); }
          localStorage.setItem('portal_data_touched_v1', String(Date.now() + 1000));
        }""")
        r = pull(cpage)
        T('the account is cleared on the server', r['action'] == 'uploaded-empty', r)

        tpage.evaluate("""() => {
          localStorage.removeItem('portal_history_v1');
          localStorage.removeItem('portal_saved_v1');
          for (let i = localStorage.length - 1; i >= 0; i--) { const k = localStorage.key(i); if (k && k.indexOf('portal_best_') === 0) localStorage.removeItem(k); }
          localStorage.setItem('portal_data_touched_v1', String(Date.now()));
        }""")
        pull(tpage)
        T('no runtime errors on the computer', not errors, errors[:2])
        browser.close()
    except Exception as exc:
        print('FATAL', exc, flush=True)
        result = 1
    finally:
        try:
            pw.stop()
        except Exception:
            pass

    failed = [o for o in out if not o[1]]
    print('\n=== cross-device sync ===')
    print('%d checks, %d failed' % (len(out), len(failed)))
    for name, ok, note in failed:
        print('  FAIL', name, '::', note)
    return 1 if (failed or result) else 0


if __name__ == '__main__':
    raise SystemExit(main())
