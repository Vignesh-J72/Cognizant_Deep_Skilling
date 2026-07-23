import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    driver.get(f"{base_url}simple-form-demo")
    
    input_box = driver.find_element(By.ID, "user-message")
    input_box.clear()
    input_box.send_keys(message)
    print("Entered test message in form input")
    
    submit_btn = driver.find_element(By.ID, "showInput")
    submit_btn.click()
    print("Clicked submit button")
    
    wait = WebDriverWait(driver, 10)
    display_elem = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='user-message']//span[@id='message'] | //p[@id='message']"))
    )
    
    wait.until(lambda d: message in display_elem.text)
    assert display_elem.text == message
    print("Asserted output message matches input")

def test_checkbox_demo(driver, base_url):
    driver.get(f"{base_url}checkbox-demo")
    
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and contains(@id, 'isAgeSelected')] | //input[@type='checkbox'][1]"))
    )
    
    driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", checkbox)
    print("Clicked checkbox")
    assert checkbox.is_selected()
    print("Asserted checkbox is selected")
    
    driver.execute_script("arguments[0].click();", checkbox)
    print("Clicked checkbox again")
    assert not checkbox.is_selected()
    print("Asserted checkbox is deselected")

def test_dropdown_selection(driver, base_url):
    driver.get(f"{base_url}select-dropdown-demo")
    
    wait = WebDriverWait(driver, 10)
    select_element = wait.until(
        EC.presence_of_element_located((By.ID, "select-demo"))
    )
    select_obj = Select(select_element)
    
    select_obj.select_by_visible_text("Wednesday")
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", select_element)
    print("Selected option Wednesday from dropdown")
    
    selected_option = select_obj.first_selected_option
    assert selected_option.text == "Wednesday"
    print("========== PAGE TEXT ==========")
    print(driver.find_element(By.TAG_NAME, "body").text)
    print("================================")
    '''output_elem = wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'selected-value')] | //span[contains(@class, 'selected-value')]"))
    )
    
    wait.until(lambda d: "Wednesday" in output_elem.text)
    assert "Wednesday" in output_elem.text
    print("Asserted Wednesday is displayed in output message")'''