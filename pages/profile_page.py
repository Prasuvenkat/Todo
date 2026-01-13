from pages.base_page import BasePage

class ProfilePage(BasePage):

    USER_AVATAR = ("role", "img", "User Avatar")
    MY_PROFILE = "My Profile"
    EDIT_BUTTON = ("role", "button", "edit Edit")
    SAVE_BUTTON = ("role", "button", "Save")
    CLOSE_BUTTON = ("role", "button", "Close")

    def open_profile(self):
        self.click(self.page.get_by_role("img", name="User Avatar"))
        self.click(self.page.get_by_text("My Profile"))
    def click_edit(self):
        self.click(self.page.get_by_role("button", name="edit Edit"))

    def update_basic_details(self, first_name, last_name, pincode):
        self.fill(self.page.get_by_role("textbox").nth(2), first_name)
        self.fill(self.page.get_by_role("textbox").nth(1), last_name)
        self.fill(self.page.get_by_role("textbox").nth(5), pincode)

    def select_country(self, country="India"):
     country_field = self.page.get_by_text("Country", exact=True)
     self.select_ant_option(country_field, country)

    # def select_degree(self, degree="Bachelor's"):
    #     self.select_from_ant_dropdown(
    #         self.page.get_by_text("Degree Pursue Master's"),
    #         degree
    #     )

    def update_gpa_scores(self, gpa_4="3", gpa_5="3"):
        self.fill(self.page.get_by_role("textbox", name="Score /4.0"), gpa_4)
        self.fill(self.page.get_by_role("textbox", name="Score /5.0"), gpa_5)

    def update_test_scores(self, gmat="600", ielts="8"):
        # GMAT
        self.select_ant_option(self.page.locator("#rc_select_7"), "GMAT")
        self.fill(self.page.get_by_role("textbox", name="Score / 800"), gmat)

        self.select_ant_option(self.page.locator("#rc_select_8"), "IELTS")
        self.fill(self.page.get_by_role("textbox", name="Score / 9.0"), ielts)

 
    def update_experience(self, years="5", months="10"):
        self.fill(
            self.page.locator(".input-underlined-exp").first,
            years
        )
        self.fill(
            self.page.locator("input:nth-child(3)"),
            months
        )

    def select_discipline(self, discipline="Communications Technologies/"):
        self.select_ant_option(
            self.page.locator("#rc_select_5"),
            discipline
        )

    def select_preferences(self):
     self.toggle_ant_checkbox("Earnings")
     self.toggle_ant_checkbox("Employment")
     self.toggle_ant_checkbox("Ranking")

    def select_year(self, year="2026"):
        self.select_ant_option(
            self.page.locator("div:nth-child(5) > .ant-select-selector"),
            year
        )

    def save_profile(self):
        self.click(self.page.get_by_role("button", name="Save"))