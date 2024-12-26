SETUP INSTRUCTIONS

1.	Install Google Chrome (latest stable version) and ensure it is up to date.
2.	Install Python and the following libraries:
    - selenium
    - pytest
    - webdriver-manager
3.	Use the WebDriver Manager to simplify browser driver setup:
               pip install selenium pytest webdriver-manager
4.	Verify your environment setup by running:
               python -m pytest --version

ADDITIONAL NOTES

1.	The script includes a time.sleep(2) statement to accommodate dynamic table updates. This can be replaced with explicit waits for better reliability.
2.  It assumes Chrome as the primary browser. For other browsers, replace webdriver.Chrome with the appropriate WebDriver setup.
3.  Make sure you have an active internet connection for the script to load the website.
