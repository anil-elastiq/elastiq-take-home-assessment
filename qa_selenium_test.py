import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test URL
URL = "https://www.seleniumeasy.com/test/table-search-filter-demo.html"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(service=service, options=options)
    
    yield browser
    browser.quit()

def test_search_functionality(driver):
    driver.get(URL)
    driver.maximize_window()
    
    # Locate search input box and input "New York"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "task-table-filter"))
    )
    search_box.clear()
    search_box.send_keys("New York")
    
    # Validate search results
    rows = driver.find_elements(By.XPATH, "//table[@id='task-table']//tbody/tr")
    visible_rows = [row for row in rows if row.is_displayed()]
    
    assert len(visible_rows) == 5, f"Expected 5 results, but found {len(visible_rows)}"
