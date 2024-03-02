from selenium.webdriver.common.by import By

from page_objects.cities_by_zip_code_sub_page import CitiesByZipSubPage


class LookUpPage:
    def __init__(self, driver):
        self.driver = driver

    find_cities_by_zip_button = (By.LINK_TEXT, "Find Cities by ZIP")

    def click_on_find_cities_by_zip_button(self):
        button = self.driver.find_element(*LookUpPage.find_cities_by_zip_button)
        button.click()
        assert "https://tools.usps.com/zip-code-lookup.htm?citybyzipcode" == self.driver.current_url
        cities_by_zip = CitiesByZipSubPage(self.driver)
        return cities_by_zip