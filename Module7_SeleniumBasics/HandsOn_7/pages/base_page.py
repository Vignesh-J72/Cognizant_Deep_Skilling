from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def js_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", element)