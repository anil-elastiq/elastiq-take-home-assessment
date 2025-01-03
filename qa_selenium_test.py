import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    SEARCH_BOX = (By.XPATH, "//input[@type='search']")
    INFO_TEXT = (By.ID, "example_info")

@pytest.fixture
def setup_and_teardown():
    driver_path = "chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search_functionality(setup_and_teardown):
    driver = setup_and_teardown
    URL="https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    searchText = "New York"
    driver.get(URL)
    #search new york
    search_box = driver.find_element(*Locators.SEARCH_BOX)
    search_box.send_keys(searchText)

    #using explicite wait
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            Locators.INFO_TEXT, "Showing 1 to 5 of 5 entries"
        )
    )

    #Validate search results show 5 entries out of 24 total entries
    info_text = driver.find_element(*Locators.INFO_TEXT).text
    assert "Showing 1 to 5 of 5 entries" in info_text, "Search results validation failed"

if __name__ == "__main__":
    pytest.main()
