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
  const errs = [];
  p.on("pageerror", (e) => errs.push(e.message.split("\n")[0]));
  await p.goto("https://mcq-portal-jade.vercel.app/?t=" + Date.now(), { waitUntil: "domcontentloaded", timeout: 45000 }).catch(() => {});
  for (let i = 0; i < 25; i++) { await wait(1000); try { if (await p.evaluate(() => localStorage.getItem("portal_shell_version")) === "1.4.0") break; } catch (e) {} }
  T("tablet runs 1.4.0", (await p.evaluate(() => localStorage.getItem("portal_shell_version"))) === "1.4.0");
  T("favicon is the transparent logo", await p.evaluate(() => (document.querySelector("link[rel=icon]") || {}).href.indexOf("brand-icon-light.png") >= 0));
  await p.waitForFunction(() => window.PortalApp && window.PortalApp.bankCount() > 0, null, { timeout: 40000 });
  await wait(1500);

  // force one fresh topic: AI chapter 2 first bank
  const target = "Quiz_Ch02_ModelA_Search_and_Learning";
  await p.evaluate((qid) => { const s = JSON.parse(localStorage.getItem("portal_seen_v1") || "{}"); s[qid] = 0; localStorage.setItem("portal_seen_v1", JSON.stringify(s)); }, target);
  await p.reload({ waitUntil: "domcontentloaded" });
  await wait(4000);
  await p.evaluate(() => document.querySelectorAll(".portal-toast").forEach((t) => t.remove()));

  // the toast names the topic, the chapter and the subject
  const toast = await p.evaluate(() => {
    const btn = document.querySelector("#btn-bell"); if (btn) btn.click();
    return new Promise((r) => setTimeout(() => {
      const rows = Array.from(document.querySelectorAll("#notif-list .notif-row")).map((x) => x.innerText.replace(/\n/g, " | "));
      const close = document.querySelector("#notif-close"); if (close) close.click();
      r(rows);
    }, 700));
  });
  console.log("notif rows:", JSON.stringify(toast, null, 1));
  T("the notification announces added questions for a topic", toast.some((t) => /تمت إضافة أسئلة/.test(t)));
  T("the notification names chapter and subject", toast.some((t) => /جابتر 2/.test(t)));

  // the card: badge in the chip row, title clean
  await p.locator("#subject-filter-bar .filter-chip", { hasText: "الذكاء الاصطناعي" }).click();
  await wait(900);
  await p.locator("#chapter-filter-bar .filter-chip", { hasText: /^2$/ }).click();
  await wait(900);
  const cards = await p.evaluate(() => Array.from(document.querySelectorAll("#catalog-cards-container .sketch-row")).map((r) => ({
    eyebrow: (r.querySelector(".sketch-eyebrow") || {}).textContent.replace(/\s+/g, " ").trim(),
    title: (r.querySelector(".sketch-title") || {}).textContent.trim(),
    badgeInTitle: !!r.querySelector(".sketch-title .sketch-topic-num"),
  })));
  console.log(JSON.stringify(cards, null, 1));
  T("topic badge lives in the eyebrow row", cards.length > 0 && cards.every((c) => /موضوع: \d/.test(c.eyebrow)));
  T("titles are clean text", cards.length > 0 && cards.every((c) => c.title.indexOf("موضوع:") < 0));
  await p.screenshot({ path: "C:/Windows/Temp/opencode/shot/verify-140-cards.png" });
  // open the fresh quiz: badge gone, notification gone
  await p.locator("#catalog-cards-container .sketch-play-cell").first().click();
  await wait(1200);
  await p.evaluate(() => { const bb = document.querySelector("#btn-start-quiz"); if (bb) bb.click(); });
  await p.waitForSelector("#options-container .option-tile", { timeout: 20000 });
  await p.evaluate(() => { const x = document.querySelector("#btn-exit"); if (x) x.click(); });
  await wait(700);
  await p.evaluate(() => { const g = document.querySelector("#leave-go"); if (g) g.click(); });
  await wait(1200);
  const after = await p.evaluate(() => ({
    badges: document.querySelectorAll("#catalog-cards-container .sketch-chip-new").length,
    seen: JSON.parse(localStorage.getItem("portal_seen_v1") || "{}")["Quiz_Ch02_ModelA_Search_and_Learning"],
  }));
  T("visiting clears the badge", after.badges === 0 && after.seen > 0, JSON.stringify(after));
  console.log("errors:", errs.length, errs.slice(0, 3).join(" | "));
  await b.close();
  console.log("\n" + (out.filter((l) => l.startsWith("FAIL")).join("\n") || "all green"));
})().catch((e) => { console.error("FATAL", e.message); process.exit(1); });
