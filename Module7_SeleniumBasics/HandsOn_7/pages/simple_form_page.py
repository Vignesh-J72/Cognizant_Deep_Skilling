from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SimpleFormPage(BasePage):
    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.ID, "showInput")
    DISPLAYED_MESSAGE = (By.ID, "message")

    def enter_message(self, text):
        input_element = self.wait_for_element(self.MESSAGE_INPUT)
        input_element.clear()
        input_element.send_keys(text)

    def click_submit(self):
        button_element = self.wait_for_clickable(self.SUBMIT_BUTTON)
        button_element.click()

    def get_displayed_message(self):
        message_element = self.wait_for_element(self.DISPLAYED_MESSAGE)
        return message_element.text