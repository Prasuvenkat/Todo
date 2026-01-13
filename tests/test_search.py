from pages.search_page import SearchPage

def test_search_and_course_flow(page):
    search = SearchPage(page)
    search.open_base_url()
    search.open_search_tab()
    search.search_university("barry university")
    search.select_university()
    search.add_university_to_list()
    search.apply_filters()
    search.open_all_courses()
    search.search_course("administration")
    search.search_course("teaching")
    search.select_course()
    search.add_course_to_favorites()
    search.view_college_details()
