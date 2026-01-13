import re
from pages.base_page import BasePage

class CollegeFilterPage(BasePage):

    def open_search_tab(self):
        self.page.get_by_role("tab", name="Search").click()

    def open_all_colleges(self):
        self.page.get_by_text("View All Colleges").click()

    def open_sort(self):
        self.page.get_by_role("button", name="sort").click()

    def sort_by(self, option: str):
        self.open_sort()
        self.page.get_by_text(option).click()

    def apply_ranking_filter(self):
        self.open_sort()
        self.page.get_by_role("menu").get_by_text("Ranking").click()

        slider = self.page.get_by_role("slider").first
        for _ in range(4):
            slider.click()

        self.page.get_by_role("button", name="Apply").first.click()

        self.page.locator("#rc_select_5").click()
        self.page.get_by_text("QS - Academic Reputation").click()
        self.page.locator("div").filter(has_text=re.compile(r"^0700$")).first.click()

        self.page.get_by_role("button", name="Apply").nth(1).click()

    def apply_city_filter(self):
        self.page.get_by_text("City").click()
        self.page.get_by_role("button", name="Clear").nth(2).click()

        self.page.get_by_role("switch").first.click()
        self.page.get_by_role("switch").nth(1).click()
        self.page.get_by_role("checkbox", name="Connecticut").check()

    def apply_advanced_filters(self):
        self.page.get_by_role("button", name="Advanced Filters down").click()

        self.page.locator(
            "div:nth-child(2) > div > .filterContainer > .filterGroup > .sliderWrapper > .ant-slider"
        ).first.click()
        self.page.get_by_role("button", name="Apply").nth(3).click()

        self.page.locator(
            "div:nth-child(3) > .filterContainer > .filterGroup > .sliderWrapper > .ant-slider"
        ).click()
        self.page.get_by_role("button", name="Apply").nth(4).click()

        self.page.get_by_text("Very Small").click()

    def clear_all_filters(self):
        self.page.get_by_role("button", name="reload Clear All").click()
