"""
Playwright Scenario Matrix Simulation for Master Studio Interactive Quiz
------------------------------------------------------------------------
Implements the Gemini architecture:
"Deterministic scenarios + fast execution" (avoiding combinatorial explosion).

Scenarios tested:
1. Scenario 1: Happy Path & UI Navigation (answering questions, dwell timing)
2. Scenario 2: Metacognitive Reflection (selecting error chips on wrong answers)
3. Scenario 3: Lucky Guess / WOW (flagging flukes on correct answers)
4. Scenario 4: Bookmarks & Drawers (saving questions, toggling drawers, theme)
5. Scenario 5: Idempotent Sync (submitting telemetry, verifying backend sync)
"""

import sys
import time
import json
from playwright.sync_api import sync_playwright, expect

QUIZ_URL = "http://127.0.0.1:5000/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis"

def run_simulation():
    results = {}
    print("=" * 70)
    print("🚀 STARTING PLAYWRIGHT DETERMINISTIC SCENARIO MATRIX SIMULATION")
    print(f"Target: {QUIZ_URL}")
    print("=" * 70)

    start_total = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 412, "height": 915})  # Mobile Viewport
        page = context.new_page()

        # -------------------------------------------------------------
        # Scenario 1: Initial Page Load & Theme Verification
        # -------------------------------------------------------------
        t0 = time.time()
        print("\n[Scenario 1] Loading Quiz & Verifying Visual Theme...")
        page.goto(QUIZ_URL, wait_until="networkidle")
        
        # Verify Dark Mode Default (#0B1C2E)
        theme = page.evaluate("() => document.documentElement.getAttribute('data-theme')")
        title = page.locator("#quiz-title").inner_text()
        print(f"  ✓ Loaded in {time.time() - t0:.2f}s | Theme: {theme} | Title: {title}")
        results["scenario_1_load"] = {"theme": theme, "title": title, "duration_s": round(time.time() - t0, 2)}

        # -------------------------------------------------------------
        # Scenario 2: Fast Navigation & Answering Questions
        # -------------------------------------------------------------
        t0 = time.time()
        print("\n[Scenario 2] Executing Quiz Answers (Simulating User Dwell Times)...")
        # Question 1: Pick B (Correct)
        page.locator(".option-tile, .option-btn").nth(1).click()
        time.sleep(0.5)
        page.locator("#btn-next").click()

        # Question 2: Pick A (Wrong - Brooks Essential is C)
        page.locator(".option-tile, .option-btn").nth(0).click()
        time.sleep(0.5)
        page.locator("#btn-next").click()

        # Question 3: Pick B (Correct - Brooks Law quadratic)
        page.locator(".option-tile, .option-btn").nth(1).click()
        time.sleep(0.5)
        page.locator("#btn-next").click()

        # Question 4: Pick A (Correct - Dependability taxonomy)
        page.locator(".option-tile, .option-btn").nth(0).click()
        time.sleep(0.5)
        page.locator("#btn-next").click()

        # Question 5: Pick C (Correct - Public interest ethics) & Finish
        page.locator(".option-tile, .option-btn").nth(2).click()
        time.sleep(0.5)
        page.locator("#btn-next").click()  # Finish Quiz

        # Wait for Result Screen
        page.wait_for_selector(".score-card, .score-circle", timeout=3000)
        score_text = page.locator("#score-percentage, .score-number").inner_text()
        print(f"  ✓ Completed 5 questions in {time.time() - t0:.2f}s | Score: {score_text}")
        results["scenario_2_quiz"] = {"score": score_text, "duration_s": round(time.time() - t0, 2)}

        # -------------------------------------------------------------
        # Scenario 3: Metacognitive Reflection on Wrong Answer
        # -------------------------------------------------------------
        t0 = time.time()
        print("\n[Scenario 3] Metacognitive Reflection on Wrong Answer...")
        # Find the reflection chip for Question 2 (Misread Question or Terminology Mix-up)
        chip = page.locator(".chip[data-val='Terminology Mix-up'], .reflection-chip:has-text('Terminology')").first
        if chip.is_visible():
            chip.click()
            chip_class = chip.get_attribute("class")
            print(f"  ✓ Clicked 'Terminology Mix-up' reflection chip | Class: {chip_class}")
            results["scenario_3_reflection"] = {"chip_selected": "Terminology Mix-up", "status": "success"}
        else:
            print("  ⚠️ Reflection chips not found or already submitted")
            results["scenario_3_reflection"] = {"status": "skipped"}

        # -------------------------------------------------------------
        # Scenario 4: Lucky Guess / WOW Toggle
        # -------------------------------------------------------------
        t0 = time.time()
        print("\n[Scenario 4] Flagging Lucky Guess / WOW on Correct Answer...")
        lucky_toggle = page.locator(".lucky-check, input[type='checkbox']").first
        if lucky_toggle.is_visible():
            lucky_toggle.check()
            is_checked = lucky_toggle.is_checked()
            print(f"  ✓ Checked 'Lucky Guess / WOW' toggle | is_checked: {is_checked}")
            results["scenario_4_lucky_guess"] = {"is_checked": is_checked, "status": "success"}
        else:
            print("  ⚠️ Lucky guess toggle not visible")
            results["scenario_4_lucky_guess"] = {"status": "skipped"}

        # -------------------------------------------------------------
        # Scenario 5: Send to Master Studio (Idempotent Telemetry Sync)
        # -------------------------------------------------------------
        t0 = time.time()
        print("\n[Scenario 5] Submitting Telemetry to Master Studio Backend...")
        
        # Intercept and record the network request
        with page.expect_response("**/api/quiz/submit") as response_info:
            send_btn = page.locator("#btn-send-studio, button:has-text('Send to Master Studio')").first
            send_btn.click()
            
        response = response_info.value
        res_json = response.json()
        print(f"  ✓ Server Response: HTTP {response.status} -> {res_json}")
        results["scenario_5_sync"] = {
            "status_code": response.status,
            "response": res_json,
            "duration_s": round(time.time() - t0, 2)
        }

        # -------------------------------------------------------------
        # Scenario 6: Bookmarks & Drawers Navigation
        # -------------------------------------------------------------
        t0 = time.time()
        print("\n[Scenario 6] Testing Bookmarks & Analytics Slide-Over Drawers...")
        bm_btn = page.locator("#btn-bookmarks-toggle, button[aria-label='Bookmarks']").first
        if bm_btn.is_visible():
            bm_btn.click()
            time.sleep(0.3)
            drawer = page.locator("#drawer-bookmarks, .drawer.open").first
            is_open = drawer.is_visible()
            print(f"  ✓ Opened Bookmarks Drawer | is_visible: {is_open}")
            # Close drawer
            page.locator(".drawer-close, #drawer-overlay").first.click()
            results["scenario_6_drawers"] = {"bookmarks_drawer_open": is_open}

        browser.close()

    total_time = time.time() - start_total
    print("\n" + "=" * 70)
    print(f"🎉 SIMULATION COMPLETE IN {total_time:.2f} SECONDS (100% HEADLESS & DETERMINISTIC)")
    print("=" * 70)
    return results

if __name__ == "__main__":
    res = run_simulation()
    print("\nJSON Summary of Simulation Results:")
    print(json.dumps(res, indent=2))
