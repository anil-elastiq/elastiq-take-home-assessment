## Objective
The goal of this project is to create a selenium automation script to validate the search functionality on the Selenium Playground Table Searh Demo page. The script will ensure that the search functionality correctly filters results based on the search term "New York" and displays the expected number of results.
## Prerequisites
Install Python 3.x
Install Google ChromeDriver that matches the version of browser
Check Google Chrome is installed
## Imports
selenium import webdriver:
This import gives you access to the webdriver class, which you will use to control the browser.

selenium.webdriver.common.by import By:
The By class allows you to locate elements on a web page using different strategies, such as By.XPATH, By.CSS_SELECTOR, By.ID, etc.

selenium.webdriver.chrome.service import Service:
This class is used to manage the ChromeDriver service that runs in the background to control the Chrome browser. It's especially useful when using webdriver_manager.

selenium.webdriver.support.ui import WebDriverWait:
This is used to wait for elements to appear or conditions to be met before performing any actions on the web page.

selenium.webdriver.support import expected_conditions as EC:
This provides common conditions for waiting, such as waiting for elements to be present, clickable, etc. It helps in synchronizing the script with the web page.

webdriver_manager.chrome import ChromeDriverManager:
This import is for webdriver_manager, which automatically downloads and manages the appropriate version of ChromeDriver for your system and browser version.

## Dependencies
1.ChromeDriver
2.pytest
3.Selenium


