import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Home_page import Homepage

# set up the driver fixture
@pytest.fixture
def driver():
    # Install and setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search(driver):
    homepage= Homepage(driver)
    homepage.open_page("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    time.sleep(2)
    homepage.search_value("New York")
    visible_rows=homepage.filter_rows()
    assert len(visible_rows) == 5, f"Expected 5 entries, but found {len(visible_rows)}"
    time.sleep(4)
    words=homepage.result_words()
    assert 'filtered from 24 ' in words.text



