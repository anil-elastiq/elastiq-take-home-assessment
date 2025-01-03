import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    yield driver
    driver.quit()


def test_search_functionality(driver):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))
    )
    search_box.clear()
    search_box.send_keys("New York")
    search_box.send_keys(Keys.RETURN)

    found_new_york = []
    while True:

        rows = driver.find_elements(By.XPATH, "//tr[@role='row' and @class='odd' or @class='even']")
        
        for row in rows:
            if "New York" in row.text:
                found_new_york.append(row.text)
        
        try:
            next_button = driver.find_element(By.XPATH, "//a[@id='example_next']")
            if "disabled" not in next_button.get_attribute("class"):
                next_button.click()
                time.sleep(2)
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    assert len(found_new_york) == 5, f"Expected 5 entries, but found {len(found_new_york)}"


if __name__ == "__main__":
    pytest.main()