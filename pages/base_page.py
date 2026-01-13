from playwright.sync_api import Page
from utils.config import BASE_URL

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_base_url(self):
        from utils.config import BASE_URL
        self.page.goto(BASE_URL)

    def fill(self, locator, value):
        locator.wait_for(state="visible")
        locator.fill(value)

    def click_by_role(self, role: str, name: str, index: int | None = None):
        locator = self.page.get_by_role(role, name=name)
        if index is not None:
            locator = locator.nth(index)
        locator.click()

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def press(self, locator, key):
        locator.wait_for(state="visible")
        locator.press(key)

    def select_text(self, text):
        self.page.get_by_text(text, exact=True).click()

    def is_visible(self, locator) -> bool:
        return locator.is_visible()

    def wait_for_visible(self, locator):
        locator.wait_for(state="visible")

    def select_ant_option(self, trigger_locator, option_text: str):
        trigger_locator.wait_for(state="visible")
        trigger_locator.scroll_into_view_if_needed()
        trigger_locator.click(force=True)

        dropdown_option = self.page.locator(
        ".ant-select-dropdown:visible .ant-select-item-option-content",
        has_text=option_text
    )

        dropdown_option.wait_for(state="visible")
        dropdown_option.click()

    def toggle_ant_checkbox(self, label_text: str):
        checkbox_label = self.page.get_by_text(label_text, exact=True)
        checkbox_label.wait_for(state="visible")
        checkbox_label.click()