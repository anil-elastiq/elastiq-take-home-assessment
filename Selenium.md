# qa_selenium_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Constants
demo_url = "https://www.seleniumeasy.com/test/table-search-filter-demo.html"
search_term = "New York"
expected_entries = 5

# Setup the WebDriver (Ensure you have the appropriate driver installed and in PATH)
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to the Selenium Playground Table Search Demo
    driver.get(demo_url)

    # Allow page to load
    time.sleep(2)

    # Locate the search box and enter the search term
    search_box = driver.find_element(By.ID, "task-table-filter")
    search_box.send_keys(search_term)

    # Allow search results to filter
    time.sleep(1)

    # Locate the table rows
    rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")

    # Filter visible rows
    visible_rows = [row for row in rows if row.is_displayed()]

    # Validate the search results
    if len(visible_rows) == expected_entries:
        print(f"Test Passed: Found {len(visible_rows)} entries as expected.")
    else:
        print(f"Test Failed: Expe
