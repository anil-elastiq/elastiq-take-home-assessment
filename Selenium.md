import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="module")
def setup():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.selenium.dev/selenium/playground/")
    driver.maximize_window()
    yield driver  # This is the setup for the test, teardown happens after the yield
    driver.quit()  # Teardown, close browser after tests complete

def test_search_functionality(setup):
    driver = setup
    
    # Locate the search input field and search button
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed(), "Search box should be visible on the page"
    
    # Enter search term into the search box
    search_term = "Selenium"
    search_box.send_keys(search_term)
    
    # Press 'Enter' to initiate the search
    search_box.send_keys(Keys.RETURN)
    
    # Wait for a while to ensure search results have time to load
    time.sleep(2)  # You can use WebDriverWait for better synchronization
    
    # Verify if search results contain the expected term
    search_results = driver.find_elements(By.CSS_SELECTOR, ".search-result")
    assert len(search_results) > 0, "No search results found"
    
    # Optionally, check if the search term is mentioned in the search results
    for result in search_results:
        assert search_term.lower() in result.text.lower(), f"Search term '{search_term}' not found in result"
    
    print("Search functionality test passed!")

