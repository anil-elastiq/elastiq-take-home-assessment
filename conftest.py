import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_configure(config):
    # log file for the standalone test
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/assessment_test.log"

    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    logging.info(".....Starting the standalone test setup...")


# pytest fixture for WebDriver setup
@pytest.fixture()
def setup_and_teardown():
    # setup browser & its mode
    browser = "chrome"  # provide chrome/edge/firefox
    browser_mode = "non_headless"   # provide headless/non_headless mode

    logging.info(f"Running test in '{browser_mode}-Standalone' mode on '{browser}' browser in local environment")
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
