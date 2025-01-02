# QA Selenium Automation with Python

## Objective
Create a Selenium automation script in Python to validate search functionality on the **Selenium Playground** website.

> [!NOTE]
> **Deliverables:**
> 1. A Python script (`qa_selenium_test.py`) that:
>    - Navigates to the [Selenium Playground Table Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo).
>    - Locates and interacts with the search box to search for "New York".
>    - Validates that the search results show **5 entries out of 24 total entries**.
> 2. A brief **README** explaining the approach and how to run the script.
> 3. Any additional setup instructions (e.g., local environment, dependencies, drivers etc).

> [!TIP]
> Use Python's `pytest` framework to structure your test cases.

> [!IMPORTANT]
> - **Environment Setup:** Follow good coding practices and ensure the script is compatible with the latest stable Selenium version.
> - **Browser Compatibility:** Test with at least one major browser (e.g., Chrome, Firefox).

> [!CAUTION]
> - **Assertions:** Ensure all validations use robust assertion statements.
> - **Code Quality:** Follow PEP8 standards for Python code.

**Good luck!**


# QA Selenium Automation with Python

## Objective
# Create a Selenium automation script in Python to validate search functionality on the **Selenium Playground** website.

# [!NOTE]
# **Deliverables:**
# 1. A Python script (`qa_selenium_test.py`) that:
#    - Navigates to the [Selenium Playground Table Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo).
#    - Locates and interacts with the search box to search for "New York".
#    - Validates that the search results show **5 entries out of 24 total entries**.
# 2. A brief **README** explaining the approach and how to run the script.
# 3. Any additional setup instructions (e.g., local environment, dependencies, drivers etc).

# [!TIP]
# Use Python's `pytest` framework to structure your test cases.

# [!IMPORTANT]
# - **Environment Setup:** Follow good coding practices and ensure the script is compatible with the latest stable Selenium version.
# - **Browser Compatibility:** Test with at least one major browser (e.g., Chrome, Firefox).

# [!CAUTION]
# - **Assertions:** Ensure all validations use robust assertion statements.
# - **Code Quality:** Follow PEP8 standards for Python code.

# **Good luck!**


# 1. A Python script (`qa_selenium_test.py`)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

def validate_table_search():
    # Set up Firefox WebDriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()

    try:
        # Open the demo page
        url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
        driver.get(url)

        # Wait for the search box to load
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )

        # Interact with the search box
        search_box.clear()
        search_box.send_keys("New York")

        # Wait for the table rows to update
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#example tbody tr"))
        )

        # Get all visible rows
        rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
        visible_rows = [row for row in rows if row.is_displayed()]

        # Validate filtered row count
        expected_entries = 5
        found_entries = len(visible_rows)
        print(f"Expected Entries: {expected_entries}, Found Entries: {found_entries}")

        # Print visible rows
        print("Visible Rows:")
        for row in visible_rows:
            print(row.text)

        # Validate the total entries text
        total_entries_text = driver.find_element(By.ID, "example_info").text
        print(f"Total Entries Text: {total_entries_text}")
        total_entries_valid = "filtered from 24 total entries" in total_entries_text

        # Assertions
        assert found_entries == expected_entries, f"Expected {expected_entries}, found {found_entries}"
        assert total_entries_valid, f"Expected 'filtered from 24', got '{total_entries_text}'"

        # Pause to view results
        time.sleep(5)

        print("Validation successful.")

    except Exception as e:
        # Handle errors
        print(f"Error: {e}")

    finally:
        # Clean up and close the WebDriver
        driver.quit()

if __name__ == "__main__":
    validate_table_search()



# 2. A brief **README** explaining the approach and how to run the script.

# a) README Overview:-
# This Python script automates the interaction with the Selenium Playground Table Search Demo Website.
# It searches for the term "New York" in the table, validates the number of entries shown (5),
# and confirms that the total number of entries matches the expected count of 24.

# b) How to Run the Script:- 
# Ensure that Python 3.x is installed on your system.
# Install the required Python libraries:
# Selenium: pip install selenium

# c) WebDriver Setup:
# This script uses Firefox and GeckoDriver.
# WebDriver Manager will automatically download the appropriate version of GeckoDriver for you.
# Ensure you have Firefox installed on your system.

# d) Running the Script:
# Download the Python script "qa_selenium_test.py".
# Open a terminal or command prompt.
# Navigate to the directory where "qa_selenium_test.py" is located.

# e) Run the script using the command:
# python qa_selenium_test.py

# f) Expected Output:
# The script will display the number of found entries and print out the visible rows matching "New York".
# The script will validate that exactly 5 entries are displayed out of a total of 24 entries.
# If the validation is successful, it will print "Validation successful."

# g) Dependencies
# Python 3.x
# Selenium (pip install selenium)
# Firefox browser and GeckoDriver

   
   
