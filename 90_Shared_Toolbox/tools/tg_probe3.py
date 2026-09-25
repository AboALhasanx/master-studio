from playwright.sync_api import sync_playwright
import time
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
time.sleep(1)
info = pg.evaluate("""() => {
  const ce = [...document.querySelectorAll('[contenteditable=true]')].map(e => ({txt:(e.innerText||'').slice(0,60), ph:e.getAttribute('placeholder')||e.getAttribute('data-placeholder')||'', vis:e.offsetParent!==null, cls:(e.className||'').toString().slice(0,60)}));
  // find element containing 'Group name' and its siblings
  const all = [...document.querySelectorAll('*')].filter(e => e.childElementCount===0 && (e.innerText||'').trim()==='Group name');
  const gn = all.map(e => { const r=e.getBoundingClientRect(); const sib=e.parentElement?e.parentElement.innerHTML.slice(0,500):''; return {rect:[Math.round(r.x),Math.round(r.y),Math.round(r.width),Math.round(r.height)], sib}; });
  // next-step buttons (arrow / create / next)
  const btns = [...document.querySelectorAll('button, [role=button]')].map(e=>({t:(e.getAttribute('aria-label')||e.title||e.innerText||'').trim().slice(0,50), vis:e.offsetParent!==null})).filter(x=>x.t);
  return {ce:ce.slice(0,10), gn:gn.slice(0,3), btns:btns.slice(0,30)};
}""")
print("---CONTENTEDITABLE---")
for c in info["ce"]:
    print("CE|" + str(c))
print("---GROUPNAME NODES---")
for g in info["gn"]:
    print("GN|" + str(g)[:600])
print("---BUTTONS(all)---")
for x in info["btns"]:
    print("B|" + str(x))
p.stop()
