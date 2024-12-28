import pytest
from driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_count_rows(driver):
    # Navigate to Selenium Playground Table Search Demo
    playground_url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(playground_url)

    search_string = "New York"
    expected_row_count = 5
    expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

    # Locate the search box and enter "New York"
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()
    search_box.send_keys(search_string)

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

    # Validating the actual text with expected text
    assert actual_text == expected_text, \
        f"Expected text is: '{expected_text}', but actual text is: '{actual_text}'"