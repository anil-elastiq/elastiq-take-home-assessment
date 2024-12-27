import time

import pytest
from selenium import webdriver

from utilities import XLUtils

@pytest.fixture()
def setup():
    # Set up the WebDriver instance
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture()
def test_Login(setup):
    path = "Elastiq.AI_Assessment/testData/Selenium_Playground_testData.xlsx"
    driver = setup
    driver.maximize_window()

    rows = XLUtils.getRowCount(path, 'HomePage')
    print("Number of rows in excel", rows)
    colums = XLUtils.getColumnCount(path, 'HomePage')
    print("Number of colms in excel", colums)
    url = XLUtils.readData(path, 'HomePage', 2, 1)
    driver.get(url)
