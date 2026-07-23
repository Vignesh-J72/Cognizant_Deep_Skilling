import os
import time
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
    """
    CONSISTENT WINDOW SIZE IN AUTOMATION:
    Web applications use responsive CSS breakpoints. Varying screen resolutions across
    test runs can cause elements (like navigation bars or buttons) to hide inside
    hamburger menus or change coordinates, leading to brittle locator failures.
    Setting an explicit window size guarantees deterministic layout behavior.
    """
    driver.set_window_size(1280, 800)
    current_size = driver.get_window_size()
    print(f"Configured Window Size: {current_size['width']}x{current_size['height']}")

    driver.get("https://www.lambdatest.com/selenium-playground/")
    
    simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
    simple_form_link.click()
    
    current_url = driver.current_url
    assert "simple-form-demo" in current_url, f"Expected 'simple-form-demo' in URL, got: {current_url}"

    driver.back()
    driver.execute_script('window.open("https://www.google.com");')
    
    handles = driver.window_handles
    

    driver.switch_to.window(handles[1])
    driver.switch_to.window(handles[0])
    output="Module7_SeleniumBasics/HandsOn_4"
    screenshot_filename = "playground_screenshot.png"
    ss_path=os.path.join(output,screenshot_filename)
    driver.save_screenshot(ss_path)
    
    assert os.path.exists(screenshot_filename), "Screenshot file was not created!"
finally:
    driver.quit()