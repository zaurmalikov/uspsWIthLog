import pytest

from page_objects.main_page import MainPage
from test_data.test_data_excel import TestDataExcel
from utilities.base_class import BaseClass


class TestFindCityByZipCode(BaseClass):

    @pytest.fixture(params=TestDataExcel.data_list)  # this will pull data from Excel file in test data
    def value(self, request):
        return request.param

    def test_find_city_by_zip_code(self, value):
        main_page = MainPage(self.driver)
        log = self.get_logger()

        log.info("Step 1 - open usps.com and move mouse to quick tools menu")
        main_page.move_to_quick_tools_menu()

        log.info("Step 2 - click on look up a zip code icon")
        look_up_page = main_page.click_on_look_up_a_zipcode_icon()

        log.info("Step 3 - click on find cities by zip code button")
        cities_by_zip_sub_page = look_up_page.click_on_find_cities_by_zip_button()

        log.info(f"Step 4 - enter zip code {value['zip_code']}")
        cities_by_zip_sub_page.enter_zip_code(value["zip_code"])

        log.info("Step 5 - click on find button")
        validation_page = cities_by_zip_sub_page.click_find_button()

        assert value["city"] in validation_page.result_validation()
        log.info(f"Expected Result - {value['city']} /////// Actual result - {validation_page.result_validation()}")
        log.info("============== Testing Completed Successfully ==============")



