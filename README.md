This repository contains a Python script that uses Selenium and Pytest to test the functionality of a search on the Selenium Playground website. The test script validates the total number of rows in the table and ensures that filtering the table for a specific keyword produces the expected results.

1. **Features**

Web Automation: Uses Selenium WebDriver to interact with a web table.
Pytest Framework: Implements the test using Python's pytest framework.
Dynamic Interaction: Handles pagination and filtering dynamically.
Assertions: Includes assertions to validate the table's data.

2. **Requirements**

To run this script, ensure you have the following installed:
Python 3.7 or higher
Google Chrome browser
ChromeDriver (matching the version of Chrome installed)
Required Python packages:
selenium
pytest

3. **Usage**

Run the test using Pytest:
pytest -v test_script.py

The test performs the following steps:

--> Opens the table sort and search demo.
--> Iterates through all pages of the table to count the total number of rows.
--> Filters the table using the keyword New York.
-->Validates:Total number of rows is 24.
             Filtering returns exactly 5 rows

**Script Explanation**

Fixture: driver

The driver fixture initializes a Selenium WebDriver instance, navigates to the test URL, and ensures the browser is properly closed after the test.

Test Function: test_table_data

Pagination Handling:
The script iterates through all pages of the table to count rows dynamically.

Filtering:
Filters the table using the input box and validates the filtered results.

Assertions:
Ensures the expected number of rows are present both before and after filtering.

*Example Output*

===================================================== test session starts =====================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir:

searchFunc.py
                                                                                                          [100%]

====================================================== 1 passed in 7.63s ======================================================
