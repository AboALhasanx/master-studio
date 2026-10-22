const { chromium } = require("playwright-core");
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const out = [];
const T = (n, c, x = "") => { out.push(`${c ? "PASS" : "FAIL"} ${n}${!c && x ? " :: " + x : ""}`); console.log(out[out.length - 1]); };
(async () => {
  const b = await chromium.connectOverCDP("http://127.0.0.1:9222");
  const ctx = b.contexts()[0];
  let p = null;
  try { p = ctx.pages().find((x) => x.url().indexOf("mcq-portal") >= 0); if (p) await p.evaluate(() => 1); } catch (e) { p = null; }
  if (!p) p = await ctx.newPage();
  await p.bringToFront();
  await p.goto("https://mcq-portal-jade.vercel.app/?t=" + Date.now(), { waitUntil: "domcontentloaded", timeout: 45000 }).catch(() => {});
  for (let i = 0; i < 25; i++) { await wait(1000); try { if (await p.evaluate(() => localStorage.getItem("portal_shell_version")) === "1.3.1") break; } catch (e) {} }
  T("tablet runs 1.3.1", (await p.evaluate(() => localStorage.getItem("portal_shell_version"))) === "1.3.1");
  await p.waitForFunction(() => window.PortalApp && window.PortalApp.bankCount() > 0, null, { timeout: 40000 });
  await wait(1500);
  // the toggle must be visible on the home bar
  const home = await p.evaluate(() => {
    const b = document.querySelector("#lang-toggle-catalog");
    return { vis: !!b && !!b.offsetParent, yellow: b ? b.className.indexOf("lang-active") >= 0 : null };
  });
  T("the icon is fixed on the home bar too", home.vis, JSON.stringify(home));
  // and on every other bar
  for (const h of ["#/saved", "#/stats", "#/league", "#/account"]) {
    await p.evaluate((x) => { location.hash = x; }, h);
    await wait(1200);
    const v = await p.evaluate(() => !!document.querySelector("#lang-toggle-catalog") && !!document.querySelector("#lang-toggle-catalog").offsetParent);
    T("visible on " + h, v);
  }
  // toggle still works from home
  await p.evaluate(() => { location.hash = "#/"; });
  await wait(900);
  await p.locator("#lang-toggle-catalog").click();
  await wait(600);
  const st = await p.evaluate(() => ({
    cls: document.querySelector("#lang-toggle-catalog").className,
    lang: document.documentElement.getAttribute("lang"),
    qlang: document.documentElement.getAttribute("data-qlang"),
  }));
  T("tapping it on home toggles the language", /lang-active/.test(st.cls) === (st.lang === "ar"), JSON.stringify(st));
  await p.screenshot({ path: "C:/Windows/Temp/opencode/shot/tablet-lang-home.png" });
  // back to Arabic for the student
  const cur = await p.evaluate(() => document.querySelector("#lang-toggle-catalog").className);
  if (cur.indexOf("lang-active") < 0) { await p.locator("#lang-toggle-catalog").click(); await wait(500); }
  await b.close();
  console.log("\n" + (out.filter((l) => l.startsWith("FAIL")).join("\n") || "all green"));
})().catch((e) => { console.error("FATAL", e.message); process.exit(1); });
