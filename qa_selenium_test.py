 
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Constants
SELENIUM_PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
SEARCH_TERM = "New York"
EXPECTED_RESULTS_COUNT = 5

@pytest.fixture(scope="module")
def driver():
    """Set up the WebDriver instance and yield it."""
    service = ChromeService(ChromeDriverManager().install())
    print('service ====>>>>', service)
    driver_instance = webdriver.Chrome(service=service)
    driver_instance.implicitly_wait(10)
    yield driver_instance
    driver_instance.quit()

def test_search_functionality(driver):
    """Test the search functionality on the Selenium Playground."""
    # Navigate to the Selenium Playground Table Search Demo
    driver.get(SELENIUM_PLAYGROUND_URL)

    # Locate the search box and input the search term
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()
    search_box.send_keys(SEARCH_TERM)
    print('Searched for newYork')

    # Locate the table rows
    table_rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    print('table_rows ====>>>>', table_rows)

    # Filter rows based on visibility and search term
    visible_rows = [row for row in table_rows if row.is_displayed()]
    print('visible_rows', visible_rows)

    # Validate the number of results displayed matches the expected count
    assert len(visible_rows) == EXPECTED_RESULTS_COUNT, (
        f"Expected {EXPECTED_RESULTS_COUNT} results, but found {len(visible_rows)}."
    )

if __name__ == "__main__":
    pytest.main(["-v", __file__])
