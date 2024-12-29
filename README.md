
# README: Selenium Search Functionality Validation

## Overview:
This Python script uses Selenium to automate the validation of the search functionality on the Selenium Playground
Table Search Demo. Specifically, it tests whether searching for "New York" filters the table to show exactly 5 entries
out of a total of 24.

## Prerequisites:
Before running the script, ensure you have the following installed:

1. **Python**: Version 3.7 or higher
2. **Google Chrome**: Latest version
3. **Chromedriver**: Ensure it matches your Chrome version and is in your PATH
4. **Selenium**: Install via pip:
   ```bash
   pip install selenium
   ```
5. **Pytest**: Install via pip:
   ```bash
   pip install pytest
   ```
6. **Pylint**: For linting:
   ```bash
   pip install pylint
   ```

## Files:
- `qa_selenium_test.py`: Main test script.
- `README.md`: This file.

## Script Features:
1. Navigates to the Selenium Playground Table Search Demo.
2. Searches for "New York" and validates filtered results.
3. Validates filtered result is 5 enteries out of 24 total enteries
4. Verifies that the filtered results text matches the expected format
   (e.g., "5 entries filtered from 24 total entries").

## Installation:

1. Clone or download this repository.(https://github.com/saeedsmulla/selenium-python-search-validation)
2. Install the dependencies listed above using pip commands.
3. Ensure `chromedriver` is in your PATH or specify its location in the script.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the test script using `pytest`:
   ```bash
   pytest qa_selenium_test.py
   ```
3. To generate a report, use the following command:
   ```bash
   pytest --html=report.html --self-contained-html
   ```

## Code Quality

1. Run pylint to check for PEP8 compliance:
   ```bash
   pylint qa_selenium_test.py
   ```

## Key Assertions
- **Number of Filtered Rows**: Ensures that searching for "New York" results in exactly 5 rows.
- **Total Entries**: Verifies that the total number of table entries is 24.
- **Filtered Text Format**: Matches the text "5 entries filtered from 24 total entries" to confirm expected behavior.

## Troubleshooting

1. **Chromedriver Version Mismatch**:
   - Ensure the chromedriver version matches your installed Chrome browser version.
   - Download the appropriate version from
     [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).

2. **Element Not Found Errors**:
   - Check if the website layout or element locators have changed.
   - Update the script to reflect any changes in the target website.

3. **Timeout Errors**:
   - Increase the WebDriverWait timeout in the script if elements are slow to load.


