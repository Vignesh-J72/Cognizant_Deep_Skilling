from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DropdownPage(BasePage):
    SELECT_DROPDOWN = (By.ID, "select-demo")
    SELECTED_TEXT_MESSAGE = (By.CSS_SELECTOR, "p.selected-value")

    def select_day(self, day_name):
        dropdown_element = self.wait_for_presence(self.SELECT_DROPDOWN)
        select_obj = Select(dropdown_element)
        select_obj.select_by_visible_text(day_name)

    def get_selected_day_message(self):
        wait = WebDriverWait(self.driver, 10)
        message_element = wait.until(EC.visibility_of_element_located(self.SELECTED_TEXT_MESSAGE))
        return message_element.text