import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


SEARCH_TERM = "New York"
EXPECTED_VISIBLE_ENTRIES = 5
TOTAL_ENTRIES = 24

@pytest.fixture(scope="module")
def browser():
   
    driver = webdriver.Chrome()  
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search_functionality(browser):
    
    browser.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    search_box = browser.find_element(By.XPATH, "//*[@id='example_filter']/label/input")
    search_box.clear()
    search_box.send_keys(SEARCH_TERM)

    rows = browser.find_elements(By.XPATH, "//*[@id='example']/tbody/tr")
    visible_entries = [row for row in rows if row.is_displayed()]

    assert len(visible_entries) == EXPECTED_VISIBLE_ENTRIES, (
        f"Expected {EXPECTED_VISIBLE_ENTRIES} visible entries for '{SEARCH_TERM}', "
        f"but found {len(visible_entries)}."
    )

if __name__ == "__main__":
    pytest.main(["-v", "qa_selenium_test.py"])