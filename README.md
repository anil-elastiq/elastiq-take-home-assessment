# Elastiq
QA Selenium Automation with Python

# Selenium Automation Script for Search Validation

This project automates testing of the search functionality on the Selenium Playground Table Search Demo.

## Prerequisites

1. Install Python 3.7 or later.
2. Install pip (Python package manager).

## Setup Instructions

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Ensure you have either Google Chrome or Mozilla Firefox installed.
## Dependencies
selenium: For browser automation.
pytest: For structuring and running test cases.
webdriver-manager: For managing browser drivers.

Install these dependencies using:
bash
pip install selenium pytest webdriver-manager

## How to Run the Tests
Run the script using pytest:

bash
pytest qa_selenium_test.py --browser chrome
Replace chrome with firefox to test with Mozilla Firefox.

## Test Case Details
Test Scenario: Validate that searching "New York" on the Selenium Playground Table Search Demo returns exactly 5 results.
Assertions:
The total number of visible rows should equal 5 after the search.
## Code Quality
This script follows PEP8 standards for readability and maintainability.

## Notes
The script uses webdriver-manager to automatically download and manage browser drivers.
Tested with Selenium version 4.x.
yaml


---

selenium pytest webdriver-manager

vbnet


