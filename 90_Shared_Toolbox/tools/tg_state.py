from playwright.sync_api import sync_playwright
import time
p = sync_playwright().start()
b = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
pg = b.contexts[0].pages[0]
pg.bring_to_front()
time.sleep(1)
info = pg.evaluate("""() => {
  const nameInp = document.querySelector('input[aria-label="Group name"]');
  const fabs = [...document.querySelectorAll('button')].filter(e=>(e.className||'').toString().includes('FloatingActionButton')).map(e=>({t:e.getAttribute('aria-label')||e.title||'', dis:e.disabled}));
  const adds = [...document.querySelectorAll('input')].map(i=>({lb:i.getAttribute('aria-label')||i.placeholder||'', v:(i.value||'').slice(0,60)}));
  return {nameVal: nameInp?nameInp.value:'MISSING', fabs, adds:adds.slice(0,6), body:(document.body.innerText||'').slice(0,400)};
}""")
print("NAME_VAL=" + str(info["nameVal"]))
print("FABS=" + str(info["fabs"]))
print("INPUTS=" + str(info["adds"]))
print("BODY:" + str(info["body"])[:350])
p.stop()
