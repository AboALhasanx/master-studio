from playwright.sync_api import sync_playwright
import time
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
time.sleep(1)
# Click "Continue To Group Info" arrow via JS (element reports invisible to PW)
pg.evaluate("() => { const el=[...document.querySelectorAll('button')].find(e=>(e.getAttribute('aria-label')||'')==='Continue To Group Info'); if(el){el.click(); return 'JS_CLICK_OK';} return 'NOT_FOUND'; }")
print("JS_CLICK_SENT")
time.sleep(2)
info = pg.evaluate("() => { return (document.body.innerText||'').slice(0,800); }")
print("AFTER_CONTINUE:")
print(info[:700])
# Now click Create Group
try:
    r = pg.evaluate("() => { const el=[...document.querySelectorAll('button')].find(e=>(e.getAttribute('aria-label')||'')==='Create Group'); if(el){el.click(); return 'JS_CREATE_OK';} return 'NOT_FOUND'; }")
    print("CREATE:" + str(r))
except Exception as e:
    print("CREATE_CLICK_FAIL " + str(e)[:200])
time.sleep(3)
info2 = pg.evaluate("() => { return {body:(document.body.innerText||'').slice(0,800), url:location.href}; }")
print("---AFTER_CREATE---")
print(info2["body"][:700])
print("URL=" + info2["url"])
p.stop()
