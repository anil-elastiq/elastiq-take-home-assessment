from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Make sure to provide the correct path to your ChromeDriver


@pytest.fixture(scope="module")
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
    yield driver
    driver.quit()


def test_search_new_york(setup):
    search_box = driver.find_element(By.XPATH,"//input[@type = 'search']")
    search_box.send_keys('New York')
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # Wait for the results to update

    rows = driver.find_elements(By.XPATH, '//table[@id = "example" ]/tbody/tr')
    visible_rows = [row for row in rows if row.is_displayed()]

    assert len(visible_rows) == 5, f"Expected 5 entries, but found {len(visible_rows)}"
