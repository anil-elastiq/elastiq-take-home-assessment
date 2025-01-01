README
Approach:
 * Setup:
   * Install necessary libraries: pip install pytest selenium
   * Download and configure the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
 * Test Case:
   * Navigate to the Selenium Playground Table Search Demo.
   * Locate and interact with the search box to enter "New York".
   * Assert that the search results display the correct message: "Showing 5 entries out of 24 total entries".
How to Run:
 * Save the script as qa_selenium_test.py.
 * Open a terminal or command prompt.
 * Navigate to the directory where you saved the script.
 * Run the following command: pytest qa_selenium_test.py
3. Additional Setup Instructions
 * Local Environment:
   * Python 3.x or higher
 * Dependencies:
   * pytest
   * selenium
 * Drivers:
   * Download the appropriate WebDriver (e.g., ChromeDriver) from the official website and place it in your system's PATH or in the same directory as your script.
Explanation:
 * pytest: The pytest framework is used for structuring the test case and running the tests.
 * WebDriver: The webdriver module from the selenium library is used to control the browser.
 * Locators: The By class and XPath expressions are used to locate elements on the web page.
 * Wait Conditions: The WebDriverWait class and expected_conditions are used to wait for elements to load before interacting with them.
 * Assertions: The assert statement is used to verify that the search results match the expected outcome.
