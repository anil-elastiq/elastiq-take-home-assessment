"""
QA Selenium Test Script

This script tests the search functionality on the Selenium Playground
Table Search Demo. It validates that searching for 'New York' correctly
filters the table to 5 entries out of a total of 24 entries.
"""

import re

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    """
    Fixture to set up and tear down the browser.
    """
    driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
    driver.maximize_window()
    yield driver
    driver.quit()


def test_validate_search_functionality(browser):
    """
    Test case to validate the search functionality on the Selenium Playground website.
    """
    driver = browser
    wait = WebDriverWait(driver, 10)
    expected_visible = 5
    expected_total = 24
    print("Navigating to the Selenium Playground Table Search Demo...")
    driver.get(
        "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    )

    # Calculate all entries present in the table
    total_entries = calculate_total_entries(driver)
    print(f"Total entries in the table: {total_entries}")

    # Wait for the search box to be present
    print("Waiting for the search box...")
    search_box = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )

    # Enter "New York" in the search box
    print("Entering search text: 'New York'...")
    search_box.send_keys("New York")

    # Wait for filtered rows to appear
    print("Waiting for filtered rows...")
    wait.until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, "//table[@id='example']/tbody/tr")
        ))

    # Validate the number of filtered rows
    filtered_rows = driver.find_elements(
        By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style, 'display: none'))]"
    )
    print(f"Number of filtered rows: {len(filtered_rows)} (expected: 5)")

    # Validating 5 Entries out of 24 enteries
    assert len(filtered_rows) == expected_visible, (
        f"Expected {expected_visible} rows, but found {len(filtered_rows)}."
    )
    assert total_entries == expected_total, (
        f"Expected {expected_total} total entries, but found {total_entries}."
    )
    print(f"Filtered Enteries {filtered_rows} out of Total entries in the table: {total_entries}")

    # Validate the filtered entries text
    validate_filtered_entries_text(driver, expected_visible, expected_total)


def validate_filtered_entries_text(driver, expected_visible, expected_total):
    """
    Function to validate the text showing filtered entries.
    """
    # Wait for the element that displays the entry text
    wait = WebDriverWait(driver, 10)
    entry_text_element = wait.until(EC.visibility_of_element_located((By.ID, "example_info")))

    # Extract the full text
    entry_text = entry_text_element.text
    print(f"Full entry text displayed: '{entry_text}'")

    # Parse the portion "5 entries filtered from 24 total entries"
    match = re.search(r"(\d+) entries .*?filtered from (\d+) total entries", entry_text)
    if not match:
        raise AssertionError(f"Unexpected text format: {entry_text}")

    visible_entries = int(match.group(1))
    total_entries = int(match.group(2))

    print(f"Parsed values: Visible={visible_entries}, Total={total_entries}")

    # Validate visible and total entries
    assert visible_entries == expected_visible, (
        f"Expected {expected_visible} visible entries, but found {visible_entries}"
    )
    assert total_entries == expected_total, (
        f"Expected {expected_total} total entries, but found {total_entries}"
    )

    print("Filtered entries validation passed!")


def calculate_total_entries(driver):
    """
    Function to calculate the total number of entries in the table across all pages.
    """
    print("Calculating total entries in the table...")
    total_entries = 0

    # Wait for the table rows on the current page
    wait = WebDriverWait(driver, 10)

    while True:
        # Wait for the table rows to load on the current page
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@id='example']/tbody/tr"))
        )

        # Count the rows on the current page and add to total entries
        total_entries += len(rows)
        print(f"Rows on current page: {len(rows)}, Total so far: {total_entries}")

        # Check if the "Next" button is enabled
        next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'paginate_button next')]")
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages to navigate.")
            break  # Exit the loop if the "Next" button is disabled

        # Click the "Next" button to go to the next page
        print("Navigating to the next page...")
        next_button.click()

    print(f"Total entries across all pages: {total_entries}")
    return total_entries
