 Selenium Table Search Test

This repository contains a Python script `qa_selenium_test.py` that:
- Navigates to the Selenium Playground Table Search Demo.
- Locates and interacts with the search box to search for "New York".
- Validates that the search results show 5 entries out of 24 total entries.

Program executed on version:
1. Python –  3.13
2. Selenium – 4.27.1
3. Pytest  – 8.3.4
 
Setup Instructions

1. Install Python and Pip:
Ensure Python and pip are installed on your system. 

2. Install Selenium:
 Install the Selenium package using pip:
 pip install selenium

3. Download ChromeDriver:
Download the ChromeDriver that matches the version of your Chrome browser. Place the driver in a known directory.

4. Install Pytest:
Install the pytest framework using pip:
pip install pytest


Instructions to Run the Script

1. Edit the Script:
Update the path to your ChromeDriver in the `qa_selenium_test.py` script:
python driver = webdriver.Chrome('/path/to/chromedriver')

2. Run the test using Pytest:
pytest qa_selenium_test.py

3. Validation: The script will search for "New York" in the table and validate that 5 entries are displayed out of 24 total entries. If the validation passes, the test will succeed; otherwise, it will fail and show the discrepancy.
Additional Notes
Ensure that the Chrome browser is installed on your system.

Make sure the ChromeDriver version matches your installed Chrome browser version.

The script uses a 2-second sleep to wait for the search results to update. Adjust this if necessary based on your network speed.
