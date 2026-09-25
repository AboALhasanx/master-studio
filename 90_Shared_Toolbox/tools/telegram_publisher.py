"""Master-Studio Telegram FINALs publisher — one tech: playwright-python + debug Chromium :9222."""
import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

CDP = "http://127.0.0.1:9222"
TG_URL = "https://web.telegram.org/a/"

TOPICS = [
    ("00-Start-Here", "Rules + index. Read-only."),
    ("01-Cyber-Security", "CS501 FINALs."),
    ("02-English-Language", "CS502 FINALs."),
    ("03-Data-Mining", "CS602 FINALs."),
    ("04-Advanced-Software-Eng", "CS504 FINALs."),
    ("05-Soft-Computing", "CS603 FINALs."),
    ("06-Artificial-Intelligence", "CS605 FINALs."),
    ("90-Toolbox", "Tools, exporters, dashboard."),
    ("99-Chat", "Discussion only. Open chat."),
]
GROUP_NAME = "Master-Studio FINAL"

def connect():
    p = sync_playwright().start()
    b = p.chromium.connect_over_cdp(CDP)
    ctx = b.contexts[0] if b.contexts else b.new_context()
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    return p, b, ctx, pg

def login_status(pg) -> bool:
    try:
        if "web.telegram.org" not in pg.url:
            pg.goto(TG_URL, wait_until="domcontentloaded")
        time.sleep(2)
        # logged in if chat list or search box present, no QR canvas login screen
        has_login = pg.locator("text=Log in by phone").count() > 0 or pg.locator("text=START MESSAGING").count() > 0
        return not has_login
    except Exception as e:
        print(f"status check failed: {e}")
        return False

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    p, b, ctx, pg = connect()
    try:
        if cmd == "status":
            print("LOGGED_IN" if login_status(pg) else "NEED_LOGIN")
            print(f"url={pg.url}")
        elif cmd == "open":
            pg.goto(TG_URL, wait_until="domcontentloaded")
            print(f"OPENED {pg.url}")
            time.sleep(3600)
    finally:
        p.stop()
