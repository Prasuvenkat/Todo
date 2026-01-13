from pages.base_page import BasePage

class CourseFilterPage(BasePage):

    def open_search_tab(self):
        self.page.get_by_role("tab", name="Search").click()

    def open_course_section(self):
        self.page.get_by_title("Course").click()

    def open_all_courses(self):
        self.page.get_by_text("View All Courses").click()

    def apply_duration_filter(self):
        self.page.locator(".ant-slider-track").first.click()
        self.page.get_by_role("button", name="Apply").first.click()

    def apply_study_mode_filter(self):
        self.page.get_by_role("switch").first.click()
        self.page.get_by_role("switch").nth(1).click()

    def apply_state_filter(self, state: str):
        self.page.get_by_role("checkbox", name=state).check()

    def search_location(self, location: str):
        box = self.page.get_by_role("textbox", name="Search")
        box.fill(location)
        self.page.get_by_text(location.capitalize()).click()

    def open_advanced_filters(self):
        self.page.get_by_role("button", name="Advanced Filters down").click()

    def apply_experience_filter(self):
        self.page.get_by_text("1 years").click()

    def clear_all_filters(self):
        self.page.get_by_role("button", name="reload Clear All").click()
