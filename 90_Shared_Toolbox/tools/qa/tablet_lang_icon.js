const { chromium } = require("playwright-core");
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const out = [];
const T = (n, c, x = "") => { out.push(`${c ? "PASS" : "FAIL"} ${n}${!c && x ? " :: " + x : ""}`); console.log(out[out.length - 1]); };
(async () => {
  const b = await chromium.connectOverCDP("http://127.0.0.1:9222");
  const ctx = b.contexts()[0];
  let p = ctx.pages().find((x) => { try { return x.url().indexOf("mcq-portal") >= 0; } catch (e) { return false; } });
  try { if (p) await p.evaluate(() => 1); else p = null; } catch (e) { p = null; }
  if (!p) { p = await ctx.newPage(); }
  await p.bringToFront();
  const errs = [];
  p.on("pageerror", (e) => errs.push(e.message.split("\n")[0]));
  await p.goto("https://mcq-portal-jade.vercel.app/?t=" + Date.now(), { waitUntil: "domcontentloaded", timeout: 45000 }).catch(() => {});
  for (let i = 0; i < 25; i++) { await wait(1000); try { if (await p.evaluate(() => localStorage.getItem("portal_shell_version")) === "1.3.0") break; } catch (e) {} }
  T("tablet runs 1.3.0", (await p.evaluate(() => localStorage.getItem("portal_shell_version"))) === "1.3.0");
  await p.waitForFunction(() => window.PortalApp && window.PortalApp.bankCount() > 0, null, { timeout: 40000 });
  await wait(1500);

  // the old pill switch must be gone, the icon toggle present before the bell
  const bar = await p.evaluate(() => ({
    oldPill: document.querySelectorAll(".lang-switch, .lang-opt").length,
    toggle: !!document.querySelector("#lang-toggle-catalog") && !!document.querySelector("#lang-toggle-session"),
    order: Array.from(document.querySelectorAll("#header-catalog-view .header-right > *")).filter((x) => x.offsetParent).map((x) => x.id || x.className),
    sesOrder: Array.from(document.querySelectorAll("#header-session-view .header-right > *")).map((x) => x.id || x.className),
  }));
  T("the old pill switch is gone", bar.oldPill === 0, JSON.stringify(bar.oldPill));
  T("the icon toggle exists in both headers", bar.toggle);
  console.log("catalog order:", JSON.stringify(bar.order));
  console.log("session order:", JSON.stringify(bar.sesOrder));
  T("the toggle sits before the bell", bar.sesOrder.indexOf("lang-toggle-session") < bar.sesOrder.indexOf("btn-bell-session"), JSON.stringify(bar.sesOrder));

  // start a quiz: the icon is yellow in Arabic mode
  await p.locator("#subject-filter-bar .filter-chip").nth(5).click();
  await wait(600);
  await p.locator("#catalog-cards-container .sketch-play-cell").first().click();
  await wait(1100);
  await p.click("#btn-start-quiz");
  await p.waitForSelector("#options-container .option-tile", { timeout: 20000 });
  await wait(500);
  // normalize to a known state first (the tablet may remember English)
  const cur = await p.evaluate(() => document.querySelector("#lang-toggle-session").className);
  if (cur.indexOf("lang-active") < 0) { await p.locator("#lang-toggle-session").click(); await wait(700); }
  const ar = await p.evaluate(() => ({
    cls: document.querySelector("#lang-toggle-session").className,
    label: document.querySelector("#lang-toggle-session").getAttribute("aria-label"),
    letters: document.querySelector(".option-letter").textContent.trim(),
  }));
  T("the icon is yellow in Arabic mode", ar.cls.indexOf("lang-active") >= 0 && ar.letters === "أ", JSON.stringify(ar));
  await p.locator("#lang-toggle-session").click();
  await wait(700);
  const en = await p.evaluate(() => ({
    cls: document.querySelector("#lang-toggle-session").className,
    letters: document.querySelector(".option-letter").textContent.trim(),
  }));
  T("tapping it switches to English and goes plain white", en.cls.indexOf("lang-active") < 0 && en.letters === "A", JSON.stringify(en));
  await p.locator("#lang-toggle-session").click();
  await wait(500);
  await p.screenshot({ path: "C:/Windows/Temp/opencode/shot/tablet-lang-icon.png" });

  // refresh on the quiz URL: the header and the icon must be right at once
  await p.goto("https://mcq-portal-jade.vercel.app/#/quiz/06_Artificial_Intelligence/Quiz_Ch01_ModelA_AI_Foundations?t=" + Date.now(), { waitUntil: "domcontentloaded", timeout: 45000 }).catch(() => {});
  await wait(1200);
  const flash = await p.evaluate(() => ({
    shell: localStorage.getItem("portal_shell_version"),
    header: [...document.querySelectorAll(".header-inner")].filter((x) => x.offsetParent).map((x) => x.id),
    iconYellow: (document.querySelector("#lang-toggle-session") || { className: "" }).className.indexOf("lang-active") >= 0,
    oldPill: document.querySelectorAll(".lang-switch, .lang-opt").length,
  }));
  T("after refresh the session header shows at once", JSON.stringify(flash.header) === JSON.stringify(["header-session-view"]), JSON.stringify(flash));
  T("no old pill after refresh", flash.oldPill === 0);
  console.log("errors:", errs.length, errs.slice(0, 3).join(" | "));
  await b.close();
  console.log("\n" + (out.filter((l) => l.startsWith("FAIL")).join("\n") || "all green"));
})().catch((e) => { console.error("FATAL", e.message); process.exit(1); });
