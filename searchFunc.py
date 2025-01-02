from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_table_data(driver):

    total_rows = 0
    wait = WebDriverWait(driver, 20)

    while True:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='example']/tbody/tr")))
        rows_pg = driver.find_elements(By.XPATH, "//*[@id='example']/tbody/tr")
        total_rows += len(rows_pg)
        
        
        next_button = driver.find_element(By.XPATH, "//*[@id='example_next']")
        if "disabled" in next_button.get_attribute("class"):
            break
        next_button.click()

    search=driver.find_element(By.XPATH, "//*[@id='example_filter']/label/input")
    search.send_keys("New York")

    WebDriverWait(driver, 20)
    rows = driver.find_elements(By.XPATH, "//*[@id='example']/tbody/tr")
    
        
    assert len(rows) == 5, f"Expected 5 rows after filtering, but got {len(rows)}"
    assert total_rows == 24, f"Expected 24 total rows, but got {total_rows}"


