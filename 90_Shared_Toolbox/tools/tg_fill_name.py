from playwright.sync_api import sync_playwright
import time, sys
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
time.sleep(1)
inp = pg.locator('input[aria-label="Group name"]')
inp.click()
time.sleep(0.5)
inp.fill("Master-Studio FINAL")
time.sleep(0.5)
print("VAL=" + inp.input_value())
# find next/create button state
info = pg.evaluate("""() => {
  const btns = [...document.querySelectorAll('button')].map(e=>({t:(e.getAttribute('aria-label')||e.title||e.innerText||'').trim().slice(0,60), dis:e.disabled, cls:(e.className||'').toString().slice(0,80)}));
  return {body:(document.body.innerText||'').slice(0,500), btns:btns.slice(-15)};
}""")
print("BODY:" + info["body"][:400])
for x in info["btns"]:
    print("B|" + str(x))
p.stop()
