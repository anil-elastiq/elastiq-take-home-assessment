import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def setup_browser():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver
    driver.quit()


def test_search_functionality(setup_browser):
    driver = setup_browser
    driver.get("provide_url")
    searchBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search-data-filter"))
    )
    searchBox.clear()
    searchBox.send_keys("New York")
    rows = driver.find_elements(By.XPATH, "search_xpath")
    visible_rows = [row for row in rows if row.is_displayed()]

    assert len(visible_rows) == 5, f"Expected 5 results, but found {
    len(visible_rows)}"
    print("Test passed: Search functionality works as expected.")

1. Ensure you have Python 3.7+ and install dependencies.
2. Download the correct version of ChromeDriver
3. Set the ChromeDriver
4. provide the url and replace with "provide_url".
5. provide the locator using xpath and replace with "search_xpath"
6. Asserted result as New York and the length is 5.
7. Run the test .
