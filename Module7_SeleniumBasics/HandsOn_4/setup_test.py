"""
SELENIUM ARCHITECTURE OVERVIEW
1. Selenium WebDriver:
   - What it is: A client-server browser automation framework that provides a
     unified API to control web browsers programmatically.
   - How it communicates: The Python test script sends HTTP requests over the
     W3C WebDriver protocol to a browser-specific driver binary (e.g., ChromeDriver).
     The driver binary translates these requests into native browser automation API
     commands and returns responses back to the client script.

2. Selenium Grid:
   - Problem solved: Enables cross-browser testing and parallel execution across
     multiple operating systems, physical machines, or virtual containers simultaneously.
   - Mechanism: Uses a central Hub that receives test requests and routes them to
     registered Node instances (browser environments).

3. Selenium IDE:
   - What it is: A browser extension (Chrome/Firefox) providing "Record and Playback"
     capabilities for automated web testing.
   - Purpose: Useful for rapid prototyping, generating initial test code skeletons,
     and quick visual regression checks without initial coding setup.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

"""
Why global implicit wait is bad practice-
Setting driver.implicitly_wait(10) globally makes WebDriver poll the DOM for 10
seconds whenever an element is missing. This creates hidden test delays, masks real
UI/DOM performance issues, and when combined with Explicit Waits (WebDriverWait),
it introduces unpredictable wait timeouts across different browser engines. Explicit
waits should always be preferred for targeted element states.
"""
driver.implicitly_wait(10)

try:
    url = "https://www.lambdatest.com/selenium-playground/"
    driver.get(url)
    
    page_title = driver.title
    print(f"[Task 1] Page Title in Headless Mode: {page_title}")
    
    assert "Selenium Grid Online" in page_title or "LambdaTest" in page_title, "Title validation failed!"
    print("[Task 1] Verification successful: Headless execution retrieved title correctly.")

finally:
    driver.quit()