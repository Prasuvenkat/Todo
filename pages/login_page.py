from pages.base_page import BasePage

class LoginPage(BasePage):

    def email_input(self):
        return self.page.get_by_role("textbox", name="Email address")

    def password_input(self):
        return self.page.get_by_role("textbox", name="Password")

    def continue_button(self):
        return self.page.get_by_role("button", name="Continue", exact=True)

    PROFILE_ICON = "[data-testid='profile-icon']"

    def open(self):
        self.open_base_url()

    def login(self, email: str, password: str):
        self.fill(self.email_input(), email)
        self.fill(self.password_input(), password)
        self.click(self.continue_button())

    def wait_for_dashboard(self):
        self.page.locator(self.PROFILE_ICON).wait_for(state="visible")

    def is_login_successful(self) -> bool:
        return self.page.locator(self.PROFILE_ICON).is_visible()
