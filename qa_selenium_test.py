import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
SEARCH_TEXT = "New York"
EXPECTED_RESULTS = 5

def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    return driver

def test_search_functionality():
    driver = setup_browser()
    try:
        search_box = driver.find_element(By.XPATH, "//input[@type='search']")
        search_box.send_keys(SEARCH_TEXT)
      
        results = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
        assert len(results) == EXPECTED_RESULTS, f"Expected {EXPECTED_RESULTS} entries, but found {len(results)}"
    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main([__file__])
