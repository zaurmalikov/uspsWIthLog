from selenium.webdriver.common.by import By


class ResultValidationSubPage:
    def __init__(self, driver):
        self.driver = driver

    validation_text = (By.XPATH, "//div[@class='row col-md-5 col-sm-12 col-xs-12 recommended-cities']/p[@class='row-detail-wrapper']")


    def result_validation(self):
        valid_text = self.driver.find_element(*ResultValidationSubPage.validation_text).text
        return valid_text