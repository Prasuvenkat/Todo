from pages.login_page import LoginPage
from utils.test_data import VALID_LOGIN

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(
        VALID_LOGIN["email"],
        VALID_LOGIN["password"]
    )
    login_page.wait_for_dashboard()
    assert login_page.is_login_successful()
