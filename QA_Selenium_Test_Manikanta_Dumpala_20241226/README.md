# QA Selenium Test - 'qa_selenium_test.py'

## Objective
This script has been developed to perform automated testing using Selenium WebDriver and pytest. It includes a basic example of testing a web page for sorting and searching functionality.

## Prerequisites
- Install Python 3.x (>= 3.11.3 is preferred).
- Ensure Google Chrome is installed.
- Install Google ChromeDriver that matches the browser version.

## Script Explanation
### Imports
Install the required Python libraries:
- 'selenium.webdriver': Provides tools to control the browser programmatically.
- 'selenium.webdriver.common.by.By': Used to locate elements on a web page.
- 'pytest': Framework for writing and running tests.

### Setup Fixture
- **Creates a Chrome WebDriver instance.**
- **Opens the target URL.**
- **Maximizes the browser window.**
- **Yields the WebDriver object for reuse in test cases.** The WebDriver is automatically closed after the test module finishes.

### Test Case: "test_sort_table"
#### Steps:
1. Uses the search box to filter the table for the term "New York".
2. Locates and extracts the informational text about the filtered result.
3. Verifies that the text returned matches the expected result.

## Expected Outcome
The assertion checks if the text displayed matches: "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

## How to Run the Test
1. Ensure that all prerequisites are installed.
2. Save the script as "qa_selenium_test.py".
3. Use the following command to run the test:
    
   ```sh
   pytest qa_selenium_test.py
