import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--window-size=1280,800')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

    start_time_sleep = time.time()
    
    success_btn = driver.find_element(By.XPATH, "//button[contains(translate(normalize-space(text()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'autoclosable success')]")
    success_btn.click()
    print("Clicked success alert button using hardcoded sleep")
    
    time.sleep(3)
    
    alert_div_sleep = driver.find_element(By.XPATH, "//div[contains(@class, 'alert') and contains(@class, 'success')]")
    sleep_duration = time.time() - start_time_sleep
    print("Retrieved alert message after hardcoded sleep")

    driver.refresh()

    start_time_explicit = time.time()
    
    success_btn = driver.find_element(By.XPATH, "//button[contains(translate(normalize-space(text()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'autoclosable success')]")
    success_btn.click()
    print("Clicked success alert button using explicit wait")
    
    wait = WebDriverWait(driver, 10)
    alert_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert') and contains(@class, 'success')]"))
    )
    
    explicit_duration = time.time() - start_time_explicit
    print("Retrieved alert message using explicit wait")
    
    assert "success" in alert_element.text.lower()
    print("Verified success message text")

    clickable_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(normalize-space(text()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'autoclosable success')]"))
    )
    print("Verified button clickability using element_to_be_clickable")

    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    fluent_wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5,
        ignored_exceptions=[NoSuchElementException, ElementNotInteractableException]
    )

    table_row = fluent_wait.until(
        EC.presence_of_element_located((By.XPATH, "//table[@id='example']/tbody/tr[1]"))
    )
    print("Located dynamic table row using FluentWait")

finally:
    driver.quit()