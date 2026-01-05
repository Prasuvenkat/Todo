from playwright.sync_api import sync_playwright
import time


def test_todo_with_full_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300   
        )

        # video recording
        context = browser.new_context(
            record_video_dir="videos/"
        )
        page = context.new_page()
 
        page.goto("https://demo.playwright.dev/todomvc/")
        time.sleep(2)

        page.wait_for_selector("input.new-todo")
        todo = page.locator("input.new-todo")

        todo.fill("Learn Playwright")
        todo.press("Enter")
        time.sleep(1)

        todo.fill("Write automation test")
        todo.press("Enter")
        time.sleep(1)

        todo.fill("Practice QA interview questions")
        todo.press("Enter")
        time.sleep(1)

        page.locator(".todo-list li").nth(0).locator("input.toggle").check()
        time.sleep(1)

        page.get_by_role("link", name="Active").click()
        time.sleep(2)

        page.get_by_role("link", name="Completed").click()
        time.sleep(2)

        page.get_by_role("link", name="All").click()
        time.sleep(2)

        second_item = page.locator(".todo-list li").nth(1)
        second_item.hover()
        time.sleep(1)
        second_item.locator("button.destroy").click()
        time.sleep(2)

        page.screenshot(path="screenshots/final_todo_state.png")

        context.close()
        browser.close()
