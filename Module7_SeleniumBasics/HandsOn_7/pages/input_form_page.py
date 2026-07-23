from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InputFormPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "inputEmail4")
    PASSWORD_INPUT = (By.ID, "inputPassword4")
    COMPANY_INPUT = (By.ID, "company")
    WEBSITE_INPUT = (By.ID, "websitename")
    COUNTRY_SELECT = (By.NAME, "country")
    CITY_INPUT = (By.ID, "inputCity")
    ADDRESS1_INPUT = (By.ID, "inputAddress1")
    ADDRESS2_INPUT = (By.ID, "inputAddress2")
    STATE_INPUT = (By.ID, "inputState")
    ZIP_INPUT = (By.ID, "inputZip")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "p.success-msg")

    def fill_form(self, name, email, phone, address, country="United States"):
        self.wait_for_element(self.NAME_INPUT).send_keys(name)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys("Pass123!")
        self.wait_for_element(self.COMPANY_INPUT).send_keys("TechCorp")
        self.wait_for_element(self.WEBSITE_INPUT).send_keys("https://example.com")
        
        country_element = self.wait_for_element(self.COUNTRY_SELECT)
        select_obj = Select(country_element)
        select_obj.select_by_visible_text(country)
        
        self.wait_for_element(self.CITY_INPUT).send_keys("Austin")
        self.wait_for_element(self.ADDRESS1_INPUT).send_keys(address)
        self.wait_for_element(self.ADDRESS2_INPUT).send_keys("Suite 100")
        self.wait_for_element(self.STATE_INPUT).send_keys("Texas")
        self.wait_for_element(self.ZIP_INPUT).send_keys(phone)

    def submit_form(self):
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).text