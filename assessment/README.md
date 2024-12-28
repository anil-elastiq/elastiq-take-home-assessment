# _Selenium Search Functionality Test with Python_

This project demonstrates how to use **Selenium** with **Python** to test the search functionality on a web page that displays a table of data. Specifically, it performs a search for “New York” on the **Selenium Playground Table Sort and Search Demo** and validates both the number of resulting rows and total no. of rows.

---
## _Project Structure_
### _assessment/_
    1. qa_selenium_test.py:      Main test script to perform the search functionality test
    2. driver_setup.py           Initializes and configures the Selenium WebDriver
    3. README.md                 Project description and setup instructions

---
### _Approach_
	1.	Setup WebDriver: The script uses Selenium to open a web browser (Chrome in this case) and navigate to the table page.
	2.	Perform Search: The script interacts with a search input field, clears it, and types the search query (“New York”).
	3.	Wait for Results: The script waits for the rows of the table to appear after the search operation.
	4.	Validate Results: It checks if the number of displayed rows matches the expected result (5 rows in this case). It also validates that the total no. of rows.

---
## _How to Run the Script_

### _Pre-requisites_:

1. **Python**:
   - Ensure [Python 3.7+](https://www.python.org/downloads/) is installed.

2. **PyCharm** (IDE):
   - Download [PyCharm](https://www.jetbrains.com/pycharm/download/) community version and install.

3. **Google Chrome**:
   - Install the latest version of [Google Chrome](https://www.google.com/chrome/).

4. **Dependencies**:
   - Selenium, pytest, and webdriver-manager are required. See the [Dependencies](#dependencies) section below.

5. **Chrome WebDriver**:
    - This script uses **Google Chrome** for automation, so you need the **ChromeDriver** executable to run the tests.

---
## _Dependencies_

You can install the required dependencies using pip by running the following command in your terminal:
* pip install selenium pytest

---
## _Test Output_

The results will be displayed in the terminal. If the test passes, you will see a message indicating test pass. If the test fails, the assertion error message will indicate the discrepancy.