from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    """
    This function initializes and returns a Chrome WebDriver instance.
    It uses the ChromeDriverManager to automatically download and install
    the correct version of ChromeDriver.
    """
    # Set up ChromeDriver using ChromeDriverManager
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Maximize the browser window
    driver.maximize_window()

    return driver