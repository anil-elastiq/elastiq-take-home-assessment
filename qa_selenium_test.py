import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Setup
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@pytest.fixture(scope="module")
def driver():
    driver_instance = setup_driver()
    yield driver_instance
    driver_instance.quit()

# Test Case
def test_search_functionality(driver):
    # Navigate to the webpage
    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(url)

    # Wait for the search box to load
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#example_filter input")))

    # Perform search
    search_term = "New York"
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Validate search results
    time.sleep(2)
    rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
    visible_rows = [row for row in rows if row.is_displayed()]

    assert len(visible_rows) == 5, f"Expected 5 visible rows, but got {len(visible_rows)}"

    # Validate total entries text
    entries_text = driver.find_element(By.ID, "example_info").text
    assert "24 entries" in entries_text, "Total entries text validation failed"

    print("Test completed successfully.")
