from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxPage(BasePage):
    SINGLE_CHECKBOX = (By.ID, "isAgeSelected")
    CHECKBOX_OPTION_1 = (By.XPATH, "//input[@id='ex1-check1']")
    CHECKBOX_OPTION_2 = (By.XPATH, "//input[@id='ex1-check2']")
    CHECKBOX_OPTION_3 = (By.XPATH, "//input[@id='ex1-check3']")
    CHECKBOX_OPTION_4 = (By.XPATH, "//input[@id='ex1-check4']")

    def __init__(self, driver):
        super().__init__(driver)
        self.options_map = {
            1: self.CHECKBOX_OPTION_1,
            2: self.CHECKBOX_OPTION_2,
            3: self.CHECKBOX_OPTION_3,
            4: self.CHECKBOX_OPTION_4
        }

    def check_single_checkbox(self):
        checkbox = self.wait_for_presence(self.SINGLE_CHECKBOX)
        if not checkbox.is_selected():
            self.js_click(checkbox)

    def uncheck_single_checkbox(self):
        checkbox = self.wait_for_presence(self.SINGLE_CHECKBOX)
        if checkbox.is_selected():
            self.js_click(checkbox)

    def is_single_checkbox_checked(self):
        checkbox = self.wait_for_presence(self.SINGLE_CHECKBOX)
        return checkbox.is_selected()

    def check_option(self, index):
        locator = self.options_map.get(index, self.SINGLE_CHECKBOX)
        checkbox = self.wait_for_presence(locator)
        if not checkbox.is_selected():
            self.js_click(checkbox)

    def uncheck_option(self, index):
        locator = self.options_map.get(index, self.SINGLE_CHECKBOX)
        checkbox = self.wait_for_presence(locator)
        if checkbox.is_selected():
            self.js_click(checkbox)

    def is_option_checked(self, index):
        locator = self.options_map.get(index, self.SINGLE_CHECKBOX)
        checkbox = self.wait_for_presence(locator)
        return checkbox.is_selected()