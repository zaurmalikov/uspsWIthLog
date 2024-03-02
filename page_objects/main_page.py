from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.look_up_page import LookUpPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    quick_tools_menu = (By.XPATH, "//a[@class='nav-first-element menuitem']")
    all_quick_tools_menu_items = (By.XPATH, "//li[@class='qt-nav menuheader']/div/ul/li")

    def move_to_quick_tools_menu(self):
        action = ActionChains(self.driver)
        move = action.move_to_element(self.driver.find_element(*MainPage.quick_tools_menu)).perform()
        return move

    def click_on_look_up_a_zipcode_icon(self):
        menu_items = self.driver.find_elements(*MainPage.all_quick_tools_menu_items)
        for item in menu_items:
            if "Look Up a" in item.text:
                item.click()
                break
        assert "ZIP Code™ Lookup | USPS" in self.driver.title
        look_up_page = LookUpPage(self.driver)
        return look_up_page