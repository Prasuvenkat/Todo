import pytest
from playwright.sync_api import sync_playwright

AUTH_FILE = "auth/auth_state.json"

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=800 )

        context = browser.new_context(
            storage_state=AUTH_FILE
        )

        page = context.new_page()
        yield page

        context.close()
        browser.close()
