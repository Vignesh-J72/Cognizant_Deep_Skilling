from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--window-size=1280,800')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    input_by_id = driver.find_element(By.ID, "user-message")
    input_by_class = driver.find_element(By.CLASS_NAME, "form-control")
    inputs_by_tag = driver.find_elements(By.TAG_NAME, "input")
    input_by_abs_xpath = driver.find_element(By.XPATH, "/html/body//input[@id='user-message']")
    input_by_rel_xpath = driver.find_element(By.XPATH, "//input[@id='user-message']")
    css_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
    css_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")
    css_parent_child = driver.find_element(By.CSS_SELECTOR, "div > input#user-message")
    driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
    option1_label = driver.find_element(By.XPATH, "//label[text()='Option 1']")
    option_labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
    
finally:
    driver.quit()