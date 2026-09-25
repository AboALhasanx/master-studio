from playwright.sync_api import sync_playwright
import time
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
time.sleep(1)
# dump modal inputs
info = pg.evaluate("""() => {
  const modals = [...document.querySelectorAll('[class*=modal], [class*=Modal], [class*=popup], [class*=Popup]')].map(m => (m.innerText||'').slice(0,400));
  const inputs = [...document.querySelectorAll('input')].map(i => ({type:i.type, ph:i.placeholder||'', val:(i.value||'').slice(0,60), vis:i.offsetParent!==null}));
  return {modals, inputs, body:(document.body.innerText||'').slice(0,600)};
}""")
print("BODY:" + info["body"][:500])
print("---MODALS---")
for m in info["modals"][:5]:
    print("MODAL|" + m[:300])
print("---INPUTS---")
for i in info["inputs"][:15]:
    print("INP|" + str(i))
p.stop()
