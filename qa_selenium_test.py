import pytest
from driver_setup import get_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  # Replace with your desired browser
    yield driver
    driver.quit()

def test_search_functionality(driver):
    # Navigate to the Selenium Playground Table Search Demo
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo.html")

    # Locate and interact with the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
    )
    search_box.send_keys("New York")
  
    # Wait for the resulting rows to appear
    resulting_rows = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//table[@id='example']/tbody/tr"))
    )

    # Counting and validating the number of resulting rows with expected number of rows
    total_rows_count = [row for row in resulting_rows if row.is_displayed()]
    assert len(total_rows_count) == expected_row_count, \
        f"Expected rows: {expected_row_count} results, but actual rows: " \
        f"'{len(total_rows_count)}'"

    # Wait for the status text to appear and validate it
    actual_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='status']"))
    ).text
  
    # Validate the search results
    results_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="dataTables_info"]'))
    ).text
    assert "Showing 5 entries out of 24 total entries" in results_text
   
