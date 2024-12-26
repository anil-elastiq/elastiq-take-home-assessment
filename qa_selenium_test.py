import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# pytest fixture for WebDriver setup
@pytest.fixture()
def setup_and_teardown():
    # setup browser & its mode
    browser = "chrome"  # provide chrome/edge/firefox
    browser_mode = "non_headless"   # provide headless/non_headless mode

    site_url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"

    if browser == 'chrome':
        options = ChromeOptions()
        if browser_mode == 'headless':  # now added headless test here
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        if browser_mode == 'headless':
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    elif browser == 'edge':
        options = EdgeOptions()
        if browser_mode == 'headless':
            options.add_argument("--headless")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError("provide valid browser name")

    if browser_mode != 'headless':
        driver.maximize_window()

    # Navigate to the Selenium Playground website
    driver.get(site_url)
    yield driver
    driver.quit()


def enter_text_into_search_box(driver, input_text):
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()
    search_box.send_keys(input_text)


search_text = "New York"    # search string


# Test Cases
def test_search_result_text(setup_and_teardown):
    driver = setup_and_teardown

    # Perform search
    enter_text_into_search_box(driver, search_text)

    # Validate the search result text
    actual_text = driver.find_element(By.XPATH, "//div[@role='status']").text
    expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"


def test_search_result_table(setup_and_teardown):
    driver = setup_and_teardown

    # Perform search
    enter_text_into_search_box(driver, search_text)

    # validate rows having searched text in table
    actual_count = len(driver.find_elements(By.XPATH,
                                            f"//thead/following-sibling::tbody/tr/td[text()='{search_text}']"))
    expected_count = 5
    assert actual_count == expected_count, f"Expected rows '{expected_count}', but got '{actual_count}'"
