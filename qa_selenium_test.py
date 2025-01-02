import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Configuration
URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
SEARCH_TERM = "New York"
EXPECTED_TOTAL_ENTRIES = 24
EXPECTED_VISIBLE_ENTRIES = 5

@pytest.fixture(scope="module")
def driver():
    service = Service("c:/driver/chromedriver-win32/chromedriver.exe")  # Update with the actual path to chromedriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_search_functionality(driver):
    driver.get(URL)

    # Locate the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-controls='example']"))
    )

    # Interact with the search box
    search_box.clear()
    search_box.send_keys(SEARCH_TERM)

    # Wait for results to update
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.c, "#example_info"), f"{EXPECTED_VISIBLE_ENTRIES} of {EXPECTED_TOTAL_ENTRIES}")
    )

    # Validate the entries count
    entries_info = driver.find_element(By.CSS_SELECTOR, "#example_info")  # Update with actual CSS selector for the entries info element
    assert f"{EXPECTED_VISIBLE_ENTRIES} of {EXPECTED_TOTAL_ENTRIES}" in entries_info.text, (
        f"Expected '{EXPECTED_VISIBLE_ENTRIES} of {EXPECTED_TOTAL_ENTRIES}', but got '{entries_info.text}'"
    )

# README Content
README_CONTENT = """
# Selenium Playground Table Search Test

This script validates the search functionality on the Selenium Playground Table Sort Search Demo page.

## Approach

1. Navigate to the Table Sort Search Demo page.
2. Locate and interact with the search box to search for "New York".
3. Validate that the search results show 5 visible entries out of 24 total entries.

## Prerequisites

- Python 3.7+
- Google Chrome
- ChromeDriver compatible with your browser version
- Selenium package (latest stable version)
- pytest for running the test cases

## Setup Instructions

1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install selenium pytest
   ```
3. Ensure you have ChromeDriver or GeckoDriver installed and the path updated in the script.
4. Update the `chromedriver` path in the script if necessary.

## Running the Test

To execute the test case, run:
```bash
pytest qa_selenium_test.py
```

## Browser Compatibility

This script is tested with Google Chrome. Ensure you have the latest version of Chrome and ChromeDriver.

## Code Quality

The script follows PEP8 standards and uses robust assertions for validation.
"""

if __name__ == "__main__":
    with open("README.md", "w") as readme_file:
        readme_file.write(README_CONTENT)
