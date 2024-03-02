from selenium.webdriver.common.by import By

from page_objects.validation_sub_page import ResultValidationSubPage


class CitiesByZipSubPage:
    def __init__(self, driver):
        self.driver = driver

    zip_code_text_box = (By.CSS_SELECTOR, "#tZip")
    find_button = (By.CSS_SELECTOR, "#cities-by-zip-code")

    def enter_zip_code(self, zip_code_value):
        text_box = self.driver.find_element(*CitiesByZipSubPage.zip_code_text_box).send_keys(zip_code_value)
        return text_box

    def click_find_button(self):
        button = self.driver.find_element(*CitiesByZipSubPage.find_button).click()
        validation_sub_page = ResultValidationSubPage(self.driver)
        return validation_sub_page