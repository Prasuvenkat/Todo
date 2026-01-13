from playwright.sync_api import sync_playwright
from utils.config import BASE_URL

def generate_auth_state():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="playwright-profile",
            channel="chrome",
            headless=False
        )

        page = context.new_page()

        print("👉 Opening FuturX base URL")
        page.goto(BASE_URL, timeout=15000)

        print("👉 Please login manually (Google / Email)")
        print("👉 After successful login, DO NOT close the browser")
        page.wait_for_timeout(20000)

        context.storage_state(path="auth_state.json")
        print("✅ auth_state.json generated successfully")

        context.close()

if __name__ == "__main__":
    generate_auth_state()
