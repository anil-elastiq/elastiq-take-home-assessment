import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="module")
def browser():
    options = ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI/CD
    service = Service("path/to/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()


def test_search_functionality(browser):
    url = "https://www.seleniumeasy.com/test/table-search-filter-demo.html"
    browser.get(url)

    wait = WebDriverWait(browser, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "task-table-filter")))

    search_box.send_keys("New York")
    rows = browser.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")

    visible_rows = [row for row in rows if row.is_displayed()]
    assert len(visible_rows) == 5, f"Expected 5 visible rows, found {len(visible_rows)}."

    total_entries_text = browser.find_element(By.XPATH, "//table[@id='task-table']/tfoot/tr/td").text
    assert "24 entries" in total_entries_text, "Total entries text mismatch."

    print("Test completed successfully.")

if __name__ == "__main__":
    pytest.main(["-v", "--disable-warnings"])
