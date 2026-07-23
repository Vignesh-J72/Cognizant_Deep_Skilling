"""
===============================================================================
WHY PAGE OBJECT MODEL (POM) SOLVES SCRIPT FRAGILITY
===============================================================================
Problem in Flat (Non-POM) Scripts:
If the Submit button's ID changes from 'submit' to 'btn-submit', every flat test
script referencing driver.find_element(By.ID, 'submit') across dozens or hundreds
of test files will break. Updating them requires searching and modifying every single file,
creating massive maintenance overhead and risk of missed updates.

POM Solution:
In the Page Object Model, element locators are declared once as class-level variables
inside page classes (e.g., SimpleFormPage.SUBMIT_BUTTON = (By.ID, 'btn-submit')).
Test files only invoke high-level action methods like page.click_submit().
When a locator changes, updating a single line in the page object fixes the entire test suite.
===============================================================================
"""

import pytest
from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage

@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    page = SimpleFormPage(driver)
    page.navigate_to(f"{base_url}simple-form-demo")
    
    page.enter_message(message)
    print("Entered message via SimpleFormPage")
    
    page.click_submit()
    print("Clicked submit via SimpleFormPage")
    
    assert page.get_displayed_message() == message
    print("Asserted displayed message matches input text")

def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(f"{base_url}checkbox-demo")
    
    page.check_single_checkbox()
    print("Checked age checkbox via CheckboxPage")
    assert page.is_single_checkbox_checked()
    
    page.uncheck_single_checkbox()
    print("Unchecked age checkbox via CheckboxPage")
    assert not page.is_single_checkbox_checked()

def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(f"{base_url}select-dropdown-demo")
    
    page.select_day("Wednesday")
    print("Selected Wednesday via DropdownPage")
    
    assert "Wednesday" in page.get_selected_day_message()
    print("Asserted selected day message")

def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(f"{base_url}input-form-demo")
    
    page.fill_form("Alex Johnson", "alex@example.com", "78701", "123 Main St")
    print("Filled input form fields via InputFormPage")
    
    page.submit_form()
    print("Submitted input form via InputFormPage")
    
    success_text = page.get_success_message()
    assert "Thanks for contacting us" in success_text
    print("Asserted input form submission success message")