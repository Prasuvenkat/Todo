from pages.college_page import CollegeFilterPage

def test_college_filter_flow(page):
    college = CollegeFilterPage(page)
    college.open_base_url()
    college.open_search_tab()
    college.open_all_colleges()
    college.sort_by("Popularity")
    college.sort_by("College Name (A to Z)")
    college.sort_by("Tuition Fee (Low to High)")
    college.sort_by("Test Score by SAT (Low to")
    college.apply_ranking_filter()
    college.apply_city_filter()
    college.apply_advanced_filters()
    college.clear_all_filters()
