from playwright.sync_api import sync_playwright
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
info = pg.evaluate("() => { return { body: (document.body.innerText||'').slice(0,1200), title: document.title, url: location.href }; }")
print("TITLE=" + info["title"])
print("URL=" + info["url"])
print("---BODY---")
print(info["body"])
# buttons
btns = pg.evaluate("() => { return [...document.querySelectorAll('button')].slice(0,50).map(e => (e.getAttribute('aria-label')||e.title||e.innerText||'').trim().slice(0,80)); }")
print("---BUTTONS---")
for x in btns:
    print("BTN|" + x)
# left column chat titles
chats = pg.evaluate("() => { const s=[...document.querySelectorAll('[id^=column-left] [class*=row], #column-left li, [class*=dialogs] li')].slice(0,20).map(e=>(e.innerText||'').trim().slice(0,100)); return s; }")
print("---CHATS---")
for c in chats:
    print("CHAT|" + c)
p.stop()
