from pages.course_page import CourseFilterPage

def test_course_filter_flow(page):
    course = CourseFilterPage(page)
    course.open_base_url()
    course.open_search_tab()
    course.open_course_section()
    course.open_all_courses()
    course.apply_duration_filter()
    course.apply_study_mode_filter()
    course.apply_state_filter("Alabama")
    course.search_location("arizona")
    course.open_advanced_filters()
    course.apply_experience_filter()
    course.clear_all_filters()
