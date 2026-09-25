from playwright.sync_api import sync_playwright
import time
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
time.sleep(1)
info = pg.evaluate("""() => {
  // middle column header (open chat title)
  const mid = document.querySelector('#column-center, [class*=MiddleColumn], [class*=middle]');
  const hdr = mid ? (mid.innerText||'').slice(0,300) : 'NO_MID';
  // left list first items
  const left = document.querySelector('#column-left');
  const items = left ? [...left.querySelectorAll('a, [role=listitem], li')].slice(0,12).map(e=>(e.innerText||'').trim().slice(0,80).replace(/\\n/g,' | ')) : [];
  // search our group
  const all = (document.body.innerText||'');
  const hasGroup = all.includes('Master-Studio FINAL');
  return {hdr, items, hasGroup};
}""")
print("HAS_GROUP=" + str(info["hasGroup"]))
print("---OPEN CHAT HEADER---")
print(str(info["hdr"])[:400])
print("---LEFT LIST---")
for it in info["items"][:12]:
    print("L|" + it[:100])
p.stop()
