from pages.profile_page import ProfilePage

def test_update_profile(page):
    profile = ProfilePage(page)
    profile.open_base_url()
    profile.open_profile()
    profile.click_edit()
    profile.update_basic_details(
        first_name="prasu",
        last_name="venkatesan",
        pincode="641043"
    )
    profile.update_gpa_scores(gpa_4="3", gpa_5="3")
    profile.update_test_scores(gmat="600", ielts="8")
    profile.update_experience(years="5", months="10")
    profile.select_discipline("Communications Technologies/")
    profile.select_preferences()
    profile.select_year("2026")
    profile.save_profile()

    assert True 