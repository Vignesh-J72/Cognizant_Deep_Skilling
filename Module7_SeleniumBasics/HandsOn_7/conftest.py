import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1280,800")
    
    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver_instance
    
    driver_instance.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.name
            driver.save_screenshot(f"{test_name}_failure.png")
            print(f"Captured failure screenshot: {test_name}_failure.png")