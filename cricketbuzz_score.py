
from playwright.sync_api import sync_playwright, TimeoutError

def capture_live_score():
    with sync_playwright() as p:
        # Launch a visible browser for the first test
        browser = p.chromium.launch(headless=False)

        page = browser.new_page(
            viewport={"width": 1366, "height": 900}
        )

        try:
            print("Opening Cricbuzz...")

            page.goto(
                "https://www.cricbuzz.com/",
                wait_until="domcontentloaded",
                timeout=60000
            )

            # Cricbuzz live-score card selector.
            # Verify this selector in browser DevTools.
            score = page.locator(".cb-lv-scrs-well").first

            print("Waiting for live match score...")

            score.wait_for(
                state="visible",
                timeout=20000
            )

            score_text = score.inner_text()

            print("\n========== LIVE CRICKET SCORE ==========")
            print(score_text)
            print("========================================")

        except TimeoutError:
            print("\nNo live match score found.")
            print("There may be no ongoing match, or the page structure may have changed.")

        except Exception as e:
            print(f"\nSomething went wrong: {e}")

        finally:
            # Save screenshot whether or not a live score was found
            page.screenshot(
                path="score.png",
                full_page=True
            )

            print("\nScreenshot saved as score.png")

            browser.close()


if __name__ == "__main__":
    capture_live_score()
