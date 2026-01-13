from playwright.sync_api import expect
from pages.base_page import BasePage

class SearchPage(BasePage):

    SEARCH_TAB = "role=tab[name='Search']"
    SEARCH_BOX = "role=textbox"

    UNIVERSITY_OPTION = "role=button[name='University of Idaho Moscow,']"
    ADD_TO_LIST_HEART = "role=button[name='heart Add to List']"

    FILTER_OFFICER_TRAINING = "role=button[name='Officer Training']"
    FILTER_DIVERSITY = "role=button[name='Diversity and Inclusion']"
    FILTER_WEATHER = "role=button[name='Weather']"

    VIEW_ALL_COURSES = "role=button[name='View All Courses']"
    COURSE_SEARCH = "role=textbox[name='Enter course name']"

    COURSE_ADMINISTRATION = "text=Teaching English or French as a Second or Foreign Language Course"
    COURSE_SELECT = "role=button[name='Teaching English or French as']"

    COURSE_HEART = "role=button[name='heart']"
    VIEW_COLLEGE_DETAILS = "role=button[name='View College Details']"

    def open_search_tab(self):
        self.page.get_by_role("tab", name="Search").click()

    def search_university(self, name: str):
        self.page.get_by_role("textbox").fill(name)

    def select_university(self):
        self.page.get_by_role("button", name="University of Idaho Moscow,").click()

    def add_university_to_list(self):
        university_card = self.page.locator(".college-card").first
        university_card.get_by_role(
        "button",
        name="heart Add to List"
        ).click()


    def apply_filters(self):
        self.page.get_by_role("button", name="Officer Training").click()
        self.page.get_by_role("button", name="Diversity and Inclusion").click()
        self.page.get_by_role("button", name="Weather").click()

    def open_all_courses(self):
        self.page.get_by_role("button", name="View All Courses").click()

    def search_course(self, course_name: str):
        search_box = self.page.get_by_role("textbox", name="Enter course name")
        search_box.fill(course_name)
        search_box.press("Enter")

    def select_course(self):
        self.page.get_by_role("button", name="Teaching English or French as").nth(1).click()

    def add_course_to_favorites(self):
        self.page.get_by_role("button", name="heart").nth(1).click()

    def view_college_details(self):
        self.page.get_by_role("button", name="View College Details").click()
