from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
def test_sort_table(setup):
    driver = setup
    driver.find_element(By.XPATH, "//input[@type='search']").send_keys("New York")
    validate_text = driver.find_element(By.XPATH, "//div[@id='example_info']").text
    assert validate_text == "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"